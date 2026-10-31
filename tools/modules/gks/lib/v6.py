from common import U27, G26, STD

MOD = dict(
    title="O'quv rejasi",
    desc="GKS Lab M6: GKS o'quv rejasi (Study Plan), Hozirgi holat → Bo'shliq → Strategiya → Vaqt, til yili va daraja yillari rejasi, tadqiqot savoli va bitiruvdan keyingi yo'l. Natija: yakuniy o'quv rejasi.",
    lead="O'quv rejasi komissiyaga Koreyada vaqtingizni qanday ishlatishingizni ko'rsatadi: til yili, daraja yillari va undan keyin. Magistratura va doktoranturada u eng og'ir hujjat. Bu modulda uni vaqt jadvali bilan quring.",
    hero="calendar", weeks="3", next="Paketni yig'ish va topshirish",
    goals=[("calendar", "Yakuniy o'quv rejasi", "forma bandlari bo'yicha, vaqt jadvali bilan"),
           ("telescope", "Tadqiqot yoki o'qish yo'nalishi", "M, D: tadqiqot savoli; U: fan va ko'nikmalar rejasi"),
           ("compass", "Bitiruvdan keyingi yo'l", "shaxsiy bayonot bilan izchil")],
    warn="O'quv rejasi ham siz to'ldiradigan forma (2027 GKS-U da 3-forma). Forma bandlari va hajm har yil yo'riqnoma ilovasida. Bu moduldagi namunalar Kompas tuzgan o'quv materiali.",
    lessons=[
        dict(t="O'quv rejasi nima uchun markaziy hujjat", short="Rol", min=30, kind="📋 Forma", ic="scroll",
             hook="Shaxsiy bayonot \"nega\" savoliga javob beradi, o'quv rejasi \"qanday\" savoliga. Baholovchi rejaga qarab sizning uddalashingizni tasavvur qiladi.",
             body=f"""<h4>Faktlar</h4>
<ul><li><span class="trk">U</span> 2027 GKS-U: o'quv rejasi 3-forma; ingliz yoki koreys tilida yoziladi.</li>
<li><span class="trk">M</span> <span class="trk">D</span> GKS-G: o'quv rejasi to'ldiriladigan formalardan biri; tadqiqot dasturi nomzodlari qo'shimcha formalar topshiradi.</li></ul>
<h4>Kuchli va kuchsiz reja</h4>
<div class="tbl"><table><thead><tr><th>Kuchsiz</th><th>Kuchli</th></tr></thead><tbody>
<tr><td>\"Koreys tilini o'rganaman, keyin yaxshi o'qiyman\"</td><td>Til yilida qaysi darajaga, qachon (TOPIK sanasi bilan)</td></tr>
<tr><td>Fanlarni umumiy sanash</td><td>Dastur o'quv rejasidan aniq fanlar va ular nimaga kerak</td></tr>
<tr><td>\"Ilmiy ish qilaman\"</td><td><span class="trk">M</span> <span class="trk">D</span> Tadqiqot savoli, usul, laboratoriya, semestrlar bo'yicha bosqich</td></tr>
<tr><td>\"Vatanimga xizmat qilaman\"</td><td>Qaysi sohada, qanday lavozimda, qanday loyiha bilan</td></tr>
</tbody></table></div>
<div class="srcs">Manba: {U27}; {G26}.</div>""",
             take="O'quv rejasi \"qanday\" savoliga javob beradi: aniq vaqt, aniq fan yoki tadqiqot va aniq keyingi qadam.",
             task="<ul><li>O'quv rejasi formasidagi bandlarni ko'chiring. Har band yoniga hozir javobingiz bormi (ha/qisman/yo'q) belgilang.</li></ul>",
             ph="Band 1: ... (qisman) ..."),
        dict(t="Hozirgi holat → Bo'shliq → Strategiya → Vaqt", short="Freymvork", min=40, kind="🛠 Skelet", ic="compass",
             hook="Reja nuqtadan nuqtaga yo'l. Boshlang'ich nuqta va manzil aniq bo'lmasa, qadamlar havoda qoladi.",
             body="""<div class="tbl"><table><thead><tr><th>Qism</th><th>Savol</th><th>Manba</th></tr></thead><tbody>
<tr><td><b>Hozirgi holat</b></td><td>Bugun nimani bilasiz va qila olasiz?</td><td>M3 inventari, transkript</td></tr>
<tr><td><b>Bo'shliq</b></td><td>Maqsadga yetish uchun nima yetishmaydi?</td><td>M3 profil izohi</td></tr>
<tr><td><b>Strategiya</b></td><td>Koreyadagi dastur bo'shliqni qanday yopadi: fan, laboratoriya, loyiha?</td><td>M2 moslik dalili</td></tr>
<tr><td><b>Vaqt</b></td><td>Qaysi yil, semestrda nima qilinadi?</td><td>3-dars jadvali</td></tr>
</tbody></table></div>
<p>Har qism keyingisiga ulanadi: bo'shliq hozirgi holatdan kelib chiqadi, strategiya aynan shu bo'shliqni yopadi, vaqt jadvali strategiyani bosqichlarga bo'ladi.</p>
<div class="box info"><b>Kompas tuzgan namuna</b> (shartli): Hozir: geologiya bakalavri, GIS va asosiy statistika. Bo'shliq: yer osti suvlarini raqamli modellash. Strategiya: dasturdagi gidrogeologik modellash fani va laboratoriyadagi maydon ma'lumotlari bilan ishlash. Vaqt: 1-semestr nazariya, 2-semestr usul, 3–4-semestr dissertatsiya.</div>""",
             take="Hozirgi holat → Bo'shliq → Strategiya → Vaqt: har qism oldingisidan kelib chiqadi va keyingisini asoslaydi.",
             task="<ul><li>To'rt qism uchun 2–3 jumladan skelet yozing.</li></ul>",
             ph="Hozir: ... Bo'shliq: ... Strategiya: ... Vaqt: ..."),
        dict(t="Til yili va daraja yillari rejasi", short="Vaqt", min=35, kind="🗓 Jadval", ic="calendar",
             hook="GKS dasturining birinchi yili odatda koreys tili. Rejada bu yil bo'sh qolsa, komissiya til yilini qanday o'tkazishingizni bilmaydi.",
             body=f"""<h4>Dastur davomiyligi</h4>
<ul><li><span class="trk">U</span> 2027 GKS-U: 1 yil koreys tili + 4–6 yil bakalavriat (yo'nalishga qarab).</li>
<li><span class="trk">M</span> 2026 GKS-G: 1 yil til + 2 yil magistratura.</li>
<li><span class="trk">D</span> 2026 GKS-G: 1 yil til + 3 yil doktorantura.</li>
<li>TOPIK 5 yoki 6 bilan til kursidan ozod bo'lasiz; til kursining birinchi 6 oyida 5–6 darajani olsangiz, qolgan 6 oydan ozod qilinasiz va daraja dasturini ertaroq boshlaysiz.</li></ul>
<h4>Jadval tuzilmasi</h4>
<div class="tbl"><table><thead><tr><th>Davr</th><th>O'qish</th><th>Natija</th></tr></thead><tbody>
<tr><td>Til yili, 1-yarim</td><td>Koreys tili kursi</td><td>TOPIK maqsadi va sanasi</td></tr>
<tr><td>Til yili, 2-yarim</td><td>Til + sohaga oid lug'at, dastur fanlari bilan tanishish</td><td>TOPIK yuqori daraja</td></tr>
<tr><td>1-yil</td><td><span class="trk">U</span> asosiy fanlar; <span class="trk">M</span> <span class="trk">D</span> majburiy kurslar, mavzu</td><td>...</td></tr>
<tr><td>Oxirgi yil</td><td>Bitiruv ishi, dissertatsiya</td><td>Himoya, nashr yoki loyiha</td></tr>
</tbody></table></div>
<div class="box warn">Rejadagi fanlar va laboratoriyalar universitetning rasmiy o'quv rejasidan bo'lsin. Mavjud bo'lmagan fan yoki laboratoriyani yozish moslik dalilini buzadi.</div>
<div class="srcs">Manba: {U27}; {G26}.</div>""",
             take="Reja til yilidan boshlanadi va har davrga aniq o'qish va o'lchanadigan natija beradi. Fanlar rasmiy o'quv rejasidan olinadi.",
             task="<ul><li>O'z trekingiz bo'yicha yilma-yil (D, M uchun semestrma-semestr) jadval tuzing: davr · o'qish · natija.</li></ul>",
             ph="Til yili: ... 1-yil: ... "),
        dict(t="Tadqiqot savoli yoki o'qish yo'nalishi", short="Savol", min=45, kind="🔬 Savol", ic="telescope",
             hook="\"Sun'iy intellektni o'rganmoqchiman\" mavzu emas. Komissiya javob beriladigan savolni ko'rmoqchi.",
             body="""<h4><span class="trk">M</span> <span class="trk">D</span> Mavzudan savolga</h4>
<ol><li><b>Soha:</b> gidrogeologiya.</li><li><b>Mavzu:</b> yer osti suvlarining sho'rlanishi.</li>
<li><b>Savol:</b> Sirdaryo havzasidagi sug'oriladigan yerlarda yer osti suvi sho'rlanishini mavjud kuzatuv ma'lumotlari bilan qaysi usul eng aniq bashorat qiladi?</li></ol>
<p>Yaxshi savol: <b>o'lchanadigan</b> (ma'lumot bilan javob beriladi), <b>javob beriladigan</b> (dastur muddatida), <b>ahamiyatli</b> (kimgadir foydasi bor).</p>
<h4>Muammo → Yechim → Yangilik → Ta'sir</h4>
<ul><li><b>Muammo:</b> nima ishlamayapti yoki noma'lum.</li><li><b>Yechim:</b> qaysi usul bilan yondashasiz.</li>
<li><b>Yangilik:</b> mavjud ishlardan nima bilan farq qiladi (2–3 manbaga tayangan holda).</li><li><b>Ta'sir:</b> natija kimga, qanday foyda beradi.</li></ul>
<p><span class="trk">D</span> Doktorantura uchun 10–15 manbali qisqa adabiyotlar bazasi va bo'shliqni aniq ko'rsatish kerak; laboratoriya bilan moslik (M4) og'irroq.</p>
<h4><span class="trk">U</span> Bakalavriat uchun</h4>
<p>Tadqiqot savoli talab qilinmaydi. Uning o'rniga: qaysi fanlar va ko'nikmalar sizni maqsadga olib boradi, qaysi to'garak, loyiha yoki amaliyotda qatnashmoqchisiz.</p>
<div class="box warn">Savolni shu yerda \"yopmang\": u laboratoriya va professor bilan muloqotda o'zgarishi mumkin. Rejada buni \"dastlabki yo'nalish\" deb ko'rsatish halol.</div>""",
             take="M va D: mavzudan o'lchanadigan savolga, Muammo → Yechim → Yangilik → Ta'sir. U: fanlar, ko'nikmalar va loyihalar rejasi.",
             task="<ul><li><span class=\"trk\">M</span> <span class=\"trk\">D</span> Soha → mavzu → savol zanjirini va 4 qismli qisqa tavsifni yozing.</li><li><span class=\"trk\">U</span> Maqsadingizga olib boradigan 4–6 fan va 2 ta loyiha yoki to'garakni yozing.</li></ul>",
             ph="Soha → mavzu → savol: ..."),
        dict(t="Bitiruvdan keyingi yo'l va izchillik", short="Keyin", min=30, kind="🎯 Mini-test", ic="seedling",
             hook="Bayonotda \"tadqiqotchi bo'laman\", rejada \"xalqaro kompaniyada menejer\" deb yozilsa, komissiya ikkalasiga ham ishonmaydi.",
             body="""<h4>Bitiruvdan keyingi yo'l</h4>
<ul><li>Aniq: qaysi soha, qanday lavozim yoki loyiha turi, qaysi tashkilot turida.</li>
<li>Bog'liq: dasturda olingan bilim aynan shu yerda qanday ishlatiladi.</li>
<li>Halol: bir necha variant bo'lsa, asosiysi va zaxirasini ayting; ishonchsiz va'da bermang.</li></ul>
<h4>Izchillik tekshiruvi</h4>
<div class="tbl"><table><thead><tr><th>Element</th><th>Shaxsiy bayonot</th><th>O'quv rejasi</th></tr></thead><tbody>
<tr><td>Soha va yo'nalish</td><td>Bir xil</td><td>Bir xil</td></tr>
<tr><td>Maqsad</td><td>Motivatsiya bilan</td><td>Vaqt va qadamlar bilan</td></tr>
<tr><td>Universitet va dastur</td><td>Nega shu</td><td>Shu dasturda nima</td></tr>
</tbody></table></div>
<div class="box info">Ikkala hujjatni yonma-yon qo'yib, sohani, maqsadni va dastur nomini bo'yab chiqing: farq bo'lsa, bittasini tuzating.</div>""",
             take="Bitiruvdan keyingi yo'l aniq, bog'liq va halol. Bayonot va reja soha, maqsad va dasturda bir xil gapiradi.",
             quiz=[("O'quv rejasida til yilini ko'rsatish shart emas, u avtomatik.", "n", "Noto'g'ri: til yilini qanday o'tkazishingiz rejaning bir qismi."),
                   ("2026 GKS-G da doktorantura 1 yil til va 3 yil dasturdan iborat.", "t", "To'g'ri."),
                   ("Bakalavriat o'quv rejasida tadqiqot savoli majburiy.", "n", "Noto'g'ri: U uchun fanlar, ko'nikmalar va loyihalar rejasi."),
                   ("Bayonot va o'quv rejasidagi maqsadlar bir-biriga zid bo'lmasligi kerak.", "t", "To'g'ri: izchillik ishonchni oshiradi.")],
             task="<ul><li>Bitiruvdan keyingi yo'lni 3–4 jumlada yozing.</li><li>M5 bayonotingiz bilan izchillik jadvalini to'ldiring.</li></ul>",
             ph="Bitiruvdan keyin: ... Izchillik: ..."),
    ],
    tool=dict(id="reja", short="Reja", h2="O'quv rejasi quruvchi", sub="Freymvork bloklari va to'liq matn. So'z hisoblagichi mo'ljal; forma chegarasi ustun.",
              h3="O'quv rejasi", tag="4 blok + jadval + matn", ic="calendar", btn="Rejani saqlash", badge="Rejachi", min=5,
              fields=[dict(k="p1", label="Hozirgi holat", type="area", ph=""),
                      dict(k="p2", label="Bo'shliq", type="area", ph=""),
                      dict(k="p3", label="Strategiya: dastur bo'shliqni qanday yopadi", type="area", ph=""),
                      dict(k="p4", label="Vaqt jadvali", hint="til yili, yillar yoki semestrlar", type="area", ph="Til yili: ... 1-yil: ..."),
                      dict(k="p5", label="Bitiruvdan keyingi yo'l", type="area", ph=""),
                      dict(k="pfull", label="To'liq matn", type="area", wc="500-1000", ph="")]),
    check=dict(h2="Reja nazorati", sub="Yakuniy versiyadan oldin.", h3="9 bandlik nazorat",
               items=["Forma bandlarining hammasiga javob bor.", "Til yili aniq maqsad va sana bilan.",
                      "Fanlar va laboratoriyalar universitetning rasmiy o'quv rejasidan.", "M, D: tadqiqot savoli o'lchanadigan va javob beriladigan.",
                      "D: 10–15 manbali baza va bo'shliq ko'rsatilgan.", "U: fanlar, ko'nikmalar va loyihalar aniq.",
                      "Bitiruvdan keyingi yo'l aniq va bog'liq.", "Shaxsiy bayonot bilan zid joy yo'q.", "Hajm forma chegarasidan oshmaydi."]),
    art_title="O'quv rejasi", art_short="Reja",
    art=[("Forma bandlari xaritasi", ["a1"]), ("Hozirgi holat", ["p1"]), ("Bo'shliq", ["p2"]), ("Strategiya", ["p3", "a4"]),
         ("Vaqt jadvali", ["p4", "a3"]), ("Bitiruvdan keyingi yo'l", ["p5", "a5"]), ("To'liq matn", ["pfull"])],
    tip="Rejani o'qigan odam \"bu nomzod til yilining uchinchi oyida nima qiladi?\" savoliga javob topa olishi kerak. Topa olmasa, jadval hali umumiy.",
    sources=STD,
)
