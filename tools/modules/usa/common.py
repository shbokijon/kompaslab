# USA Lab M1–M8: umumiy manba havolalari. Tekshirildi: 2026-10-31.
# Qoida (2026-10-31): manbalar faqat universitetlar va masʼul tashkilotlar (AQSh Davlat departamenti,
# elchixona, DHS/ICE, Taʼlim vazirligi, NSF, College Board, CGS, CHEA, Carnegie/ACE) sahifalari.
# Blog, agentlik, reyting yigʻuvchi va yangilik saytlari manba sifatida ishlatilmaydi.
# Matnda oddiy apostrof (') yoziladi; engine.fix() uni U+02BB / U+02BC ga aylantiradi.
def a(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


DATE = "31.10.2026"
HOL = f"{DATE} holatiga"
STD = f"Faktlar {HOL}; har sikl rasmiy sahifadan qayta tekshiring. Muddat, toʻlov, summa va siyosatlar har yili oʻzgaradi."

# AQSh Davlat departamenti va elchixona
EMB_UGRAD = a("https://uz.usembassy.gov/global-undergraduate-exchange-program/", "AQSh elchixonasi (Toshkent): Global UGRAD")
EMB_FUL = a("https://uz.usembassy.gov/fulbright-foreign-student-program/", "AQSh elchixonasi (Toshkent): Fulbright Foreign Student Program")
EMB_FUL_EXP = a("https://uz.usembassy.gov/us-and-uz-expand-fulbright-program-to-build-workforce-for-critical-minerals-energy-and-advanced-technology-sectors/", "AQSh elchixonasi: Fulbright dasturini kengaytirish eʼloni (05.06.2026)")
EMB_EXCH = a("https://uz.usembassy.gov/exchange-programs/", "AQSh elchixonasi: almashinuv dasturlari roʻyxati")
EMB_VISA = a("https://uz.usembassy.gov/applying-for-a-visa/", "AQSh elchixonasi: vizaga ariza berish")
EMB_DOCS = a("https://uz.usembassy.gov/required-documents/", "AQSh elchixonasi: talab qilinadigan hujjatlar")
UGRAD_WL = a("https://www.globalugrad.org/overview-host-eligibility/", "Global UGRAD (World Learning, Davlat departamenti dasturi)")
FUL_IIE = a("https://foreign.fulbrightonline.org/about/foreign-student-program", "Fulbright Foreign Student Program (IIE)")
DOS_VISA = a("https://travel.state.gov/content/travel/en/us-visas/study/student-visa.html", "AQSh Davlat departamenti: talaba vizasi")
DOS_WAIVER = a("https://travel.state.gov/content/travel/en/us-visas/study/exchange/waiver-of-the-exchange-visitor.html", "AQSh Davlat departamenti: J-1 2 yillik talabidan ozod qilish")
DS160 = a("https://ceac.state.gov/genniv/", "DS-160 onlayn formasi (CEAC)")
EDUSA_UG = a("https://educationusa.state.gov/your-5-steps-us-study/finance-your-studies/undergraduate", "EducationUSA: bakalavriatni moliyalashtirish")
EDUSA_GR = a("https://educationusa.state.gov/your-5-steps-us-study/finance-your-studies/graduate", "EducationUSA: magistratura va doktoranturani moliyalashtirish")
EDUSA_FIND = a("https://educationusa.state.gov/find-advising-center", "EducationUSA: maslahat markazini topish")

# DHS / ICE
SITS_SEARCH = a("https://studyinthestates.dhs.gov/school-search", "Study in the States (DHS): SEVP sertifikatli maktablar qidiruvi")
SEVIS = a("https://www.ice.gov/sevis/i901", "ICE: SEVIS I-901 toʻlovi")

# Taʼlim vazirligi, NSF, akkreditatsiya, tasnif
ED_AID = a("https://awsfinancialaidtoolkit.ed.gov/tk/outreach/target/noncitizens.jsp", "AQSh Taʼlim vazirligi: fuqaro boʻlmaganlar va federal yordam")
NPC = a("https://collegecost.ed.gov/net-price", "AQSh Taʼlim vazirligi: Net Price Calculator markazi")
NAV = a("https://nces.ed.gov/collegenavigator/", "College Navigator (NCES, AQSh Taʼlim vazirligi)")
CHEA = a("https://www.chea.org/about-accreditation", "CHEA: akkreditatsiya haqida va bazasi")
DAPIP = a("https://ope.ed.gov/dapip/", "AQSh Taʼlim vazirligi: akkreditatsiyalangan muassasalar bazasi (DAPIP)")
CARNEGIE = a("https://carnegieclassifications.acenet.edu/news/carnegie-classifications-release-2025-research-activity-designations-debut-updated-methodology/", "Carnegie tasnifi (ACE): 2025 tadqiqot darajalari")
HERD = a("https://ncses.nsf.gov/surveys/higher-education-research-development/", "NSF NCSES: HERD soʻrovi (soha boʻyicha ilmiy xarajat)")
NSF_GRFP = a("https://undergraduates.utexas.edu/odps/explore/nsf-grfp", "Texas universiteti (Ostin): NSF GRFP muvofiqligi")
CGS = a("https://cgsnet.org/resources/for-current-prospective-graduate-students/april-15-resolution/", "CGS (Council of Graduate Schools): 15-aprel qarori")

# College Board, CDS
CSS = a("https://cssprofile.collegeboard.org", "CSS Profile (College Board)")
CSS_INT = a("https://cssprofile.collegeboard.org/frequently-asked-questions/international", "CSS Profile: xalqaro abituriyentlar uchun savollar")
CDS = a("https://commondataset.org", "Common Data Set loyihasi")
CDS_H6 = a("https://iea.unl.edu/common-data-set-2025-2026/h-financial-aid/aid-undergraduate-degree-seeking-nonresidents", "Nebraska universiteti: CDS 2025–2026, H6 bandi (namuna)")

# Universitetlar (namuna sifatida; har biri oʻz rasmiy sahifasi)
HARVARD = a("https://college.harvard.edu/financial-aid/how-aid-works", "Harvard College: yordam qanday ishlaydi")
PRINCETON = a("https://admission.princeton.edu/cost-aid", "Princeton: xarajat va yordam")
MIT = a("https://sfs.mit.edu/financial-aid-mit", "MIT Student Financial Services")
DARTMOUTH = a("https://financialaid.dartmouth.edu/apply-aid/international-students", "Dartmouth: xalqaro talabalar uchun yordam")
NORTHWESTERN = a("https://undergradaid.northwestern.edu/apply-for-aid/prospective-students/international-students-application-instructions.html", "Northwestern: xalqaro abituriyentlar uchun yordam arizasi")
OSU = a("https://sfa.osu.edu/international-student/about-aid", "Ohio State: xalqaro talabalar va moliyaviy yordam")
DUKE = a("https://gradschool.duke.edu/financial-support/phd-financial-support/", "Duke Graduate School: PhD kafolatlangan moliyalashtirish")
BU = a("https://www.bu.edu/earth/phd-funding", "Boston universiteti, Earth & Environment: PhD moliyalashtirish")
PRINCETON_MS = a("https://gradschool.princeton.edu/financial-support/financial-support-model/master%E2%80%99s-degree-funding", "Princeton Graduate School: magistratura moliyalashtirishi")
BUFFALO = a("https://www.buffalo.edu/grad/explore/funding/masters-level-funding.html", "Buffalo universiteti: magistratura darajasida moliyalashtirish")
GMU = a("https://oips.gmu.edu/f-1-employment/", "George Mason universiteti (OIPS): F-1 ishlash qoidalari")
HARVARD_212E = a("https://www.hio.harvard.edu/node/127", "Harvard International Office: 212(e) 2 yillik talab")
BROWN_TB = a("https://isss.brown.edu/traveling/current-travel-and-visa-restrictions-presidential-proclamation", "Brown universiteti ISSS: prezident proklamatsiyalari boʻyicha cheklovlar")
MIT_VET = a("https://iso.mit.edu/news/student-and-scholar-f-j-m-visa-interviews-to-resume-with-new-vetting-procedures", "MIT ISO: F, J, M vizalari uchun kengaytirilgan tekshiruv (2025-iyun)")
SJSU = a("https://sjsu.edu/admissions/internationalfinancialdocs.php", "San José State universiteti: I-20 uchun moliyaviy hujjatlar")
KSU = a("https://campus.kennesaw.edu/current-students/academics/global-education/international-student-scholar-services/f-1/cost-to-attend.php", "Kennesaw State universiteti: bir yillik taxminiy xarajat (I-20)")
