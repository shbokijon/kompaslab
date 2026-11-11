from common import KCL, LEEDS, UKRIO, HOL, STD

MOD = dict(
    title="Ilmiy loyiha taklifi va metodologiya",
    desc="PhD Lab M4: ilmiy loyiha taklifining (Research Proposal) vazifasi, fon va ahamiyat, savol va vazifalar, usul va tekshiruv, ish rejasi, etika va ma'lumot, tahrir. Natija: taklifning uch versiyasi (v1–v3).",
    lead="Ilmiy loyiha taklifini o'qigan odam savolingizni, uni <b>qanday tekshirishingizni</b> va qaysi xavflarni ko'rganingizni tushunishi kerak. Bu modulda savol, dalil, usul, xavf va kutilgan hissani bitta izchil hujjatga yig'asiz va uni baholash mezoni bo'yicha uch marta tahrir qilasiz.",
    hero="scroll", weeks="3–4", next="M5 Akademik profil va ariza hujjatlari", next_href="phd-lab-o.html?m=5",
    goals=[("scroll", "Ilmiy loyiha taklifi (Research Proposal)", "v1 dan v3 gacha, dastur talab qilgan hajmda"),
           ("calendar", "Gantt jadvali", "4–6 bosqich, har birining natijasi bilan"),
           ("shield", "Etika va ma'lumot rejasi", "8 bandlik tekshiruv")],
    warn="Taklif tuzilmasi: Muammo → Yechim → Yangilik → Ta'sir. Hamma PhD dasturi alohida taklif so'ramaydi: e'lon qilingan loyihalarda ko'pincha qisqa bayon yetarli. Namunalar Kompas tuzgan tuzilma misollari; ularni tayyor matn sifatida ko'chirmang.",
    lessons=[
        dict(t="Taklif nima uchun kerak", short="Vazifa", min=25, kind="🧭 Talab", ic="scroll",
             hook="Taklifni qabul komissiyasi, bo'lajak rahbar va ba'zan stipendiya hay'ati o'qiydi. Ular <b>qanday fikrlashingizni</b> va rejangiz qanchalik real ekanini ko'rmoqchi.",
             body=f"""<p>Ba'zi e'lon qilingan PhD loyihalarida mavzu tayyor bo'ladi va uzun taklif so'ralmaydi. Mavzuni o'zingiz taklif qiladigan yo'lda esa to'liq taklif talab qilinishi mumkin. Avval quyidagilarni toping: <b>so'z chegarasi</b>, shakl, iqtibos uslubi, kim o'qiydi va qanday baholanadi.</p>
<p>Taklif yangi savolni va uni bajarsa bo'ladigan usulni asoslaydi. Dissertatsiya natijasini oldindan va'da qilmaydi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Bir universitet 1 500–3 000 so'zlik taklif kutishi, boshqasi faqat qisqa bayon so'rashi mumkin. Hamma uchun bir xil qoida yo'q.</div>
<div class="box warn">Mavzusi tayyor moliyalashtirilgan loyihaga butunlay boshqa mavzu bilan ariza yozmang.</div>
<div class="srcs">Manba: {KCL}; {LEEDS}. {HOL}.</div>""",
             take="Avval dastur talabini o'qing: taklif kerakmi, necha so'z, qaysi bo'limlar va qanday baholanadi.",
             task="<ul><li>3 ta dasturning taklif talabini solishtiring.</li><li>O'z dasturingiz uchun bo'limlar ro'yxatini yozing.</li><li>Qaysi bo'lim ixtiyoriy ekanini belgilang.</li></ul><p><b>O'zingizga savol:</b> sizdan to'liq taklif so'ralyaptimi yoki qisqa ilmiy qiziqish bayoni yetadimi?</p>",
             ph="Dastur 1: ... so'z, bo'limlar ... ; Dastur 2: ... ; Mening tuzilmam: ..."),
        dict(t="Fon va ahamiyat", short="Fon", min=30, kind="📚 Adabiyot", ic="books",
             hook="Bo'shliqni ko'rsatishdan oldin bu sohada <b>nima ma'lum</b> ekanini adolatli yozing. Aks holda bo'shliq o'ylab topilgandek ko'rinadi.",
             body=f"""<h4>Adabiyotni bog'lab yozish</h4>
<p>Tartib: asosiy natija → cheklov → qarama-qarshi natijalar → ochiq qolgan imkoniyat. Har iqtibos bitta fikrni qo'llab-quvvatlasin; maqolani faqat ro'yxat to'ldirish uchun keltirmang.</p>
<p><b>Ahamiyat</b>: ish natijasida qaysi ilmiy yoki amaliy qaror yaxshilanadi, undan kim foydalanadi va nega aynan hozir muhim.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Zaif: <i><span lang="en">“Energy crises are important and AI can change everything.”</span></i> Kuchliroq: <i><span lang="en">“Existing monitoring studies rely on method X in condition Y; performance under Z is unclear, which affects decision W.”</span></i> Bu faqat tuzilma misoli.</div>
<div class="box warn">O'ylab topilgan iqtibos, tekshirilmagan DOI va <i><span lang="en">“world first”</span></i> kabi iboralarni ishlatmang.</div>""",
             take="Fon qismida bo'shliq adabiyotning o'zidan kelib chiqadi; ahamiyat bitta aniq jumlada yoziladi.",
             task="<ul><li>250 so'zlik fon qismini yozing.</li><li>5 ta tayanch maqolani biriktiring.</li><li>Ahamiyatni bitta jumlada yozing.</li></ul><p><b>O'zingizga savol:</b> bo'shliq siz aytmasangiz ham adabiyotdan ko'rinib turadimi?</p>",
             ph="Fon: ... (manba 1, 2) ... Cheklov: ... Ahamiyat: ..."),
        dict(t="Tadqiqot savoli va vazifalar", short="Savol", min=25, kind="🎯 Aniqlik", ic="compass",
             hook="Savolni usuldan ajratmasangiz, ish oldindan tanlangan xulosani tasdiqlashga aylanib qoladi. Bu <b>ilmiy halollikka</b> to'g'ri kelmaydi.",
             body=f"""<p>Savolda nima o'rganilishini, qaysi natija o'lchanishini, nima bilan taqqoslanishini va qaysi sharoitda ekanini yozing. Vazifalar ketma-ket bo'lishi mumkin: taqqoslash nuqtasi ([[baseline]]) → tajriba → tekshiruv → umumlashtirish.</p>
<p>Gipotezani sinab ko'rsa bo'lsa, o'lchov va noaniqlik mezonlarini yozing. Sifat tadqiqotlarida gipoteza bo'lmasligi mumkin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Zaif: <i><span lang="en">“To prove method A is better.”</span></i> Kuchliroq: <i><span lang="en">“Under which conditions, and relative to which baseline, does method A reduce uncertainty?”</span></i> <i>“A usul yaxshiroq ekan”</i> degan xulosa chiqmasa ham, bu ilmiy natija hisoblanadi.</div>
<div class="box warn">Maqsadni <i>“isbotlash”</i> deb qo'yib, kutilmagan natijani yashirish ilmiy halollikka zid.</div>""",
             take="Bitta savol, 3 ta vazifa va har biri uchun kutilgan dalil. Kutilmagan natija ham javob bo'la oladi.",
             task="<ul><li>Bitta savol yozing.</li><li>3 ta vazifa tuzing.</li><li>Har biri uchun kutilgan dalilni yozing.</li></ul><p><b>O'zingizga savol:</b> qaysi tajriba asosiy taxminingizni rad etishi mumkin?</p>",
             ph="Savol: ...? ; Vazifa 1: ... (dalil: ...) ; 2: ... ; 3: ..."),
        dict(t="Usul va tekshiruv", short="Usul", min=35, kind="🧪 Dizayn", ic="miya",
             hook="<i>“Mashinali o'qitishdan foydalanaman”</i> degan gap usul hisoblanmaydi. Usul savolga javob beradigan <b>dalilni qanday yig'ishingizni</b> ko'rsatadi.",
             body=f"""<h4>Tadqiqot dizayni nimalardan iborat</h4>
<p>Ma'lumot manbasi, tanlanma ([[sampling]]), asbob, dastlabki ishlov, model, taqqoslash nuqtasi ([[baseline]]), tekshiruv ([[validation]]), noaniqlik va <b>usul ishlamagan hisoblanadigan holat</b>.</p>
<p>Boshqalar natijani takrorlay olishi uchun dastur muhiti, ma'lumot tavsifi (metama'lumot), versiyalar va kod yoki ma'lumot ochiqligini rejalang. Odamlar ishtirok etadigan tadqiqotda tanlanma, rozilik va etika alohida yoziladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Usulni tekshirsa bo'ladi, agar unda yozilgan bo'lsa: qaysi o'zgaruvchilar, haqiqiy qiymat ([[ground truth]]) nima, ma'lumot qanday bo'linadi, ma'lumot oqishining ([[data leakage]]) oldi qanday olinadi va usul qachon ishlamaydi.</div>
<div class="box warn">Ma'lumot oqishi yoki bitta ko'rsatkichga ortiqcha moslab yuborish noto'g'ri xulosaga olib keladi.</div>""",
             take="Usul: ma'lumot, taqqoslash nuqtasi, tekshiruv va noaniqlik. Taqqoslash nuqtasi bo'lmasa, yangi usulning foydasini ko'rsatib bo'lmaydi.",
             quiz=[("Taklif dissertatsiya natijasini oldindan kafolatlashi kerak.", "n", "Noto'g'ri: taklif bajarsa bo'ladigan usulni asoslaydi, natijani va'da qilmaydi."),
                   ("Taqqoslash nuqtasi (baseline) bo'lmasa, yangi usulning foydasini ko'rsatish qiyin.", "t", "To'g'ri: nima bilan solishtirayotganingiz aniq bo'lishi kerak."),
                   ("Etika ruxsati kerak bo'lsa, u tadqiqot boshlanishidan oldin olinadi.", "t", "To'g'ri: UKRIO tamoyillari va universitet qoidalari shunday."),
                   ("Ochiq fan tamoyili barcha maxfiy ma'lumotni ochishni talab qiladi.", "n", "Noto'g'ri: ochiqlik va xavfsiz saqlash birga hisobga olinadi.")],
             task="<ul><li>Usulning bosqichlarini chizib chiqing.</li><li>2 ta taqqoslash nuqtasini tanlang.</li><li>Tekshiruv va noaniqlik qismini yozing.</li></ul><p><b>O'zingizga savol:</b> taqqoslash nuqtasisiz natijaning foydasini qanday ko'rsatasiz?</p>",
             ph="Ma'lumot ... → ishlov ... → model ... → taqqoslash 1: ..., 2: ... → tekshiruv ... ; noaniqlik: ..."),
        dict(t="Ish rejasi va natijalar", short="Reja", min=25, kind="📅 Gantt", ic="calendar",
             hook="Doktorantura rejasi ilmiy xavflarni boshqarish uchun kerak. <i>“2-yil: tajribalar”</i> degan reja hech narsani nazorat qilmaydi.",
             body=f"""<p>Adabiyot, o'quv kurslari, ma'lumot yig'ish, tahlil, tekshiruv, yozish, ko'rib chiqish va zaxira vaqt bir-biriga qanday bog'liqligini belgilang. Davomiylik (36 yoki 48 oy) dasturga bog'liq: rejani rasmiy muddatga moslang.</p>
<p>Har bosqich <b>o'lchasa bo'ladigan natija</b> bilan tugasin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Noaniq: <i>“2-yil: tajribalar.”</i> Tekshirsa bo'ladigan: <i>“5-chorak: kalibrlash ma'lumoti sifat tekshiruvidan o'tgan, xatoliklar jadvali tayyor.”</i></div>
<div class="box warn">Etika ruxsati yoki dala mavsumiga ketadigan vaqtni hisobdan chiqarib qo'ymang.</div>""",
             take="Gantt jadvalida bosqichlar, ularning natijasi va kechikish uchun zaxira bor; muddat dastur davomiyligiga mos.",
             task="<ul><li>4–6 bosqichli Gantt jadvalini tuzing.</li><li>Har bosqich natijasini yozing.</li><li>Ma'lumot kechiksa nima qilishingizni belgilang.</li></ul><p><b>O'zingizga savol:</b> ma'lumot kechiksa, qaysi vazifa baribir bajariladi?</p>",
             ph="1-bosqich (1–6 oy): ... → natija ... ; 2-bosqich: ... ; zaxira: ..."),
        dict(t="Etika, ma'lumot va ochiqlik", short="Etika", min=25, kind="🛡 Halollik", ic="shield",
             hook="Etika va ma'lumot masalalari usul sifatiga bevosita ta'sir qiladi, shuning uchun ular <b>taklifning boshidan</b> rejalanadi.",
             body=f"""<p>Tadqiqot turiga qarab: <b>xabardor rozilik</b>, maxfiylik, intellektual mulk, xavfsizlik, eksport nazorati, dala ruxsatnomalari, sun'iy intellektdan foydalanilganini ochiq aytish va ma'lumotlarni boshqarish rejasi ([[data management plan]], DMP).</p>
<p>Ochiq fan maxfiy ma'lumotni ham hammaga ochishni talab qilmaydi: [[FAIR]] tamoyillari va xavfsiz saqlash birga hisobga olinadi. Etika ruxsati kerak bo'lsa, u ish boshlanishidan oldin olinadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Odamlar bilan suhbat rejalansa, ismlarni yashirish va rozilik ish boshlanishidan oldin kelishiladi. Geofizik dala ma'lumotida esa hududga kirish va xavfsizlik ruxsati muhim bo'lishi mumkin.</div>
<div class="box warn"><i>“Ochiq ma'lumot”</i> deb shaxsiy yoki litsenziyali ma'lumotni tarqatib bo'lmaydi.</div>
<div class="srcs">Manba: {UKRIO}. {HOL}.</div>""",
             take="8 bandlik etika tekshiruvi va qisqa ma'lumot rejasi taklifga ishonch qo'shadi.",
             task="<ul><li>8 bandlik etika tekshiruvini tuzing.</li><li>Ma'lumotlarni boshqarish rejasini qisqa yozing.</li><li>Universitet qoidasiga havola qo'shing.</li></ul><p><b>O'zingizga savol:</b> bu xavf uchun kim ruxsat beradi va kim nazorat qiladi?</p>",
             ph="Etika: rozilik ..., maxfiylik ..., xavfsizlik ... ; Ma'lumot rejasi: saqlash ..., ulashish ..."),
        dict(t="Tahrir va baholash mezoni", short="Tahrir", min=35, kind="✍️ Tahrir", ic="memo",
             hook="Birinchi qoralama hali tayyor taklif bo'lmaydi. Sifat <b>fikr-mulohaza olib, qayta yozganingiz</b> sari oshadi.",
             body=f"""<h4>Tahrir tartibi</h4>
<ol><li>Tuzilma: bo'shliq, savol va usul bir-biriga ulanadimi.</li><li>Dalil: har da'vo manbaga tayanadimi.</li><li>Da'volar: ortiqcha va'da yo'qmi.</li><li>Til: jumlalar aniqmi.</li><li>Dastur talabi: hajm va shakl to'g'rimi.</li></ol>
<p>Ingliz tilidagi jumlalarni silliqlashdan oldin fikrdagi uzilishlarni toping. Qoralama tarixini, manbalar ro'yxatini va matnni o'zingiz yozganingizni ko'rsatadigan izni saqlang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Taqrizchi <i>“savol qiziq, lekin usul yetarli yozilmagan”</i> desa, taqqoslash nuqtasi va ma'lumot rejasini kuchaytiring; tilni keyin tuzatasiz.</div>
<div class="box warn">Matnni butunlay sun'iy intellektga yozdirib, u o'ylab topgan manbalarni qoldirib ketmang.</div>
<div class="srcs">Manba: {KCL}; {UKRIO}. {HOL}.</div>""",
             take="v1 → mezon bo'yicha 5 ta zaif joy → v2 → v3 → dastur shakli. Har versiya saqlanadi.",
             task="<ul><li>v1 qoralamani yozing.</li><li>Baholash mezoni bo'yicha 5 ta zaif joyni toping.</li><li>v2 va v3 ni solishtiring.</li><li>Oxirgi versiyani dastur shakliga keltiring.</li></ul><p><b>O'zingizga savol:</b> taklifning qaysi bo'limida xavf aniq ko'rinadi?</p>",
             ph="Zaif joylar: 1) ... 2) ... ; v2 da o'zgardi: ... ; v3: ..."),
    ],
    tool=dict(id="taklif", short="Taklif", h2="Taklif bo'limlari", sub="Har bo'limni o'z so'zlaringiz bilan yozing: muammo, bo'shliq va savol, usul, hissa, xavf va etika.",
              h3="Taklif qoralamasi", tag="6 maydon", ic="scroll", btn="Taklifni saqlash", badge="Taklif muallifi", min=5,
              fields=[dict(k="sarl", label="Sarlavha", ph="..."),
                      dict(k="muammo", label="Muammo va ahamiyat", type="area", wc="150-250", ph="..."),
                      dict(k="boshliq", label="Bo'shliq va savol", type="area", wc="100-200", ph="..."),
                      dict(k="usul", label="Usul, taqqoslash nuqtasi va tekshiruv", type="area", wc="200-400", ph="..."),
                      dict(k="hissa", label="Yangilik va kutilgan hissa", type="area", wc="80-150", ph="..."),
                      dict(k="xavf", label="Vaqt, xavf va etika", type="area", wc="100-200", ph="...")]),
    check=dict(h2="M4 nazorati", sub="Taklifni topshirishdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Savol aniq va unga javob topsa bo'ladi.", "Fon va bo'shliq ishonchli manbalarga tayangan.", "Usul vazifalar va ma'lumotga mos.",
                      "Taqqoslash nuqtasi va tekshiruv yozilgan.", "Reja qanchalik realligi, noaniqlik va etika yozilgan.", "Gantt jadvalidagi har bosqichning natijasi bor.",
                      "Har iqtibos va DOI qo'lda tekshirilgan.", "Hajm dasturning so'z chegarasiga mos."]),
    art_title="Ilmiy loyiha taklifi (Research Proposal)", art_short="Taklif",
    art=[("Sarlavha", ["sarl"]), ("Muammo va ahamiyat", ["muammo", "a2"]), ("Bo'shliq va savol", ["boshliq", "a3"]), ("Usul va tekshiruv", ["usul", "a4"]),
         ("Yangilik va hissa", ["hissa"]), ("Ish rejasi", ["a5"]), ("Etika va ma'lumot", ["a6", "xavf"]), ("Tahrir izi", ["a1", "a7"])],
    tip="Taklifni ovoz chiqarib o'qing. Intervyuda himoya qila olmaydigan jumlani o'chiring yoki manba bilan mustahkamlang.",
    sources=f"{KCL}; {LEEDS}; {UKRIO}. {STD}",
)
