from common import LEEDS, UKRIO, DORA, HOL, STD

MOD = dict(
    title="Akademik profil va ariza hujjatlari",
    desc="PhD Lab M5: akademik CV dalil tuzilmasi, ilmiy portfel va kod ombori, tavsiya beruvchilar bilan ishlash, maqsad bayonnomasi va ilmiy bayon, transkript va rasmiy hujjatlar, sun'iy intellekt va akademik halollik. Natija: akademik hujjatlar to'plami va tavsiya beruvchilar uchun faktlar varaqalari.",
    lead="O'z ishingizning dalillarini tekshiriladigan shaklda yozasiz, tavsiya beruvchiga faktlar bilan yordam berasiz va har hujjatda ilmiy halollikni saqlaysiz.",
    hero="books", weeks="2", next="M6. Moliyalashtirish va moliyaviy qaror", next_href="phd-lab-m6.html",
    goals=[("memo", "Akademik CV", "dalil bilan, 2–3 bet"),
           ("books", "Ilmiy portfel", "kod, maqola, poster, takrorlash yo'riqnomasi"),
           ("shield", "Tavsiya uchun faktlar varaqasi", "har tavsiya beruvchiga alohida")],
    warn=f"Tavsiya xatini faqat tavsiya beruvchi o'zi yozadi: siz unga faktlar varaqasini tayyorlaysiz. CV, maqsad bayonnomasi va boshqa hujjatlarni o'zingiz yozasiz. Universitet talablari {HOL}.",
    lessons=[
        dict(t="Akademik CV: dalil tuzilmasi", short="CV", min=35, kind="📄 Hujjat", ic="memo",
             hook="PhD uchun CV ish joylari ro'yxati emas: u ilmiy qobiliyatingizni dalil bilan ko'rsatadi. Komissiya bir daqiqada qaysi metodni bilishingizni ko'ra olishi kerak.",
             body=f"""<h4>Bo'limlar tartibi</h4>
<ol><li>Ta'lim</li><li>Ilmiy loyihalar va tadqiqot tajribasi</li><li>Metodlar va texnik ko'nikmalar</li><li>Nashrlar (holati to'g'ri belgilangan)</li><li>Kod va ma'lumotlar</li><li>O'qitish tajribasi</li><li>Mukofotlar va tegishli ish tajribasi</li></ol>
<p>Natija va shaxsiy hissangizni ajrating: jamoaviy ishda aynan o'zingiz nima qilganingizni yozing (STAR: Vaziyat, Vazifa, Harakat, Natija).</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Noaniq: \"Seysmik ma'lumotlar bilan ishladim\". Tekshiriladigan: \"X turdagi ma'lumotga dastlabki ishlov berdim, takrorlanadigan sifat nazorati jarayonini yozdim va 2 ta asosiy usul bilan solishtirdim\". O'z tajribangizga moslang.</div>
<div class="box warn">Qabul qilinmagan maqolani \"nashr etilgan\" deb yozish ilmiy halollik buzilishi hisoblanadi. Holatlar: nashr etilgan, qabul qilingan, yuborilgan, tayyorlanmoqda. Iqtiboslar soni va jurnal nufuzi yagona qiymat emas (DORA).</div>
<div class="srcs">Manba: {DORA}; {UKRIO}.</div>""",
             take="CV: ta'lim, tadqiqot, metodlar, nashrlar (to'g'ri holat bilan), kod, o'qitish. Har band shaxsiy hissa bilan.",
             task="<ul><li>CV dagi har bandni tekshiring.</li><li>3 ta asosiy ilmiy yutuqni ajrating.</li><li>Har bandga dalil havolasini biriktiring.</li></ul>",
             ph="Yutuq 1: ... (dalil: ...); yutuq 2: ...; o'zgartirilgan bandlar: ..."),
        dict(t="Ilmiy portfel va kod ombori", short="Portfel", min=30, kind="💻 Dalil", ic="books",
             hook="Ishingizni ko'rsatish ilmiy va texnik ishonchni oshiradi, lekin maxfiylikni buzmasligi kerak. Begona odam loyihangizni sizsiz ham tushuna olsin.",
             body="""<ul><li>Kod ombori: tushuntirish fayli ([[README]]), takrorlash yo'riqnomasi, dasturiy muhit fayli, litsenziya.</li><li>Ma'lumot: ochiq yoki sintetik ma'lumot bilan namoyish; haqiqiy ma'lumot maxfiy bo'lsa, ruxsatsiz joylanmaydi.</li><li>Rasm va grafiklar qaysi kod va ma'lumotdan chiqqani yozilgan.</li><li>Gumanitar sohada: izohli bibliografiya, arxiv ishi yoki yozuv namunasi ham portfel bo'ladi.</li></ul>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: izohsiz 70 ta fayl. Kuchliroq: bitta kichik ombor, 3 qadamli ishga tushirish yo'riqnomasi, kutilgan natija va cheklovlar.</div>
<div class="box warn">API kaliti, parol, bemor yozuvi yoki boshqa tashkilotga tegishli o'lchov fayllarini ochiq omborga joylamang.</div>""",
             take="Bitta tushunarli ombor: README, takrorlash yo'riqnomasi, muhit, litsenziya. Maxfiy ma'lumot va kalitlar yo'q.",
             task="<ul><li>Bitta ishingizni tanlang.</li><li>README va takrorlash qadamlarini yozing.</li><li>Kirish huquqlari va maxfiy kalitlarni tekshiring.</li></ul>",
             ph="Ombor: ... README: 1) o'rnatish ... 2) ishga tushirish ... 3) natija ..."),
        dict(t="Tavsiya beruvchilar bilan ishlash", short="Tavsiya", min=30, kind="🤝 Tavsiya", ic="shield",
             hook="Tavsiya xatining kuchi uni kim yozgani va sizning ishingizni qanchalik yaqindan ko'rganiga bog'liq. Tavsiya beruvchiga ish osonlashsin: faktlarni oldindan bering.",
             body="""<ul><li>2–3 nomzodni baholang: sizning ilmiy savolingiz, ishonchliligingiz, mustaqilligingiz va akademik yozuvingizni qanchalik biladi.</li><li>Tavsiya shakli, muddati, portal havolasi va maxfiylik qoidasini oldindan tekshiring.</li><li>Faktlar varaqasi: CV, loyiha qisqa bayoni va birga ishlagan aniq vaziyatlar.</li></ul>
<div class="box info"><b>Kompas tuzgan namuna.</b> \"Men mehnatkashman, shuni yozing\" o'rniga: \"2025-yilda X loyihada Y asosiy usulni sinovdan o'tkazdik; men Z qismini bajardim\".</div>
<div class="box warn">Tavsiya beruvchi nomidan xat yozish va uning nomidan yuborish mumkin emas.</div>""",
             take="Sizni ilmiy ishda ko'rgan tavsiya beruvchi + faktlar varaqasi + aniq muddat. Xatni faqat u yozadi.",
             task="<ul><li>3 ta tavsiya beruvchi ro'yxatini tuzing.</li><li>Har biriga faktlar varaqasi tayyorlang.</li><li>So'rov sanasini kalendarga yozing.</li></ul>",
             ph="1) ... — birga: ... loyiha — so'rov sanasi: ... — muddat: ..."),
        dict(t="Maqsad bayonnomasi va ilmiy bayon", short="Bayon", min=35, kind="✍️ Yozish", ic="scroll",
             hook="Loyiha taklifi \"nima va qanday?\" savoliga, maqsad bayonnomasi esa \"nega aynan siz va nega shu guruh?\" savoliga javob beradi. Ikkalasi bir-birini takrorlamasligi kerak.",
             body="""<p>Tuzilma: <b>Kimlik → Dalil → Maqsad → Moslik</b>. Ilmiy yo'lingiz, o'tgan dalillar, hozirgi bo'shliq, aniq laboratoriya bilan moslik va keyingi yo'nalish bitta mantiqiy hikoyaga birlashsin.</p>
<p>Universitetlar turli nomdagi hujjat so'raydi: shaxsiy bayonot ([[personal statement]]), maqsad bayonnomasi ([[Statement of Purpose]], SoP), ilmiy bayon ([[research statement]]), motivatsion xat. Har birining talabini alohida o'qing.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Umumiy: \"Bolaligimdan ilm-fanni sevaman\". Dalilli: \"Dissertatsiyamda model X sharoitda ishlamay qoldi; bu meni Y savoliga olib keldi; Z laboratoriyaning ishi shu savolga bog'liq\".</div>
<div class="box warn">Hamma universitetga bir xil professor nomi va bir xil paragraf yuborish moslikni zaiflashtiradi.</div>""",
             take="Kimlik → Dalil → Maqsad → Moslik. Har universitetga moslashtirilgan; loyiha taklifini takrorlamaydi.",
             task="<ul><li>4 qismli reja yozing.</li><li>2 ta aniq yutuqni biriktiring.</li><li>Bitta laboratoriyaga moslashtirilgan versiyani tuzing.</li></ul>",
             ph="Kimlik: ... Dalil: ... Maqsad: ... Moslik (... laboratoriyasi): ..."),
        dict(t="Transkript va rasmiy hujjatlar", short="Hujjatlar", min=25, kind="📑 Ro'yxat", ic="calendar",
             hook="Hujjatning ishonchliligi tarjima, shakl va qabul tizimi ko'rsatmasiga bog'liq. Har universitet ro'yxati boshqacha bo'lishi mumkin.",
             body=f"""<ul><li>Diplom, to'liq yoki oraliq transkript, baholash shkalasi</li><li>Tarjimalar</li><li>Til sertifikati</li><li>Pasport ma'lumotlari</li><li>Tavsiyalar va dasturga xos shakllar</li></ul>
<p>Apostil va notarial tasdiq faqat talab qilingan joyda; holati va qayerda tayyorlanishini alohida yozing. Shaxsiy ma'lumotni faqat rasmiy portalga va minimal hajmda yuklang.</p>
<div class="box info">Bir universitet oraliq transkriptni qabul qiladi, boshqasi yakuniy diplom sanasini so'raydi. \"Hamma joyda bir xil\" degan ro'yxat xatoga olib keladi.</div>
<div class="box warn">Pasport nusxasini norasmiy shaxslarga yubormang: faqat universitetning rasmiy ariza portaliga yuklang.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Har universitet uchun alohida ro'yxat: hujjat, shakl, tarjima, holat, muddat. Shaxsiy ma'lumot faqat rasmiy portalga.",
             task="<ul><li>4 ariza uchun hujjat talablarini solishtiring.</li><li>Fayl nomi va shaklini yozing.</li><li>Yetishmayotgan hujjatni belgilang.</li></ul>",
             ph="A: diplom (PDF, tarjima bilan) — tayyor; transkript — ...; yetishmaydi: ..."),
        dict(t="Sun'iy intellekt va akademik halollik", short="Halollik", min=25, kind="🛡️ Qoida", ic="miya",
             hook="Sun'iy intellekt matnni tushuntirish yoki tahrirlashda yordam berishi mumkin, lekin mualliflik va faktlar uchun javobgarlik sizda qoladi. Har jumlani intervyuda himoya qila olishingiz kerak.",
             body=f"""<ul><li>Universitetingizning sun'iy intellekt va plagiat siyosatini oldin o'qing.</li><li>AI to'qigan iqtiboslar, laboratoriya nashrlari, baholar va nashr holatini tekshirmasdan ishlatmang.</li><li>Loyiha taklifi va yozuv namunasi sizning fikrlashingizni ko'rsatishi kerak.</li><li>Maxfiy fayllarni AI xizmatiga yuborishdan oldin ruxsat va siyosatni tekshiring.</li></ul>
<div class="box info">Tilni tahrirlashda yordam olish bir narsa, o'zingiz o'qimagan ishga fikr qo'shish boshqa narsa. Qoralamalar tarixini saqlang.</div>
<div class="box warn">To'qima iqtiboslar va yashirilgan AI mualliflik qabulga ham, ilmiy obro'ga ham xavf.</div>
<div class="srcs">Manba: {UKRIO}.</div>""",
             take="AI faqat yordamchi: siyosatni o'qing, har faktni tekshiring, qoralamalar tarixini saqlang.",
             quiz=[("Akademik CV da tekshiriladigan hissa va vazifaga mos dalil muhim.", "t", "To'g'ri: rol, metod, natija va dalil ajratiladi."),
                   ("Nomzod tavsiya beruvchi nomidan xatni yozib yuborishi mumkin.", "n", "Noto'g'ri: nomzod faqat faktlar varaqasini tayyorlaydi."),
                   ("Maqola nashri har bir PhD arizasi uchun majburiy.", "n", "Noto'g'ri: faqat aniq e'lon talab qilsa; ilmiy dalil turlicha bo'ladi."),
                   ("AI dan foydalanishdan oldin universitet siyosati tekshiriladi va matnni o'zingiz yaratasiz.", "t", "To'g'ri.")],
             task="<ul><li>Arizadagi barcha da'volarni tekshirib chiqing.</li><li>AI siyosati havolasini saqlang.</li><li>Yakuniy matnni ovoz chiqarib tushuntirib bering.</li></ul>",
             ph="Tekshirilgan da'volar: .../...; AI siyosati: (havola); tuzatilganlar: ..."),
    ],
    tool=dict(id="dalil", short="Dalillar", h2="Akademik dalillar banki", sub="CV va ariza dalillarini tekshiriladigan shaklda yozing.",
              h3="Dalillar banki", tag="5 maydon", ic="books", btn="Bankni saqlash", badge="Dalil egasi", min=4,
              fields=[dict(k="loyiha", label="Eng kuchli tadqiqot tajribasi", type="area", ph="Rol, metod, natija"),
                      dict(k="chiqish", label="Portfel, kod, maqola yoki poster", type="area", ph="DOI yoki havola va mualliflik"),
                      dict(k="konikma", label="Metod va texnik ko'nikmalar", type="area", ph="Qaysi metodni qayerda qo'lladingiz?"),
                      dict(k="tavsiya", label="Tavsiya beruvchilar va dalillar", type="area", ph="Kim, qaysi ishingizni ko'rgan?"),
                      dict(k="halollik", label="Halollik va hujjatlar izchilligi", type="area", ph="Tekshiriladigan faktlar va ruxsatlar")]),
    check=dict(h2="M5 nazorati", sub="Hujjatlar to'plamini yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["CV da tekshirib bo'lmaydigan da'vo yo'q.", "Nashr holatlari to'g'ri belgilangan.",
                      "Shaxsiy hissa har bandda aniq.", "Maqsad bayonnomasi va loyiha taklifi bir-birini takrorlamaydi.",
                      "Tavsiya beruvchilarga faktlar varaqasi berilgan.", "Har universitet uchun hujjat shakli va fayl nomi to'g'ri.",
                      "Ochiq omborda maxfiy kalit yoki ma'lumot yo'q.", "AI siyosati o'qilgan va iqtiboslar tekshirilgan."]),
    art_title="Akademik hujjatlar to'plami va tavsiya varaqalari", art_short="To'plam",
    art=[("Akademik CV", ["loyiha", "a1"]), ("Portfel", ["chiqish", "a2"]), ("Ko'nikmalar", ["konikma"]), ("Tavsiya beruvchilar", ["tavsiya", "a3"]),
         ("Maqsad bayonnomasi rejasi", ["a4"]), ("Hujjatlar ro'yxati", ["a5"]), ("Halollik", ["halollik", "a6"])],
    tip="Hujjatlaringizdagi har jumlani intervyuda dalil bilan tushuntira olasizmi? Shu savol eng yaxshi tahrir mezoni.",
    sources=f"{LEEDS}; {UKRIO}; {DORA}. {STD}",
)
