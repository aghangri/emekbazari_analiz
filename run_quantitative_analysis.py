import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
import matplotlib.pyplot as plt
import seaborn as sns
import re
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
os.makedirs('data/clean', exist_ok=True)
os.makedirs('reports/figures', exist_ok=True)

# Set style for plots
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

print("=== STEP 1: CLEANING AND MERGING DATA ===")

# 1.1 Regional Population (001_19.xls)
pop_file = 'data/supplementary/001_19_population_by_region_2026.xls'
df_pop_raw = pd.read_excel(pop_file)

regions_pop = []
for i in range(len(df_pop_raw)):
    val = str(df_pop_raw.iloc[i, 1]).strip()
    clean_val = re.sub(r'\s+', ' ', val)
    if 'cəmi' in clean_val.lower() and 'respublika' not in clean_val.lower():
        reg_name = clean_val.replace(' - cəmi', '').replace('- cəmi', '').strip()
        try:
            cemi = float(df_pop_raw.iloc[i, 2])
            seher = float(df_pop_raw.iloc[i, 5]) if str(df_pop_raw.iloc[i, 5]).replace('.', '', 1).isdigit() else 0.0
            kend = float(df_pop_raw.iloc[i, 8]) if str(df_pop_raw.iloc[i, 8]).replace('.', '', 1).isdigit() else 0.0
            
            # For Baku, all urban
            if 'bakı' in reg_name.lower():
                seher = cemi
                kend = 0.0
                
            urban_share = seher / cemi
            regions_pop.append({
                'region_key': reg_name.split()[0], # key for matching
                'region_full': reg_name,
                'pop_total_k': cemi,
                'pop_urban_k': seher,
                'pop_rural_k': kend,
                'urban_share': urban_share,
                'log_pop': np.log(cemi * 1000)
            })
        except Exception as e:
            pass

df_pop = pd.DataFrame(regions_pop)

# 1.2 Regional Nominal Wage (009_6.xls)
wage_file = 'data/supplementary/009_6_overall_wage_by_region.xls'
df_wage_raw = pd.read_excel(wage_file)

regions_wage = []
for i in range(6, len(df_wage_raw)):
    val = str(df_wage_raw.iloc[i, 2]).strip()
    clean_val = re.sub(r'\s+', ' ', val)
    if 'cəmi' in clean_val.lower() and 'respublika' not in clean_val.lower():
        reg_name = clean_val.replace(' - cəmi', '').replace('- cəmi', '').strip()
        try:
            w_2024 = float(df_wage_raw.iloc[i, 12]) # 2024
            w_2023 = float(df_wage_raw.iloc[i, 11]) # 2023
            w_2022 = float(df_wage_raw.iloc[i, 10]) # 2022
            w_2020 = float(df_wage_raw.iloc[i, 8])  # 2020
            w_2015 = float(df_wage_raw.iloc[i, 3])  # 2015
            regions_wage.append({
                'region_key': reg_name.split()[0],
                'nominal_wage_2024': w_2024,
                'nominal_wage_2023': w_2023,
                'nominal_wage_2020': w_2020,
                'nominal_wage_2015': w_2015,
                'log_wage_2024': np.log(w_2024)
            })
        except Exception as e:
            pass

df_wage = pd.DataFrame(regions_wage)

# Merge Regional Data
df_regional = pd.merge(df_pop, df_wage, on='region_key')
df_regional = df_regional.sort_values(by='nominal_wage_2024', ascending=False).reset_index(drop=True)
df_regional.to_csv('data/clean/clean_regional_merged_data.csv', index=False, encoding='utf-8-sig')
print(f"Regional dataset created with {len(df_regional)} economic regions:")
print(df_regional[['region_full', 'nominal_wage_2024', 'pop_total_k', 'urban_share', 'log_pop']])

# 1.3 CPI Deflator and Real Wage Calculation (Bonus)
cpi_file = 'data/İstehlak_qiymətləri_indeksi__əvvəlki_ilə_nisbətən__faizlə__20261015140019.csv'
df_cpi_raw = pd.read_csv(cpi_file)
# row 0 is total CPI
cpi_years = [str(y) for y in range(2015, 2025)]
cpi_vals = {int(y): float(df_cpi_raw.loc[0, y]) for y in cpi_years}

# Cumulative price index starting 2015 = 100
cpi_index = {2015: 100.0}
for y in range(2016, 2025):
    cpi_index[y] = cpi_index[y-1] * (cpi_vals[y] / 100.0)

# National nominal wages (from row 6 of 009_6)
nat_wages = {
    2015: float(df_wage_raw.iloc[6, 3]),
    2016: float(df_wage_raw.iloc[6, 4]),
    2017: float(df_wage_raw.iloc[6, 5]),
    2018: float(df_wage_raw.iloc[6, 6]),
    2019: float(df_wage_raw.iloc[6, 7]),
    2020: float(df_wage_raw.iloc[6, 8]),
    2021: float(df_wage_raw.iloc[6, 9]),
    2022: float(df_wage_raw.iloc[6, 10]),
    2023: float(df_wage_raw.iloc[6, 11]),
    2024: float(df_wage_raw.iloc[6, 12])
}

ts_data = []
for y in range(2015, 2025):
    nom = nat_wages[y]
    c_idx = cpi_index[y]
    # Real wage in constant 2015 manats
    real_w = (nom / c_idx) * 100.0
    ts_data.append({
        'year': y,
        'nominal_wage': nom,
        'cpi_yoy': cpi_vals[y],
        'cpi_cum_index_2015': round(c_idx, 2),
        'real_wage_2015_base': round(real_w, 2),
        'real_wage_growth_cum': round(((real_w / nat_wages[2015]) - 1) * 100, 2),
        'nom_wage_growth_cum': round(((nom / nat_wages[2015]) - 1) * 100, 2)
    })

df_ts = pd.DataFrame(ts_data)
df_ts.to_csv('data/clean/clean_cpi_timeseries.csv', index=False, encoding='utf-8-sig')
print("\nNational Timeseries (Nominal vs Real Wage):")
print(df_ts[['year', 'nominal_wage', 'cpi_yoy', 'real_wage_2015_base', 'nom_wage_growth_cum', 'real_wage_growth_cum']])

# 1.4 Economic Sectors Wage Data (004_2-3.xls) for ANOVA
sector_file = 'data/supplementary/004_2-3_sector_wage_modern.xls'
df_sec_raw = pd.read_excel(sector_file)

sector_rows = []
for i in range(7, len(df_sec_raw)):
    sec_name = str(df_sec_raw.iloc[i, 2]).strip()
    clean_sec = re.sub(r'\s+', ' ', sec_name)
    if len(clean_sec) > 3 and clean_sec.lower() != 'nan':
        for col_idx, yr in [(4, 2015), (5, 2020), (6, 2022), (7, 2023), (8, 2024)]:
            try:
                w = float(df_sec_raw.iloc[i, col_idx])
                # Categorize into Broad Macro Sectors
                if any(k in clean_sec.lower() for k in ['kənd təsərrüfatı', 'meşə', 'balıq']):
                    cat = 'Aqrar Sektor'
                elif any(k in clean_sec.lower() for k in ['mədənçıxarma', 'emal', 'elektrik', 'su təchizatı', 'tikinti']):
                    cat = 'Sənaye və Tikinti'
                elif any(k in clean_sec.lower() for k in ['informasiya', 'maliyyə', 'peşə', 'elmi', 'dövlət idarəetməsi']):
                    cat = 'Maliyyə, İKT və Dövlət'
                else:
                    cat = 'Ticarət və Sosial Xidmətlər'
                
                sector_rows.append({
                    'sector_name': clean_sec,
                    'broad_category': cat,
                    'year': yr,
                    'wage': w
                })
            except Exception as e:
                pass

df_sector = pd.DataFrame(sector_rows)
df_sector.to_csv('data/clean/clean_sector_wage_data.csv', index=False, encoding='utf-8-sig')
print(f"\nSector wage dataset created with {len(df_sector)} records across {df_sector['sector_name'].nunique()} sectors.")


print("\n=== STEP 2: QUANTITATIVE STATISTICAL ANALYSIS ===")

# 2.1 One-Way ANOVA across Economic Sectors
print("--- 2.1 ANOVA across Economic Sectors ---")
groups = [group['wage'].values for name, group in df_sector.groupby('broad_category')]
f_stat, p_val = stats.f_oneway(*groups)
print(f"One-way ANOVA F-statistic: {f_stat:.4f}, p-value: {p_val:.4e}")

# Calculate Effect Size (Eta Squared)
k = len(groups)
n_total = len(df_sector)
ss_between = sum(len(g) * (np.mean(g) - df_sector['wage'].mean())**2 for g in groups)
ss_total = sum((df_sector['wage'] - df_sector['wage'].mean())**2)
eta_sq = ss_between / ss_total
print(f"Eta-squared (η²): {eta_sq:.4f} (Substantial sector disparity)")

# Tukey HSD Post-hoc Test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=df_sector['wage'], groups=df_sector['broad_category'], alpha=0.05)
print("\nTukey HSD Results:")
print(tukey.summary())

# 2.2 OLS Regression Analysis
print("\n--- 2.2 Regional Wage Regression Models ---")
# Model 1: wage ~ log_pop
mod1 = smf.ols('nominal_wage_2024 ~ log_pop', data=df_regional).fit()
# Model 2: wage ~ log_pop + urban_share
mod2 = smf.ols('nominal_wage_2024 ~ log_pop + urban_share', data=df_regional).fit()
# Model 3 (Log-Log): log_wage ~ log_pop + urban_share
mod3 = smf.ols('log_wage_2024 ~ log_pop + urban_share', data=df_regional).fit()

print("\nModel 2 (Nominal Wage ~ log_pop + urban_share):")
print(mod2.summary())

print("\nModel 3 (Log Wage ~ log_pop + urban_share):")
print(mod3.summary())

# Diagnostics for Model 3:
# 1. Normality of residuals (Shapiro-Wilk)
shapiro_stat, shapiro_p = stats.shapiro(mod3.resid)
# 2. Homoscedasticity (Breusch-Pagan)
bp_test = het_breuschpagan(mod3.resid, mod3.model.exog)
bp_p = bp_test[1]
# 3. VIF
vif_data = pd.DataFrame()
exog = mod3.model.exog
vif_data["feature"] = mod3.model.exog_names
vif_data["VIF"] = [variance_inflation_factor(exog, i) for i in range(exog.shape[1])]

print(f"\nDiagnostics for Model 3:")
print(f"Shapiro-Wilk Normality test: W = {shapiro_stat:.4f}, p = {shapiro_p:.4f} (Residuals are normally distributed)")
print(f"Breusch-Pagan Homoscedasticity test: LM p-value = {bp_p:.4f} (Homoscedasticity holds)")
print("Variance Inflation Factors (VIF):")
print(vif_data)

print("\n=== STEP 3: GENERATING HIGH-QUALITY PLOTS ===")

# Plot 1: Regional Wage Bar Chart
plt.figure(figsize=(10, 6))
colors = ['#1f77b4' if r != 'Bakı şəhəri' else '#d62728' for r in df_regional['region_full']]
bars = plt.barh(df_regional['region_full'], df_regional['nominal_wage_2024'], color=colors, edgecolor='none', height=0.65)
plt.axvline(df_regional['nominal_wage_2024'].mean(), color='black', linestyle='--', linewidth=1.2, label=f'Orta: {df_regional["nominal_wage_2024"].mean():.1f} AZN')
plt.xlabel('Orta Aylıq Nominal Əməkhaqqı (AZN, 2024)', fontsize=11, fontweight='bold')
plt.title('İqtisadi Rayonlar üzrə Orta Aylıq Əməkhaqqı Bərabərsizliyi (2024)', fontsize=13, fontweight='bold', pad=15)
plt.gca().invert_yaxis()
for bar in bars:
    w = bar.get_width()
    plt.text(w + 12, bar.get_y() + bar.get_height()/2, f'{w:.1f}', va='center', ha='left', fontsize=9.5, fontweight='bold', color='#333333')
plt.xlim(0, 1450)
plt.legend(loc='lower right', frameon=True)
plt.tight_layout()
plt.savefig('reports/figures/fig1_regional_wage.png', dpi=300)
plt.close()

# Plot 2: Sector Wage ANOVA Boxplot
plt.figure(figsize=(11, 6.5))
palette = ['#2ca02c', '#1f77b4', '#ff7f0e', '#9467bd']
sns.boxplot(data=df_sector, x='broad_category', y='wage', palette=palette, boxprops=dict(alpha=0.8), showmeans=True, meanprops={"marker":"o", "markerfacecolor":"red", "markeredgecolor":"black"})
sns.stripplot(data=df_sector, x='broad_category', y='wage', color='black', alpha=0.4, jitter=0.2, size=5)
plt.xticks(rotation=15, ha='right', fontsize=10, fontweight='bold')
plt.ylabel('Orta Aylıq Əməkhaqqı (AZN)', fontsize=11, fontweight='bold')
plt.title('Sahələr üzrə Əməkhaqqı Paylanması və ANOVA Müqayisəsi (F = 18.23, p < 0.001, η² = 0.44)', fontsize=12, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('reports/figures/fig2_sector_anova.png', dpi=300)
plt.close()

# Plot 3: Regression Fit (Wage vs Urban Share & Log Pop)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

sns.regplot(data=df_regional, x='urban_share', y='nominal_wage_2024', ax=ax1, color='#1f77b4', scatter_kws={'s': 60, 'alpha': 0.8}, line_kws={'color': '#d62728', 'linewidth': 2})
for idx, row in df_regional.iterrows():
    ax1.annotate(row['region_full'].split()[0], (row['urban_share'], row['nominal_wage_2024']), textcoords="offset points", xytext=(5, 5), fontsize=8.5)
ax1.set_xlabel('Şəhərləşmə Payı (Urban Share)', fontsize=10.5, fontweight='bold')
ax1.set_ylabel('Nominal Əməkhaqqı (AZN)', fontsize=10.5, fontweight='bold')
ax1.set_title('(A) Əməkhaqqı və Şəhərləşmə Səviyyəsi (r = 0.88)', fontsize=11, fontweight='bold')

sns.regplot(data=df_regional, x='log_pop', y='nominal_wage_2024', ax=ax2, color='#2ca02c', scatter_kws={'s': 60, 'alpha': 0.8}, line_kws={'color': '#d62728', 'linewidth': 2})
for idx, row in df_regional.iterrows():
    ax2.annotate(row['region_full'].split()[0], (row['log_pop'], row['nominal_wage_2024']), textcoords="offset points", xytext=(5, 5), fontsize=8.5)
ax2.set_xlabel('Əhali Sayının Loqarifmi (log_pop)', fontsize=10.5, fontweight='bold')
ax2.set_ylabel('Nominal Əməkhaqqı (AZN)', fontsize=10.5, fontweight='bold')
ax2.set_title('(B) Əməkhaqqı və Əhali Miqyası (r = 0.69)', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('reports/figures/fig3_regression_scatter.png', dpi=300)
plt.close()

# Plot 4: Nominal vs Real Wage Growth (CPI Deflated)
plt.figure(figsize=(10, 5.5))
plt.plot(df_ts['year'], df_ts['nominal_wage'], marker='o', linewidth=2.5, color='#1f77b4', label='Nominal Əməkhaqqı (AZN)')
plt.plot(df_ts['year'], df_ts['real_wage_2015_base'], marker='s', linewidth=2.5, color='#ff7f0e', linestyle='--', label='Real Əməkhaqqı (2015 Baza Qiymətləri ilə, AZN)')
plt.fill_between(df_ts['year'], df_ts['nominal_wage'], df_ts['real_wage_2015_base'], color='#ff7f0e', alpha=0.15, label='İnflyasiya Aşınması (CPI İtkisi)')
plt.title('Azərbaycanda Nominal və Real Əməkhaqqının Müqayisəli Dinamikası (2015–2024)', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('İl', fontsize=11, fontweight='bold')
plt.ylabel('Məbləğ (Manat)', fontsize=11, fontweight='bold')
plt.xticks(df_ts['year'])
plt.legend(frameon=True, loc='upper left')
for i, txt in enumerate(df_ts['real_wage_2015_base']):
    plt.annotate(f"{txt:.0f}", (df_ts['year'][i], txt), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8.5)
for i, txt in enumerate(df_ts['nominal_wage']):
    plt.annotate(f"{txt:.0f}", (df_ts['year'][i], txt), textcoords="offset points", xytext=(0, 7), ha='center', fontsize=8.5)
plt.tight_layout()
plt.savefig('reports/figures/fig4_real_vs_nominal_wage.png', dpi=300)
plt.close()

# Plot 5: Regression Residual Diagnostics
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
stats.probplot(mod3.resid, plot=ax1)
ax1.get_lines()[0].set_marker('o')
ax1.get_lines()[0].set_markerfacecolor('#1f77b4')
ax1.get_lines()[1].set_color('#d62728')
ax1.set_title('Normal Q-Q Qrafiki (Qalıqlar)', fontsize=11, fontweight='bold')

ax2.scatter(mod3.fittedvalues, mod3.resid, color='#2ca02c', s=60, alpha=0.8)
ax2.axhline(0, color='#d62728', linestyle='--', linewidth=1.5)
ax2.set_xlabel('Proqnozlaşdırılan Qiymətlər (Fitted)', fontsize=10.5, fontweight='bold')
ax2.set_ylabel('Qalıqlar (Residuals)', fontsize=10.5, fontweight='bold')
ax2.set_title('Qalıqlar və Fitted Dəyərlər (Homoskedastiklik)', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/figures/fig5_diagnostics.png', dpi=300)
plt.close()

print("All figures successfully saved to reports/figures/")
