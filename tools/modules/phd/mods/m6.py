from common import UKRI, MSCA, EURAXESS, LEEDS, VISA, HOL, STD

INP = "min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"

MOD = dict(
    title="Moliya, doktorlik o'rni va moliyaviy qaror",
    desc="PhD Lab M6: moliyalashtirish turlari, Buyuk Britaniyadagi doktorlik o'rinlari (studentship), Yevropadagi maoshli PhD va MSCA, dastlabki xarajatlar, taklif shartlari va moliyaviy qaror. Natija: moliya taqqoslash jadvali va 12 oylik pul oqimi.",
    lead="<i>“To'liq moliyalashtirilgan”</i> degan so'z har e'londa boshqacha ma'noda ishlatiladi. Bu modulda paket nimalarni qoplashini <b>qatorma-qator</b> ajratasiz, dastlabki xarajatni hisoblaysiz va moliyaviy bo'shliqni ko'rib, qaror qilasiz.",
    hero="money", weeks="1–2", next="M7 Ariza, intervyu va qaror", next_href="phd-lab-o.html?m=7",
    goals=[("money", "Moliya taqqoslash jadvali", "o'qish to'lovi, stipendiya, maosh va yig'imlar alohida"),
           ("calendar", "12 oylik pul oqimi", "eng kam, kutilgan va qiyin holat"),
           ("shield", "Moliyaviy bo'shliq va zaxira reja", "dastlabki 60 kunlik naqd pul bilan")],
    warn="Mamlakat va stipendiya qoidalari tez o'zgaradi. Darsda moliyaning mantig'i bor; aniq summa, to'lov, muddat va fuqarolik cheklovini dasturning rasmiy sahifasidan oling. Bu kurs moliyaviy maslahat bermaydi.",
    lessons=[
        dict(t="Moliyalashtirish turlari", short="Turlar", min=25, kind="🧭 Xarita", ic="money",
             hook="<i>“To'liq moliyalashtirilgan”</i> ([[fully funded]]) e'lonlar har xil narsani qoplaydi. Qaysi qism <b>yozma tasdiqlanganini</b> bilmasangiz, byudjetingiz faqat qog'ozda qoladi.",
             body=f"""<h4>Paket qismlari</h4>
<ul><li>O'qish to'lovidan ozod qilish ([[tuition waiver]]).</li><li>Yashash uchun stipendiya ([[maintenance stipend]]).</li><li>Ish shartnomasi bo'yicha maosh.</li><li>Dars berish yoki tadqiqot assistentligi.</li><li>Dala ishi, konferensiya va tibbiy sug'urta uchun alohida mablag'.</li></ul>
<p>Mablag' kafedraga yoki rahbarning grantiga tegishli bo'lishi mumkin. Shartlar bir yilga yoki butun muddatga ekanini tekshiring. UKRI mablag'ini talaba to'g'ridan-to'g'ri olmaydi, universitet orqali oladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> A paket faqat o'qish to'lovini qoplaydi, yashash xarajati unga kirmaydi. B paket ikkalasini qoplaydi, lekin ilmiy safar uchun alohida ruxsat kerak.</div>
<div class="box warn">O'qish to'lovidan ozod qilishni stipendiya yoki maosh bilan adashtirmang.</div>
<div class="srcs">Manba: {UKRI}. {HOL}.</div>""",
             take="Har paketni qismlarga ajrating va har biriga belgi qo'ying: yozma tasdiqlangan, shartli yoki noma'lum.",
             task="<ul><li>4 ta paket tarkibini yozing.</li><li>Qaysi qismlar kafolatlangan, qaysilari shartli ekanini belgilang.</li><li>Pul qachon to'lanishini yozing.</li></ul><p><b>O'zingizga savol:</b> moliyaning qaysi qismi yozma taklif bilan tasdiqlangan?</p>",
             ph="Paket A: to'lov ✓, stipendiya yo'q, sug'urta ? ; Paket B: ..."),
        dict(t="Buyuk Britaniyada doktorlik o'rinlari", short="UK", min=30, kind="🇬🇧 Tizim", ic="scroll",
             hook="Buyuk Britaniyada moliyalashtirilgan PhD ko'pincha doktorlik o'rni ([[studentship]]) shaklida bo'ladi. Xalqaro talaba uchun shartlarni <b>alohida</b> o'qish kerak.",
             body=f"""<p>Yo'llar: doktorlik ta'limi hamkorliklari va markazlari ([[DTP]], [[CDT]]), tadqiqot kengashlari o'rinlari, fakultet stipendiyalari va loyihaga biriktirilgan o'rinlar.</p>
<p>UKRI mablag'ni tadqiqot tashkilotlariga beradi. UKRI sahifasida yozilishicha, xalqaro talabalar odatda ariza bera oladi, lekin ular uchun <b>o'rinlar soni cheklangan</b>. O'qish to'lovidagi farqni kim qoplashini universitet hal qiladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> O'rin faqat mahalliy talaba to'lovini ([[home fee]]) qoplasa, xalqaro to'lov ([[international fee]]) bilan farqni kim to'lashi noma'lum bo'lishi mumkin. Bunday e'lonni <i>“xalqaro talaba uchun to'liq moliyalashtirilgan”</i> deb hisoblamang.</div>
<div class="box warn">O'tgan yilgi stipendiya summasini bu yil uchun kafolat deb yozmang.</div>
<div class="srcs">Manba: {UKRI}; {LEEDS}. {HOL}.</div>""",
             take="Buyuk Britaniyada asosiy savol: xalqaro to'lov farqini kim to'laydi? Javob yozma bo'lishi kerak.",
             task="<ul><li>UKRI va universitet sahifalarini yonma-yon o'qing.</li><li>Xalqaro to'lov holatini tekshiring.</li><li>Farq haqida universitetga xat yozing.</li></ul><p><b>O'zingizga savol:</b> mahalliy va xalqaro to'lov farqini kim to'laydi?</p>",
             ph="E'lon: ... ; qoplaydi: home fee / international fee ; xatdagi savol: ..."),
        dict(t="Yevropa: maoshli PhD va MSCA", short="Yevropa", min=30, kind="🇪🇺 Tizim", ic="daad",
             hook="Yevropada ba'zi PhD o'rinlari <b>ish shartnomasi</b> bilan beriladi. Bunda soliq, sug'urta va huquqlaringiz stipendiyadagidan boshqacha bo'ladi.",
             body=f"""<p>MSCA doktorlik tarmoqlariga istalgan mamlakat fuqarosi topshira oladi, lekin mobillik qoidasi bor: ishga olinishdan oldingi 36 oyning 12 oyidan ko'prog'ini o'sha mamlakatda yashab yoki ishlab o'tkazmagan bo'lish kerak. O'rinlar EURAXESS kabi saytlarda e'lon qilinadi.</p>
<p>Yashash va mobillik to'lovlari <b>soliqdan oldingi</b> ([[gross]]) yoki <b>qo'lga tegadigan</b> ([[net]]) summa ekanini va o'sha mamlakat soliqlarini alohida tekshiring. Ish beruvchi, qabul qiluvchi tashkilot, diplom beradigan universitet va shartnoma muddatini farqlang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> E'londagi summa soliqdan oldingi bo'lsa, uni bank hisobingizga tushadigan pul deb hisoblash xato. Yashash narxi ham shaharga qarab farq qiladi.</div>
<div class="box warn">MSCA tarmog'ining mablag' tanlovi muddatini doktorantning ishga ariza muddati bilan adashtirmang.</div>
<div class="srcs">Manba: {MSCA}; {EURAXESS}. {HOL}.</div>""",
             take="Maoshli PhD da soliqdan oldingi va qo'lga tegadigan summa, soliq va shartnoma muddati alohida tekshiriladi.",
             task="<ul><li>EURAXESS dagi 3 ta e'lonni solishtiring.</li><li>Mobillik qoidasi va diplom kim tomonidan berilishini belgilang.</li><li>Summa soliqdan oldingimi yoki keyingimi, shu haqda savol yozing.</li></ul><p><b>O'zingizga savol:</b> aynan qayerga ariza berasiz?</p>",
             ph="E'lon 1: ..., ish beruvchi ..., diplom ..., summa (soliqdan oldin yoki keyin?) ... ; mobillik: ✓"),
        dict(t="Xarajatlar va dastlabki pul", short="Xarajat", min=30, kind="🧮 Hisob", ic="hourglass",
             hook="Yaxshi stipendiya bilan ham birinchi oylar qiyin kechishi mumkin: depozit, viza va yo'l puli <b>birinchi stipendiyadan oldin</b> to'lanadi.",
             body=f"""<p>Hisobga oling: viza, kerak bo'lsa ATAS, yo'l, ijara depoziti, birinchi oy ijarasi, ko'chish, tibbiy yig'im, sug'urta, bola parvarishi, jihozlar va valyuta ayirboshlash.</p>
<p>Stipendiya ko'pincha oyma-oy yoki choraklik to'lanadi, shuning uchun dastlabki naqd pulni alohida hisoblang. Narxlarni rasmiy sahifadan yoki yozma taklifdan oling.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Oylik daromad 100 birlik, xarajat 95 birlik: har oy 5 birlik qoladi. Ammo boshida 250 birlik depozit to'lash uchun pul yetmaydi.</div>
<div class="box warn"><i>“Yarim stavka ishlab olaman”</i> degan rejani viza ish huquqini tekshirmasdan hisobga qo'shmang.</div>
<div class="srcs">Manba: {VISA}. {HOL}.</div>""",
             take="Uch holat (eng kam, kutilgan, qiyin) va bir martalik xarajatlar bilan dastlabki 60 kunlik naqd pul hisoblanadi.",
             task="<ul><li>Eng kam, kutilgan va qiyin holat uchun hisob qiling.</li><li>Bir martalik xarajatlarni qo'shing.</li><li>3 oylik zaxira qanchaga teng ekanini ko'ring.</li></ul><p><b>O'zingizga savol:</b> birinchi 60 kunga naqd pulingiz yetadimi?</p>",
             ph="Oylik daromad ..., xarajat ... ; bir martalik: viza ..., depozit ..., yo'l ... ; 60 kunlik naqd: ..."),
        dict(t="Taklif shartlarini o'qish", short="Shartlar", min=25, kind="📑 Hujjat", ic="memo",
             hook="Moliya taklifi akademik taklif bilan birga yoki undan keyin kelishi mumkin. Ikkalasini <b>alohida</b> o'qing.",
             body=f"""<p>Moliya xatida qarang: summa, qachon to'lanadi, qancha muddat, o'qishdagi yutuq talablari, dars berish majburiyati, to'lov toifasi, yillik ko'rik, o'qishni tashlasangiz nima bo'ladi va boshlashni kechiktirish qoidasi.</p>
<p>Ish shartnomasi va stipendiya kelishuvi har xil hujjatlar: ikkalasini ham rasmiy shart sifatida o'qing.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Akademik taklif shartli bo'lsa, moliya boshlanadigan sana avtomatik tasdiqlanmasligi mumkin. Professorning <i>“pul bor”</i> degan gapi moliya bo'limining xati o'rnini bosmaydi.</div>
<div class="box warn">Og'zaki va'dalarni byudjetga kafolatlangan pul sifatida yozmang.</div>""",
             take="Har tushunarsiz band uchun savol yozing va yozma javobni saqlang.",
             quiz=[("Mahalliy talaba to'lovini qoplaydigan o'rin xalqaro talaba uchun ham avtomatik to'liq moliyalashtirilgan bo'ladi.", "n", "Noto'g'ri: xalqaro to'lov farqini kim qoplashi alohida tekshiriladi."),
                   ("MSCA doktorlik tarmog'iga istalgan mamlakat fuqarosi topshira oladi.", "t", "To'g'ri, lekin mobillik qoidasi bor."),
                   ("E'londagi soliqdan oldingi summa bank hisobingizga to'liq tushadi.", "n", "Noto'g'ri: soliq va ajratmalar ushlab qolinadi."),
                   ("Og'zaki moliya va'dasi byudjetda kafolatlangan daromad sifatida yoziladi.", "n", "Noto'g'ri: faqat yozma tasdiq hisobga olinadi.")],
             task="<ul><li>Taklif bo'yicha nazorat ro'yxatini to'ldiring.</li><li>Har tushunarsiz bandga savol yozing.</li><li>Yozma javobni saqlang.</li></ul><p><b>O'zingizga savol:</b> moliya qachondan va qaysi hujjat bilan kuchga kiradi?</p>",
             ph="Summa ..., qachon to'lanadi ..., muddat ..., dars berish ..., o'qishni tashlasa ... ; savol: ..."),
        dict(t="Moliyaviy qaror", short="Qaror", min=25, kind="⚖️ Qaror", ic="scroll",
             hook="Moliyaviy bo'shliq ilmiy imkoniyat va hayot sharoiti bilan birga baholanadi. <b>Eng kuchli rahbar ham</b> pul yetishmovchiligini hal qilib bermaydi.",
             body=f"""<p>Baholang: qo'lga tegadigan pul oqimi, o'qish to'lovidagi farq, dastlabki xarajat, oila a'zolari, tibbiy xarajat, inflyatsiya, stipendiya uzaytirilmasligi xavfi va yashash narxi. Maqsad: <b>3–4 yil xotirjam ilmiy ishlashga</b> imkon beradigan shartni tanlash.</p>
<p>Takliflarni solishtirganda ilmiy moslik, rahbarlik, moliyaning ishonchliligi va turmush sharoitini birga ko'ring.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> A taklif: kuchli rahbar, lekin katta pul yetishmovchiligi. B taklif: yaxshi laboratoriya va moliyaviy jihatdan xavfsizroq. B ni tanlasangiz, ilmiy maqsaddan voz kechgan bo'lmaysiz.</div>
<div class="box warn">Moliyaviy rejasiz taklifni qabul qilsangiz, qaytarib bo'lmaydigan xarajatlarga duch kelishingiz mumkin.</div>""",
             take="Eng yomon holat hisoblangan va zaxira reja yozilgan bo'lsa, qaror asosli.",
             task="<ul><li>3 ta taklifni yoki 3 ta real imkoniyatni solishtiring.</li><li>Eng yomon holatni hisoblang.</li><li>Qaror daftariga shartli tavsiya yozing.</li></ul><p><b>O'zingizga savol:</b> moliya topilmasa, bu ariza bo'yicha nima qilasiz?</p>",
             ph="A: bo'shliq ..., B: ..., C: ... ; eng yomon holat: ... ; qaror: ..."),
    ],
    tool=dict(id="hisob", short="Hisob", h2="Moliyaviy bo'shliq hisoblagichi", sub="Bir xil valyutada oylik va bir martalik xarajatlarni kiriting: 12 oylik bo'shliq va boshidagi naqd pul ehtiyoji chiqadi.",
              h3="12 oylik pul oqimi", tag="5 maydon", ic="money", btn="Hisobni saqlash", badge="Hisobchi", min=4,
              pre=f"""<div class="fld"><label>Hisoblagich <small>bir xil valyutada</small></label><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px"><input id="fI" type="number" min="0" placeholder="Oylik daromad (qo'lga tegadigan)" style="{INP}"><input id="fC" type="number" min="0" placeholder="Oylik xarajat" style="{INP}"><input id="fO" type="number" min="0" placeholder="Bir martalik xarajat" style="{INP}"><input id="fD" type="number" min="0" max="6" placeholder="Birinchi to'lovgacha necha oy" style="{INP}"></div><div id="fOut" class="out" style="white-space:normal">Raqamlarni kiriting.</div></div>""",
              fields=[dict(k="paket", label="Paket va manba", ph="... universiteti, studentship, havola ..."),
                      dict(k="qamrov", label="Nimalarni qoplaydi", type="area", ph="To'lov ..., stipendiya ..., sug'urta ..., safar ..."),
                      dict(k="birm", label="Bir martalik xarajatlar", type="area", ph="Viza ..., ATAS ..., yo'l ..., depozit ..."),
                      dict(k="breja", label="Zaxira reja", type="area", ph="Bo'shliq yopilmasa: ..."),
                      dict(k="qaror", label="Moliyaviy xulosa", type="select", opts=["Moliya yetarli", "Kichik bo'shliq bor, zaxira reja tayyor", "Katta bo'shliq, qabul qilmayman", "Yozma tasdiq kutilmoqda"])]),
    check=dict(h2="M6 nazorati", sub="Moliyaviy qarordan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["O'qish to'lovi, stipendiya, yig'im va xarajatlar alohida yozilgan.", "Moliya muddati va shartlari aniq.", "Xalqaro talaba holati manba bilan tekshirilgan.",
                      "Bir martalik xarajatlar va oila ehtiyojlari hisoblangan.", "Soliqdan oldingi va qo'lga tegadigan summa farqi aniqlangan.",
                      "Ish daromadi viza shartlarini tekshirmasdan qo'shilmagan.", "Moliyaviy bo'shliq va zaxira reja hisoblangan."]),
    art_title="Moliya taqqoslash va 12 oylik pul oqimi", art_short="Moliya",
    art=[("Paket", ["paket", "a1"]), ("Qamrov", ["qamrov", "a2", "a3"]), ("Bir martalik xarajatlar", ["birm", "a4"]), ("Hisob", ["fcalc"]),
         ("Taklif shartlari", ["a5"]), ("Qaror va zaxira reja", ["a6", "breja", "qaror"])],
    tip="Byudjetga faqat yozma tasdiqlangan pulni yozing. Qolganini zaxira reja ustuniga qo'ying.",
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
    else if (year >= 0) { cls = "chk"; tag = "Yil bo\\u02bbyi yetadi, lekin boshida naqd pul kerak"; }
    else { cls = "no"; tag = "12 oyda pul yetmaydi"; }
    var txt = "12 oy: " + (year >= 0 ? "+" : "") + fmt(year) + " (daromad " + fmt(I * 12) + ", xarajat " + fmt(C * 12 + O) + "). Birinchi to\\u02bblovgacha kerakli naqd pul: " + fmt(start) + ". " + tag + ".";
    o.innerHTML = "<span class=\\"pill " + cls + "\\">" + KG.esc(tag) + "</span> " + KG.esc(txt);
    KG.S.notes.fcalc = txt; KG.S.notes.f_in = [I, C, O, D].join("|"); KG.save();
  }
  if (KG.S.notes.f_in) { var p = String(KG.S.notes.f_in).split("|"); ids.forEach(function (id, i) { if (p[i] && p[i] !== "0") document.getElementById(id).value = p[i]; }); }
  ids.forEach(function (id) { document.getElementById(id).addEventListener("input", run); });
  run();
} };""",
)
