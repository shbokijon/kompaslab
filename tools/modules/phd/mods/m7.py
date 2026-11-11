from common import LEEDS, UKRI, UKRIEXP, HOL, STD

INP = "min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"

MOD = dict(
    title="Ariza, intervyu va qaror",
    desc="PhD Lab M7: arizani topshirishdan oldingi tekshiruv, tavsiya va portalni kuzatish, ilmiy intervyu, taqdimot va qiyin savollar, taklif, kutish ro'yxati va rad javobi, yakuniy qaror. Natija: topshirilgan arizalar ro'yxati, intervyu savollari to'plami va qaror jadvali.",
    lead="Puxta tayyorlangan hujjatlar ham <b>noto'g'ri fayl</b> yoki kelmay qolgan tavsiya sabab yo'qolishi mumkin. Bu modulda arizani tekshirib topshirasiz, ilmiy intervyuga tayyorlanasiz va takliflarni yozma shartlari bo'yicha solishtirasiz.",
    hero="calendar", weeks="2–4", next="M8 Qabuldan keyingi tayyorgarlik va birinchi 90 kun", next_href="phd-lab-o.html?m=8",
    goals=[("shield", "Arizalar ro'yxati", "portal tasdig'i, raqam va holat bilan"),
           ("miya", "Intervyu savollari to'plami", "10 ta savol, javoblar dalilga tayangan"),
           ("scroll", "Qaror jadvali", "taklif shartlari va hal bo'lmagan xavflar")],
    warn="PhD intervyusi har universitetda boshqacha o'tadi: taqdimot, texnik intervyu yoki rahbar bilan suhbat bo'lishi mumkin. Portal va dastur qoidasi asosiy manba. Intervyu javoblarini yodlab olmang: ular o'z ishingizdagi dalillarga tayanadi.",
    lessons=[
        dict(t="Topshirishdan oldingi tekshiruv", short="Tekshiruv", min=25, kind="✅ Tekshiruv", ic="shield",
             hook="Puxta tayyorlangan hujjatlar noto'g'ri portal yoki noto'g'ri fayl sabab kechikib qolishi mumkin. <b>Bitta tekshiruv ro'yxati</b> buning oldini oladi.",
             body=f"""<p>Bitta ro'yxat bo'yicha tekshiring: dastur yo'riqnomasi, fayl turlari, tavsiya so'rovlari, ariza to'lovi, aloqa ma'lumotlari, muddat va vaqt mintaqasi, bayonot va oxirgi <i>“yuborish”</i> tasdig'i.</p>
<p>Portaldagi <b>“saqlangan qoralama”</b> bilan <b>“yuborilgan”</b> holatini farqlang. Tasdiq xati, ariza raqami va to'lov chekini saqlab qo'ying.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Ariza yuborilgan, lekin tavsiya portalida tavsiya beruvchi hali <i>“kutilmoqda”</i> holatida turibdi. Muddatgacha nima majburiy ekanini qabul tashkilotining yo'riqnomasi belgilaydi.</div>
<div class="box warn">Ekran surati ariza qabul qilinganini isbotlamasligi mumkin: portaldagi holatni tekshiring.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="12 bandli tekshiruv, ochib ko'rilgan PDF lar va saqlangan tasdiq: shundan keyingina ariza yuborilgan hisoblanadi.",
             task="<ul><li>12 bandli tekshiruvdan o'ting.</li><li>Fayl nomlarini va PDF larni ochib ko'ring.</li><li>Yuborish tasdig'ini saqlang.</li></ul><p><b>O'zingizga savol:</b> arizangizni boshqa odam ham shu ro'yxat bo'yicha tekshira oladimi?</p>",
             ph="Ariza 1: yuborildi ..., raqam ..., tasdiq xati ✓, tavsiyalar: 2/3"),
        dict(t="Tavsiya va portalni kuzatish", short="Kuzatuv", min=20, kind="🔔 Kuzatuv", ic="bell",
             hook="Tavsiya jarayonini odob bilan kuzatib borish mumkin, lekin tavsiya beruvchiga <b>bosim o'tkazmang</b>.",
             body=f"""<p>Tavsiya so'rovi yetib borganini, muddatni, spam papkasini va portal holatini tekshiring. Bir mavzuda qayta-qayta xat yubormang. Kerak bo'lsa, qabul bo'limidan tavsiya beruvchini almashtirish tartibini so'rang. Tavsiya mazmuni sizga ko'rsatilmasligi mumkin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Tavsiya beruvchi <i>“yubordim”</i> degan, portal esa <i>“qabul qilinmagan”</i> deb ko'rsatyapti. Bunday holda qabul bo'limiga odob bilan yozing.</div>
<div class="box warn">Tavsiya beruvchining maxfiy xatiga aralashmang va uni o'zgartirishni so'ramang.</div>""",
             take="Har tavsiya beruvchining holati, bitta odobli eslatma va zaxira yo'l yozib qo'yiladi.",
             task="<ul><li>Har tavsiya beruvchining holatini yozing.</li><li>Bitta odobli eslatma xatini rejalang.</li><li>Zaxira yo'lni tekshiring.</li></ul><p><b>O'zingizga savol:</b> nimani portalda, nimani tavsiya beruvchidan tekshirasiz?</p>",
             ph="1) ...: so'rov ..., holat: qabul qilindi ; 2) ...: kutilmoqda, eslatma ..."),
        dict(t="Ilmiy intervyu", short="Intervyu", min=35, kind="🎙 Intervyu", ic="miya",
             hook="PhD intervyusida yodlangan faktlardan ko'ra <b>savolingizni ilmiy himoya qila olishingiz</b> tekshiriladi.",
             body=f"""<h4>Nimaga tayyorlanish kerak</h4>
<ul><li>Tadqiqotingizning 90 soniyalik qisqa bayoni.</li><li>Bo'shliq borligini asoslash.</li><li>Nega shu usul va qanday muqobillar bor.</li><li>Usul ishlamasa nima qilasiz.</li><li>Ish rejasi.</li><li>Moslik va moliya haqidagi savollar.</li></ul>
<p><i><span lang="en">“I don't know yet, but I would test…”</span></i> degan javob o'ylab topilgan aniq javobdan yaxshiroq. Intervyu qanday o'tishini dastur yo'riqnomasi belgilaydi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Savol: <i><span lang="en">“Your method fails on noisy data. What would you do?”</span></i> Kuchli javob tartibi: shovqin qanday ekani, taqqoslash nuqtasi, sezgirlik tahlili, noaniqlik, zaxira usul va qachon to'xtash.</div>
<div class="box warn">Har savolga <i>“100% ishonch bilan”</i> javob berish ilmiy noaniqlikni inkor qilgandek eshitiladi.</div>""",
             take="Savollar to'plami va ikki marta yozib olingan mashq intervyusi usuldagi zaif joylarni ko'rsatadi.",
             quiz=[("Portaldagi “saqlangan qoralama” ariza yuborilganini bildiradi.", "n", "Noto'g'ri: yuborilganini tasdiq xati va ariza raqami ko'rsatadi."),
                   ("Intervyuda “hali bilmayman, lekin shunday tekshirgan bo'lardim” degan javob qabul qilinadi.", "t", "To'g'ri: bu noaniqlikni ochiq tan olish."),
                   ("Professor “ha” desa, qabul shartsiz hisoblanadi.", "n", "Noto'g'ri: rasmiy taklif va uning shartlari alohida keladi."),
                   ("Qaror qilgach, rad etilgan takliflarga o'z vaqtida javob berish kerak.", "t", "To'g'ri: boshqa nomzodlar ham javob kutmoqda.")],
             task="<ul><li>10 ta savoldan iborat to'plam tuzing.</li><li>2 ta mashq intervyusini yozib olib baholang.</li><li>Usuldagi 3 ta zaif joyni tuzating.</li></ul><p><b>O'zingizga savol:</b> savolingiz kutilgan natijani bermasa ham, ilmiy hissa qoladimi?</p>",
             ph="1) Nega bu savol? ... 2) Usul ishlamasa? ... 3) Nega shu rahbar? ..."),
        dict(t="Taqdimot va qiyin savollar", short="Taqdimot", min=30, kind="🖥 Taqdimot", ic="chart",
             hook="Ba'zi intervyularda <b>ilmiy taqdimot</b> yoki oldingi dissertatsiyangizni muhokama qilish so'raladi.",
             body=f"""<p>5–7 slaydda: muammo, dalil, usul, hissa, cheklov va moslik. Slaydda uzun matn bo'lmasin; asosiy fikrni chizma yoki jadval bilan ko'rsating.</p>
<p>Qiyin savol berilsa, avval savolni aniqlashtirib oling, keyin qo'lingizdagi dalil <b>qayergacha yetishini</b> ayting.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> <i>“Nega aynan shu rahbar?”</i> savoliga rahbarning 2 ta real ishini va kelajakdagi bitta umumiy yo'nalishni aytib javob bering; reytingni tilga olish shart emas.</div>
<div class="box warn">Natijani oldindan kafolatlash yoki boshqa laboratoriyani yomonlash nojo'ya ko'rinadi.</div>""",
             take="5 ta slayd, 5 ta qarshi savol va har biriga dalil qayergacha yetishini aytadigan javob.",
             task="<ul><li>5 slaydlik reja yozing.</li><li>5 ta qarshi savolni yozib, mashq qiling.</li><li>Tushunarsiz slaydlarni qayta chizing.</li></ul><p><b>O'zingizga savol:</b> qaysi cheklovni ochiq tan olasiz?</p>",
             ph="Slaydlar: 1) muammo 2) ... ; Qarshi savollar: ... ; Tan olinadigan cheklov: ..."),
        dict(t="Taklif, kutish ro'yxati va rad javobi", short="Taklif", min=25, kind="📬 Natija", ic="bell",
             hook="Natija har doim oddiy <i>“ha”</i> yoki <i>“yo'q”</i> bo'lmaydi: shartli taklif, kutish ro'yxati va moliya qarori alohida kelishi mumkin.",
             body=f"""<p>Farqlang: shartli taklif ([[conditional offer]]), stipendiya qarori, kutish ro'yxati ([[waitlist]]), loyihaga biriktirish, daraja holati va taklifni qabul qilish muddati.</p>
<p>Rad javobidan keyin nimalarni o'rganganingizni yozib boring; izoh so'rasangiz, bir marta va qisqa so'rang. Boshqa grantni kutayotganda depozit to'lash yoki taklifni qabul qilish majburiyati <b>qachon boshlanishini</b> tekshiring.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> A taklifga javob muddati 10 kun, B moliya hali noaniq. Muddatni uzaytirish mumkinmi, buni faqat o'sha tashkilotning qoidasi va yozma javobi aniqlaydi.</div>
<div class="box warn"><i>“Professor ha dedi”</i> degan gapni shartsiz qabul deb tushunmang.</div>
<div class="srcs">Manba: {UKRI}. {HOL}.</div>""",
             take="Har taklif uchun shartlar jadvali va muddat; rad javobi uchun 30 kunlik reja.",
             task="<ul><li>Har taklif uchun shartlar jadvalini tuzing.</li><li>Muddatlarni yozing.</li><li>Rad javobi kelsa, keyingi 30 kunda nima qilishingizni rejalang.</li></ul><p><b>O'zingizga savol:</b> aynan qaysi shart bajarilmasa, taklif bekor bo'ladi?</p>",
             ph="Taklif A: shartlar ..., javob muddati ... ; B: ... ; Rad: sabab ..., 30 kunlik reja ..."),
        dict(t="Yakuniy qaror", short="Qaror", min=25, kind="⚖️ Qaror", ic="scroll",
             hook="Qaysi taklifni olishni <b>ilmiy moslik, moliya va hayot sharoiti</b> birgalikda hal qiladi. Universitet nomi bu omillardan faqat bittasi.",
             body=f"""<p>Ballar faqat murosalarni ko'rsatadi, tanlovni sizning o'rningizga qilmaydi. Qaytarib bo'lmaydigan xarajat qilishdan oldin yozma moliya, qabul, turar joy rejasi va oila ehtiyojlarini tasdiqlab oling. Qaror qilgach, rad etilgan takliflarga o'z vaqtida javob bering.</p>
<p>Rahbarlik va yordam bo'yicha UKRI kutilmalar bayonini taklif shartlari bilan solishtirib ko'ring.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> <i>“Kafedra reytingi eng yuqori”</i> degan sababdan ko'ra <i>“bu rahbarda mos ma'lumot, to'liq moliya va yordam beradigan jamoa bor”</i> degan sabab asosliroq bo'lishi mumkin.</div>
<div class="box warn">Noaniq joylarni yashirib, umumiy ballni haqiqatga aylantirmang.</div>
<div class="srcs">Manba: {UKRIEXP}. {HOL}.</div>""",
             take="4 mezonli qaror xati, hal bo'lmagan xavflar va keyingi qadamlar: qabul qilish, kechiktirish yoki rad etish.",
             task="<ul><li>4 mezonli qaror xatini yozing.</li><li>Hal bo'lmagan xavflarni belgilang.</li><li>Qabul qilish, kechiktirish yoki rad etish qadamlarini rejalang.</li></ul><p><b>O'zingizga savol:</b> 2 yildan keyin ham bu qarorni asoslay olasizmi?</p>",
             ph="Ilmiy moslik ..., moliya ..., rahbarlik ..., hayot sharoiti ... → qaror: ..."),
    ],
    tool=dict(id="kalendar", short="Kalendar", h2="Teskari kalendar", sub="Ariza muddatini kiriting: nazorat sanalari undan orqaga qarab hisoblanadi. Keyin arizalar ro'yxatini to'ldiring.",
              h3="Arizalar ro'yxati", tag="5 maydon", ic="calendar", btn="Ro'yxatni saqlash", badge="Topshiruvchi", min=4,
              pre=f"""<div class="fld"><label for="dD">Ariza muddati <small>portal yopiladigan sana</small></label><input id="dD" type="date" style="{INP}"><div id="dOut" class="out" style="white-space:normal">Sanani tanlang.</div></div>""",
              fields=[dict(k="ariza", label="Arizalar va raqamlar", type="area", ph="1) ...: yuborildi ..., raqam ... ; 2) ..."),
                      dict(k="tavs", label="Tavsiyalar holati", type="area", ph="...: qabul qilindi ; ...: kutilmoqda"),
                      dict(k="bank", label="Intervyu savollari to'plami", type="area", ph="1) ...: javob tayanchi ..."),
                      dict(k="taklif", label="Takliflar va shartlar", type="area", ph="A: ..., B: ..."),
                      dict(k="qaror", label="Qaror", type="select", opts=["Hali taklif yo'q", "Taklifni qabul qilaman", "Kechiktiraman", "Rad etaman, keyingi yil"])]),
    check=dict(h2="M7 nazorati", sub="Yakuniy qarordan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Har ariza portal tasdig'i va holati bilan yozilgan.", "Fayl nomlari va versiyalari tekshirilgan.", "Tavsiyalar holati portalda tekshirilgan.",
                      "Intervyu savollariga dalilga tayangan javoblar tayyor.", "Taklif moliya va shartlar bo'yicha tekshirilgan.",
                      "Rad javobi uchun zaxira reja yozilgan.", "Rad etiladigan takliflarga javob berish rejasi bor."]),
    art_title="Arizalar ro'yxati, intervyu savollari va qaror jadvali", art_short="Qaror",
    art=[("Nazorat sanalari", ["dcalc"]), ("Arizalar", ["ariza", "a1"]), ("Tavsiyalar", ["tavs", "a2"]), ("Intervyu", ["bank", "a3", "a4"]),
         ("Takliflar", ["taklif", "a5"]), ("Qaror", ["a6", "qaror"])],
    tip="Har arizaning tasdiq xatini alohida papkaga saqlang. Keyinroq <i>“yuborganmidim?”</i> degan savolga bir daqiqada javob topasiz.",
    sources=f"{LEEDS}; {UKRI}; {UKRIEXP}. {STD}",
    js="""window.KGTool = { init: function () {
  var d = document.getElementById("dD"), o = document.getElementById("dOut");
  var steps = [[42, "Tavsiya beruvchilarga so\\u02bbrov va rasmiy tarjima"], [28, "Ilmiy loyiha taklifi v3 va bayonnoma"], [14, "Hamma hujjatlar tayyor, tekshiruv ro\\u02bbyxati"], [7, "Topshirish (7 kunlik zaxira)"], [0, "Portal yopiladi"]];
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
