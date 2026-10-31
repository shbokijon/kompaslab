from common import UKRI_STUD, MSCA, EURAXESS, LEEDS, VISA, HOL, STD

INP = 'min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px'

MOD = dict(
    title="Moliyalashtirish va moliyaviy qaror",
    desc="PhD Lab M6: moliyalashtirish turlari, Buyuk Britaniyada doktorlik o'rinlari, MSCA va Yevropadagi maoshli doktorantura, xarajat va boshlang'ich pul, taklif shartlarini tekshirish, moliyaviy qaror. Natija: moliyalashtirish taqqoslamasi, 12 oylik pul oqimi va kamomad tahlili.",
    lead="Moliyalashtirish paketi aynan nimani qoplashini va sizga qancha kamomad qolishini hisoblaysiz. \"To'liq moliyalashtirilgan\" degan so'z hisob o'rnini bosmaydi.",
    hero="money", weeks="1–2", next="M7. Ariza, intervyu va qaror", next_href="phd-lab-m7.html",
    goals=[("money", "Moliyalashtirish taqqoslamasi", "qoplanadi / qoplanmaydi, shartlar"),
           ("chart", "12 oylik pul oqimi", "oylik qoldiq va boshlang'ich xarajat"),
           ("shield", "Kamomad va B reja", "eng yomon holat hisoblangan")],
    warn=f"Stipendiya summalari, to'lovlar, muddatlar va fuqarolik cheklovlari har yili o'zgaradi: darsda mantiq, aniq raqam esa tanlagan dasturingizning rasmiy sahifasidan olinadi. Kompas Lab moliyaviy maslahatchi emas. Faktlar {HOL}.",
    lessons=[
        dict(t="Moliyalashtirish turlari", short="Turlar", min=25, kind="🧭 Xarita", ic="money",
             hook="\"To'liq moliyalashtirilgan\" ([[fully funded]]) iborasi har e'londa bir xil qamrovni anglatmaydi. Har qismini alohida tekshirmasangiz, birinchi oyda kutilmagan xarajat chiqadi.",
             body=f"""<div class="tbl"><table><thead><tr><th>Qism</th><th>Nima</th></tr></thead><tbody>
<tr><td>O'qish to'lovidan ozod qilish</td><td>Universitet to'lovi qoplanadi, yashash xarajati emas</td></tr>
<tr><td>Yashash stipendiyasi</td><td>Oylik yoki choraklik to'lov</td></tr>
<tr><td>Maosh (ish shartnomasi)</td><td>Soliq va ijtimoiy to'lovlar bilan</td></tr>
<tr><td>Ilmiy yoki o'qituvchi assistentlik</td><td>Ish evaziga to'lov (soat bilan)</td></tr>
<tr><td>Dala ishi, konferensiya byudjeti</td><td>Ko'pincha alohida</td></tr>
<tr><td>Tibbiy sug'urta yoki sog'liqni saqlash to'lovi</td><td>Mamlakatga qarab</td></tr></tbody></table></div>
<p>Pul kafedra, rahbar granti yoki tashqi fonddan kelishi mumkin; shartlar har yilga yoki butun muddatga ekanini tekshiring. UKRI pulni talabaga emas, tashkilotga beradi: o'rin universitet orqali olinadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> A taklif o'qish to'lovini qoplaydi, yashashni emas. B taklif ikkalasini qoplaydi, lekin dala safari uchun alohida ruxsat kerak.</div>
<div class="box warn">O'qish to'lovidan ozod qilishni stipendiya yoki maosh bilan adashtirmang.</div>
<div class="srcs">Manba: {UKRI_STUD}. {HOL}.</div>""",
             take="Har qism alohida: o'qish to'lovi, yashash, maosh, assistentlik, dala, sug'urta. Qaysi biri kafolatlangan, qaysi biri shartli, yozma tekshiriladi.",
             quiz=[("O'qish to'lovidan ozod qilish bor, stipendiya yo'q bo'lsa, bu to'liq moliyalashtirish.", "n", "Noto'g'ri: yashash xarajati alohida hisoblanadi."),
                   ("Paketlarni faqat summasi bilan emas, muddat, shartlar va shahar narxi bilan taqqoslash kerak.", "t", "To'g'ri."),
                   ("UKRI moliyalashtirgan o'ringa talaba universitet orqali ariza beradi.", "t", "To'g'ri: UKRI'ga to'g'ridan-to'g'ri ariza berilmaydi."),
                   ("Stipendiya sharti noaniq bo'lsa, og'zaki javob yetarli.", "n", "Noto'g'ri: yozma tasdiq so'raladi.")],
             task="<ul><li>4 ta paket tarkibini yozing.</li><li>Qaysi qism kafolatlangan, qaysi biri shartli, belgilang.</li><li>To'lov jadvalini yozing.</li></ul>",
             ph="Paket A: o'qish to'lovi — kafolat; stipendiya — ..., oylik; dala — shartli ..."),
        dict(t="Buyuk Britaniyada doktorlik o'rinlari", short="Britaniya", min=30, kind="🇬🇧 Mexanizm", ic="phd",
             hook="Buyuk Britaniyada moliyalashtirilgan PhD ko'pincha universitet orqali beriladigan doktorlik o'rni ([[studentship]]) shaklida bo'ladi. Xalqaro nomzod uchun eng muhim savol: qaysi to'lov stavkasi qoplanadi.",
             body=f"""<ul><li>Turlar: doktorlik o'qitish hamkorliklari va markazlari (DTP, CDT), universitet stipendiyalari, rahbar granti hisobidan loyiha o'rni.</li><li>UKRI mablag'ni tashkilotga beradi; xalqaro talabalar uchun o'rinlar soni cheklangan (UKRI sahifasi aniq foiz ko'rsatmaydi), muvofiqlikni universitet belgilaydi.</li><li>O'rin faqat mahalliy ([[home]]) stavkani qoplasa, xalqaro ([[international]]) stavka bilan farqni kim to'lashi e'londa yozilgan bo'lishi kerak.</li></ul>
<div class="box info">E'londa farq kim tomonidan qoplanishi yozilmagan bo'lsa, uni \"xalqaro talaba uchun to'liq moliyalashtirilgan\" deb hisoblamang: universitetga yozma savol yuboring.</div>
<div class="box warn">O'tgan yilgi stipendiya miqdorini joriy yil uchun kafolat deb yozmang.</div>
<div class="srcs">Manba: {UKRI_STUD}; {LEEDS}. {HOL}.</div>""",
             take="Britaniya: o'rin universitet orqali; xalqaro o'rinlar cheklangan; mahalliy va xalqaro stavka farqini kim qoplashi yozma aniqlanadi.",
             task="<ul><li>UKRI va universitet sahifalarini juftlab o'qing.</li><li>Xalqaro to'lov holatini tekshiring.</li><li>Farq bo'yicha universitetga savol yozing.</li></ul>",
             ph="O'rin: ... — qoplaydi: mahalliy/xalqaro stavka; savol yuborildi: ..."),
        dict(t="MSCA va Yevropadagi maoshli doktorantura", short="Yevropa", min=30, kind="🇪🇺 Mexanizm", ic="compass",
             hook="Yevropadagi ayrim PhD lar stipendiya emas, mehnat shartnomasi orqali moliyalanadi. Bu soliq, ijtimoiy kafolat va viza turini o'zgartiradi.",
             body=f"""<ul><li>MSCA doktorlik tarmoqlari: istalgan fuqarolik; ishga olish sanasidan oldingi 36 oyda ishga oluvchi mamlakatda 12 oydan ortiq yashamagan yoki asosiy faoliyat yuritmagan bo'lish; doktorlik darajasi yo'qligi. Ariza EURAXESS dagi e'lon orqali to'g'ridan-to'g'ri tashkilotga beriladi.</li><li>Maoshli PhD (Niderlandiya, Skandinaviya, Shveytsariya kabi): ish beruvchi, mezbon va daraja beruvchi tashkilot farq qilishi mumkin.</li><li>Yashash va mobillik nafaqalari yalpi (soliqdan oldin) yoki sof bo'lishi mumkin: shuni aniqlang.</li></ul>
<div class="box info">E'londagi summa yalpi bo'lsa, uni bankka tushadigan sof daromad deb hisoblamang: yashash xarajati shaharga qarab farq qiladi.</div>
<div class="box warn">MSCA tarmog'ining loyiha tanlovi muddatini doktorantning ishga ariza muddati bilan aralashtirmang: siz e'lon qilingan o'ringa topshirasiz.</div>
<div class="srcs">Manba: {MSCA}; {EURAXESS}. {HOL}.</div>""",
             take="MSCA: istalgan fuqarolik, mobillik qoidasi (36 oyda 12 oydan ortiq emas), ariza e'lon orqali. Maoshli PhD: yalpi va sof summani ajrating.",
             task="<ul><li>EURAXESS dagi 3 e'lonni solishtiring.</li><li>Mobillik va daraja holatini tekshiring.</li><li>Yalpi va sof summa bo'yicha savollarni yozing.</li></ul>",
             ph="E'lon 1: ... — mobillik: mos/tekshirish; summa: yalpi ...; savol: ..."),
        dict(t="Xarajatlar va boshlang'ich pul", short="Xarajat", min=30, kind="🧮 Hisob", ic="chart",
             hook="Kuchli stipendiyada ham dastlabki oylar xarajati muammo bo'lishi mumkin: depozit, viza, chipta birinchi stipendiyadan oldin to'lanadi.",
             body=f"""<h4>Hisobga olinadi</h4>
<ul><li>Viza va (kerak bo'lsa) ATAS</li><li>Sog'liqni saqlash to'lovi yoki sug'urta</li><li>Chipta va ko'chish</li><li>Ijara depoziti va birinchi oy ijarasi</li><li>Oila a'zolari xarajatlari</li><li>Uskuna va valyuta almashinuvi</li></ul>
<p>Stipendiya ko'pincha oylik yoki choraklik to'lanadi, shuning uchun boshlang'ich naqd pulni alohida hisoblang. Raqamni rasmiy sahifadan yoki yozma taklifdan oling.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Oylik daromad 100 birlik, yashash 95 birlik: 5 birlik zaxira. Lekin 250 birlik boshlang'ich depozit uchun birinchi oylarda naqd pul yetishmaydi.</div>
<div class="box warn">\"Borib ishlab topaman\" degan rejani viza ruxsatini tekshirmay pul oqimiga qo'shmang.</div>
<div class="srcs">Manba: {VISA}. {HOL}.</div>""",
             take="Uch holat: minimal, kutilgan, og'ir. Bir martalik xarajatlar va 60 kunlik naqd pul alohida.",
             task="<ul><li>Minimal, kutilgan va og'ir holat hisobini yozing.</li><li>Bir martalik xarajatlarni qo'shing.</li><li>3 oylik zaxira maqsadini belgilang.</li></ul>",
             ph="Bir martalik: viza ..., chipta ..., depozit ... Oylik: kutilgan ...; og'ir ..."),
        dict(t="Taklif shartlarini tekshirish", short="Shartlar", min=25, kind="✅ Tekshiruv", ic="shield",
             hook="Moliyalashtirish taklifi akademik taklif bilan bir vaqtda yoki undan keyin kelishi mumkin. Professorning \"pul bor\" degani moliya bo'limining xati o'rnini bosmaydi.",
             body="""<h4>Moliyalashtirish xatida qidiriladi</h4>
<ul><li>Summa va to'lov oralig'i</li><li>Davomiylik</li><li>Taraqqiyot talablari va yillik ko'rib chiqish</li><li>O'qitish majburiyati</li><li>To'lov stavkasi (mahalliy yoki xalqaro)</li><li>O'qishni to'xtatsangiz nima bo'ladi</li><li>Boshlanishni kechiktirish qoidasi</li></ul>
<p>Ish shartnomasi va stipendiya kelishuvi turli hujjatlar: ikkalasini ham o'qing.</p>
<div class="box info">Akademik taklif shartli bo'lsa, moliyalashtirish boshlanish sanasi avtomatik tasdiqlanmaydi.</div>
<div class="box warn">Og'zaki va'dalarni byudjetda \"kafolatlangan\" deb belgilamang.</div>""",
             take="Summa, oraliq, muddat, majburiyat, stavka, to'xtatish va kechiktirish qoidalari yozma. Og'zaki va'da kafolat emas.",
             task="<ul><li>Taklif nazorat ro'yxatini to'ldiring.</li><li>Har hal bo'lmagan band uchun aniqlik so'rovi savolini yozing.</li><li>Yozma tasdiqni saqlang.</li></ul>",
             ph="Summa: ... (yozma: ha/yo'q); muddat: ...; savollar: 1) ..."),
        dict(t="Moliyaviy qaror", short="Qaror", min=25, kind="⚖️ Qaror", ic="seedling",
             hook="Moliyalashtirish kamomadi ilmiy qaror va hayot sifati bilan birga baholanadi. Maqsad istalgan qabulni olish emas, 3–4 yil ishlash imkonini beradigan shartni tanlash.",
             body="""<ul><li>Sof pul oqimi va o'qish to'lovi farqi</li><li>Boshlang'ich xarajat</li><li>Oila a'zolari va sog'liqni saqlash</li><li>Inflyatsiya va valyuta kursiga sezgirlik</li><li>Stipendiya muddati tugasa nima bo'ladi</li></ul>
<p>Takliflarni solishtirishda ilmiy moslik, rahbarlik, moliyaning ishonchliligi va yashash sharoiti birga ko'riladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> A taklif: kuchli rahbar, lekin kamomad katta. B taklif: yaxshi laboratoriya va moliyaviy xavfsizroq. B ni tanlash ilmiy maqsaddan voz kechish degani emas.</div>
<div class="box warn">Moliyaviy rejasiz taklifni qabul qilish qaytarib bo'lmaydigan xarajatlarga olib kelishi mumkin.</div>""",
             take="Qaror: ilmiy moslik + moliya ishonchliligi + eng yomon holat hisobi. Moliyasiz holat uchun oldindan qaror.",
             task="<ul><li>3 taklif yoki 3 haqiqiy imkoniyatni solishtiring.</li><li>Eng yomon holatni hisoblang.</li><li>Shartli qaroringizni yozing.</li></ul>",
             ph="A: oylik qoldiq ...; B: ...; eng yomon holat: ...; qarorim: ..., agar ..."),
    ],
    tool=dict(id="moliya", short="Taqqos", h2="Moliyalashtirish taqqoslamasi", sub="Barcha summalarni bitta valyuta va bitta yil kesimida kiriting. Bu taxminiy hisob, rasmiy taklif o'rnini bosmaydi.",
              h3="Moliya kartasi", tag="5 maydon + hisoblagich", ic="money", btn="Taqqoslamani saqlash", badge="Moliya realisti", min=4,
              pre=f"""<div class="fld"><label>Yillik balans hisoblagichi <small>bitta valyutada (masalan, GBP yoki EUR), 12 oy uchun</small></label>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px">
<input id="mInc" type="number" min="0" placeholder="Sof stipendiya yoki maosh" style="{INP}">
<input id="mExt" type="number" min="0" placeholder="Qo'shimcha tasdiqlangan yordam" style="{INP}">
<input id="mLiv" type="number" min="0" placeholder="Yillik yashash xarajati" style="{INP}">
<input id="mFee" type="number" min="0" placeholder="Qoplanmagan to'lovlar" style="{INP}">
<input id="mOne" type="number" min="0" placeholder="Bir martalik xarajatlar" style="{INP}">
</div><div id="mOut" class="out" style="white-space:normal">Raqamlarni kiriting.</div></div>""",
              fields=[dict(k="nom", label="Moliyalashtirish yoki o'rin nomi", hint="aniq rasmiy e'lon", ph="..."),
                      dict(k="tur", label="Turi", type="select", opts=["UKRI orqali doktorlik o'rni", "Universitet stipendiyasi", "Kafedra assistentligi", "Maoshli doktorlik lavozimi", "MSCA", "O'z hisobidan yoki boshqa"]),
                      dict(k="qamrov", label="Nima qoplanadi, nima qoplanmaydi?", type="area", ph="O'qish to'lovi, stipendiya, sug'urta, oila, to'lovlar"),
                      dict(k="shart", label="Majburiyat va davomiylik", type="area", ph="Har raqam uchun manba va sikl"),
                      dict(k="savol", label="Asosiy noaniqlik va keyingi savol", type="area", ph="Universitetga yozma savol")]),
    check=dict(h2="M6 nazorati", sub="Taqqoslamani yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["O'qish to'lovi, stipendiya, to'lovlar va xarajatlar alohida yozilgan.", "Moliyalashtirish muddati va shartlari aniq.",
                      "Xalqaro nomzod muvofiqligi manba bilan tekshirilgan.", "Mahalliy va xalqaro stavka farqi aniqlangan.",
                      "Bir martalik xarajatlar va oila ehtiyojlari hisoblangan.", "Yalpi va sof summa ajratilgan.",
                      "Kamomad va B reja hisoblangan.", "Og'zaki va'da kafolat deb yozilmagan."]),
    art_title="Moliyalashtirish taqqoslamasi va 12 oylik pul oqimi", art_short="Moliya",
    art=[("Paket tarkibi", ["nom", "tur", "a1"]), ("Qamrov", ["qamrov", "a2"]), ("Yevropa variantlari", ["a3"]), ("Xarajatlar", ["a4"]),
         ("Balans hisobi", ["mcalc"]), ("Taklif shartlari", ["shart", "a5"]), ("Qaror", ["a6"]), ("Ochiq savollar", ["savol"])],
    tip="Taklifni maosh kabi solishtiring: summa, yillar, majburiyat va shahar narxi. Hisobni ko'rmasdan \"ha\" demang.",
    sources=f"{UKRI_STUD}; {MSCA}; {EURAXESS}; {LEEDS}; {VISA}. {STD}",
    js="""window.KGTool = { init: function () {
  var ids = ["mInc", "mExt", "mLiv", "mFee", "mOne"], o = document.getElementById("mOut");
  function v(id) { var x = parseFloat(document.getElementById(id).value); return isNaN(x) ? 0 : x; }
  function fmt(n) { return Math.round(n).toLocaleString("ru-RU"); }
  function run() {
    if (!v("mInc") && !v("mLiv")) { o.textContent = "Raqamlarni kiriting."; return; }
    var y = v("mInc") + v("mExt") - v("mLiv") - v("mFee"), first = y - v("mOne"), m = y / 12;
    var txt = "Yillik balans: " + fmt(y) + " (oyiga " + fmt(m) + "). Birinchi yil bir martalik xarajatlar bilan: " + fmt(first) + ".";
    var cls = first < 0 ? "no" : "ok";
    o.innerHTML = "<span class=\\"pill " + cls + "\\">" + (first < 0 ? "Kamomad bor" : "Qoldiq musbat") + "</span> " + KG.esc(txt);
    KG.S.notes.mcalc = txt; KG.S.notes.m_in = ids.map(v).join("|"); KG.save();
  }
  if (KG.S.notes.m_in) { var p = String(KG.S.notes.m_in).split("|"); ids.forEach(function (id, i) { if (p[i] && p[i] !== "0") document.getElementById(id).value = p[i]; }); }
  ids.forEach(function (id) { document.getElementById(id).addEventListener("input", run); });
  run();
} };""",
)
