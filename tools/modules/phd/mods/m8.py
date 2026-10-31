from common import LEEDS, ATAS, VISA, UKRI_SOE, UKRIO, HOL, STD

MOD = dict(
    title="Qabuldan keyingi tayyorgarlik va birinchi 90 kun",
    desc="PhD Lab M8: taklif shartlarini yopish, viza va ATAS, uy, xavfsizlik va boshlang'ich xarajat, tadqiqotga kirishish tizimi, 90 kunlik ilmiy ritm, karyera yo'llari. Natija: jo'nash oldi nazorat ro'yxati va 90 kunlik tadqiqot rejasi.",
    lead="Taklif shartlarini bajarasiz, viza va hujjatlarni tartibga solasiz va doktoranturaning birinchi 90 kunini aniq natijalar bilan rejalaysiz.",
    hero="seedling", weeks="1–3 (+90 kun)", next="", next_href="",
    goals=[("shield", "Jo'nash oldi nazorat ro'yxati", "taklif shartlari, viza, ATAS, uy, pul"),
           ("calendar", "90 kunlik tadqiqot rejasi", "30/60/90 kunlik o'lchanadigan natijalar"),
           ("seedling", "Ko'nikmalar yo'l xaritasi", "3 yillik, 2 karyera yo'li")],
    warn=f"Kompas Lab viza bo'yicha yuridik maslahat bermaydi va viza natijasiga ta'sir qilmaydi. Viza va ATAS qoidalari shaxsiy holat, fan va davlatga bog'liq: rasmiy sahifa va universitet xatini o'qing. Faktlar {HOL}.",
    lessons=[
        dict(t="Taklif shartlarini yopish", short="Shartlar", min=25, kind="✅ Ro'yxat", ic="shield",
             hook="Taklifni qabul qilish dasturga yozilishning oxirgi qadami bo'lmasligi mumkin. Shartli taklifdagi har band yopilganini hujjat bilan ko'rsatish kerak.",
             body=f"""<ul><li>Diplom va yakuniy transkript</li><li>Til sertifikati</li><li>Depozit (bo'lsa)</li><li>Moliyalashtirish tasdig'i</li><li>Immigratsiya hujjatlari</li><li>Boshlanish sanasi va rahbar tasdig'i</li></ul>
<p>Shartlar, muddatlar va rasmiy qabul holatini portal orqali kuzating. Noaniq band bo'lsa, qabul bo'limidan yozma aniqlik so'rang.</p>
<div class="box info">Shartli akademik taklif qo'lingizda bo'lsa ham, moliyalashtirish xati shartlari alohida tekshiriladi.</div>
<div class="box warn">\"Taklif olindi\" va \"shartsiz va moliyalashtirilgan\" degan holatlarni aralashtirmang.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Har shart uchun: kim bajaradi, qachongacha, qaysi hujjat isbotlaydi.",
             task="<ul><li>Taklifdagi barcha shartlarni yozing.</li><li>Har biriga mas'ul va sana qo'ying.</li><li>Bajarilganini isbotlovchi hujjatni saqlang.</li></ul>",
             ph="Shart 1: ... — mas'ul: ... — sana: ... — dalil: ..."),
        dict(t="Viza, ATAS va immigratsiya", short="Viza", min=30, kind="🛂 Rasmiy", ic="scroll",
             hook="Viza va tadqiqot ruxsatnomasi qoidalari shaxsiy holatga, fanga va davlatga bog'liq. Forumdagi o'tgan yilgi javob sizning holatingiz uchun dalil emas.",
             body=f"""<h4>Buyuk Britaniya ({HOL})</h4>
<ul><li><b>Talaba vizasi:</b> Buyuk Britaniyadan tashqarida ariza kurs boshlanishidan eng erta 6 oy oldin beriladi (GOV.UK).</li><li><b>ATAS:</b> magistratura yoki doktorantura darajasidagi ayrim fanlar uchun, ozod etilgan davlatlar fuqarolaridan tashqari nomzodlarga kerak. Fan CAH3 kodi bilan aniqlanadi; kod odatda taklif xatida yoziladi yoki universitet alohida tasdiqlaydi. O'zbekiston ozod etilgan davlatlar ro'yxatida yo'q.</li></ul>
<p>Boshqa mamlakatlar uchun o'sha davlatning rasmiy immigratsiya organi va universitet xalqaro bo'limi sahifasidan foydalaning.</p>
<div class="box info">Geofizika yoki muhandislik loyihasi ATAS talabiga tushishi mumkin, lekin avtomatik \"shart\" demang: taklif xatidagi CAH3 kodi va universitet xati hal qiladi.</div>
<div class="box warn">ATAS kerak bo'lsa, u viza arizasidan oldin olinadi: ko'rib chiqish vaqtini GOV.UK sahifasidan tekshirib, kalendarga zaxira bilan qo'ying.</div>
<div class="srcs">Manba: {VISA}; {ATAS}. {HOL}.</div>""",
             take="Viza: kurs boshlanishidan eng erta 6 oy oldin. ATAS: CAH3 kodi va fuqarolikka bog'liq, vizadan oldin. O'zbekiston ozod etilganlar ro'yxatida yo'q.",
             quiz=[("ATAS Buyuk Britaniyada hamma talabalar uchun majburiy.", "n", "Noto'g'ri: fuqarolik va CAH3 kodiga bog'liq."),
                   ("O'zbekiston fuqarosi ATAS dan ozod etilgan davlatlar ro'yxatida emas.", "t", "To'g'ri (GOV.UK, 24.03.2026 holatiga)."),
                   ("Etika ruxsati kerak bo'lsa, ma'lumot yig'ib bo'lgach olinadi.", "n", "Noto'g'ri: ruxsat ish boshlanishidan oldin olinadi."),
                   ("Viza bo'yicha kurs xulosasi shaxsiy yuridik maslahat o'rnini bosmaydi.", "t", "To'g'ri: rasmiy manba va kerak bo'lsa mutaxassis.")],
             task="<ul><li>Talaba vizasi sahifasini oching.</li><li>ATAS sizga tegishli-tegishli emasligini tekshiring.</li><li>Muddatlar va hujjatlar ro'yxatini tuzing.</li></ul>",
             ph="Kurs boshlanishi: ... → viza arizasi ... dan erta emas; ATAS: kerak/kerak emas (CAH3: ...); hujjatlar: ..."),
        dict(t="Uy, xavfsizlik va boshlang'ich xarajat", short="Uy", min=25, kind="🏠 Amaliy", ic="money",
             hook="Birinchi oyda ilmiy ishni boshlash uchun asosiy ehtiyojlar oldindan hal qilingan bo'lishi kerak: uy, aloqa, bank, sog'liq.",
             body="""<ul><li>Ijara shartnomasi va depozit</li><li>Kommunal xizmatlar va yo'l</li><li>Tibbiy ro'yxatdan o'tish va sug'urta</li><li>Bank hisobi va telefon</li><li>Favqulodda aloqa raqamlari</li></ul>
<p>Universitetning xalqaro talabalar xizmati va shahar rasmiy sahifalarini toping. Qo'shimcha ishga tayanishdan oldin viza shartlarini tekshiring.</p>
<div class="box info">Stipendiya bir oy kechiksa, boshlang'ich ijara uchun naqd pul bo'lishi muhim (M6 hisob-kitobi).</div>
<div class="box warn">Uy uchun oldindan pul so'raydigan va faqat messenjer orqali bog'lanadigan vositachilardan ehtiyot bo'ling: shartnomani ko'rmasdan pul o'tkazmang.</div>""",
             take="60 kunlik naqd pul rejasi, 3 ta ishonchli yordam aloqasi, o'qilgan ijara shartnomasi.",
             task="<ul><li>60 kunlik naqd pul rejasini tuzing.</li><li>3 ta ishonchli yordam aloqasini toping.</li><li>Uy shartnomasini o'qing va savollarni yozing.</li></ul>",
             ph="60 kun: ijara ..., depozit ..., ovqat ... Aloqalar: 1) universitet ... 2) ... 3) ..."),
        dict(t="Tadqiqotga kirishish tizimi", short="Kirishish", min=25, kind="🧭 Tizim", ic="compass",
             hook="Doktoranturani boshlash \"tadqiqotni boshladim\" degan mavhum his bo'lmasligi kerak. Birinchi oyda tizim qursangiz, keyingi yillar osonlashadi.",
             body=f"""<ul><li>Universitetga kirishish ([[induction]]) va etika bo'yicha kurs</li><li>Ma'lumotlarni boshqarish va laboratoriya xavfsizligi</li><li>Hisoblash resurslariga kirish</li><li>Rahbar bilan uchrashuv tartibi</li><li>Bosqichlar va treninglar rejasi</li></ul>
<p>Loyiha qamrovi birinchi oylarda o'zgarishi mumkin: kelishilgan uchrashuv qaydlari va xavflar jadvali buni boshqaradi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> 1–2-hafta: kirish huquqlari va adabiyot xaritasi; 3–4-hafta: asosiy usul va takrorlanadigan muhit. Bu namuna: har fan uchun qat'iy jadval emas.</div>
<div class="box warn">Maxfiy ma'lumot va xavfsizlik ruxsatisiz dala ishini boshlamang.</div>
<div class="srcs">Manba: {UKRI_SOE}; {UKRIO}.</div>""",
             take="Kirishish ro'yxati, rahbar bilan uchrashuv tartibi va kun tartibi, trening talablari.",
             task="<ul><li>Kirishish nazorat ro'yxatini tuzing.</li><li>Birinchi uchrashuv kun tartibini yozing.</li><li>Trening talablarini belgilang.</li></ul>",
             ph="Ro'yxat: ... Uchrashuv kun tartibi: 1) ... 2) ... Treninglar: ..."),
        dict(t="90 kunlik ilmiy ritm", short="90 kun", min=25, kind="📅 Ritm", ic="calendar",
             hook="Ilmiy ishda bandlik emas, tekshiriladigan natija va fikr-mulohaza muhim. 90 kunlik reja birinchi chorakni aniq natijalarga aylantiradi.",
             body="""<div class="tbl"><table><thead><tr><th>Davr</th><th>Natija</th></tr></thead><tbody>
<tr><td>30 kun</td><td>Adabiyot xaritasi va ishchi savol</td></tr>
<tr><td>60 kun</td><td>Bajarilishi mumkinlik sinovi va asosiy usul</td></tr>
<tr><td>90 kun</td><td>Qayta ko'rilgan tadqiqot rejasi va xavflar tahlili</td></tr></tbody></table></div>
<p>Bosqichlar soha va rahbar bilan kelishiladi. Haftalik qayd: bajarildi, o'rganildi, to'xtab qoldi, keyingi qadam.</p>
<div class="box info">\"Har kuni 8 soat ishlayman\" o'rniga \"2 hafta ichida ochiq ma'lumotda asosiy usulni takrorlash va xatolar jadvali\" aniqroq.</div>
<div class="box warn">Qattiq kunlik reja va o'zini ayblash ilmiy sifat o'rnini bosmaydi: charchoq belgilarida universitet yordam xizmatlariga murojaat qiling.</div>""",
             take="30/60/90 kunlik natijalar, haftalik qayd, rahbar bilan muntazam ko'rib chiqish.",
             task="<ul><li>30/60/90 kunlik bosqichlarni yozing.</li><li>Haftalik ko'rib chiqish tartibini tuzing.</li><li>Xavf belgilari va yordam kanallarini yozing.</li></ul>",
             ph="30 kun: ...; 60 kun: ...; 90 kun: ...; haftalik qayd: ... kuni"),
        dict(t="Karyera va foydali tadqiqot", short="Karyera", min=25, kind="🌱 Yo'l", ic="seedling",
             hook="PhD davomida ham akademik, ham boshqa professional yo'llar ochiq qolishi kerak. Ko'nikmalarni birinchi yildan rejalang.",
             body="""<ul><li>O'tkaziladigan ko'nikmalar: dasturlash, ma'lumot tahlili, yozish, taqdimot, loyiha boshqaruvi</li><li>Sanoat hamkorligi va o'qitish tajribasi</li><li>Takrorlanadigan tadqiqot va ochiq fan</li><li>Mualliflik odobi va ilmiy halollik</li></ul>
<p>O'zbekistonga qaytish, xalqaro tadqiqot yoki sanoat yo'llarini har biri uchun kerakli kompetensiya va real imkoniyat bilan baholang.</p>
<div class="box info">Bitta ilmiy kod ombori, poster va sanoat misoli akademik va sanoat portfeliga turlicha yordam beradi.</div>
<div class="box warn">PhD yakuni doimiy ish yoki immigratsiyani kafolatlamaydi.</div>""",
             take="3 yillik ko'nikmalar xaritasi, 2 ta karyera yo'li, birinchi 90 kun uchun bitta ko'nikma.",
             task="<ul><li>3 yillik ko'nikmalar xaritasini chizing.</li><li>2 ta ehtimoliy karyera yo'lini solishtiring.</li><li>Birinchi 90 kun uchun bitta ko'nikma tanlang.</li></ul>",
             ph="1-yil: ...; 2-yil: ...; 3-yil: ... Yo'llar: A ..., B ... Birinchi ko'nikma: ..."),
    ],
    tool=dict(id="reja90", short="90 kun", h2="Birinchi 90 kunlik tadqiqot rejasi", sub="Ish boshlashdan oldingi ruxsatlar, ma'lumot va rahbar bilan uchrashuvlarni rejalang.",
              h3="90 kunlik reja", tag="5 maydon", ic="seedling", btn="Rejani saqlash", badge="Boshlovchi", min=4,
              fields=[dict(k="boshlanish", label="Dastur boshlanish sanasi", type="date"),
                      dict(k="d30", label="1–30 kun: kirishish va resurslar", type="area", ph="Rahbar bilan uchrashuv, uskunalar, ma'lumotga kirish"),
                      dict(k="d60", label="31–60 kun: adabiyot va sinov", type="area", ph="Qidiruv jurnali, metod sinovi, xavflar jadvali"),
                      dict(k="d90", label="61–90 kun: ko'rib chiqish va bosqich", type="area", ph="Sinov natijasi, etika, keyingi chorak"),
                      dict(k="halollik", label="Ilmiy halollik, etika va ma'lumot boshqaruvi", type="area", ph="Qaysi ruxsat, ma'lumotga kirish va xavfsizlik talab qilinadi?")]),
    check=dict(h2="M8 nazorati", sub="Rejani yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Taklif shartlari va dalillari yozilgan.", "Viza va ATAS holati rasmiy sahifadan tekshirilgan.",
                      "Uy va 60 kunlik naqd pul rejasi bor.", "Rahbar bilan birinchi uchrashuv kun tartibi tayyor.",
                      "Etika va ma'lumot boshqaruvi talablari aniqlangan.", "30/60/90 kunlik o'lchanadigan natijalar yozilgan.",
                      "Yordam kanallari aniqlangan.", "Har o'zgaruvchan talab yonida sana va manba bor."]),
    art_title="Jo'nash oldi nazorat ro'yxati va 90 kunlik reja", art_short="Reja",
    art=[("Taklif shartlari", ["a1"]), ("Viza va ATAS", ["a2"]), ("Uy va pul", ["a3"]), ("Kirishish", ["a4"]),
         ("90 kunlik reja", ["boshlanish", "d30", "d60", "d90", "a5"]), ("Halollik va etika", ["halollik"]), ("Karyera", ["a6"])],
    tip="Birinchi 90 kunda katta natija emas, ishonchli tizim quring: kirish huquqlari, takrorlanadigan muhit va rahbar bilan muntazam uchrashuv.",
    sources=f"{LEEDS}; {VISA}; {ATAS}; {UKRI_SOE}; {UKRIO}. {STD}",
)
