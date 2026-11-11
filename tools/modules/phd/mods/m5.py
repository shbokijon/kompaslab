from common import LEEDS, DORA, UKRIO, HOL, STD

MOD = dict(
    title="Akademik profil va ariza hujjatlari",
    desc="PhD Lab M5: akademik CV, tadqiqot portfeli va kod, tavsiya beruvchilar, maqsad bayonnomasi va tadqiqot bayoni, rasmiy hujjatlar, sun'iy intellekt va akademik halollik. Natija: hujjatlar to'plami va tavsiya beruvchilar uchun faktlar varaqalari.",
    lead="PhD arizasidagi hujjatlar <b>ilmiy ish qila olishingizni</b> ko'rsatishi kerak. Bu modulda CV, portfel, tavsiya so'rovi va maqsad bayonnomasini tekshirsa bo'ladigan faktlar asosida tayyorlaysiz.",
    hero="memo", weeks="2", next="M6 Moliya, doktorlik o'rni va moliyaviy qaror", next_href="phd-lab-o.html?m=6",
    goals=[("memo", "Akademik CV", "har bandda dalil va o'zingiz qilgan ish"),
           ("books", "Tavsiya uchun faktlar varaqasi", "har tavsiya beruvchiga alohida"),
           ("scroll", "Hujjatlar ro'yxati", "4 ta ariza bo'yicha fayl, format va holat")],
    warn="CV (STAR: Vaziyat, Vazifa, Harakat, Natija), tavsiya xati va motivatsion xatning umumiy usuli Master Lab da. Bu modulda faqat PhD ga xos qism: tadqiqot dalillari va rahbarga moslashtirish. Tavsiya xatini faqat tavsiya beruvchi o'zi yozadi.",
    lessons=[
        dict(t="Akademik CV", short="CV", min=35, kind="📄 Hujjat", ic="memo",
             hook="Komissiya PhD CV ni o'qiganda bitta savolga javob izlaydi: <i>bu odam nimani o'zi qila oladi?</i>",
             body=f"""<h4>Bo'limlar</h4>
<p>Ta'lim, tadqiqot loyihalari, usullar, nashrlar (holati to'g'ri yozilgan), kod va ma'lumot, dars berish tajribasi, mukofotlar, sohaga tegishli ish tajribasi.</p>
<p>Natija bilan <b>o'zingiz qilgan ishni</b> ajratib yozing: jamoaviy loyihada aynan qaysi qismni bajarganingizni ko'rsating. Akademik CV va ishchi rezyume ([[Academic CV vs Resume]]) farqi: akademik CV da tadqiqot tajribasi birinchi turadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Noaniq: <i><span lang="en">“Worked on seismic data.”</span></i> Tekshirsa bo'ladigan: <i><span lang="en">“Preprocessed a field dataset, built a reproducible quality-control pipeline and compared two baseline methods.”</span></i> Bu tuzilma; uni o'z tajribangizga moslang.</div>
<div class="box warn">Hali qabul qilinmagan maqolani <i>“nashr qilingan”</i> deb yozish ilmiy qoidabuzarlik hisoblanishi mumkin. Iqtiboslar soni va jurnal nufuzi sizni yolg'iz o'zi baholamaydi.</div>
<div class="srcs">Manba: {DORA}; {UKRIO}. {HOL}.</div>""",
             take="Har CV bandi: nima qildim, qaysi usul bilan, qanday natija chiqdi va buni qayerdan tekshirsa bo'ladi.",
             task="<ul><li>CV dagi barcha bandlarni tekshiring.</li><li>3 ta asosiy tadqiqot yutug'ini ajrating.</li><li>Har bandga dalil havolasini qo'shing.</li></ul><p><b>O'zingizga savol:</b> CV ni ko'rgan odam sizni qaysi usulni yaxshi biladi deb o'ylaydi?</p>",
             ph="Yutuq 1: ... (dalil: ...) ; 2: ... ; 3: ..."),
        dict(t="Tadqiqot portfeli va kod", short="Portfel", min=30, kind="💾 Dalil", ic="books",
             hook="Ishingizni ko'rsatish ishonch uyg'otadi, lekin <b>maxfiy ma'lumotni</b> oshkor qilmasligi kerak.",
             body=f"""<p>Kod omborxonasida bo'lsin: tushuntirish fayli ([[README]]), qayta ishga tushirish yo'riqnomasi, sun'iy yoki ochiq ma'lumot, rasmlar qaysi koddan chiqqani, dastur muhiti fayli va litsenziya.</p>
<p>Haqiqiy ma'lumot maxfiy bo'lsa, usulni sun'iy misolda ko'rsating. Gumanitar sohada izohli bibliografiya, arxiv ishi yoki yozuv namunasi ham portfel bo'la oladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Zaif: tushuntirishsiz 70 ta fayl. Kuchliroq: bitta kichik omborxona, 3 qadamda ishga tushadi, kutilgan natija va cheklovlar yozilgan.</div>
<div class="box warn">API kaliti, bemor yozuvi yoki korxonaga tegishli xom ma'lumotni ochiq omborxonaga yuklamang.</div>""",
             take="Bitta toza, ishga tushadigan va maxfiy ma'lumotsiz omborxona tartibsiz o'nta fayldan foydaliroq.",
             task="<ul><li>Bitta ishingizni tanlang.</li><li>Tushuntirish fayli va ishga tushirish qadamlarini yozing.</li><li>Kim ko'ra olishini va maxfiy kalitlar yo'qligini tekshiring.</li></ul><p><b>O'zingizga savol:</b> begona odam loyihangizni sizsiz tushuna oladimi?</p>",
             ph="Omborxona: ... ; README: maqsad ..., ishga tushirish 1) 2) 3) ..., cheklov ..."),
        dict(t="Tavsiya beruvchilar", short="Tavsiya", min=25, kind="🤝 Tavsiya", ic="bell",
             hook="Tavsiya xatining kuchi uni kim yozgani va u <b>sizning qaysi ishingizni ko'rganiga</b> bog'liq. Sizni yaxshi bilmaydigan mashhur olimning xati zaif chiqadi.",
             body=f"""<p>2–3 nomzodni o'ylab ko'ring: ular sizni ilmiy savol qo'yish, ishonchlilik, mustaqil ishlash va akademik yozuv bo'yicha qanchalik yaxshi biladi. Tavsiya shakli, muddati, portal havolasi va maxfiyligini oldindan tekshiring.</p>
<p>Tavsiya beruvchiga CV, loyiha qisqachasi va birga ishlagan aniq holatlar ro'yxatini yuboring. Bu ro'yxat Yutuqlar varaqasi ([[Brag Sheet]]) deyiladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> <i>“Mehnatkash deb yozib bering”</i> deyish o'rniga shunday faktlar bering: <i>“2025-yilda X loyihada Y sinovini birga ishlab chiqdik; Z qismini men bajardim.”</i></div>
<div class="box warn">Tavsiya beruvchi nomidan xat yozish va uning nomidan yuborish mumkin emas.</div>""",
             take="Tavsiya beruvchi ishingizni ko'rgan odam bo'lsin; unga faktlar varaqasi va aniq muddat bering.",
             task="<ul><li>3 ta tavsiya beruvchi ro'yxatini tuzing.</li><li>Har biriga faktlar varaqasini tayyorlang.</li><li>Qachon so'rashingizni kalendarga yozing.</li></ul><p><b>O'zingizga savol:</b> har tavsiya beruvchi sizni ishda ko'rgan real holat bormi?</p>",
             ph="1) Dots. ...: birga ... (2025), ko'rgan ishi ... ; so'rash sanasi ..."),
        dict(t="Maqsad bayonnomasi va tadqiqot bayoni", short="Bayonnoma", min=35, kind="✍️ Matn", ic="scroll",
             hook="Taklif <i>“nima va qanday?”</i> savoliga javob beradi. Maqsad bayonnomasi esa <i>“nega aynan siz va nega shu guruh?”</i> savoliga.",
             body=f"""<p>Tuzilma: <b>Kimlik → Dalil → Maqsad → Moslik</b>. Tadqiqotdagi yo'lingiz, oldingi ishlaringiz, hozirgi bo'shliq, aniq laboratoriya bilan moslik va keyingi yo'nalish bitta izchil hikoyaga ulanadi.</p>
<p>Universitetlar buni turlicha nomlaydi: shaxsiy bayonnoma ([[personal statement]]), Maqsad bayonnomasi ([[Statement of Purpose]], SoP), tadqiqot bayoni ([[research statement]]), motivatsion xat. Mazmuni farq qilishi mumkin, shuning uchun talabni o'qing.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Umumiy: <i><span lang="en">“Since childhood I have loved science.”</span></i> Dalilliroq: <i><span lang="en">“During my thesis, model failure under condition X led me to question Y; this lab's work on Z addresses it.”</span></i></div>
<div class="box warn">Hamma universitetga bir xil professor nomi va bir xil paragraf yuborsangiz, moslik zaif ko'rinadi.</div>""",
             take="Bayonnoma qilgan ishingiz va undan olgan saboqqa tayanadi va har laboratoriyaga alohida moslanadi.",
             quiz=[("Ko'rib chiqilayotgan maqolani CV da “nashr qilingan” deb yozsa bo'ladi.", "n", "Noto'g'ri: holati aniq yoziladi: yuborilgan yoki ko'rib chiqilmoqda."),
                   ("Tavsiya xatini tavsiya beruvchi o'zi yozadi.", "t", "To'g'ri: siz faqat faktlar varaqasini berasiz."),
                   ("Maxfiy ma'lumot o'rniga usulni sun'iy misolda ko'rsatish mumkin.", "t", "To'g'ri: ruxsatsiz ma'lumot ochilmaydi."),
                   ("Sun'iy intellekt keltirgan manbalarni tekshirmasdan ishlatsa bo'ladi.", "n", "Noto'g'ri: u ba'zan mavjud bo'lmagan manbani keltiradi; javobgarlik sizda.")],
             task="<ul><li>4 qismli reja yozing: Kimlik, Dalil, Maqsad, Moslik.</li><li>2 ta aniq yutuqni qo'shing.</li><li>Bitta laboratoriyaga moslangan versiyani yozing.</li></ul><p><b>O'zingizga savol:</b> bayonnomada sizning qarorlaringiz va tajribangiz ko'rinadimi?</p>",
             ph="Kimlik: ... ; Dalil: ... ; Maqsad: ... ; Moslik (prof. ..., laboratoriya ...): ..."),
        dict(t="Transkript va rasmiy hujjatlar", short="Hujjatlar", min=25, kind="📁 Ro'yxat", ic="shield",
             hook="Hujjatga ishonch tarjima, format va qabul tizimi qoidalariga bog'liq. Hamma universitet uchun <b>bitta ro'yxat</b> tuzsangiz, xato ketadi.",
             body=f"""<p>Ro'yxat tuzing: diplom, to'liq yoki oraliq transkript, baholash shkalasi, tarjimalar, til sertifikati, pasport ma'lumoti, tavsiyalar va dasturning o'z shakllari. Apostil va notarial tasdiq faqat talab qilingan joyda kerak; har hujjatning holati va qayerda tayyorlanishini alohida yozing.</p>
<p>Shaxsiy ma'lumotni faqat kerakli joyga yuklang va xavfsiz saqlang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Bir universitet oraliq transkriptni qabul qiladi, boshqasi diplom berilgan sanani so'raydi.</div>
<div class="box warn">Pasport nusxasini tanimagan odamga yubormang; faqat rasmiy qabul portaliga yuklang.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Har ariza uchun hujjat, format, fayl nomi va holat jadvali bo'lsin; bir-biriga bog'liq muddatlar alohida belgilanadi.",
             task="<ul><li>4 ta ariza bo'yicha hujjat talablarini solishtiring.</li><li>Fayl nomi va formatini yozing.</li><li>Hali aniq bo'lmagan bandni belgilang.</li></ul><p><b>O'zingizga savol:</b> qaysi hujjat qaysi muddatga bog'liq, aniqmi?</p>",
             ph="Ariza 1: diplom (PDF, tarjima ✓), transkript (oraliq), IELTS ..., ... ; Aniq emas: ..."),
        dict(t="Sun'iy intellekt va akademik halollik", short="Halollik", min=20, kind="🛡 Halollik", ic="lock",
             hook="Sun'iy intellekt tushuntirish yoki tilni tahrirlashda yordam berishi mumkin. Lekin matn muallifi siz bo'lib qolasiz va <b>har fakt uchun siz javob berasiz</b>.",
             body=f"""<p>Universitetning sun'iy intellekt va plagiat qoidalarini oldindan o'qing. Sun'iy intellekt keltirgan manba, nashr, baho yoki natijani tekshirmasdan ishlatmang. Taklif va yozuv namunasi sizning o'z fikringizni ko'rsatishi kerak.</p>
<p>Maxfiy fayllarni modelga yuklashdan oldin ruxsat va qoidalarni tekshiring.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Til tahriri bilan jumlani aniqroq qilish bir narsa; o'zingiz o'qimagan ish haqida fikr qo'shish boshqa narsa. Tahrir tarixini saqlang.</div>
<div class="box warn">O'ylab topilgan iqtibos va yashirilgan sun'iy intellekt mualliflik qabulga ham, ilmiy obro'ga ham zarar yetkazadi.</div>
<div class="srcs">Manba: {UKRIO}. {HOL}.</div>""",
             take="Arizadagi har jumlani intervyuda dalil bilan himoya qila olsangiz, hujjat haqiqatan sizniki.",
             task="<ul><li>Arizadagi barcha da'volarni tekshiring.</li><li>Universitetning sun'iy intellekt qoidasiga havolani saqlang.</li><li>Oxirgi matnni ovoz chiqarib tushuntirib ko'ring.</li></ul><p><b>O'zingizga savol:</b> har jumlani intervyuda dalil bilan himoya qila olasizmi?</p>",
             ph="Tekshirilgan da'volar: ... ; qoida havolasi: ... ; olib tashlandi: ..."),
    ],
    tool=dict(id="royxat", short="Ro'yxat", h2="Hujjatlar ro'yxati", sub="Arizaga tayyor hujjatlar va tavsiyalarni bir joyda kuzating.",
              h3="Hujjatlar ro'yxati", tag="6 maydon", ic="shield", btn="Ro'yxatni saqlash", badge="Tartibli", min=5,
              fields=[dict(k="cv", label="Akademik CV holati", type="select", opts=["Qoralama", "Dalillar qo'shilgan", "Tayyor"]),
                      dict(k="sop", label="Maqsad bayonnomasi", hint="qaysi dastur uchun qaysi versiya", type="area", ph="Dastur 1: v2 ..., dastur 2: ..."),
                      dict(k="ref", label="Tavsiya beruvchilar va holati", type="area", ph="1) ...: so'raldi ..., portal ... ; 2) ..."),
                      dict(k="docs", label="Rasmiy hujjatlar", type="area", ph="Diplom ✓, transkript ..., tarjima ..., til ..."),
                      dict(k="port", label="Portfel havolasi", ph="https://..."),
                      dict(k="ochiq", label="Hal bo'lmagan masalalar", type="area", ph="...")]),
    check=dict(h2="M5 nazorati", sub="Hujjatlarni yuklashdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["CV da tekshirib bo'lmaydigan da'vo yo'q.", "Tadqiqotdagi o'z hissam aniq yozilgan.", "Bayonnoma va taklif bir-birini takrorlamaydi.",
                      "Tavsiya beruvchilarga faktlar varaqasi berilgan.", "Har universitet talab qilgan format va fayl nomlari to'g'ri.",
                      "Portfelda maxfiy kalit va shaxsiy ma'lumot yo'q.", "Sun'iy intellekt qoidalari o'qilgan, matn o'zimniki."]),
    art_title="Akademik hujjatlar to'plami", art_short="To'plam",
    art=[("Akademik CV", ["cv", "a1"]), ("Tadqiqot portfeli", ["port", "a2"]), ("Tavsiyalar", ["ref", "a3"]), ("Maqsad bayonnomasi", ["sop", "a4"]),
         ("Rasmiy hujjatlar", ["docs", "a5"]), ("Halollik tekshiruvi", ["a6", "ochiq"])],
    tip="Tavsiya beruvchidan muddatdan kamida uch hafta oldin so'rang va faktlar varaqasini bitta sahifada bering.",
    sources=f"{LEEDS}; {DORA}; {UKRIO}. {STD}",
)
