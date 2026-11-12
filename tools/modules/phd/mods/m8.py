from common import LEEDS, ATAS, VISA, UKRIEXP, UKRIO, HOL, STD

MOD = dict(
    title="Qabuldan keyingi tayyorgarlik va birinchi 90 kun",
    desc="PhD Lab M8: taklif shartlarini bajarish, viza va ATAS, turar joy, xavfsizlik va dastlabki xarajat, tadqiqotni boshlash, 90 kunlik ish tartibi, karyera. Natija: jo'nash oldi nazorat ro'yxati va 90 kunlik reja.",
    lead="Taklifni qabul qilganingizdan keyin ham ish ko'p. Bu modulda taklif shartlarini bajarasiz, viza va turar joy masalasini hal qilasiz va birinchi 90 kunni <b>o'lchasa bo'ladigan natijalar</b> bilan rejalaysiz.",
    hero="seedling", weeks="1–3", next="", next_href="",
    goals=[("shield", "Jo'nash oldi nazorat ro'yxati (Pre-departure checklist)", "har shart: kim bajaradi va qachongacha"),
           ("calendar", "30/60/90 kunlik reja", "har bosqich natijasi bilan"),
           ("bulb", "Rahbar bilan birinchi uchrashuv rejasi", "kutilmalar, uchrashuvlar tartibi, o'quv kurslari")],
    warn="Bu kurs huquqiy yoki immigratsiya maslahati bermaydi. Viza va ATAS bo'yicha yakuniy javobni rasmiy idora va universitetingiz beradi. Dastlabki 90 kun rejasi universitetdagi yordam xizmatlari o'rnini bosmaydi; tadqiqot dizayni, etika va nashr bo'yicha chuqur mavzular bu modulga kirmaydi.",
    lessons=[
        dict(t="Taklif shartlarini bajarish", short="Shartlar", min=20, kind="✅ Nazorat", ic="shield",
             hook="Taklifni qabul qilish bilan dasturga yozilish tugamasligi mumkin. <b>Bitta shart</b> bajarilmasa, taklif kuchini yo'qotishi mumkin.",
             body=f"""<p>Tekshiring: diplom, til sertifikati, depozit, moliya tasdig'i, immigratsiya hujjati, boshlanish sanasi va rahbar tasdig'i bir-biriga mos keladimi. Shartlar, muddatlar va rasmiy qabul portal orqali kuzatiladi. Tushunarsiz bandni qabul bo'limidan rasmiy so'rang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Qo'lingizda shartli akademik taklif bo'lsa, grant xatidagi shartlarni alohida tekshiring.</div>
<div class="box warn"><i>“Taklif keldi”</i> bilan <i>“shartsiz va moliyalashtirilgan”</i> degan holatni aralashtirmang.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Har shart uchun kim bajarishi, qachongacha va bajarilganini ko'rsatadigan hujjat yoziladi.",
             task="<ul><li>Taklifdagi barcha shartlarni yozing.</li><li>Har biri uchun kim bajarishini va sanasini belgilang.</li><li>Bajarilganini ko'rsatadigan hujjatni saqlang.</li></ul><p><b>O'zingizga savol:</b> har shart bajarilganini qaysi hujjat ko'rsatadi?</p>",
             ph="Shart 1: diplom (men, ... sanagacha, dalil ...) ; 2: til ... ; 3: depozit ..."),
        dict(t="Viza, ATAS va immigratsiya", short="Viza", min=30, kind="🛂 Rasmiy", ic="lock",
             hook="Viza va tadqiqot ruxsati qoidalari shaxsiy holatingiz, faningiz va mamlakatga bog'liq. <b>Forumdagi o'tgan yilgi javobga</b> tayanmang.",
             body=f"""<p>Buyuk Britaniya uchun talaba vizasi ([[Student visa]]) va ba'zi fanlarda kerak bo'ladigan [[ATAS]] (Academic Technology Approval Scheme) talabini GOV.UK va universitet ko'rsatmasidan tekshiring.</p>
<ul><li>ATAS hammaga kerak emas: u fuqarolik (ozod qilingan mamlakatlar ro'yxati bor) va universitet bergan fan kodiga ([[CAH3]]) qarab aniqlanadi.</li><li>GOV.UK ma'lumotiga ko'ra, ATAS arizasi <b>kamida 30 ish kuni (6 hafta)</b> ko'rib chiqiladi, aprel–avgustda bundan uzoqroq bo'lishi mumkin.</li><li>Talaba vizasida ishlash mumkinligi va necha soat ishlash o'qish turi va vaqtiga bog'liq: buni GOV.UK sahifasidan o'qing.</li></ul>
<p>Boshqa mamlakatlar uchun o'sha mamlakatning rasmiy immigratsiya idorasiga murojaat qiling.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Geofizika yoki muhandislik loyihasi ATAS tekshiruviga tushishi mumkin, lekin buni oldindan aniq aytib bo'lmaydi: universitet taklifidagi fan kodi hal qiladi.</div>
<div class="box warn">Immigratsiya qoidalarini faqat rasmiy sahifadan oling; forumdagi javoblar eskirgan bo'lishi mumkin.</div>
<div class="srcs">Manba: {VISA}; {ATAS}. {HOL}.</div>""",
             take="Viza va ATAS talabini rasmiy sahifadan tekshiring; ATAS uchun rejada kamida 6 hafta qoldiring.",
             quiz=[("ATAS Buyuk Britaniyadagi barcha xalqaro PhD talabalariga majburiy.", "n", "Noto'g'ri: fuqarolik va fan kodiga (CAH3) bog'liq."),
                   ("GOV.UK ma'lumotiga ko'ra, ATAS kamida 30 ish kunida ko'rib chiqiladi.", "t", "To'g'ri: aprel–avgustda uzoqroq bo'lishi mumkin."),
                   ("Ish haqini viza shartlarini tekshirmasdan byudjetga qo'shsa bo'ladi.", "n", "Noto'g'ri: ishlash huquqi o'qish turi va vaqtiga bog'liq."),
                   ("PhD ni tamomlash doimiy ish yoki yashash huquqini kafolatlamaydi.", "t", "To'g'ri: bu yo'llar alohida ko'rib chiqiladi.")],
             task="<ul><li>Buyuk Britaniya yoki boshqa mamlakatning rasmiy viza sahifasini oching.</li><li>ATAS sizga tegishli-tegishli emasligini tekshiring.</li><li>Muddatlar va hujjatlar ro'yxatini tuzing.</li></ul><p><b>O'zingizga savol:</b> sizga yakuniy shaxsiy javobni qaysi idora bera oladi?</p>",
             ph="Viza: ..., hujjatlar ... ; ATAS: kerak yoki kerak emas (fan kodi ...) ; ariza sanasi ..."),
        dict(t="Turar joy, xavfsizlik va dastlabki xarajat", short="Uy", min=25, kind="🏠 Amaliy", ic="hourglass",
             hook="Birinchi oyda ilmiy ishni boshlash uchun turmushdagi asosiy masalalar <b>oldindan hal bo'lgan</b> bo'lishi kerak.",
             body=f"""<p>Ro'yxat tuzing: ijara shartnomasi, depozit, kommunal to'lovlar, yo'l, shifokorda ro'yxatdan o'tish, bank hisobi, telefon, favqulodda aloqalar va sug'urta. Universitetning xalqaro talabalar xizmatini va shaharning rasmiy saytlarini toping.</p>
<p>Qo'shimcha ishga umid qilishdan oldin viza shartlarini tekshiring.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Stipendiya bir oy kechiksa, turar joy uchun qo'lingizda naqd pul bo'lishi juda muhim.</div>
<div class="box warn">Soxta ijara e'lonlari va faqat Telegram orqali gaplashadigan vositachilardan ehtiyot bo'ling.</div>""",
             take="60 kunlik naqd pul rejasi, 3 ta ishonchli yordam aloqasi va o'qib chiqilgan ijara shartnomasi.",
             task="<ul><li>60 kunlik naqd pul rejasini tuzing.</li><li>3 ta ishonchli yordam aloqasini toping.</li><li>Ijara shartnomasini o'qib chiqing.</li></ul><p><b>O'zingizga savol:</b> yetib borgan kuningiz telefon, manzil, yordam aloqasi va pul tayyormi?</p>",
             ph="Naqd pul: ... ; aloqalar: 1) universitet xizmati ... 2) ... 3) ... ; ijara: ..."),
        dict(t="Tadqiqotni boshlash", short="Boshlash", min=25, kind="🧭 Tizim", ic="compass",
             hook="Birinchi haftalarda nima qilishni oldindan rejalang, aks holda vaqt <b>tushunarsiz ishlarga</b> ketadi.",
             body=f"""<p>Tartibga soling: universitetga kirish tadbirlari, etika bo'yicha kirish kursi, ma'lumotlarni boshqarish, laboratoriya xavfsizligi, hisoblash resurslariga kirish, rahbar bilan uchrashuvlar tartibi, asosiy bosqichlar va o'quv rejasi.</p>
<p>Loyiha chegarasi birinchi oylarda o'zgarishi mumkin. Har uchrashuvdan keyin kelishilgan narsalarni yozib boring va xavflar ro'yxatini yuriting. UKRI kutilmalar bayoni talaba va rahbarning majburiyatlarini ko'rsatadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> 1–2-hafta: tizimlarga kirish va adabiyot xaritasi; 3–4-hafta: taqqoslash nuqtasi ([[baseline]]) va qayta ishga tushadigan dastur muhiti. Bu umumiy namuna, har fan uchun qat'iy jadval emas.</div>
<div class="box warn">Maxfiy ma'lumot bilan ishlashni va dala ishini xavfsizlik ruxsatisiz boshlamang.</div>
<div class="srcs">Manba: {UKRIEXP}; {UKRIO}. {HOL}.</div>""",
             take="Boshlash ro'yxati, birinchi uchrashuv rejasi va o'quv talablari birinchi oyning asosini tashkil qiladi.",
             task="<ul><li>Boshlash uchun nazorat ro'yxatini tuzing.</li><li>Rahbar bilan birinchi uchrashuv rejasini yozing.</li><li>O'quv kurslari talablarini belgilang.</li></ul><p><b>O'zingizga savol:</b> birinchi uchrashuvda nimani ko'rsatasiz?</p>",
             ph="Boshlash: ... ; uchrashuv: 1) kutilmalar 2) uchrashuvlar tartibi 3) ... ; kurslar: ..."),
        dict(t="90 kunlik ish tartibi", short="90 kun", min=25, kind="📅 Tartib", ic="calendar",
             hook="Ilmiy ishda band bo'lib yurishdan ko'ra <b>tekshirsa bo'ladigan natija</b> va fikr-mulohaza muhimroq.",
             body=f"""<ul><li><b>30 kun</b>: adabiyot xaritasi va ishchi savol.</li><li><b>60 kun</b>: rejani kichik sinovda tekshirish va taqqoslash nuqtasi.</li><li><b>90 kun</b>: qayta ko'rilgan tadqiqot rejasi va xavflar tahlili.</li></ul>
<p>Bosqichlarni soha va rahbar bilan kelishing. Haftalik yozuv (nima qilindi, nima o'rganildi, nima to'xtab qoldi, keyingi qadam) fikr-mulohaza olishni osonlashtiradi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> <i>“Har kuni 8 soat ishlayman”</i> o'rniga <i>“2 hafta ichida ochiq ma'lumotda taqqoslash natijasini takrorlayman va xatolar jadvalini tuzaman”</i> deb yozing.</div>
<div class="box warn">Qattiq kundalik intizom va o'zini ayblash ilmiy sifatga yordam bermaydi.</div>""",
             take="30, 60 va 90 kunlik bosqichlar natijasi bilan yoziladi va haftalik yozuv bilan kuzatiladi.",
             task="<ul><li>30, 60 va 90 kunlik bosqichlarni yozing.</li><li>Haftalik ko'rib chiqish kunini belgilang.</li><li>Ogohlantiruvchi belgilar va maslahat oladigan joylarni yozing.</li></ul><p><b>O'zingizga savol:</b> 90 kundan keyin nimani bilib olgan bo'lasiz?</p>",
             ph="30: ... ; 60: ... ; 90: ... ; haftalik ko'rib chiqish: juma ..."),
        dict(t="Karyera va foydali tadqiqot", short="Karyera", min=20, kind="🌱 Yo'l", ic="seedling",
             hook="PhD davomida akademik va boshqa kasbiy yo'llarni ochiq saqlang. <b>Birinchi yildayoq</b> bitta yo'lga bog'lanib qolish xavfli.",
             body=f"""<p>Rejalang: boshqa sohalarda ham kerak bo'ladigan ko'nikmalar, sanoat bilan hamkorlik, dars berish, ilmiy muloqot, natijasini takrorlasa bo'ladigan tadqiqot va karyera bo'yicha maslahatchi. Ochiq fan, halol mualliflik va ilmiy halollik keyinchalik ham sizga foyda beradi.</p>
<p>O'zbekistonga qaytish, xalqaro ilmiy ish yoki sanoat yo'llarini har biri uchun kerakli ko'nikma va real imkoniyat bilan baholang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Bitta ilmiy kod omborxonasi, poster va sanoatdan olingan misol akademik va sanoat portfeliga turlicha foyda beradi.</div>
<div class="box warn">PhD ni tamomlash doimiy ish yoki yashash huquqini kafolatlamaydi.</div>
<div class="srcs">Manba: {UKRIO}. {HOL}.</div>""",
             take="3 yillik ko'nikmalar rejasi va 2 ta karyera yo'li; birinchi 90 kunda bitta ko'nikma tanlanadi.",
             task="<ul><li>3 yillik ko'nikmalar rejasini chizing.</li><li>2 ta mumkin bo'lgan karyera yo'lini solishtiring.</li><li>Birinchi 90 kun uchun bitta ko'nikma tanlang.</li></ul><p><b>O'zingizga savol:</b> tadqiqotingiz kim uchun va qanday foyda beradi?</p>",
             ph="Ko'nikmalar: 1-yil ..., 2-yil ..., 3-yil ... ; yo'llar: ... / ... ; 90 kun: ..."),
    ],
    tool=dict(id="reja", short="90 kun", h2="30/60/90 kunlik reja", sub="Birinchi o'lchasa bo'ladigan tadqiqot natijalarini yozing.",
              h3="Jo'nash va 90 kun", tag="6 maydon", ic="calendar", btn="Rejani saqlash", badge="Yo'lboshchi", min=5,
              fields=[dict(k="shart", label="Taklif shartlari holati", type="area", ph="Diplom ✓, til ✓, moliya xati ..., viza ..."),
                      dict(k="viza", label="Viza va ATAS", type="area", ph="Viza arizasi sanasi ..., ATAS: ..."),
                      dict(k="uy", label="Turar joy va dastlabki pul", type="area", ph="Ijara ..., depozit ..., 60 kunlik naqd ..."),
                      dict(k="d30", label="30 kun natijasi", ph="Adabiyot xaritasi va ishchi savol"),
                      dict(k="d60", label="60 kun natijasi", ph="..."),
                      dict(k="d90", label="90 kun natijasi", ph="...")]),
    check=dict(h2="M8 nazorati", sub="Jo'nashdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Taklif, viza va ATAS shartlari tekshirilgan.", "Turar joy va naqd pul rejasi tayyor.", "Favqulodda aloqalar yozilgan.",
                      "Rahbar bilan birinchi uchrashuv rejasi tayyor.", "Ma'lumot bilan ishlash va ilmiy halollik bo'yicha kurslar rejalangan.",
                      "30/60/90 natijalarini o'lchasa bo'ladi.", "Ruhiy va akademik yordam xizmatlari oldindan topilgan."]),
    art_title="Jo'nash oldi nazorat ro'yxati va 90 kunlik reja", art_short="Reja",
    art=[("Taklif shartlari", ["shart", "a1"]), ("Viza va ATAS", ["viza", "a2"]), ("Turar joy va xavfsizlik", ["uy", "a3"]), ("Tadqiqotni boshlash", ["a4"]),
         ("30/60/90", ["d30", "d60", "d90", "a5"]), ("Karyera", ["a6"])],
    tip="Universitetning talabalarga maslahat xizmatini birinchi haftadayoq toping; muammo chiqishini kutib o'tirmang.",
    sources=f"{LEEDS}; {ATAS}; {VISA}; {UKRIEXP}; {UKRIO}. {STD}",
)
