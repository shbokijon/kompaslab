from common import CA_FRAUD, UCAS_SIM, UCAS_PS, UCAS_AI, CA, HOL, STD

MOD = dict(
    title="Inshoni tahrirlash va yakuniy matn",
    desc="Bachelor Lab M10: uch bosqichli tahrir (mazmun, tuzilma, til), klishe va ortiqcha so'zlar, o'zaro tahrir, AI davrida insho qoidalari, yakuniy versiyani platformaga joylash. Natija: yakuniy insholar va tahrir qaydi.",
    lead="Birinchi qoralama faqat boshlanish. Kuchli insho 3–5 marta qayta yoziladi. Bu modulda tahrirni tartibli qilasiz, fikr olishni o'rganasiz va AI dan halol foydalanish chegarasini aniqlaysiz.",
    hero="memo", weeks="2–3", next="M11 Davlat stipendiyalari", next_href="bachelor-lab-m11.html",
    goals=[("memo", "Yakuniy insholar", "chegaraga mos, platformaga tayyor"),
           ("scroll", "Tahrir qaydi", "v1 → yakuniy: nima o'zgardi va nega"),
           ("shield", "Halollik qarori", "AI va boshqa odam yordamidan qanday foydalandingiz")],
    warn=f"Platformalarning AI va o'xshashlik bo'yicha qoidalari yangilanib turadi. Bu moduldagi qoidalar {HOL}; topshirishdan oldin Common App, UCAS va universitet sahifasini qayta o'qing.",
    lessons=[
        dict(t="Uch bosqichli tahrir", short="Tahrir", min=30, kind="🛠 Tahrir", ic="memo",
             hook="Ko'p o'quvchilar tahrirni vergul va imlo tuzatishdan boshlaydi. Lekin keyin paragraf o'chirilsa, u mehnat behuda ketadi. Tahrir yirikdan maydaga boradi.",
             body="""<div class="tbl"><table><thead><tr><th>Bosqich</th><th>Savol</th><th>Usul</th></tr></thead><tbody>
<tr><td><b>1. Mazmun</b></td><td>Insho siz haqingizda nima deydi? Bu M3 profilingizga mosmi?</td><td>Inshoni bir jumlada aytib bering. Ayta olmasangiz, mazmun aniq emas</td></tr>
<tr><td><b>2. Tuzilma</b></td><td>Epizod → fikr → o'zgarish → ma'no ketma-ketligi bormi? Har paragraf bitta vazifa bajaradimi?</td><td>Har paragraf yoniga uning vazifasini 3 so'zda yozing</td></tr>
<tr><td><b>3. Til</b></td><td>Jumlalar aniqmi? Ortiqcha so'z, xato bormi?</td><td>Ovoz chiqarib o'qish; imlo tekshiruvi</td></tr>
</tbody></table></div>
<p>Har bosqich alohida o'tishda bajariladi. Bir vaqtda hammasini tuzatishga urinmang.</p>
<h4>Versiyalarni saqlang</h4>
<p>Har yirik o'zgarishdan keyin yangi versiya: v1, v2, v3. Fayl nomida sana. Tahrir qaydiga nima o'zgarganini 1–2 jumlada yozing. Bu sizni ham, o'qituvchini ham yo'naltiradi va halollikni ko'rsatadi.</p>
<div class="box info">Mazmun bosqichida insho butunlay o'zgarishi mumkin. Bu normal: ko'p kuchli insholar ikkinchi yoki uchinchi hikoyadan chiqadi.</div>""",
             take="Tahrir yirikdan maydaga: mazmun, tuzilma, til. Har versiyani saqlang va nima o'zgarganini qayd qiling.",
             task="<ul><li>Inshoingizni bir jumlada aytib bering.</li><li>Har paragraf vazifasini 3 so'zda yozing va vazifasi takrorlangan paragrafni belgilang.</li></ul>",
             ph="Insho bir jumlada: ... Paragraflar: 1) sahna, 2) ..., 3) ..."),
        dict(t="Klishelar va ortiqcha so'zlar", short="Klishe", min=25, kind="🎯 Mini-test", ic="bulb",
             hook="\"Bolaligimdan muhandis bo'lishni orzu qilardim\" bilan boshlangan insholar shunchalik ko'pki, komissiya keyingi jumlaga e'tibor bermasligi mumkin.",
             body="""<h4>Keng tarqalgan klishelar</h4>
<ul><li>\"Bolaligimdan ...\", \"Men har doim ...\" bilan boshlash.</li><li>Lug'atdan ta'rif: \"Vebsterning lug'atiga ko'ra ...\"</li><li>Mashhur iqtibos bilan boshlash.</li><li>O'z-o'zini maqtash: \"Men juda mehnatkash va iqtidorli o'quvchiman.\"</li><li>Mavhum iboralar: \"dunyoni o'zgartirmoqchiman\", \"insoniyatga foyda keltirmoqchiman\".</li></ul>
<h4>Ortiqcha so'zlar</h4>
<div class="tbl"><table><thead><tr><th>Ortiqcha</th><th>Aniq (Kompas tuzgan namuna)</th></tr></thead><tbody>
<tr><td>Men juda ham katta qiziqish bilan shuni ta'kidlashni istardimki ...</td><td>(olib tashlang, to'g'ri fikrdan boshlang)</td></tr>
<tr><td>Bu tajriba men uchun juda muhim bo'ldi.</td><td>Shundan keyin har hafta ... qila boshladim.</td></tr>
</tbody></table></div>
<h4>Usul</h4>
<p>\"juda\", \"haqiqatan\", \"aslida\", \"har doim\" so'zlarini qidiring va har birini olib tashlab ko'ring. Ma'no o'zgarmasa, olib tashlang.</p>""",
             take="Klishe bilan boshlamang, o'zingizni maqtamang, mavhum va'da bermang. Ortiqcha so'zni olib tashlang, uning o'rniga harakat yozing.",
             quiz=[("Mashhur iqtibos bilan boshlash inshoni original qiladi.", "n", "Noto'g'ri: bu eng keng tarqalgan boshlanishlardan biri."),
                   ("\"Men juda mehnatkashman\" jumlasi epizoddan kuchliroq dalil.", "n", "Noto'g'ri: xususiyatni voqea orqali ko'rsatish kuchliroq."),
                   ("\"juda\" so'zini olib tashlaganda ma'no o'zgarmasa, uni olib tashlash mumkin.", "t", "To'g'ri: ortiqcha so'z joyni egallaydi."),
                   ("Mavhum va'dalar (\"dunyoni o'zgartiraman\") aniq rejadan ko'ra ishonchliroq.", "n", "Noto'g'ri: aniq qadam ishonchliroq.")],
             task="<ul><li>Inshoingizdan 3 ta klishe yoki ortiqcha jumlani toping.</li><li>Har birini aniq harakat yoki epizod bilan qayta yozing.</li></ul>",
             ph="Eski: ... → Yangi: ..."),
        dict(t="O'zaro tahrir", short="Peer review", min=25, kind="🤝 Fikr olish", ic="compass",
             hook="Siz inshoingizni juda yaxshi bilasiz, shuning uchun undagi bo'shliqlarni ko'rmaysiz. Boshqa odam ko'zi tahrirning eng arzon va eng foydali vositasi.",
             body="""<h4>Kimga ko'rsatish</h4>
<ul><li><b>1–2 kishi yetarli</b>: masalan ingliz tili o'qituvchisi va sizni yaxshi biladigan do'st.</li><li>Ko'p odam ko'p qarama-qarshi fikr beradi va inshoingiz o'z ovozini yo'qotadi.</li><li>Ota-onalar mazmun bo'yicha foydali, lekin ular ko'pincha klishelarni yoqtiradi.</li></ul>
<h4>Qanday so'rash</h4>
<p>\"Qanday?\" deb emas, aniq savollar bilan:</p>
<ol><li>O'qib bo'lgach, men haqimda qaysi 3 narsani eslab qoldingiz?</li><li>Qaysi joyda zerikdingiz yoki chalkashdingiz?</li><li>Qaysi jumla menga o'xshamaydi?</li></ol>
<h4>Qaysi fikrni qabul qilish</h4>
<ul><li>Ikki odam bir joyni belgilasa, o'sha joyda muammo bor.</li><li>Yechim taklifini emas, muammoni qabul qiling; yechimni o'zingiz toping.</li><li>Kimdir jumlangizni qayta yozib bersa, uni ko'chirmang: bu sizning matningiz bo'lishi kerak.</li></ul>
<div class="box warn">Pullik \"insho yozib beramiz\" xizmatlari va matnni o'zi qayta yozadigan muharrirlar arizangizni xavf ostiga qo'yadi. O'zaro tahrir fikr beradi, matn emas.</div>""",
             take="1–2 kishiga aniq savollar bilan ko'rsating. Ikki odam bir joyni belgilasa, u yerda muammo bor. Muammoni qabul qiling, yechimni o'zingiz yozing.",
             task="<ul><li>2 ta o'quvchini tanlang va ularga uchta aniq savol yuboring.</li><li>Olingan fikrlarni va qaysi birini qabul qilganingizni yozing.</li></ul>",
             ph="O'quvchi 1: ... fikri: ... qabul qildim/qilmadim, chunki ..."),
        dict(t="AI davrida insho", short="AI qoidalari", min=30, kind="⚖️ Chegara", ic="shield",
             hook="AI bir necha soniyada \"chiroyli\" insho yozib beradi. Lekin platformalar va universitetlar buni firibgarlik deb hisoblashi mumkin, va eng muhimi, u sizning hikoyangiz emas.",
             body=f"""<h4>Platforma qoidalari</h4>
<ul><li><b>Common App</b>: firibgarlik siyosati AI platformasi yaratgan mazmunni o'z ishi sifatida topshirishni firibgarlik qatoriga kiritadi. Arizani imzolaganingizda matn o'zingizniki ekanini tasdiqlaysiz.</li>
<li><b>UCAS</b>: AI dan g'oya to'plash, tuzilma taklifi va o'qilishni tekshirish uchun foydalanish mumkin. Bayonotning hammasini yoki katta qismini AI ga yozdirib, o'ziniki sifatida topshirish universitetlar tomonidan ko'chirish ([[cheating]]) deb hisoblanadi. Siz bayonot boshqa manbadan, jumladan AI dan ko'chirilmaganini tasdiqlaysiz. UCAS tekshiruv jamoasi bayonotlar orasidagi o'xshashlikni tekshiradi; o'xshashlik topilsa universitetlarga xabar berilishi, taklif berilmasligi yoki qaytarib olinishi mumkin.</li>
<li><b>Universitetlar</b>: ko'pchiligi o'z qoidasini e'lon qiladi. Ariza beradigan har universitet sahifasini tekshiring.</li></ul>
<h4>Chegara</h4>
<div class="tbl"><table><thead><tr><th>Odatda maqbul</th><th>Maqbul emas</th></tr></thead><tbody>
<tr><td>G'oyalar ro'yxatini tuzish uchun savol-javob</td><td>Insho yoki uning qismini yozdirish</td></tr>
<tr><td>Imlo va grammatika tekshiruvi (matnni qayta yozmasdan)</td><td>\"Yaxshiroq qilib qayta yoz\" deb butun paragrafni almashtirish</td></tr>
<tr><td>\"Bu paragraf nima demoqchi?\" deb tushunarlilikni tekshirish</td><td>AI yozgan matnni o'z so'zingiz bilan qayta yozish (u baribir sizning fikringiz emas)</td></tr>
</tbody></table></div>
<p>Kompas Lab qoidasi: matnni siz yozasiz; AI va odamlar faqat savol beradi va xatoni ko'rsatadi.</p>
<div class="srcs">Manba: {CA_FRAUD}; {UCAS_AI}; {UCAS_SIM}. {HOL}.</div>""",
             take="Common App AI yaratgan matnni o'z ishi sifatida topshirishni firibgarlik deydi; UCAS barcha bayonotlarni o'xshashlikka tekshiradi. AI faqat savol va tekshiruv uchun, matnni siz yozasiz.",
             task="<ul><li>Ariza beradigan 3 universitet va platformaning AI qoidasini toping va havolasini yozing.</li><li>O'zingizning AI dan foydalanish qoidangizni 3 bandda yozing.</li></ul>",
             ph="Common App: ... UCAS: ... ... universiteti: ... Mening qoidam: 1) ... 2) ... 3) ..."),
        dict(t="Yakuniy versiya", short="Yakun", min=25, kind="✅ Joylash", ic="seedling",
             hook="Muddat oxirgi kunida platforma sekinlashadi, matn formatlash buziladi, belgi chegarasi boshqacha hisoblanadi. Yakuniy versiyani erta va tekshirib joylang.",
             body=f"""<h4>Chegara</h4>
<ul><li>Common App: so'z soni platforma hisoblagichi bo'yicha; matnni joylab, hisoblagichga qarang.</li><li>UCAS: belgilar bo'sh joylar bilan; satr oralig'i va maxsus belgilar ham hisoblanishi mumkin.</li><li>Portallar: ba'zilari PDF fayl so'raydi, ba'zilari matn maydoni.</li></ul>
<h4>Fayl va format</h4>
<ul><li>Matnni avval oddiy matn muharririga ko'chirib, keyin platformaga joylang: yashirin formatlash yo'qoladi.</li><li>Qo'shtirnoq, tire va apostrof platformada to'g'ri ko'rinishini tekshiring.</li><li>PDF so'ralsa: fayl nomi \"Familiya_Ism_Universitet_MotivationLetter.pdf\" kabi; hajm chegarasini tekshiring.</li></ul>
<h4>Oxirgi tekshiruv</h4>
<ol><li>Universitet nomi to'g'rimi (boshqa universitet nomi qolib ketmaganmi)?</li><li>Ovoz chiqarib oxirgi marta o'qing.</li><li>Ko'rib chiqish ([[preview]]) sahifasini PDF qilib saqlang.</li></ol>
<div class="srcs">Manba: {CA}; {UCAS_PS}. {HOL}.</div>""",
             take="Matnni oddiy matn orqali joylang, platforma hisoblagichi bilan tekshiring, universitet nomini qayta ko'ring va ko'rib chiqish sahifasini saqlang.",
             task="<ul><li>Yakuniy insholarni platformaga joylab, so'z yoki belgi sonini yozing.</li><li>Tahrir qaydini yakunlang: v1 dan yakuniy versiyagacha 3 asosiy o'zgarish.</li></ul>",
             ph="Common App: ... so'z. UCAS: ... belgi. O'zgarishlar: 1) ... 2) ... 3) ..."),
    ],
    tool=dict(id="tahrir", short="Tahrir qaydi", h2="Yakuniy insholar va tahrir qaydi", sub="Yakuniy matn va uni qanday yaxshilaganingiz bitta joyda.",
              h3="Tahrir qaydi", tag="5 maydon", ic="memo", btn="Qaydni saqlash", badge="Muharrir", min=4,
              fields=[dict(k="yakun", label="Yakuniy asosiy insho (yoki motivatsion xat)", type="area", wc="250-650", ph="..."),
                      dict(k="versiya", label="Versiyalar qaydi", hint="v1, v2, v3: sana va nima o'zgardi", type="area", ph="v1 (...): ... v2 (...): ..."),
                      dict(k="fikr", label="O'zaro tahrir: kim va qaysi fikr qabul qilindi", type="area", ph="..."),
                      dict(k="ai", label="AI va yordamdan foydalanish bayoni", hint="halol yozing", type="area", ph="AI dan faqat ... uchun foydalandim; matnni o'zim yozdim."),
                      dict(k="joylash", label="Platformaga joylash", hint="platforma · so'z/belgi soni · sana", ph="Common App · 612 so'z · ...")]),
    check=dict(h2="Yakuniy versiya nazorati", sub="Topshirishdan oldin tekshiring.", h3="10 bandlik nazorat",
               items=["Insho bir jumlada aytib berila oladi.", "Har paragraf alohida vazifa bajaradi.", "Klishe bilan boshlanmaydi.",
                      "Ortiqcha so'zlar olib tashlangan.", "1–2 kishidan aniq savollar bilan fikr olingan.", "Hech kim matnni men uchun qayta yozmagan.",
                      "AI dan foydalanish platforma va universitet qoidalariga mos.", "Chegara platforma hisoblagichi bilan tekshirilgan.",
                      "Boshqa universitet nomi qolib ketmagan.", "Ko'rib chiqish sahifasi saqlangan."]),
    art_title="Yakuniy insholar va tahrir qaydi", art_short="Yakun",
    art=[("Yakuniy insho", ["yakun"]), ("Tahrir bosqichlari", ["a1", "a2"]), ("Versiyalar qaydi", ["versiya"]), ("O'zaro tahrir", ["fikr", "a3"]),
         ("AI va yordamdan foydalanish", ["ai", "a4"]), ("Platformaga joylash", ["joylash", "a5"])],
    tip="Inshoni universitetga emas, 17 yoshli sizni bilmaydigan odamga yozayotgandek yozing. U o'qib bo'lib siz bilan gaplashgisi kelsa, insho ishlaydi.",
    sources=f"{CA_FRAUD}; {UCAS_AI}; {UCAS_SIM}; {UCAS_PS}; {CA}. {STD}",
)
