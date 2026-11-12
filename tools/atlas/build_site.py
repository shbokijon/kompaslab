#!/usr/bin/env python3
"""Kompas Atlas sahifalarini yigʻadi (qoʻlda tahrirlanmaydi, shu faylni oʻzgartiring).

Natija (repo ildizida):
  atlas.html                       — Atlas bosh sahifasi: O'qish + Ish yo'llari
  atlas-professorga-xat.html       — maqola
  atlas-talaba-ishi.html           — maqola (8 mamlakat)
  atlas-ingliz-tili-testi.html     — maqola
  nl-sponsors.html, ca-lmia.html   — rasmiy registr nusxasidan qidiruv (js/atlas-registry.js)

Ishga tushirish: python3 tools/atlas/build_site.py
Maʼlumot: data/nl-sponsors.json, data/ca-lmia.json (.github/workflows/atlas-data.yml yangilaydi).
Faktlar "… holatiga" sanasi bilan; mamlakat qoidasi oʻzgarsa, CHECKED va matnni yangilang.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "site"))
from shell import FOOTER, head, nav, page, pagehead, uz  # noqa: E402

CHECKED = "30.10.2026"
ISO = "2026-10-30"

LABS = {
    "musofir": ('musofir-lab-m0.html', "Musofir Lab M0"),
    "master": ("master-lab-m0.html", "Master Lab M0"),
    "phd": ("phd-lab-m0.html", "PhD Lab M0"),
    "bachelor": ("bachelor-lab-m0.html", "Bachelor Lab M0"),
    "daad": ("daad-lab-m0.html", "DAAD Lab M0"),
    "gks": ("gks-lab-m0.html", "GKS Lab M0"),
    "usa": ("usa-lab-m0.html", "USA Lab M0"),
    "reja": ("master-planner.html", "Bepul reja"),
}


def lab_links(*keys: str) -> str:
    return '<div class="at-labs">' + "".join(f'<a href="{LABS[k][0]}">{LABS[k][1]}</a>' for k in keys) + "</div>"


# Sotuvdagi Lablar (tools/landing/labs_data.ON_SALE bilan bir xil): maqola oxirida narx sahifasiga havola.
# Narx raqami yozilmaydi: yagona manba bazadagi courses jadvali.
SALE = {"master": ("master-lab-narxlar.html", "Master Lab"), "phd": ("phd-lab-narxlar.html", "PhD Lab"),
        "bachelor": ("bachelor-lab-narxlar.html", "Bachelor Lab"), "gks": ("gks-lab-narxlar.html", "GKS Lab"),
        "usa": ("usa-lab-narxlar.html", "USA Lab")}


def sale_links(*keys: str) -> str:
    ks = [k for k in keys if k in SALE]
    if not ks:
        return ""
    links = "".join(f'<a href="{SALE[k][0]}">{SALE[k][1]}: narx va obuna</a>' for k in ks)
    return f'<p style="margin-top:14px">To\'liq dastur obuna bilan ochiladi: oylik tarif bitta bosqichni, 6 oylik hammasini.</p><div class="at-labs">{links}</div>'


def ext(url: str, label: str, lang: str = "") -> str:
    la = f' lang="{lang}"' if lang else ""
    return f'<a href="{url}" target="_blank" rel="noopener"{la}>{label}</a>'


# ---------------------------------------------------------------- maqolalar
ARTICLES = [
    dict(
        slug="atlas-professorga-xat",
        kind="O'qish · PhD, Master, DAAD",
        title="Professorga dastlabki xat (Cold email): 5 ta keng tarqalgan xato",
        card="Bir xil xatni o'nlab professorga yuborish, \"Dear Sir/Madam\" va birinchi xatdayoq stipendiya so'rash. Nimadan qochish va xat qanday tuzilishi.",
        desc="Professorga dastlabki xatda (cold email) ko'p uchraydigan 5 ta xato va xat tuzilmasi. DAAD va universitet tavsiyalari asosida, o'zbek tilida.",
        labs=("phd", "master", "daad", "gks"),
        body=f"""
<p class="at-short"><b>Qisqa javob.</b> Professor xatni bir necha soniyada baholaydi: u sizga aniq yozilganmi, uning tadqiqoti bilan nima bog'lab turibdi va sizdan nima so'ralyapti. Quyidagi besh xato shu uch savolning birortasiga javob bermaydi.</p>

<h2>1. Umumiy murojaat</h2>
<p><span lang="en">"Dear Sir/Madam"</span> yoki <span lang="en">"Dear Professor"</span> deb familiyasiz boshlash xat ko'pchilikka yuborilganini darhol ko'rsatadi. DAAD qo'llanmasi professorga ismi bilan murojaat qilishni va shaxssiz murojaatdan qochishni tavsiya qiladi. <span lang="en">Saskatchewan</span> universiteti ham unvon va familiyani yozishni maslahat beradi (masalan, <span lang="en">"Dear Dr. Smith"</span>).</p>

<h2>2. Bitta xatni ko'p professorga yuborish</h2>
<p>DAAD qo'llanmasi bir xil xatni bir nechta odamga yubormaslikni alohida ta'kidlaydi. Har xatda shu professorning aniq ishi tilga olinishi kerak: maqola, loyiha yoki laboratoriya yo'nalishi. 10 ta puxta xat 100 ta bir xil xatdan foydaliroq.</p>

<h2>3. Umumiy maqtov, ilmiy moslik (Research fit) yo'q</h2>
<p><span lang="en">"You are a world-renowned scientist"</span> kabi gaplar hech narsa demaydi. DAAD yozishicha, xatda umumiy tadqiqot yo'nalishingizni nomlash kerak, maqtov emas. Bitta gap yetadi: uning qaysi ishi sizning qaysi tajribangiz yoki savolingiz bilan bog'liq.</p>

<h2>4. Juda uzun xat</h2>
<p><span lang="en">Saskatchewan</span> universiteti xatni taxminan uch abzats va 250 so'zdan qisqa yozishni tavsiya qiladi: siz kimsiz (2–3 gap), nega aynan u, va aniq so'rov. Batafsil ma'lumot CV va qisqa tadqiqot g'oyasida beriladi (ilova sifatida).</p>

<h2>5. Birinchi xatdayoq pul so'rash</h2>
<p>DAAD birinchi xatda moliyalashtirish so'ramaslikni maslahat beradi: birinchi xat faqat aloqa o'rnatadi va professor mavzuga qiziqadimi, shuni bilish uchun yoziladi. Stipendiya imkoniyatlari keyingi suhbatda yoki dastur sahifasidan aniqlanadi.</p>

<h2>Xat tuzilmasi</h2>
<div class="at-sample"><b>Kompas tuzgan namuna (andoza, nusxa ko'chirish uchun emas)</b>
<ol>
<li><b>Mavzu qatori:</b> dastur yoki yo'nalish + sizning qiziqishingiz (masalan, "Prospective PhD student: [mavzu]").</li>
<li><b>Kimsiz:</b> daraja, universitet, asosiy natija (1–2 gap).</li>
<li><b>Moslik:</b> uning aniq ishi va sizning tajribangiz yoki savolingiz o'rtasidagi bog'liqlik (2–3 gap).</li>
<li><b>So'rov:</b> u shu dastur va muddat uchun nomzodlarni qabul qiladimi (1 gap).</li>
<li><b>Ilova:</b> CV va 1 sahifalik tadqiqot g'oyasi.</li>
</ol></div>
<p>Xatni yuborishdan oldin imloni tekshiring: DAAD qo'llanmasi kichik xatolar ham akademik standart haqidagi taassurotni buzishini yozadi.</p>

<h2>Javob kelmasa</h2>
<p>DAAD javob kelmasa tushkunlikka tushmaslikni yozadi: professorlar band va asosan qiziqarli taklif bilan kelgan, o'zlari rahbarlik qila oladigan nomzodlarga javob beradi. <b>Kompas tavsiyasi (rasmiy qoida emas):</b> 1–2 hafta kutib, bitta qisqa eslatma yuboring, keyin ro'yxatdagi keyingi professorga o'ting.</p>
""",
        sources=[
            ("https://www2.daad.de/medien/deutschland/stipendien/formulare/gerss-how-to-find-a-phd-supervisor.pdf", "DAAD: How to Find a German PhD Supervisor or Research Partner (PDF)"),
            ("https://grad.usask.ca/admissions/tips-for-finding-a-supervisor.php", "University of Saskatchewan: Tips for finding a supervisor"),
            ("https://www.findaphd.com/advice/finding/contacting-phd-supervisors.aspx", "FindAPhD: Contacting PhD supervisors"),
        ],
    ),
    dict(
        slug="atlas-talaba-ishi",
        kind="O'qish · 8 mamlakat",
        title=f"Talaba vizasida ishlash: 8 mamlakat qoidalari ({CHECKED} holatiga)",
        card="Buyuk Britaniya, Germaniya, Niderlandiya, Kanada, AQSh, Yaponiya, Polsha va Koreya: o'qish davrida haftasiga necha soat ishlash mumkin va qanday shartlar bilan.",
        desc="Talaba vizasida ishlash qoidalari: Buyuk Britaniya, Germaniya, Niderlandiya, Kanada, AQSh, Yaponiya, Polsha va Janubiy Koreya. Rasmiy manbalar bilan, 30.10.2026 holatiga.",
        labs=("master", "usa", "bachelor", "musofir", "reja"),
        body=f"""
<p class="at-short"><b>Qisqa javob.</b> Ko'p mamlakatda talaba o'qish davrida qisman, ta'tilda ko'proq ishlay oladi. Lekin limit soatda, kunda yoki ruxsatnomada belgilanadi va har mamlakatda boshqacha. Quyidagi jadval {CHECKED} holatiga rasmiy yoki universitet sahifalaridan olingan. Topshirishdan oldin har birini qayta tekshiring.</p>

<div class="at-tablewrap"><table>
<thead><tr><th>Mamlakat</th><th>O'qish davrida</th><th>Ta'tilda</th><th>Muhim shart</th></tr></thead>
<tbody>
<tr><td>Buyuk Britaniya (Student visa)</td><td>Bakalavr va undan yuqori: haftasiga 20 soatgacha. Bakalavrdan past: 10 soatgacha</td><td>To'liq kun</td><td>O'zini o'zi band qilish (freelance) mumkin emas. Sirtqi (part-time) magistrlar umuman ishlay olmaydi</td></tr>
<tr><td>Germaniya</td><td>Yiliga 140 to'liq yoki 280 yarim kun; yoki semestrda haftasiga 20 soatgacha</td><td>Cheklov yo'q (rasmiy sahifa bo'yicha)</td><td>Universitetdagi ilmiy yordamchi ishi bu limitga kirmaydi. O'zini o'zi band qilishga xorijliklar idorasi ruxsati kerak</td></tr>
<tr><td>Niderlandiya</td><td>Yil bo'yi haftasiga 16 soatgacha</td><td>Yoki iyun–avgustda mavsumiy ish (to'liq kun ham)</td><td>Yiliga ikkisidan bittasi tanlanadi. Ish beruvchi ish ruxsatnomasi (TWV) olishi kerak</td></tr>
<tr><td>Kanada</td><td>Kampusdan tashqarida haftasiga 24 soatgacha</td><td>Rejali ta'tillarda cheklovsiz</td><td>Ruxsatnoma shartlariga mos bo'lish kerak; ta'tili yo'q dasturda 24 soat limiti qoladi</td></tr>
<tr><td>AQSh (F-1)</td><td>Kampus ichida haftasiga 20 soatgacha</td><td>Kampus ichida ko'proq</td><td>Kampusdan tashqari ish faqat CPT yoki OPT ruxsati bilan. OPT kamida bir o'quv yilidan keyin, 12 oygacha</td></tr>
<tr><td>Yaponiya</td><td>Ruxsat bilan haftasiga 28 soatgacha</td><td>Uzun ta'tilda kuniga 8 soatgacha</td><td>Ishlashdan oldin immigratsiya idorasidan qo'shimcha faoliyat ruxsati olinadi</td></tr>
<tr><td>Polsha</td><td>Rasmiy sahifada soat limiti ko'rsatilmagan</td><td>—</td><td>O'qish vizasi yoki o'qish uchun vaqtinchalik yashash ruxsati bilan ish ruxsatnomasisiz ishlash mumkin (sahifadagi shartlar bilan)</td></tr>
<tr><td>Janubiy Koreya (D-2)</td><td>Limit daraja, koreys tili darajasi va universitetga bog'liq</td><td>—</td><td>Ishlash faqat immigratsiya ruxsati bilan. Aniq soatni universitet xalqaro bo'limi va HiKorea dan tekshiring</td></tr>
</tbody></table></div>
<p class="at-meta">Koreya uchun aniq raqam yozilmadi: qoida tafsilotlari bir-biriga zid manbalarda turlicha keltirilgan va rasmiy sahifani biz to'liq tekshira olmadik.</p>

<h2>Ish xarajatni to'liq qoplamaydi</h2>
<p>Viza uchun odatda ishga emas, oldindan bor pulga qaraladi. Masalan, Make it in Germany sahifasida 2026 yil uchun talaba oyiga 992 yevro mablag'ini isbotlashi kerakligi yozilgan. Qisman ish xarajatning bir qismini qoplashi mumkin, lekin reja undan boshlanmasligi kerak.</p>

<h2>Qoidani buzish xavfi</h2>
<p>Ish sharti viza shartining bir qismi. UKCISA ish beruvchi taklif qilgan "contractor" yoki "freelance" kelishuvlari ham shartni buzishi mumkinligini ogohlantiradi. Shubha bo'lsa, universitetingiz xalqaro talabalar bo'limidan so'rang.</p>
""",
        sources=[
            ("https://ukcisa.org.uk/student-advice/working/student-work/", "UKCISA: Student work (28.01.2026 yangilangan)"),
            ("https://www.gov.uk/student-visa/what-you-can-and-cannot-do", "GOV.UK: Student visa, what you can and cannot do"),
            ("https://www.make-it-in-germany.com/en/study-training/study/study-and-work/", "Make it in Germany: Study and work"),
            ("https://www.uva.nl/en/education/practical-information/working-in-the-netherlands/work-and-internship-during-your-studies", "Universiteit van Amsterdam: Work and internship during your studies"),
            ("https://ind.nl/en", "IND (Niderlandiya immigratsiya xizmati)"),
            ("https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/work-off-campus.html", "IRCC: Work off campus (15.04.2026 yangilangan)"),
            ("https://www.umass.edu/global-affairs/international-students-scholars/immigration/f1-students/employment", "UMass Amherst: F-1 employment"),
            ("https://www.u-tokyo.ac.jp/adm/inbound/en/life-daily-pj.html", "University of Tokyo: Part-time job"),
            ("https://www.gov.pl/web/udsc-en/work-student", "UDSC (Polsha): Work, student"),
            ("https://www.hikorea.go.kr", "HiKorea (Koreya immigratsiya portali)"),
        ],
    ),
    dict(
        slug="atlas-ingliz-tili-testi",
        kind="O'qish · Bachelor, Master",
        title="IELTS nima va qachon kerak bo'ladi",
        card="IELTS Academic nimadan iborat, qachon universitet talab qiladi, qachon viza uchun kerak va qachon talab qilinmasligi mumkin.",
        desc="IELTS Academic nima, qachon kerak va qachon kerak emas: Buyuk Britaniya talaba vizasi talabi, universitet o'zi baholashi va muqobil testlar. Rasmiy manbalar bilan.",
        labs=("bachelor", "master", "reja"),
        body=f"""
<p class="at-short"><b>Qisqa javob.</b> IELTS Academic chet elda o'qish uchun ingliz tili testi. Kerakmi yoki yo'qmi, avvalo siz tanlagan dastur sahifasi hal qiladi, keyin viza qoidasi. Shuning uchun testdan oldin dasturlarni tanlang.</p>

<h2>IELTS Academic nimadan iborat</h2>
<p>Rasmiy saytga ko'ra, IELTS Academic bakalavriat yoki magistraturada o'qish uchun mo'ljallangan. To'rt qism bor: tinglash (taxminan 30 daqiqa), o'qish (60 daqiqa), yozish (60 daqiqa) va gapirish (11–14 daqiqa); jami 2 soat 45 daqiqa. Testni markazda yoki onlayn topshirish mumkin, format bir xil. IELTS British Council, IDP va Cambridge University Press &amp; Assessment ga tegishli.</p>

<h2>Qachon kerak</h2>
<ul>
<li><b>Universitet talabi.</b> Har dastur o'z minimal ballini va qaysi testlarni qabul qilishini o'zi yozadi. Aynan dastur sahifasidagi talab asosiy.</li>
<li><b>Viza talabi.</b> Masalan, Buyuk Britaniya talaba vizasi uchun bakalavr va undan yuqori darajada CEFR B2 darajasi talab qilinadi. Ingliz tilini tasdiqlovchi hujjat bo'lmasa, tasdiqlangan provayderning xavfsiz ingliz tili testi (SELT) kerak bo'ladi.</li>
</ul>

<h2>Qachon talab qilinmasligi mumkin</h2>
<ul>
<li>GOV.UK ga ko'ra, oliy ta'lim muassasasi talabaning ingliz tilini o'zi baholashi mumkin (B2 ga teng bo'lishi sharti bilan).</li>
<li>Ingliz tilida o'qitilgan va Buyuk Britaniya bakalavriga teng deb baholangan daraja ham viza uchun istisno bo'lishi mumkin; bunday diplom Ecctis orqali baholanadi.</li>
<li>Ba'zi universitetlar boshqa testlarni ham qabul qiladi (masalan, TOEFL iBT yoki PTE Academic). Qaysi biri o'tishini faqat dastur sahifasi aytadi.</li>
</ul>
<p>Bu istisnolar universitetning o'z talabini bekor qilmaydi: viza uchun yetarli bo'lgan narsa qabul uchun yetarli bo'lmasligi mumkin.</p>

<h2>Tartib</h2>
<p><b>Kompas tavsiyasi:</b> avval 3–5 ta dasturning til talabini Bepul rejadagi saralangan ro'yxatga yozing (ball, qabul qilinadigan testlar, muddat). Keyin eng yuqori talab va eng yaqin muddatga qarab test sanasini tanlang.</p>
""",
        sources=[
            ("https://ielts.org/take-a-test/test-types/ielts-academic-test", "IELTS: IELTS Academic test"),
            ("https://www.gov.uk/student-visa/knowledge-of-english", "GOV.UK: Student visa, knowledge of English"),
        ],
    ),
]

# ----------------------------------------------------- mamlakatlar (ish yo'llari)
INTERNAL = [
    ("🇬🇧", "Buyuk Britaniya", "Home Office registri: Skilled Worker vizasi bo'yicha homiylik litsenziyasi bor tashkilotlar. Nom va shahar bo'yicha qidiruv, xarita.", "uk-sponsors.html"),
    ("🇳🇱", "Niderlandiya", "IND registri: yuqori malakali migrant va boshqa ish yo'llari uchun tan olingan homiylar (nom va KvK raqami).", "nl-sponsors.html"),
    ("🇨🇦", "Kanada", "Ijobiy LMIA olgan ish beruvchilar, eng so'nggi e'lon qilingan chorak. Tarixiy ma'lumot: hozirgi bo'sh ish o'rni emas.", "ca-lmia.html"),
]
PORTALS = [
    ("🇺🇸", "AQSh", "H-1B petitsiyalari (tarixiy)", "USCIS H-1B Employer Data Hub: ish beruvchilar topshirgan va ko'rib chiqilgan petitsiyalar. Amaldagi homiylar ro'yxati emas.", "https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub"),
    ("🇩🇪", "Germaniya", "Rasmiy vakansiyalar portali", "Make it in Germany: ish e'lonlari. Har ish uchun viza, diplomni tan oldirish va ish beruvchi shartlari alohida tekshiriladi.", "https://www.make-it-in-germany.com/en/working-in-germany/job-listings"),
    ("🇵🇱", "Polsha", "Ish ruxsatnomasi", "Xorijliklar idorasi (UDSC): ish ruxsatnomasi turlari va kim ruxsatnomasiz ishlay olishi.", "https://www.mos.cudzoziemcy.gov.pl/en/categories-information/doing-the-job/work-permit/"),
    ("🇰🇷", "Janubiy Koreya", "EPS (E-9)", "EPS: E-9 mehnat migratsiyasi tizimi. Professional E-7 yo'li alohida.", "https://www.eps.go.kr/"),
    ("🇯🇵", "Yaponiya", "Specified Skilled Worker", "Yaponiya immigratsiya xizmati: SSW yo'li, til va kasbiy malaka imtihonlari.", "https://www.ssw.go.jp/en/about/visa/"),
    ("🇪🇺", "Yevropa (EURES)", "Transchegaraviy vakansiyalar", "EURES: Yevropa bo'yicha vakansiyalar. Yevropa uchun yagona homiylar registri yo'q, har davlat qoidasi alohida.", "https://eures.europa.eu/index_en"),
    ("🇳🇿", "Yangi Zelandiya", "Akkreditatsiyalangan ish beruvchilar", "Immigration NZ: AEWV uchun akkreditatsiyalangan kompaniyalarni nom bo'yicha tekshirish (yuklab olinadigan ro'yxat yo'q).", "https://www.immigration.govt.nz/work/requirements-for-work-visas/approved-employers/accredited-employer-list/"),
    ("🇦🇺", "Avstraliya", "Homiylik qoidalari", "Home Affairs: ish beruvchi homiyligi va ishchi vizalari bo'yicha rasmiy yo'riqnoma. Faqat ma'lumot.", "https://immi.homeaffairs.gov.au/visas/employing-and-sponsoring-someone/sponsoring-workers"),
    ("🇸🇬", "Singapur", "Employment Pass", "MOM: Employment Pass uchun minimal maosh va COMPASS mezonlari. Faqat ma'lumot.", "https://www.mom.gov.sg/passes-and-permits/employment-pass/eligibility"),
]


def atlas_index() -> str:
    arts = "".join(
        f'<article class="at-card"><span class="at-kind">{a["kind"]}</span><h3>{a["title"]}</h3><p>{a["card"]}</p><a class="at-go" href="{a["slug"]}.html">O\'qish →</a></article>'
        for a in ARTICLES)
    arts += '<article class="at-card"><span class="at-kind">Katalog</span><h3>Rasmiy manbalar katalogi</h3><p>Stipendiya tashkilotlari, universitet portallari va immigratsiya idoralarining rasmiy sahifalari.</p><a class="at-go" href="sources.html">Ochish →</a></article>'
    internal = "".join(
        f'<article class="at-card at-int"><span class="at-flag" aria-hidden="true">{fl}</span><span class="at-kind">Kompas ichida qidiruv</span><h3>{name}</h3><p>{txt}</p><a class="at-go" href="{href}">Qidirish →</a></article>'
        for fl, name, txt, href in INTERNAL)
    portals = "".join(
        f'<article class="at-card"><span class="at-flag" aria-hidden="true">{fl}</span><span class="at-kind">{kind}</span><h3>{name}</h3><p>{txt}</p><a class="at-go" href="{url}" target="_blank" rel="noopener">Rasmiy sahifa ↗</a></article>'
        for fl, name, kind, txt, url in PORTALS)
    body = nav("atlas", "atlas") + pagehead(
        [("Kompas Lab", "index.html"), ("Atlas", None)],
        "Kompas Atlas",
        "Xorijda o'qish va ishlash bo'yicha rasmiy manbalar: qisqa maqolalar va rasmiy registrlardan qidiruv. Har faktda manba va tekshirilgan sana bor.",
        "telescope") + f"""<main>
<section class="at-sec" id="oqish"><div class="wrap">
<h2>O'qish</h2>
<p class="at-intro">Universitet, stipendiya, til testi va o'qish davridagi qoidalar haqida qisqa maqolalar. Har birida rasmiy manbalar va mos Labning bepul M0 moduli ko'rsatilgan.</p>
<div class="at-grid">{arts}</div>
{lab_links("reja", "master", "bachelor", "phd")}
</div></section>
<section class="at-sec" id="ish"><div class="wrap">
<h2>Ish yo'llari</h2>
<p class="at-intro">Har mamlakatda tizim boshqacha: homiylik litsenziyasi, avvalgi ish vizalari statistikasi va e'lon qilingan vakansiya bir narsa emas. Shuning uchun har kartada qanday ma'lumot ekani yozilgan.</p>
<h3 class="at-sub">Kompas ichida qidiruv</h3>
<div class="at-grid">{internal}</div>
<h3 class="at-sub" style="margin-top:22px">Rasmiy portal orqali tekshirish</h3>
<div class="at-grid">{portals}</div>
<div class="at-note"><b>Diqqat.</b> Ro'yxatda bo'lish kompaniyada hozir bo'sh ish o'rni borligini, sizni ishga olishini yoki viza homiyligini bildirmaydi. Kompas ish topib bermaydi va viza bo'yicha maslahat bermaydi; har vakansiya va viza shartini rasmiy manbada tekshiring.</div>
{lab_links("musofir")}
<p class="at-src">Manbalar {CHECKED} holatiga tekshirilgan. Ichki qidiruvdagi har nusxada yuklab olingan sana ko'rsatiladi.</p>
</div></section>
</main>
"""
    ld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Kompas Atlas",
                     "url": "https://www.kompaslab.uz/atlas", "inLanguage": "uz",
                     "dateModified": ISO,
                     "hasPart": [{"@type": "Article", "headline": a["title"], "url": f"https://www.kompaslab.uz/{a['slug']}"} for a in ARTICLES]},
                    ensure_ascii=False)
    h = head(title="Kompas Atlas: xorijda o'qish va ishlash bo'yicha rasmiy manbalar",
             desc="Xorijda o'qish va ishlash bo'yicha rasmiy manbalar: maqolalar, UK, Niderlandiya va Kanada registrlaridan qidiruv, 9 mamlakatning rasmiy portallari. O'zbek tilida.",
             path="atlas", jsonld=ld, css=".at-sub{font-size:16px;margin:4px 0 10px;color:var(--muted)}")
    return page(head_html=h, body=body)


def article(a: dict) -> str:
    src = "".join(f"<li>{ext(u, t, 'en')}</li>" for u, t in a["sources"])
    body = nav("atlas", "atlas") + pagehead(
        [("Kompas Lab", "index.html"), ("Atlas", "atlas.html"), ("Maqola", None)],
        a["title"], a["desc"]) + f"""<main><div class="wrap"><article class="at-art">
<p class="at-meta">Kompas Lab · {CHECKED} holatiga tekshirilgan</p>
{a["body"]}
<h2>Manbalar</h2>
<ol class="at-sources">{src}</ol>
<div class="at-cta"><h3>Keyingi qadam</h3><p>Bu mavzu Lablarda topshiriq va vositalar bilan o'tiladi. M0 bepul.</p>{lab_links(*a["labs"])}{sale_links(*a["labs"])}</div>
<p class="at-meta" style="margin-top:18px"><a href="atlas.html">← Atlasga qaytish</a></p>
</article></div></main>
"""
    ld = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": a["title"],
                     "description": a["desc"], "inLanguage": "uz", "datePublished": ISO, "dateModified": ISO,
                     "author": {"@type": "Organization", "name": "Kompas Lab", "url": "https://www.kompaslab.uz/"},
                     "publisher": {"@type": "Organization", "name": "Kompas Lab"},
                     "mainEntityOfPage": f"https://www.kompaslab.uz/{a['slug']}",
                     "citation": [u for u, _ in a["sources"]]}, ensure_ascii=False)
    h = head(title=f"{a['title']} · Kompas Atlas", desc=a["desc"], path=a["slug"], jsonld=ld)
    return page(head_html=h, body=body)


REGISTRIES = [
    dict(
        file="nl-sponsors.html", data="data/nl-sponsors.json", kind="nl", lang="nl",
        title="Niderlandiya: tan olingan homiylar (IND registri)",
        h1="Niderlandiya: tan olingan homiylar",
        desc="Niderlandiyada IND tan olgan homiy tashkilotlarni (yuqori malakali migrant va boshqa ish yo'llari) nomi yoki KvK raqami bo'yicha qidiring. Rasmiy registr nusxasi, sana bilan.",
        lead="IND (Niderlandiya immigratsiya xizmati) ish yo'llari uchun tan olgan homiylar registridan nusxa. Nom yoki KvK raqami bo'yicha qidiring.",
        notice="Registrda bo'lish kompaniyada bo'sh ish o'rni borligini yoki sizga homiylik qilishini bildirmaydi. IND registrni oyiga bir marta yangilaydi; yakuniy tekshiruvni rasmiy sahifada qiling.",
        filter=None,
        source=("https://ind.nl/en/public-register-recognised-sponsors/public-register-work", "IND: Public register recognised sponsors, work"),
        rules=("https://ind.nl/en", "IND rasmiy sayti"),
        licence="Ma'lumot IND ommaviy registridan olinadi. Qayta foydalanish shartlari registr sahifasida alohida ko'rsatilmagan (tekshirilmagan).",
    ),
    dict(
        file="ca-lmia.html", data="data/ca-lmia.json", kind="ca", lang="en",
        title="Kanada: ijobiy LMIA olgan ish beruvchilar",
        h1="Kanada: ijobiy LMIA olgan ish beruvchilar",
        desc="Kanadada ijobiy LMIA (Labour Market Impact Assessment) olgan ish beruvchilarni nomi, shahri yoki kasbi bo'yicha qidiring. Eng so'nggi chorak, Open Government Licence – Canada.",
        lead="Kanada hukumati ochiq ma'lumotlaridan: oxirgi e'lon qilingan chorakda ijobiy LMIA olgan ish beruvchilar. Nom, shahar yoki kasb bo'yicha qidiring.",
        notice="Bu tarixiy ma'lumot: o'tgan chorakdagi ijobiy LMIA hozirgi bo'sh ish o'rni, ish taklifi yoki ish ruxsatnomasi emas. Yakuniy tekshiruvni rasmiy manbada qiling.",
        filter="Provinsiya",
        source=("https://open.canada.ca/data/en/dataset/90fed587-1364-4f33-a9ee-208181dc0b97", "Open Government Portal: Temporary Foreign Worker Program, positive LMIA employers"),
        rules=("https://www.canada.ca/en/employment-social-development/services/foreign-workers.html", "Canada.ca: Hire a temporary foreign worker"),
        licence="Ma'lumot Open Government Licence – Canada shartlari asosida qayta ishlatiladi.",
    ),
]


def registry(r: dict) -> str:
    cfg = json.dumps({"data": r["data"], "kind": r["kind"], "lang": r["lang"]})
    flt = ""
    cls = " one"
    if r["filter"]:
        cls = ""
        flt = f'<label>{r["filter"]}<select id="arF" disabled><option value="">Hammasi</option></select></label>'
    body = nav("atlas", "atlas") + pagehead(
        [("Kompas Lab", "index.html"), ("Atlas", "atlas.html#ish"), (r["h1"], None)], r["h1"], r["lead"]) + f"""<main><div class="wrap" style="padding-bottom:64px">
<div class="at-note"><b>Diqqat.</b> {r["notice"]} {ext(r["source"][0], "Rasmiy manba ↗")}</div>
<div class="ar-panel">
<div class="ar-controls{cls}"><label>Qidiruv<input id="arQ" type="search" placeholder="Kompaniya nomi" autocomplete="off" disabled data-suggest="off"></label>{flt}</div>
<p id="arStat" class="ar-stat">Kompas nusxasi yuklanmoqda…</p>
</div>
<div class="ar-bar"><h2>Natijalar</h2><span id="arCount"></span></div>
<div id="arList" class="ar-list" data-alifbo="off" aria-live="polite"></div>
<button id="arMore" class="btn btn-g ar-more" type="button" hidden>Yana ko'rsatish</button>
<div class="at-cta"><h3>Topgach nima qilish kerak</h3><p>Kompaniyaning o'z sahifasidan vakansiyani toping va homiylik shartini to'g'ridan-to'g'ri tekshiring. Rasmiy ish yo'llari va firibgarlik belgilari Musofir Lab M0 da (bepul, ro'yxatdan o'tib ochiladi).</p>{lab_links("musofir")}</div>
<p class="at-src">Manba: {ext(r["source"][0], r["source"][1], "en")}. Qoidalar: {ext(r["rules"][0], r["rules"][1], "en")}. {r["licence"]} Kompas Atlas mustaqil ta'limiy vosita, davlat idorasi bilan bog'liq emas. <a href="atlas.html#ish">← Atlas</a></p>
</div></main>
"""
    h = head(title=f"{r['title']} · Kompas Atlas", desc=r["desc"], path=r["file"][:-5])
    scripts = f'<script type="application/json" id="atlas-cfg">{cfg}</script>\n<script src="js/atlas-registry.js" defer></script>\n'
    return page(head_html=h, body=body, scripts=scripts)


def main() -> None:
    out = {"atlas.html": atlas_index()}
    for a in ARTICLES:
        out[a["slug"] + ".html"] = article(a)
    for r in REGISTRIES:
        out[r["file"]] = registry(r)
    for name, html in out.items():
        if "'" in html.replace("&#39;", ""):
            bad = html.split("'")[0][-60:]
            raise SystemExit(f"{name}: ASCII apostrof qoldi: ...{bad}")
        (ROOT / name).write_text(html, encoding="utf-8")
        print("yozildi:", name)


if __name__ == "__main__":
    main()
