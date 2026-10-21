# AZƏRBAYCAN RESPUBLİKASINDA ƏMƏK BAZARININ REGİONAL VƏ SAHƏVİ DİFERENSİASİYASI: EKONOMETRİK MODELLƏŞDİRMƏ VƏ MƏTN KORPUSUNUN TEMATİK TƏHLİLİ
**Müəllif:** Agha Asgarov  
**Tədris Modulu:** Data Analitika • Keyfiyyət və Kəmiyyət Analizi  
**Məlumat Bazası:** Azərbaycan Respublikasının Dövlət Statistika Komitəsi (`stat.gov.az`)  
**Tarix:** Oktyabr 2026  

---

## XÜLASƏ (ABSTRACT)
Bu tədqiqat işində Azərbaycan Respublikasında əməkhaqqı səviyyəsinin sahəvi və regional formalaşma mexanizmləri həm kəmiyyət (ekonometrik reqressiya, ANOVA), həm də keyfiyyət (tematik mətn təhlili, kodlaşdırma sistemi) metodlarının inteqrasiyası (qarışıq metodlar - *mixed-methods triangulation*) vasitəsilə dərindən araşdırılmışdır. Tədqiqat çərçivəsində Dövlət Statistika Komitəsinin (DSK) 14 iqtisadi rayon, 19 iqtisadi fəaliyyət sahəsi, 2015–2024-cü illəri əhatə edən istehlak qiymətləri indeksi (CPI) və 10 rəsmi mətbuat xülasəsindən ibarət mətn korpusu təhlil edilmişdir. 

Kəmiyyət təhlili göstərir ki, sahələr arasında əməkhaqqı fərqləri statistik olaraq kəskin dərəcədə əhəmiyyətlidir (Birfaktorlu ANOVA: $F = 8.36, p < 0.001, \eta^2 = 0.22$). Ekonometrik reqressiya modelləri ($R^2 = 0.665, p = 0.0024$) regional əməkhaqqı asimmetriyasının əsasən şəhərləşmə payı (`urban_share`, $\beta = 401.44, p = 0.027$) və demoqrafik konsentrasiya ilə şərtləndiyini sübut edir. CPI deflyasiyası nəticəsində aşkar edilmişdir ki, 2015–2024-cü illərdə nominal əməkhaqqı 116.2% artsa da, məcmu inflyasiyanın 85.0% olması səbəbindən real əməkhaqqı artımı cəmi 16.8% təşkil etmişdir. Keyfiyyət təhlilində iki müstəqil kodlayıcı tərəfindən həyata keçirilən kodlaşdırma prosesi nəticəsində Cohen's Kappa etibarlılıq əmsalı $\kappa = 0.9427$ səviyyəsində qiymətləndirilmişdir. Sintez nəticəsində rəsmi statistik hesabatlarda ikirəqəmli nominal artımların qabardıldığı, lakin inflyasiya aşınması və regional qütbləşmənin təhlil sənədlərində arxa planda qaldığı tənqidi şəkildə əsaslandırılmışdır.

---

## 1. GİRİŞ VƏ TƏDQİQAT SUALLARI (RQ)
Keçid iqtisadiyyatını geridə qoyaraq post-neft modelinə inteqrasiya edən Azərbaycanda regional inkişaf disbalansı və sahələr üzrə gəlir qütbləşməsi makroiqtisadi siyasətin ən aktual problemlərindən biridir. İqtisadi fəaliyyətin və kapital qoyuluşunun paytaxt Bakı və Abşeron yarımadasında həddindən artıq cəmləşməsi rayonlararası sosial-iqtisadi təbəqələşməni dərinləşdirir. Bu reallığı təhlil etmək məqsədilə layihə çərçivəsində dörd əsas tədqiqat sualı (Research Questions - RQ) irəli sürülmüşdür:

* **RQ1 (Sahəvi Kəmiyyət):** İqtisadi fəaliyyət növləri üzrə formalaşan orta aylıq nominal əməkhaqqı göstəriciləri arasında statistik cəhətdən əhəmiyyətli fərqlər mövcuddurmu və bu fərqlərin effekt ölçüsü nə dərəcədədir?
* **RQ2 (Regional Ekonometrika):** İqtisadi rayonlar üzrə nominal əməkhaqqı səviyyəsi əhalinin miqyası (`log_pop`) və şəhərləşmə dərəcəsi (`urban_share`) ilə necə əlaqələnir?
* **RQ3 (Real Alıcılıq Qabiliyyəti - Bonus):** 2015–2024-cü illərdə qeydə alınan nominal əməkhaqqı artımı istehlak qiymətləri indeksi (CPI) ilə inflyasiyadan təmizləndikdə real alıcılıq qabiliyyətində necə əks olunur?
* **RQ4 (Keyfiyyət və Rəsmi Diskurs):** Dövlət Statistika Komitəsinin rəsmi mətbuat relizlərində və metodoloji sənədlərində əmək bazarının hansı aspektləri prioritetləşdirilir və bu təqdimat empirik kəmiyyət reallıqları ilə necə uzlaşır?

---

## 2. METODOLOGİYA VƏ MƏLUMAT BAZASI (DATA & METHODOLOGY)

### 2.1 Məlumat Dəstləri və Dəyişənlərin Təsviri
Tədqiqat üçün ilkin məlumatlar Azərbaycan Respublikası Dövlət Statistika Komitəsinin rəsmi portalından (`stat.gov.az`) əldə edilmiş və təmizlənərək vahid formata gətirilmişdir:
1. **İqtisadi rayonlar üzrə əməkhaqqı (`wage`, asılı dəyişən):** 14 iqtisadi rayonun 2015–2024-cü illər üzrə orta aylıq nominal əməkhaqqı göstəriciləri (`009_6.xls` və təsdiqləyici CSV).
2. **Regional demoqrafiya (`log_pop`, `urban_share`, izah edici dəyişənlər):** 2026-cı ilin əvvəlinə 14 iqtisadi rayon üzrə cəmi, şəhər və kənd əhalisi (`001_19.xls`). Buradan şəhərləşmə payı $\text{urban\_share} = \frac{\text{Şəhər Əhalisi}}{\text{Cəmi Əhali}}$ və əhali miqyası $\text{log\_pop} = \ln(\text{Əhali Sayı})$ hesablanmışdır.
3. **Sahəvi əməkhaqqı (`sector`):** 19 iqtisadi sahə üzrə 2015–2024-cü illərin rəsmi əməkhaqqı göstəriciləri (`004_2-3.xls`), 4 makroiqtisadi qrupa klasterləşdirilmişdir: *Aqrar Sektor*, *Sənaye və Tikinti*, *Maliyyə, İKT və Dövlət*, *Ticarət və Sosial Xidmətlər*.
4. **İstehlak qiymətləri indeksi (CPI):** 2015–2024 illəri üzrə illik CPI zənciri (2015 = 100 bazası).
5. **Keyfiyyət korpusu:** 2026-cı il ərzində dərc edilmiş 10 rəsmi statistik mətbuat xülasəsi və DSK-nın əmək bazarı metodoloji izahat sənədləri (`004.doc`).

### 2.2 Ekonometrik və Statistik Modelləşdirmə
* **Birfaktorlu ANOVA (One-way ANOVA) və Post-Hoc Test:** Makro-sahələr üzrə fərqlər $F$-statistikası və $\eta^2$ (Eta-kvadrat) effekt ölçüsü ilə ölçülmüş, sahələrarası cüt fərqlər Tukey HSD testi ilə sınaqdan keçirilmişdir.
* **OLS Çoxölçülü Reqressiya Modelləri:**
  $$\text{Model 1:} \quad \text{wage}_i = \beta_0 + \beta_1 \log(\text{pop}_i) + \varepsilon_i$$
  $$\text{Model 2:} \quad \text{wage}_i = \beta_0 + \beta_1 \log(\text{pop}_i) + \beta_2 \text{urban\_share}_i + \varepsilon_i$$
  $$\text{Model 3 (Log-Log):} \quad \log(\text{wage}_i) = \alpha_0 + \alpha_1 \log(\text{pop}_i) + \alpha_2 \text{urban\_share}_i + u_i$$
* **Ekonometrik Diaqnostika:** Qalıqların paylanmasının normallığı (Shapiro-Wilk və Jarque-Bera), sabit dispersiya (Breusch-Pagan) və multikollinearlıq riski (Variance Inflation Factor - VIF) qiymətləndirilmişdir.

### 2.3 Keyfiyyət Analizi: Kodlaşdırma Sxemi və Etibarlılıq
Keyfiyyət təhlili çərçivəsində 6 operativ kod və 6 tematik kateqoriyadan ibarət kodlaşdırma kitabı (`codebook.csv`) tərtib edilmişdir. Tədqiqat korpusuna daxil olan 46 mətn vahidi iki müstəqil kodlayıcı (Coder 1 və Coder 2) tərəfindən kodlaşdırılmış və kodlayıcılararası etibarlılıq dərəcəsi Cohen's Kappa ($\kappa$) formulu ilə hesablanmışdır:
$$\kappa = \frac{P_o - P_e}{1 - P_e}$$

---

## 3. EMPİRİK KƏMİYYƏT TƏHLİLİ VƏ NƏTİCƏLƏR

### 3.1 İqtisadi Fəaliyyət Sahələri üzrə ANOVA Nəticələri
Aparılan birfaktorlu ANOVA testi nəticəsində iqtisadi sahələr arasında əməkhaqqı fərqlərinin yüksək statistik əhəmiyyətə malik olduğu təsdiq olunmuşdur:
* **F-statistikası:** $F(3, 91) = 8.3616, \quad p = 5.72 \times 10^{-5} < 0.001$
* **Effekt Ölçüsü:** $\eta^2 = 0.2161$ (Sahələrarası fərq ümumi dispersiyanın 21.6%-ni izah edir ki, bu da Cohen standartlarına görə çox böyük effekt ölçüsüdür).

**Cədvəl 1: Tukey HSD Cütlü Müqayisə Nəticələri ($\alpha = 0.05$)**
| Qrup 1 | Qrup 2 | Orta Fərq (AZN) | p-adj | 95% Etibarlılıq İntervalı | Qərar ($H_0$) |
|---|---|---|---|---|---|
| Aqrar Sektor | Maliyyə, İKT və Dövlət | +999.98 | 0.0113 | [172.3, 1827.7] | **Rədd edilir** |
| Aqrar Sektor | Sənaye və Tikinti | +767.70 | 0.0578 | [-17.5, 1552.9] | Sərhəddə |
| Aqrar Sektor | Ticarət və Sosial Xidmətlər | +271.20 | 0.7812 | [-480.6, 1023.0] | Qəbul edilir |
| Maliyyə, İKT və Dövlət | Ticarət və Sosial Xidmətlər | -728.79 | 0.0006 | [-1200.6, -256.9] | **Rədd edilir** |
| Sənaye və Tikinti | Ticarət və Sosial Xidmətlər | -496.50 | 0.0072 | [-889.1, -103.9] | **Rədd edilir** |

Tukey HSD testi sübut edir ki, *Maliyyə, İKT və Dövlət* klasteri ilə *Aqrar Sektor* arasında orta hesabla 1000 AZN-lik kəskin uçurum mövcuddur. Eyni zamanda təhsil, səhiyyə və pərakəndə ticarəti birləşdirən *Sosial Xidmətlər* sahəsi həm sənaye, həm də maliyyə sektorlarından statistik olaraq kəskin şəkildə geri qalır.

### 3.2 İqtisadi Rayonlar üzrə Ekonometrik Reqressiya Təhlili
14 iqtisadi rayon üzrə qiymətləndirilən OLS reqressiya modellərinin nəticələri Cədvəl 2-də ümumiləşdirilmişdir.

**Cədvəl 2: Regional Əməkhaqqı Reqressiya Modellərinin Nəticələri (N = 14)**
| Müstəqil Dəyişənlər | Model 1 (Xətti) | Model 2 (Çoxölçülü Xətti) | Model 3 (Loqarifmik: $\log(\text{wage})$) |
|---|---|---|---|
| **Sabit Hədd (Intercept)** | -1106.88 (t = -1.09) | -756.27 (t = -0.76) | **5.3552\*\*\* (t = 4.83)** |
| **log_pop** | 136.21\* (t = 1.80, p=0.09) | 98.04 (t = 1.27, p=0.230) | 0.0748 (t = 0.86, p=0.406) |
| **urban_share** | — | **401.44\*\* (t = 2.56, p=0.027)** | **0.5019\*\* (t = 2.85, p=0.016)** |
| **$R^2$** | 0.213 | **0.665** | **0.660** |
| **Düzəliş edilmiş $R^2$** | 0.147 | **0.604** | **0.598** |
| **Model F-statistikası** | $F = 3.25$ (p = 0.09) | **$F = 10.92$ (p = 0.0024)** | **$F = 10.66$ (p = 0.0027)** |

*Qeyd: \*\*\* p < 0.01, \*\* p < 0.05, \* p < 0.10.*

Model 2 və Model 3-ün nəticələri göstərir ki, şəhərləşmə səviyyəsi (`urban_share`) əməkhaqqı üzərində ən güclü və statistik əhəmiyyətli pozitiv təsirə malikdir ($p = 0.016$). Model 3-ün loqarifmik əmsalına görə, regionda şəhər əhalisinin payının 10 faiz bəndi artması orta aylıq əməkhaqqının təqribən **5.02%** artması ilə müşayiət olunur. Təkcə əhali miqyası (`log_pop`) təkbaşına zəif təsirə malik olsa da, şəhərləşmə amili daxil edildikdə modelin izahedicilik qabiliyyəti 21.3%-dən **66.5%-ə** yüksəlir.

### 3.3 Ekonometrik Diaqnostika
Qiymətləndirilən Model 3 üzrə klassik reqressiya fərziyyələrinin doğruluğu diaqnostik testlərlə yoxlanılmışdır:
1. **Qalıqların Normallığı:** Shapiro-Wilk testi statistikası $W = 0.9127, p = 0.1724 > 0.05$; Jarque-Bera testi $\chi^2 = 1.131, p = 0.568 > 0.05$. Qalıqlar normal paylanmaya malikdir.
2. **Homoskedastiklik:** Breusch-Pagan LM testi $p = 0.1526 > 0.05$. Qalıqların dispersiyası sabitdir (heteroskedastiklik mövcud deyil).
3. **Multikollinearlıq:** Həm `log_pop`, həm də `urban_share` üçün VIF dəyəri **1.757** təşkil edir. Bu göstərici kritik hədd olan 5.0-dən xeyli aşağıdır və modeldə multikollinearlıq problemi olmadığını sübut edir.

### 3.4 Bonus Təhlil: CPI İnflyasiya Deflyasiyası və Real Əməkhaqqı Dinamikası
2015–2024-cü illərdə nominal əməkhaqqı ilə istehlak qiymətləri indeksi (CPI) müqayisəli zəncirvari indeks kimi hesablanmışdır:

**Cədvəl 3: Nominal və Real Əməkhaqqının İnflyasiya ilə Tənzimlənmiş Dinamikası (2015=100)**
| İl | Nominal Əməkhaqqı (AZN) | İllik CPI (%) | Məcmu CPI İndeksi | Real Əməkhaqqı (2015 bazası, AZN) | Nominal Artım (%) | Real Artım (%) |
|---|---|---|---|---|---|---|
| **2015** | 466.9 | 104.0 | 100.0 | 466.9 | 0.0% | 0.0% |
| **2017** | 528.5 | 112.9 | 126.9 | 416.5 | +13.2% | **-10.8%** |
| **2019** | 635.1 | 102.6 | 133.2 | 476.8 | +36.0% | +2.1% |
| **2021** | 732.1 | 106.7 | 145.4 | 503.5 | +56.8% | +7.3% |
| **2023** | 933.9 | 108.8 | 181.1 | 515.8 | +100.0% | +10.5% |
| **2024** | 1009.4 | 102.2 | 185.1 | 545.5 | **+116.2%** | **+16.8%** |

Nəticələr göstərir ki, 2016–2017-ci illərdə manatın devalvasiyasından sonrakı kəskin inflyasiya dövründə nominal əməkhaqqı artsa da, real gəlirlər 2015-ci il səviyyəsinə nəzərən 10.8% azalmışdır. Yalnız 2019-cu ildən sonra real alıcılıq bərpa olunmağa başlamış və 2024-cü ildə 16.8%-lik xalis artım qeydə alınmışdır. Beləliklə, nominal artımın təxminən **85.5%-i inflyasiya tərəfindən udulmuşdur**.

---

## 4. KEYFİYYƏT ANALİZİ: KORPUSUN TEMATİK TƏHLİLİ VƏ KODLAŞDIRMA

### 4.1 Kodlaşdırma Sxemi (`codebook.csv`)
Tərtib edilmiş kodlaşdırma sistemi əmək bazarının rəsmi diskursunu 6 kod üzrə təsnif edir:
* **C01 (Mülkiyyət və Struktur):** Dövlət və qeyri-dövlət (özəl) sektorlarında çalışanların sayı və nisbəti.
* **C02 (Sahəvi Asimmetriya):** Fərqli iqtisadi sahələrdə işçi paylanması və əməkhaqqı təbəqələşməsi.
* **C03 (Nominal Artım Dinamikası):** Orta aylıq nominal əməkhaqqının illik və rüblük faiz artımları.
* **C04 (İnflyasiya və Alıcılıq Qabiliyyəti):** İstehlak qiymətlərinin bahalaşması və CPI dinamikası.
* **C05 (Dövlət İdarəetməsi və Qulluqçular):** Dövlət qulluqçularının vəzifə dərəcələri və əməkhaqqı.
* **C06 (Metodologiya və Standartlar):** BƏT (İLO) qaydaları, əməkhaqqı fondunun tərkibi və bruto hesablama metodları.

### 4.2 Kodlayıcılararası Etibarlılıq: Cohen's Kappa ($\kappa$)
Tədqiqat korpusuna daxil olan 46 mətn vahidi üzrə iki kodlayıcının müstəqil qiymətləndirməsi nəticəsində:
* **Müşahidə olunan razılıq ($P_o$):** 93.5%
* **Təsadüfi razılıq ehtimalı ($P_e$):** 21.8%
* **Cohen's Kappa ($\kappa$):** **0.9427**

Akademik metodologiyada (Landis & Koch, 1977; Fleiss et al., 2003) $\kappa > 0.80$ səviyyəsi "Demək olar ki, Mükəmməl Razılıq" (*Almost Perfect Agreement*) kimi qəbul olunur. Bu göstərici kodlaşdırma sxeminin obyektivliyini və təkrarlana bilənliyini (reproducibility) elmi cəhətdən təmin edir.

### 4.3 Tematik Tezliklərin Təhlili
Mətn korpusunda mövzuların paylanması:
1. **Nominal Artım Dinamikası (C03):** 16 vahid (34.8%) — Rəsmi relizlərin əsas vurğusu.
2. **Sahəvi Asimmetriya (C02):** 11 vahid (23.9%) — Sahələrarası işçi axını və fərqlər.
3. **İnflyasiya və Qiymət İndeksi (C04):** 8 vahid (17.4%) — İnflyasiya xəbərləri.
4. **Mülkiyyət Bölgüsü (C01):** 7 vahid (15.2%) — Özəl sektorun payının artması.
5. **Dövlət Qulluqçuları (C05):** 2 vahid (4.3%) — İnzibati kadrların maaşları.
6. **Metodoloji İzahlar (C06):** 2 vahid (4.3%) — Standartlar və təriflər.

---

## 5. SİNTEZ VƏ TƏNQİDİ ŞƏRH (MIXED-METHODS TRIANGULATION)

Kəmiyyət və keyfiyyət metodlarının çarpaz təhlili (*triangulation*) aşağıdakı strateji nəticələri ortaya qoyur:

1. **Rəsmi Təqdimat və Real Gəlir Paradoksu:**
   Keyfiyyət korpusunda ən yüksək təkrarlanan mövzu *Nominal Artım Dinamikasıdır* (34.8%). Rəsmi press-relizlərdə "orta aylıq nominal əməkhaqqı 7.2% artaraq 1173 manat olmuşdur" kimi pozitiv başlıqlar ön plana çıxarılır. Lakin kəmiyyət deflyasiya təhlili (Cədvəl 3) sübut edir ki, 10 il ərzində 116.2%-lik nominal artımın 85%-i qiymət artımları ilə sıradan çıxmış və faktiki real rifah artımı ildə orta hesabla cəmi 1.6% təşkil etmişdir. İnflyasiya relizləri (C04) əməkhaqqı hesabatlarından ayrı təqdim olunur ki, bu da gəlirlərin real alıcılıq dinamikası barədə bütöv təsəvvür formalaşdırmağa mane olur.

2. **Paytaxt Cəmləşməsi və Regional Polarizasiya:**
   Reqressiya modelimiz sübut edir ki, regional əməkhaqqı səviyyəsini formalaşdıran əsas determinant şəhərləşmə dərəcəsidir ($\beta = 401.44$). Bakı şəhərində orta aylıq əməkhaqqı 1269.3 AZN təşkil etdiyi halda, kənd təsərrüfatı yönümlü Mərkəzi Aran (621.2 AZN) və Şəki-Zaqatala (622.1 AZN) rayonlarında bu göstərici paytaxtdan iki dəfə aşağıdır. Keyfiyyət korpusunda xüsusi vurğulanan "özəl sektorun və xidmətlərin inkişafı" (C01 və C02) demək olar ki, tamamilə Abşeron iqtisadi zonasında cəmləşmişdir.

3. **Sahəvi Dualizm:**
   ANOVA nəticələri ($F = 8.36, \eta^2 = 0.22$) iqtisadiyyatda iki fərqli əmək bazarının mövcud olduğunu göstərir: bir tərəfdə yüksək əlavə dəyər yaradan mədənçıxarma (3350 AZN) və maliyyə-İKT sektoru (2327 AZN), digər tərəfdə isə məşğul əhalinin böyük hissəsini cəmləşdirən aqrar (558 AZN) və ictimai xidmətlər sahəsi. Rəsmi mətbuat məlumatlarında aqrar sektorun məşğulluq payı 2.3% kimi göstərilsə də (muzdlu işçilər üzrə), faktiki olaraq özünüməşğul kənd əhalisinin aşağı gəlir tələsində qalması struktur islahatların zəruriliyini göstərir.

---

## 6. MƏHDUDİYYƏTLƏR VƏ TÖVSİYƏLƏR (LIMITATIONS & RECOMMENDATIONS)

### 6.1 Tədqiqatın Məhdudiyyətləri
* **Regional CPI İndeksinin Olmaması:** Dövlət Statistika Komitəsi istehlak qiymətləri indeksini iqtisadi rayonlar üzrə ayrı-ayrılıqda dərc etmir. Nəticədə Bakıdakı yaşayış xərcləri ilə regionlardakı xərclər eyni qəbul edilmişdir. Əgər regional CPI mövcud olsaydı, paytaxtla rayonlar arasındakı real gəlir fərqinin bir qədər yumşaldığı müşahidə oluna bilərdi.
* **Qeyri-Formal Məşğulluq və "Zərf Əməkhaqqı":** Rəsmi statistika yalnız rəsmi əmək müqaviləsi ilə çalışan muzdlu işçiləri əhatə edir. Özəl sektorda geniş yayılmış qeyri-formal ödəmələr və kənd təsərrüfatında ailə təsərrüfatlarının gəlirləri bu cədvəllərdə tam əksini tapmır.

### 6.2 Siyasət Tövsiyələri
1. **Regional Diferensiallaşdırılmış Vergi və İnvestisiya Təşviqləri:** Regionlarda şəhərləşmə və sənaye mərkəzlərinin (Sumqayıt və Gəncədən kənar) inkişaf etdirilməsi, aqrar emal müəssisələrinə vergi tətillərinin verilməsi.
2. **Statistik İnteqrasiya və Şəffaflıq:** DSK tərəfindən rəsmi aylıq hesabatlarda nominal göstəricilərlə yanaşı mütləq şəkildə **inflyasiyadan təmizlənmiş real əməkhaqqı indekslərinin** dərc olunması.
3. **Sahəvi Əməkhaqqı İndeksasiyası:** Aşağı gəlirli sosial sahələrdə (təhsil, səhiyyə) baza maaşların illik inflyasiya dərəcəsinə avtomatik indeksləşdirilməsi mexanizminin tətbiqi.

---

## 7. İSTİFADƏ OLUNMUŞ ƏDƏBİYYAT VƏ MƏNBƏLƏR
1. Azərbaycan Respublikasının Dövlət Statistika Komitəsi (2026). *Əmək bazarı üzrə statistik göstəricilər*. `https://www.stat.gov.az/source/labour/`
2. Azərbaycan Respublikasının Dövlət Statistika Komitəsi (2026). *Demoqrafik göstəricilər və əhalinin sayı*. `https://www.stat.gov.az/source/demoqraphy/`
3. Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37-46.
4. Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 159-174.
5. Wooldridge, J. M. (2015). *Introductory Econometrics: A Modern Approach*. Cengage Learning.
