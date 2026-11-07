from common import UKRI, MSCA, EURAXESS, LEEDS, VISA, HOL, STD

INP = "min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"

MOD = dict(
    title="Moliya, doktorlik o'rni va moliyaviy qaror",
    desc="PhD Lab M6: moliyalashtirish turlari, Buyuk Britaniyada doktorlik o'rinlari (studentship), Yevropada maoshli PhD va MSCA, dastlabki xarajatlar, taklif shartlarini o'qish va moliyaviy qaror. Natija: moliya taqqoslash jadvali va 12 oylik pul oqimi.",
    lead="“To'liq moliyalashtirilgan” iborasi har e'londa bir xil narsani anglatmaydi. Bu modulda paket nimani qoplashini qatorma-qator ajratasiz, dastlabki xarajatni hisoblaysiz va moliyaviy bo'shliqni ko'rib, qaror qilasiz.",
    hero="money", weeks="1–2", next="M7 Ariza, intervyu va qaror", next_href="phd-lab-o.html?m=7",
    goals=[("money", "Moliya taqqoslash jadvali", "o'qish to'lovi, stipendiya, maosh, yig'imlar alohida"),
           ("calendar", "12 oylik pul oqimi", "minimal, kutilgan va qiyin stsenariy"),
           ("shield", "Moliyaviy bo'shliq va B reja", "dastlabki 60 kunlik naqd pul bilan")],
    warn="Mamlakat va stipendiya qoidalari tez o'zgaradi. Darsda moliya mantig'i; aniq summa, to'lov, muddat va fuqarolik cheklovi tanlangan dasturning rasmiy sahifasidan olinadi. Bu kurs moliyaviy maslahat emas.",
    lessons=[
        dict(t="Moliyalashtirish turlarining farqi", short="Turlar", min=25, kind="🧭 Xarita", ic="money",
             hook="“To'liq moliyalashtirilgan” ([[fully funded]]) e'lonlarning qamrovi har xil. Qaysi qism yozma tasdiqlanganini bilmasangiz, byudjet qog'ozda qoladi.",
             body=f"""<h4>Paketning qismlari</h4>
<ul><li>O'qish to'lovidan ozod qilish ([[tuition waiver]]).</li><li>Yashash stipendiyasi ([[maintenance stipend]]).</li><li>Ish shartnomasi bo'yicha maosh.</li><li>O'qitish yoki tadqiqot assistentligi.</li><li>Dala ishi, konferensiya, tibbiy sug'urta uchun alohida mablag'.</li></ul>
<p>Moliya kafedraga yoki rahbarning grantiga tegishli bo'lishi mumkin; shartlar yillik yoki butun muddatga ekanini tekshiring. UKRI mablag'ini talaba UKRI ga emas, tashkilot orqali oladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> A paket o'qish to'lovini qoplaydi, yashashni emas. B paket ikkalasini qoplaydi, lekin ilmiy safar uchun alohida tasdiq kerak.</div>
<div class="box warn">O'qish to'lovidan ozod qilishni stipendiya yoki maosh bilan adashtirmang.</div>
<div class="srcs">Manba: {UKRI}. {HOL}.</div>""",
             take="Har paketni qismlarga ajrating va har qismga “yozma tasdiqlangan / shartli / noma'lum” belgisini qo'ying.",
             task="<ul><li>4 ta paket tarkibini yozing.</li><li>Qaysi qismlar kafolatli, qaysilari shartli ekanini belgilang.</li><li>To'lov jadvalini yozing.</li></ul><p><b>O'zingizga savol:</b> moliyaning qaysi bandi yozma taklif bilan tasdiqlangan?</p>",
             ph="Paket A: to'lov ✓, stipendiya —, sug'urta ? ; Paket B: ..."),
        dict(t="Buyuk Britaniyada doktorlik o'rinlari", short="UK", min=30, kind="🇬🇧 Tizim", ic="scroll",
             hook="Buyuk Britaniyada moliyalashtirilgan PhD ko'pincha doktorlik o'rni ([[studentship]]) shaklida keladi. Xalqaro talaba uchun shartlar alohida o'qiladi.",
             body=f"""<p>Yo'llar: doktorlik ta'limi hamkorliklari va markazlari ([[DTP]], [[CDT]]), tadqiqot kengashi o'rinlari, fakultet stipendiyasi va loyihaga biriktirilgan o'rin.</p>
<p>UKRI mablag'ni tadqiqot tashkilotlariga beradi. UKRI sahifasiga ko'ra xalqaro talabalar odatda ariza bera oladi, lekin ular uchun o'rinlar soni cheklangan; o'qish to'lovidagi farqni kim qoplashini tashkilot hal qiladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> O'rin faqat mahalliy talaba to'lovini ([[home fee]]) qoplasa, xalqaro to'lov ([[international fee]]) farqini kim to'lashi noma'lum bo'lishi mumkin. Bunday e'lonni “xalqaro uchun to'liq moliyalashtirilgan” deb xulosa qilmang.</div>
<div class="box warn">O'tgan yilgi stipendiya summasini joriy yil uchun kafolat deb yozmang.</div>
<div class="srcs">Manba: {UKRI}; {LEEDS}. {HOL}.</div>""",
             take="UK da asosiy savol: xalqaro to'lov farqi kimning zimmasida? Javob yozma bo'lishi kerak.",
             task="<ul><li>UKRI va universitet manbalarini juftlang.</li><li>Xalqaro to'lov holatini tekshiring.</li><li>Farqni email bilan aniqlang.</li></ul><p><b>O'zingizga savol:</b> mahalliy va xalqaro to'lov farqi kimning zimmasida?</p>",
             ph="E'lon: ... ; qoplaydi: home fee / international fee ; email savoli: ..."),
        dict(t="Yevropa: maoshli PhD va MSCA", short="Yevropa", min=30, kind="🇪🇺 Tizim", ic="daad",
             hook="Yevropadagi ba'zi PhD lar stipendiya emas, ish shartnomasi orqali moliyalanadi. Bu soliq, sug'urta va huquqlarni o'zgartiradi.",
             body=f"""<p>MSCA doktorlik tarmoqlarida nomzod har qanday fuqarolikda bo'lishi mumkin, lekin mobillik qoidasi bor: yollash sanasidan oldingi 36 oyda 12 oydan ko'p o'sha mamlakatda yashamagan yoki ishlamagan bo'lish kerak. O'rinlar EURAXESS kabi portallarda e'lon qilinadi.</p>
<p>Yashash va mobillik to'lovlari yalpi ([[gross]]) yoki sof ([[net]]) ekanini va mamlakat soliqlarini alohida ko'ring. Ish beruvchi, mezbon tashkilot, daraja beradigan universitet va shartnoma muddatini ajrating.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> E'londagi summa yalpi bo'lsa, uni bank hisobiga tushadigan sof daromad deb olish xato; yashash xarajati shaharga qarab farq qiladi.</div>
<div class="box warn">MSCA tarmog'ining moliya tanlovi muddatini doktorantning ishga ariza muddati bilan aralashtirmang.</div>
<div class="srcs">Manba: {MSCA}; {EURAXESS}. {HOL}.</div>""",
             take="Maoshli PhD da yalpi va sof summa, soliq va shartnoma muddati alohida tekshiriladi.",
             task="<ul><li>EURAXESS dagi 3 ta e'lonni solishtiring.</li><li>Mobillik va daraja holatini belgilang.</li><li>Yalpi va sof summa bo'yicha savollarni yozing.</li></ul><p><b>O'zingizga savol:</b> nomzod sifatida aynan qayerga ariza berasiz?</p>",
             ph="E'lon 1: ..., ish beruvchi ..., daraja ..., summa (yalpi/sof?) ... ; mobillik: ✓"),
        dict(t="Xarajatlar va dastlabki pul", short="Xarajat", min=30, kind="🧮 Hisob", ic="hourglass",
             hook="Hatto yaxshi stipendiyada ham dastlabki oylar qiyin bo'lishi mumkin: depozit, viza va yo'l birinchi stipendiyadan oldin to'lanadi.",
             body=f"""<p>Model qiling: viza, kerak bo'lsa ATAS, yo'l, ijara depoziti, birinchi oy ijarasi, ko'chish, tibbiy yig'im, sug'urta, bola parvarishi, jihozlar va valyuta almashinuvi.</p>
<p>Stipendiya ko'pincha oyma-oy yoki chorakma-chorak to'lanadi; dastlabki naqd pulni alohida hisoblang. Narxni rasmiy sahifadan yoki yozma taklifdan oling.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Oylik daromad 100 birlik, xarajat 95 birlik: 5 birlik zaxira. Lekin 250 birlik dastlabki depozit uchun qisqa muddatli naqd pul yetishmaydi.</div>
<div class="box warn">“Yarim stavka ishlab olaman” degan taxminni viza ish huquqini tekshirmasdan pul oqimiga qo'shmang.</div>
<div class="srcs">Manba: {VISA}. {HOL}.</div>""",
             take="Uch stsenariy (minimal, kutilgan, qiyin) va bir martalik xarajatlar bilan dastlabki 60 kunlik naqd pul hisoblanadi.",
             task="<ul><li>Minimal, kutilgan va qiyin stsenariy tuzing.</li><li>Bir martalik xarajatlarni qo'shing.</li><li>3 oylik zaxira maqsadini ko'ring.</li></ul><p><b>O'zingizga savol:</b> dastlabki 60 kunlik naqd pul yetarlimi?</p>",
             ph="Oylik daromad ..., xarajat ... ; bir martalik: viza ..., depozit ..., yo'l ... ; 60 kunlik naqd: ..."),
        dict(t="Taklif shartlarini o'qish", short="Shartlar", min=25, kind="📑 Hujjat", ic="memo",
             hook="Moliya taklifi akademik taklif bilan bir vaqtda yoki keyin kelishi mumkin. Ikkalasini alohida o'qish kerak.",
             body=f"""<p>Moliya xatida: summa, to'lov oralig'i, muddat, progress talablari, o'qitish majburiyati, to'lov maqomi, yillik ko'rik, chiqib ketish oqibatlari va kechiktirish qoidalari.</p>
<p>Ish shartnomasi va stipendiya kelishuvi boshqa-boshqa hujjatlar: ikkalasini ham rasmiy shart sifatida o'qing.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Akademik taklif shartli bo'lsa, moliya boshlanish sanasi avtomatik tasdiqlanmasligi mumkin. “Professor moliya bor dedi” moliya bo'limi xatining o'rnini bosmaydi.</div>
<div class="box warn">Og'zaki va'dalarni byudjetda kafolatli deb belgilamang.</div>""",
             take="Har noaniq band uchun aniqlik so'rovi yoziladi va yozma javob saqlanadi.",
             quiz=[("Mahalliy talaba to'lovini qoplaydigan o'rin xalqaro talaba uchun avtomatik to'liq moliyalashtirilgan.", "n", "Noto'g'ri: xalqaro to'lov farqini kim qoplashi alohida tekshiriladi."),
                   ("MSCA doktorlik tarmog'ida nomzod har qanday fuqarolikda bo'lishi mumkin.", "t", "To'g'ri, lekin mobillik qoidasi bor."),
                   ("E'londagi yalpi summa bank hisobiga tushadigan sof daromadga teng.", "n", "Noto'g'ri: soliq va ajratmalar chiqariladi."),
                   ("Og'zaki moliya va'dasi byudjetda kafolatli daromad sifatida yoziladi.", "n", "Noto'g'ri: faqat yozma tasdiq hisoblanadi.")],
             task="<ul><li>Taklif nazorat ro'yxatini to'ldiring.</li><li>Har hal bo'lmagan bandga aniqlik so'rovini yozing.</li><li>Yozma tasdiqni saqlang.</li></ul><p><b>O'zingizga savol:</b> moliya qachon va qaysi hujjat bilan kuchga kiradi?</p>",
             ph="Summa ..., to'lov ..., muddat ..., o'qitish ..., chiqib ketish ... ; savol: ..."),
        dict(t="Moliyaviy yakuniy qaror", short="Qaror", min=25, kind="⚖️ Qaror", ic="scroll",
             hook="Moliyaviy bo'shliq ilmiy qaror va hayot sifati bilan birga baholanadi. Eng kuchli rahbar ham pul yetishmovchiligini yopmaydi.",
             body=f"""<p>Baholang: sof pul oqimi, to'lov farqi, dastlabki xarajat, oila a'zolari, tibbiy xarajat, inflyatsiya, stipendiya uzaytirilmaslik xavfi va yashash narxi. Maqsad qabul olish emas, 3–4 yil ilmiy ishlash imkonini beradigan shartni tanlash.</p>
<p>Takliflarni solishtirishda ilmiy moslik, rahbarlik, moliya ishonchliligi va turmush sharoiti birga ko'riladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> A taklif: kuchli rahbar, lekin katta taqchillik. B taklif: yaxshi laboratoriya va moliyaviy xavfsizroq. B ni tanlash ilmiy maqsaddan voz kechish degani emas.</div>
<div class="box warn">Moliyaviy rejasiz taklifni qabul qilish qaytarib bo'lmaydigan xarajatlarga olib kelishi mumkin.</div>""",
             take="Eng yomon stsenariy hisoblangan va B reja yozilgan bo'lsa, qaror asosli.",
             task="<ul><li>3 ta taklif yoki 3 ta real imkoniyatni solishtiring.</li><li>Eng yomon holatni hisoblang.</li><li>Qaror jurnaliga shartli tavsiya yozing.</li></ul><p><b>O'zingizga savol:</b> moliya bo'lmasa, ariza bo'yicha qanday qaror qilasiz?</p>",
             ph="A: bo'shliq ..., B: ..., C: ... ; eng yomon holat: ... ; qaror: ..."),
    ],
    tool=dict(id="hisob", short="Hisob", h2="Moliyaviy bo'shliq hisoblagichi", sub="Bir xil valyutada oylik va bir martalik xarajatlarni kiriting; 12 oylik bo'shliq va dastlabki naqd pul ehtiyoji chiqadi.",
              h3="12 oylik pul oqimi", tag="5 maydon", ic="money", btn="Hisobni saqlash", badge="Moliyachi", min=4,
              pre=f"""<div class="fld"><label>Hisoblagich <small>bir xil valyutada</small></label><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px"><input id="fI" type="number" min="0" placeholder="Oylik daromad (sof)" style="{INP}"><input id="fC" type="number" min="0" placeholder="Oylik xarajat" style="{INP}"><input id="fO" type="number" min="0" placeholder="Bir martalik xarajat" style="{INP}"><input id="fD" type="number" min="0" max="6" placeholder="Birinchi to'lovgacha oy" style="{INP}"></div><div id="fOut" class="out" style="white-space:normal">Raqamlarni kiriting.</div></div>""",
              fields=[dict(k="paket", label="Paket va manba", ph="... universiteti, studentship, havola ..."),
                      dict(k="qamrov", label="Nimani qoplaydi", type="area", ph="To'lov ..., stipendiya ..., sug'urta ..., safar ..."),
                      dict(k="birm", label="Bir martalik xarajatlar ro'yxati", type="area", ph="Viza ..., ATAS ..., yo'l ..., depozit ..."),
                      dict(k="breja", label="B reja", type="area", ph="Bo'shliq yopilmasa: ..."),
                      dict(k="qaror", label="Moliyaviy xulosa", type="select", opts=["Moliya yetarli", "Kichik bo'shliq, B reja bor", "Katta bo'shliq, qabul qilinmaydi", "Yozma tasdiq kutilmoqda"])]),
    check=dict(h2="M6 nazorati", sub="Moliyaviy qarordan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["To'lov, stipendiya, yig'im va xarajatlar alohida yozilgan.", "Moliya muddati va shartlari aniq.", "Xalqaro talaba holati manba bilan tekshirilgan.",
                      "Bir martalik xarajatlar va oila ehtiyojlari hisoblangan.", "Yalpi va sof summa farqi aniqlangan.",
                      "Ish daromadi viza shartisiz hisobga olinmagan.", "Moliyaviy bo'shliq va B reja hisoblangan."]),
    art_title="Moliya taqqoslash va 12 oylik pul oqimi", art_short="Moliya",
    art=[("Paket", ["paket", "a1"]), ("Qamrov", ["qamrov", "a2", "a3"]), ("Bir martalik xarajatlar", ["birm", "a4"]), ("Hisob", ["fcalc"]),
         ("Taklif shartlari", ["a5"]), ("Qaror va B reja", ["a6", "breja", "qaror"])],
    tip="Byudjetga faqat yozma tasdiqlangan pulni kiriting. Qolgani B reja ustuniga.",
    sources=f"{UKRI}; {MSCA}; {EURAXESS}; {LEEDS}; {VISA}. {STD}",
    js="""window.KGTool = { init: function () {
  var ids = ["fI", "fC", "fO", "fD"], o = document.getElementById("fOut");
  function v(id) { var x = parseFloat(document.getElementById(id).value); return isNaN(x) ? 0 : x; }
  function fmt(n) { return Math.round(n).toLocaleString("ru-RU"); }
  function run() {
    var I = v("fI"), C = v("fC"), O = v("fO"), D = Math.max(0, Math.min(6, Math.round(v("fD"))));
    if (!I && !C) { o.textContent = "Raqamlarni kiriting."; return; }
    var year = (I - C) * 12 - O, start = O + C * D, cls, tag;
    if (year >= 0 && start <= Math.max(0, I - C) * 3) { cls = "ok"; tag = "Moliya yetarli"; }
    else if (year >= 0) { cls = "chk"; tag = "Yil yopiladi, lekin boshida naqd pul kerak"; }
    else { cls = "no"; tag = "12 oylik bo\\u02bbshliq bor"; }
    var txt = "12 oy: " + (year >= 0 ? "+" : "") + fmt(year) + " (daromad " + fmt(I * 12) + ", xarajat " + fmt(C * 12 + O) + "). Birinchi to\\u02bblovgacha kerakli naqd pul: " + fmt(start) + ". " + tag + ".";
    o.innerHTML = "<span class=\\"pill " + cls + "\\">" + KG.esc(tag) + "</span> " + KG.esc(txt);
    KG.S.notes.fcalc = txt; KG.S.notes.f_in = [I, C, O, D].join("|"); KG.save();
  }
  if (KG.S.notes.f_in) { var p = String(KG.S.notes.f_in).split("|"); ids.forEach(function (id, i) { if (p[i] && p[i] !== "0") document.getElementById(id).value = p[i]; }); }
  ids.forEach(function (id) { document.getElementById(id).addEventListener("input", run); });
  run();
} };""",
)
