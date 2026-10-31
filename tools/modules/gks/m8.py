from common import U27, G26, JA, SIK, STD

MOD = dict(
    title="Intervyu, natija va jo'nash",
    desc="GKS Lab M8: GKS intervyusi mantiqi, javob tuzilmasi, bosqich natijalari va universitet tanlovi, jo'nash oldi tayyorgarlik, stipendiya majburiyatlari va rad javobidan keyingi reja. Natija: intervyu kartochkalari va jo'nash rejasi.",
    lead="Hujjatlar o'tgach, sizni gapirib turgan holda ko'rishadi. Bu modulda intervyuga hujjatlaringiz asosida tayyorlanasiz, natijalarga to'g'ri javob berasiz va jo'nashni yoki keyingi siklni rejalaysiz.",
    hero="lock", weeks="2–3", next="",
    goals=[("bulb", "Intervyu kartochkalari", "5 asosiy savolga o'z dalillaringiz bilan javob"),
           ("calendar", "Natija va tanlov rejasi", "bosqich sanalari va universitet tanlovi qoidasi"),
           ("lock", "Jo'nash oldi nazorat ro'yxati", "yoki rad javobidan keyingi B-reja")],
    warn="Intervyu shakli (onlayn yoki yuzma-yuz, til, davomiylik) yo'riqnomada batafsil berilmagan va bosqichga qarab farq qiladi. Taklifnomadagi va rasmiy xabardagi ko'rsatma ustun. Viza va jo'nash talablari universitet taklifnomasi va Koreya elchixonasi e'lonidan olinadi.",
    lessons=[
        dict(t="Intervyu mantiqi", short="Mantiq", min=30, kind="📋 Faktlar", ic="books",
             hook="Intervyu yangi imtihon emas. Komissiya qog'ozda o'qiganini sizning og'zingizdan eshitib, ishonch hosil qilmoqchi.",
             body=f"""<h4>Yo'riqnomada</h4>
<ul><li><span class="trk">U</span> 2027 GKS-U: qobiliyatni baholash hujjatlar ekspertizasi va og'zaki intervyuni o'z ichiga oladi; shakl, davomiylik va sana alohida xabar qilinadi.</li>
<li><span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G: komissiyalar hujjatlar va og'zaki intervyu orqali baholaydi; NIIED ikkinchi bosqichida og'zaki intervyu yo'q. Intervyu elchixona yoki universitet bosqichida bo'ladi.</li></ul>
<h4>Ular nimani tekshiradi</h4>
<ul><li><b>Muallif ekaningizni:</b> bayonot va rejadagi voqealar va fikrlarni o'z so'zingiz bilan tushuntira olasizmi.</li>
<li><b>Aniqlik:</b> nega shu soha, shu dastur, shu universitet.</li>
<li><b>Uddalash:</b> til yili va o'qishni qanday o'tkazasiz, qiyinchilikda nima qilasiz.</li>
<li><b>Maqsad:</b> bitiruvdan keyin bilimni qayerda ishlatasiz.</li></ul>
<div class="box info">Intervyuga tayyorgarlikning asosi M5 va M6 hujjatlaringiz. Ularni qayta o'qing: komissiya ularni allaqachon o'qigan.</div>
<div class="srcs">Manba: {U27}; {G26}.</div>""",
             take="Intervyu hujjatlaringizning og'zaki tekshiruvi: muallif ekaningiz, aniqlik, uddalash va maqsad.",
             task="<ul><li>Bayonot va rejangizni qayta o'qing. Komissiya qaysi 5 joy haqida so'rashi mumkin? Ro'yxat qiling.</li></ul>",
             ph="1) ... haqida 2) ..."),
        dict(t="Savollar va javob tuzilmasi", short="Javob", min=45, kind="🛠 Kartochka", ic="bulb",
             hook="Tayyorlanmagan javob uzun va aylanma bo'ladi. Tuzilmali javob 60–90 soniyada asosiy fikr, dalil va xulosani beradi.",
             body="""<h4>Javob tuzilmasi</h4>
<ol><li><b>Javob:</b> birinchi jumlada savolga to'g'ridan-to'g'ri javob.</li>
<li><b>Dalil:</b> bitta aniq misol (STAR qisqa shakli).</li>
<li><b>Bog'lash:</b> bu Koreyadagi dasturingizga qanday ulanadi.</li></ol>
<h4>Mashq savollari (Kompas tuzgan ro'yxat)</h4>
<ul><li>O'zingiz va o'qishingiz haqida qisqacha gapirib bering.</li>
<li>Nega Koreya va nega aynan shu universitet?</li>
<li>O'quv rejangizni qisqacha tushuntiring; til yilini qanday o'tkazasiz?</li>
<li><span class="trk">M</span> <span class="trk">D</span> Tadqiqot savolingiz va usulingiz nima? Laboratoriya bilan qanday bog'liq?</li>
<li>Eng katta qiyinchiligingiz va undan nima o'rgandingiz?</li>
<li>Bitiruvdan keyin nima qilasiz?</li>
<li>Koreyada yashashning qaysi tomoni siz uchun qiyin bo'lishi mumkin va nima qilasiz?</li></ul>
<div class="box warn">Javoblarni yodlamang, ular sun'iy eshitiladi. Har savol uchun 3 ta kalit so'z va bitta misolni yodda tuting.</div>
<h4>Mashq tartibi</h4>
<ol><li>Har javobni telefonga yozib oling (60–90 soniya).</li><li>Tinglang: birinchi jumla javobmi? Misol aniqmi?</li><li>Bir kishi bilan kutilmagan savollar bilan sinov intervyusi o'tkazing.</li></ol>""",
             take="Har javob: bir jumlada javob, bitta aniq misol, dasturga bog'lash. Yodlamang, kalit so'zlar bilan mashq qiling.",
             task="<ul><li>Pastdagi vositada 5 asosiy savolga kartochka yozing.</li><li>Kamida 3 tasini ovoz yozib mashq qiling va nimani o'zgartirganingizni yozing.</li></ul>",
             ph="Mashqdan keyin o'zgartirganlarim: ..."),
        dict(t="Natijalar va universitet tanlovi", short="Natija", min=30, kind="🎯 Mini-test", ic="calendar",
             hook="Bir nechta universitet qabul qilsa, tanlov uchun bir necha kun bo'ladi. O'ylanib qolgan nomzod muddatni o'tkazib yuborishi mumkin.",
             body=f"""<h4><span class="trk">U</span> 2027 GKS-U natijalari</h4>
<ul><li>Elchixona treki: 1-bosqich natijasi 16-oktabrgacha, NIIED 2-bosqichi noyabrda, universitet 3-bosqichi 23-dekabr 18:00 gacha.</li>
<li>Elchixona trekida tanlangan nomzod yakuniy universitetni Study in Korea saytida 29-dekabr, 18:00 (KST) gacha tanlaydi.</li>
<li>Yakuniy e'lon taxminan 07.01.2027; taklifnomalar 2027-yil yanvarida.</li></ul>
<h4><span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G (o'tgan sikl)</h4>
<ul><li>Universitet natijasi iyun boshida, universitet tanlovini bildirish 12-iyun 18:00 gacha, yakuniy e'lon iyun oxiri.</li></ul>
<h4>Tanlov qilish</h4>
<ul><li>Bir nechta qabul bo'lsa: M2 matritsangizni qayta ko'ring (ilmiy moslik, til, hayot).</li>
<li>Tanlov qilingach, o'zgartirish odatda mumkin emas; 2027 GKS-U ga ko'ra o'qishga kirgach mutaxassislikni ham o'zgartirib bo'lmaydi.</li></ul>
<div class="srcs">Manba: {U27}; {JA}; {G26}; {SIK}.</div>""",
             take="Natija sanalarini va universitet tanlovi muddatini oldindan taqvimga qo'ying; tanlovni M2 mezonlari bilan tez qiling.",
             quiz=[("2027 GKS-U elchixona trekida universitet tanlovi 29-dekabr, 18:00 (KST) gacha bildiriladi.", "t", "To'g'ri."),
                   ("2026 GKS-G da NIIED ikkinchi bosqichida og'zaki intervyu bor.", "n", "Noto'g'ri: NIIED ikkinchi bosqichida og'zaki intervyu yo'q."),
                   ("2027 GKS-U ga ko'ra o'qishga kirgach mutaxassislikni o'zgartirish mumkin emas.", "t", "To'g'ri."),
                   ("Intervyu javoblarini so'zma-so'z yodlash eng yaxshi usul.", "n", "Noto'g'ri: kalit so'zlar va misol bilan mashq qiling.")],
             task="<ul><li>Natija va tanlov sanalarini Toshkent vaqtiga o'girib yozing.</li><li>Ikki universitet qabul qilsa, qaysi birini tanlaysiz va nega?</li></ul>",
             ph="Sanalar: ... Tanlov qoidam: ..."),
        dict(t="Jo'nash oldi tayyorgarlik va majburiyatlar", short="Jo'nash", min=35, kind="✅ Ro'yxat", ic="lock",
             hook="Stipendiya qozonish oxiri emas. Taklifnoma, viza, tibbiy hujjat va chipta uchun ham muddatlar bor.",
             body=f"""<h4>Jo'nash oldi nazorat ro'yxati (Pre-departure checklist)</h4>
<ul><li><b>Taklifnoma:</b> universitet yoki NIIED dan; viza uchun asosiy hujjat.</li>
<li><b>Viza:</b> turi va hujjatlar ro'yxati taklifnoma va Koreya elchixonasi e'lonidan. Pasport amal muddatini tekshiring.</li>
<li><b>Tibbiy:</b> yo'riqnoma nomzoddan butun dastur davomida sog'lom bo'lishni talab qiladi; keyingi bosqichdagi tibbiy ko'rik talablari xabarnomada.</li>
<li><b>Chipta:</b> <span class="trk">U</span> 2027 GKS-U borish-qaytish aviachiptasini qoplaydi. <span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G ekonom-klass chiptani qoplaydi; xarid tartibi (universitet sotib oladi yoki xarajat qaytariladi) yo'riqnomada.</li>
<li><b>Sug'urta:</b> 2026 GKS-G ga ko'ra Koreyaga kirishdan oldingi sug'urta badallari qoplanmaydi; o'zingiz rejalang.</li>
<li><b>Moliya:</b> stipendiya to'lovi Koreyada bank hisobi ochilgach boshlanadi; birinchi haftalar uchun shaxsiy zaxira rejalang. Oylik summalarni joriy yo'riqnomaning moliyaviy jadvalidan oling.</li>
<li><b>Hujjatlar:</b> diplom, transkript, apostil nusxalari, pasport nusxasi, fotosuratlar.</li></ul>
<h4>Stipendiya majburiyatlari (2027 GKS-U)</h4>
<ul><li>Semestr davomida Koreyadan 2 haftadan ortiq chiqib ketish mumkin emas (favqulodda holatlardan tashqari); vaqtinchalik chiqish universitet rahbariyatining ruxsati bilan.</li>
<li>O'qishga kirgach mutaxassislik o'zgartirilmaydi.</li></ul>
<div class="srcs">Manba: {U27}; {JA}; {G26}.</div>""",
             take="Taklifnoma → viza → tibbiy → chipta → sug'urta → moliya. Stipendiya qoidalari (chiqish, mutaxassislik) birinchi kundan amal qiladi.",
             task="<ul><li>Jo'nash oldi ro'yxatini sanalar bilan tuzing; birinchi oy uchun shaxsiy xarajat zaxirasini hisoblang.</li></ul>",
             ph="Taklifnoma: ... Viza: ... Zaxira: ..."),
        dict(t="Rad javobidan keyingi reja", short="B-reja", min=25, kind="🧭 Reja", ic="compass",
             hook="Rad javobi ariza sifatini to'liq o'lchamaydi: kvota kichik, nomzodlar ko'p. Lekin undan to'g'ri xulosa chiqarmasangiz, keyingi yil ham shu natija takrorlanadi.",
             body="""<h4>Uch qadam</h4>
<ol><li><b>Tahlil:</b> qaysi bosqichda to'xtadingiz? Elchixona, NIIED yoki universitet bosqichi turli zaif nuqtani ko'rsatadi.</li>
<li><b>Tuzatish:</b> eng zaif hujjatni (odatda moslik dalili yoki o'quv rejasi) baholash mezoni bilan qayta ko'ring; til sertifikatini oshiring.</li>
<li><b>Muqobil yo'llar:</b> keyingi GKS sikli, boshqa yo'l (elchixona o'rniga universitet treki yoki aksincha), Koreya universitetlarining o'z stipendiyalari, boshqa davlatlar.</li></ol>
<h4>Bosqich bo'yicha ehtimoliy sabab (Kompas tahlili)</h4>
<div class="tbl"><table><thead><tr><th>To'xtagan bosqich</th><th>Tekshiriladigan joy</th></tr></thead><tbody>
<tr><td>Elchixona (1-bosqich)</td><td>Hujjatlar to'liqligi, baho, bayonotning aniqligi, intervyu</td></tr>
<tr><td>NIIED (2-bosqich)</td><td>Umumiy taqqoslash: ball, til, hujjat sifati</td></tr>
<tr><td>Universitet (3-bosqich)</td><td>Dastur bilan moslik, o'quv rejasi, (M, D) professor</td></tr>
</tbody></table></div>
<div class="box warn">Qayta topshirish shartlari va cheklovlari (masalan, avval GKS olganlar) har yil yo'riqnomada. Keyingi siklga o'tishdan oldin muvofiqlikni M0 dagidek qayta tekshiring: yoshingiz va darajangiz o'zgargan bo'lishi mumkin.</div>""",
             take="Rad javobidan keyin: qaysi bosqich, qaysi hujjat, qaysi muqobil yo'l. Muvofiqlikni yangi yo'riqnoma bilan qayta tekshiring.",
             task="<ul><li>B-rejangizni yozing: keyingi sikl sanasi, nimani kuchaytirasiz, qaysi muqobil yo'lni parallel ko'rasiz.</li></ul>",
             ph="Agar rad javobi kelsa: ..."),
    ],
    tool=dict(id="kartochka", short="Kartochka", h2="Intervyu kartochkalari", sub="Har savolga: bir jumlada javob, bitta misol, dasturga bog'lash. Bu matnni yodlamang, kalit so'z sifatida ishlating.",
              h3="5 kartochka", tag="intervyu + jo'nash", ic="bulb", btn="Kartochkalarni saqlash", badge="Suhbatdosh", min=5,
              fields=[dict(k="q1", label="O'zingiz va o'qishingiz haqida", type="area", ph="Javob · misol · bog'lash"),
                      dict(k="q2", label="Nega Koreya, nega shu universitet", type="area", ph=""),
                      dict(k="q3", label="O'quv rejangiz va til yili", type="area", ph=""),
                      dict(k="q4", label="Qiyinchilik va saboq", type="area", ph=""),
                      dict(k="q5", label="Bitiruvdan keyin", type="area", ph=""),
                      dict(k="dep", label="Jo'nash oldi ro'yxati yoki B-reja", type="area", ph="")]),
    check=dict(h2="Intervyu va jo'nash nazorati", sub="Intervyudan va jo'nashdan oldin.", h3="9 bandlik nazorat",
               items=["Bayonot va reja intervyudan oldin qayta o'qilgan.", "Har asosiy savolga kalit so'zlar va bitta misol bor.",
                      "Kamida 3 javob ovoz yozib mashq qilingan.", "Bir kishi bilan sinov intervyusi o'tkazilgan.",
                      "Intervyu shakli va vaqti rasmiy xabardan tekshirilgan (Toshkent vaqti).", "Natija va universitet tanlovi sanalari taqvimda.",
                      "Viza va taklifnoma talablari rasmiy manbadan.", "Birinchi oy uchun shaxsiy moliyaviy zaxira rejalangan.", "B-reja yozilgan."]),
    art_title="Intervyu kartochkalari va jo'nash rejasi", art_short="Yakun",
    art=[("Komissiya so'rashi mumkin bo'lgan joylar", ["a1"]), ("O'zingiz haqida", ["q1"]), ("Nega Koreya", ["q2"]), ("O'quv rejasi va til yili", ["q3"]),
         ("Qiyinchilik va saboq", ["q4"]), ("Bitiruvdan keyin", ["q5"]), ("Natija va tanlov rejasi", ["a3"]), ("Jo'nash oldi ro'yxati", ["dep", "a4"]), ("B-reja", ["a5"])],
    tip="Intervyuda bilmagan savolga \"bilmayman, lekin buni qanday aniqlardim\" deb javob berish, taxmin qilib noto'g'ri gapirishdan kuchliroq.",
    sources=STD,
)
