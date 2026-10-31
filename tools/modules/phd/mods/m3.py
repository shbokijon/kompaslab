from common import LEEDS, UKRI_SOE, DORA, HOL, STD

MOD = dict(
    title="Ilmiy rahbar va laboratoriya bilan aloqa",
    desc="PhD Lab M3: rahbar topish usullari, rahbar bilan moslik jadvali, professorga dastlabki xat tuzilmasi, portfel va ilovalar, qayta yozish odobi, rahbar bilan suhbat, ikkinchi rahbar va qo'llab-quvvatlash. Natija: 6 ta rahbar moslik kartasi va aloqalar jurnali.",
    lead="Rahbarni faqat mashhurligi bo'yicha emas, ilmiy moslik, bo'sh o'rin va rahbarlik sharoiti bo'yicha tanlaysiz va unga hurmat bilan, dalil bilan yozasiz.",
    hero="memo", weeks="2–3", next="M4. Ilmiy loyiha taklifi va metodologiya", next_href="phd-lab-m4.html",
    goals=[("telescope", "6 ta rahbar moslik kartasi", "ilmiy moslik, metod, bo'sh o'rin, moliya"),
           ("memo", "Professorga dastlabki xat", "o'zingiz yozgan, dalilli"),
           ("calendar", "Aloqalar jurnali", "sana, holat, keyingi qadam")],
    warn=f"Kompas Lab xatni sizning o'rningizga yozmaydi va professorga tanishtirmaydi. Bu modul tuzilma, mezon va xato misollarini beradi. Rahbarning ijobiy javobi qabul yoki moliyalashtirish kafolati emas. Universitet qoidalari {HOL}.",
    lessons=[
        dict(t="Rahbar topish usullari", short="Qidiruv", min=30, kind="🔎 Qidiruv", ic="telescope",
             hook="PhD uchun mos professor mashhur olim bo'lishi shart emas: u aynan sizning savolingizdagi ishni boshqara oladigan odam bo'lishi kerak. Birinchi qadamda 100 ta xat emas, dalilli qisqa ro'yxat kerak.",
             body=f"""<h4>Qayerdan izlanadi</h4>
<ul><li>Kafedra o'qituvchilari sahifalari</li><li>So'nggi grantlar va laboratoriya loyihalari</li><li>Sohangizdagi so'nggi maqolalarning birinchi va oxirgi mualliflari</li><li>Universitetning ochiq loyiha e'lonlari</li></ul>
<p>Har nomzod uchun yozing: metod bo'yicha tajribasi, ma'lumotga kirish imkoni, yangi doktorant olishga bo'sh o'rni bormi, ikkinchi rahbar bo'lishi mumkin bo'lgan hamkorlari.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: \"Siz dunyodagi eng buyuk olimsiz\". Kuchliroq: \"Sizning 2025-yilgi maqolangizda X usulning Y sharoitdagi cheklovi yozilgan; mening savolim aynan shu cheklovga bog'liq\". Faqat haqiqiy bibliografik ma'lumotni yozing.</div>
<div class="box warn">Professor javob bermasligi sizning qobiliyatingiz haqidagi baho emas: bo'sh o'rin yo'qligi yoki bandlik sabab bo'lishi mumkin.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Qisqa, dalilli ro'yxat: so'nggi maqolalar, grantlar, laboratoriya sahifasi. Har nomzodda metod, ma'lumot, bo'sh o'rin va hamkorlar.",
             task="<ul><li>12 ta nomni toping.</li><li>6 tasiga moslik kartasi yozing.</li><li>Qaysi guruh ochiq loyiha e'lon qilganini tekshiring.</li></ul>",
             ph="1) Prof. ..., ... universiteti — metod: ...; maqola: ... (DOI); ochiq o'rin: ha/yo'q/noma'lum"),
        dict(t="Rahbar bilan moslik jadvali", short="Jadval", min=25, kind="📊 Baholash", ic="chart",
             hook="Moslik bahosini \"yoqdi, yoqmadi\" hisidan dalilga o'tkazing. Jadval qaysi professorga birinchi yozishni va nimani so'rash kerakligini ko'rsatadi.",
             body="""<div class="tbl"><table><thead><tr><th>Mezon</th><th>Ball</th><th>Dalil</th></tr></thead><tbody>
<tr><td>Mavzu mosligi</td><td>0–2</td><td>Maqola yoki loyiha</td></tr><tr><td>Metod mosligi</td><td>0–2</td><td>Ishlatgan usullari</td></tr>
<tr><td>Rahbarlik imkoni</td><td>0–2</td><td>Bo'sh o'rin, doktorantlar soni</td></tr><tr><td>Moliya aniqligi</td><td>0–2</td><td>E'lon, grant</td></tr>
<tr><td>Laboratoriya muhiti</td><td>0–2</td><td>Seminar, bitiruvchilar</td></tr></tbody></table></div>
<p>Ball faqat qaysi professorga birinchi yozishni tanlash uchun: inson sifati haqidagi hukm emas. Ma'lumot bo'lmasa, 0 emas, \"noma'lum\" deb yozing.</p>
<div class="box info">\"Maqolalar juda mos, moliya noma'lum\" yomon holat emas: bu xatda nimani so'rash kerakligini ko'rsatadi.</div>
<div class="box warn">Professor \"doktorant olaman\" deb o'zi yozmagan bo'lsa, buni bor deb hisoblamang.</div>""",
             take="5 mezon, har biri 0–2 ball va dalil. \"Noma'lum\" alohida belgi: u xatdagi savolga aylanadi.",
             task="<ul><li>6 professorni 5 mezonda solishtiring.</li><li>Har biri uchun bitta \"noma'lum\" bandni yozing.</li><li>Birinchi 3 tasini tanlang.</li></ul>",
             ph="Prof. A: mavzu 2, metod 1, rahbarlik ?, moliya ?, muhit 1 — noma'lum: bo'sh o'rin"),
        dict(t="Professorga dastlabki xat tuzilmasi", short="Xat", min=35, kind="✉️ Yozish", ic="memo",
             hook="Xatning vazifasi o'zingizni maqtash emas, aniq ilmiy aloqani boshlash. Professor uni bir necha soniyada ko'zdan kechiradi: moslik birinchi ikki jumlada ko'rinishi kerak.",
             body=f"""<h4>Tuzilma (150–200 so'z)</h4>
<ol><li><b>Mavzu qatori:</b> \"PhD so'rovi\" va ilmiy yo'nalish.</li><li><b>Kim ekaningiz:</b> bir jumla.</li><li><b>Nega aynan shu laboratoriya:</b> uning bitta aniq ishi.</li><li><b>Bog'liqlik:</b> sizning savolingiz shu ishga qanday bog'lanadi.</li><li><b>Dalil:</b> tegishli tajribangiz.</li><li><b>Aniq so'rov:</b> bo'sh o'rin bormi, qaysi yo'l bilan ariza berish mumkin.</li><li><b>Ilovalar:</b> CV va qisqa bayon, agar so'ralgan bo'lsa.</li></ol>
<p>Avval universitet qoidasini o'qing: ba'zi e'lon qilingan loyihalarda professorga oldindan yozish talab qilinmaydi yoki ariza portal orqali beriladi.</p>
<div class="box info"><b>Kompas tuzgan namuna (xato).</b> <span lang=\"en\">\"Please accept me to your university, I am highly motivated.\"</span> Bu xatda moslik ham, dalil ham, aniq so'rov ham yo'q.</div>
<div class="box warn">Sun'iy intellekt orqali o'qimagan maqolangiz xulosasini yoki laboratoriya bilan bo'lmagan aloqani to'qimang: professor buni darhol ko'radi.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Moslik birinchi ikki jumlada; bitta aniq ish, bitta aniq dalil, bitta aniq so'rov. 150–200 so'z.",
             task="<ul><li>Professorning bitta tegishli ishini tanlang va o'qing.</li><li>7 qismli tuzilma bo'yicha qoralama yozing.</li><li>Faqat tekshirilgan fakt bilan yuboring.</li></ul>",
             ph="Mavzu: PhD so'rovi: ... Asosiy qism: ..."),
        dict(t="Portfel va ilovalar", short="Ilovalar", min=25, kind="📎 Dalil", ic="books",
             hook="Rahbar siz haqingizdagi dalilni tez topa olishi kerak. 30 betlik \"yutuqlarim\" fayli emas, 2 betlik CV va qisqa bayon yaxshiroq ishlaydi.",
             body="""<ul><li><b>Akademik CV</b> (M5) va 1–2 sahifalik qisqa bayon (M1).</li><li>Ish namunasi: maqola qoralamasi, kod ombori, poster yoki ma'lumotlar namoyishi.</li><li>Havolalar ochiladimi va ruxsatlar to'g'rimi, tekshiring.</li><li>PDF nomi tartibli: <span lang=\"en\">Familiya_CV_2026.pdf</span>.</li></ul>
<div class="box info">CV dan qaysi metodni o'zingiz bajarganingiz aniq ko'rinsin: jamoaviy ishda o'z hissangizni alohida yozing.</div>
<div class="box warn">Birinchi xatga pasport nusxasi, shaxsiy rasm yoki hali e'lon qilinmagan maxfiy natijani qo'shmang.</div>""",
             take="Ixcham dalil: 2 betlik CV, qisqa bayon, bitta ish namunasi. Shaxsiy hujjat va maxfiy ma'lumot yo'q.",
             task="<ul><li>CV ni 2 sahifaga qisqartiring.</li><li>Portfel uchun 3 dalil tanlang.</li><li>Fayllarga versiya va sana qo'ying.</li></ul>",
             ph="CV v2 (2 bet). Dalillar: 1) ... 2) ... 3) ..."),
        dict(t="Qayta yozish va muloqot odobi", short="Odob", min=20, kind="🤝 Muloqot", ic="bell",
             hook="Ketma-ket xat yozish va bosim o'tkazish akademik aloqani buzadi. Bitta xushmuomala eslatma yetarli, keyin boshqa yo'llarni davom ettiring.",
             body="""<ul><li>Universitetning yozishma qoidasini hurmat qiling.</li><li>Birinchi xatdan keyin oqilona vaqt kuting, keyin bitta qisqa eslatma yozing.</li><li>Javob bo'lmasa, ro'yxatdagi keyingi nomzodga o'ting.</li><li>\"Bo'sh o'rin yo'q\" javobini shaxsiy rad deb emas, rejalashtirish signali deb qabul qiling.</li></ul>
<div class="box info"><b>Kompas tuzgan namuna.</b> Qo'pol: <span lang=\"en\">\"Dear Professor, why don't you answer?\"</span> Professional: <span lang=\"en\">\"Thank you for considering my message; I understand if no openings are available.\"</span></div>
<div class="box warn">Bir xil xatni bir nechta professorga nusxa (CC) bilan yubormang.</div>""",
             take="Bitta eslatma, keyin keyingi nomzod. Har aloqani jurnalga yozing: sana, holat, keyingi qadam.",
             task="<ul><li>Har aloqa sanasini jurnalga yozing.</li><li>Eslatma uchun sana belgilang.</li><li>Javobga mos holat qo'ying: javob yo'q / rad / suhbat / ariza.</li></ul>",
             ph="Prof. A — yuborildi ... — eslatma ... — holat: ..."),
        dict(t="Rahbar bilan suhbat", short="Suhbat", min=30, kind="🗣️ Suhbat", ic="miya",
             hook="Birinchi 20 daqiqalik suhbat rasmiy intervyu bo'lmasligi mumkin, lekin unda moslik va bajarilishi mumkinlik aniqlanadi. Tayyor savollar bilan boring.",
             body="""<h4>Tayyorlaning</h4>
<ul><li>Mavzuning 90 soniyalik bayoni.</li><li>Tegishli tajriba va dalil.</li><li>2 ta ilmiy savol.</li><li>Rahbarlik va moliya bo'yicha 3 ta savol.</li></ul>
<p>Rahbarlik madaniyatini tekshiradigan savollar: <span lang=\"en\">\"How many students do you supervise?\"</span>, <span lang=\"en\">\"How is feedback organised?\"</span>, <span lang=\"en\">\"What happens if the project scope changes?\"</span> Suhbatdan keyin qisqa xulosa xati kelishilganlarni aniq qiladi.</p>
<div class="box info">Professor savolingizdan ko'ra ma'lumot mavjudligiga ko'proq qiziqsa, bu metod bilan bog'liq muammo signali. Qisqa bayonni yangilang.</div>
<div class="box warn">Professorning og'zaki ijobiy javobi qabul yoki moliyalashtirish tasdig'i emas.</div>""",
             take="90 soniyalik bayon, dalil, 2 ilmiy va 3 rahbarlik savoli. Suhbatdan keyin xulosa xati. Og'zaki \"ha\" kafolat emas.",
             quiz=[("Rahbar bilan moslik asosan uning taniqli ismiga bog'liq.", "n", "Noto'g'ri: so'nggi ishlar, metod va bo'sh vaqt muhim."),
                   ("Dastlabki xat aniq ilmiy bog'liqlik va qisqa savoldan iborat bo'lishi kerak.", "t", "To'g'ri."),
                   ("Javob kelmasa, har kuni qayta yozish kerak.", "n", "Noto'g'ri: bitta xushmuomala eslatma, keyin boshqa nomzod."),
                   ("Rahbarning roziligi ko'pincha universitet qabulidan alohida bosqich.", "t", "To'g'ri: rasmiy qabul tizimi qaror qiladi.")],
             task="<ul><li>90 soniyalik bayonni ovoz chiqarib mashq qiling.</li><li>6 savolni ustuvorlik bo'yicha tartiblang.</li><li>Suhbatdan keyin qaror qaydini yozing.</li></ul>",
             ph="Savollar: 1) ... 2) ... Suhbatdan keyin o'zgargan farazlarim: ..."),
        dict(t="Ikkinchi rahbar va qo'llab-quvvatlash", short="Jamoa", min=20, kind="🧩 Muhit", ic="shield",
             hook="Ilmiy muvaffaqiyat ko'pincha bitta rahbardan tashqari muhitga ham bog'liq. Muammo chiqqanda kimga murojaat qilishni oldindan biling.",
             body=f"""<ul><li>Ikkinchi rahbar ([[co-supervisor]]) va maslahatchilar roli</li><li>Treninglar rejasi va ko'nikmalar rivoji</li><li>Fikr-mulohaza (feedback) chastotasi</li><li>Shikoyat va yordam kanallari: doktorantura maktabi, talabalar xizmati</li></ul>
<p>UKRI va hamkor fondlarning doktorantlar uchun kutilmalar bayonoti doktorant, rahbar va universitet majburiyatlarini yozadi: arizadan oldin o'qing.</p>
<div class="box info">Kuchli rahbar bor, lekin dala ma'lumotiga kirish yo'q bo'lsa, ikkinchi rahbar yoki sanoat hamkori kerak bo'lishi mumkin.</div>
<div class="box warn">Faqat rahbarning og'zaki va'dasiga tayanib, universitetning rasmiy qoidalarini o'qimaslik xavfli.</div>
<div class="srcs">Manba: {UKRI_SOE}. {HOL}.</div>""",
             take="Ikkinchi rahbar, treninglar, fikr-mulohaza tartibi va yordam kanallari boshlanishdan oldin aniq bo'lsin.",
             task="<ul><li>Bo'lajak jamoangizni sxemaga joylang.</li><li>Universitetning talabalarni qo'llab-quvvatlash kanallarini toping.</li><li>Hal bo'lmagan 2 xavfni yozing.</li></ul>",
             ph="Rahbar: ...; ikkinchi rahbar: ...; yordam: ...; xavflar: ..."),
    ],
    tool=dict(id="aloqa", short="Jurnal", h2="Rahbar aloqalar jurnali", sub="Bitta professor uchun manbali profil va aloqa tarixini yuriting.",
              h3="Rahbar kartasi", tag="5 maydon", ic="memo", btn="Kartani saqlash", badge="Aloqachi", min=4,
              fields=[dict(k="ism", label="Rahbar", hint="ism, institut, laboratoriya", ph="..."),
                      dict(k="ish", label="2 ta so'nggi ishi va DOI", type="area", ph="Muallif, nom, sizga aloqasi"),
                      dict(k="moslik", label="Ilmiy moslik dalili", type="area", ph="Bo'shliq va metod"),
                      dict(k="xat", label="Xatning asosiy dalillari", type="area", ph="Muammo, bog'liqlik, aniq savol"),
                      dict(k="holat", label="Aloqa holati va eslatma sanasi", type="area", ph="Yuborilgan sana, javob, keyingi qadam")]),
    check=dict(h2="M3 nazorati", sub="Aloqalar jurnalini yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har professor uchun 2 ta haqiqiy moslik dalili bor.", "Ma'lumotlar havola va sana bilan.",
                      "Xat har professorga alohida yozilgan, ommaviy emas.", "Universitetning professorga yozish qoidasi tekshirilgan.",
                      "Eslatma sanalari me'yorida.", "Rahbarlik va moliya bo'yicha savollar tayyor.",
                      "Og'zaki \"ha\" kafolat deb yozilmagan.", "Yordam kanallari aniqlangan."]),
    art_title="Rahbar moslik kartalari va aloqalar jurnali", art_short="Jurnal",
    art=[("Nomzodlar ro'yxati", ["a1"]), ("Moslik jadvali", ["a2"]), ("Rahbar kartasi", ["ism", "ish", "moslik"]), ("Xat qoralamasi", ["xat", "a3"]),
         ("Ilovalar", ["a4"]), ("Aloqa holati", ["holat", "a5"]), ("Suhbat", ["a6"]), ("Jamoa va yordam", ["a7"])],
    tip="Professorga yozganda u sizdan nima oladi, shuni o'ylang: aniq savol, tegishli dalil va o'z vaqtini hurmat qiladigan qisqa xat.",
    sources=f"{LEEDS}; {UKRI_SOE}; {DORA}. {STD}",
)
