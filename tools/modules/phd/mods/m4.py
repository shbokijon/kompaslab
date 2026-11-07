from common import KCL, LEEDS, UKRIO, HOL, STD

MOD = dict(
    title="Ilmiy loyiha taklifi va metodologiya",
    desc="PhD Lab M4: ilmiy loyiha taklifining (Research Proposal) roli, fon va ahamiyat, savol va vazifalar, usul va tekshiruv, vaqt rejasi, etika va ma'lumot, tahrir va baholash mezoni. Natija: taklifning v1–v3 versiyalari.",
    lead="Ilmiy loyiha taklifi savolni “sotadigan” reklama matni emas, tekshiriladigan ish rejasi. Bu modulda savol, dalil, usul, xavf va ilmiy hissani bitta izchil hujjatga yig'asiz va uni baholash mezoni bilan uch marta tahrir qilasiz.",
    hero="scroll", weeks="3–4", next="M5 Akademik profil va ariza hujjatlari", next_href="phd-lab-o.html?m=5",
    goals=[("scroll", "Ilmiy loyiha taklifi (Research Proposal)", "v1 → v3, dastur talabidagi hajmda"),
           ("calendar", "Gantt jadvali", "4–6 bosqich, har birida natija"),
           ("shield", "Etika va ma'lumot eskizi", "8 bandlik xavf tekshiruvi")],
    warn="Taklif freymvorki: Muammo → Yechim → Yangilik → Ta'sir. Hamma PhD dasturi alohida taklif so'ramaydi: e'lon qilingan loyihalarda ko'pincha qisqa bayon yetadi. Namunalar Kompas tuzgan tuzilma misollari; tayyor matn sifatida ko'chirilmaydi.",
    lessons=[
        dict(t="Taklif va uning haqiqiy roli", short="Rol", min=25, kind="🧭 Talab", ic="scroll",
             hook="Taklifni komissiya, rahbar va ba'zan stipendiya paneli o'qiydi. Ular reklama emas, sizning fikrlash sifatingizni ko'rmoqchi.",
             body=f"""<p>Ba'zi e'lon qilingan PhD loyihalarida mavzu tayyor va uzun taklif talab qilinmaydi; o'zi taklif qilgan yo'lda esa to'liq taklif so'ralishi mumkin. Avval topiladi: so'z chegarasi, shakl, iqtibos uslubi, kim o'qiydi va baholash mezoni.</p>
<p>Taklif yangi savol va bajariladigan usulni asoslaydi; dissertatsiya natijasini oldindan kafolatlamaydi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Bir universitet 1 500–3 000 so'zlik taklif kutishi, boshqasi faqat qisqa bayon so'rashi mumkin. Universal qoida yo'q.</div>
<div class="box warn">Tayyor moliyalashtirilgan loyihaga butunlay boshqa mavzu bilan tekshirmasdan yozmang.</div>
<div class="srcs">Manba: {KCL}; {LEEDS}. {HOL}.</div>""",
             take="Avval dastur talabini o'qing: taklif kerakmi, qancha so'z, qaysi bo'limlar va qanday baholanadi.",
             task="<ul><li>3 ta dasturning taklif talabini solishtiring.</li><li>O'z dasturingiz uchun tuzilma yozing.</li><li>Qaysi bo'lim ixtiyoriyligini belgilang.</li></ul><p><b>O'zingizga savol:</b> taklif kerakmi yoki qisqa ilmiy qiziqish bayoni yetadimi?</p>",
             ph="Dastur 1: ... so'z, bo'limlar ... ; Dastur 2: ... ; Mening tuzilmam: ..."),
        dict(t="Fon va ahamiyat", short="Fon", min=30, kind="📚 Adabiyot", ic="books",
             hook="Bo'shliqni ko'rsatishdan oldin nima ma'lum ekanini adolatli aytish kerak. Aks holda bo'shliq to'qilgan ko'rinadi.",
             body=f"""<h4>Adabiyot sintezi</h4>
<p>Asosiy natija → cheklov → qarama-qarshilik → imkoniyat. Har iqtibos fikrga xizmat qilsin; maqolalarni sanash yetarli emas.</p>
<p><b>Ahamiyat</b>: qaysi nazariy yoki amaliy qaror yaxshilanadi, kim foydalanadi va nega hozir muhim.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: <span lang="en">“Energy crises are important and AI can change everything.”</span> Kuchliroq: <span lang="en">“Existing monitoring studies rely on method X in condition Y; performance under Z is unclear, which affects decision W.”</span> Bu faqat tuzilma misoli.</div>
<div class="box warn">To'qilgan iqtibos, tekshirilmagan DOI va <span lang="en">“world first”</span> iborasini ishlatmang.</div>""",
             take="Fon qismi bo'shliqni adabiyotning o'zidan chiqaradi; ahamiyat bitta aniq jumlada.",
             task="<ul><li>250 so'zlik fon qismini yozing.</li><li>5 ta tayanch maqolani biriktiring.</li><li>Bitta ahamiyat jumlasini ajrating.</li></ul><p><b>O'zingizga savol:</b> bo'shliq sizsiz ham adabiyot dalillaridan kelib chiqadimi?</p>",
             ph="Fon: ... (manba 1, 2) ... Cheklov: ... Ahamiyat: ..."),
        dict(t="Tadqiqot savoli va vazifalar", short="Savol", min=25, kind="🎯 Aniqlik", ic="compass",
             hook="Savolni usuldan ajratmasangiz, natija oldindan tasdiqlangan xulosaga aylanadi. Bu ilmiy halollikka zid.",
             body=f"""<p>Savolda tizim, natija, taqqoslash va sharoitlarni yozing. Vazifalar ketma-ket bo'lishi mumkin: asos ([[baseline]]) → tajriba → tekshiruv → umumlashtirish.</p>
<p>Gipoteza sinaladigan bo'lsa, o'lchov va noaniqlik mezonlari aniqlansin; sifatli tadqiqotda gipoteza majburiy bo'lmasligi mumkin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: <span lang="en">“To prove method A is better.”</span> Kuchliroq: <span lang="en">“Under which conditions, and relative to which baseline, does method A reduce uncertainty?”</span> “Yaxshiroq emas” degan javob ham ilmiy natija.</div>
<div class="box warn">Maqsadni “isbotlash” deb qo'yib, salbiy natijani yashirish ilmiy halollikka zid.</div>""",
             take="Bitta savol, 3 ta vazifa va har biriga kutilgan dalil: salbiy natija ham javob bo'la oladi.",
             task="<ul><li>Bitta savol yozing.</li><li>3 ta vazifa tuzing.</li><li>Har biriga kutilgan dalilni belgilang.</li></ul><p><b>O'zingizga savol:</b> qaysi tajriba asosiy taxminingizni rad etishi mumkin?</p>",
             ph="Savol: ...? ; Vazifa 1: ... (dalil: ...) ; 2: ... ; 3: ..."),
        dict(t="Usul va tekshiruv", short="Usul", min=35, kind="🧪 Dizayn", ic="miya",
             hook="Yaxshi usul murakkab algoritm nomi emas, savolga mos dalil yig'ish jarayoni. “Mashinali o'qitish ishlataman” yetarli emas.",
             body=f"""<h4>Tadqiqot dizayni tarkibi</h4>
<p>Ma'lumot manbasi, tanlov ([[sampling]]), asbob, oldindan ishlov, model, asos ([[baseline]]), tekshiruv ([[validation]]), noaniqlik va muvaffaqiyatsizlik mezoni.</p>
<p>Takrorlanuvchanlik uchun muhit, metama'lumot, versiyalash va kod yoki ma'lumot ochiqligini rejalang. Odamlar ishtirok etadigan tadqiqotda tanlov, rozilik va etika alohida o'rinda.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Usul tekshiriladi, agar yozilgan bo'lsa: qaysi o'zgaruvchilar, haqiqiy qiymat ([[ground truth]]) nima, ma'lumot qanday bo'linadi, ma'lumot sizib chiqishi ([[data leakage]]) qanday nazorat qilinadi va qachon usul ishlamaydi.</div>
<div class="box warn">Ma'lumot sizib chiqishi yoki tanlangan ko'rsatkichni ortiqcha moslash noto'g'ri xulosaga olib keladi.</div>""",
             take="Usul = ma'lumot + asos + tekshiruv + noaniqlik. Asos bo'lmasa, qo'shimcha qiymatni isbotlab bo'lmaydi.",
             quiz=[("Taklif dissertatsiya natijasini oldindan kafolatlashi kerak.", "n", "Noto'g'ri: taklif bajariladigan usulni asoslaydi, natijani kafolatlamaydi."),
                   ("Asos (baseline) bo'lmasa, yangi usulning qo'shimcha qiymatini ko'rsatish qiyin.", "t", "To'g'ri: taqqoslash nuqtasi kerak."),
                   ("Etika ruxsati kerak bo'lsa, u tadqiqot boshlanishidan oldin olinadi.", "t", "To'g'ri: UKRIO tamoyillari va institut siyosati."),
                   ("Ochiq fan tamoyili barcha maxfiy ma'lumotni ochishni talab qiladi.", "n", "Noto'g'ri: ochiqlik va xavfsiz kirish muvozanatlanadi.")],
             task="<ul><li>Usul oqim diagrammasini chizing.</li><li>2 ta asos tanlang.</li><li>Tekshiruv va noaniqlik bandini yozing.</li></ul><p><b>O'zingizga savol:</b> asos bo'lmasa, natijaning qo'shimcha qiymatini qanday isbotlaysiz?</p>",
             ph="Ma'lumot ... → ishlov ... → model ... → asos 1: ..., asos 2: ... → tekshiruv ... ; noaniqlik: ..."),
        dict(t="Vaqt rejasi va natijalar", short="Reja", min=25, kind="📅 Gantt", ic="calendar",
             hook="Doktorantura uchun vaqt rejasi ilmiy xavfni boshqarish vositasi. “2-yil: tajribalar” degan reja hech narsani nazorat qilmaydi.",
             body=f"""<p>Adabiyot, trening, ma'lumot yig'ish, tahlil, tekshiruv, yozish, ko'rib chiqish va zaxira vaqt o'rtasidagi bog'liqliklarni belgilang. Davomiylik (36 yoki 48 oy) dasturga bog'liq: rejani rasmiy muddatga moslang.</p>
<p>Har bosqich o'lchanadigan natija bilan tugasin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Noaniq: “2-yil: tajribalar.” Tekshiriladigan: “5-chorak: kalibrlash ma'lumoti sifat nazoratidan o'tgan, xatoliklar jadvali tayyor.”</div>
<div class="box warn">Etika ruxsati yoki dala mavsumiga ketadigan vaqtni nol deb olmang.</div>""",
             take="Gantt jadvali bosqichlar, natijalar va kechikishdagi zaxira bilan; muddat dastur davomiyligiga mos.",
             task="<ul><li>4–6 bosqichli Gantt jadvalini tuzing.</li><li>Har bosqichga natija yozing.</li><li>Ma'lumot kechikishi uchun zaxira belgilang.</li></ul><p><b>O'zingizga savol:</b> ma'lumot kechiksa, qaysi vazifa baribir tugaydi?</p>",
             ph="1-bosqich (1–6 oy): ... → natija ... ; 2-bosqich: ... ; zaxira: ..."),
        dict(t="Etika, ma'lumot va ochiqlik", short="Etika", min=25, kind="🛡 Halollik", ic="shield",
             hook="Tadqiqot halolligi taklifning oxirgi rasmiyati emas, usul sifatini belgilaydigan qatlam.",
             body=f"""<p>Tadqiqot turiga qarab: xabardor rozilik, maxfiylik, intellektual mulk, xavfsizlik, eksport nazorati, dala ruxsatlari, sun'iy intellektdan foydalanishni oshkor qilish va ma'lumotlarni boshqarish rejasi ([[data management plan]], DMP).</p>
<p>Ochiq fan barcha maxfiy ma'lumotni ochish degani emas: [[FAIR]] tamoyillari va xavfsiz kirish muvozanatlanadi. Etika ruxsati kerak bo'lsa, tadqiqot boshlanishidan oldin olinadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Odamlar bilan intervyu rejalansa, anonimlik va rozilik boshlanishdan oldin kelishiladi; geofizik dala ma'lumotida hududga kirish va xavfsizlik ruxsati muhim bo'lishi mumkin.</div>
<div class="box warn">“Ochiq ma'lumot” deb shaxsiy yoki litsenziyali ma'lumotni tarqatish mumkin emas.</div>
<div class="srcs">Manba: {UKRIO}. {HOL}.</div>""",
             take="8 bandlik etika tekshiruvi va qisqa DMP taklifni ishonchli qiladi.",
             task="<ul><li>8 bandlik etika xavf tekshiruvini tuzing.</li><li>Ma'lumotlarni boshqarish eskizini yozing.</li><li>Institut siyosatiga havola qo'shing.</li></ul><p><b>O'zingizga savol:</b> xavfga mos nazoratchi va ruxsat beruvchi kim?</p>",
             ph="Etika: rozilik ..., maxfiylik ..., xavfsizlik ... ; DMP: saqlash ..., ulashish ..."),
        dict(t="Tahrir va baholash mezoni", short="Tahrir", min=35, kind="✍️ Tahrir", ic="memo",
             hook="Birinchi qoralama natija emas. Sifat fikr olish va moslashtirish bilan oshadi.",
             body=f"""<h4>Tahrir tartibi</h4>
<ol><li>Tuzilma: bo'shliq → savol → usul izchilmi.</li><li>Dalil tekshiruvi: har da'vo manbali.</li><li>Da'volar: ortiqcha va'da yo'q.</li><li>Til aniqligi.</li><li>Dastur talabiga moslik.</li></ol>
<p>Ingliz tilini bezashdan oldin mantiqdagi uzilishni toping. Qoralama tarixi, manba izi va o'z mualliflikingizni saqlang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Taqrizchi “savol qiziq, lekin usul yetarli yozilmagan” desa, tilni emas, asos va ma'lumot rejasini kuchaytiring.</div>
<div class="box warn">Matnni butunlay sun'iy intellektga topshirib, uning to'qigan manbalarini qoldirmang.</div>
<div class="srcs">Manba: {KCL}; {UKRIO}. {HOL}.</div>""",
             take="v1 → mezon bilan 5 ta zaif joy → v2 → v3 → dastur shakli. Har versiya saqlanadi.",
             task="<ul><li>v1 qoralamani yozing.</li><li>Baholash mezoni bilan 5 ta zaif joyni toping.</li><li>v2 va v3 ni solishtiring.</li><li>Yakuniy shaklni dastur talabiga moslang.</li></ul><p><b>O'zingizga savol:</b> taklifning qaysi bo'limida xavf aniq ko'rinadi?</p>",
             ph="Zaif joylar: 1) ... 2) ... ; v2 da o'zgardi: ... ; v3: ..."),
    ],
    tool=dict(id="taklif", short="Taklif", h2="Ilmiy loyiha taklifi quruvchisi", sub="Muammo → bo'shliq → savol → usul → tekshiruv → etika. Har bo'limni o'z so'zlaringiz bilan yozing.",
              h3="Taklif bo'limlari", tag="6 maydon", ic="scroll", btn="Taklifni saqlash", badge="Taklifchi", min=5,
              fields=[dict(k="sarl", label="Sarlavha", ph="..."),
                      dict(k="muammo", label="Muammo va ahamiyat", type="area", wc="150-250", ph="..."),
                      dict(k="boshliq", label="Bo'shliq va savol", type="area", wc="100-200", ph="..."),
                      dict(k="usul", label="Usul, asos va tekshiruv", type="area", wc="200-400", ph="..."),
                      dict(k="hissa", label="Yangilik va kutilgan hissa", type="area", wc="80-150", ph="..."),
                      dict(k="xavf", label="Vaqt, xavf va etika", type="area", wc="100-200", ph="...")]),
    check=dict(h2="M4 nazorati", sub="Taklifni topshirishdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Savol aniq va javob berib bo'ladigan.", "Fon va bo'shliq ishonchli manbalar bilan.", "Usul vazifalar va ma'lumotga mos.",
                      "Asos va tekshiruv yozilgan.", "Bajarilishi mumkinlik, noaniqlik va etika aniq.", "Gantt jadvalida har bosqich natijasi bor.",
                      "Har iqtibos va DOI qo'lda tekshirilgan.", "Hajm dastur so'z chegarasiga mos."]),
    art_title="Ilmiy loyiha taklifi (Research Proposal)", art_short="Taklif",
    art=[("Sarlavha", ["sarl"]), ("Muammo va ahamiyat", ["muammo", "a2"]), ("Bo'shliq va savol", ["boshliq", "a3"]), ("Usul va tekshiruv", ["usul", "a4"]),
         ("Yangilik va hissa", ["hissa"]), ("Vaqt rejasi", ["a5"]), ("Etika va ma'lumot", ["a6", "xavf"]), ("Tahrir izi", ["a1", "a7"])],
    tip="Taklifni ovoz chiqarib o'qing. Biror jumlani intervyuda himoya qila olmasangiz, uni o'chiring yoki manba bilan mustahkamlang.",
    sources=f"{KCL}; {LEEDS}; {UKRIO}. {STD}",
)
