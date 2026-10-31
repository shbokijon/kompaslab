from common import KCL, LEEDS, UKRIO, HOL, STD

MOD = dict(
    title="Ilmiy loyiha taklifi va metodologiya",
    desc="PhD Lab M4: ilmiy loyiha taklifining (Research Proposal) vazifasi, ilmiy asos va ahamiyat, savol va vazifalar, metod va tekshiruv, ish rejasi, etika va ma'lumotlarni boshqarish, baholash mezoni bilan tahrir. Natija: loyiha taklifi v1–v3.",
    lead="Aniq savol, dalil, metod, xavf va ilmiy hissani bitta tekshiriladigan loyiha taklifiga keltirasiz. Taklif muhandislik hujjati: unda nima qilishingiz va qanday tekshirishingiz ko'rinadi.",
    hero="scroll", weeks="3–4", next="M5. Akademik profil va ariza hujjatlari", next_href="phd-lab-m5.html",
    goals=[("scroll", "Loyiha taklifi v1–v3", "dastur talabiga mos hajmda"),
           ("chart", "Baholash mezoni", "5 ta zaif joy topilgan va tuzatilgan"),
           ("calendar", "Gantt jadvali", "bosqich, natija, zaxira reja")],
    warn=f"Hamma PhD dasturi alohida loyiha taklifi so'ramaydi: e'lon qilingan loyihalarda ko'pincha qisqa ilmiy qiziqish bayoni yetarli. Taklifni o'zingiz yozasiz; Kompas namunalari faqat tuzilmani ko'rsatadi. Talablar {HOL}.",
    lessons=[
        dict(t="Loyiha taklifi va uning vazifasi", short="Vazifa", min=25, kind="🧭 Tushuncha", ic="scroll",
             hook="Ilmiy loyiha taklifi savolni sotadigan reklama matni emas, tekshiriladigan ish rejasi. Avval dasturingiz aynan nimani so'rashini aniqlang: hajm, shakl va baholovchi kim.",
             body=f"""<ul><li>O'z loyihangiz bilan topshirsangiz, to'liq taklif so'ralishi mumkin.</li><li>E'lon qilingan loyihada ko'pincha tayyor loyiha bor va qisqa bayon yetarli.</li><li>Avval toping: so'z chegarasi, shakl, iqtibos uslubi, kim o'qiydi va qaysi mezon bilan baholaydi.</li></ul>
<p>Taklif yangi savolni va uni bajarish mumkinligini asoslaydi. U dissertatsiya natijasini oldindan kafolatlamaydi va boshlangandan keyin rahbar bilan o'zgarishi mumkin.</p>
<div class="box info">King's College London sahifasiga ko'ra taklif odatda 1 500–3 000 so'z; Leeds o'z loyihasi bilan topshiruvchidan taklif yoki ilmiy yo'nalish tavsifini so'raydi. Bu ikki universitet misoli: sizning dasturingiz chegarasi boshqacha bo'lishi mumkin.</div>
<div class="box warn">Tayyor moliyalashtirilgan loyihaga butunlay boshqa mavzu bilan topshirmang: avval e'lon mavzusini o'qing.</div>
<div class="srcs">Manba: {KCL}; {LEEDS}. {HOL}.</div>""",
             take="Taklif: savol va uni bajarish rejasi. Hajm, shakl va baholovchini dastur sahifasidan oling.",
             quiz=[("Har qanday PhD dasturi alohida loyiha taklifini talab qiladi.", "n", "Noto'g'ri: e'lon qilingan loyiha va o'z loyihasi yo'li farq qiladi."),
                   ("Metod yaxshi tanlanganini savol, ma'lumot, tekshiruv va xavflar bilan izchillik ko'rsatadi.", "t", "To'g'ri: metod savolga xizmat qiladi."),
                   ("Etika va xavf bo'limi oxirgi kunda qo'shiladigan rasmiyatchilik.", "n", "Noto'g'ri: ular bajarilishi mumkinlikning bir qismi."),
                   ("Natija hali noma'lum bo'lsa, taklifda tekshiriladigan gipoteza va muqobillar ko'rsatiladi.", "t", "To'g'ri: taklif natija kafolati emas, ilmiy reja.")],
             task="<ul><li>3 ta dastur talabini solishtiring (hajm, shakl, majburiy bo'limlar).</li><li>O'z dasturingiz uchun tuzilmani yozing.</li><li>Qaysi bo'lim ixtiyoriyligini belgilang.</li></ul>",
             ph="Dastur A: ... so'z, bo'limlar: ...; B: ...; mening tuzilmam: ..."),
        dict(t="Ilmiy asos va ahamiyat", short="Asos", min=35, kind="📚 Yozish", ic="books",
             hook="Bo'shliqni ko'rsatishdan oldin nimalar ma'lum ekanini adolatli bayon qiling. Komissiya sizning sohani bilishingizni shu qismdan baholaydi.",
             body="""<p>Adabiyot sintezi tartibi: asosiy natija → cheklov → ziddiyat → imkoniyat. Har iqtibos argumentga xizmat qilsin: maqolalarni sanab chiqish yetarli emas.</p>
<p><b>Ahamiyat</b> qaysi nazariy yoki amaliy qaror yaxshilanishini, kim foydalanishi mumkinligini va nega hozir muhimligini aytadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: \"Energiya inqirozi muhim va sun'iy intellekt hammasini o'zgartiradi\". Aniqroq tuzilma: \"Mavjud kuzatuv ishlari X sharoitda Y usulga tayanadi; uning Z sharoitdagi aniqligi noma'lum, bu esa W qarorining ishonchliligiga ta'sir qiladi\".</div>
<div class="box warn">To'qima iqtibos, tekshirilmagan DOI va \"dunyoda birinchi\" iborasini ishlatmang.</div>""",
             take="Ma'lum → cheklov → ziddiyat → imkoniyat. Ahamiyat: qaysi qaror yaxshilanadi va kim uchun.",
             task="<ul><li>250 so'zlik ilmiy asos yozing.</li><li>5 ta asosiy manbani biriktiring.</li><li>Bitta ahamiyat jumlasini ajrating.</li></ul>",
             ph="Ilmiy asos (250 so'z): ... Ahamiyat: ..."),
        dict(t="Savol va vazifalar", short="Savol", min=30, kind="🎯 Tuzilma", ic="miya",
             hook="Savol va metodni ajratmasangiz, natija oldindan tayyorlangan xulosaga aylanadi. Vazifa \"isbotlash\" emas, \"qaysi sharoitda va nimaga nisbatan\" degan savolga javob berish.",
             body="""<p>Savolda yozing: tizim yoki ishtirokchi, natija, taqqoslash va sharoit. Vazifalar ketma-ket bo'lishi mumkin: asosiy holat → tajriba → tekshiruv → umumlashtirish.</p>
<p>Gipoteza tekshiriladigan bo'lsa, o'lchov va noaniqlik mezoni ham yoziladi. Sifat tadqiqotida gipoteza shart emas.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: \"A usul yaxshiroq ekanini isbotlash\". Aniqroq: \"Qaysi sharoitda va qaysi asosiy usulga nisbatan A usul noaniqlikni kamaytiradi?\" Javob \"kamaytirmaydi\" chiqishi ham ilmiy natija.</div>
<div class="box warn">Maqsadni \"isbotlash\" deb qo'yib, salbiy natijani yashirish ilmiy halollikka zid.</div>""",
             take="Savol: tizim, natija, taqqoslash, sharoit. Vazifa: asosiy holat → tajriba → tekshiruv. Salbiy natija ham natija.",
             task="<ul><li>Bitta savol yozing.</li><li>3 ta vazifa tuzing.</li><li>Har biri uchun kutilgan dalilni belgilang.</li></ul>",
             ph="Savol: ...? Vazifa 1: ... → dalil: ..."),
        dict(t="Metod va tekshiruv", short="Metod", min=40, kind="🧪 Dizayn", ic="chart",
             hook="Yaxshi metod chiroyli algoritm nomi emas, savolga mos dalil yig'ish jarayoni. Komissiya \"qanday tekshirasiz?\" savoliga javob qidiradi.",
             body="""<h4>Tadqiqot dizayni</h4>
<ul><li>Ma'lumot manbasi va tanlama</li><li>O'lchov vositasi va dastlabki ishlov</li><li>Model yoki tahlil usuli</li><li>Taqqoslash uchun asosiy usul ([[baseline]])</li><li>Tekshiruv ([[validation]]) va noaniqlik</li><li>Muvaffaqiyatsizlik mezoni: qachon usul ishlamadi deysiz</li></ul>
<p>Takrorlanuvchanlik uchun dasturiy muhit, metama'lumot va versiyalarni rejalang. Inson ishtirokidagi tadqiqotda tanlama va rozilik alohida yoziladi (4.6).</p>
<div class="box info">\"Mashinali o'qitishdan foydalanaman\" yetarli emas: qaysi kirish ma'lumoti, haqiqiy qiymat qayerdan, ma'lumot qanday bo'linadi, ma'lumot sizib chiqishi ([[data leakage]]) qanday oldi olinadi.</div>
<div class="box warn">Bitta tanlangan ko'rsatkichni haddan tashqari moslashtirish noto'g'ri xulosaga olib keladi.</div>""",
             take="Ma'lumot, o'lchov, usul, asosiy taqqoslash, tekshiruv, noaniqlik, muvaffaqiyatsizlik mezoni. Asosiy usulsiz natija qiymatini isbotlab bo'lmaydi.",
             task="<ul><li>Metod oqim sxemasini chizing.</li><li>2 ta asosiy taqqoslash usulini tanlang.</li><li>Tekshiruv va noaniqlik bandini yozing.</li></ul>",
             ph="Ma'lumot → ishlov → usul → taqqoslash (..., ...) → tekshiruv: ... Noaniqlik: ..."),
        dict(t="Ish rejasi va natijalar", short="Reja", min=30, kind="📅 Gantt", ic="calendar",
             hook="Doktorantura vaqt rejasi ilmiy xavfni boshqarish vositasi. Har bosqich tekshiriladigan natija bilan tugasa, rahbar ham, siz ham qayerda ekaningizni bilasiz.",
             body="""<p>Bosqichlar: adabiyot va qamrov, trening, ma'lumot yig'ish, tahlil, tekshiruv, yozish, ko'rib chiqish va zaxira vaqt. Ular orasidagi bog'liqliklarni belgilang.</p>
<p>Davomiylik (masalan, 36 yoki 48 oy) dasturga bog'liq: rejani rasmiy davomiylikka moslang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Noaniq: \"2-yil: tajribalar\". Tekshiriladigan: \"5-chorak: sifat nazoratidan o'tgan kalibrlash ma'lumoti va asosiy usul bilan xatolik jadvali\".</div>
<div class="box warn">Etika ruxsati yoki dala mavsumi uchun ketadigan vaqtni nol deb olmang.</div>""",
             take="Gantt jadvali: bosqich, bog'liqlik, natija, zaxira. Davomiylik dastur qoidasiga mos.",
             task="<ul><li>4–6 bosqichli Gantt jadvali tuzing.</li><li>Har bosqichga natija yozing.</li><li>Ma'lumot kechiksa nima qilishingizni belgilang.</li></ul>",
             ph="1-chorak: ... → natija: ...; ...; zaxira: ma'lumot kechiksa ..."),
        dict(t="Etika, ma'lumot va ochiqlik", short="Etika", min=30, kind="🛡️ Halollik", ic="shield",
             hook="Ilmiy halollik loyiha taklifining oxirgi rasmiyatchiligi emas: u metod sifatini belgilaydi. Etika ruxsati kerak bo'lsa, ish boshlanishidan oldin olinadi.",
             body=f"""<h4>Tadqiqot turiga qarab tekshiriladi</h4>
<ul><li>Xabardor rozilik va maxfiylik</li><li>Intellektual mulk</li><li>Xavfsizlik va dala ruxsatnomalari</li><li>Eksport nazorati</li><li>Sun'iy intellektdan foydalanishni oshkor qilish</li><li>Ma'lumotlarni boshqarish rejasi ([[Data Management Plan]], DMP)</li></ul>
<p>Ochiq fan barcha maxfiy ma'lumotni ochish degani emas: ochiqlik va xavfsiz kirishni muvozanatlang. Buyuk Britaniyada tadqiqot halolligi bo'yicha asosiy hujjat: Tadqiqot halolligini qo'llab-quvvatlash konkordati.</p>
<div class="box info">Inson ishtirokchilari bilan intervyu bo'lsa, anonimlik va rozilik ish boshlanishidan oldin hal qilinadi; dala ma'lumoti bo'lsa, hududga kirish va xavfsizlik ruxsati muhim.</div>
<div class="box warn">\"Ochiq ma'lumot\" deb shaxsiy yoki litsenziyali ma'lumotni tarqatmang.</div>
<div class="srcs">Manba: {UKRIO}. {HOL}.</div>""",
             take="Rozilik, maxfiylik, mulk, xavfsizlik, AI oshkorligi, DMP. Ruxsat ishdan oldin.",
             task="<ul><li>8 bandli etika xavfi ro'yxatini tuzing.</li><li>Ma'lumotlarni boshqarish rejasining qoralamasini yozing.</li><li>Universitetingiz siyosatiga havola qo'shing.</li></ul>",
             ph="Etika: 1) rozilik — kerak/kerak emas ... DMP: saqlash ..., ulashish ..., o'chirish ..."),
        dict(t="Tahrir va baholash mezoni", short="Tahrir", min=40, kind="✍️ Tahrir", ic="memo",
             hook="Birinchi qoralama ilmiy natija emas: sifat fikr-mulohaza va qayta yozish bilan oshadi. Avval mantiqni, keyin tilni tuzating.",
             body="""<h4>Tahrir tartibi</h4>
<ol><li>Tuzilma: bo'shliq → savol → metod zanjiri uzilmaganmi.</li><li>Dalil: har da'vo manbaga ega.</li><li>Da'volar: ortiqcha va'da yo'q.</li><li>Til: aniq va qisqa.</li><li>Dastur talabiga moslik: hajm, shakl, iqtibos.</li></ol>
<div class="tbl"><table><thead><tr><th>Baholash mezoni</th><th>0</th><th>1</th><th>2</th></tr></thead><tbody>
<tr><td>Savol aniqligi</td><td>Mavzu</td><td>Savol, chegarasiz</td><td>Chegaralangan savol</td></tr>
<tr><td>Bo'shliq dalili</td><td>Yo'q</td><td>1 manba</td><td>2+ manba</td></tr>
<tr><td>Metod mosligi</td><td>Umumiy</td><td>Usul bor</td><td>Usul, taqqoslash, tekshiruv</td></tr>
<tr><td>Bajarilishi mumkinlik</td><td>Yozilmagan</td><td>Qisman</td><td>Resurs va zaxira reja</td></tr>
<tr><td>Etika va ma'lumot</td><td>Yo'q</td><td>Eslatilgan</td><td>Reja bor</td></tr></tbody></table></div>
<div class="box info">Komissiya \"savol qiziq, metod noaniq\" desa, tilni bezash emas, asosiy taqqoslash va ma'lumot rejasini qo'shish kerak.</div>
<div class="box warn">Matnni to'liq sun'iy intellektga topshirib, uning to'qima manbalarini qoldirmang. Qoralamalar tarixini saqlang.</div>""",
             take="Avval tuzilma va dalil, keyin til. 5 mezonli jadval bilan v1 → v2 → v3.",
             task="<ul><li>v1 qoralamani yozing.</li><li>Baholash mezoni bilan 5 ta zaif joyni toping.</li><li>v2 va v3 ni solishtiring.</li><li>Yakuniy shaklni dastur talabiga moslang.</li></ul>",
             ph="v1 ball: .../10; zaif joylar: 1) ... v3 ball: .../10"),
    ],
    tool=dict(id="taklif", short="Taklif", h2="Loyiha taklifi quruvchisi", sub="Muammo → savol → metod → tekshiruv → etika → reja.",
              h3="Taklif qoralamasi", tag="5 maydon", ic="scroll", btn="Qoralamani saqlash", badge="Taklif muhandisi", min=4,
              fields=[dict(k="asos", label="Muammo va ilmiy asos", type="area", wc="200-400", ph="Asosiy manbalar va kontekst"),
                      dict(k="savol", label="Savol va vazifalar", type="area", ph="Aniq savol, 2–3 vazifa"),
                      dict(k="metod", label="Ma'lumot, metod va baholash", type="area", wc="200-500", ph="Tanlama, usul, tekshiruv, noaniqlik"),
                      dict(k="etika", label="Etika, bajarilishi mumkinlik va zaxira reja", type="area", ph="Ruxsatlar, ma'lumot boshqaruvi, B reja"),
                      dict(k="reja", label="Bosqichlar va ilmiy hissa", type="area", ph="Yil yoki chorak bo'yicha o'lchanadigan natijalar")]),
    check=dict(h2="M4 nazorati", sub="Taklifni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Savol aniq va javob berish mumkin.", "Ilmiy asos va bo'shliq ishonchli manbalar bilan.",
                      "Metod vazifa va ma'lumotga mos.", "Asosiy taqqoslash usuli va tekshiruv yozilgan.",
                      "Bajarilishi mumkinlik, noaniqlik va etika aniq.", "Hajm dastur chegarasiga mos.",
                      "Barcha iqtiboslar tekshirilgan, to'qima manba yo'q.", "Qoralamalar tarixi saqlangan."]),
    art_title="Ilmiy loyiha taklifi v1–v3", art_short="Taklif",
    art=[("Talablar", ["a1"]), ("Ilmiy asos", ["asos", "a2"]), ("Savol va vazifalar", ["savol", "a3"]), ("Metod", ["metod", "a4"]),
         ("Ish rejasi", ["reja", "a5"]), ("Etika va ma'lumot", ["etika", "a6"]), ("Tahrir", ["a7"])],
    tip="Taklifingizni o'qigan odam \"bu savolga qanday javob topiladi?\" degan savolga birinchi sahifadayoq javob olsin. Qolgani shu javobni mustahkamlaydi.",
    sources=f"{KCL}; {LEEDS}; {UKRIO}. {STD}",
)
