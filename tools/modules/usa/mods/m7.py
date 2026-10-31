from common import EDUSA_GR, PRINCETON_MS, BUFFALO, DUKE, BU, NSF_GRFP, CGS, HOL, STD

MOD = dict(
    title="Magistratura va PhD moliyasi",
    desc="USA Lab M7: AQShda magistratura va PhD moliyalashtirishi farqi, PhD moliya paketi (stipendiya, o'qish to'lovidan ozod qilish, sug'urta, TA va RA), kafedra sahifasini o'qish, xalqaro talabaga yopiq tashqi grantlar, takliflarni solishtirish va 15-aprel qarori. Natija: moliya paketi taqqoslagichi.",
    lead="AQShda PhD ko'pincha ish kabi moliyalashtiriladi: kafedra o'qish to'lovini qoplaydi va oylik beradi. Magistratura esa ko'pincha o'z hisobidan. Bu modulda shu farqni hisobga olib dasturlarni tanlaysiz va takliflarni raqam bilan solishtirasiz.",
    hero="phd", weeks="2", next="M8 Viza, maqom va ishlash huquqi", next_href="usa-lab-o.html?m=8",
    goals=[("chart", "Moliya paketi taqqoslagichi", "2 taklif: oylik sof qoldiq"),
           ("memo", "Kafedra moliyasi jadvali", "har kafedra: yillar, summa, majburiyat, muddat"),
           ("shield", "Grant muvofiqlik filtri", "xalqaro talabaga yopiq grantlarni chiqarish")],
    warn=f"Ilmiy rahbar tanlash, professorga xat, ilmiy loyiha taklifi va maqsad bayonnomasi PhD Lab M2–M5 va Master Lab M4–M6 da. Bu modul faqat AQSh moliyalashtirish mexanizmi. Summalar {HOL}; kafedra sahifasidan qayta tekshiring.",
    lessons=[
        dict(t="Magistratura va PhD: pul qayerdan", short="Farq", min=25, kind="⚖️ Farq", ic="phd",
             hook="Bir xil universitetning bir xil kafedrasida PhD talabasi oylik oladi, magistratura talabasi esa o'qish to'lovini o'zi to'laydi. Bu farqni bilmay magistraturaga ariza bersangiz, qabul xati bilan birga katta hisob ham keladi.",
             body=f"""<div class="tbl"><table><thead><tr><th></th><th>Magistratura</th><th>PhD</th></tr></thead><tbody>
<tr><td>Odatiy moliya</td><td>Ko'pincha o'z hisobidan</td><td>Ko'pincha kafedra paketi</td></tr>
<tr><td>Rasmiy misol</td><td>Buffalo universiteti: magistratura dasturlari asosan o'z hisobidan, assistentlik cheklangan. Princeton Graduate School magistratura talabalarini markazdan moliyalashtirmaydi, lekin ba'zi kafedralar qisman yoki to'liq moliyalashtiradi</td><td>EducationUSA: o'qituvchi yoki tadqiqot assistentligi, o'qish to'lovidan ozod qilish va stipendiya bilan, PhD darajasida juda keng tarqalgan</td></tr>
<tr><td>Kimga mos</td><td>Oila to'lay oladigan yoki tashqi stipendiyasi bor (masalan, Fulbright, M6) talaba</td><td>Ilmiy tajribasi bor, 5 yillik tadqiqotga tayyor talaba</td></tr>
</tbody></table></div>
<h4>Xulosa: yo'lni pulga qarab tanlash</h4>
<ul><li>Moliyasiz magistratura + oila to'lay olmaydi = real emas. Muqobil: Fulbright (M6), moliyalashtiradigan magistratura kafedralari yoki to'g'ridan-to'g'ri PhD.</li><li>AQSh PhD ga ko'pincha bakalavrdan keyin ham kirish mumkin (M1); kafedra qoidasini tekshiring.</li></ul>
<div class="srcs">Manba: {BUFFALO}; {PRINCETON_MS}; {EDUSA_GR}. {HOL}.</div>""",
             take="Magistratura ko'pincha o'z hisobidan, PhD ko'pincha kafedra paketi bilan. Pulga qarab yo'l tanlang: tashqi stipendiya, moliyalashtiradigan kafedra yoki to'g'ridan-to'g'ri PhD.",
             quiz=[("AQShda magistratura har doim kafedra tomonidan moliyalashtiriladi.", "n", "Noto'g'ri: ko'p dasturlar asosan o'z hisobidan."),
                   ("Assistentlik PhD darajasida keng tarqalgan.", "t", "To'g'ri: EducationUSA."),
                   ("Ba'zi kafedralar magistratura talabalarini ham moliyalashtiradi.", "t", "To'g'ri: Princeton misoli."),
                   ("Magistraturaga moliyasiz qabul qilinsa, oila to'lay olmasa ham bu real yo'l.", "n", "Noto'g'ri: I-20 uchun pul dalili kerak (M2).")],
             task="<ul><li>Sizning maqsadingiz: magistratura yoki PhD? Moliya bo'yicha ikki dalil bilan yozing.</li></ul>",
             ph="Maqsad: ... Chunki 1) oila ... 2) ilmiy tajribam ..."),
        dict(t="PhD moliya paketi", short="Paket", min=30, kind="🧮 Paket", ic="money",
             hook="\"To'liq moliyalashtirilgan\" degan so'z kafedradan kafedraga turlicha ma'no beradi: necha yil, yozda pul bormi, sug'urta kimdan, qancha soat dars berasiz.",
             body=f"""<h4>Paket qismlari</h4>
<div class="tbl"><table><thead><tr><th>Qism</th><th>Savol</th></tr></thead><tbody>
<tr><td>Stipendiya ([[stipend]])</td><td>Oyiga yoki yiliga qancha; 9 oylikmi yoki 12 oylik?</td></tr>
<tr><td>O'qish to'lovidan ozod qilish ([[tuition remission]])</td><td>To'liqmi; yig'imlar ([[fees]]) ham kiradimi?</td></tr>
<tr><td>Tibbiy sug'urta</td><td>Kim to'laydi; oila a'zolari uchun?</td></tr>
<tr><td>Kafolatlangan yillar</td><td>Necha yil; undan keyin nima?</td></tr>
<tr><td>Majburiyat</td><td>O'qituvchi assistent (TA) yoki tadqiqot assistenti (RA); haftasiga necha soat?</td></tr>
</tbody></table></div>
<h4>Ikki rasmiy misol</h4>
<ul><li><b>Duke Graduate School:</b> birinchi 5 yil stipendiya, o'qish to'lovi va majburiy yig'imlar kafolatlangan; stipendiya 12 oylik; birinchi 6 yil sog'liq va stomatologiya sug'urtasi badali qoplanadi; oila a'zolari sug'urtasi talabaning o'zi hisobidan. Sahifada bu \"umuman olganda\" ekani va kafedralar farq qilishi yozilgan.</li><li><b>Boston universiteti, Earth &amp; Environment:</b> yaxshi akademik holatdagi talabaga 5 yilgacha stipendiya va sug'urta; aralash: dars berish (TA), loyihada ishlash (RA) va birinchi yilda majburiyatsiz [[fellowship]]; to'liq o'qish to'lovi va yig'imlar qoplanadi.</li></ul>
<div class="box info">Har ikki sahifada stipendiya summasi alohida jadvalda. Summani har doim manba yili bilan yozing.</div>
<div class="srcs">Manba: {DUKE}; {BU}. {HOL}.</div>""",
             take="PhD paketi: stipendiya, o'qish va yig'imlardan ozod qilish, sug'urta, kafolatlangan yillar, TA yoki RA majburiyati. Har qismni kafedra sahifasidan alohida tekshiring.",
             task="<ul><li>Bitta PhD dasturining paketini 5 qism bo'yicha yozing (manba va yil bilan).</li></ul>",
             ph="... universiteti, ... kafedrasi: stipendiya ... USD (12 oy, 2026–27), o'qish: to'liq, sug'urta: ..., yillar: 5, majburiyat: TA ... soat"),
        dict(t="Kafedra sahifasini o'qish", short="Kafedra", min=30, kind="🔎 Tekshiruv", ic="telescope",
             hook="Kafedra sahifasida qabul uchun eng muhim ma'lumotlar ko'pincha [[FAQ]] yoki [[handbook]] ichida yashiringan. 15 daqiqalik tekshiruv ariza to'lovini behuda to'lashdan saqlaydi.",
             body=f"""<h4>10 savollik tekshiruv</h4>
<ol><li>PhD qabul qilinganlarning hammasi moliyalashtiriladimi?</li><li>Necha yil kafolatlanadi?</li><li>Stipendiya summasi va davri (9 yoki 12 oy)?</li><li>Xalqaro talabaga bir xil paketmi?</li><li>GRE talab qilinadimi, ixtiyoriymi yoki qabul qilinmaydimi?</li><li>Ingliz tili testi va minimal ball?</li><li>Ariza to'lovi va undan ozod qilish tartibi?</li><li>Muddat (kafedra muddati universitet muddatidan oldin bo'lishi mumkin)?</li><li>Professor bilan oldindan bog'lanish tavsiya qilinadimi?</li><li>Ichki [[fellowship]] uchun alohida ariza kerakmi?</li></ol>
<h4>Vaqt va professorlar</h4>
<p>EducationUSA: stipendiya va grant muddatlari dastur boshlanishidan 18 oy oldin bo'lishi mumkin; professorlar ko'pincha grant va moliyalashtirish oluvchilarni tanlashda qatnashadi, shuning uchun kafedra professorlari bilan bog'lanish foydali. Professorga xat yozish usuli PhD Lab M3 da.</p>
<div class="box warn">Bu 10 savoldan birortasiga sahifada javob bo'lmasa, kafedraning [[graduate coordinator]] manziliga qisqa, aniq savol yozing. Javobni saqlang.</div>
<div class="srcs">Manba: {EDUSA_GR}. {HOL}.</div>""",
             take="Har kafedrada 10 savolga javob toping: moliya kafolati, yillar, summa, xalqaro talaba, GRE, til, to'lov, muddat, professor, fellowship.",
             task="<ul><li>2 kafedra sahifasini 10 savol bo'yicha tekshiring va javobsiz qolgan savollarni yozing.</li></ul>",
             ph="... kafedrasi: 1) ha 2) 5 yil 3) ... 4) ... 5) GRE ixtiyoriy ... Javobsiz: ..."),
        dict(t="Tashqi grantlar: kimga ochiq", short="Grantlar", min=20, kind="✅ Filtr", ic="shield",
             hook="Internetdagi \"AQShdagi eng yaxshi PhD grantlari\" ro'yxatining katta qismi faqat AQSh fuqarolari uchun. Ularga vaqt sarflashdan oldin bitta qatorni tekshiring.",
             body=f"""<h4>Muvofiqlik qatori</h4>
<p>Har grant sahifasida [[eligibility]] bo'limini oching va fuqarolik talabini toping. Misol: NSF ning [[Graduate Research Fellowship Program]] (GRFP) talabi \"AQSh fuqarosi, fuqaroligi yoki doimiy rezidenti\". Demak O'zbekiston fuqarosi uchun yopiq.</p>
<div class="tbl"><table><thead><tr><th>Grant manbasi</th><th>Xalqaro talabaga</th></tr></thead><tbody>
<tr><td>AQSh federal agentliklari (NSF GRFP kabi)</td><td>Ko'pincha yopiq; har birining sahifasini tekshiring</td></tr>
<tr><td>Kafedra va universitet [[fellowship]]lari</td><td>Ko'pincha qabul paketi ichida (7.2)</td></tr>
<tr><td>O'z mamlakati moliyalashtirishi</td><td>Boston universiteti xalqaro talabalar o'z mamlakatidan moliya olishi mumkinligini yozadi</td></tr>
<tr><td>Fulbright</td><td>O'zbekiston uchun magistratura (M6)</td></tr>
</tbody></table></div>
<div class="box info">Grant sahifasida \"[[U.S. citizen]]\", \"[[permanent resident]]\" yoki \"[[eligible noncitizen]]\" so'zlari bo'lsa, u sizga yopiq bo'lishi ehtimoli yuqori. Bunday grantni ro'yxatdan chiqaring.</div>
<div class="srcs">Manba: {NSF_GRFP}; {BU}. {HOL}.</div>""",
             take="Har grantni fuqarolik qatori bilan filtrlang. NSF GRFP kabi federal grantlar ko'pincha faqat AQSh fuqarolari va rezidentlari uchun.",
             task="<ul><li>Topgan 3 grantingizni fuqarolik qatori bo'yicha tekshiring: ochiq / yopiq, dalil bilan.</li></ul>",
             ph="... — yopiq: \"U.S. citizen...\"; ... — ochiq: ...; ..."),
        dict(t="Takliflarni solishtirish va 15-aprel", short="Taklif", min=30, kind="📊 Taqqos", ic="chart",
             hook="Ikki moliyalashtirilgan PhD taklifi bir xil ko'rinadi, lekin biri qimmat shaharda, boshqasi yozda pul bermaydi. Raqam bilan solishtirmasangiz, oylik kamomadni birinchi qishda bilasiz.",
             body=f"""<h4>Solishtirish formulasi</h4>
<p>Oylik sof qoldiq = (yillik stipendiya − qoplanmagan yig'imlar va sug'urta) ÷ 12 − oylik ijara va yashash xarajati.</p>
<ul><li>Stipendiya 9 oylik bo'lsa, yozgi oylar uchun manba bormi?</li><li>Kafolatlangan yillar soni bir xilmi?</li><li>TA soatlari tadqiqot vaqtini qanchalik kamaytiradi?</li></ul>
<h4>15-aprel qarori (CGS)</h4>
<p>Council of Graduate Schools ning [[April 15 Resolution]] hujjatiga ko'ra, kuzgi semestrga qabul qilingan talaba moliyaviy yordam takliflarini (to'liq o'qish to'lovi, [[fellowship]], [[traineeship]], assistentlik) 15-aprelgacha qabul qilish yoki rad etishga majbur emas; undan oldingi muddat qarorga zid. Qaror qabul taklifiga emas, faqat moliya takliflariga tegishli va uni imzolagan universitetlar uchun amal qiladi. 2027-yil kuzidan boshlanadigan dasturlar uchun universitetlar qarorni qayta imzolashi kerak.</p>
<div class="box warn">Universitet qarorni imzolaganmi, tekshiring. 15-aprelgacha taklifni qabul qilib, keyin boshqasini tanlasangiz, voz kechishni yozma bildiring.</div>
<div class="srcs">Manba: {CGS}; {DUKE}; {BU}. {HOL}.</div>""",
             take="Takliflarni oylik sof qoldiq, yozgi moliya, kafolat yillari va majburiyat bo'yicha solishtiring. CGS 15-aprel qarorini imzolagan universitetlarda moliya taklifiga 15-aprelgacha javob berish majburiy emas.",
             task="<ul><li>2 taklif (yoki 2 kafedra sahifasi) uchun oylik sof qoldiqni hisoblang.</li><li>Universitetlar CGS qarorini imzolaganini tekshiring.</li></ul>",
             ph="A: stipendiya ... − ... = ...; ijara ... → oylik qoldiq ...; B: ...; CGS: A imzolagan / ..."),
    ],
    tool=dict(id="taqqos", short="Taqqos", h2="Moliya paketi taqqoslagichi", sub="Ikki taklifni oylik sof qoldiq bo'yicha solishtiring (AQSh dollarida).",
              h3="Taqqoslagich", tag="5 maydon", ic="chart", btn="Taqqoslashni saqlash", badge="Paket tahlilchisi", min=4,
              pre="""<div class="fld"><label>Hisoblagich <small>yillik summalar, ijara oylik</small></label>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px">
<input id="aS" type="number" min="0" placeholder="A: yillik stipendiya" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px">
<input id="aF" type="number" min="0" placeholder="A: qoplanmagan yig'im + sug'urta" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px">
<input id="aR" type="number" min="0" placeholder="A: oylik ijara va yashash" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px">
<input id="bS" type="number" min="0" placeholder="B: yillik stipendiya" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px">
<input id="bF" type="number" min="0" placeholder="B: qoplanmagan yig'im + sug'urta" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px">
<input id="bR" type="number" min="0" placeholder="B: oylik ijara va yashash" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px">
</div><div id="tOut" class="out" style="white-space:normal">Raqamlarni kiriting.</div></div>""",
              fields=[dict(k="a", label="A taklif", hint="universitet, kafedra, yillar, majburiyat", type="area", ph="... — 5 yil, TA 20 soat, 12 oylik stipendiya"),
                      dict(k="b", label="B taklif", type="area", ph="..."),
                      dict(k="yoz", label="Yozgi moliya va kafolatdan keyingi yillar", type="area", ph="A: ...; B: ..."),
                      dict(k="cgs", label="15-aprel qarori va javob muddati", ph="A: imzolagan, muddat ...; B: ..."),
                      dict(k="qaror", label="Qaror", type="select", opts=["A", "B", "Qo'shimcha ma'lumot so'rayman", "Ikkalasi ham mos emas"])]),
    check=dict(h2="M7 nazorati", sub="Taqqoslashni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Magistratura va PhD moliyasi farqi hisobga olingan.", "Har paketning 5 qismi manba bilan yozilgan.",
                      "Stipendiya 9 yoki 12 oylik ekani aniqlangan.", "Xalqaro talabaga bir xil paket ekani tekshirilgan.",
                      "Tashqi grantlar fuqarolik qatori bilan filtrlangan.", "Oylik sof qoldiq ikkala taklif uchun hisoblangan.",
                      "15-aprel qarori va javob muddati tekshirilgan.", "Javobsiz savollar kafedraga yozma yuborilgan."]),
    art_title="Moliya paketi taqqoslagichi", art_short="Taqqos",
    art=[("Yo'l tanlovi", ["a1"]), ("PhD paketi", ["a2"]), ("Kafedra tekshiruvi", ["a3"]), ("Grant filtri", ["a4"]),
         ("A taklif", ["a"]), ("B taklif", ["b"]), ("Hisob", ["tcalc", "a5"]), ("Yozgi moliya", ["yoz"]), ("15-aprel", ["cgs"]), ("Qaror", ["qaror"])],
    tip="PhD taklifini maosh kabi solishtiring: summa, yillar, majburiyat va shahar narxi. \"To'liq moliyalashtirilgan\" degan so'z hisob o'rnini bosmaydi.",
    sources=f"{BUFFALO}; {PRINCETON_MS}; {EDUSA_GR}; {DUKE}; {BU}; {NSF_GRFP}; {CGS}. {STD}",
    js="""window.KGTool = { init: function () {
  var ids = ["aS", "aF", "aR", "bS", "bF", "bR"], o = document.getElementById("tOut");
  function v(id) { var x = parseFloat(document.getElementById(id).value); return isNaN(x) ? 0 : x; }
  function fmt(n) { return Math.round(n).toLocaleString("ru-RU"); }
  function run() {
    if (!v("aS") && !v("bS")) { o.textContent = "Raqamlarni kiriting."; return; }
    var a = (v("aS") - v("aF")) / 12 - v("aR"), b = (v("bS") - v("bF")) / 12 - v("bR");
    var best = a === b ? "teng" : (a > b ? "A" : "B");
    var txt = "Oylik sof qoldiq: A " + fmt(a) + " USD, B " + fmt(b) + " USD. Pul boʻyicha ustun: " + best + ".";
    var cls = Math.min(a, b) < 0 ? "no" : "ok";
    o.innerHTML = "<span class=\\"pill " + cls + "\\">" + (Math.min(a, b) < 0 ? "Kamomad bor" : "Qoldiq musbat") + "</span> " + KG.esc(txt);
    KG.S.notes.tcalc = txt; KG.S.notes.t_in = ids.map(v).join("|"); KG.save();
  }
  if (KG.S.notes.t_in) { var p = String(KG.S.notes.t_in).split("|"); ids.forEach(function (id, i) { if (p[i] && p[i] !== "0") document.getElementById(id).value = p[i]; }); }
  ids.forEach(function (id) { document.getElementById(id).addEventListener("input", run); });
  run();
} };""",
)
