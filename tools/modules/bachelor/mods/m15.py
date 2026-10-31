from common import UCAS, TB, SIK, HOL, STD

MOD = dict(
    title="Intervyu va qabul qarori",
    desc="Bachelor Lab M15: intervyu turlari, 3 daqiqalik \"o'zingiz haqingizda\", akademik intervyu, o'zini yozib olish va 8 bandli mezon, qabul, rad va kutish ro'yxati bilan ishlash. Natija: 3 ta yozib olingan javob va mezon bali.",
    lead="Intervyu tayyorlanadigan ko'nikma. Bu modulda intervyu turlarini ajratasiz, javoblaringizni telefonga yozib, aniq mezon bilan baholaysiz va natijalar kelganda qanday qaror qabul qilishni rejalaysiz.",
    hero="bell", weeks="2", next="M16 Qabuldan keyin: viza va jo'nash", next_href="bachelor-lab-m16.html",
    goals=[("bell", "3 ta yozib olingan javob", "o'zingiz haqingizda, akademik masala, motivatsiya"),
           ("chart", "Mezon bali", "8 bandli baholash, ikki urinish solishtirilgan"),
           ("compass", "Qaror jadvali", "bir nechta taklif, kutish ro'yxati yoki rad bo'lsa")],
    warn=f"Intervyu formati universitet va stipendiyaga qarab har yili o'zgarishi mumkin. Javob berish muddatlari va depozit qoidalarini {HOL} universitet xatidan va rasmiy sahifadan o'qing.",
    lessons=[
        dict(t="Intervyu turlari", short="Turlar", min=25, kind="🎯 Mini-test", ic="bell",
             hook="Bitiruvchi bilan suhbat va akademik intervyu butunlay boshqa narsa. Biri sizni tanishga, ikkinchisi qanday fikrlashingizni ko'rishga qaratilgan.",
             body=f"""<div class="tbl"><table><thead><tr><th>Tur</th><th>Qayerda</th><th>Maqsad</th></tr></thead><tbody>
<tr><td>Bitiruvchi bilan suhbat ([[alumni interview]])</td><td>Ba'zi AQSh universitetlari</td><td>Sizni tanish, qiziqishlaringiz; ko'pincha qarorga kichik ta'sir</td></tr>
<tr><td>Akademik intervyu</td><td>Oksford, Kembrij, ba'zi Yevropa va Osiyo universitetlari</td><td>Fan bo'yicha fikrlash, yangi masalani yechish</td></tr>
<tr><td>Stipendiya intervyusi</td><td>GKS, MEXT, Türkiye Bursları va boshqalar</td><td>Motivatsiya, reja, mamlakat va dasturga moslik</td></tr>
<tr><td>Qabul suhbati</td><td>Ba'zi universitetlar va dasturlar</td><td>Til, motivatsiya, hujjatlar bo'yicha savollar</td></tr>
</tbody></table></div>
<h4>Onlayn texnika</h4>
<ul><li>Kamera ko'z darajasida, yuz yoritilgan, orqa fon tinch.</li><li>Internet zaxirasi (mobil internet), quloqchin.</li><li>Platformani (Zoom, Teams) bir kun oldin sinab ko'ring.</li><li>Vaqt mintaqasini tekshiring: intervyu vaqti Toshkent vaqtiga to'g'ri o'girilganmi?</li></ul>
<div class="srcs">Manba: universitetlarning intervyu sahifalari; {SIK}; {TB}. {HOL}.</div>""",
             take="Bitiruvchi suhbati tanishish, akademik intervyu fikrlash, stipendiya intervyusi motivatsiya va reja uchun. Onlayn texnikani bir kun oldin tekshiring.",
             quiz=[("Akademik intervyuda to'g'ri javobdan ko'ra fikrlash jarayoni muhimroq bo'lishi mumkin.", "t", "To'g'ri: intervyuchi qanday o'ylashingizni ko'rmoqchi."),
                   ("Bitiruvchi bilan suhbat har doim qabulni hal qiladi.", "n", "Noto'g'ri: ko'pincha qarorga kichik ta'sir qiladi."),
                   ("Intervyu vaqtini Toshkent vaqtiga o'girib tekshirish kerak.", "t", "To'g'ri: vaqt mintaqasi xatosi keng uchraydi."),
                   ("Stipendiya intervyusida o'qishdan keyingi rejangiz so'ralmaydi.", "n", "Noto'g'ri: reja va motivatsiya asosiy mavzu.")],
             task="<ul><li>Arizalaringizda qaysi intervyu turlari kutilishini yozing.</li><li>Onlayn intervyu uchun texnik nazorat ro'yxatingizni tuzing.</li></ul>",
             ph="... — akademik intervyu; ... — stipendiya intervyusi. Texnika: ..."),
        dict(t="\"O'zingiz haqingizda\": 3 daqiqa", short="3 daqiqa", min=25, kind="🎙 Yozib olish", ic="seedling",
             hook="\"O'zingiz haqingizda gapirib bering\" deyarli har intervyuning birinchi savoli. Birinchi 3 daqiqa butun suhbat ohangini belgilaydi.",
             body="""<h4>Tuzilma: Hozir → O'tmish → Kelajak</h4>
<ol><li><b>Hozir (30 soniya)</b>: kimsiz, qayerda o'qiysiz, nimaga qiziqasiz (M3 profili).</li><li><b>O'tmish (90 soniya)</b>: bu qiziqish qanday shakllangan, 1–2 aniq epizod va natija.</li><li><b>Kelajak (60 soniya)</b>: nega shu dastur yoki stipendiya, nimani o'rganmoqchisiz, keyin nima qilasiz.</li></ol>
<h4>Misol tahlili (Kompas tuzgan namuna)</h4>
<div class="tbl"><table><thead><tr><th>Kuchsiz</th><th>Kuchli</th></tr></thead><tbody>
<tr><td>\"Men Aziz, 17 yoshdaman, maktabda a'lochiman, sport bilan shug'ullanaman, kitob o'qishni yaxshi ko'raman...\"</td><td>\"Men energiya tizimlariga qiziqaman. Shu yil mahallamizdagi elektr uzilishlarini 3 oy kuzatib, ...\"</td></tr>
</tbody></table></div>
<p>Kuchsiz javob ro'yxat, kuchli javob bitta yo'nalish va dalil.</p>
<div class="box info">Javobni yod olmang, tuzilmasini yod oling. Yodlangan matn sun'iy eshitiladi va savol o'zgarsa yo'qolib qolasiz.</div>""",
             take="Hozir → O'tmish → Kelajak, jami 3 daqiqa. Ro'yxat emas, bitta yo'nalish va dalil. Tuzilmani yod oling, matnni emas.",
             task="<ul><li>3 daqiqalik javobni telefonga yozib oling.</li><li>Uchta qism necha soniya olganini yozing.</li></ul>",
             ph="Hozir: ... soniya; O'tmish: ...; Kelajak: ... Umumiy: ..."),
        dict(t="Akademik intervyu", short="Akademik", min=30, kind="🧠 Masala", ic="bulb",
             hook="Akademik intervyuda sizga hech qachon ko'rmagan masala beriladi. Intervyuchi to'g'ri javobni emas, siz qanday fikrlashingizni eshitmoqchi.",
             body="""<h4>Ovoz chiqarib fikrlash</h4>
<ol><li><b>Savolni qayta ayting</b>: tushunganingizni tekshirish uchun.</li><li><b>Ma'lumni ajrating</b>: nimani bilaman, nima berilgan?</li><li><b>Oddiy holatdan boshlang</b>: kichik son, maxsus holat, chizma.</li><li><b>Har qadamni ayting</b>: \"Avval ... ni ko'raman, chunki ...\"</li><li><b>Xatoni tan oling</b>: \"Bu yerda xato qildim, qayta ko'raman.\"</li><li><b>Maslahatni qabul qiling</b>: intervyuchi yo'naltirsa, uni ishlating.</li></ol>
<h4>Tayyorgarlik</h4>
<ul><li>Sohangiz bo'yicha olimpiada va qiziqarli masalalar to'plamidan haftasiga 3–5 masalani ovoz chiqarib yeching.</li><li>Do'stingiz intervyuchi bo'lsin: u faqat savol beradi va to'xtab qolsangiz yo'naltiradi.</li><li>O'qigan kitob yoki maqolangiz haqida 2 daqiqa gapira olishingizni tekshiring: intervyuchi bayonotingizdagi narsalar haqida so'rashi mumkin.</li></ul>
<div class="box warn">Bilmasangiz, to'qimang. \"Buni bilmayman, lekin shunday o'ylayman...\" deb taxminingizni asoslang. Bu kuchli javob.</div>""",
             take="Akademik intervyuda savolni qayta ayting, oddiydan boshlang, har qadamni ovoz chiqarib ayting, xatoni tan oling va maslahatni ishlating.",
             task="<ul><li>Sohangiz bo'yicha bitta yangi masalani ovoz chiqarib yechib, yozib oling.</li><li>Qaysi qadamda to'xtaganingizni va nima yordam berganini yozing.</li></ul>",
             ph="Masala: ... To'xtagan joy: ... Yordam bergan: ..."),
        dict(t="O'z-o'zini yozib olish va baholash", short="Mezon", min=30, kind="🛠 8 band", ic="chart",
             hook="O'z ovozingizni yozuvda eshitish noqulay, lekin intervyuga tayyorlanishning eng tez yo'li. Mezon bilan baholasangiz, nimani tuzatishni aniq ko'rasiz.",
             body="""<h4>8 bandli mezon (har biri 0–2 ball, jami 16)</h4>
<div class="tbl"><table><thead><tr><th>№</th><th>Band</th><th>2 ball</th></tr></thead><tbody>
<tr><td>1</td><td>Tuzilma</td><td>Boshlanish, asosiy qism, xulosa aniq</td></tr>
<tr><td>2</td><td>Aniq dalil</td><td>Kamida bitta epizod yoki natija</td></tr>
<tr><td>3</td><td>Savolga javob</td><td>Aynan so'ralganga javob berdi</td></tr>
<tr><td>4</td><td>Vaqt</td><td>Chegarada (masalan 2–3 daqiqa)</td></tr>
<tr><td>5</td><td>Til aniqligi</td><td>Tushunarli, takrorsiz</td></tr>
<tr><td>6</td><td>Tezlik va pauza</td><td>Shoshilmasdan, pauzalar o'rinli</td></tr>
<tr><td>7</td><td>Ko'z va kamera</td><td>Kameraga qaraydi, yozuvdan o'qimaydi</td></tr>
<tr><td>8</td><td>Halollik va ishonch</td><td>To'qimaydi, bilmaganini tan oladi</td></tr>
</tbody></table></div>
<h4>Jarayon</h4>
<ol><li>Telefonda yozib oling.</li><li>1 kundan keyin ko'ring va mezon bo'yicha baholang.</li><li>Eng past 2 bandni tanlab, ularni tuzatib qayta yozing.</li><li>Ikki urinish balini solishtiring.</li></ol>
<p><b>Ixtiyoriy o'zaro tahrir</b>: yozuvni faqat ishonchli bir kishiga (o'qituvchi yoki ota-ona) ko'rsating. Ochiq guruhga yoki noma'lum odamlarga yubormang: yozuvda yuzingiz va shaxsiy ma'lumotingiz bor.</p>""",
             take="8 band, har biri 0–2 ball. Yozib oling, ertasi kuni baholang, eng past 2 bandni tuzating va ikki urinishni solishtiring.",
             task="<ul><li>3 ta javobni (o'zingiz haqingizda, akademik masala, \"nega shu dastur\") yozib oling.</li><li>Pastdagi vositada mezon ballarini kiriting.</li></ul>",
             ph="1-javob: 11/16, eng past: vaqt, pauza ..."),
        dict(t="Natijalar: qabul, rad, kutish ro'yxati", short="Natijalar", min=30, kind="🧭 Qaror", ic="compass",
             hook="Natijalar kelganda his-tuyg'u kuchli bo'ladi. Oldindan tuzilgan qaror jadvali sizni shoshilinch va qimmat xatodan saqlaydi.",
             body=f"""<h4>Bir nechta qabul bo'lsa</h4>
<p>Solishtiring: to'liq 4 yillik xarajat va moliyaviy yordam (M12), dastur va moslik bali (M2), viza va hujjat talablari, javob va depozit muddati.</p>
<h4>Javob muddatlari</h4>
<ul><li><b>AQSh</b>: ko'p universitetlarda oddiy muddat bo'yicha qabul qilinganlar uchun javob muddati 1-may atrofida; aniq sanani qabul xatidan o'qing. Bir nechta universitetga depozit to'lash ([[double deposit]]) odatda qoidaga zid.</li><li><b>UK (UCAS)</b>: takliflar orasidan asosiy ([[firm]]) va zaxira ([[insurance]]) tanlovni belgilaysiz; muddat UCAS tizimida ko'rsatiladi.</li><li><b>Boshqa mamlakatlar</b>: universitet xatidagi muddat; ko'pincha qisqa.</li></ul>
<h4>Kutish ro'yxati</h4>
<p>Agar universitet ruxsat bersa, qiziqishingizni tasdiqlovchi qisqa xat ([[letter of continued interest]]) yuboring: hali ham birinchi tanlovmi, ariza berilgandan keyingi yangi yutuqlar. Lekin boshqa taklifni qabul qilib, depozit to'lang: kutish ro'yxati kafolat emas.</p>
<h4>Rad javobidan keyin</h4>
<ul><li>Qolgan takliflarni baholang.</li><li>Gap yili ([[gap year]]) va keyingi yil qayta ariza: nimani kuchaytirasiz?</li><li>O'zbekistonda o'qib, keyin almashinuv yoki magistraturada chet elga chiqish.</li></ul>
<div class="srcs">Manba: {UCAS}; universitetlarning qabul xatlari va rasmiy sahifalari. {HOL}.</div>""",
             take="Qabullarni xarajat, dastur va muddat bo'yicha solishtiring; UCAS'da firm va insurance; kutish ro'yxatida qisqa xat yuboring, lekin boshqa taklifni ham qabul qiling.",
             task="<ul><li>Pastdagi qaror jadvali uchun mezonlaringizni va ularning og'irligini yozing.</li><li>Rad javobi kelsa, zaxira rejangizni 3 qadamda yozing.</li></ul>",
             ph="Mezonlar: xarajat (40%), dastur (30%) ... Zaxira: 1) ... 2) ... 3) ..."),
    ],
    tool=dict(id="mezon", short="Mezon", h2="Yozib olingan javoblar va mezon bali", sub="Har javob uchun 8 band bo'yicha 0–2 ball. Hisoblagich jami va eng zaif bandlarni ko'rsatadi.",
              h3="Intervyu mezoni", tag="5 maydon", ic="chart", btn="Natijani saqlash", badge="Intervyu ustasi", min=4,
              pre="""<div class="fld"><label>Hisoblagich <small>oxirgi yozuv uchun, har band 0–2</small></label><div id="rbG" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px"></div><div id="rbOut" class="out" style="white-space:normal">Ballarni tanlang.</div></div>""",
              fields=[dict(k="j1", label="1-javob: o'zingiz haqingizda", hint="urinish 1 va 2 ballari, nima o'zgardi", type="area", ph="1-urinish 9/16 → 2-urinish 13/16: vaqt va dalil tuzatildi"),
                      dict(k="j2", label="2-javob: akademik masala", type="area", ph="..."),
                      dict(k="j3", label="3-javob: nega shu dastur yoki stipendiya", type="area", ph="..."),
                      dict(k="qaror", label="Qaror jadvali mezonlari", type="area", ph="Xarajat 40%, dastur 30%, viza 15%, shahar 15%"),
                      dict(k="zaxira", label="Rad yoki kutish ro'yxati uchun reja", type="area", ph="...")]),
    check=dict(h2="Intervyu va qaror nazorati", sub="Intervyu va natijalardan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har ariza uchun kutiladigan intervyu turi ma'lum.", "Onlayn texnika sinab ko'rilgan.", "Vaqt mintaqasi tekshirilgan.",
                      "3 ta javob yozib olingan va mezon bilan baholangan.", "Eng zaif 2 band tuzatilib, qayta yozilgan.", "Yozuvlar faqat ishonchli odamga ko'rsatilgan.",
                      "Qaror jadvali mezonlari natijalardan oldin yozilgan.", "Javob va depozit muddatlari xatdan o'qiladi."]),
    art_title="Intervyu tayyorgarligi va qaror jadvali", art_short="Intervyu",
    art=[("Intervyu turlari va texnika", ["a1"]), ("O'zingiz haqingizda", ["j1", "a2"]), ("Akademik masala", ["j2", "a3"]), ("Nega shu dastur", ["j3"]),
         ("Mezon natijalari", ["rb", "a4"]), ("Qaror jadvali", ["qaror", "a5"]), ("Zaxira reja", ["zaxira"])],
    tip="Intervyudan keyin 10 daqiqa ichida berilgan savollarni yozib qo'ying. Keyingi intervyu uchun eng qimmatli material shu.",
    sources=f"{UCAS}; {SIK}; {TB}. {STD}",
    js="""window.KGTool = { init: function () {
  var B = ["Tuzilma", "Aniq dalil", "Savolga javob", "Vaqt", "Til aniqligi", "Tezlik va pauza", "Koʻz va kamera", "Halollik va ishonch"];
  var g = document.getElementById("rbG"), o = document.getElementById("rbOut");
  var prev = String(KG.S.notes.rb_in || "").split(",");
  B.forEach(function (b, i) {
    var s = document.createElement("select"); s.id = "rb" + i;
    s.setAttribute("aria-label", b);
    s.style.cssText = "min-height:44px;padding:8px 10px;border:2px solid var(--border);border-radius:12px;font-size:15px;width:100%";
    s.innerHTML = "<option value=\\"\\">" + b + "</option><option value=\\"0\\">" + b + ": 0</option><option value=\\"1\\">" + b + ": 1</option><option value=\\"2\\">" + b + ": 2</option>";
    if (prev[i]) s.value = prev[i];
    s.addEventListener("change", run); g.appendChild(s);
  });
  function run() {
    var v = B.map(function (b, i) { return document.getElementById("rb" + i).value; });
    var n = v.filter(function (x) { return x !== ""; }).length;
    if (!n) { o.textContent = "Ballarni tanlang."; return; }
    var t = 0, low = []; v.forEach(function (x, i) { if (x !== "") { t += +x; if (+x === 0) low.push(B[i]); } });
    var txt = "Jami " + t + " / " + (n * 2) + (n < 8 ? " (" + n + " band baholandi)" : "") + (low.length ? ". Tuzatish kerak: " + low.join(", ") : "");
    o.textContent = txt; KG.S.notes.rb = txt; KG.S.notes.rb_in = v.join(","); KG.save();
  }
  run();
} };""",
)
