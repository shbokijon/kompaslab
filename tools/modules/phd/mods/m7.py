from common import LEEDS, UKRI, UKRIEXP, HOL, STD

INP = "min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"

MOD = dict(
    title="Ariza, intervyu va qaror",
    desc="PhD Lab M7: topshirishdan oldingi sifat nazorati, tavsiya va portal kuzatuvi, ilmiy intervyu, taqdimot va qiyin savollar, taklif, kutish ro'yxati va rad javobi, yakuniy qaror. Natija: topshirilgan arizalar reyestri, intervyu savollari banki va qaror jadvali.",
    lead="Yaxshi hujjatlar ham noto'g'ri fayl yoki o'tkazib yuborilgan tavsiya sabab yo'qolishi mumkin. Bu modulda arizani nazorat ostida topshirasiz, ilmiy intervyuga tayyorlanasiz va takliflarni yozma shartlar asosida solishtirasiz.",
    hero="calendar", weeks="2–4", next="M8 Qabuldan keyingi tayyorgarlik va birinchi 90 kun", next_href="phd-lab-o.html?m=8",
    goals=[("shield", "Arizalar reyestri", "portal tasdig'i, raqam va holat bilan"),
           ("miya", "Intervyu savollari banki", "10 ta savol, dalil bilan javoblar"),
           ("scroll", "Qaror jadvali", "taklif shartlari va hal bo'lmagan xavflar")],
    warn="PhD intervyusi har universitetda boshqacha: taqdimot, texnik intervyu yoki rahbar bilan suhbat bo'lishi mumkin. Portal va dastur qoidasi ustun. Intervyu javoblari tayyor matn emas: ular sizning ishingizdagi dalillarga tayanadi.",
    lessons=[
        dict(t="Topshirishdan oldingi sifat nazorati", short="Nazorat", min=25, kind="✅ Tekshiruv", ic="shield",
             hook="Yaxshi hujjatlar to'plami noto'g'ri portal yoki noto'g'ri fayl sabab kechikishi mumkin. Bitta ro'yxat buni oldini oladi.",
             body=f"""<p>Bitta nazorat ro'yxati bilan tekshiring: dastur yo'riqnomasi, fayl turlari, tavsiya so'rovlari, ariza to'lovi, aloqa ma'lumoti, muddat va vaqt mintaqasi, bayonot va yakuniy “yuborish” tasdig'i.</p>
<p>Portaldagi “saqlangan qoralama” va “yuborilgan” holatlarini ajrating. Tasdiq xati, ariza raqami va kvitansiyani saqlang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Ariza yuborilgan, lekin tavsiya portalida tavsiya beruvchi hali “kutilmoqda” holatida. Nima muddatgacha majburiy ekanini qabul tashkiloti yo'riqnomasi belgilaydi.</div>
<div class="box warn">Ekran surati arizaning qabul qilinganini isbotlamasligi mumkin: portal holatini tekshiring.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="12 bandli nazorat, ochib ko'rilgan PDF lar va saqlangan tasdiq: shundan keyingina ariza “yuborilgan”.",
             task="<ul><li>12 bandli nazoratdan o'ting.</li><li>Fayl nomlari va PDF larni ochib ko'ring.</li><li>Yuborish tasdig'ini saqlang.</li></ul><p><b>O'zingizga savol:</b> arizangizni boshqa odam ham shu ro'yxat bo'yicha tekshira oladimi?</p>",
             ph="Ariza 1: yuborildi ..., raqam ..., tasdiq xati ✓, tavsiyalar: 2/3"),
        dict(t="Tavsiya va portal kuzatuvi", short="Kuzatuv", min=20, kind="🔔 Kuzatuv", ic="bell",
             hook="Tavsiya jarayonini hurmat bilan kuzatish mumkin, lekin bosim o'tkazish emas.",
             body=f"""<p>Tavsiya so'rovi kelganini, muddatni, spam papkasini va portal holatini tekshiring. Bir mavzuda qayta-qayta xat yubormang; kerak bo'lsa, qabul bo'limidan tavsiya beruvchini almashtirish tartibini so'rang. Tavsiya mazmuni maxfiy bo'lishi mumkin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Tavsiya beruvchi “yubordim” degan, portal esa “qabul qilinmagan” ko'rsatmoqda: qabul bo'limidan professional aniqlik so'raladi.</div>
<div class="box warn">Tavsiya beruvchining maxfiy xatiga aralashmang va tahrir talab qilmang.</div>""",
             take="Har tavsiya beruvchi uchun holat, bitta xushmuomala eslatma rejasi va zaxira yo'l.",
             task="<ul><li>Har tavsiya beruvchi holatini yozing.</li><li>Bitta xushmuomala eslatma rejasini tuzing.</li><li>Zaxira yo'lni tekshiring.</li></ul><p><b>O'zingizga savol:</b> qaysi tekshiruv portalga, qaysisi tavsiya beruvchiga tegishli?</p>",
             ph="1) ... — so'rov ..., holat: qabul qilindi ; 2) ... — kutilmoqda, eslatma ..."),
        dict(t="Ilmiy intervyu", short="Intervyu", min=35, kind="🎙 Intervyu", ic="miya",
             hook="PhD intervyusida fakt yodlashdan ko'ra savolingizni ilmiy himoya qila olishingiz tekshiriladi.",
             body=f"""<h4>Tayyorlanadi</h4>
<ul><li>90 soniyalik tadqiqot qisqachasi.</li><li>Bo'shliqni asoslash.</li><li>Usul tanlovi va muqobillari.</li><li>Usul ishlamay qolsa nima bo'ladi.</li><li>Vaqt rejasi.</li><li>Moslik va moliya savollari.</li></ul>
<p><span lang="en">“I don't know yet, but I would test…”</span> degan javob to'qilgan aniqlikdan kuchliroq. Intervyu shakli aynan dastur ko'rsatmasiga bog'liq.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Savol: <span lang="en">“Your method fails on noisy data. What would you do?”</span> Kuchli javob tuzilmasi: shovqin modeli, asos, sezgirlik tahlili, noaniqlik, zaxira usul va to'xtash mezoni.</div>
<div class="box warn">“Har savolga 100% ishonch bilan javob” uslubi ilmiy noaniqlikka zid.</div>""",
             take="Savollar banki va ikki marta yozib olingan mashq intervyusi zaif usul joylarini ochadi.",
             quiz=[("Portaldagi “saqlangan qoralama” arizaning yuborilganini bildiradi.", "n", "Noto'g'ri: yuborish tasdig'i va ariza raqami kerak."),
                   ("Intervyuda “hali bilmayman, lekin shunday tekshirgan bo'lardim” degan javob qabul qilinadi.", "t", "To'g'ri: bu ilmiy noaniqlikni ochiq tan olish."),
                   ("Professor “ha” desa, bu shartsiz qabul.", "n", "Noto'g'ri: rasmiy taklif va shartlar alohida keladi."),
                   ("Qaror qilingach, rad etilgan takliflarga o'z vaqtida javob berish professional odob.", "t", "To'g'ri: boshqa nomzodlar ham kutmoqda.")],
             task="<ul><li>10 ta savol banki tuzing.</li><li>2 ta mashq intervyusini yozib olib baholang.</li><li>3 ta zaif usul joyini tuzating.</li></ul><p><b>O'zingizga savol:</b> savolingiz muvaffaqiyatsiz chiqsa ham ilmiy hissa qoladimi?</p>",
             ph="1) Nega bu savol? — ... 2) Usul ishlamasa? — ... 3) Nega shu rahbar? — ..."),
        dict(t="Taqdimot va qiyin savollar", short="Taqdimot", min=30, kind="🖥 Taqdimot", ic="chart",
             hook="Ba'zi intervyular ilmiy taqdimot yoki oldingi dissertatsiyangiz muhokamasini so'raydi.",
             body=f"""<p>5–7 slaydda: muammo, dalil, usul, hissa, cheklov va moslik. Slaydda o'qib beriladigan matn emas, qarorga yordam beradigan diagramma bo'lsin.</p>
<p>Qiyin savolda avval savolni aniqlashtiring, keyin mavjud dalil chegarasini ayting.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> “Nega aynan shu rahbar?” savoliga reyting emas, 2 ta real ish va 1 ta kelajakdagi moslik bilan javob bering.</div>
<div class="box warn">Natijani kafolatlash va boshqa laboratoriyani yomonlash professional emas.</div>""",
             take="5 slayd, 5 ta qarshi savol va har biriga dalil chegarasi bilan javob.",
             task="<ul><li>5 slaydlik reja yozing.</li><li>5 ta qarshi savolni yozib mashq qiling.</li><li>Tushunarsiz joylarni qayta chizing.</li></ul><p><b>O'zingizga savol:</b> qaysi cheklovni ochiq tan olasiz?</p>",
             ph="Slaydlar: 1) muammo 2) ... ; Qarshi savollar: ... ; Tan olinadigan cheklov: ..."),
        dict(t="Taklif, kutish ro'yxati va rad javobi", short="Taklif", min=25, kind="📬 Natija", ic="bell",
             hook="Qabul natijasi har doim oddiy “ha/yo'q” emas: shartli taklif, kutish ro'yxati va moliya qarori alohida kelishi mumkin.",
             body=f"""<p>Farqlang: shartli taklif ([[conditional offer]]), stipendiya qarori, zaxira yoki kutish ro'yxati ([[waitlist]]), loyihaga biriktirish, daraja holati va qabul qilish muddati.</p>
<p>Rad javobidan o'rganish jurnalini yozing; fikr so'rash me'yorida bo'lsin. Boshqa grantni kutayotganda depozit yoki taklifni qabul qilish majburiyati qachon kuchga kirishini tekshiring.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> A taklifga javob muddati 10 kun, B moliya hali noaniq. Muddatni uzaytirish mumkinmi, faqat tegishli tashkilot siyosati va yozma javob bilan aniqlanadi.</div>
<div class="box warn">“Professor ha dedi” ni shartsiz qabul deb olmang.</div>
<div class="srcs">Manba: {UKRI}. {HOL}.</div>""",
             take="Har taklif uchun shartlar matritsasi va muddat; rad javobi uchun 30 kunlik reja.",
             task="<ul><li>Har taklif uchun shartlar matritsasini tuzing.</li><li>Muddatlarni yozing.</li><li>Rad javobi uchun 30 kunlik bo'shliqni yopish rejasini yozing.</li></ul><p><b>O'zingizga savol:</b> aynan qaysi bandni bajarmasangiz, taklif bekor bo'ladi?</p>",
             ph="Taklif A: shartlar ..., javob muddati ... ; B: ... ; Rad: sabab ..., 30 kunlik reja ..."),
        dict(t="Yakuniy qaror", short="Qaror", min=25, kind="⚖️ Qaror", ic="scroll",
             hook="Qabul qarorini reputatsiya emas, ilmiy moslik, moliya va hayot sharoitining birikmasi hal qiladi.",
             body=f"""<p>Vaznli ballar faqat murosalarni ochadi, tanlovni siz uchun qilmaydi. Qaytarib bo'lmaydigan xarajatlardan oldin yozma moliya, qabul, yashash rejasi va oila ehtiyojlarini tasdiqlang. Qaror qilgach, rad etilgan takliflarga o'z vaqtida javob bering.</p>
<p>Rahbarlik va qo'llab-quvvatlash bo'yicha UKRI kutilmalar bayonini taklif shartlari bilan solishtirish foydali.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> “Kafedra reytingi eng yuqori” o'rniga “bu rahbarda mos ma'lumot, to'liq moliya va qo'llab-quvvatlovchi jamoa bor” asosli qaror bo'lishi mumkin.</div>
<div class="box warn">Noaniqlikni yashirib, umumiy ballni faktga aylantirmang.</div>
<div class="srcs">Manba: {UKRIEXP}. {HOL}.</div>""",
             take="4 mezonli qaror xati, hal bo'lmagan xavflar va qabul / kechiktirish / rad qadamlari.",
             task="<ul><li>4 mezonli qaror xatini yozing.</li><li>Qolgan hal bo'lmagan xavflarni belgilang.</li><li>Qabul, kechiktirish yoki rad qadamlarini rejalang.</li></ul><p><b>O'zingizga savol:</b> 2 yil o'tgach ham bu qarorni asoslay olasizmi?</p>",
             ph="Ilmiy moslik ..., moliya ..., rahbarlik ..., hayot sharoiti ... → qaror: ..."),
    ],
    tool=dict(id="kalendar", short="Kalendar", h2="Teskari kalendar", sub="Ariza muddatini kiriting: nazorat nuqtalari orqaga qarab hisoblanadi. Keyin reyestrni to'ldiring.",
              h3="Arizalar reyestri", tag="5 maydon", ic="calendar", btn="Reyestrni saqlash", badge="Topshiruvchi", min=4,
              pre=f"""<div class="fld"><label for="dD">Ariza muddati <small>portal yopilish sanasi</small></label><input id="dD" type="date" style="{INP}"><div id="dOut" class="out" style="white-space:normal">Sanani tanlang.</div></div>""",
              fields=[dict(k="ariza", label="Arizalar va raqamlar", type="area", ph="1) ... — yuborildi ..., raqam ... ; 2) ..."),
                      dict(k="tavs", label="Tavsiyalar holati", type="area", ph="... — qabul qilindi ; ... — kutilmoqda"),
                      dict(k="bank", label="Intervyu savollari banki", type="area", ph="1) ... — javob tayanchi: ... "),
                      dict(k="taklif", label="Takliflar va shartlar", type="area", ph="A: ..., B: ..."),
                      dict(k="qaror", label="Qaror", type="select", opts=["Hali taklif yo'q", "Taklifni qabul qilaman", "Kechiktiraman", "Rad etaman, keyingi sikl"])]),
    check=dict(h2="M7 nazorati", sub="Yakuniy qarordan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Har ariza portal tasdig'i va holati bilan.", "Fayl nomlari va versiyalari tekshirilgan.", "Tavsiyalar holati portalda tekshirilgan.",
                      "Intervyu savollari dalil bilan tayyorlangan.", "Taklif moliya va shartlar bo'yicha tekshirilgan.",
                      "Rad javobi uchun B reja yozilgan.", "Rad etilgan takliflarga javob berish rejasi bor."]),
    art_title="Arizalar reyestri, intervyu banki va qaror jadvali", art_short="Qaror",
    art=[("Nazorat nuqtalari", ["dcalc"]), ("Arizalar", ["ariza", "a1"]), ("Tavsiyalar", ["tavs", "a2"]), ("Intervyu", ["bank", "a3", "a4"]),
         ("Takliflar", ["taklif", "a5"]), ("Qaror", ["a6", "qaror"])],
    tip="Har topshirilgan arizaning tasdiq xatini alohida papkaga saqlang. Keyinroq “yubordimmi?” degan savolga bir daqiqada javob topasiz.",
    sources=f"{LEEDS}; {UKRI}; {UKRIEXP}. {STD}",
    js="""window.KGTool = { init: function () {
  var d = document.getElementById("dD"), o = document.getElementById("dOut");
  var steps = [[42, "Tavsiya beruvchilarga so\\u02bbrov va rasmiy tarjima"], [28, "Ilmiy loyiha taklifi v3 va bayonnoma"], [14, "Hujjatlar to\\u02bbliq, nazorat ro\\u02bbyxati"], [7, "Topshirish (7 kunlik zaxira)"], [0, "Portal yopiladi"]];
  function run() {
    if (!d.value) { o.textContent = "Sanani tanlang."; return; }
    var end = new Date(d.value + "T12:00:00"), lines = [];
    steps.forEach(function (s) { var t = new Date(end.getTime() - s[0] * 864e5); lines.push(t.toLocaleDateString("uz-UZ") + ": " + s[1]); });
    o.innerHTML = lines.map(function (l) { return KG.esc(l); }).join("<br>");
    KG.S.notes.dcalc = lines.join("\\n"); KG.S.notes.d_in = d.value; KG.save();
  }
  if (KG.S.notes.d_in) d.value = KG.S.notes.d_in;
  d.addEventListener("input", run); d.addEventListener("change", run);
  run();
} };""",
)
