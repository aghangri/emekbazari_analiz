# 5 DƏQİQƏLİK QRUP TƏQDİMATI PLANI VƏ ÇIXIŞ SSENARİSİ
## Azərbaycan Respublikasında Əmək Bazarının Regional və Sahəvi Diferensiasiyası: Ekonometrik Modelləşdirmə və Mətn Korpusunun Tematik Təhlili

*Təqdimat Müddəti: 5 dəqiqə*  
*Format: 6 Slaydlıq Strukturlaşdırılmış Çıxış*

---

### SLAYD 1: Giriş, Problem və Tədqiqat Sualları (0:00 – 0:50)
* **Slayd Başlığı:** Azərbaycan Əmək Bazarında Gəlir Bərabərsizliyi: Reallıq və Rəsmi Təqdimat
* **Vizual:** Azərbaycan xəritəsi üzərində iqtisadi rayonların əməkhaqqı disbalansı.
* **Əsas Nöqtələr:**
  * Post-neft dövründə respublikada iqtisadi aktivliyin paytaxt Bakı və Abşeronda cəmləşməsi regional gəlir qütbləşməsini dərinləşdirir.
  * Tədqiqatın 4 əsas sualı:
    1. İqtisadi sahələr arasında əməkhaqqı fərqi statistik əhəmiyyətlidirmi? (ANOVA)
    2. Regional əməkhaqqı şəhərləşmə (`urban_share`) və əhali miqyası (`log_pop`) ilə necə əlaqələnir? (Reqressiya)
    3. 2015–2024 illərində nominal artım inflyasiyadan (CPI) təmizləndikdə real gəlir necə dəyişib?
    4. Rəsmi mətbuat bülletenlərində əmək bazarının hansı aspektləri vurğulanır? (Keyfiyyət təhlili)
* **Natiqin Çıxış Mətni:**
  > *"Hörmətli auditoriya və münsiflər heyəti, bu gün sizə təqdim etdiyimiz tədqiqat işi həm ekonometrik kəmiyyət modelləri, həm də rəsmi mətbuat korpusunun keyfiyyət analizi vasitəsilə Azərbaycan əmək bazarındakı gəlir asimmetriyasını araşdırır. Əsas məqsədimiz rəsmi statistik hesabatlardakı nominal göstəricilər ilə arxa fonda baş verən real iqtisadi prosesləri üz-üzə qoymaq və sintez etməkdir."*

---

### SLAYD 2: Məlumat Mənbələri və Metodologiya (0:50 – 1:30)
* **Slayd Başlığı:** Metodoloji Çərçivə: Kəmiyyət və Keyfiyyətin Vəhdəti (Mixed-Methods)
* **Vizual:** İş axını diaqramı (DSK portalları &rarr; Data Cleaning &rarr; ANOVA/OLS &rarr; Codebook/Kappa &rarr; Triangulation).
* **Əsas Nöqtələr:**
  * **Mənbə:** Dövlət Statistika Komitəsinin (`stat.gov.az`) rəsmi statistik cədvəlləri (`009_6`, `001_19`, `004_2`, CPI zənciri).
  * **Reqressiya Modeli:** OLS çoxölçülü model: $\log(\text{wage}_i) = \beta_0 + \beta_1 \log(\text{pop}_i) + \beta_2 \text{urban\_share}_i + \varepsilon_i$.
  * **Sahəvi ANOVA:** 19 sahə üzrə F-testi, Tukey HSD və Eta-kvadrat ($\eta^2$).
  * **Keyfiyyət Korpusu:** 10 rəsmi mətbuat xülasəsi, 46 mətn vahidi, 6 operativ kod, iki müstəqil kodlayıcı.
* **Natiqin Çıxış Mətni:**
  > *"Tədqiqatımızda metodoloji bütövlüyü təmin etmək üçün 14 iqtisadi rayonun və 19 sahənin 10 illik rəsmi məlumatlarını təmizləyərək birləşdirdik. Təkcə kəmiyyətlə kifayətlənməyərək, DSK-nın 10 rəsmi bülletenini mətn analizinə cəlb etdik və iki analitikin müstəqil kodlaşdırması ilə keyfiyyət ölçməsini həyata keçirdik."*

---

### SLAYD 3: Kəmiyyət Nəticələri: ANOVA və Ekonometrik Reqressiya (1:30 – 2:45)
* **Slayd Başlığı:** Empirik Sübutlar: Şəhərləşmə Faktoru və Sahəvi Uçurum
* **Vizual:** Yan-yana iki qrafik: Sahələr üzrə ANOVA boxplot (`fig2_sector_anova.png`) və Reqressiya uyğunluq qrafiki (`fig3_regression_scatter.png`).
* **Əsas Nöqtələr:**
  * **ANOVA Nəticəsi:** $F(3, 91) = 8.36, p < 0.001$, Effekt ölçüsü $\eta^2 = 0.22$. *Maliyyə, İKT və Dövlət* klasteri ilə *Aqrar Sektor* arasında orta hesabla **1000 AZN-lik** kəskin fərq var (Tukey HSD: $p = 0.011$).
  * **Reqressiya Nəticəsi:** $R^2 = 0.665, F = 10.92, p = 0.0024$.
  * Şəhərləşmə payı (`urban_share`) ən güclü izahedici amildir ($\beta = 401.44, p = 0.027$). Şəhər əhalisinin payı 10% artdıqda nominal əməkhaqqı 5.0% yüksəlir.
  * **Diaqnostika:** Shapiro-Wilk ($p=0.172$), Breusch-Pagan ($p=0.153$), VIF = 1.76 (Model bütün ekonometrik fərziyyələri ödəyir).
* **Natiqin Çıxış Mətni:**
  > *"Kəmiyyət təhlilimizin nəticələri iki mühüm qanunauyğunluğu sübut edir: Birincisi, sahələr üzrə birfaktorlu ANOVA testi göstərir ki, sahəvi fəaliyyət gəlir fərqlərinin 22%-ni təkbaşına izah edir və aqrar sahə ilə maliyyə-İKT sektoru arasında 1000 manatlıq uçurum var. İkincisi, ekonometrik reqressiya modelimiz sübut edir ki, regional gəlir fərqini izah edən əsas amil əhali miqyası deyil, məhz şəhərləşmə dərəcəsidir (R²=0.665). Bakıda əməkhaqqı 1269 manat olduğu halda, aqrar rayonlarda 620 manat səviyyəsində qalır."*

---

### SLAYD 4: Bonus Təhlil: CPI İnflyasiyası və Real Əməkhaqqı (2:45 – 3:30)
* **Slayd Başlığı:** Real vs Nominal Əməkhaqqı: İnflyasiya Aşınması
* **Vizual:** Nominal və Real əməkhaqqı dinamikası qrafiki (`fig4_real_vs_nominal_wage.png`).
* **Əsas Nöqtələr:**
  * 2015–2024 illərində nominal əməkhaqqı: 466.9 AZN &rarr; 1009.4 AZN (**+116.2% artım**).
  * 10 illik məcmu istehlak inflyasiyası: **+85.0%**.
  * 2015-ci il alıcılıq qabiliyyətinə görə real əməkhaqqı: 2024-cü ildə **545.5 AZN** (**cəmi +16.8% xalis artım**).
  * 2016–2017 devalvasiya dalğasında real əməkhaqqı 10.8% azalmışdır.
* **Natiqin Çıxış Mətni:**
  > *"Slaydımızdakı qrafik layihəmizin ən maraqlı empirik tapıntısını nümayiş etdirir. 10 il ərzində nominal maaşlar 116% artsa da, istehlak qiymətləri indeksi ilə tənzimlədikdə görürük ki, real alıcılıq qabiliyyəti cəmi 16.8% artıb. Yəni nominal artımın 85%-dən çoxu inflyasiya tərəfindən 'udulmuşdur'."*

---

### SLAYD 5: Keyfiyyət Analizi: Kodlaşdırma Sxemi və Cohen's Kappa (3:30 – 4:15)
* **Slayd Başlığı:** Keyfiyyət Təhlili: Rəsmi Mətbuat Korpusu və Etibarlılıq
* **Vizual:** Keyfiyyət mövzularının paylanması diaqramı (`fig6_qualitative_themes.png`) və `codebook.csv` struktur cədvəli.
* **Əsas Nöqtələr:**
  * 6 tematik kod: *Mülkiyyət və Struktur*, *Sahəvi Asimmetriya*, *Nominal Artım Dinamikası*, *İnflyasiya və Alıcılıq*, *Dövlət Qulluqçuları*, *Metodologiya*.
  * İki kodlayıcı arasında etibarlılıq: **Cohen's Kappa $\kappa = 0.9427$** (mükəmməl elmi razılıq).
  * Rəsmi korpusda ən çox təkrarlanan mövzu: **Nominal Artım Dinamikası (34.8%)** və **Sahəvi Asimmetriya (23.9%)**.
* **Natiqin Çıxış Mətni:**
  > *"Keyfiyyət korpusumuzda 46 mətn vahidini kodlaşdırarkən iki analitik arasında Cohen's Kappa əmsalını 0.94 səviyyəsində əldə etdik. Bu, beynəlxalq elmi standartlara görə demək olar ki, mükəmməl razılıqdır. Mətn təhlili göstərir ki, rəsmi hesabatlarda ən çox diqqət mərkəzində saxlanılan mövzu məhz 'nominal artım faizləridir' (34.8%)."*

---

### SLAYD 6: Sintez, Tənqidi Nəticələr və Tövsiyələr (4:15 – 5:00)
* **Slayd Başlığı:** Sintez və Siyasət Tövsiyələri (Triangulation)
* **Vizual:** Kəmiyyət və keyfiyyətin qarşılaşdırma matrisi və 3 strateji tövsiyə.
* **Əsas Nöqtələr:**
  * **İnstitusional Paradoks:** Rəsmi diskurs ikirəqəmli nominal artımları qabardır, lakin inflyasiya hesabatları təcrid olunmuş şəkildə verilir. Real alıcılıq artımının illik orta hesabla cəmi 1.6% olması ictimai kommunikasiyada kölgədə qalır.
  * **Regional Dualizm:** Kənd rayonlarında şəhərləşmənin zəifliyi aqrar gəlir tələsi yaradır.
  * **Tövsiyələr:**
    1. DSK tərəfindən inflyasiyadan təmizlənmiş *real əməkhaqqı indekslərinin* mütəmadi dərci.
    2. Rayonlarda sənaye və xidmət klasterlərinə diferensial vergi təşviqləri.
    3. Sosial sahələrdə (təhsil, səhiyyə) baza maaşların inflyasiyaya avtomatik indeksasiyası.
* **Natiqin Çıxış Mətni:**
  > *"Yekun olaraq: Kəmiyyət və keyfiyyət metodlarının sintezi sübut edir ki, rəsmi hesabatlar gəlirlərin nominal artımını önə çəksə də, ölkədə ikiqat qütbləşmə mövcuddur: paytaxt və rayonlar arasındakı şəhərləşmə uçurumu və yüksək texnoloji sahələrlə aqrar sektor arasındakı maaş fərqi. Siyasət səviyyəsində DSK-nın real əməkhaqqı indekslərini mütləq şəkildə dərc etməsi və regionlarda qeyri-aqrar iş yerlərinə vergi təşviqlərinin verilməsi zəruridir. Diqqətiniz üçün təşəkkür edirik!"*
