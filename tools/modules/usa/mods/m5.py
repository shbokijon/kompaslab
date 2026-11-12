from common import EMB_UGRAD, UGRAD_WL, EMB_EXCH, HARVARD_212E, HOL, STD

MOD = dict(
    title="Global UGRAD va almashinuv dasturlari",
    desc="USA Lab M5: Global UGRAD nima va nima emas, O'zbekiston uchun muvofiqlik shartlari, sikl holatini kuzatish, ariza va tanlov, elchixona ro'yxatidagi boshqa almashinuv dasturlari va J-1 majburiyati. Natija: almashinuv dasturi kartasi.",
    lead="Global UGRAD O'zbekistonda o'qiyotgan bakalavr talabasini AQSh universitetiga bir semestrga olib boradi. Bu daraja emas, lekin AQSh ta'limini ichidan ko'rish imkoniyati. Bu modulda dasturni, muvofiqlikni va sikl e'lon qilinganini qanday kuzatishni o'rganasiz.",
    hero="usa", weeks="1–2", next="M6 Fulbright magistraturasi", next_href="usa-lab-o.html?m=6",
    goals=[("usa", "Almashinuv dasturi kartasi", "muvofiqlik, hujjatlar, sikl holati"),
           ("bell", "Sikl kuzatuv rejasi", "rasmiy kanal, oy, eslatma"),
           ("compass", "B reja", "UGRAD bo'lmasa yoki rad javobi kelsa")],
    warn=f"{HOL}: AQSh elchixonasi sahifasidagi oxirgi Global UGRAD e'loni 2024–2025 sikli uchun (muddat 15.12.2024). Keyingi sikllar uchun O'zbekistonda e'lon topilmadi. Sikl rasman e'lon qilinmaguncha dasturga tayyorlanish xavfini hisobga oling. Insholarni yozish Bachelor Lab M9–M10 da o'rgatiladi; bu yerda takrorlanmaydi.",
    lessons=[
        dict(t="Global UGRAD nima", short="UGRAD", min=25, kind="🧭 Xarita", ic="usa",
             hook="\"AQShga grant bilan bakalavr\" degan e'lonlar ko'pincha Global UGRAD ni anglatadi. Lekin u daraja bermaydi va universitetni siz tanlamaysiz. Buni bilmasdan ariza bersangiz, kutganingiz boshqa bo'ladi.",
             body=f"""<h4>Asosiy faktlar (elchixona sahifasi)</h4>
<ul><li>AQSh Davlat departamentining Ta'lim va madaniyat ishlari byurosi dasturi; World Learning boshqaradi.</li><li>AQSh kolleji yoki universitetida bir semestr daraja bermaydigan ([[non-degree]]) o'qish.</li><li>Siz AQShlik talabalar bilan kampusda yashaysiz, kunduzgi bakalavriat kurslarini (jumladan AQSh haqidagi bitta kursni) o'qiydi va 20 soat jamoat ishida qatnashadi.</li><li>Dastur oxirida Vashingtonda yetakchilik, aloqalar va vatanga qaytishga tayyorgarlik bo'yicha seminar.</li><li>Universitetni siz tanlamaysiz: joylashtirish akademik qiziqishingizga qarab.</li><li>Kreditni o'z universitetingizga o'tkazish sizning o'z mas'uliyatingiz; dastur yordam bermaydi.</li><li>Klinik yo'nalishlarda (tibbiyot, hamshiralik, veterinariya, farmakologiya) J-1 qoidalari tufayli kurslar cheklangan bo'lishi mumkin.</li></ul>
<h4>Nima qoplanadi</h4>
<p>AQShga borish-kelish, o'qish to'lovi, kampusda yashash va ovqat, tibbiy sug'urta, majburiy kitoblar, oylik kichik stipendiya va finalistlar uchun TOEFL imtihoni.</p>
<div class="box info">World Learning sahifasi: AQShning 60 dan ortiq oliy ta'lim muassasasi har yili talaba qabul qiladi va dastur arizalari odatda har yili noyabr boshidan dekabrgacha ochiladi.</div>
<div class="srcs">Manba: {EMB_UGRAD}; {UGRAD_WL}. {HOL}.</div>""",
             take="Global UGRAD: bir semestr, daraja yo'q, universitetni dastur tanlaydi, kredit o'tkazish sizning ishingiz. Xarajatlar dastur tomonidan qoplanadi.",
             quiz=[("Global UGRAD AQSh bakalavr diplomini beradi.", "n", "Noto'g'ri: bir semestrlik daraja bermaydigan o'qish."),
                   ("AQSh universitetini o'zingiz tanlaysiz.", "n", "Noto'g'ri: joylashtirish akademik qiziqishga qarab dastur tomonidan."),
                   ("Kreditni o'z universitetingizga o'tkazish sizning mas'uliyatingiz.", "t", "To'g'ri: dastur bunda yordam bermaydi."),
                   ("Dastur aviabilet, o'qish va yashashni qoplaydi.", "t", "To'g'ri: elchixona sahifasidagi ro'yxat.")],
             task="<ul><li>UGRAD sizga nima beradi va nima bermaydi: 3 tadan band yozing.</li><li>O'z universitetingizda kredit o'tkazish tartibini kimdan so'rashingizni yozing.</li></ul>",
             ph="Beradi: 1) ... Bermaydi: 1) ... Kredit: ... dekanat / xalqaro bo'lim"),
        dict(t="Muvofiqlik shartlari", short="Muvofiqlik", min=25, kind="✅ Tekshiruv", ic="shield",
             hook="UGRAD da bitta shartga mos kelmaslik arizani boshidan yopadi. Eng ko'p uchraydigan xato: oxirgi kurs talabasining ariza berishi.",
             body=f"""<h4>Kim ariza bera oladi (oxirgi e'lon, 2024–2025)</h4>
<div class="tbl"><table><thead><tr><th>Shart</th><th>Tekshirish</th></tr></thead><tbody>
<tr><td>Dastur boshlanishida kamida 18 yosh</td><td>Tug'ilgan sana</td></tr>
<tr><td>O'zbekiston fuqarosi, hozir O'zbekistonda yashaydi va o'qiydi</td><td>Pasport, o'qish joyi</td></tr>
<tr><td>Akkreditatsiyalangan O'zbekiston universitetida (davlat yoki xususiy) kunduzgi bakalavriatda, yaxshi akademik holatda</td><td>Ma'lumotnoma</td></tr>
<tr><td>Dasturdan keyin kamida bir o'quv yili o'qish qoladi; UGRAD bakalavriatning oxirgi semestri bo'la olmaydi</td><td>Kurs va o'quv rejasi</td></tr>
<tr><td>Yetakchilik salohiyati: o'qish, jamoat ishi, darsdan tashqari faoliyat</td><td>Dalillar (STAR usuli Bachelor Lab M7 da)</td></tr>
<tr><td>Ingliz tilini bilish; finalistlar TOEFL iBT topshiradi (dastur to'laydi)</td><td>Til darajasi</td></tr>
<tr><td>Dasturdan keyin to'g'ridan-to'g'ri O'zbekistonga qaytish</td><td>Majburiyat</td></tr>
</tbody></table></div>
<h4>Kim ariza bera olmaydi</h4>
<ul><li>AQSh fuqarolari va doimiy rezidentlari; hozir O'zbekistondan tashqarida o'qiyotgan, yashayotgan yoki ishlayotganlar; oxirgi kurs talabalari; UGRAD bitiruvchilari.</li><li>AQSh hukumati homiyligidagi 6 haftadan uzun almashinuvni tugatib, 2 yillik vatanda bo'lish talabini hali bajarmaganlar.</li><li>So'nggi 3 yilda AQSh doimiy yashash huquqiga ariza berganlar; AQSh missiyalarining mahalliy xodimlari va ularning oila a'zolari (belgilangan muddat ichida).</li></ul>
<p>AQSh yoki xorijda tajribasi kam yoki umuman yo'q nomzodlarga ustunlik beriladi.</p>
<div class="srcs">Manba: {EMB_UGRAD}. Shartlar oxirgi e'londan; yangi sikl e'lonida o'zgarishi mumkin.</div>""",
             take="Asosiy shartlar: 18+, O'zbekistonda yashash va kunduzgi o'qish, kamida bir yil o'qish qolishi, ingliz tili, qaytish. Oxirgi kurs va xorijda yashayotganlar mos emas.",
             task="<ul><li>Har shart bo'yicha o'zingizni \"mos / tekshirish kerak / mos emas\" deb belgilang.</li><li>Bitta \"mos emas\" bo'lsa, UGRAD yopiq: 5.5 dagi muqobilga o'ting.</li></ul>",
             ph="18+: mos; fuqarolik va yashash: mos; kunduzgi: ...; 1 yil qoladi: ...; til: ...; xulosa: ..."),
        dict(t="Sikl holatini kuzatish", short="Kuzatuv", min=20, kind="🔔 Kuzatuv", ic="bell",
             hook="UGRAD ning har sikli alohida e'lon qilinadi. E'lon chiqmagan sikl uchun \"muddat\" aytayotgan har qanday post rasmiy emas.",
             body=f"""<h4>{HOL} holat</h4>
<div class="tbl"><table><thead><tr><th>Manba</th><th>Nima ko'rsatadi</th></tr></thead><tbody>
<tr><td>AQSh elchixonasi (Toshkent), UGRAD sahifasi</td><td>2024–2025 sikli e'loni, muddat 15.12.2024 (sahifa 05.12.2025 da yangilangan, yangi sikl yo'q)</td></tr>
<tr><td>Elchixonaning almashinuv dasturlari ro'yxati (05.08.2026 yangilangan)</td><td>Global UGRAD ro'yxatda bor; joriy ariza holati ko'rsatilmagan</td></tr>
<tr><td>World Learning UGRAD sahifasi</td><td>Dastur faol tasvirlangan; arizalar odatda har yili noyabr boshidan dekabrgacha</td></tr>
</tbody></table></div>
<h4>Kuzatuv rejasi</h4>
<ol><li>Elchixonaning UGRAD va almashinuv dasturlari sahifalarini oyiga bir marta oching, sana bilan yozing.</li><li>Rasmiy elchixona ijtimoiy tarmoq kanallarini kuzating; boshqa kanaldagi xabarni elchixona sahifasi bilan solishtiring.</li><li>Savol bo'lsa, oxirgi e'londagi rasmiy manzilga (Tashkent-Program@state.gov, mavzuda \"Global UGRAD\") yozing.</li><li>Noyabr–dekabr oylarida tekshirishni haftalik qiling.</li></ol>
<div class="box warn">Sikl e'lon qilinmaguncha UGRAD uchun pul to'lab \"tayyorlov\" xizmati sotib olmang. Kompas Lab ham bu bosqichda faqat bepul tayyorgarlikni tavsiya qiladi: ingliz tili, yetakchilik dalillari, o'qish natijalari.</div>
<div class="srcs">Manba: {EMB_UGRAD}; {EMB_EXCH}; {UGRAD_WL}.</div>""",
             take="UGRAD sikli rasman e'lon qilinmaguncha muddat yo'q. Elchixona sahifasini oyiga bir marta, noyabr–dekabrda haftalik tekshiring.",
             task="<ul><li>Elchixonaning UGRAD sahifasini oching va bugungi holatni sana bilan yozing.</li><li>Telefoningizga oylik eslatma qo'ying.</li></ul>",
             ph="31.10.2026: UGRAD sahifasi — oxirgi sikl ..., yangi e'lon: yo'q / bor. Eslatma: har oyning ... kuni"),
        dict(t="Ariza va tanlov", short="Ariza", min=30, kind="📝 Reja", ic="memo",
             hook="UGRAD arizasi ingliz tilida, onlayn topshiriladi va muddatdan keyin o'zgartirib bo'lmaydi. Tayyorgarlik e'londan oldin boshlanadi, lekin ariza faqat e'lon ko'rsatmasi bo'yicha to'ldiriladi.",
             body="""<h4>Oxirgi e'londagi tartib</h4>
<ul><li>Ariza World Learning portali orqali onlayn, faqat ingliz tilida.</li><li>Muddatdan keyin ariza tahrirlanmaydi; erta topshirish tavsiya qilinadi.</li><li>Finalistlar va zaxiradagilar TOEFL iBT topshiradi; xarajatni dastur qoplaydi.</li></ul>
<h4>E'lon chiqquncha tayyorlanadigan dalillar</h4>
<div class="tbl"><table><thead><tr><th>Dalil</th><th>Qayerda o'rganiladi</th></tr></thead><tbody>
<tr><td>Yetakchilik va jamoat ishi holatlari (STAR)</td><td>Bachelor Lab M7</td></tr>
<tr><td>Insho yozish va tahrir</td><td>Bachelor Lab M9–M10</td></tr>
<tr><td>Tavsiya so'rash</td><td>Bachelor Lab M8</td></tr>
<tr><td>Ingliz tili darajasi</td><td>Mustaqil; test strategiyasi Bachelor Lab M5</td></tr>
<tr><td>O'qish natijalari va ma'lumotnoma</td><td>O'z universitetingiz</td></tr>
</tbody></table></div>
<h4>UGRAD ga xos ikki savol</h4>
<ol><li><b>Akademik qiziqish:</b> sizni qaysi yo'nalishdagi kurslarga joylashtirish kerak va nega? Bu joylashtirishga ta'sir qiladi.</li><li><b>Qaytgandan keyin:</b> O'zbekistonda o'qishni tugatish va olgan tajribangizni qanday ishlatishingiz. Dastur qaytishni talab qiladi.</li></ol>
<div class="box info">Insho savollari va hajmi har siklda e'londa beriladi. O'tgan yilgi savollarni yod olib tayyorlamang.</div>""",
             take="Ariza onlayn, ingliz tilida, muddatdan keyin o'zgarmaydi. Hozir dalillarni tayyorlang; insho faqat yangi e'londagi savollar bo'yicha yoziladi.",
             task="<ul><li>5 ta dalilning har biri bo'yicha hozirgi holatingizni yozing.</li><li>Akademik qiziqish va qaytgandan keyingi reja bo'yicha 2–3 jumlalik qoralama fikr (insho emas).</li></ul>",
             ph="STAR holatlari: ... ta; ingliz tili: ...; ma'lumotnoma: ...; qiziqish: ...; qaytgandan keyin: ..."),
        dict(t="Boshqa almashinuv dasturlari va J-1", short="Boshqalar", min=25, kind="🧭 Xarita", ic="compass",
             hook="UGRAD yopiq yoki mos kelmasa, bu AQSh tajribasining oxiri emas. Elchixona ro'yxatida turli yosh va kasb uchun boshqa dasturlar bor.",
             body=f"""<h4>Elchixona ro'yxatidan (yangilangan 05.08.2026)</h4>
<div class="tbl"><table><thead><tr><th>Dastur</th><th>Kimga</th><th>Nima</th></tr></thead><tbody>
<tr><td>FLEX</td><td>Maktab o'quvchilari</td><td>AQSh maktabida bir o'quv yili, oilada yashab</td></tr>
<tr><td>SUSI ([[Young Women Leaders]])</td><td>Talaba yetakchi qizlar</td><td>Qisqa yozgi akademik dastur</td></tr>
<tr><td>[[TechGirls]]</td><td>Fan va texnologiyaga qiziqqan qizlar</td><td>Yozgi almashinuv</td></tr>
<tr><td>[[TechWomen]]</td><td>STEM sohasidagi ayollar</td><td>Martaba va mentorlik</td></tr>
<tr><td>Fulbright Foreign Student Program</td><td>Bakalavr diplomli mutaxassislar</td><td>Magistratura (M6)</td></tr>
<tr><td>Hubert H. Humphrey [[Fellowship]]</td><td>Martaba o'rtasidagi mutaxassislar</td><td>10 oylik daraja bermaydigan o'qish va amaliyot</td></tr>
<tr><td>Fulbright [[Visiting Scholar]]</td><td>Olimlar va o'qituvchilar</td><td>3–5 oylik ma'ruza yoki tadqiqot</td></tr>
</tbody></table></div>
<h4>J-1 va 2 yillik talab</h4>
<p>Davlat dasturlari J-1 almashinuv vizasi bilan bo'ladi. Harvard xalqaro ofisi tushuntiradi: J-1 egasi AQSh hukumati, o'z hukumati yoki xalqaro tashkilot mablag'i bilan moliyalashtirilgan bo'lsa, 212(e) talabi qo'llanadi: vatanga qaytib, 2 yil yashamaguncha immigratsion viza, H yoki L vizasini ololmaydi va AQSh ichida boshqa maqomga o'ta olmaydi. UGRAD e'loni ham bu talabni bajarmaganlarni ariza berishdan chetlatadi.</p>
<div class="box warn">AQShda qolib ishlashni rejalashtirgan nomzod uchun hukumat moliyalashtirgan J-1 dasturlari mos emas. Bu yo'l M3–M4 (bakalavr) yoki M7 (PhD) orqali F-1 bilan.</div>
<div class="srcs">Manba: {EMB_EXCH}; {HARVARD_212E}; {EMB_UGRAD}. {HOL}.</div>""",
             take="UGRAD dan tashqari maktab, yozgi, kasbiy va ilmiy almashinuvlar bor. Hukumat moliyalashtirgan J-1 dasturlarida 2 yillik vatanda yashash talabi qo'llanadi.",
             task="<ul><li>Ro'yxatdan sizga yoki oilangizga mos 1–2 dasturni tanlang.</li><li>B rejangizni yozing: UGRAD bo'lmasa nima qilasiz.</li></ul>",
             ph="Mos dastur: ... B reja: ..."),
    ],
    tool=dict(id="ugrad", short="Karta", h2="Almashinuv dasturi kartasi", sub="Muvofiqlikni tez tekshirish va kuzatuv rejasi.",
              h3="UGRAD kartasi", tag="6 maydon", ic="usa", btn="Kartani saqlash", badge="Almashinuvchi", min=5,
              pre="""<div class="fld"><label>Tez tekshiruv <small>oxirgi e'lon shartlari</small></label><div class="cklist" id="ugQ">
<label class="ck"><input type="checkbox" data-u="1"><span>Dastur boshlanishida 18 yoshdan oshgan bo'laman</span></label>
<label class="ck"><input type="checkbox" data-u="2"><span>O'zbekiston fuqarosiman, hozir O'zbekistonda yashayman va o'qiyman</span></label>
<label class="ck"><input type="checkbox" data-u="3"><span>Kunduzgi bakalavriatda, yaxshi akademik holatdaman</span></label>
<label class="ck"><input type="checkbox" data-u="4"><span>Dasturdan keyin kamida bir o'quv yilim qoladi</span></label>
<label class="ck"><input type="checkbox" data-u="5"><span>Avval UGRAD da qatnashmaganman va bajarilmagan 2 yillik talabim yo'q</span></label>
<label class="ck"><input type="checkbox" data-u="6"><span>Dasturdan keyin O'zbekistonga qaytishga tayyorman</span></label>
</div><div id="ugOut" class="out" style="white-space:normal">Belgilang.</div></div>""",
              fields=[dict(k="holat", label="Sikl holati", hint="sana bilan", ph="31.10.2026: yangi e'lon yo'q / bor, muddat ..."),
                      dict(k="kanal", label="Kuzatuv kanallari va eslatma", type="area", ph="Elchixona sahifasi, rasmiy kanal ...; har oy ... kuni"),
                      dict(k="dalil", label="Tayyorlanayotgan dalillar", type="area", ph="STAR ..., ingliz tili ..., ma'lumotnoma ..."),
                      dict(k="kredit", label="Kredit o'tkazish bo'yicha kelishuv", hint="kim bilan gaplashdingiz", ph="..."),
                      dict(k="breja", label="B reja", type="area", ph="..."),
                      dict(k="qaror", label="Qaror", type="select", opts=["UGRAD ga tayyorlanaman", "Sikl e'lonini kutaman", "Boshqa dastur", "Mos emasman"])]),
    check=dict(h2="M5 nazorati", sub="Kartani yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["UGRAD daraja bermasligini va universitetni dastur tanlashini bilaman.", "Har shart bo'yicha o'zimni tekshirdim.",
                      "Sikl holatini elchixona sahifasidan sana bilan yozdim.", "Kuzatuv eslatmasi qo'yilgan.",
                      "Kredit o'tkazish bo'yicha o'z universitetimdan so'radim yoki so'rash rejasi bor.", "Insho faqat yangi e'lon savollari bo'yicha yozilishini tushunaman.",
                      "J-1 va 2 yillik talab rejalarimga ta'sirini o'qidim.", "B reja yozilgan."]),
    art_title="Almashinuv dasturi kartasi", art_short="Karta",
    art=[("Dastur haqida", ["a1"]), ("Muvofiqlik", ["ugcalc", "a2"]), ("Sikl holati va kuzatuv", ["holat", "kanal", "a3"]), ("Dalillar", ["dalil", "a4"]),
         ("Kredit o'tkazish", ["kredit"]), ("B reja", ["breja", "a5"]), ("Qaror", ["qaror"])],
    tip="Davlat dasturida eng katta xavf e'lon qilinmagan sikl uchun vaqt va pul sarflash. Kuting, kuzating va shu vaqtda boshqa arizalarda ham ishlaydigan dalillarni yig'ing.",
    sources=f"{EMB_UGRAD}; {UGRAD_WL}; {EMB_EXCH}; {HARVARD_212E}. {STD}",
    js="""window.KGTool = { init: function () {
  var box = document.getElementById("ugQ"), o = document.getElementById("ugOut");
  var cbs = box.querySelectorAll("input[data-u]");
  function run() {
    var n = 0, st = [];
    cbs.forEach(function (c) { if (c.checked) n++; st.push(c.checked ? 1 : 0); c.parentNode.classList.toggle("on", c.checked); });
    var ok = n === cbs.length;
    var txt = ok ? "Oxirgi eʼlon shartlari boʻyicha mos. Yangi sikl eʼlonida shartlarni qayta tekshiring." : "Mos emas yoki tekshirilmagan bandlar: " + (cbs.length - n) + " ta. Bitta mos kelmaydigan shart arizani yopadi.";
    o.innerHTML = "<span class=\\"pill " + (ok ? "ok" : "no") + "\\">" + n + "/" + cbs.length + "</span> " + KG.esc(txt);
    KG.S.notes.ugcalc = n + "/" + cbs.length + ": " + txt; KG.S.notes.ug_in = st.join(""); KG.save();
  }
  if (KG.S.notes.ug_in) { String(KG.S.notes.ug_in).split("").forEach(function (v, i) { if (cbs[i]) cbs[i].checked = v === "1"; }); }
  cbs.forEach(function (c) { c.addEventListener("change", run); });
  run();
} };""",
)
