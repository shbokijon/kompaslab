from common import CA, UCAS_DATES, UNIASSIST, UNIVERSITALY, CAMPUSCHINA, HOL, STD

MOD = dict(
    title="Ariza muddatlari va ish rejasi",
    desc="Bachelor Lab M4: ariza oynalari (ED, EA, RD, UCAS, portallar), teskari reja, Asosiy nazorat jadvali (Master Tracker), maktab bilan muvozanat, Birinchi bosqichdagi ishlar xulosasi. Natija: nazorat jadvali, muddatdan orqaga tuzilgan ish jadvali (Gantt) va Tayyorgarlik rejasi v1.0.",
    lead="Ko'p arizalar mazmun emas, vaqt tufayli buziladi: test natijasi kech keladi, tavsiya xati muddatdan keyin yuboriladi. Bu modulda barcha muddatlarni bitta tizimga yig'asiz va I bosqichni yakunlovchi tayyorgarlik rejasini yozasiz.",
    hero="calendar", weeks="1–2", next="M5 Baholar va testlar", next_href="bachelor-lab-m5.html",
    goals=[("calendar", "Asosiy nazorat jadvali (Master Tracker)", "har universitet: holat, muddat, hujjatlar, to'lov, natija"),
           ("hourglass", "Muddatdan orqaga tuzilgan ish jadvali (Gantt)", "muddatdan orqaga hisoblangan ishlar"),
           ("scroll", "Tayyorgarlik rejasi v1.0", "kim, qayerga, qachon, qanday moliyalashtirish bilan")],
    warn=f"Bu modulda muddatlarning umumiy tuzilmasi o'rgatiladi. Aniq sanalar har yili e'lon qilinadi: ularni faqat platforma va universitet sahifasidan oling ({HOL}).",
    lessons=[
        dict(t="Ariza oynalari", short="Oynalar", min=30, kind="🎯 Mini-test", ic="calendar",
             hook="AQShda bir xil universitetga uch xil muddatda ariza berish mumkin va har biri boshqa majburiyat bilan keladi. Noto'g'ri tanlangan oyna sizni boshqa takliflardan voz kechishga majbur qilishi mumkin.",
             body=f"""<h4>AQSh</h4>
<div class="tbl"><table><thead><tr><th>Oyna</th><th>Qachon (odatda)</th><th>Majburiyat</th></tr></thead><tbody>
<tr><td><b>Erta qaror</b> ([[Early Decision, ED]])</td><td>Kuz (ko'pincha noyabr boshi yoki o'rtasi)</td><td>Majburiy: qabul qilinsangiz, boshqa arizalarni qaytarib olasiz. Faqat bitta universitetga. Moliyaviy yordam yetarli bo'lmasa, odatda chiqish mumkin, lekin buni oldindan universitet qoidasidan o'qing</td></tr>
<tr><td><b>Erta ariza</b> ([[Early Action, EA]])</td><td>Kuz</td><td>Majburiy emas. Ba'zi universitetlarda cheklangan shakli ([[Restrictive EA]]) boshqa erta arizalarni taqiqlaydi</td></tr>
<tr><td><b>Oddiy muddat</b> ([[Regular Decision, RD]])</td><td>Qish (ko'pincha yanvar)</td><td>Majburiy emas</td></tr>
</tbody></table></div>
<p>Xalqaro talaba uchun ED xavfli bo'lishi mumkin: moliyaviy yordam taklifini boshqa universitetlar bilan solishtira olmaysiz.</p>
<h4>Buyuk Britaniya (UCAS)</h4>
<p>Oksford, Kembrij va ko'p tibbiyot dasturlari uchun erta muddat (oktabr o'rtasi). Qolgan dasturlar uchun yanvardagi \"teng ko'rib chiqish\" muddati ([[equal consideration date]]). Xalqaro abituriyentlar uchun keyinroq ham ariza qabul qilinishi mumkin, lekin joylar kamayadi.</p>
<h4>To'g'ridan-to'g'ri portallar</h4>
<p>Germaniya (uni-assist yoki universitet portali), Italiya (universitet arizasi + Universitaly), Xitoy (universitet portali va CSC), Koreya va boshqalar: har universitetning o'z muddati, ko'pincha mamlakat o'qish yilidan 6–10 oy oldin.</p>
<div class="box warn"><b>Qobiq qoidasi.</b> Jadvalga sana yozganda manbani va tekshirilgan kunni qo'shing. Eski yildan qolgan sana eng ko'p uchraydigan xato.</div>
<div class="srcs">Manba: {CA}; {UCAS_DATES}; {UNIASSIST}; {UNIVERSITALY}; {CAMPUSCHINA}. {HOL}.</div>""",
             take="ED majburiy, EA va RD majburiy emas; UCAS'da erta va yanvar muddatlari bor; portallarda har universitetning o'z muddati. Har sanani manba bilan yozing.",
             quiz=[("Early Decision bilan qabul qilinsangiz, odatda boshqa arizalarni qaytarib olishingiz kerak.", "t", "To'g'ri: ED majburiy kelishuv."),
                   ("Early Action ham ED kabi majburiy.", "n", "Noto'g'ri: EA majburiy emas, lekin Restrictive EA boshqa erta arizalarni cheklaydi."),
                   ("Oksford va Kembrij uchun UCAS muddati boshqa dasturlarnikidan erta.", "t", "To'g'ri: odatda oktabr o'rtasida."),
                   ("O'tgan yilgi muddatni bu yil ham ishlatish xavfsiz.", "n", "Noto'g'ri: sanalar har yili e'lon qilinadi va o'zgarishi mumkin.")],
             task="<ul><li>Roʻyxatingizdagi har universitet uchun ariza oynasini va muddatni rasmiy sahifadan yozing.</li><li>ED yoki EA ni ko'rib chiqayotgan bo'lsangiz, nima uchun ekanini yozing.</li></ul>",
             ph="... — RD, muddat: ... (manba, sana). ... — EA ..."),
        dict(t="Teskari reja", short="Teskari reja", min=30, kind="🛠 Gantt", ic="hourglass",
             hook="Muddatdan boshlab orqaga hisoblash \"qachon boshlashim kerak?\" degan savolga aniq javob beradi. Ko'p ishlar bir-biriga bog'liq: test natijasisiz ariza yo'q, tarjimasiz apostil yo'q.",
             body="""<h4>Muddatdan orqaga tuzilgan ish jadvali (Gantt)</h4>
<p>Gantt jadvali ([[Gantt chart]]) ishlarni vaqt chizig'ida ko'rsatadi. Teskari variantda eng erta muddatdan boshlab orqaga yurasiz.</p>
<div class="tbl"><table><thead><tr><th>Ish</th><th>Muddatdan necha hafta oldin</th><th>Nimaga bog'liq</th></tr></thead><tbody>
<tr><td>Arizani topshirish</td><td>1 hafta (zaxira)</td><td>Hamma narsa</td></tr>
<tr><td>Insholar yakuniy versiyasi</td><td>2–3</td><td>Tahrir (M10)</td></tr>
<tr><td>Tavsiya so'rovi</td><td>6–8</td><td>Yutuqlar varaqasi (M8)</td></tr>
<tr><td>Til testi natijasi</td><td>8–12</td><td>Imtihon sanasi, natija kelishi</td></tr>
<tr><td>SAT yoki ACT (kerak bo'lsa)</td><td>10–16</td><td>Ro'yxatdan o'tish</td></tr>
<tr><td>Tarjima va apostil</td><td>8–10</td><td>Attestat, transkript</td></tr>
<tr><td>Insho birinchi qoralamasi</td><td>10–12</td><td>Qiziqish sohasi bayoni (M3)</td></tr>
</tbody></table></div>
<p>Haftalar tavsiya, qat'iy qoida emas. Testni qayta topshirish ehtimoli bo'lsa, test qatorini yana 6–8 hafta oldinga suring.</p>
<div class="box info">Har ish uchun bitta \"bloklovchi\" savol yozing: bu ish nimani kutmoqda? Shu savol rejani real qiladi.</div>""",
             take="Eng erta muddatdan orqaga yuring: test, tavsiya, tarjima va insho haftalarini belgilang. Qayta topshirish uchun zaxira qo'ying.",
             task="<ul><li>Eng erta muddatingizdan orqaga 7 ta asosiy ishni haftalar bo'yicha joylashtiring.</li><li>Har ishning nimaga bog'liqligini yozing.</li></ul>",
             ph="Eng erta muddat: ... ; insho qoralama: ... hafta; tavsiya: ...; test: ..."),
        dict(t="Asosiy nazorat jadvali", short="Tracker", min=25, kind="📋 Jadval", ic="scroll",
             hook="10 ta universitet, har birida 6–8 hujjat va bir nechta muddat. Xotirada saqlab bo'lmaydi. Bitta jadval hamma narsani ko'rinadigan qiladi.",
             body="""<h4>Ustunlar</h4>
<div class="tbl"><table><thead><tr><th>Ustun</th><th>Misol</th></tr></thead><tbody>
<tr><td>Universitet va dastur</td><td>... universiteti, Mechanical Engineering</td></tr>
<tr><td>Platforma</td><td>Common App / UCAS / portal</td></tr>
<tr><td>Oyna va muddat</td><td>RD, sana (manba)</td></tr>
<tr><td>Hujjatlar</td><td>Insho ✓, qo'shimcha insho ✗, tavsiya 1/2, test yuborilgan ✗</td></tr>
<tr><td>To'lov</td><td>Ariza to'lovi yoki ozod qilish</td></tr>
<tr><td>Holat</td><td>Boshlanmagan / jarayonda / topshirilgan / natija</td></tr>
<tr><td>Natija va javob muddati</td><td>M15 da to'ldiriladi</td></tr>
</tbody></table></div>
<h4>Ishlatish qoidasi</h4>
<ul><li>Jadvalni haftasiga bir marta, bir xil kunda yangilang.</li><li>Rang: qizil (2 haftadan kam qoldi), sariq (2–6 hafta), yashil (topshirilgan).</li><li>Jadvalning bitta nusxasi bo'lsin; bir nechta nusxa chalkashlik keltiradi.</li></ul>
<div class="box info">Jadvalni [[Google Sheets]], Excel yoki qog'ozda yuritish mumkin. Asbob emas, haftalik yangilash odati muhim.</div>""",
             take="Asosiy nazorat jadvali: universitet, platforma, muddat, hujjatlar, to'lov, holat va natija. Uni haftasiga bir marta yangilang.",
             task="<ul><li>O'z jadvalingizni yarating va kamida 5 universitetni kiriting.</li><li>Haftalik yangilash kunini tanlang.</li></ul>",
             ph="Jadval qayerda: ... ; yangilash kuni: ... ; kiritilgan: ..."),
        dict(t="Maktab bilan muvozanat", short="Ritm", min=20, kind="⏱ Haftalik ritm", ic="bell",
             hook="Ariza jarayoni maktabning eng og'ir yiliga to'g'ri keladi. Baholar tushib ketsa, ariza ham zaiflashadi. Ritm ikkalasini ham saqlaydi.",
             body="""<h4>Haftasiga 3–5 soat</h4>
<p>Bachelor Lab haftasiga 3–5 soatga mo'ljallangan. Bu ikki-uch blokka bo'linadi:</p>
<ul><li><b>Blok 1 (1–2 soat)</b>: darslar va topshiriqlar.</li><li><b>Blok 2 (1–2 soat)</b>: hujjat ustida ish (insho, ro'yxat, jadval).</li><li><b>Blok 3 (30–60 daqiqa)</b>: nazorat jadvalini yangilash va keyingi hafta rejasi.</li></ul>
<h4>Imtihon davrlari</h4>
<p>Choraklik imtihonlar, olimpiadalar va bitiruv imtihonlari oldidan yuklamani kamaytiring. Teskari rejaga bu haftalarni oldindan \"yengil hafta\" deb belgilang.</p>
<h4>Dam olish</h4>
<p>Haftasiga kamida bir kun ariza ishi yo'q. Uyqu va jismoniy faollik test natijasiga ham ta'sir qiladi.</p>
<div class="box warn">Agar 3 hafta ketma-ket reja bajarilmasa, rejani qisqartiring: universitetlar sonini yoki qo'shimcha faoliyatni kamaytiring. Charchoq bilan yozilgan insho kuchsiz bo'ladi.</div>""",
             take="Haftasiga 3–5 soat, uch blok. Imtihon haftalarini oldindan yengil qiling va haftada bir kun dam oling.",
             task="<ul><li>Haftalik jadvalingizda 3 blok uchun aniq kun va vaqtni belgilang.</li><li>Keyingi 3 oydagi imtihon haftalarini yozing.</li></ul>",
             ph="Blok 1: seshanba 19:00–20:30 ... Imtihonlar: ..."),
        dict(t="Birinchi bosqichdagi ishlar xulosasi", short="Xulosa", min=30, kind="🧩 Tayyorgarlik rejasi", ic="memo",
             hook="Birinchi to'rt modulda to'plangan qarorlar alohida varaqlarda yotsa, foydasi kam. Tayyorgarlik rejasi ularni bitta sahifaga yig'adi va keyingi bosqichlar uchun yo'l ko'rsatadi.",
             body="""<h4>Tayyorgarlik rejasi v1.0: to'rt savol</h4>
<div class="tbl"><table><thead><tr><th>Savol</th><th>Javob qayerdan</th></tr></thead><tbody>
<tr><td><b>Kim?</b> Profil va soha</td><td>M3: bir jumlali profil, qiziqish sohasi bayoni</td></tr>
<tr><td><b>Qayerga?</b> Mamlakatlar va universitetlar</td><td>M1–M2: talablar jadvali, saralangan ro'yxat</td></tr>
<tr><td><b>Qachon?</b> Muddatlar va reja</td><td>M4: nazorat jadvali, teskari Gantt</td></tr>
<tr><td><b>Qanday moliyalashtirish bilan?</b></td><td>M2 byudjeti; to'liq reja M11–M12</td></tr>
</tbody></table></div>
<h4>Xavflar</h4>
<p>Hujjat oxiriga 3 ta asosiy xavfni yozing (masalan: til testi natijasi yetmasligi, attestat talabi, oilaviy byudjet) va har biri uchun bitta zaxira harakat.</p>
<div class="box info">Bu hujjat \"v1.0\": II va III bosqichlarda yangilanadi. Uni oila bilan muhokama qilish uchun ham ishlating.</div>""",
             take="Tayyorgarlik rejasi to'rt savolga javob beradi: kim, qayerga, qachon, qanday moliyalashtirish bilan; oxirida 3 xavf va zaxira harakatlar.",
             task="<ul><li>Pastdagi vositada Tayyorgarlik rejasini to'ldiring.</li><li>3 xavf va har biri uchun zaxira harakatni yozing.</li></ul>",
             ph="Xavf 1: ... → zaxira: ... Xavf 2: ..."),
    ],
    tool=dict(id="strategiya", short="Strategiya", h2="Tayyorgarlik rejasi v1.0", sub="I bosqich yakuni: barcha qarorlar bitta sahifada.",
              h3="Tayyorgarlik rejasi", tag="6 maydon", ic="memo", btn="Hujjatni saqlash", badge="Strateg", min=5,
              fields=[dict(k="kim", label="Kim? Profil va soha", type="area", ph="Profil: ... Soha: ..."),
                      dict(k="qayer", label="Qayerga? Mamlakatlar va 8–12 universitet", type="area", ph="Orzu: ... Mo'ljal: ... Ishonchli: ..."),
                      dict(k="qachon", label="Qachon? Asosiy muddatlar", hint="manba va sana bilan", type="area", ph="Eng erta: ... ; asosiy: ..."),
                      dict(k="pul", label="Qanday moliyalashtirish bilan?", type="area", ph="Oila: ... Stipendiyalar: ... Arizalar byudjeti: ..."),
                      dict(k="tracker", label="Nazorat jadvali qayerda va yangilash kuni", ph="Google Sheets, har yakshanba"),
                      dict(k="xavf", label="3 xavf va zaxira harakat", type="area", ph="1) ... → ... 2) ... → ... 3) ... → ...")]),
    check=dict(h2="I bosqich nazorati", sub="II bosqichga o'tishdan oldin tekshiring.", h3="9 bandlik nazorat",
               items=["Har universitet uchun ariza oynasi va muddat manba bilan yozilgan.", "ED ni tanlasam, uning majburiyatini va moliyaviy yordam qoidasini o'qidim.",
                      "Muddatdan orqaga tuzilgan ish jadvali (Gantt)da test, tavsiya, tarjima va insho haftalari bor.", "Asosiy nazorat jadvali yaratilgan va kamida 5 universitet kiritilgan.",
                      "Haftalik yangilash kuni belgilangan.", "Imtihon haftalari \"yengil hafta\" deb belgilangan.",
                      "Tayyorgarlik rejasining to'rt savoliga javob bor.", "3 xavf va zaxira harakat yozilgan.", "Tayyorgarlik rejasi oila bilan muhokama qilingan."]),
    art_title="Tayyorgarlik rejasi v1.0", art_short="Strategiya",
    art=[("Kim", ["kim"]), ("Qayerga", ["qayer"]), ("Qachon", ["qachon", "a1"]), ("Teskari reja", ["a2"]),
         ("Nazorat jadvali va ritm", ["tracker", "a3", "a4"]), ("Moliyalashtirish", ["pul"]), ("Xavflar va zaxira", ["xavf", "a5"])],
    tip="Jadvalni yangilash 15 daqiqa oladi, unutilgan muddat esa bir yil. Har hafta bir xil kunda, bir xil vaqtda yangilang.",
    sources=f"{CA}; {UCAS_DATES}; {UNIASSIST}; {UNIVERSITALY}; {CAMPUSCHINA}. {STD}",
)
