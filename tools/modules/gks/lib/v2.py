from common import U27, G26, SIK, JA, STD

MOD = dict(
    title="Universitet va dastur tanlash",
    desc="GKS Lab M2: elchixona yoki universitet treki, A va B turdagi universitetlar, dasturni o'qish, saralangan ro'yxat va kvotani to'g'ri talqin qilish. Natija: 3 ta asoslangan universitet tanlovi.",
    lead="GKS da universitet tanlovi qoidalar bilan cheklangan: qaysi yo'l, nechta universitet, qaysi turdan. Bu modulda shu qoidalar ichida o'zingizga mos 3 ta tanlovni dalil bilan asoslaysiz.",
    hero="telescope", weeks="2–3", next="Nomzod profili va dalillar",
    goals=[("compass", "Yo'l qarori", "elchixona yoki universitet treki, sababi bilan"),
           ("telescope", "3 ta universitet tanlovi", "turi (A/B), fakultet va moslik dalili bilan"),
           ("chart", "Xavf izohi", "kvota va raqobatni to'g'ri o'qish asosida")],
    warn="Universitetlar ro'yxati, A/B turlari va kvotalar har yil yo'riqnoma ilovasida yangilanadi. Bu yerdagi raqamlar 2027 GKS-U va 2026 GKS-G yo'riqnomalaridan, 31.10.2026 holatiga.",
    lessons=[
        dict(t="Elchixona treki yoki universitet treki", short="Yo'l", min=35, kind="🎯 Mini-test", ic="compass",
             hook="Ikki yo'l ikki xil o'yin: elchixona trekida avval O'zbekistondagi raqiblar bilan bellashasiz, universitet trekida esa bitta universitetning barcha nomzodlari bilan. Yo'lni tanlash keyingi barcha qarorlarni belgilaydi.",
             body=f"""<h4>Bosqichlar</h4>
<div class="tbl"><table><thead><tr><th></th><th>Elchixona treki</th><th>Universitet treki</th></tr></thead><tbody>
<tr><td>1-bosqich</td><td>Koreya elchixonasi</td><td>Universitet</td></tr>
<tr><td>2-bosqich</td><td>NIIED</td><td>NIIED (yakuniy e'lon)</td></tr>
<tr><td>3-bosqich</td><td>Universitet</td><td>Yo'q</td></tr>
<tr><td>Universitetlar soni</td><td>3 tagacha (qoidalar 2-darsda)</td><td>Bitta universitet, bitta yo'nalish</td></tr>
</tbody></table></div>
<h4><span class="trk">U</span> 2027 GKS-U: O'zbekiston uchun</h4>
<ul><li><b>Elchixona treki:</b> O'zbekiston kvotasi 3 o'rin: umumiy dastur 1, R-GKS (mintaqaviy universitetlar) 1, chet eldagi koreyslar 1.</li>
<li><b>Universitet treki:</b> mamlakatlar bo'yicha kvota yo'q. UIC dasturi (fan va muhandislik yo'nalishlari) barcha mamlakatlarga ochiq.</li></ul>
<h4><span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G: O'zbekiston uchun</h4>
<ul><li><b>Elchixona treki:</b> umumiy 13 o'rin, chet eldagi koreyslar 6 o'rin.</li>
<li><b>Universitet treki:</b> umumiy 6 o'rin, R-GKS 6 o'rin.</li></ul>
<div class="box info"><b>Qaror qoidasi.</b> Universitetni hali tanlamagan bo'lsangiz va bir nechtasini ko'rsatmoqchi bo'lsangiz, elchixona treki mantiqiyroq. Aniq universitet va (M, D uchun) professor bilan moslik dalili kuchli bo'lsa, universitet treki ko'rib chiqiladi. Ikkala yo'lga bir siklda topshirish qoidalarini o'z yo'riqnomangizdan tekshiring.</div>
<div class="srcs">Manba: {U27}; {G26}; {JA}. 31.10.2026 holatiga.</div>""",
             take="Elchixona treki: elchixona → NIIED → universitet, 3 tagacha universitet. Universitet treki: universitet → NIIED, bitta universitet. Kvota raqamlari yo'lga qarab keskin farq qiladi.",
             quiz=[("Universitet trekida birinchi bosqichni Koreya elchixonasi o'tkazadi.", "n", "Noto'g'ri: universitet trekida birinchi bosqichni universitet o'tkazadi."),
                   ("2027 GKS-U da O'zbekistonning elchixona treki kvotasi jami 3 o'rin.", "t", "To'g'ri: umumiy 1, R-GKS 1, chet eldagi koreyslar 1."),
                   ("Elchixona trekida 3 tagacha universitet tanlanadi.", "t", "To'g'ri: 2027 GKS-U va 2026 GKS-G da shunday."),
                   ("2027 GKS-U universitet trekida mamlakatlar bo'yicha kvota bor.", "n", "Noto'g'ri: universitet treki uchun mamlakat kvotasi berilmagan.")],
             task="<ul><li>Ikki yo'lni o'z holatingizga qo'yib solishtiring: universitet tanlovingiz qanchalik aniq, moslik dalilingiz qanchalik kuchli.</li><li>Qaysi yo'lni tanlaysiz va nega? 3–4 jumla.</li></ul>",
             ph="Yo'l: ... Sabab: ..."),
        dict(t="A va B turdagi universitetlar", short="A/B", min=30, kind="📋 Qoidalar", ic="scroll",
             hook="Uchta kuchli universitetni tanlab, hammasini A turidan qo'ysangiz, arizangiz qoidaga zid bo'ladi. A/B qoidasi tanlov emas, shart.",
             body=f"""<h4>Elchixona treki qoidalari</h4>
<ul><li><span class="trk">U</span> 2027 GKS-U: A turi 28, B turi 42 ta muassasa. Umumiy dastur nomzodi 3 tagacha universitet tanlaydi, <b>kamida bittasi B turidan</b>. R-GKS nomzodi faqat B turidan 2 tagacha universitet tanlaydi.</li>
<li><span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G: 3 tagacha <b>har xil</b> universitet, kamida bittasi B turidan. Bitta universitetning bir nechta bo'limiga topshirilmaydi.</li>
<li>B bo'limida ko'rsatilgan joyga A turdagi universitetni yozish arizani chiqarib yuborishga olib kelishi mumkin.</li></ul>
<h4>A va B nimani bildiradi</h4>
<p>Turlar yo'riqnoma ilovasidagi ro'yxat bilan belgilanadi; B turi asosan poytaxt hududidan tashqaridagi universitetlarni o'z ichiga oladi. Bu \"kuchli\" va \"kuchsiz\" degani emas: ko'plab B turdagi universitetlar sizning sohangizda kuchli laboratoriyaga ega bo'lishi mumkin. Tanlovni nomga emas, fakultet va dasturga qarab qiling.</p>
<div class="box warn"><b>Har yil tekshiring.</b> Universitet qaysi turda turgani va qaysi yo'nalishlar ochiqligi ilovada har yili yangilanadi. O'tgan yilgi ro'yxatdan nusxa olmang.</div>
<div class="srcs">Manba: {U27}; {G26}; {JA}. 31.10.2026 holatiga.</div>""",
             take="Elchixona trekida 3 tagacha universitet, kamida bittasi B turidan; R-GKS da faqat B turi. Turni joriy yil ilovasidan tekshiring.",
             task="<ul><li>Joriy (yoki eng so'nggi) yo'riqnoma ilovasidan sohangiz bo'yicha 6–8 universitetni yozing va har birining turini (A/B) belgilang.</li></ul>",
             ph="1) ... (A) 2) ... (B) ..."),
        dict(t="Dastur va fakultetni o'qish", short="Dastur", min=40, kind="🔎 Tadqiqot", ic="books",
             hook="Universitet nomi komissiyaga hech narsa demaydi. \"Nega aynan shu dastur?\" savoliga javob fakultet sahifasida, o'quv rejasida va laboratoriyalarda yotadi.",
             body=f"""<h4>Nimani o'qiysiz</h4>
<ul><li><b>Yo'riqnoma ilovasi:</b> universitetda GKS uchun ochiq yo'nalishlar, o'qitish tili, maxsus talablar.</li>
<li><b>Fakultet sahifasi:</b> o'quv rejasi (fanlar ro'yxati), o'qitish tili, bitiruv talablari.</li>
<li><span class="trk">U</span> 1–2-kurs fanlari: siz kuchli bo'lgan asosiy fanlar bilan bog'liqmi?</li>
<li><span class="trk">M</span> <span class="trk">D</span> Laboratoriya va professorlar: so'nggi 3 yildagi maqolalar, loyihalar, foydalanilgan usullar. Bu M4 dagi professorga xat va M6 dagi o'quv rejasi uchun xom ashyo.</li></ul>
<h4>Moslik dalili</h4>
<p>Har universitet uchun bitta jumlalik dalil yozing: <i>\"Fakultetdagi X laboratoriyasi Y usulida ishlaydi; mening Z tajribam shu usulga yaqin.\"</i> Dalil tekshiriladigan bo'lishi kerak: havola, maqola nomi, fan nomi.</p>
<div class="box info"><b>Kompas tuzgan namuna</b> (shartli): <span lang="en">The Department of Earth and Environmental Sciences offers a groundwater modelling track; my bachelor thesis used MODFLOW for a similar aquifer.</span> Bu namunada universitet nomi yo'q; o'zingiznikini haqiqiy havolalar bilan yozing.</div>
<div class="box warn">Sharhlar va forumlardagi \"eng yaxshi universitet\" ro'yxatlariga tayanmang. Birlamchi manba: yo'riqnoma ilovasi va universitetning rasmiy sahifasi.</div>
<div class="srcs">Manba: {SIK}; {U27}; {G26}.</div>""",
             take="Tanlov fakultet, dastur va (M, D uchun) laboratoriya darajasida qilinadi. Har universitet uchun tekshiriladigan bitta moslik dalili yozing.",
             task="<ul><li>Saralangan 6–8 universitetdan har biri uchun: dastur nomi, o'qitish tili, bitta moslik dalili va havola.</li></ul>",
             ph="Universitet · dastur · til · dalil · havola"),
        dict(t="Saralangan ro'yxat va xavf taqsimoti", short="Ro'yxat", min=35, kind="🛠 Matritsa", ic="chart",
             hook="Uchta o'rinni bir xil xavfdagi universitetlarga sarflash bitta savatga barcha tuxumni qo'yishdir. Saralangan ro'yxat (Shortlist) xavfni taqsimlaydi.",
             body=f"""<h4>Baholash mezoni (Rubric)</h4>
<div class="tbl"><table><thead><tr><th>Mezon</th><th>Savol</th><th>Ball</th></tr></thead><tbody>
<tr><td>Ilmiy moslik</td><td>Dastur yoki laboratoriya mening tajribamga bevosita bog'liqmi?</td><td>0–3</td></tr>
<tr><td>Til</td><td>O'qitish tili va mening sertifikatim mosmi?</td><td>0–2</td></tr>
<tr><td>Qoidalar</td><td>Turi (A/B) va yo'l qoidasiga mosmi?</td><td>0 yoki 2</td></tr>
<tr><td>Hayot</td><td>Shahar, xarajat, iqlim men uchun maqbulmi?</td><td>0–1</td></tr>
<tr><td>Dalil sifati</td><td>Mosligimni bitta tekshiriladigan jumlada aytib bera olamanmi?</td><td>0–2</td></tr>
</tbody></table></div>
<h4>Taqsimot</h4>
<ul><li>Uchta tanlovning hammasi bir xil xavfli bo'lmasin: kamida bittasi mosligi eng kuchli, B turidagi universitet bo'lsin.</li>
<li>Qoidalar mezonidan 0 olgan universitet ro'yxatdan chiqadi.</li>
<li>Ball teng bo'lsa, ilmiy moslik ustun.</li></ul>
<div class="box info">Bu jadval Kompas tahlili, NIIED baholash mezoni emas. Rasmiy baholash mezonlari yo'riqnomada e'lon qilinadi; jadval faqat sizning tanlovingizni tartibga soladi.</div>""",
             take="Har universitetni bir xil mezon bilan ballang; qoidaga zid tanlov chiqadi, qolganlari orasida xavfni taqsimlang.",
             task="<ul><li>6–8 universitetni jadval bo'yicha ballang va eng yaxshi 3 tasini tanlang.</li><li>Uchtasining kamida bittasi B turidanmi? Tekshiring.</li></ul>",
             ph="1) ... 9/10 (B) 2) ... 3) ..."),
        dict(t="Kvota va raqobatni to'g'ri o'qish", short="Kvota", min=25, kind="📊 Tahlil", ic="hourglass",
             hook="\"13 o'rin bor, demak imkonim bor\" va \"1 o'rin bor, umuman umid yo'q\" ikkalasi ham noto'g'ri xulosa. Kvota raqobatchilar sonisiz to'liq ma'lumot emas.",
             body=f"""<h4>Kvota nimani aytadi va nimani aytmaydi</h4>
<ul><li><b>Aytadi:</b> shu yo'l bo'yicha O'zbekistondan yakuniy tanlanadigan maksimal o'rin.</li>
<li><b>Aytmaydi:</b> nechta nomzod topshirishi, bosqichlarda nechta odam o'tishi, sizning imkoningiz qancha.</li></ul>
<p>Rasmiy yo'riqnomalar topshirgan nomzodlar sonini e'lon qilmaydi. Shuning uchun \"qabul foizi\" haqidagi har qanday raqamni manbasini tekshirmasdan ishlatmang.</p>
<h4>Amaliy xulosa</h4>
<ul><li><span class="trk">U</span> 2027 GKS-U da O'zbekiston elchixona trekida 3 o'rin, universitet trekida mamlakat kvotasi yo'q. Bu universitet trekining (masalan UIC, fan va muhandislik) ahamiyatini oshiradi, lekin u yerda butun dunyodan nomzodlar bilan bellashasiz.</li>
<li><span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G da elchixona treki umumiy kvotasi 13, universitet treki umumiy 6 va R-GKS 6. Ikki yo'lni ham ko'rib chiqing.</li>
<li>Kvota kichik bo'lsa, hujjat sifati va moslik dalili og'irroq vazn oladi. Tayyorgarlikni shunga moslang, umidni emas.</li></ul>
<div class="srcs">Manba: {U27}; {G26}. 31.10.2026 holatiga.</div>""",
             take="Kvota raqobatchilar sonini aytmaydi. Imkon foizini taxmin qilmang; tayyorgarlik sifatini oshiring va ikkala yo'lni ko'rib chiqing.",
             task="<ul><li>O'z treking bo'yicha O'zbekiston kvotasini yo'riqnomadan yozing (har yo'l alohida).</li><li>Bu raqam sizning rejangizni qanday o'zgartiradi? 2–3 jumla.</li></ul>",
             ph="Elchixona: ... o'rin; universitet: ... Xulosa: ..."),
    ],
    tool=dict(id="tanlov", short="Tanlov", h2="Universitet tanlovi matritsasi", sub="Uchta yakuniy tanlovingizni turi va dalili bilan yozing. Elchixona trekida kamida bittasi B turidan bo'lishi tekshiriladi.",
              h3="3 ta tanlov", tag="yo'l + 3 universitet", ic="telescope", btn="Tanlovni saqlash", badge="Strateg", min=5,
              fields=[dict(k="yol", label="Ariza yo'li", type="select", opts=["Elchixona treki", "Universitet treki"]),
                      dict(k="u1", label="1-tanlov", hint="universitet · dastur · dalil · havola", type="area", ph="Universitet, dastur, moslik dalili, havola"),
                      dict(k="u1t", label="1-tanlov turi", type="select", opts=["A", "B"]),
                      dict(k="u2", label="2-tanlov", type="area", ph="Universitet treki bo'lsa, bo'sh qoldiring"),
                      dict(k="u2t", label="2-tanlov turi", type="select", opts=["A", "B"]),
                      dict(k="u3", label="3-tanlov", type="area", ph=""),
                      dict(k="u3t", label="3-tanlov turi", type="select", opts=["A", "B"]),
                      dict(k="xavf", label="Xavf izohi", hint="kvota va taqsimot", type="area", ph="Qaysi tanlov eng ishonchli va nega ...")]),
    check=dict(h2="Tanlov nazorati", sub="Ro'yxatni yakunlashdan oldin.", h3="8 bandlik nazorat",
               items=["Universitet turi (A/B) joriy yil ilovasidan tekshirilgan.", "Elchixona trekida kamida bitta B turi bor.",
                      "Bitta universitetning ikki bo'limi tanlanmagan.", "Har tanlov uchun dastur o'qitish tili va mening sertifikatim mos.",
                      "Har tanlov uchun tekshiriladigan moslik dalili va havola bor.", "Kvota yo'riqnomadan olingan, taxmin qilinmagan.",
                      "Forum va reyting ro'yxatlariga emas, rasmiy sahifalarga tayanilgan.", "Tanlovlar xavf bo'yicha taqsimlangan."]),
    art_title="Universitet tanlovi va moslik dalilnomasi", art_short="Tanlov",
    art=[("Ariza yo'li", ["yol", "a1"]), ("1-tanlov", ["u1t", "u1"]), ("2-tanlov", ["u2t", "u2"]), ("3-tanlov", ["u3t", "u3"]),
         ("Saralangan ro'yxat va ballar", ["a2", "a3", "a4"]), ("Kvota va xavf izohi", ["xavf", "a5"])],
    tip="Har universitet uchun o'zingizdan so'rang: agar komissiya \"nega biz?\" desa, men ularning saytidan qaysi aniq faktni keltira olaman? Javob bo'lmasa, tanlov hali tayyor emas.",
    sources=STD,
    js="""window.KGTool = { check: function () {
  var n = window.KG && KG.S.notes;
  if (!n || n.yol !== "Elchixona treki") return "";
  var t = [n.u1t, n.u2t, n.u3t].filter(Boolean);
  if (t.length && t.indexOf("B") < 0) return "Elchixona trekida kamida bitta B turdagi universitet boʻlishi shart";
  return "";
} };""",
)
