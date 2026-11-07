from common import LEEDS, ATAS, VISA, UKRIEXP, UKRIO, HOL, STD

MOD = dict(
    title="Qabuldan keyingi tayyorgarlik va birinchi 90 kun",
    desc="PhD Lab M8: taklif shartlarini yopish, viza va ATAS, uy, xavfsizlik va dastlabki xarajat, tadqiqotga kirishish tizimi, 90 kunlik ilmiy ritm, karyera va foydali tadqiqot. Natija: jo'nash oldi nazorat ro'yxati va 90 kunlik reja.",
    lead="Taklifni qabul qilish yo'lning oxiri emas. Bu modulda shartlarni yopasiz, viza va uy masalasini hal qilasiz va birinchi 90 kunni o'lchanadigan natijalar bilan rejalaysiz.",
    hero="seedling", weeks="1–3", next="", next_href="",
    goals=[("shield", "Jo'nash oldi nazorat ro'yxati (Pre-departure checklist)", "har shart, egasi va sanasi bilan"),
           ("calendar", "30/60/90 kunlik reja", "har bosqichda o'lchanadigan natija"),
           ("bulb", "Rahbar bilan birinchi uchrashuv kun tartibi", "kutilmalar, ritm, trening")],
    warn="Bu kurs huquqiy yoki immigratsiya maslahati emas. Viza va ATAS bo'yicha yakuniy javobni rasmiy idora va universitetingiz beradi. Qabuldan keyingi 90 kun PhD qo'llab-quvvatlash tizimining o'rnini bosmaydi; tadqiqot dizayni, etika va nashr bo'yicha chuqur mavzular Research Lab da.",
    lessons=[
        dict(t="Taklif shartlarini yopish", short="Shartlar", min=20, kind="✅ Nazorat", ic="shield",
             hook="Taklifni qabul qilish dasturga yozilishning oxirgi nuqtasi bo'lmasligi mumkin. Shartlardan biri yopilmasa, taklif kuchsiz qoladi.",
             body=f"""<p>Izchilligini tekshiring: diplom, til dalili, depozit, moliya tasdig'i, immigratsiya hujjati, boshlanish sanasi va rahbar tasdig'i. Shartlar, muddatlar va rasmiy qabul portal orqali kuzatiladi. Noma'lum bandga qabul bo'limidan rasmiy aniqlik so'rang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Qo'lingizda shartli akademik taklif bo'lsa, grant xatining shartlari alohida tekshiriladi.</div>
<div class="box warn">“Taklif olindi” va “shartsiz va moliyalashtirilgan” iboralarini aralashtirmang.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Har shart uchun egasi, sanasi va yopilganini isbotlaydigan hujjat yoziladi.",
             task="<ul><li>Taklifdagi barcha shartlarni yozing.</li><li>Har biriga egasi va sanasini belgilang.</li><li>Yopilganini isbotlovchi hujjatni saqlang.</li></ul><p><b>O'zingizga savol:</b> har shart yopilganini qaysi hujjat isbotlaydi?</p>",
             ph="Shart 1: diplom — men, ... sana, dalil ... ; 2: til — ... ; 3: depozit — ..."),
        dict(t="Viza, ATAS va immigratsiya", short="Viza", min=30, kind="🛂 Rasmiy", ic="lock",
             hook="Viza va tadqiqot ruxsati qoidalari shaxsiy holat, fan va mamlakatga bog'liq. Forumdagi o'tgan yilgi javob ishonchli manba emas.",
             body=f"""<p>Buyuk Britaniya uchun talaba vizasi ([[Student visa]]) va ba'zi fanlar uchun [[ATAS]] (Academic Technology Approval Scheme) talabini GOV.UK va universitet ko'rsatmasidan tekshiring.</p>
<ul><li>ATAS hammaga emas: fuqarolik (ozod etilgan mamlakatlar ro'yxati bor) va universitet bergan fan kodi ([[CAH3]]) bo'yicha aniqlanadi.</li><li>GOV.UK ko'rsatishicha, ATAS ko'rib chiqilishi kamida 30 ish kuni (6 hafta) davom etadi, aprel–avgustda uzoqroq bo'lishi mumkin.</li><li>Talaba vizasida ishlash mumkin bo'lishi va qancha ishlash o'qish turi va vaqtiga bog'liq: GOV.UK sahifasidan o'qing.</li></ul>
<p>Boshqa mamlakatlar uchun rasmiy immigratsiya idorasiga murojaat qiling.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Geofizika yoki muhandislik loyihasi ATAS tekshiruviga tushishi mumkin, lekin avtomatik “shart” deyish xato: universitet taklifidagi fan kodi hal qiladi.</div>
<div class="box warn">Immigratsiya qoidalarini o'tgan yilgi forum javobidan olmang.</div>
<div class="srcs">Manba: {VISA}; {ATAS}. {HOL}.</div>""",
             take="Viza va ATAS talabini rasmiy sahifadan tekshiring va ATAS uchun kamida 6 haftani rejaga qo'ying.",
             quiz=[("ATAS Buyuk Britaniyadagi barcha xalqaro PhD talabalarga majburiy.", "n", "Noto'g'ri: fuqarolik va fan kodiga (CAH3) bog'liq."),
                   ("GOV.UK ga ko'ra ATAS kamida 30 ish kunida ko'rib chiqiladi.", "t", "To'g'ri: aprel–avgustda uzoqroq bo'lishi mumkin."),
                   ("Ish daromadini viza shartlarini tekshirmasdan byudjetga qo'shish mumkin.", "n", "Noto'g'ri: ish huquqi o'qish turi va vaqtiga bog'liq."),
                   ("PhD tugashi doimiy ish yoki immigratsiyani kafolatlamaydi.", "t", "To'g'ri: yo'llar alohida baholanadi.")],
             task="<ul><li>UK yoki mezbon mamlakat viza sahifasini oching.</li><li>ATAS sizga tegishli ekanini tekshiring.</li><li>Muddatlar va hujjatlar ro'yxatini tuzing.</li></ul><p><b>O'zingizga savol:</b> qaysi idora sizga yakuniy shaxsiy javob bera oladi?</p>",
             ph="Viza: ..., hujjatlar ... ; ATAS: kerak / kerak emas (fan kodi ...) ; ariza sanasi ..."),
        dict(t="Uy, xavfsizlik va dastlabki xarajat", short="Uy", min=25, kind="🏠 Amaliy", ic="hourglass",
             hook="Birinchi oyda ilmiy ishni boshlash uchun asosiy ehtiyojlar oldindan hal bo'lishi kerak.",
             body=f"""<p>Amaliy ro'yxat: ijara shartnomasi, depozit, kommunal to'lovlar, yo'l, tibbiyotda ro'yxatdan o'tish, bank hisobi, telefon, favqulodda aloqalar va sug'urta. Universitetning xalqaro talabalar xizmati va shahar rasmiy manbalarini toping.</p>
<p>Qo'shimcha ishga moliyaviy tayanishdan oldin viza shartlarini tekshiring.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Stipendiya bir oy kechiksa, dastlabki turar joy uchun naqd pul borligi hal qiluvchi.</div>
<div class="box warn">Soxta ijara depozitlari va faqat Telegram orqali bog'lanadigan vositachilardan ehtiyot bo'ling.</div>""",
             take="60 kunlik naqd pul rejasi, 3 ta ishonchli yordam aloqasi va o'qilgan ijara shartnomasi.",
             task="<ul><li>60 kunlik naqd pul rejasini tuzing.</li><li>3 ta ishonchli yordam aloqasini toping.</li><li>Ijara shartnomasini o'qing.</li></ul><p><b>O'zingizga savol:</b> borgan kuningiz telefon, manzil, yordam aloqasi va pulingiz tayyormi?</p>",
             ph="Naqd pul: ... ; aloqalar: 1) universitet xizmati ... 2) ... 3) ... ; ijara: ..."),
        dict(t="Tadqiqotga kirishish tizimi", short="Kirishish", min=25, kind="🧭 Tizim", ic="compass",
             hook="Doktorantura boshlanishi “tadqiqotni boshladim” degan mavhum his bo'lmasligi kerak.",
             body=f"""<p>Tartibga solinadi: institut tanishtiruvi, etika bo'yicha kirish treningi, ma'lumotlarni boshqarish, laboratoriya xavfsizligi, hisoblash resurslariga kirish, rahbar bilan uchrashuv ritmi, bosqichlar va trening rejasi.</p>
<p>Loyiha doirasi birinchi oylarda o'zgarishi mumkin: kelishilgan uchrashuv qaydi va xavflar ro'yxati buni boshqaradi. UKRI kutilmalar bayoni talaba va rahbar majburiyatlarini ko'rsatadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> 1–2-hafta: kirish huquqlari va adabiyot xaritasi; 3–4-hafta: asos ([[baseline]]) va qayta ishga tushadigan muhit. Bu umumiy o'quv namunasi, hamma fan uchun qat'iy jadval emas.</div>
<div class="box warn">Maxfiy ma'lumot va xavfsizlik ruxsatisiz dala ishini boshlamang.</div>
<div class="srcs">Manba: {UKRIEXP}; {UKRIO}. {HOL}.</div>""",
             take="Kirishish ro'yxati, birinchi uchrashuv kun tartibi va trening talablari: birinchi oyning asosi.",
             task="<ul><li>Kirishish nazorat ro'yxatini tuzing.</li><li>Rahbar bilan 1:1 uchrashuv kun tartibini yozing.</li><li>Trening talablarini belgilang.</li></ul><p><b>O'zingizga savol:</b> birinchi progress uchrashuvida ko'rsatadigan birinchi natijangiz nima?</p>",
             ph="Kirishish: ... ; kun tartibi: 1) kutilmalar 2) uchrashuv ritmi 3) ... ; trening: ..."),
        dict(t="90 kunlik ilmiy ritm", short="90 kun", min=25, kind="📅 Ritm", ic="calendar",
             hook="Ilmiy ishda bandlik emas, tekshiriladigan natija va fikr olish muhim.",
             body=f"""<ul><li><b>30 kun</b>: adabiyot xaritasi va ishchi savol.</li><li><b>60 kun</b>: bajarilishi mumkinlik sinovi va asos.</li><li><b>90 kun</b>: qayta ko'rilgan tadqiqot rejasi va xavflar ko'rigi.</li></ul>
<p>Bosqichlar soha va rahbar bilan kelishiladi. Haftalik jurnal (bajarildi, o'rganildi, to'xtab qoldi, keyingi qadam) fikr olishni yaxshilaydi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> “Har kuni 8 soat ishlayman” o'rniga “2 hafta ichida ochiq ma'lumotda asos natijani takrorlash va xatolar jadvali” aniqroq.</div>
<div class="box warn">Qattiq kunlik zanjir va o'zini ayblash ilmiy sifat o'rnini bosmaydi.</div>""",
             take="30/60/90 bosqichlari natija bilan yoziladi va haftalik jurnal bilan kuzatiladi.",
             task="<ul><li>30/60/90 bosqichlarini yozing.</li><li>Haftalik ko'rik odatini belgilang.</li><li>Xavf belgilarini va maslahat kanallarini yozing.</li></ul><p><b>O'zingizga savol:</b> 90 kundan keyin qaysi bilimingiz yangilangan bo'ladi?</p>",
             ph="30: ... ; 60: ... ; 90: ... ; haftalik ko'rik: juma ..."),
        dict(t="Karyera va foydali tadqiqot", short="Karyera", min=20, kind="🌱 Yo'l", ic="seedling",
             hook="PhD davomida akademik va boshqa professional yo'llar ochiq qolishi kerak. Bir yo'lga erta yopilish xavfli.",
             body=f"""<p>Rejalang: boshqa sohalarga ko'chadigan ko'nikmalar, sanoat hamkorligi, o'qitish, ilmiy muloqot, takrorlanuvchan tadqiqot va karyera bo'yicha mentor. Ochiq fan, halol mualliflik va tadqiqot halolligi kelajakdagi qiymatga aylanadi.</p>
<p>O'zbekistonga qaytish, xalqaro tadqiqot yoki sanoat yo'llarini har biri uchun real ko'nikma va imkoniyat bilan baholang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Bitta ilmiy kod omborxonasi, poster va sanoat misoli akademik va sanoat portfeliga turlicha yordam beradi.</div>
<div class="box warn">PhD tugashi doimiy ish yoki immigratsiyani kafolatlamaydi.</div>
<div class="srcs">Manba: {UKRIO}. {HOL}.</div>""",
             take="3 yillik ko'nikma xaritasi va 2 ta karyera yo'li: birinchi 90 kunda bitta ko'nikma tanlanadi.",
             task="<ul><li>3 yillik ko'nikma xaritasini chizing.</li><li>2 ta ehtimoliy karyera yo'lini solishtiring.</li><li>Birinchi 90 kun uchun bitta ko'nikma tanlang.</li></ul><p><b>O'zingizga savol:</b> tadqiqotingiz kim uchun qanday amaliy yoki ilmiy foyda beradi?</p>",
             ph="Ko'nikmalar: 1-yil ..., 2-yil ..., 3-yil ... ; yo'llar: ... / ... ; 90 kun: ..."),
    ],
    tool=dict(id="reja", short="90 kun", h2="30/60/90 kunlik reja", sub="Birinchi, o'lchanadigan tadqiqot natijalarini yozing.",
              h3="Jo'nash va 90 kun", tag="6 maydon", ic="calendar", btn="Rejani saqlash", badge="Yo'lboshchi", min=5,
              fields=[dict(k="shart", label="Taklif shartlari holati", type="area", ph="Diplom ✓, til ✓, moliya xati ..., viza ..."),
                      dict(k="viza", label="Viza va ATAS", type="area", ph="Viza ariza sanasi ..., ATAS: ..."),
                      dict(k="uy", label="Uy va dastlabki pul", type="area", ph="Ijara ..., depozit ..., 60 kunlik naqd ..."),
                      dict(k="d30", label="30 kun natijasi", ph="Adabiyot xaritasi + ishchi savol"),
                      dict(k="d60", label="60 kun natijasi", ph="..."),
                      dict(k="d90", label="90 kun natijasi", ph="...")]),
    check=dict(h2="M8 nazorati", sub="Jo'nashdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Taklif, viza va ATAS shartlari tekshirilgan.", "Uy va naqd pul rejasi tayyor.", "Favqulodda aloqalar yozilgan.",
                      "Rahbar bilan birinchi uchrashuv kun tartibi tayyor.", "Ma'lumot va tadqiqot halolligi bo'yicha kirishish rejalangan.",
                      "30/60/90 natijalari o'lchanadigan.", "Ruhiy va akademik yordam kanallari oldindan topilgan."]),
    art_title="Jo'nash oldi nazorat ro'yxati va 90 kunlik reja", art_short="Reja",
    art=[("Taklif shartlari", ["shart", "a1"]), ("Viza va ATAS", ["viza", "a2"]), ("Uy va xavfsizlik", ["uy", "a3"]), ("Kirishish", ["a4"]),
         ("30/60/90", ["d30", "d60", "d90", "a5"]), ("Karyera", ["a6"])],
    tip="Universitetning talabalar maslahat xizmatini birinchi haftada toping, muammo chiqishini kutmang.",
    sources=f"{LEEDS}; {ATAS}; {VISA}; {UKRIEXP}; {UKRIO}. {STD}",
)
