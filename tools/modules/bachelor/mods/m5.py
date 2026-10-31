from common import SAT, ACT, IELTS, TOEFL, DET, APO, MYGOV, CDS, HOL, STD

MOD = dict(
    title="Baholar va testlar",
    desc="Bachelor Lab M5: attestat baholarini taqdim etish, transkript va tarjima, IELTS/TOEFL/Duolingo strategiyasi, SAT va ACT, test talabi siyosatlari. Natija: test kalendari va baholar jadvali.",
    lead="Baholar va testlar arizaning raqamli qismi. Ularni to'g'ri taqdim etmasangiz, kuchli natija ham noaniq ko'rinadi. Bu modulda baholaringizni universitet talablari bilan solishtirasiz va testlar kalendarini tuzasiz.",
    hero="chart", weeks="2", next="M6 Yutuqlar, CV va hujjatlar", next_href="bachelor-lab-m6.html",
    goals=[("chart", "Baholar jadvali", "asl shkalada, universitet talablari bilan solishtirilgan"),
           ("calendar", "Test kalendari", "til testi va SAT/ACT: sana, ro'yxatdan o'tish, qayta topshirish zaxirasi"),
           ("shield", "Test siyosati xaritasi", "har universitet: talab qilinadi, ixtiyoriy yoki hisobga olinmaydi")],
    warn=f"Test talablari, minimal ballar va imtihon narxlari universitet va yilga qarab o'zgaradi. Bu moduldagi misollar umumiy; har universitet uchun rasmiy sahifani tekshiring ({HOL}).",
    lessons=[
        dict(t="Attestat baholarini taqdim etish", short="Baholar", min=25, kind="🎯 Mini-test", ic="chart",
             hook="Komissiya O'zbekiston baholash tizimini bilmasligi mumkin. \"4.7\" deb yozib qo'yish yetmaydi: qaysi shkala, qaysi fanlar, qaysi yillar?",
             body="""<h4>Uch qoida</h4>
<ol><li><b>Asl shkalada yozing.</b> \"4.7 / 5\" yoki \"86 / 100\". O'zingiz AQSh GPA'siga aylantirmang: universitetlar baholarni o'z usuli bilan qayta hisoblaydi.</li>
<li><b>Shkalani tushuntiring.</b> Ariza formasida yoki qo'shimcha izohda: 5 eng yuqori, 3 o'tish bahosi.</li>
<li><b>Fanlarni ko'rsating.</b> Matematika, fizika, informatika kabi sohangizga yaqin fanlar baholari umumiy o'rtachadan muhimroq bo'lishi mumkin.</li></ol>
<h4>Maktab hisoboti</h4>
<p>AQShda maktab o'z haqida hisobot ([[school profile]]) yuboradi: baholash tizimi, sinfdagi o'quvchilar soni, fanlar. O'zbekiston maktablarida bunday hujjat ko'pincha yo'q. M8 da uni direktor bilan qanday tayyorlashni ko'rasiz.</p>
<div class="box warn"><b>\"GPA to'qimang.\"</b> Internetdagi kalkulyator bilan hisoblangan \"3.9 GPA\" rasmiy hujjat emas. Shkalasiz yoki tasdiqlanmagan raqam ishonchni pasaytiradi.</div>""",
             take="Baholarni asl shkalada yozing, shkalani tushuntiring va sohangizga yaqin fanlarni ko'rsating. O'zboshimchalik bilan GPA hisoblamang.",
             quiz=[("Arizaga 5 ballik bahoni o'zim 4.0 GPA'ga aylantirib yozishim kerak.", "n", "Noto'g'ri: asl shkalada yozing; universitet o'zi qayta hisoblaydi."),
                   ("Sohaga yaqin fanlar baholari alohida ahamiyatga ega bo'lishi mumkin.", "t", "To'g'ri: muhandislik uchun matematika va fizika, informatika uchun matematika ko'riladi."),
                   ("School profile maktab haqidagi kontekst hujjati.", "t", "To'g'ri: AQSh kollejlari baholarni shu kontekstda o'qiydi."),
                   ("Shkalani tushuntirish shart emas, hamma 5 ballik tizimni biladi.", "n", "Noto'g'ri: xorijiy xodim bilmasligi mumkin.")],
             task="<ul><li>Oxirgi 3 yildagi baholaringizni asl shkalada fanlar bo'yicha yozing.</li><li>Sohangizga yaqin 3 fanni belgilang va ularning o'rtachasini hisoblang.</li></ul>",
             ph="9-sinf: matematika 5, fizika 5 ... ; sohaga yaqin o'rtacha: ..."),
        dict(t="Transkript va attestat", short="Transkript", min=25, kind="📄 Hujjat", ic="scroll",
             hook="Bitiruvdan oldin ariza berasiz, demak attestat hali yo'q. Universitet nima so'raydi va maktab nima bera oladi, oldindan aniqlang.",
             body=f"""<h4>Qaysi hujjat</h4>
<div class="tbl"><table><thead><tr><th>Hujjat</th><th>Kim beradi</th><th>Qachon kerak</th></tr></thead><tbody>
<tr><td>Baholar ko'chirmasi (transkript)</td><td>Maktab: oxirgi 3–4 yil fanlar bo'yicha</td><td>Ariza vaqtida</td></tr>
<tr><td>O'qish joyidan ma'lumotnoma</td><td>Maktab</td><td>Ariza vaqtida (kutilayotgan bitiruv sanasi bilan)</td></tr>
<tr><td>Attestat (asl)</td><td>Maktab, bitiruvda</td><td>Qabuldan keyin yoki shartli qabul shartini bajarishda</td></tr>
</tbody></table></div>
<h4>Tarjima va tasdiq</h4>
<ul><li>Ingliz tiliga tarjima: fan nomlari, baho shkalasi, maktab nomi va ismingiz pasportdagidek.</li>
<li>Ba'zi universitetlar notarial tarjima, ba'zilari maktab tasdiqlagan nusxa, ba'zilari apostil so'raydi (M6).</li>
<li>Ko'p universitetlar ariza vaqtida skanerlangan nusxani qabul qiladi, asl hujjatni qabuldan keyin so'raydi.</li></ul>
<h4>Ism va transliteratsiya</h4>
<p>Pasport, attestat, test sertifikati va ariza formasidagi ism harfma-harf bir xil bo'lsin. Farq bo'lsa (masalan Ulug'bek va [[Ulugbek]]), tarjimada pasport variantini ishlating va izohda ko'rsating.</p>
<div class="srcs">Manba: {APO}; {MYGOV}; universitetlarning hujjat talablari sahifalari. {HOL}.</div>""",
             take="Ariza vaqtida transkript va ma'lumotnoma, asl attestat odatda qabuldan keyin. Tarjimadagi ism pasport bilan harfma-harf bir xil bo'lsin.",
             task="<ul><li>Maktabingizdan qaysi hujjatlarni va qachon olishingiz mumkinligini aniqlang.</li><li>Ismingizning pasportdagi yozilishini va boshqa hujjatlardagi farqlarni yozing.</li></ul>",
             ph="Transkript: ... gacha. Ma'lumotnoma: ... Ism (pasport): ... Farqlar: ..."),
        dict(t="Ingliz tili testi strategiyasi", short="Til testi", min=30, kind="🗺 Test tanlovi", ic="books",
             hook="Uch xil test, har biri boshqa universitetlarda qabul qilinadi. Noto'g'ri test tanlasangiz, yaxshi natija ham ish bermaydi.",
             body=f"""<div class="tbl"><table><thead><tr><th>Test</th><th>Format</th><th>E'tibor bering</th></tr></thead><tbody>
<tr><td>IELTS Academic</td><td>Markazda yoki kompyuterda; 4 qism</td><td>UK uchun eng keng tarqalgan; UK vizasi uchun UKVI talabi bilan alohida variant kerak bo'lishi mumkin</td></tr>
<tr><td>TOEFL iBT</td><td>Kompyuterda; uydan topshirish varianti ham bor</td><td>AQShda keng qabul qilinadi</td></tr>
<tr><td>Duolingo English Test</td><td>Onlayn, uydan</td><td>Ko'p AQSh universitetlari qabul qiladi; UK va Yevropada kamroq. Har universitetda alohida tekshiring</td></tr>
</tbody></table></div>
<h4>Strategiya</h4>
<ol><li>Saralangan ro'yxatdagi universitetlar qabul qiladigan testlarni jadvalga yozing.</li>
<li>Hammasiga mos keladigan bitta testni tanlang.</li>
<li>Har universitetning minimal ballini va qism (masalan yozish) bo'yicha minimalni yozing.</li>
<li>Birinchi urinishni muddatdan kamida 3–4 oy oldin rejalang: qayta topshirishga vaqt qolsin.</li></ol>
<div class="box warn">Sertifikatning amal qilish muddati bor (ko'pincha 2 yil). Ariza va viza vaqtida amalda bo'lishini tekshiring.</div>
<div class="srcs">Manba: {IELTS}; {TOEFL}; {DET}. {HOL}.</div>""",
             take="Ro'yxatingizdagi hamma universitet qabul qiladigan bitta testni tanlang, qismlar bo'yicha minimalni yozing va qayta topshirishga 3–4 oy zaxira qo'ying.",
             task="<ul><li>Ro'yxatingizdagi universitetlar qabul qiladigan testlar va minimal ballarni yozing.</li><li>Tanlagan testingiz va birinchi urinish sanasini belgilang.</li></ul>",
             ph="... universiteti: IELTS 6.5 (har qism 6.0), TOEFL ..., DET ... Tanlov: ... ; sana: ..."),
        dict(t="SAT va ACT", short="SAT/ACT", min=25, kind="📝 Reja", ic="bulb",
             hook="SAT yoki ACT faqat AQSh (va ba'zi boshqa) universitetlari uchun kerak. Hamma uchun shart emas, lekin kerak bo'lsa, tayyorgarlik oylab davom etadi.",
             body=f"""<h4>Kimga kerak</h4>
<ul><li>AQSh universitetlariga ariza beradiganlar (test siyosatiga qarab, L5).</li>
<li>Ba'zi boshqa mamlakatlardagi universitetlar ham SAT natijasini qabul qiladi yoki qo'shimcha dalil sifatida ko'radi.</li>
<li>UK, Germaniya, Italiya va ko'p Osiyo universitetlari uchun odatda kerak emas.</li></ul>
<h4>SAT va ACT farqi</h4>
<p>SAT hozir raqamli (Digital SAT): matematika va o'qish-yozish bo'limlari. ACT ingliz tili, matematika, o'qish va ixtiyoriy fan bo'limlarini o'z ichiga oladi. Ikkalasi ham universitetlarda teng qabul qilinadi; sizga qaysi format qulayligini sinov testi bilan aniqlang.</p>
<h4>Tayyorgarlik vaqti</h4>
<p>Odatda 2–4 oy muntazam tayyorgarlik. College Board'ning bepul rasmiy sinov testlari (Bluebook ilovasi) bor.</p>
<h4>Topshirish joyi</h4>
<p>O'zbekistonda test markazlari va sanalar soni cheklangan; joylar tez to'lishi mumkin. Ro'yxatdan o'tishni imkon qadar erta qiling.</p>
<div class="srcs">Manba: {SAT}; {ACT}. {HOL}.</div>""",
             take="SAT yoki ACT asosan AQSh uchun. Sinov testi bilan formatni tanlang, 2–4 oy tayyorlaning va markazda joyni erta band qiling.",
             task="<ul><li>Ro'yxatingizda SAT yoki ACT talab qiladigan universitetlar bormi, aniqlang.</li><li>Kerak bo'lsa, bitta rasmiy sinov testini topshiring va natijani yozing.</li></ul>",
             ph="SAT kerak: ... Sinov testi natijasi: ... Maqsad ball: ..."),
        dict(t="Test talabi siyosatlari", short="Siyosat", min=20, kind="⚖️ Qaror", ic="shield",
             hook="\"Test ixtiyoriy\" degani \"test muhim emas\" degani emas. Ballni yuborish yoki yubormaslik strategik qaror.",
             body=f"""<div class="tbl"><table><thead><tr><th>Siyosat</th><th>Ma'nosi</th><th>Nima qilish</th></tr></thead><tbody>
<tr><td>Talab qilinadi ([[test-required]])</td><td>Ballsiz ariza ko'rib chiqilmaydi</td><td>Albatta topshiring</td></tr>
<tr><td>Ixtiyoriy ([[test-optional]])</td><td>Ball yubormasangiz ham ko'riladi</td><td>Ball universitetda qabul qilinganlar oralig'ining o'rtasi yoki yuqorisida bo'lsa, yuboring</td></tr>
<tr><td>Hisobga olinmaydi ([[test-blind]])</td><td>Ball yuborsangiz ham ko'rilmaydi</td><td>Vaqtni boshqa qismga sarflang</td></tr>
</tbody></table></div>
<p>Ba'zi tanlovli universitetlar so'nggi yillarda test talabini qayta joriy qildi. Xalqaro abituriyentlar uchun alohida qoida bo'lishi ham mumkin. Shuning uchun siyosatni har yili universitet sahifasidan tekshiring.</p>
<h4>Ballni solishtirish</h4>
<p>Universitetning Common Data Set'idagi C9 bo'limida qabul qilinganlarning 25- va 75-persentil ballari bor. Ballingiz 25-persentildan past bo'lsa, ixtiyoriy siyosatda yubormaslik haqida o'ylang.</p>
<div class="srcs">Manba: {CDS}; universitetlarning rasmiy qabul sahifalari. {HOL}.</div>""",
             take="Siyosat uch xil: talab qilinadi, ixtiyoriy, hisobga olinmaydi. Ixtiyoriyda ballingizni CDS'dagi oraliq bilan solishtirib yuborish yoki yubormaslikni hal qiling.",
             task="<ul><li>Har universitetingizning test siyosatini rasmiy sahifadan yozing.</li><li>Ixtiyoriy siyosatdagi universitetlar uchun ballni yuborish qarorini asoslang.</li></ul>",
             ph="... — talab qilinadi; ... — ixtiyoriy, CDS 25–75: ...–..., qaror: ..."),
    ],
    tool=dict(id="kalendar", short="Kalendar", h2="Test kalendari va baholar jadvali", sub="Baholaringiz va testlar rejasini universitet talablari bilan solishtiring.",
              h3="Test kalendari", tag="5 maydon", ic="calendar", btn="Kalendarni saqlash", badge="Test strategi", min=4,
              fields=[dict(k="baho", label="Baholar jadvali", hint="asl shkalada, sohaga yaqin fanlar", type="area", ph="Umumiy: 4.8/5; matematika 5, fizika 5, informatika 5 ..."),
                      dict(k="talab", label="Universitetlar talablari", hint="universitet · til minimal · SAT siyosati", type="area", ph="... · IELTS 6.5 · test-optional ..."),
                      dict(k="tiltest", label="Til testi rejasi", hint="test, 1-urinish sanasi, zaxira sana", ph="IELTS, ... ; zaxira ..."),
                      dict(k="sat", label="SAT/ACT rejasi (kerak bo'lsa)", ph="Digital SAT, ... ; sinov testi ..."),
                      dict(k="hujjat", label="Transkript va tarjima rejasi", type="area", ph="Transkript: ... ; tarjima: ... ; ism: ...")]),
    check=dict(h2="Baholar va testlar nazorati", sub="Topshirishdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Baholar asl shkalada, shkala izohi bilan yozilgan.", "O'zboshimchalik bilan hisoblangan GPA ishlatilmagan.",
                      "Har universitet qabul qiladigan til testlari tekshirilgan.", "Til testi uchun qayta topshirish zaxirasi bor.",
                      "SAT/ACT kerak yoki kerak emasligi har universitet uchun aniq.", "Test siyosati joriy yil sahifasidan olingan.",
                      "Hujjatlardagi ism pasport bilan bir xil.", "Sertifikatlar ariza va viza vaqtida amalda bo'ladi."]),
    art_title="Test kalendari va baholar jadvali", art_short="Kalendar",
    art=[("Baholar jadvali", ["baho", "a1"]), ("Transkript va hujjatlar", ["hujjat", "a2"]), ("Universitetlar talablari", ["talab"]),
         ("Til testi rejasi", ["tiltest", "a3"]), ("SAT/ACT rejasi", ["sat", "a4"]), ("Test siyosati qarorlari", ["a5"])],
    tip="Test sanasini tanlaganda natija kelish muddatini ham qo'shing. Natija universitetga muddatdan oldin yetib borishi kerak.",
    sources=f"{IELTS}; {TOEFL}; {DET}; {SAT}; {ACT}; {CDS}; {APO}. {STD}",
)
