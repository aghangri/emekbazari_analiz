import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.stdout.reconfigure(encoding='utf-8')

# Register TrueType Fonts for full Azerbaijani character support
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Italic', 'C:/Windows/Fonts/ariali.ttf'))

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Arial", 9)
        self.setFillColor(colors.HexColor("#666666"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(2 * cm, 28.2 * cm, "Data Analitika Layihəsi: Keyfiyyət və Kəmiyyət Analizi Hesabatı")
            self.setStrokeColor(colors.HexColor("#dddddd"))
            self.setLineWidth(0.5)
            self.line(2 * cm, 28 * cm, 19 * cm, 28 * cm)
            
        # Footer
        page_text = f"Səhifə {self._pageNumber} / {page_count}"
        self.drawRightString(19 * cm, 1.2 * cm, page_text)
        self.drawString(2 * cm, 1.2 * cm, "Mənbə: Azərbaycan Respublikasının Dövlət Statistika Komitəsi (stat.gov.az)")
        self.setStrokeColor(colors.HexColor("#dddddd"))
        self.setLineWidth(0.5)
        self.line(2 * cm, 1.5 * cm, 19 * cm, 1.5 * cm)
        self.restoreState()

def build_pdf():
    pdf_filename = "HESABAT_Keyfiyyet_ve_Kemiyyet_Analizi.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2.2 * cm,
        bottomMargin=2.2 * cm
    )

    styles = getSampleStyleSheet()
    
    # Custom Typography
    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Arial-Bold',
        fontSize=17,
        leading=22,
        textColor=colors.HexColor('#1a365d'),
        alignment=1, # Center
        spaceAfter=12
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        fontName='Arial-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#2b6cb0'),
        alignment=1,
        spaceAfter=8
    )
    
    meta_style = ParagraphStyle(
        'DocMeta',
        fontName='Arial',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#4a5568'),
        alignment=1,
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        fontName='Arial-Bold',
        fontSize=12.5,
        leading=16,
        textColor=colors.HexColor('#1a365d'),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        fontName='Arial-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#2d3748'),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        fontName='Arial',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#2d3748'),
        spaceAfter=6,
        alignment=4 # Justified
    )
    
    abstract_style = ParagraphStyle(
        'AbstractText',
        fontName='Arial-Italic',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#2d3748'),
        alignment=4
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        fontName='Arial',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#2d3748')
    )
    
    table_header = ParagraphStyle(
        'TableHeader',
        fontName='Arial-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    story = []

    # Title Block
    story.append(Paragraph("AZƏRBAYCAN RESPUBLİKASINDA ƏMƏK BAZARININ REGİONAL VƏ SAHƏVİ DİFERENSİASİYASI", title_style))
    story.append(Paragraph("Ekonometrik Modelləşdirmə və Mətn Korpusunun Tematik Təhlili (Mixed-Methods Tədqiqat)", subtitle_style))
    story.append(Paragraph("<b>Müəllif:</b> Agha Asgarov &nbsp;|&nbsp; <b>Kurs:</b> Data Analitika • Keyfiyyət və Kəmiyyət Analizi &nbsp;|&nbsp; <b>Tarix:</b> Oktyabr 2026", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2b6cb0'), spaceBefore=2, spaceAfter=10))

    # Abstract Box
    abstract_data = [[
        Paragraph("<b>XÜLASƏ (ABSTRACT):</b> Bu tədqiqat işində Azərbaycan əmək bazarının sahəvi və regional diferensiasiyası həm kəmiyyət (ekonometrik OLS regressiya, ANOVA), həm də keyfiyyət (tematik mətn təhlili, kodlaşdırma sistemi) metodlarının inteqrasiyası vasitəsilə təhlil edilmişdir. Dövlət Statistika Komitəsinin (stat.gov.az) 14 iqtisadi rayon, 19 iqtisadi fəaliyyət sahəsi, 2015–2024 CPI zənciri və 10 rəsmi mətbuat xülasəsindən ibarət korpus tədqiq olunmuşdur. Kəmiyyət təhlili sahələrarası əməkhaqqı fərqlərinin yüksək statistik əhəmiyyətini (ANOVA: F=8.36, p<0.001, η²=0.22), ekonometrik modellər isə regional gəlir bərabərsizliyində şəhərləşmənin həlledici rolunu (urban_share: β=401.44, p=0.027, R²=0.665) təsdiq edir. CPI deflyasiyası nəticəsində aşkar edilmişdir ki, 2015–2024-cü illərdə nominal əməkhaqqı 116.2% artsa da, məcmu inflyasiyanın 85.0% olması səbəbindən real əməkhaqqı artımı cəmi 16.8% olmuşdur. İki müstəqil kodlayıcı üzrə etibarlılıq Cohen's Kappa κ = 0.9427 səviyyəsində qiymətləndirilmişdir.", abstract_style)
    ]]
    t_abstract = Table(abstract_data, colWidths=[17 * cm])
    t_abstract.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f7fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e0')),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_abstract)
    story.append(Spacer(1, 10))

    # 1. Giriş və Tədqiqat Sualları
    story.append(Paragraph("1. Giriş və Tədqiqat Sualları (RQ)", h1_style))
    story.append(Paragraph("Azərbaycan iqtisadiyyatında neft-qaz sektorunun üstünlüyü və iqtisadi aktivliyin Abşeron yarımadasında cəmləşməsi regional və sahəvi gəlir bərabərsizliyini dərinləşdirən mühüm amillərdəndir. Bu tədqiqat işi əmək bazarındakı asimmetriyanı həm statistik-ekonometrik, həm də institusional mətbuat diskursu prizmasından dərindən araşdırır. Tədqiqatın əsas sualları aşağıdakılardır:", body_style))
    story.append(Paragraph("• <b>RQ1 (Sahəvi ANOVA):</b> İqtisadi fəaliyyət sahələri arasında orta aylıq nominal əməkhaqqı üzrə statistik cəhətdən əhəmiyyətli fərqlər mövcuddurmu və bu fərqin effekt ölçüsü nə dərəcədədir?", body_style))
    story.append(Paragraph("• <b>RQ2 (Regional Ekonometrika):</b> İqtisadi rayonlar üzrə nominal əməkhaqqı səviyyəsi əhali miqyası (log_pop) və şəhərləşmə dərəcəsi (urban_share) ilə necə izah olunur?", body_style))
    story.append(Paragraph("• <b>RQ3 (Real Gəlir - Bonus):</b> 2015–2024-cü illərdə nominal əməkhaqqının artımı istehlak qiymətləri indeksi (CPI) ilə inflyasiyadan təmizləndikdə real alıcılıq qabiliyyətində necə əks olunur?", body_style))
    story.append(Paragraph("• <b>RQ4 (Keyfiyyət Analizi):</b> Dövlət Statistika Komitəsinin rəsmi mətbuat xülasələrində hansı struktur mövzular prioritetləşdirilir və bu empirik nəticələrlə necə uzlaşır?", body_style))

    # 2. Metodologiya və Məlumat Dəstləri
    story.append(Paragraph("2. Metodologiya və Məlumat Bazası", h1_style))
    story.append(Paragraph("Tədqiqatda Azərbaycan Respublikası Dövlət Statistika Komitəsinin (DSK) rəsmi statistik məlumatları və xəbər bülletenləri əsasında vahid verilənlər bazası formalaşdırılmışdır:", body_style))
    story.append(Paragraph("1. <b>Regional göstəricilər:</b> 14 iqtisadi rayon üzrə nominal əməkhaqqı (wage) və əhali strukturu (pop_total, urban_pop, rural_pop). Buradan izah edici dəyişənlər kimi <i>urban_share</i> (şəhər əhalisinin payı) və <i>log_pop</i> (əhali sayının təbii loqarifmi) hesablanmışdır.", body_style))
    story.append(Paragraph("2. <b>Sahəvi göstəricilər:</b> 19 iqtisadi fəaliyyət sahəsi üzrə əməkhaqqı göstəriciləri 4 makro kateqoriyaya klasterləşdirilmişdir: Aqrar Sektor, Sənaye və Tikinti, Maliyyə/İKT/Dövlət, Ticarət və Sosial Xidmətlər.", body_style))
    story.append(Paragraph("3. <b>İnflyasiya və CPI:</b> 2015–2024 illəri üzrə illik CPI zənciri vasitəsilə 2015-ci il baza götürülərək real əməkhaqqı deflyasiya edilmişdir.", body_style))
    story.append(Paragraph("4. <b>Keyfiyyət korpusu:</b> DSK-nın 10 rəsmi statistik press-relizi və əmək bazarı metodoloji izahat sənədlərindən 46 mətn vahidi çıxarılaraq 6 kodluq kodlaşdırma kitabı (codebook.csv) əsasında iki müstəqil kodlayıcı tərəfindən kodlaşdırılmışdır.", body_style))

    # 3. Kəmiyyət Nəticələri
    story.append(Paragraph("3. Empirik Kəmiyyət Təhlili və Nəticələr", h1_style))
    story.append(Paragraph("<b>3.1 İqtisadi Sahələr üzrə ANOVA Təhlili:</b> Birfaktorlu ANOVA nəticələri sahələr arasında əməkhaqqı fərqlərinin son dərəcə yüksək statistik əhəmiyyətə malik olduğunu təsdiqləyir: <b>F(3, 91) = 8.3616, p = 5.72 × 10⁻⁵</b>. Effekt ölçüsü <b>η² = 0.2161</b> təşkil edir (ümumi dəyişkənliyin 21.6%-i sahəvi mənsubiyyətlə izah olunur).", body_style))
    
    # ANOVA Table
    anova_data = [
        [Paragraph("<b>Qrup Müqayisəsi (Tukey HSD)</b>", table_header), Paragraph("<b>Orta Fərq (AZN)</b>", table_header), Paragraph("<b>p-adj</b>", table_header), Paragraph("<b>95% Etibarlılıq İntervalı</b>", table_header), Paragraph("<b>Qərar</b>", table_header)],
        [Paragraph("Aqrar vs Maliyyə, İKT, Dövlət", table_cell), Paragraph("+999.98", table_cell), Paragraph("0.0113", table_cell), Paragraph("[172.3, 1827.7]", table_cell), Paragraph("<b>Əhəmiyyətli</b>", table_cell)],
        [Paragraph("Aqrar vs Sənaye və Tikinti", table_cell), Paragraph("+767.70", table_cell), Paragraph("0.0578", table_cell), Paragraph("[-17.5, 1552.9]", table_cell), Paragraph("Sərhəddə", table_cell)],
        [Paragraph("Aqrar vs Ticarət və Sosial Xidmət", table_cell), Paragraph("+271.20", table_cell), Paragraph("0.7812", table_cell), Paragraph("[-480.6, 1023.0]", table_cell), Paragraph("Qeyri-əhəmiyyətli", table_cell)],
        [Paragraph("Maliyyə/İKT vs Ticarət/Sosial", table_cell), Paragraph("-728.79", table_cell), Paragraph("0.0006", table_cell), Paragraph("[-1200.6, -256.9]", table_cell), Paragraph("<b>Əhəmiyyətli</b>", table_cell)],
        [Paragraph("Sənaye/Tikinti vs Ticarət/Sosial", table_cell), Paragraph("-496.50", table_cell), Paragraph("0.0072", table_cell), Paragraph("[-889.1, -103.9]", table_cell), Paragraph("<b>Əhəmiyyətli</b>", table_cell)]
    ]
    t_anova = Table(anova_data, colWidths=[5*cm, 2.5*cm, 2*cm, 4.5*cm, 3*cm])
    t_anova.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a365d')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7fafc')]),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_anova)
    story.append(Spacer(1, 6))

    # Image 1: Sector Boxplot
    if os.path.exists('reports/figures/fig2_sector_anova.png'):
        story.append(Image('reports/figures/fig2_sector_anova.png', width=16*cm, height=7*cm))
        story.append(Paragraph("<b>Şəkil 1:</b> İqtisadi Fəaliyyət Sahələri üzrə Əməkhaqqı Paylanması və ANOVA Qrup Fərqləri.", meta_style))

    story.append(Paragraph("<b>3.2 İqtisadi Rayonlar üzrə Reqressiya Modelləri:</b> 14 iqtisadi rayon üzrə qiymətləndirilən OLS reqressiya modeli (Cədvəl 2) şəhərləşmə dərəcəsinin əməkhaqqı üzərində müəyyənedici təsirini aşkara çıxarmışdır. Şəhərləşmə payı 10 faiz bəndi artdıqda nominal əməkhaqqı təqribən 40.1 AZN (loqarifmik modeldə 5.02%) yüksəlir.", body_style))

    # Regression Table
    reg_data = [
        [Paragraph("<b>Dəyişən</b>", table_header), Paragraph("<b>Model 1 (Xətti)</b>", table_header), Paragraph("<b>Model 2 (Çoxölçülü Xətti)</b>", table_header), Paragraph("<b>Model 3 (Log-Log)</b>", table_header)],
        [Paragraph("Sabit Hədd (Intercept)", table_cell), Paragraph("-1106.88 (t=-1.09)", table_cell), Paragraph("-756.27 (t=-0.76)", table_cell), Paragraph("<b>5.3552*** (t=4.83)</b>", table_cell)],
        [Paragraph("log_pop", table_cell), Paragraph("136.21* (t=1.80, p=0.09)", table_cell), Paragraph("98.04 (t=1.27, p=0.230)", table_cell), Paragraph("0.0748 (t=0.86, p=0.406)", table_cell)],
        [Paragraph("urban_share", table_cell), Paragraph("—", table_cell), Paragraph("<b>401.44** (t=2.56, p=0.027)</b>", table_cell), Paragraph("<b>0.5019** (t=2.85, p=0.016)</b>", table_cell)],
        [Paragraph("R² / Düzəliş edilmiş R²", table_cell), Paragraph("0.213 / 0.147", table_cell), Paragraph("<b>0.665 / 0.604</b>", table_cell), Paragraph("<b>0.660 / 0.598</b>", table_cell)],
        [Paragraph("F-statistikası (p-dəyəri)", table_cell), Paragraph("3.25 (p=0.096)", table_cell), Paragraph("<b>10.92 (p=0.0024)</b>", table_cell), Paragraph("<b>10.66 (p=0.0027)</b>", table_cell)]
    ]
    t_reg = Table(reg_data, colWidths=[4.5*cm, 4*cm, 4.5*cm, 4*cm])
    t_reg.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2b6cb0')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7fafc')]),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_reg)
    story.append(Spacer(1, 6))

    # Diagnostics Box
    diag_data = [[
        Paragraph("<b>Reqressiya Diaqnostik Sınaqları (Model 3):</b><br/>"
                  "• <b>Normallıq:</b> Shapiro-Wilk W = 0.9127, p = 0.1724 > 0.05 (Qalıqlar normal paylanır).<br/>"
                  "• <b>Homoskedastiklik:</b> Breusch-Pagan LM p = 0.1526 > 0.05 (Sabit dispersiya qorunur).<br/>"
                  "• <b>Multikollinearlıq:</b> VIF = 1.757 (5.0 kritik həddindən xeyli aşağıdır, kollinearlıq yoxdur).", body_style)
    ]]
    t_diag = Table(diag_data, colWidths=[17*cm])
    t_diag.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#edf2f7')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_diag)
    story.append(Spacer(1, 6))

    # Image 2: Scatter & Fit
    if os.path.exists('reports/figures/fig3_regression_scatter.png'):
        story.append(Image('reports/figures/fig3_regression_scatter.png', width=16*cm, height=6.5*cm))
        story.append(Paragraph("<b>Şəkil 2:</b> Əməkhaqqının Şəhərləşmə (A) və Əhali Miqyası (B) ilə Əlaqəsi.", meta_style))

    # 4. CPI and Real Wage
    story.append(Paragraph("3.3 Bonus Kəmiyyət Analizi: CPI İnflyasiya və Real Əməkhaqqı", h2_style))
    story.append(Paragraph("2015–2024 illərində ölkə üzrə nominal əməkhaqqı 466.9 manatdan 1009.4 manata (+116.2%) yüksəlmişdir. Lakin bu dövr ərzində məcmu inflyasiya 85.0% təşkil etmişdir. Nəticədə 2015-ci ilin baza alıcılıq qabiliyyətinə görə hesablanmış real əməkhaqqı 2024-cü ildə cəmi 545.5 manat olmuş, real artım isə 10 il üçün <b>cəmi 16.8%</b> təşkil etmişdir. Xüsusilə 2016–2017-ci illərdə devalvasiya dalğasında real əməkhaqqı 10.8% azalmışdır.", body_style))

    if os.path.exists('reports/figures/fig4_real_vs_nominal_wage.png'):
        story.append(Image('reports/figures/fig4_real_vs_nominal_wage.png', width=16*cm, height=6.8*cm))
        story.append(Paragraph("<b>Şəkil 3:</b> Nominal və Real Əməkhaqqının Müqayisəli Dinamikası (2015–2024).", meta_style))

    # 5. Keyfiyyət Analizi
    story.append(Paragraph("4. Keyfiyyət Analizi: Kodlaşdırma Sxemi və Cohen's Kappa", h1_style))
    story.append(Paragraph("Keyfiyyət korpusunda 46 mətn vahidi 6 kod üzrə iki müstəqil analitik tərəfindən kodlaşdırılmışdır. Kodlaşdırma kitabçası (codebook.csv) əsasında əldə olunan nəticələr yüksək daxili uyğunluğu təsdiqləyir: <b>Cohen's Kappa κ = 0.9427</b> (Almost Perfect Agreement).", body_style))

    # Qualitative Table
    qual_data = [
        [Paragraph("<b>Kod</b>", table_header), Paragraph("<b>Mövzu (Theme)</b>", table_header), Paragraph("<b>Məzmun Təsviri</b>", table_header), Paragraph("<b>Tezlik</b>", table_header), Paragraph("<b>Pay (%)</b>", table_header)],
        [Paragraph("C01", table_cell), Paragraph("Mülkiyyət və Struktur", table_cell), Paragraph("Dövlət və qeyri-dövlət məşğulluq payları", table_cell), Paragraph("7", table_cell), Paragraph("15.2%", table_cell)],
        [Paragraph("C02", table_cell), Paragraph("Sahəvi Asimmetriya", table_cell), Paragraph("İqtisadi fəaliyyət növləri üzrə işçi və maaş bölgüsü", table_cell), Paragraph("11", table_cell), Paragraph("23.9%", table_cell)],
        [Paragraph("C03", table_cell), Paragraph("Nominal Artım Dinamikası", table_cell), Paragraph("Orta aylıq nominal əməkhaqqının faiz artımı", table_cell), Paragraph("16", table_cell), Paragraph("34.8%", table_cell)],
        [Paragraph("C04", table_cell), Paragraph("İnflyasiya və Alıcılıq", table_cell), Paragraph("İstehlak qiymətləri indeksi (CPI) və bahalaşma", table_cell), Paragraph("8", table_cell), Paragraph("17.4%", table_cell)],
        [Paragraph("C05", table_cell), Paragraph("Dövlət Qulluqçuları", table_cell), Paragraph("İnzibati və yardımçı dövlət qulluğu heyəti", table_cell), Paragraph("2", table_cell), Paragraph("4.3%", table_cell)],
        [Paragraph("C06", table_cell), Paragraph("Metodologiya", table_cell), Paragraph("Əməkhaqqı fondu və BƏT beynəlxalq standartları", table_cell), Paragraph("2", table_cell), Paragraph("4.3%", table_cell)]
    ]
    t_qual = Table(qual_data, colWidths=[1.5*cm, 4*cm, 6.5*cm, 2*cm, 3*cm])
    t_qual.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a365d')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e0')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f7fafc')]),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_qual)
    story.append(Spacer(1, 8))

    # 6. Sintez və Tənqidi Şərh
    story.append(Paragraph("5. Sintez və Tənqidi Şərh (Mixed-Methods Triangulation)", h1_style))
    story.append(Paragraph("Kəmiyyət və keyfiyyət tapıntılarının qarşılıqlı sintezi üç mühüm institusional ziddiyyəti aşkara çıxarır:", body_style))
    story.append(Paragraph("1. <b>Nominal Diskurs və Real İqtisadiyyat Ziddiyyəti:</b> DSK-nın mətbuat xülasələrində ən yüksək təkrarlanan mövzu Nominal Artımdır (34.8%). İctimaiyyətə 'orta əməkhaqqı 7.2% artdı' mesajı ötürülür, lakin inflyasiya xəbərləri tamamilə ayrı sənədlərdə təcrid olunmuş şəkildə verilir. Kəmiyyət təhlilimiz isə sübut etdi ki, 10 ildə qeydə alınan 116%-lik artımın 85%-dən çoxu inflyasiya tərəfindən aşınmışdır.", body_style))
    story.append(Paragraph("2. <b>Aqrar Tələ və Regional Qütbləşmə:</b> ANOVA testi aqrar sahə ilə maliyyə sektoru arasında 1000 AZN-lik fərq göstərir. Reqressiya modelimiz sübut edir ki, kənd rayonlarında şəhərləşmə aşağı olduğu üçün əməkhaqqı Bakıdan iki dəfə aşağı səviyyədə ilişib qalır (Mərkəzi Aran: 621 AZN vs Bakı: 1269 AZN). Rəsmi hesabatlarda isə bu regional gəlir uçurumu analitik deyil, yalnız deskriptiv rəqəmlər şəklində təqdim edilir.", body_style))

    # 7. Məhdudiyyətlər və Tövsiyələr
    story.append(Paragraph("6. Məhdudiyyətlər və Siyasət Tövsiyələri", h1_style))
    story.append(Paragraph("<b>Məhdudiyyətlər:</b> Əsas məhdudiyyət DSK tərəfindən regional CPI indeksinin dərc edilməməsidir; ölkə üzrə vahid inflyasiya fərziyyəsi Bakı ilə rayonlar arasındakı real alıcılıq fərqlərini qismən maskalaya bilər. İkinci məhdudiyyət isə qeyri-formal məşğulluq və kənd təsərrüfatında ailə əməyinin rəsmi əməkhaqqı fondundan kənarda qalmasıdır.", body_style))
    story.append(Paragraph("<b>Tövsiyələr:</b> (1) DSK rəsmi hesabatlarında nominal əməkhaqqı ilə yanaşı inflyasiyadan təmizlənmiş <i>real əməkhaqqı indekslərini</i> mütləq dərc etməlidir; (2) Regionlarda qeyri-aqrar iş yerlərinin yaradılması üçün sənaye və xidmət klasterlərinə diferensial vergi güzəştləri tətbiq olunmalıdır; (3) Təhsil və səhiyyə işçilərinin baza maaşları illik inflyasiyaya avtomatik indeksləşdirilməlidir.", body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Publication-quality academic report saved to: {pdf_filename}")

if __name__ == '__main__':
    build_pdf()
