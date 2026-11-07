from common import LEEDS, DORA, UKRIO, HOL, STD

MOD = dict(
    title="Akademik profil va ariza hujjatlari",
    desc="PhD Lab M5: akademik CV dalil tuzilmasi, tadqiqot portfeli va kod omborxonasi, tavsiya beruvchilar strategiyasi, maqsad bayonnomasi va tadqiqot bayoni, transkript va rasmiy hujjatlar, sun'iy intellekt va akademik halollik. Natija: akademik hujjatlar to'plami va tavsiya uchun faktlar varaqalari.",
    lead="PhD hujjatlari ish joylari ro'yxati emas, ilmiy qobiliyatingizning dalili. Bu modulda CV, portfel, tavsiya so'rovi va maqsad bayonnomasini tekshiriladigan faktlar asosida tayyorlaysiz.",
    hero="memo", weeks="2", next="M6 Moliya, doktorlik o'rni va moliyaviy qaror", next_href="phd-lab-o.html?m=6",
    goals=[("memo", "Akademik CV", "har band dalil va shaxsiy hissa bilan"),
           ("books", "Tavsiya uchun faktlar varaqasi", "har tavsiya beruvchiga alohida"),
           ("scroll", "Hujjatlar reyestri", "4 ta ariza bo'yicha fayl, format va holat")],
    warn="CV (STAR: Vaziyat, Vazifa, Harakat, Natija), tavsiya xati va motivatsion xatning umumiy texnikasi Master Lab da. Bu modul PhD ga xos tadqiqot dalili va rahbarga moslashtirilgan dalillarni tayyorlaydi. Tavsiya xatini faqat tavsiya beruvchi yozadi.",
    lessons=[
        dict(t="Akademik CV dalil tuzilmasi", short="CV", min=35, kind="📄 Hujjat", ic="memo",
             hook="PhD CV ning maqsadi ish joylarini sanash emas, ilmiy qobiliyatni dalil bilan ko'rsatish. Komissiya “u nimani o'zi qila oladi?” deb o'qiydi.",
             body=f"""<h4>Bo'limlar</h4>
<p>Ta'lim, tadqiqot loyihalari, usullar, nashrlar (holati to'g'ri belgilangan), kod va ma'lumot, o'qitish, mukofotlar, tegishli ish tajribasi.</p>
<p>Natija va shaxsiy hissani ajrating: jamoaviy ishda aynan o'zingiz nima qilganingizni yozing. Akademik CV va ishchi rezyume ([[Academic CV vs Resume]]) farqi: birinchisida tadqiqot tajribasi birinchi turadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Noaniq: <span lang="en">“Worked on seismic data.”</span> Tekshiriladigan: <span lang="en">“Preprocessed a field dataset, built a reproducible quality-control pipeline and compared two baseline methods.”</span> Bu tuzilma: o'z tajribangizga moslang.</div>
<div class="box warn">Qabul qilinmagan maqolani “nashr qilingan” deb yozish ilmiy qoidabuzarlik xavfini tug'diradi. Iqtiboslar soni va jurnal nufuzini yagona qiymat deb olmang.</div>
<div class="srcs">Manba: {DORA}; {UKRIO}. {HOL}.</div>""",
             take="Har CV bandi: nima qildim, qaysi usul bilan, qanday natija va qayerda tekshirsa bo'ladi.",
             task="<ul><li>CV dagi barcha bandlarni tekshiring.</li><li>3 ta asosiy tadqiqot yutug'ini ajrating.</li><li>Har bandga dalil havolasini biriktiring.</li></ul><p><b>O'zingizga savol:</b> CV ni ko'rgan odam sizni qaysi usul bo'yicha kuchli deb biladi?</p>",
             ph="Yutuq 1: ... (dalil: ...) ; 2: ... ; 3: ..."),
        dict(t="Tadqiqot portfeli va kod", short="Portfel", min=30, kind="💾 Dalil", ic="books",
             hook="Ishingizni ko'rsatish ishonchni oshiradi, lekin maxfiylikni buzmasligi kerak.",
             body=f"""<p>Kod omborxonasida: tushuntirish fayli ([[README]]), qayta ishga tushirish yo'riqnomasi, sintetik yoki ochiq ma'lumot, rasmlar qayerdan chiqqani, muhit fayli va litsenziya.</p>
<p>Haqiqiy ma'lumot maxfiy bo'lsa, ruxsatsiz emas, sintetik misol bilan usulni ko'rsating. Gumanitar sohada izohli bibliografiya, arxiv ishi yoki yozuv namunasi ham portfel bo'la oladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: tushuntirishsiz 70 ta fayl. Kuchliroq: bitta kichik omborxona, 3 qadamli ishga tushirish, kutilgan natija va cheklovlar.</div>
<div class="box warn">API kaliti, bemor yozuvi yoki korxonaga tegishli xom ma'lumotni ochiq omborxonaga yuklamang.</div>""",
             take="Bitta toza, qayta ishga tushadigan va maxfiy ma'lumotsiz omborxona o'nta tartibsiz fayldan kuchliroq.",
             task="<ul><li>Bitta ishni tanlang.</li><li>Tushuntirish fayli va qayta ishga tushirish qadamlarini yozing.</li><li>Kirish huquqlari va maxfiy kalitlarni tekshiring.</li></ul><p><b>O'zingizga savol:</b> begona odam loyihangizni sizsiz tushuna oladimi?</p>",
             ph="Omborxona: ... ; README: maqsad ..., ishga tushirish 1) 2) 3) ..., cheklov ..."),
        dict(t="Tavsiya beruvchilar strategiyasi", short="Tavsiya", min=25, kind="🤝 Tavsiya", ic="bell",
             hook="Tavsiya xatining kuchi uni kim yozgani va u nimaga guvoh bo'lganiga bog'liq. Mashhur, lekin sizni bilmaydigan odam zaif tavsiya beradi.",
             body=f"""<p>2–3 nomzodni baholang: ular sizni ilmiy savol, ishonchlilik, texnik mustaqillik va akademik yozuv bo'yicha qanchalik yaxshi biladi. Tavsiya shakli, muddati, portal havolasi va maxfiylikni oldindan tekshiring.</p>
<p>Tavsiya beruvchiga CV, loyiha qisqachasi va birga ishlagan aniq vaziyatlar ro'yxatini (Yutuqlar varaqasi, [[Brag Sheet]]) yuboring.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> “Mehnatkash deb yozib bering” o'rniga: “2025-yilda X loyihada Y sinovini birga ishlab chiqdik; men Z qismini bajardim” kabi faktlar varaqasi foydaliroq.</div>
<div class="box warn">Tavsiya beruvchi nomidan xat yozish va uni uning nomidan yuborish mumkin emas.</div>""",
             take="Tavsiya beruvchi sizning ishingizga guvoh bo'lgan odam; unga faktlar varaqasi va aniq muddat beriladi.",
             task="<ul><li>3 ta tavsiya beruvchi ro'yxatini tuzing.</li><li>Har biriga faktlar varaqasini tayyorlang.</li><li>Qachon so'rashni kalendarga yozing.</li></ul><p><b>O'zingizga savol:</b> har tavsiya beruvchi sizni ko'rgan real ilmiy vaziyat bormi?</p>",
             ph="1) Dots. ... — birga: ... (2025), guvoh: ... ; so'rash sanasi ..."),
        dict(t="Maqsad bayonnomasi va tadqiqot bayoni", short="Bayonnoma", min=35, kind="✍️ Matn", ic="scroll",
             hook="Taklif “nima va qanday?” savoliga javob beradi. Maqsad bayonnomasi esa “nega aynan siz va nega shu guruh?” savoliga.",
             body=f"""<p>Freymvork: Kimlik → Dalil → Maqsad → Moslik. Tadqiqot yo'lingiz, avvalgi dalil, hozirgi bo'shliq, aniq laboratoriya bilan moslik va kelajak yo'nalishi bitta ilmiy hikoyaga ulanadi.</p>
<p>Universitetlar turli nomlar bilan so'raydi: shaxsiy bayonnoma ([[personal statement]]), Maqsad bayonnomasi ([[Statement of Purpose]], SoP), tadqiqot bayoni ([[research statement]]), motivatsion xat. Mazmuni farq qilishi mumkin: talabni o'qing.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Umumiy: <span lang="en">“Since childhood I have loved science.”</span> Dalilliroq: <span lang="en">“During my thesis, model failure under condition X led me to question Y; this lab's work on Z addresses it.”</span></div>
<div class="box warn">Hamma universitetga bir xil professor nomi va bir xil paragraf yuborish moslikni zaiflashtiradi.</div>""",
             take="Bayonnoma klishe emas, qilingan ish va undan olingan saboq asosida yoziladi va har laboratoriyaga moslanadi.",
             quiz=[("Qabul qilinmagan maqolani CV da “nashr qilingan” deb yozish mumkin, agar yuborilgan bo'lsa.", "n", "Noto'g'ri: holat aniq yoziladi (yuborilgan, ko'rib chiqilmoqda)."),
                   ("Tavsiya xatini tavsiya beruvchi o'zi yozadi.", "t", "To'g'ri: siz faqat faktlar varaqasi berasiz."),
                   ("Maxfiy ma'lumot o'rniga sintetik misol bilan usulni ko'rsatish mumkin.", "t", "To'g'ri: ruxsatsiz ma'lumot ochilmaydi."),
                   ("Sun'iy intellekt keltirgan iqtiboslarni tekshirmasdan ishlatsa bo'ladi.", "n", "Noto'g'ri: to'qilgan manbalar uchraydi; mas'uliyat sizda.")],
             task="<ul><li>4 blokli reja yozing (Kimlik, Dalil, Maqsad, Moslik).</li><li>2 ta aniq yutuqni biriktiring.</li><li>Bitta laboratoriyaga moslashtirilgan versiya yozing.</li></ul><p><b>O'zingizga savol:</b> bayonnoma sizning qaror va tajribangizni ko'rsatadimi?</p>",
             ph="Kimlik: ... ; Dalil: ... ; Maqsad: ... ; Moslik (prof. ..., laboratoriya ...): ..."),
        dict(t="Transkript va rasmiy hujjatlar", short="Hujjatlar", min=25, kind="📁 Reyestr", ic="shield",
             hook="Hujjat ishonchliligi tarjima, format va qabul tizimi ko'rsatmalariga bog'liq. “Hamma joyda bir xil” ro'yxat xatoga olib keladi.",
             body=f"""<p>Diplom, to'liq yoki oraliq transkript, baholash shkalasi, tarjimalar, til dalili, pasport ma'lumoti, tavsiyalar va dasturga xos shakllar ro'yxatini tuzing. Apostil va notarial tasdiq faqat talab qilingan joyda; holati va qayerda tayyorlanishi alohida yuritiladi.</p>
<p>Shaxsiy ma'lumotni minimal yuklang va xavfsiz saqlang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Bir universitet oraliq transkriptni qabul qiladi, boshqasi yakuniy diplom sanasini talab qiladi.</div>
<div class="box warn">Pasport nusxasini norasmiy shaxsga yubormang; faqat rasmiy qabul portaliga yuklang.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Har ariza uchun hujjat, format, fayl nomi va holat jadvali; bog'liq muddatlar alohida belgilanadi.",
             task="<ul><li>4 ta ariza uchun hujjat talablarini solishtiring.</li><li>Fayl nomi va formatini yozing.</li><li>Hali aniqlanmagan bandni belgilang.</li></ul><p><b>O'zingizga savol:</b> hujjat va muddat o'rtasidagi bog'liqlik aniqmi?</p>",
             ph="Ariza 1: diplom (PDF, tarjima ✓), transkript (oraliq), IELTS ..., ... ; Aniqlanmagan: ..."),
        dict(t="Sun'iy intellekt va akademik halollik", short="Halollik", min=20, kind="🛡 Halollik", ic="lock",
             hook="Sun'iy intellekt tushuntirish yoki tilni tahrirlashda yordam berishi mumkin, lekin mualliflik va faktlar uchun mas'uliyat sizda qoladi.",
             body=f"""<p>Universitetning sun'iy intellekt va plagiat siyosatini oldin o'qing. Sun'iy intellekt to'qigan manbalar, nashrlar, baholar va natijalarni tekshirmasdan ishlatmang. Taklif va yozuv namunasi sizning real mulohazangizni ko'rsatishi kerak.</p>
<p>Maxfiy fayllarni modelga yuklashdan oldin ruxsat va siyosatni tekshiring.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Til tahriri bilan aniqroq jumla yozish bir narsa; o'zingiz o'qimagan ishga fikr qo'shish boshqa narsa. Tahrir tarixini saqlang.</div>
<div class="box warn">To'qilgan iqtibos va yashirilgan sun'iy intellekt mualliflik qabulga ham, ilmiy obro'ga ham xavf.</div>
<div class="srcs">Manba: {UKRIO}. {HOL}.</div>""",
             take="Arizadagi har gapni intervyuda dalil bilan himoya qila olsangiz, hujjat sizniki.",
             task="<ul><li>Arizadagi barcha da'volarni tekshiring.</li><li>Universitet sun'iy intellekt siyosati havolasini saqlang.</li><li>Yakuniy matnni ovoz chiqarib tushuntiring.</li></ul><p><b>O'zingizga savol:</b> har gapni intervyuda dalil bilan himoya qila olasizmi?</p>",
             ph="Tekshirilgan da'volar: ... ; siyosat havolasi: ... ; olib tashlandi: ..."),
    ],
    tool=dict(id="reyestr", short="Reyestr", h2="Hujjatlar reyestri", sub="Arizaga tayyor hujjatlar va tavsiyalarni bir joyda kuzating.",
              h3="Reyestr", tag="6 maydon", ic="shield", btn="Reyestrni saqlash", badge="Hujjatchi", min=5,
              fields=[dict(k="cv", label="Akademik CV holati", type="select", opts=["Qoralama", "Dalillar biriktirilgan", "Tayyor"]),
                      dict(k="sop", label="Maqsad bayonnomasi", hint="qaysi dasturlar uchun versiya", type="area", ph="Dastur 1: v2 ..., dastur 2: ..."),
                      dict(k="ref", label="Tavsiya beruvchilar va holati", type="area", ph="1) ... — so'raldi ..., portal ... ; 2) ..."),
                      dict(k="docs", label="Rasmiy hujjatlar", type="area", ph="Diplom ✓, transkript ..., tarjima ..., til ..."),
                      dict(k="port", label="Portfel havolasi", ph="https://..."),
                      dict(k="ochiq", label="Hal bo'lmagan bandlar", type="area", ph="...")]),
    check=dict(h2="M5 nazorati", sub="Hujjatlarni yuklashdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["CV da tekshirib bo'lmaydigan da'vo yo'q.", "Tadqiqot hissam aniq yozilgan.", "Bayonnoma va taklif bir-birini takrorlamaydi.",
                      "Tavsiya beruvchilarga faktlar varaqasi berilgan.", "Universitetga xos format va fayl nomlari to'g'ri.",
                      "Portfelda maxfiy kalit va shaxsiy ma'lumot yo'q.", "Sun'iy intellekt siyosati o'qilgan va matn o'zimniki."]),
    art_title="Akademik hujjatlar to'plami", art_short="To'plam",
    art=[("Akademik CV", ["cv", "a1"]), ("Tadqiqot portfeli", ["port", "a2"]), ("Tavsiyalar", ["ref", "a3"]), ("Maqsad bayonnomasi", ["sop", "a4"]),
         ("Rasmiy hujjatlar", ["docs", "a5"]), ("Halollik tekshiruvi", ["a6", "ochiq"])],
    tip="Tavsiya beruvchidan muddatdan kamida uch hafta oldin so'rang va faktlar varaqasini bitta sahifada bering.",
    sources=f"{LEEDS}; {DORA}; {UKRIO}. {STD}",
)
