"""Mamlakatlar xaritasi (mamlakatlar.html) uchun maʼlumot. Faqat rasmiy manbalar.

Qoida (asoschi, 2026-11-16): xaritaga faqat davlat organi, xalqaro tashkilot (OECD),
stipendiya yoki taʼlim dasturi operatori va reyting tuzuvchisining oʻz sahifasidagi
raqam kiradi. Yangilik, blog va jamlovchi saytdagi raqam kirmaydi, rasmiy manba
topilguncha kutadi (roʻyxat: PENDING).

Matn ASCII apostrof bilan yoziladi, build_site.py uni uz() bilan oʻgiradi.
Har yozuv: (yoʻnalish, koʻrsatkich, qiymat, birlik, davr, manba nomi, havola, izoh).
qiymat: int yoki str ("52,46%" kabi). Hisoblangan raqam yozilmaydi.
"""
from __future__ import annotations

CHECKED = "17.11.2026"
ISO = "2026-11-17"

STAT_UZA = "https://uza.uz/ar/posts/ozbekistonliklar-eng-kop-qaysi-davlatlarga-oqish-maqsadida-safar-qilgan_818402"
STAT_NAME = "Milliy statistika qo'mitasi (O'zA orqali, 12.02.2026)"
QS = "https://www.topuniversities.com/world-university-rankings"
QS_NAME = "QS World University Rankings 2027"
OECD = "https://www.oecd.org/en/publications/international-students-in-higher-education_005ff28d-en/full-report/overview_61547f95.html"
OECD_NAME = "OECD (2026): International students in higher education"

CAMPUS_UZ = "https://ressources.campusfrance.org/publications/mobilite_pays/fr/ouzbekistan_fr.pdf"
KESS_UZ = "https://kess.kedi.re.kr/eng/post/6861900"

GROUPS = ["Ta'lim", "Qabul", "Stipendiya", "Moliya", "Viza", "Sifat"]


def flow(n: int) -> tuple:
    return ("Ta'lim", "2025-yilda O'zbekistondan o'qishga ketganlar", n, "kishi", "2025", STAT_NAME, STAT_UZA,
            "Bir yillik safarlar soni. Shu mamlakatda hozir o'qiyotgan o'zbeklar soni emas.")


COUNTRIES = {
    "UZB": dict(name="O'zbekiston", home=True, rows=[
        ("Ta'lim", "2025-yilda o'qish uchun chet elga chiqqanlar", 28954, "kishi", "2025", STAT_NAME, STAT_UZA,
         "2024-yilga nisbatan 19,3% kam. 35 ta davlatga. Bu safarlar soni."),
        ("Ta'lim", "Chet elda o'qiyotgan o'zbekistonlik talabalar", 150488, "kishi", "2022",
         "Campus France (UNESCO statistika instituti ma'lumoti)", CAMPUS_UZ,
         "Ko'pi: Qirg'iziston 51 605, Rossiya 48 430, Qozog'iston 26 130. Varaq 2024-yil oktabrda chiqqan."),
        ("Stipendiya", "Erasmus Mundus: O'zbekistondan tanlanganlar", 13, "kishi", "2026",
         "Yevropa Ittifoqining O'zbekistondagi vakolatxonasi",
         "https://www.eeas.europa.eu/delegations/uzbekistan/preparing-your-erasmus-mundus-journey-%E2%80%93-uzbekistan-2026_en",
         "7 nafari to'liq stipendiya bilan. 2015-yildan beri jami 154 kishi."),
    ]),
    "USA": dict(name="AQSh", lab="usa-lab.html", rows=[
        ("Ta'lim", "Xalqaro talabalar (OPT bilan)", 1177766, "kishi", "2024/25", "Open Doors 2025 (IIE, AQSh Davlat departamenti)",
         "https://opendoorsdata.org/wp-content/uploads/2025/11/OD25_Press-Release_EMBARGO.pdf",
         "883 513 nafari o'qiydi, 294 253 nafari OPT da ishlaydi."),
        ("Ta'lim", "O'zbekistonlik talabalar", 1310, "kishi", "2024/25", "Open Doors: Uzbekistan fact sheet",
         "https://opendoorsdata.org/wp-content/uploads/2026/01/OD_Uzbekistan_Fact-Sheet-2025.pdf",
         "787 bakalavr, 312 magistr va PhD, 189 OPT, 22 darajasiz. 2023/24: 1 219."),
        flow(351),
        ("Qabul", "Yangi xalqaro talabalar", 277118, "kishi", "kuz 2024", "Open Doors 2025 (IIE)",
         "https://www.iie.org/news/open-doors-2025-press-release/", "Oldingi yilga nisbatan 7% kam."),
        ("Viza", "B-viza rad etilishi: O'zbekiston fuqarolari", "52,46%", "", "FY2025", "AQSh Davlat departamenti",
         "https://travel.state.gov/content/dam/visas/Statistics/Non-Immigrant-Statistics/RefusalRates/FY25.pdf",
         "Bu mehmon (B1/B2) vizasi, talaba vizasi emas. F-1 bo'yicha mamlakat kesimi e'lon qilinmaydi."),
        ("Sifat", "QS reytingidagi universitetlar", 184, "universitet", "QS 2027", QS_NAME, QS,
         "Eng yuqori o'rin: MIT (1)."),
    ]),
    "GBR": dict(name="Buyuk Britaniya", rows=[
        ("Ta'lim", "Xalqaro talabalar (oliy ta'lim)", 748461, "kishi", "2023", OECD_NAME, OECD,
         "Barcha talabalarning 23%."),
        flow(886),
        ("Viza", "Berilgan talaba vizalari (sponsored study)", 383455, "viza", "iyul 2025 – iyun 2026", "UK Home Office",
         "https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2026/why-do-people-come-to-the-uk-study",
         "Oldingi yilga nisbatan 11% kam."),
        ("Moliya", "Viza uchun yashash puli: London", "£1 529 / oy", "", "2026", "GOV.UK", "https://www.gov.uk/student-visa/money",
         "Londondan tashqarida £1 171 / oy. 9 oygacha ko'rsatiladi."),
        ("Moliya", "Talaba vizasi to'lovi", "£558", "", "2026", "GOV.UK", "https://www.gov.uk/student-visa/money",
         "Tashqaridan ariza uchun. Sog'liqni saqlash yig'imi (IHS) alohida."),
        ("Sifat", "QS reytingidagi universitetlar", 93, "universitet", "QS 2027", QS_NAME, QS,
         "Eng yuqori o'rin: Imperial College London (2)."),
    ]),
    "DEU": dict(name="Germaniya", lab="daad-lab.html", rows=[
        ("Ta'lim", "Xalqaro talabalar va doktorantlar", "~402 000", "kishi", "qishki semestr 2024/25", "DAAD va DZHW: Wissenschaft weltoffen 2025",
         "https://www.daad.de/de/pressemitteilungen/2025/erneut-hohe-zahl-internationaler-studierender-in-deutschland/",
         "Manbada yaxlitlangan."),
        flow(391),
        ("Stipendiya", "DAAD qo'llab-quvvatlagan O'zbekiston fuqarolari", 452, "kishi", "2025", "DAAD: Usbekistan mamlakat varag'i",
         "https://www.daad.de/app/bsa/pdf/short/238/current/", "Barcha DAAD dasturlari, qisqa muddatlilari ham."),
        ("Moliya", "Viza uchun yashash puli", "992 € / oy", "", "2026", "Make it in Germany (Germaniya hukumati portali)",
         "https://www.make-it-in-germany.com/en/study-training/study/study-and-work/", "Odatda bloklangan hisobda (Sperrkonto) ko'rsatiladi."),
        ("Moliya", "O'qish to'lovi: Baden-Vyurtemberg", "1 500 € / semestr", "", "2026", "Heidelberg universiteti",
         "https://www.uni-heidelberg.de/de/studium/studienorganisation/beitraege-gebuehren/studiengebuehren-fuer-internationale-studierende",
         "Yevropa Ittifoqidan tashqaridagi talabalar uchun. Boshqa yerlarda davlat universitetlari odatda o'qish puli olmaydi."),
        ("Sifat", "QS: eng yuqori o'rindagi universitet", "25-o'rin", "", "QS 2027", QS_NAME, QS, "Myunxen texnika universiteti (TUM)."),
    ]),
    "FRA": dict(name="Fransiya", rows=[
        ("Ta'lim", "Xalqaro talabalar", 443500, "kishi", "2024/25", "Campus France",
         "https://www.campusfrance.org/system/files/medias/documents/2025-09/20250905_CP%20Rentree_CampusFrance.pdf",
         "Bir yilda 3%, besh yilda 17% o'sgan."),
        ("Ta'lim", "O'zbekistonlik talabalar", 165, "kishi", "2023/24", "Campus France: O'zbekiston varag'i", CAMPUS_UZ,
         "Fransiya Oliy ta'lim vazirligi (SIES) hisobi."),
        ("Moliya", "Davlat universitetida o'qish to'lovi: bakalavr (licence)", "2 895 € / yil", "", "2025/26", "Service-Public.fr",
         "https://www.service-public.gouv.fr/particuliers/actualites/A18927",
         "Master: 3 941 € / yil. 2026/27 dan imtiyozlar qisqartirildi, yangi summalar hali e'lon qilinmagan."),
        ("Sifat", "QS: eng yuqori o'rindagi universitet", "34-o'rin", "", "QS 2027", QS_NAME, QS, "Universite PSL."),
    ]),
    "ITA": dict(name="Italiya", rows=[
        ("Sifat", "QS: eng yuqori o'rindagi universitet", "87-o'rin", "", "QS 2027", QS_NAME, QS, "Milan politexnika universiteti."),
    ]),
    "NLD": dict(name="Niderlandiya", rows=[
        ("Ta'lim", "Xalqaro talabalar (daraja dasturlari)", 129764, "kishi", "2025/26", "Nuffic", "https://www.nuffic.nl/en/node/2102",
         "20 yilda birinchi marta kamaydi. 72% Yevropa iqtisodiy hududidan."),
        ("Qabul", "Yangi xalqaro talabalar", 48139, "kishi", "2025/26", "Nuffic", "https://www.nuffic.nl/en/node/1791", ""),
    ]),
    "KOR": dict(name="Janubiy Koreya", lab="gks-lab.html", rows=[
        ("Ta'lim", "Mamlakatdagi xalqaro talabalar (viza bo'yicha)", 308838, "kishi", "2025-yil oxiri", "Koreya Adliya vazirligi, immigratsiya statistikasi",
         "https://www.immigration.go.kr/moj/2412/subview.do", "Ta'lim vazirligi hisobi boshqacha usulda va boshqa sanada olinadi."),
        ("Ta'lim", "Daraja dasturidagi xorijiy talabalar: o'zbeklar ulushi", "8,0%", "", "2025", "KEDI (Koreya Ta'lim vazirligi statistikasi)", KESS_UZ,
         "Xitoy va Vetnamdan keyin 3-o'rin."),
        flow(3513),
        ("Qabul", "Yangi qabul qilingan xalqaro talabalar (D-2)", 117333, "kishi", "2025", "Koreya Adliya vazirligi",
         "https://www.moj.go.kr/bbs/moj/182/499104/download.do", "2019-yilga nisbatan 75% ko'p."),
        ("Stipendiya", "GKS magistratura/PhD: O'zbekiston elchixona kvotasi", 13, "o'rin", "2026", "NIIED: 2026 GKS-G yo'riqnomasi",
         "https://www.esteri.it/wp-content/uploads/2026/02/2026-GKS-G-Application-Guidelines-English.pdf",
         "Yana: xorijdagi koreyslar uchun 6, universitet yo'li 12. Dunyo bo'yicha jami 2 000."),
    ]),
    "JPN": dict(name="Yaponiya", rows=[
        ("Ta'lim", "Xalqaro talabalar (til maktablari bilan)", 408069, "kishi", "1.05.2025", "JASSO",
         "https://www.studyinjapan.go.jp/ja/statistics/enrollment/data/2605291000.html",
         "Oliy ta'limda 267 895, til maktablarida 140 174."),
        ("Ta'lim", "O'zbekistonlik talabalar", 2519, "kishi", "1.05.2025", "JASSO",
         "https://www.studyinjapan.go.jp/ja/_mt/2026/05/data2025z.pdf", "2024-yilda 2 844 edi."),
        ("Stipendiya", "MEXT (hukumat) stipendiatlari, jami", 9221, "kishi", "2025", "JASSO",
         "https://www.studyinjapan.go.jp/ja/_mt/2026/05/data2025z.pdf", "O'zbekiston kvotasi alohida e'lon qilinmaydi."),
    ]),
    "SGP": dict(name="Singapur", point=(1.35, 103.82), rows=[
        ("Sifat", "QS: eng yuqori o'rindagi universitet", "10-o'rin", "", "QS 2027", QS_NAME, QS, "Singapur milliy universiteti (NUS)."),
    ]),
    "AUS": dict(name="Avstraliya", rows=[
        ("Ta'lim", "Xalqaro talabalar (oliy ta'lim)", 467074, "kishi", "2023", OECD_NAME, OECD, "Barcha talabalarning 27%."),
        ("Sifat", "QS: eng yuqori o'rindagi universitet", "19-o'rin", "", "QS 2027", QS_NAME, QS, "Yangi Janubiy Uels universiteti (UNSW)."),
    ]),
    "CAN": dict(name="Kanada", rows=[
        ("Ta'lim", "Xalqaro talabalar (oliy ta'lim)", 389181, "kishi", "2023", OECD_NAME, OECD, ""),
        ("Viza", "Yangi berilgan talaba ruxsatnomalari (study permit)", 115470, "ruxsatnoma", "2025", OECD_NAME, OECD,
         "2024-yilda 293 060 edi."),
        ("Viza", "Talaba ruxsatnomasi rad etilishi (barcha davlatlar)", "58%", "", "yanvar–avgust 2025", "IRCC",
         "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/transparency/committees/cimm-oct-21-2025/international-students.html",
         "2024-yil shu davrda 48% edi. O'zbekiston kesimi berilmagan."),
        ("Moliya", "Viza uchun yashash puli (Kvebekdan tashqari)", "23 448 CAD / yil", "", "1.09.2026 dan", "IRCC",
         "https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/get-documents/financial-support.html",
         "O'qish puli va yo'l xarajati bunga kirmaydi."),
        ("Moliya", "O'rtacha o'qish to'lovi: xalqaro bakalavr", "41 746 CAD / yil", "", "2025/26", "Statistics Canada",
         "https://www150.statcan.gc.ca/n1/daily-quotidien/250910/dq250910d-eng.htm", "Magistratura: 24 028 CAD / yil."),
        ("Sifat", "QS: eng yuqori o'rindagi universitet", "30-o'rin", "", "QS 2027", QS_NAME, QS, "McGill universiteti."),
    ]),
    "CHN": dict(name="Xitoy", rows=[
        ("Ta'lim", "Xalqaro talabalar", 492185, "kishi", "2018", "Xitoy Ta'lim vazirligi",
         "http://www.moe.edu.cn/jyb_xwfb/gzdt_gzdt/s5987/201904/t20190412_377692.html",
         "2018-yildan keyin yangi umumiy son e'lon qilinmagan."),
        flow(1259),
        ("Sifat", "QS reytingidagi universitetlar", 85, "universitet", "QS 2027", QS_NAME, QS, "Eng yuqori o'rin: Pekin universiteti (13)."),
    ]),
}

# 2-qatlam: 2025-yilda O'zbekistondan o'qishga ketganlar, top-10 (bitta manba)
FLOWS = {"RUS": ("Rossiya", 6498), "TJK": ("Tojikiston", 6039), "KGZ": ("Qirg'iziston", 4648), "KOR": ("Janubiy Koreya", 3513),
         "TUR": ("Turkiya", 2496), "CHN": ("Xitoy", 1259), "KAZ": ("Qozog'iston", 1097), "GBR": ("Buyuk Britaniya", 886),
         "DEU": ("Germaniya", 391), "USA": ("AQSh", 351)}

# Rasmiy manba topilmagani uchun hozircha kiritilmagan (faqat yangilik yoki jamlovchi saytda bor)
PENDING = [
    "El-yurt umidi 2026/27 kvotalari (eyuf.uz)",
    "Buyuk Britaniyadagi o'zbek talabalar (HESA, 28-jadval)",
    "Italiya, Niderlandiya, Kanada, Avstraliyadagi o'zbek talabalar",
    "Viza rad etilishi: O'zbekiston kesimi (UK Vis_D02, Avstraliya BP0015)",
]

# ---------------------------------------------------------------- xarita qatlamlari
# Xarita ustidagi doira va yorliq joyi (taxminiy markaz, kenglik, uzunlik)
ANCHORS = {"UZB": (41.3, 64.5), "USA": (39.5, -98.5), "GBR": (53.5, -2.0), "DEU": (51.0, 10.3), "FRA": (46.6, 2.4),
           "ITA": (42.8, 12.6), "NLD": (52.2, 5.6), "KOR": (36.4, 127.9), "JPN": (36.6, 138.6), "SGP": (1.35, 103.82),
           "AUS": (-25.5, 134.0), "CAN": (57.0, -103.0), "CHN": (34.5, 103.5), "RUS": (61.0, 96.0), "TJK": (38.8, 71.2),
           "KGZ": (41.5, 74.7), "TUR": (39.0, 35.2), "KAZ": (48.2, 67.0)}

# "Xalqaro talabalar" qatlami: COUNTRIES dagi qator bilan bir xil raqam (yil va taʼrif har xil, kartada aniq yoziladi)
STUDENTS = {"USA": (1177766, "2024/25"), "GBR": (748461, "2023"), "CHN": (492185, "2018"), "AUS": (467074, "2023"),
            "FRA": (443500, "2024/25"), "JPN": (408069, "2025"), "DEU": (402000, "2024/25"), "CAN": (389181, "2023"),
            "KOR": (308838, "2025"), "NLD": (129764, "2025/26")}

# "QS eng yaxshi o'rin" qatlami (QS 2027, COUNTRIES dagi Sifat qatori bilan bir xil)
QS_TOP = {"USA": (1, "MIT"), "GBR": (2, "Imperial College London"), "SGP": (10, "NUS"), "CHN": (13, "Pekin universiteti"),
          "AUS": (19, "UNSW"), "DEU": (25, "TUM"), "CAN": (30, "McGill"), "FRA": (34, "Universite PSL"),
          "ITA": (87, "Milan politexnika universiteti")}

# Bo'lim ikonkalari: img/3d/<nom>.webp (saytdagi to'plam)
ICONS = {"Ta'lim": "books", "Qabul": "memo", "Stipendiya": "scroll", "Moliya": "money", "Viza": "shield", "Sifat": "chart"}
