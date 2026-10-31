# Bachelor Lab M1–M16: umumiy manba havolalari. Tekshirildi: 2026-10-31.
# Matnda oddiy apostrof (') yoziladi; engine.fix() uni U+02BB / U+02BC ga aylantiradi.
def a(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


DATE = "31.10.2026"
HOL = f"{DATE} holatiga"

# Platformalar
CA = a("https://www.commonapp.org", "Common App (rasmiy sayt)")
CA_ESSAY = a("https://www.commonapp.org/apply/essay-prompts", "Common App: insho mavzulari")
CA_FRAUD = a("https://www.commonapp.org/fraud-policy/", "Common App: firibgarlik siyosati (Fraud Policy)")
CA_FEE = a("https://www.commonapp.org/help-center", "Common App yordam markazi")
UCAS = a("https://www.ucas.com", "UCAS (rasmiy sayt)")
UCAS_PS = a("https://www.ucas.com/applying/applying-to-university/writing-personal-statement/personal-statement-dos-and-donts", "UCAS: shaxsiy bayonot, 2026 qabulidan")
UCAS_AI = a("https://www.ucas.com/applying/applying-to-university/writing-your-personal-statement/a-guide-to-using-ai-and-chatgpt-with-your-personal-statement", "UCAS: shaxsiy bayonotda AI va ChatGPT dan foydalanish")
UCAS_SIM = a("https://www.ucas.com/sites/default/files/similarity-detection-applicant-guide.pdf", "UCAS: oʻxshashlikni aniqlash xizmati, abituriyent uchun qoʻllanma")
UCAS_DATES = a("https://www.ucas.com/undergraduate/applying-to-university/when-to-apply-and-key-dates", "UCAS: ariza muddatlari")
UCAS_INT = a("https://www.ucas.com/international", "UCAS: xalqaro abituriyentlar")
THE_PS = a("https://www.timeshighereducation.com/counsellor/admissions-processes-and-funding/guide-2026-changes-ucas-personal-statement", "Times Higher Education: 2026 UCAS bayonoti oʻzgarishlari")
UNIASSIST = a("https://www.uni-assist.de/en/", "uni-assist (Germaniya)")
ANABIN = a("https://anabin.kmk.org", "anabin (KMK, xorijiy hujjatlarni baholash bazasi)")
DAAD_ADM = a("https://www.daad.de/en/studying-in-germany/requirements/", "DAAD: Germaniyada oʻqishga kirish talablari")
UNIVERSITALY = a("https://www.universitaly.it", "Universitaly portali")
UNIPI = a("https://www.unipi.it/en/education/registration/enrolment-and-registration/enrolment-for-international-students/pre-registration-on-universitaly/", "Pisa universiteti: Universitaly orqali oldindan roʻyxatdan oʻtish (2026/27)")
SIK = a("https://www.studyinkorea.go.kr", "Study in Korea (NIIED)")
CAMPUSCHINA = a("https://www.campuschina.org", "Campus China (CSC rasmiy portali)")
SIC = a("https://www.studyinchina.edu.cn", "Study in China (Xitoy Taʼlim vazirligi)")
SH = a("https://stipendiumhungaricum.hu", "Stipendium Hungaricum (Tempus jamgʻarmasi)")
SH_UZ = a("https://gov.uz/en/edu/news/view/32547", "gov.uz: Oliy taʼlim vazirligi, Stipendium Hungaricum eʼloni (25.12.2024)")
TB = a("https://www.turkiyeburslari.gov.tr", "Türkiye Bursları (rasmiy sayt)")
MEXT = a("https://www.studyinjapan.go.jp/en/smap-stopj-applications-scholarship.html", "Study in Japan: MEXT stipendiyasi")
NUS = a("https://www.nus.edu.sg/oam", "NUS qabul boʻlimi (OAM)")
NTU = a("https://www.ntu.edu.sg/admissions/undergraduate", "NTU bakalavriat qabuli")
MOE_SG = a("https://www.moe.gov.sg/financial-matters/tuition-grant-scheme", "Singapur MOE: Tuition Grant")
CSS = a("https://cssprofile.collegeboard.org", "CSS Profile (College Board)")
CDS = a("https://commondataset.org", "Common Data Set loyihasi")
SAT = a("https://satsuite.collegeboard.org/sat", "SAT (College Board)")
ACT = a("https://www.act.org", "ACT (rasmiy sayt)")
IELTS = a("https://ielts.org", "IELTS (rasmiy sayt)")
TOEFL = a("https://www.ets.org/toefl.html", "TOEFL (ETS)")
DET = a("https://englishtest.duolingo.com", "Duolingo English Test")
QS = a("https://support.qs.com/hc/en-gb/articles/4405955370898-QS-World-University-Rankings", "QS metodologiyasi")
THE = a("https://www.timeshighereducation.com/world-university-rankings/world-university-rankings-2026-methodology", "THE metodologiyasi")
USN = a("https://www.usnews.com/education/best-colleges/articles/how-us-news-calculated-the-rankings", "US News metodologiyasi")
APO = a("https://gov.uz/oz/advice/72/document/2620", "gov.uz: rasmiy hujjatlarga apostil qoʻyish")
MYGOV = a("https://my.gov.uz", "my.gov.uz (Yagona interaktiv davlat xizmatlari portali)")
# Viza va joʻnash
US_VISA = a("https://travel.state.gov/content/travel/en/us-visas/study/student-visa.html", "AQSh Davlat departamenti: talaba vizasi")
US_SEVIS = a("https://www.ice.gov/sevis/i901", "SEVIS I-901 toʻlovi (ICE)")
UK_VISA = a("https://www.gov.uk/student-visa", "GOV.UK: Student visa")
DE_VISA = a("https://www.auswaertiges-amt.de/en/visa-service", "Germaniya Tashqi ishlar vazirligi: viza xizmati")
IT_VISA = a("https://vistoperitalia.esteri.it", "Italiya: Visto per l'Italia")
KR_VISA = a("https://www.visa.go.kr", "Koreya Hi Korea / visa portali")
DSU = a("https://www.studiare-in-italia.it", "Study in Italy (Italiya Tashqi ishlar vazirligi portali)")
FTC = a("https://www.ftc.gov/business-guidance/resources/scholarship-scams", "FTC (AQSh): stipendiya firibgarligi belgilari")

STD = f"Faktlar {HOL}; har sikl rasmiy sahifadan qayta tekshiring. Muddat, toʻlov va kvotalar har yili oʻzgaradi."
