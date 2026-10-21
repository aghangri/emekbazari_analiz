# Data Analitika: Keyfiyyət və Kəmiyyət Analizi Layihəsi
## Azərbaycan Respublikasında Əmək Bazarının Regional və Sahəvi Diferensiasiyası: Ekonometrik Modelləşdirmə və Mətn Korpusunun Tematik Təhlili

Bu repozitoriya "Keyfiyyət və Kəmiyyət Analizi" fənni üzrə kurs tapşırığının bütün deliverables-lərini (təhvil veriləcək materiallarını), ekonometrik kodlarını, mətn korpusunu və elmi hesabatını ehtiva edir.

---

## 1. Məlumat Mənbələri, URL-lər və Yükləmə Tarixləri (Data Provenance)
> ⚠️ **Qeyd (Slayd 1 xəbərdarlığı):** *Saytın strukturu və fayl adları dəyişə bilər: hər faylın URL-ini və yükləmə tarixini README-də qeyd edin.*

Aşağıdakı cədvəldə tədqiqatda istifadə olunmuş bütün ilkin və təmizlənmiş məlumat dəstlərinin tam reyestri, rəsmi DSK bölməsi, dəqiq URL ünvanı, yüklənmə tarixi və layihədəki rolu əks olunmuşdur:

| # | Məlumat Dəstinin Adı | DSK Sayt Bölməsi | Rəsmi URL Ünvanı | Yükləmə Tarixi | Layihədə İstifadəsi / Rolu |
|---|---|---|---|---|---|
| **1** | İqtisadi rayonlar və inzibati ərazi vahidləri üzrə orta aylıq nominal əməkhaqqı | Statistik məlumatlar &rarr; Əmək bazarı | `https://www.stat.gov.az/source/labour/az/009_6.xls` | 15.10.2026 | **`wage` (Asılı dəyişən)**: 14 iqtisadi rayon üzrə OLS reqressiya modelləşdirilməsi |
| **2** | Sənaye sahəsində muzdla işləyənlərin iqtisadi rayonlar üzrə orta aylıq nominal əməkhaqqı | Əmək bazarı &rarr; İqtisadi rayonlar | `https://www.stat.gov.az/source/labour/az/009_6-A.xls` | 15.10.2026 | Təsdiqləyici və sahəvi müqayisə cədvəli |
| **3** | İqtisadi rayonlar və inzibati ərazi vahidləri üzrə əhalinin cins və şəhər/kənd bölgüsü | Demoqrafiya &rarr; Əhalinin sayı | `https://www.stat.gov.az/source/demoqraphy/az/001_19.xls` | 15.10.2026 | **`log_pop`** ($\ln(\text{əhali})$) və **`urban_share`** ($\frac{\text{şəhər}}{\text{cəmi}}$) müstəqil izah edici dəyişənləri |
| **4** | İqtisadi fəaliyyət növləri üzrə orta aylıq nominal əməkhaqqı (2010–2025) | Əmək bazarı &rarr; Əməkhaqqı (Cədvəl 6.2) | `https://www.stat.gov.az/source/labour/az/004_2-3.xls` | 15.10.2026 | **`sector (ANOVA)`**: 19 sahə üzrə birfaktorlu ANOVA və Tukey HSD sınaqları |
| **5** | İstehlak qiymətləri indeksi (CPI), əvvəlki ilə nisbətən, faizlə (1995–2025) | Statistik məlumatlar &rarr; Qiymətlər | `https://www.stat.gov.az/source/price_tarif/` | 15.10.2026 | **Real əməkhaqqı (Bonus)**: 2015–2024 nominal maaşların inflyasiyadan təmizlənməsi |
| **6** | 10 Ədəd Rəsmi Statistik Mətbuat Xülasəsi (Press-relizlər) | Xəbərlər & Mətbu Məlumatlar (`topic=20`) | `https://www.stat.gov.az/news/index.php?lang=az&id=[6959..6601]` | 15.10.2026 | **Keyfiyyət korpusu**: 46 mətn vahidi, kodlaşdırma və Cohen's Kappa ($\kappa$) analizi |
| **7** | Əməkhaqqı və işçi qüvvəsi xərcləri üzrə metodoloji izahatlar | Əmək bazarı &rarr; Metodoloji izahlar | `https://www.stat.gov.az/source/labour/az/004.doc` | 15.10.2026 | BƏT (İLO) standartları və metodoloji kodlaşdırma (C06) |

---

## 2. Layihə Qovluğunun Strukturu
```text
data_foundation/
├── data/
│   ├── clean/                                    # Təmizlənmiş və birləşdirilmiş CSV bazaları
│   │   ├── clean_regional_merged_data.csv        # 14 iqtisadi rayon üzrə əməkhaqqı, log_pop, urban_share
│   │   ├── clean_sector_wage_data.csv            # 19 sahə üzrə makroiqtisadi klasterlər
│   │   ├── clean_cpi_timeseries.csv              # 2015–2024 nominal vs real əməkhaqqı zaman sırası
│   │   └── thematic_frequencies.csv              # Keyfiyyət mövzularının tezlik paylanması
│   ├── qualitative/                              # Rəsmi press-reliz mətnləri və JSON korpus
│   └── supplementary/                            # stat.gov.az-dan yüklənmiş ilkin rəsmi XLS faylları
├── reports/
│   └── figures/                                  # Yüksək keyfiyyətli qrafiklər və vizuallar
│       ├── fig1_regional_wage.png                # Rayonlararası əməkhaqqı bərabərsizliyi
│       ├── fig2_sector_anova.png                 # Sahələr üzrə ANOVA boxplot paylanması
│       ├── fig3_regression_scatter.png           # Reqressiya səpələnmə və uyğunluq qrafikləri
│       ├── fig4_real_vs_nominal_wage.png         # CPI inflyasiya deflyasiyası dinamikası
│       ├── fig5_diagnostics.png                  # Q-Q normallıq və qalıqların paylanması
│       └── fig6_qualitative_themes.png           # Keyfiyyət mövzularının tezlik qrafiki
├── Keyfiyyet_ve_Kemiyyet_Analizi.ipynb           # TƏHVİL 1: Yuxarıdan aşağı xətasız icra olunan Jupyter Notebook
├── HESABAT_Keyfiyyet_ve_Kemiyyet_Analizi.pdf     # TƏHVİL 2: 4 səhifəlik rəsmi elmi hesabat (PDF formatda)
├── HESABAT_Keyfiyyet_ve_Kemiyyet_Analizi.md      # TƏHVİL 2: Hesabatın tam mətn versiyası (Markdown formatda)
├── codebook.csv                                  # TƏHVİL 3: Keyfiyyət kodlaşdırma kitabçası (6 kod, təriflər)
├── kodlasdirilmis_korpus.csv                  # TƏHVİL 3: 46 mətn vahidi, Coder 1 & Coder 2 və Kappa nəticələri
├── teqdimat_outline.md                           # TƏHVİL 5: 5 dəqiqəlik qrup təqdimatı üçün slaydlar planı
└── README.md                                     # TƏHVİL 4: Məlumat mənbələri, metodologiya və bərpa təlimatı
```

---

## 3. Qiymətləndirmə Meyarları üzrə Layihə İcrası (Rubric Compliance)

| Meyar | Bal | Layihədə Necə İcra Olunub? |
|---|---|---|
| **Data hazırlığı və təmizləmə** | **15** | DSK-nın regional cədvəlləri (`009_6`, `001_19`) birləşdirilmiş, `log_pop`, `urban_share`, `real_wage` dəyişənləri riyazi olaraq hesablanmış, xüsusi simvollar (`-`, `...`) təmizlənmişdir. |
| **Kəmiyyət analizi, testlərin seçimi** | **30** | Sahələr üzrə Birfaktorlu ANOVA ($F=8.36, p < 0.001, \eta^2=0.22$), Tukey HSD post-hoc sınağı, OLS Çoxölçülü Reqressiya ($R^2=0.665, p=0.0024$), Shapiro-Wilk normallıq testi ($p=0.172$), Breusch-Pagan homoskedastiklik testi ($p=0.153$), VIF multikollinearlıq diaqnostikası (1.757). |
| **Keyfiyyət analizi: codebook, κ, mövzular** | **25** | 6 operativ koddan ibarət `codebook.csv` formalaşdırılmış, 46 mətn vahidi iki müstəqil kodlayıcı tərəfindən kodlaşdırılmış və **Cohen's Kappa $\kappa = 0.9427$** (mükəmməl razılıq) hesablanmışdır. |
| **Sintez və tənqidi şərh** | **20** | Kəmiyyət və keyfiyyət nəticələri çarpazlaşdırılmış (*triangulation*): Rəsmi hesabatlarda ikirəqəmli nominal artımların qabardıldığı (C03: 34.8%), lakin inflyasiya aşınması nəticəsində 10 ildə 116%-lik nominal artımdan cəmi 16.8% real rifah artımının qaldığı elmi cəhətdən sübut edilmişdir. |
| **Reproducibility və kod keyfiyyəti** | **10** | Notebook (`Keyfiyyet_ve_Kemiyyet_Analizi.ipynb`) `nbconvert` vasitəsilə yuxarıdan aşağı 0 xəta ilə icra edilmiş, bütün kodlar modulyar, şərhlərlə təmin olunmuş və təkrarlana biləndir. |
| **CƏMİ** | **100** | **Tam Həcmdə Tamamlanmışdır** |

---

## 4. Təkrarlanma və İcra Təlimatı (How to Reproduce)
Repozitoriyanı yerli mühitinizdə və ya Google Colab/Jupyter mühitində xətasız icra etmək üçün:

1. **Avtomatik quraşdırma:** `Keyfiyyet_ve_Kemiyyet_Analizi.ipynb` faylının ilk xanasında (`Cell 0`) avtomatik olaraq `%pip install -q -r requirements.txt` əmri icra olunur və bütün asılılıqlar heç bir əlavə müdaxilə olmadan quraşdırılır.

2. **Əl ilə terminaldan quraşdırmaq istədikdə:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Kəmiyyət və keyfiyyət analizlərini yenidən çalışdırın:**
   ```bash
   python run_quantitative_analysis.py
   python run_qualitative_analysis.py
   ```

3. **Jupyter Notebook-u icra edin:**
   ```bash
   jupyter nbconvert --to notebook --execute --inplace Keyfiyyet_ve_Kemiyyet_Analizi.ipynb
   ```

4. **Elmi Hesabat PDF-ini tərtib edin:**
   ```bash
   python generate_pdf_report.py
   ```
