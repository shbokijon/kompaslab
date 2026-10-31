from common import U27, G26, STD

MOD = dict(
    title="Shaxsiy bayonot",
    desc="GKS Lab M5: GKS shaxsiy bayonot formasi, Kimlik → Dalil → Maqsad → Moslik tuzilmasi, birinchi qoralama, tahrir va o'zaro tahrir. Natija: yakuniy shaxsiy bayonot.",
    lead="Shaxsiy bayonot GKS formasining savollariga javob beradi: siz kimsiz, nimani isbotlay olasiz, qayerga ketyapsiz va nega Koreya. Bu modulda uni M3 dagi dalillardan qurasiz va baholash mezoni bilan tahrir qilasiz.",
    hero="memo", weeks="3", next="O'quv rejasi",
    goals=[("memo", "Yakuniy shaxsiy bayonot", "forma talablariga mos, o'zingiz yozgan"),
           ("chart", "Baholash mezoni natijasi", "5 mezon bo'yicha o'z bahoingiz"),
           ("shield", "Tahrir qaydi", "nima o'zgardi va nega")],
    warn="Bayonotni o'zingiz yozasiz. Kompas namunalari o'rganish uchun; ularni nusxalash, sun'iy intellektga to'liq yozdirish yoki pulli xizmatga yozdirish GKS kelishuvi va akademik halollikka zid. Forma savollari va hajm chegarasi har yil yo'riqnoma ilovasida.",
    lessons=[
        dict(t="Forma savollari va baholovchi mantiqi", short="Forma", min=30, kind="📋 Forma", ic="scroll",
             hook="Ko'p nomzod bayonotni erkin insho deb yozadi va formadagi savollarning yarmiga javob bermaydi. Baholovchi esa aynan shu savollar bo'yicha o'qiydi.",
             body=f"""<h4>Forma haqida faktlar</h4>
<ul><li>Shaxsiy bayonot GKS ning to'ldiriladigan formalaridan biri: <span class="trk">U</span> 2027 GKS-U da 2-forma, <span class="trk">M</span> <span class="trk">D</span> GKS-G da ham formalar ro'yxatida.</li>
<li>2027 GKS-U yo'riqnomasiga ko'ra ingliz yoki koreys tilida yozilishi mumkin.</li>
<li>Forma bandlari va hajm chegarasi forma shablonining o'zida. Ishni boshlashdan oldin shablonni yuklab olib, har bandni alohida yozib chiqing.</li></ul>
<h4>Kim o'qiydi</h4>
<p>Elchixona trekida bayonotni avval elchixona komissiyasi, keyin NIIED, so'ng universitet ko'radi; universitet trekida universitet va NIIED. Har bosqichda o'quvchi boshqa, savol bir xil: <b>bu odam Koreyada o'qishni uddalaydimi va bu stipendiyani maqsadiga ishlatadimi?</b></p>
<h4>Bayonot va o'quv rejasi farqi</h4>
<div class="tbl"><table><thead><tr><th>Shaxsiy bayonot</th><th>O'quv rejasi (M6)</th></tr></thead><tbody>
<tr><td>Kim va nega: motivatsiya, dalil, qadriyat, Koreya tanlovi</td><td>Nima va qanday: o'qish va tadqiqot rejasi, vaqt bo'yicha</td></tr>
<tr><td>O'tmish va hozir og'irroq</td><td>Kelajak og'irroq</td></tr></tbody></table></div>
<p>Ikkala hujjat bir-birini takrorlamasin, lekin zid ham bo'lmasin.</p>
<div class="srcs">Manba: {U27}; {G26}.</div>""",
             take="Bayonot formaning savollariga javob beradi; shablon va hajm chegarasini avval o'qing. Har bosqichdagi baholovchi bitta savolga javob izlaydi.",
             task="<ul><li>Forma shablonidagi barcha bandlarni ko'chiring va har biriga M3 inventaridan qaysi dalil javob berishini yozing.</li></ul>",
             ph="Band 1: ... → dalil: ... Band 2: ..."),
        dict(t="Kimlik → Dalil → Maqsad → Moslik", short="Tuzilma", min=40, kind="🛠 Skelet", ic="compass",
             hook="Tuzilmasiz bayonot xotiralar ro'yxatiga aylanadi. To'rt blokli skelet har paragrafga vazifa beradi.",
             body="""<div class="tbl"><table><thead><tr><th>Blok</th><th>Savol</th><th>Material</th></tr></thead><tbody>
<tr><td><b>Kimlik</b></td><td>Siz kimsiz va qaysi savol sizni harakatga keltiradi?</td><td>M3 profil izohi, kuzatuv → savol</td></tr>
<tr><td><b>Dalil</b></td><td>Buni nimalar isbotlaydi?</td><td>2–3 STAR yozuvi</td></tr>
<tr><td><b>Maqsad</b></td><td>O'qishdan keyin nima qilmoqchisiz?</td><td>Aniq lavozim, soha yoki loyiha turi</td></tr>
<tr><td><b>Moslik</b></td><td>Nega Koreya, nega shu dastur, nega GKS?</td><td>M2 moslik dalillari</td></tr>
</tbody></table></div>
<h4>\"Nega Koreya\" savoliga kuchli javob</h4>
<ul><li>Koreyadagi aniq soha yoki tajriba (masalan, sizning yo'nalishingizdagi sanoat yoki laboratoriya) va unga oid tekshiriladigan fakt.</li>
<li>Universitet dasturidagi aniq fan yoki laboratoriya (M2 dan).</li>
<li>Qaytgandan keyin bu bilimni qayerda qo'llashingiz.</li></ul>
<div class="box warn">\"K-pop va dramalarni yaxshi ko'raman\" yoki \"Koreya rivojlangan davlat\" kabi umumiy sabablar dalil emas. Madaniy qiziqish bo'lsa, u bir jumla, asosiy sabab emas.</div>""",
             take="To'rt blok: Kimlik, Dalil, Maqsad, Moslik. \"Nega Koreya\" javobi umumiy sabab emas, aniq soha, dastur va qaytgandan keyingi reja.",
             task="<ul><li>Har blok uchun 2–3 jumlalik skelet yozing. Har jumla yoniga qaysi dalilga tayanishini qavsda belgilang.</li></ul>",
             ph="Kimlik: ... (M3 profil) Dalil: ... Maqsad: ... Moslik: ..."),
        dict(t="Birinchi qoralama", short="Qoralama", min=60, kind="✍ Qoralama", ic="memo",
             hook="Birinchi qoralama yaxshi bo'lishi shart emas, to'liq bo'lishi shart. Tahrir faqat mavjud matn ustida ishlaydi.",
             body="""<h4>Skeletdan matnga</h4>
<ol><li>Har blokni bitta paragrafga aylantiring; boshlovchi jumla blokning asosiy fikri.</li>
<li>Har paragrafda kamida bitta aniq fakt (raqam, nom, sana).</li>
<li>Paragraflar orasida bog'lovchi: oldingi dalil keyingi maqsadga qanday olib keladi.</li>
<li>Bir o'tirishda yozing, tahrirni ertaga qoldiring.</li></ol>
<h4>Ochilish</h4>
<p>Iqtibos, lug'at ta'rifi yoki \"bolaligimdan\" bilan boshlamang. Ochilish sizning savolingiz yoki aniq bir voqea bo'lsin.</p>
<div class="box info"><b>Kompas tuzgan namuna</b> (o'quv uchun, nusxalash uchun emas):<br><span lang="en">In my second year, our village lost water for three days because the only pump failed and nobody knew why. I started logging pressure readings with a borrowed gauge, and that notebook became my first data set.</span><br><small>Namunada voqea aniq, fakt bor, keyingi gap savolga olib boradi. Sizning voqeangiz boshqacha bo'ladi.</small></div>
<div class="box warn">Sun'iy intellektdan tahrir yoki grammatika uchun foydalanish mumkin bo'lsa ham, matnning mazmuni va voqealari sizniki bo'lishi shart. Intervyuda bayonotdagi har voqea haqida so'rashlari mumkin.</div>""",
             take="Qoralama: har blok bir paragraf, har paragrafda bitta aniq fakt, ochilish aniq voqea yoki savol. Avval to'liq, keyin yaxshi.",
             task="<ul><li>Pastdagi bayonot quruvchida to'liq birinchi qoralamani yozing. So'z hisoblagichiga qarang, lekin forma chegarasi ustun.</li></ul>",
             ph="Qoralama haqida qayd: qayeri qiyin bo'ldi ..."),
        dict(t="Tahrir: faktga almashtirish", short="Tahrir", min=40, kind="🎯 Mini-test", ic="shield",
             hook="Baholovchi \"juda\", \"eng\", \"katta ishtiyoq\" kabi so'zlarni ko'rganda hech narsa bilib olmaydi. Har sifat o'rniga fakt qo'ying.",
             body="""<h4>Uch o'tishli tahrir</h4>
<ol><li><b>Mazmun:</b> har paragraf formadagi bandga javob beradimi? Dalilsiz da'vo bormi?</li>
<li><b>Aniqlik:</b> sifat va umumiy iboralarni faktga almashtiring.</li>
<li><b>Til:</b> grammatika, uzun jumlalar, takrorlar; ovoz chiqarib o'qing.</li></ol>
<div class="tbl"><table><thead><tr><th>Oldin</th><th>Keyin</th></tr></thead><tbody>
<tr><td><span lang="en">I am extremely passionate about renewable energy.</span></td><td><span lang="en">I built a solar dryer for my family apricot harvest and measured a 30% shorter drying time.</span></td></tr>
<tr><td><span lang="en">I was one of the best students.</span></td><td><span lang="en">I ranked 3rd of 62 in my cohort (official transcript).</span></td></tr>
</tbody></table></div>
<p>Jadval Kompas tuzgan o'quv namunasi; raqamlar shartli.</p>
<h4>O'chiriladigan narsalar</h4>
<ul><li>Tekshirib bo'lmaydigan da'vo (\"o'qituvchilarim meni eng iqtidorli deb bilishadi\").</li>
<li>Mubolag'a va katta va'dalar (\"mamlakatim energetikasini o'zgartiraman\").</li>
<li>CV ning qayta sanog'i: ro'yxat bayonotga kerak emas, u formada bor.</li></ul>""",
             take="Tahrir uch o'tishda: mazmun, aniqlik, til. Har sifatni faktga almashtiring, tekshirib bo'lmaydigan da'voni o'chiring.",
             quiz=[("\"Juda katta ishtiyoqim bor\" jumlasi kuchli dalil hisoblanadi.", "n", "Noto'g'ri: bu sifat; dalil aniq harakat va natija."),
                   ("Bayonotda CV dagi barcha yutuqlarni qayta sanab chiqish kerak.", "n", "Noto'g'ri: ro'yxat formada bor; bayonot 2–3 tanlangan dalilga tayanadi."),
                   ("Intervyuda bayonotdagi voqealar haqida savol berilishi mumkin.", "t", "To'g'ri: shuning uchun har voqea sizniki va aniq bo'lishi kerak."),
                   ("Ovoz chiqarib o'qish uzun va noqulay jumlalarni topishga yordam beradi.", "t", "To'g'ri.")],
             task="<ul><li>Qoralamangizdan 5 ta sifat yoki umumiy iborani toping va har birini faktga almashtiring. \"Oldin → keyin\" shaklida yozing.</li></ul>",
             ph="Oldin: ... → Keyin: ..."),
        dict(t="O'zaro tahrir va yakuniy versiya", short="Yakun", min=40, kind="📊 Rubric", ic="chart",
             hook="Siz o'z matningizni xotiradan o'qiysiz, boshqa odam esa sahifadan. O'zaro tahrir (Peer review) siz ko'rmagan bo'shliqlarni ko'rsatadi.",
             body="""<h4>Baholash mezoni (Rubric), har biri 0–4</h4>
<div class="tbl"><table><thead><tr><th>Mezon</th><th>4 ball</th></tr></thead><tbody>
<tr><td>Formaga javob</td><td>Har bandga aniq javob bor</td></tr>
<tr><td>Dalil</td><td>Har asosiy da'vo tekshiriladigan fakt bilan</td></tr>
<tr><td>Izchillik</td><td>Kimlik → dalil → maqsad → moslik mantiqiy zanjir</td></tr>
<tr><td>Moslik</td><td>\"Nega Koreya, nega shu dastur\" aniq va tekshiriladigan</td></tr>
<tr><td>Til</td><td>Tushunarli, xatosiz, mubolag'asiz</td></tr>
</tbody></table></div>
<h4>O'zaro tahrir tartibi</h4>
<ol><li>Tahrirchi (sinfdosh, o'qituvchi) matnni mezon bilan oladi, siz izoh bermaysiz.</li>
<li>U har mezonga ball va bitta izoh yozadi; matnni o'zi qayta yozmaydi.</li>
<li>Siz izohlarni qabul yoki rad etasiz va sababini tahrir qaydiga yozasiz.</li></ol>
<div class="box warn">Tahrirchi matnni sizning o'rningizga qayta yozsa, bu endi sizning bayonotingiz emas. Izoh oling, yozuvni o'zingiz qiling.</div>""",
             take="Yakuniy versiya 5 mezon bo'yicha baholanadi; tahrirchi izoh beradi, matnni siz o'zgartirasiz va qaydini yuritasiz.",
             task="<ul><li>Bayonotingizni mezon bo'yicha o'zingiz ballang, keyin bitta odamga o'zaro tahrirga bering.</li><li>Tahrir qaydini yozing: qaysi izoh qabul qilindi, qaysisi yo'q va nega.</li></ul>",
             ph="O'z bahoim: 3/4/3/4/3. Tahrirchi izohlari: ... Qaror: ..."),
    ],
    tool=dict(id="quruvchi", short="Bayonot", h2="Bayonot quruvchi", sub="To'rt blok va to'liq matn. So'z hisoblagichi mo'ljal; forma chegarasi har doim ustun.",
              h3="Shaxsiy bayonot", tag="4 blok + matn", ic="memo", btn="Bayonotni saqlash", badge="Muallif", min=5,
              fields=[dict(k="b1", label="Kimlik", type="area", ph=""),
                      dict(k="b2", label="Dalil", type="area", ph=""),
                      dict(k="b3", label="Maqsad", type="area", ph=""),
                      dict(k="b4", label="Moslik: nega Koreya, nega shu dastur", type="area", ph=""),
                      dict(k="full", label="To'liq matn", hint="ingliz yoki koreys tilida", type="area", wc="450-900", ph="")]),
    check=dict(h2="Bayonot nazorati", sub="Yakuniy versiyadan oldin.", h3="10 bandlik nazorat",
               items=["Forma shablonidagi har bandga javob bor.", "Hajm forma chegarasidan oshmaydi.",
                      "Ochilish iqtibos yoki umumiy gap emas.", "Har asosiy da'vo tekshiriladigan fakt bilan.",
                      "\"Nega Koreya\" javobi aniq soha va dasturga tayanadi.", "Maqsad aniq: lavozim, soha yoki loyiha turi.",
                      "Mubolag'a va katta va'dalar olib tashlangan.", "O'quv rejasi bilan zid joy yo'q.",
                      "Matnni o'zim yozdim; voqealar haqiqiy.", "O'zaro tahrir va tahrir qaydi bajarilgan."]),
    art_title="Shaxsiy bayonot", art_short="Bayonot",
    art=[("Forma bandlari xaritasi", ["a1"]), ("Skelet", ["a2"]), ("Yakuniy matn", ["full"]), ("Bloklar", ["b1", "b2", "b3", "b4"]),
         ("Tahrir qaydi", ["a4", "a5", "a3"])],
    tip="Bayonotni yozib bo'lgach, ismingizni o'chirib, boshqa nomzodning matni deb o'qing. Agar u yerda sizni boshqalardan ajratadigan bitta aniq fakt topilmasa, matn hali tayyor emas.",
    sources=STD,
)
