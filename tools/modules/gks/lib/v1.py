from common import U27, G26, SIK, APO, TOPIK, STD

MOD = dict(
    title="Hujjatlar infratuzilmasi",
    desc="GKS Lab M1: GKS hujjatlari xaritasi, apostil va tarjima, GPA talabi va konvertatsiya, TOPIK va ingliz tili strategiyasi. Natija: hujjatlar nazorat jadvali.",
    lead="GKS arizasi bitta insho emas, o'nlab varaqdan iborat to'plam. Bu modulda yo'riqnomadagi har hujjatni bitta jadvalga tushirasiz, legallashtirish zanjirini rejalaysiz, bahoingiz talabga mosligini tekshirasiz va til strategiyasini tanlaysiz.",
    hero="scroll", weeks="2–3", next="Universitet va dastur tanlash",
    goals=[("scroll", "Hujjatlar nazorat jadvali", "har hujjat, manbasi, holati va muddati bilan"),
           ("shield", "Legallashtirish yo'l xaritasi", "apostil, tarjima va nusxa qoidasi bo'yicha"),
           ("chart", "Baho va til rejasi", "GPA talabiga moslik izohi va TOPIK/ingliz tili qarori")],
    warn="Hujjatlar ro'yxati, formalar raqami va muddatlar har yili yangi yo'riqnomada e'lon qilinadi. Bu moduldagi faktlar 2027 GKS-U (sentabr 2026) va 2026 GKS-G (fevral 2026) yo'riqnomalaridan, 31.10.2026 holatiga. Topshirishdan oldin o'z siklingiz yo'riqnomasini o'qing.",
    lessons=[
        dict(t="GKS hujjatlari xaritasi", short="Xarita", min=35, kind="🎯 Mini-test", ic="scroll",
             hook="Bitta yetishmagan varaq yoki noto'g'ri formatdagi nusxa arizani mazmuni o'qilmasdan to'xtatishi mumkin. Shuning uchun birinchi ish insho emas, hujjatlar xaritasi.",
             body=f"""<p>GKS yo'riqnomasi hujjatlarni ikki guruhga ajratadi: <b>siz to'ldiradigan formalar</b> (ariza, shaxsiy bayonot, o'quv rejasi, tavsiya xati, kelishuv, tibbiy anketa, ma'lumotlarga rozilik) va <b>rasmiy guvohnomalar</b> (fuqarolik, diplom yoki attestat, transkript). Formalar apostilsiz topshiriladi; guvohnomalar esa apostil yoki konsullik tasdig'i bilan.</p>
<h4><span class="trk">U</span> 2027 GKS-U ro'yxati</h4>
<div class="tbl"><table><thead><tr><th>№</th><th>Hujjat</th><th>Izoh</th></tr></thead><tbody>
<tr><td>1–7</td><td>Formalar: ariza (faqat ingliz tilida), shaxsiy bayonot, o'quv rejasi, tavsiya xati, GKS kelishuvi, tibbiy anketa, ma'lumotlarga rozilik</td><td>Yo'riqnoma ilovasidagi shablon</td></tr>
<tr><td>8</td><td>Fuqarolik va oilaviy aloqa dalili (nomzod va ota-ona)</td><td>Apostil yoki konsullik tasdig'i</td></tr>
<tr><td>9–10</td><td>Maktab (litsey, kollej) bitiruv guvohnomasi va baholar varaqasi</td><td>Bitirmagan bo'lsa, kutilayotgan bitiruv haqida ma'lumotnoma</td></tr>
<tr><td>11–15</td><td>Kichik daraja hujjatlari, chet eldagi koreys maqomi va boshqalar</td><td>Faqat tegishli bo'lsa</td></tr>
<tr><td>16</td><td>TOPIK (asl nusxa) yoki ingliz tili sertifikati (nusxa)</td><td>Bo'lsa</td></tr>
<tr><td>17</td><td>Mukofot va sertifikatlar</td><td>Ixtiyoriy, beshtagacha</td></tr>
<tr><td>18</td><td>Pasport</td><td>Nusxa</td></tr>
</tbody></table></div>
<h4><span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G ro'yxati</h4>
<p>Magistratura va doktorantura uchun 1–10-formalar hamma nomzodga majburiy: ariza, shaxsiy bayonot, o'quv rejasi, bitta tavsiya xati, GKS kelishuvi, tibbiy anketa, ma'lumotlarga rozilik va boshqalar. Ularga fuqarolik, oilaviy aloqa, bakalavr (D uchun magistr ham) diplomi va transkripti qo'shiladi. Aniq raqamlash va tartib har yili o'zgarishi mumkin, shuning uchun jadvalni yo'riqnomaning o'zidan ko'chiring.</p>
<div class="box info"><b>Bitta haqiqat manbai.</b> Hujjatlar ro'yxatini xotirada emas, jadvalda yuriting: hujjat nomi, kim beradi, holati, muddat, nechta nusxa. Jadval yo'riqnomadagi ro'yxat bilan bandma-band mos kelishi kerak.</div>
<div class="srcs">Manba: {U27}; {G26}. 31.10.2026 holatiga.</div>""",
             take="GKS to'plami ikki qismdan iborat: o'zingiz to'ldiradigan formalar (apostilsiz) va rasmiy guvohnomalar (apostil bilan). Ro'yxatni yo'riqnomadan bandma-band jadvalga ko'chiring.",
             quiz=[("GKS formalari (ariza, shaxsiy bayonot, o'quv rejasi) ham apostil qilinadi.", "n", "Noto'g'ri: yo'riqnomaga ko'ra to'ldiriladigan formalar apostil talab qilmaydi; rasmiy guvohnomalar talab qiladi."),
                   ("2027 GKS-U da ariza formasi faqat ingliz tilida to'ldiriladi.", "t", "To'g'ri: 1-forma inglizcha bo'lishi kerak."),
                   ("Mukofot va sertifikatlardan xohlagancha qo'shish mumkin.", "n", "Noto'g'ri: 2027 GKS-U da ixtiyoriy, beshtagacha."),
                   ("Hujjatlar ro'yxati har yili bir xil bo'ladi, eski yo'riqnoma yetarli.", "n", "Noto'g'ri: ro'yxat va raqamlash har sikl yangi yo'riqnomadan olinadi.")],
             task="<ul><li>O'z treking (U, M yoki D) yo'riqnomasidagi hujjatlar ro'yxatini to'liq ko'chiring.</li><li>Har hujjat yoniga: kim beradi, hozir bormi, qachongacha tayyor bo'ladi.</li></ul>",
             ph="1) Ariza formasi: o'zim, ... 2) Attestat: maktab, ..."),
        dict(t="Apostil, tarjima va nusxa qoidalari", short="Apostil", min=35, kind="🛠 Yo'l xaritasi", ic="shield",
             hook="Notarial tasdiqlangan oddiy nusxa yetarli deb o'ylash eng qimmat xatolardan biri. GKS yo'riqnomasi oddiy va notarial nusxani qabul qilmaydi.",
             body=f"""<h4>Yo'riqnoma nima deydi</h4>
<ul><li>Rasmiy guvohnomalar <b>apostil</b> yoki Koreya elchixonasining <b>konsullik tasdig'i</b> bilan topshiriladi. O'zbekiston Apostil konvensiyasi a'zosi, shuning uchun odatda apostil ishlatiladi.</li>
<li>Apostil qo'yilgan hujjatning oddiy nusxasi yoki notarial nusxasi <b>qabul qilinmaydi</b>.</li>
<li>Ingliz yoki koreys tilida bo'lmagan hujjatga <b>tasdiqlangan tarjima</b> qo'shiladi va asl yoki tarjimaga apostil (konsullik tasdig'i) qo'yiladi.</li>
<li><span class="trk">U</span> Maktab hujjatlari uchun apostil mavjud bo'lsa ham konsullik tasdig'i ishlatilishi mumkin.</li>
<li><span class="trk">M</span> <span class="trk">D</span> Hujjatga apostil qo'yib bo'lmasa, yo'riqnoma tasdiqlangan haqiqiy nusxa variantini ko'rsatadi; buni oldindan elchixona yoki universitet bilan aniqlang.</li></ul>
<h4>O'zbekistonda apostil</h4>
<p>Apostil uchun ariza my.gov.uz orqali elektron yoki Davlat xizmatlari markazida beriladi. Gov.uz ma'lumotiga ko'ra so'rov ikki ish kuni ichida ko'rib chiqiladi; ta'lim muassasalari bergan hujjatlar uchun yig'im bazaviy hisoblash miqdorining 20 foizi. Rad etilsa, xatoni tuzatib 30 kun ichida qayta topshirish mumkin.</p>
<h4>Ketma-ketlik</h4>
<div class="tbl"><table><thead><tr><th>Qadam</th><th>Nima qilinadi</th><th>Xavf</th></tr></thead><tbody>
<tr><td>1. Asl hujjat</td><td>Diplom, attestat, transkriptdagi ism pasport bilan harfma-harf mosligini tekshiring</td><td>Ism transliteratsiyasi farqi</td></tr>
<tr><td>2. Tarjima</td><td>Ingliz tiliga tasdiqlangan tarjima: fan nomlari, baho shkalasi, daraja nomi</td><td>Fan va daraja nomi noto'g'ri</td></tr>
<tr><td>3. Apostil</td><td>my.gov.uz yoki DXM orqali</td><td>Kech boshlash</td></tr>
<tr><td>4. Nusxa</td><td>Nechta asl va nusxa kerakligini yo'riqnomadan aniqlang</td><td>Asl o'rniga nusxa yuborish</td></tr>
</tbody></table></div>
<div class="box warn"><b>Vaqtni teskari hisoblang.</b> Apostilning o'zi tez, lekin undan oldingi qadamlar (universitetdan transkript olish, tarjima, xatoni tuzatish) haftalab cho'ziladi. Ariza oynasidan kamida 2 oy oldin boshlang.</div>
<div class="srcs">Manba: {U27}; {G26}; {APO} (31.10.2026 da tekshirildi). Yig'im miqdori va muddat o'zgarishi mumkin.</div>""",
             take="Guvohnomalar apostil yoki konsullik tasdig'i bilan; oddiy va notarial nusxa o'tmaydi. Tarjimani o'zingiz tekshiring va legallashtirishni ariza oynasidan kamida 2 oy oldin boshlang.",
             task="<ul><li>Har rasmiy hujjat uchun zanjir yozing: asl → tarjima → apostil → nusxa soni.</li><li>Har qadamga sana qo'ying va ism transliteratsiyasi pasport bilan mosligini tekshiring.</li></ul>",
             ph="Attestat: asl bor → tarjima 10-noyabrgacha → apostil 20-noyabrgacha → 1 asl ..."),
        dict(t="Baholar: GPA talabi va konvertatsiya", short="GPA", min=30, kind="🛠 GPA tekshiruvi", ic="chart",
             hook="Komissiya O'zbekiston baholash tizimini bilmaydi. Shkalasi ko'rsatilmagan \"4.6\" raqami eng kuchli dalilingizni noaniq qilib qo'yadi.",
             body=f"""<h4>Talab: uchtadan biri</h4>
<p>2027 GKS-U va 2026 GKS-G yo'riqnomalarida baho talabi bir xil, siz quyidagilardan <b>bittasiga</b> javob berishingiz kerak:</p>
<ol><li>100 ballik shkalada 80 va undan yuqori;</li>
<li>sinf (kurs) bo'yicha yuqori 20 foiz ichida;</li>
<li>CGPA kamida 2.64/4.0, 2.80/4.3, 2.91/4.5 yoki 3.23/5.0.</li></ol>
<p>Boshqa tizimdagi baho uchun rasmiy baholash tizimi izohi va ta'lim muassasasi tasdiqlagan konvertatsiya qilingan baho talab qilinadi. <span class="trk">U</span> 2027 GKS-U da konvertatsiya jadvali A ilovasida.</p>
<h4>O'zbekiston uchun amaliy qoidalar</h4>
<ul><li><b>Asl shkalada yozing</b>: \"4.6 / 5.0\" yoki \"86 / 100\". O'zingiz boshqa shkalaga aylantirmang; konvertatsiyani muassasa tasdiqlaydi.</li>
<li><b>5 ballik maktab tizimi</b>: 3.23/5.0 chegarasi o'rtacha bahoga nisbatan. Barcha fanlar bo'yicha o'rtachani transkriptdan aniq hisoblang.</li>
<li><b>Yuqori 20 foiz</b> yo'li faqat maktab yoki universitet rasmiy ma'lumotnoma bera olsa ishlaydi.</li>
<li><span class="trk">M</span> <span class="trk">D</span> Magistratura uchun bakalavr bahosi, doktorantura uchun yo'riqnomadagi talab bo'yicha oldingi darajalar baholari ko'riladi.</li></ul>
<div class="box warn">Bu talab <b>minimal</b>. Chegarada bo'lish o'tishni bildiradi, ustunlikni emas. Baho past bo'lsa, buni boshqa hujjatlarda yashirmang: M3 da zaif tomonni tushuntirishni o'rganasiz.</div>
<div class="srcs">Manba: {U27}; {G26}. 31.10.2026 holatiga.</div>""",
             take="Talab: 80/100, yuqori 20 foiz yoki 2.64/4.0 (3.23/5.0) dan bittasi. Bahoni asl shkalada yozing; konvertatsiyani muassasa tasdiqlaydi.",
             task="<ul><li>Pastdagi vositada bahoingizni tekshiring.</li><li>Qaysi yo'l bilan talabga javob berasiz (80/100, 20 foiz, CGPA) va buni qaysi hujjat tasdiqlaydi? Yozing.</li></ul>",
             ph="Mening bahoim: ... / ... ; yo'l: ... ; tasdiqlovchi hujjat: ..."),
        dict(t="Til strategiyasi: TOPIK va ingliz tili", short="Til", min=30, kind="🗺 Til rejasi", ic="books",
             hook="Koreys tilini bilmaslik GKS ga to'siq emas: stipendiya bir yillik til kursini o'z ichiga oladi. Lekin TOPIK ballga va o'qish rejasiga bevosita ta'sir qiladi.",
             body=f"""<h4>TOPIK nima beradi</h4>
<ul><li><span class="trk">U</span> 2027 GKS-U: TOPIK 3-daraja umumiy ballga 3 foiz, 4-daraja 4 foiz, 5 va undan yuqori 5 foiz qo'shimcha ball beradi.</li>
<li><span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G: TOPIK 3 va undan yuqori qo'shimcha ball beradi; foiz va jadvalni o'z siklingiz yo'riqnomasidan o'qing (2026 matnida izoh va jadval bir-biriga to'liq mos emas).</li>
<li>TOPIK 5 yoki 6 bo'lsa, til kursidan ozod bo'lib, darhol daraja dasturiga kirasiz. Til kursining birinchi 6 oyida 5–6 darajani olsa, qolgan 6 oydan ozod qilinadi.</li></ul>
<h4>Ingliz tili</h4>
<p>Ko'p magistratura va doktorantura dasturlari, ayniqsa STEM da, ingliz tilida o'qitiladi. U holda IELTS yoki TOEFL dastur talabi bo'lishi mumkin. Yo'riqnoma ingliz tili sertifikatini nusxa sifatida qabul qiladi; TOPIK esa asl nusxada.</p>
<h4>Qaror jadvali</h4>
<div class="tbl"><table><thead><tr><th>Holat</th><th>Mantiqiy yo'l</th></tr></thead><tbody>
<tr><td>Ariza oynasigacha 6+ oy, koreys tiliga vaqt bor</td><td>TOPIK 3 ni nishon qiling: ball va til yili osonlashadi</td></tr>
<tr><td>STEM, ingliz tilidagi dastur, ingliz tili kuchli</td><td>IELTS/TOEFL ni mustahkamlang; koreys tilini til yilida</td></tr>
<tr><td>Ikkalasi ham yo'q, vaqt kam</td><td>Bitta tilni tanlang; ikkala tilga yarimta kuch bermang</td></tr>
</tbody></table></div>
<div class="box info">Sertifikatlarning amal qilish muddati bor. Ariza kunida sertifikat amalda bo'lishini tekshiring; TOPIK imtihon sanalari {TOPIK} da e'lon qilinadi.</div>
<div class="srcs">Manba: {U27}; {G26}. 31.10.2026 holatiga.</div>""",
             take="TOPIK ixtiyoriy, lekin ball va til yiliga ta'sir qiladi. Bitta tilni tanlab, unga sana qo'ying.",
             task="<ul><li>Joriy koreys va ingliz tili darajangizni yozing.</li><li>Maqsad sertifikat, imtihon sanasi va oylik rejani tuzing.</li></ul>",
             ph="Hozir: TOPIK yo'q, IELTS 6.0. Maqsad: ... Imtihon: ... Reja: ..."),
    ],
    tool=dict(id="jadval", short="Jadval", h2="Hujjatlar nazorat jadvali", sub="Darslardagi javoblaringizni bitta jadvalga yig'ing. Pastdagi GPA tekshiruvi hisobni o'zi qiladi.",
              h3="Nazorat jadvali va GPA", tag="4 maydon", ic="scroll", btn="Jadvalni saqlash", badge="Jadval ustasi", min=3,
              pre="""<div class="fld"><label>GPA tekshiruvi <small>bahoingiz va shkala</small></label><div style="display:flex;gap:10px;flex-wrap:wrap"><input id="gpaV" type="number" step="0.01" min="0" placeholder="Baho, masalan 4.3" style="flex:1 1 140px;min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"><select id="gpaS" style="flex:1 1 140px;min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"><option value="5">5 ballik</option><option value="4">4.0</option><option value="4.3">4.3</option><option value="4.5">4.5</option><option value="100">100 ballik</option></select></div><div id="gpaOut" class="out" style="white-space:normal">Bahoni kiriting.</div></div>""",
              fields=[dict(k="trek", label="Trekingiz", type="select", opts=["U: bakalavriat (GKS-U)", "M: magistratura (GKS-G)", "D: doktorantura (GKS-G)"]),
                      dict(k="docs", label="Hujjatlar ro'yxati", hint="hujjat · kim beradi · holat · muddat · nusxa", type="area", ph="Ariza formasi · o'zim · boshlanmagan · 1-dekabr · 1"),
                      dict(k="leg", label="Legallashtirish rejasi", type="area", ph="Attestat: tarjima → apostil (my.gov.uz) → ..."),
                      dict(k="lang", label="Til rejasi", type="area", ph="TOPIK 3: ... sana; IELTS: ...")]),
    check=dict(h2="Hujjatlar nazorati", sub="Topshirishdan oldin har bandni tekshiring.", h3="10 bandlik nazorat",
               items=["Ro'yxat joriy sikl yo'riqnomasidan ko'chirilgan, bandma-band mos.", "Har hujjatda ism pasport bilan harfma-harf mos.",
                      "Rasmiy guvohnomalarga apostil yoki konsullik tasdig'i rejalashtirilgan.", "Notarial yoki oddiy nusxaga tayanilmagan.",
                      "Tarjimadagi fan nomlari, baho shkalasi va daraja nomi tekshirilgan.", "Baho asl shkalada, talabga moslik yo'li aniq.",
                      "Til sertifikati ariza kunida amal qiladi (bo'lsa).", "Formalar (ariza, bayonot, reja) apostilsiz ekanligi tushunilgan.",
                      "Legallashtirish ariza oynasidan kamida 2 oy oldin boshlanadi.", "Har hujjat uchun mas'ul va sana yozilgan."]),
    art_title="Hujjatlar nazorat jadvali", art_short="Jadval",
    art=[("Trek", ["trek"]), ("Hujjatlar ro'yxati", ["docs", "a1"]), ("Legallashtirish yo'l xaritasi", ["leg", "a2"]),
         ("Baho va talabga moslik", ["gpa", "a3"]), ("Til rejasi", ["lang", "a4"])],
    tip="Hujjatni \"tayyor\" deb belgilashdan oldin uni yo'riqnomadagi qatorga qo'yib solishtiring: nom, til, asl yoki nusxa, apostil. Bitta farq ham qaytadan boshlashni anglatishi mumkin.",
    sources=STD,
    js="""window.KGTool = { init: function () {
  var v = document.getElementById("gpaV"), s = document.getElementById("gpaS"), o = document.getElementById("gpaOut");
  var MIN = { "4": 2.64, "4.3": 2.80, "4.5": 2.91, "5": 3.23, "100": 80 };
  function run() {
    var x = parseFloat(v.value), sc = s.value, m = MIN[sc];
    if (isNaN(x)) { o.textContent = "Bahoni kiriting."; return; }
    if (x > parseFloat(sc)) { o.textContent = "Baho shkaladan katta. Shkalani tekshiring."; return; }
    var ok = x >= m;
    var t = (ok ? "Talabga mos: " : "Talabdan past: ") + x + " / " + sc + " (minimal " + m + "). " + (ok ? "Bu minimal shart; ustunlik emas." : "Yuqori 20 foiz yoʻli bilan tekshiring yoki keyingi siklni koʻring.");
    o.innerHTML = "<span class=\\"pill " + (ok ? "ok" : "no") + "\\">" + (ok ? "Mos" : "Mos emas") + "</span> " + t;
    if (window.KG) { KG.S.notes.gpa = x + " / " + sc + ": " + (ok ? "talabga mos" : "talabdan past") + " (minimal " + m + ")"; KG.save(); }
  }
  v.addEventListener("input", run); s.addEventListener("change", run);
  if (window.KG && KG.S.notes.gpa) { var p = String(KG.S.notes.gpa).split(" / "); v.value = parseFloat(p[0]) || ""; s.value = (p[1] || "5").split(":")[0]; }
  run();
} };""",
)
