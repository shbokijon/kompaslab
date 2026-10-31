from common import CSS, CDS, FTC, UK_VISA, DE_VISA, US_SEVIS, HOL, STD

MOD = dict(
    title="Universitet grantlari va moliyaviy reja",
    desc="Bachelor Lab M12: AQSh moliyaviy yordami (need-blind, need-aware, CSS Profile), universitet stipendiyalari, to'liq xarajat modeli, 4 yillik moliyaviy reja, firibgarlikdan himoya. Natija: 4 yillik moliyaviy reja.",
    lead="Qabul xati faqat yarim natija: to'lay olmasangiz, o'qishga bora olmaysiz. Bu modulda universitetlar yordamini qanday so'rashni, haqiqiy 4 yillik xarajatni va oila bilan muhokama qilinadigan moliyaviy rejani tuzasiz.",
    hero="money", weeks="2", next="M13 Ariza platformalari", next_href="bachelor-lab-m13.html",
    goals=[("money", "4 yillik moliyaviy reja", "har yil: xarajat, qoplanadigan qism, bo'shliq, zaxira"),
           ("chart", "To'liq xarajat modeli", "o'qish, yashash, sug'urta, viza, yo'l, yashirin xarajatlar"),
           ("shield", "Firibgarlik belgilari ro'yxati", "soxta stipendiya va \"kafolatli\" agentlar")],
    warn=f"Xarajatlar, valyuta kursi va yordam siyosatlari har yili o'zgaradi. Bu moduldagi raqamlar o'rniga {HOL} rasmiy sahifalardan topganingizni yozing. Kompas Lab moliyaviy maslahatchi emas; katta qarorlarni oila bilan qabul qiling.",
    lessons=[
        dict(t="AQSh moliyaviy yordami", short="AQSh yordami", min=35, kind="🎯 Mini-test", ic="money",
             hook="AQShning ba'zi universitetlari xalqaro talabaning oilasi to'lay olmaydigan summani o'zi qoplaydi. Lekin bu universitetlar kam va qabuli juda tanlovli.",
             body=f"""<h4>Ikki siyosat</h4>
<div class="tbl"><table><thead><tr><th>Siyosat</th><th>Ma'nosi</th></tr></thead><tbody>
<tr><td>To'lov qobiliyatiga qaramaydigan ([[need-blind]])</td><td>Qabul qarorida yordam so'raganingiz hisobga olinmaydi. Xalqaro talabalar uchun bu siyosatni juda kam universitet qo'llaydi</td></tr>
<tr><td>To'lov qobiliyatiga qaraydigan ([[need-aware]])</td><td>Yordam so'rash qabul qaroriga ta'sir qilishi mumkin, chunki yordam byudjeti cheklangan</td></tr>
</tbody></table></div>
<p>Alohida savol: universitet <b>to'liq ehtiyojni qoplaydimi</b> ([[meets full demonstrated need]])? Ba'zilari need-aware bo'lsa ham, qabul qilingan talabaning to'liq ehtiyojini qoplaydi.</p>
<h4>Hujjatlar</h4>
<ul><li><b>CSS Profile</b>: College Board tizimi, oila daromadi, mulki va xarajatlari haqida batafsil anketa. Ko'p xususiy universitetlar xalqaro talabalardan so'raydi; to'lovli, lekin ozod qilish imkoniyati bor.</li><li>Ba'zi universitetlar o'z formasini yoki xalqaro talabalar uchun moliyaviy yordam anketasini so'raydi.</li><li>Daromad hujjatlari: ish joyidan ma'lumotnoma, soliq hujjatlari, bank ko'chirmasi (tarjima bilan).</li></ul>
<h4>Qaysi universitet yordam beradi</h4>
<p>Universitetning rasmiy \"international financial aid\" sahifasi va Common Data Set'ning H bo'limi (xalqaro talabalarga berilgan yordam). Javob \"yo'q\" yoki juda kam bo'lsa, u universitet ishonchli daraja bo'la olmaydi.</p>
<div class="srcs">Manba: {CSS}; {CDS}; universitetlarning rasmiy moliyaviy yordam sahifalari. {HOL}.</div>""",
             take="Need-blind xalqaro talabalar uchun kam; need-aware'da yordam so'rash qabulga ta'sir qilishi mumkin. CSS Profile va universitet sahifasi, CDS H bo'limi bilan tekshiring.",
             quiz=[("Need-aware siyosatda yordam so'rash qabul qaroriga ta'sir qilishi mumkin.", "t", "To'g'ri: yordam byudjeti cheklangan."),
                   ("Ko'p AQSh universitetlari xalqaro talabalar uchun need-blind.", "n", "Noto'g'ri: bunday universitetlar juda kam."),
                   ("CSS Profile oila moliyaviy holati haqidagi anketa.", "t", "To'g'ri: ko'p xususiy universitetlar so'raydi."),
                   ("Universitet xalqaro talabalarga yordam berishini CDS'dan tekshirish mumkin.", "t", "To'g'ri: H bo'limida xalqaro talabalarga yordam ma'lumoti bor.")],
             task="<ul><li>AQSh universitetlaringiz uchun: need-blind yoki need-aware, to'liq ehtiyojni qoplaydimi, qaysi forma kerak.</li><li>Havola va tekshirilgan sanani yozing.</li></ul>",
             ph="... — need-aware, to'liq ehtiyoj: ha, CSS Profile; havola: ..."),
        dict(t="Universitet stipendiyalari", short="Universitet", min=25, kind="🔎 Qidiruv", ic="telescope",
             hook="Ko'p universitetlar xalqaro talabalarga chegirma yoki stipendiya beradi, lekin uni topish uchun dastur sahifasidan chuqurroq qarash kerak.",
             body="""<h4>Ikki tur</h4>
<div class="tbl"><table><thead><tr><th>Tur</th><th>Qanday</th><th>Nima qilish</th></tr></thead><tbody>
<tr><td>Avtomatik</td><td>Qabul vaqtida baho yoki test asosida beriladi</td><td>Shartini (baho, muddat) o'qing; ariza shart emas</td></tr>
<tr><td>Ariza bilan</td><td>Alohida forma, insho, ba'zan intervyu</td><td>Muddatini nazorat jadvaliga qo'shing; ko'pincha qabul muddatidan oldin</td></tr>
</tbody></table></div>
<h4>Qidirish usuli</h4>
<ol><li>Universitet saytida \"scholarships\", \"international students\", \"fees and funding\" sahifalari.</li><li>Fakultet sahifasi: ba'zi stipendiyalar faqat fakultet darajasida.</li><li>Xalqaro bo'limga yozma savol: \"O'zbekistonlik bakalavr abituriyentlari qaysi stipendiyalarga ariza bera oladi?\"</li></ol>
<h4>Shartlarni o'qing</h4>
<ul><li>Bir yillikmi yoki 4 yilga?</li><li>Keyingi yillarda baho sharti bormi?</li><li>Summa qat'iymi yoki foiz?</li></ul>
<div class="box info">Birinchi yil uchun katta, keyingi yillar uchun yo'q stipendiya 4 yillik rejada katta bo'shliq qoldiradi.</div>""",
             take="Universitet stipendiyalari avtomatik yoki ariza bilan. Muddat, davomiylik (1 yil yoki 4 yil) va baho shartini o'qing.",
             task="<ul><li>Portfelingizdagi 3 universitetning xalqaro talabalar stipendiyalarini toping.</li><li>Har biri uchun: tur, summa, davomiylik, shart, muddat.</li></ul>",
             ph="... — avtomatik, o'qish to'lovining ...%, 4 yil, baho ... saqlansa"),
        dict(t="To'liq xarajat modeli", short="Xarajat", min=30, kind="🛠 Model", ic="chart",
             hook="O'qish to'lovi xarajatning faqat bir qismi. Yashash, sug'urta, viza va yo'l ko'pincha o'qish to'lovidan kam emas.",
             body=f"""<h4>Xarajat qatorlari</h4>
<div class="tbl"><table><thead><tr><th>Qator</th><th>Qayerdan</th></tr></thead><tbody>
<tr><td>O'qish to'lovi</td><td>Universitet \"fees\" sahifasi, xalqaro talaba uchun</td></tr>
<tr><td>Yashash (yotoqxona yoki ijara, ovqat, transport)</td><td>Universitetning \"cost of attendance\" yoki \"living costs\" sahifasi</td></tr>
<tr><td>Tibbiy sug'urta</td><td>Universitet yoki viza talabi (masalan UK da [[Immigration Health Surcharge]])</td></tr>
<tr><td>Viza va tegishli to'lovlar</td><td>Viza rasmiy sahifasi (AQShda SEVIS to'lovi ham)</td></tr>
<tr><td>Moliyaviy kafolat</td><td>Masalan, Germaniyada bloklangan hisob ([[Sperrkonto]]); bu xarajat emas, lekin oldindan kerak bo'ladigan pul</td></tr>
<tr><td>Yo'l</td><td>Aviabilet, yiliga kamida bir marta</td></tr>
<tr><td>Ariza va hujjatlar</td><td>M2 byudjeti</td></tr>
<tr><td>Yashirin xarajatlar</td><td>Kitob, noutbuk, qishki kiyim, depozit, birinchi oy ijarasi</td></tr>
</tbody></table></div>
<p>Universitetning \"cost of attendance\" summasini asos qiling: u odatda yashashni ham o'z ichiga oladi va real summaga yaqin.</p>
<div class="box warn">Valyuta xavfi: so'mdagi summa kurs o'zgarsa oshadi. Hisobni asl valyutada yuriting va 10–15 foiz zaxira qo'shing.</div>
<div class="srcs">Manba: {UK_VISA}; {DE_VISA}; {US_SEVIS}; universitetlarning fees va cost of attendance sahifalari. {HOL}.</div>""",
             take="To'liq xarajat: o'qish, yashash, sug'urta, viza, kafolat, yo'l va yashirin xarajatlar. Asl valyutada hisoblang, 10–15 foiz zaxira qo'shing.",
             task="<ul><li>Bitta universitet uchun 8 qator bo'yicha yillik xarajatni yozing.</li><li>Manba havolalarini qo'shing.</li></ul>",
             ph="... universiteti (yillik): o'qish ..., yashash ..., sug'urta ..., viza ..., yo'l ..., yashirin ... = ..."),
        dict(t="4 yillik moliyaviy reja", short="4 yil", min=30, kind="📊 Reja", ic="calendar",
             hook="Birinchi yilni qoplash yetarli emas. Ikkinchi yilda pul tugasa, o'qish to'xtaydi va viza ham xavf ostida qoladi.",
             body="""<h4>Reja tuzilmasi</h4>
<div class="tbl"><table><thead><tr><th>Yil</th><th>Xarajat</th><th>Stipendiya / grant</th><th>Oila</th><th>Boshqa</th><th>Bo'shliq</th></tr></thead><tbody>
<tr><td>1</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
<tr><td>2</td><td colspan="5">o'qish to'lovining yillik o'sishini hisobga oling</td></tr>
<tr><td>3–4</td><td colspan="5">stipendiya shartlari (baho) saqlanishini rejalang</td></tr>
</tbody></table></div>
<h4>Bo'shliqni yopish</h4>
<ul><li><b>Talaba ishi</b>: viza qoidalari haftalik soatni cheklaydi (masalan, ko'p mamlakatlarda o'qish davrida yarim stavka). Ish daromadini asosiy manba qilib qo'ymang.</li><li><b>Keyingi yillar stipendiyalari</b>: ba'zi universitetlar 2-kursdan keyin stipendiya beradi, lekin kafolatsiz.</li><li><b>Arzonroq variant</b>: ishonchli darajadagi arzon universitet.</li></ul>
<h4>Zaxira manba</h4>
<p>Kutilmagan holat uchun kamida bir necha oylik yashash xarajatiga teng zaxira. Valyuta kursi 20 foiz o'zgarsa, reja qanday o'zgarishini hisoblang.</p>
<div class="box warn">Reja bo'shliq 0 dan katta bo'lgan yil bilan tugasa, bu universitet hozircha real variant emas. Buni oila bilan ochiq muhokama qiling.</div>""",
             take="Har yil uchun xarajat, manbalar va bo'shliq. Talaba ishini asosiy manba qilmang, zaxira va valyuta stsenariysini qo'shing.",
             task="<ul><li>Eng ehtimolli universitetingiz uchun 4 yillik jadvalni to'ldiring.</li><li>Valyuta kursi 20 foiz oshganda bo'shliq qanday o'zgarishini yozing.</li></ul>",
             ph="1-yil: xarajat ..., stipendiya ..., oila ..., bo'shliq ... 2-yil: ... Kurs +20%: ..."),
        dict(t="Firibgarlikdan himoya", short="Himoya", min=20, kind="🛡 Belgilar", ic="shield",
             hook="Xorijda o'qish atrofida firibgarlik ko'p: soxta stipendiya, \"kafolatli qabul\" va oldindan to'lov so'raydigan agentlar. Bir xato oilaning yillik daromadini olib ketishi mumkin.",
             body=f"""<h4>Ogohlantiruvchi belgilar</h4>
<ul><li>\"Stipendiya kafolatlanadi\" yoki \"qabul 100 foiz\".</li><li>Stipendiyani olish uchun oldindan to'lov (\"rasmiylashtirish to'lovi\", \"hujjat to'lovi\").</li><li>Rasmiy bo'lmagan email (masalan, oddiy pochta xizmati manzili universitet nomidan).</li><li>Shoshirish: \"bugun to'lamasangiz joy ketadi\".</li><li>Siz ariza bermagan stipendiyani \"yutganingiz\" haqida xabar.</li><li>Universitet sahifasida topilmaydigan dastur yoki shartnoma.</li></ul>
<h4>Tekshirish</h4>
<ol><li>Universitet yoki stipendiya rasmiy saytini o'zingiz qidirib oching (xabardagi havolani emas).</li><li>Qabul bo'limiga rasmiy saytdagi manzil orqali yozib tasdiqlang.</li><li>Pulni faqat universitetning rasmiy to'lov tizimiga o'tkazing; shaxsiy kartaga emas.</li></ol>
<div class="box info">Agent bilan ishlash qonuniy, lekin agent universitetdan komissiya olishi mumkin va u sizga \"o'z\" universitetlarini taklif qiladi. Kompas Lab agentlik xizmati ko'rsatmaydi.</div>
<div class="srcs">Manba: {FTC}. {HOL}.</div>""",
             take="Kafolat, oldindan to'lov, norasmiy email va shoshirish firibgarlik belgilari. Rasmiy saytni o'zingiz oching va pulni faqat rasmiy tizimga o'tkazing.",
             task="<ul><li>6 ta ogohlantiruvchi belgini oilangiz bilan muhokama qiling.</li><li>Oila uchun 3 qoidali \"pul o'tkazishdan oldin\" ro'yxatini yozing.</li></ul>",
             ph="1) Rasmiy saytni o'zimiz ochamiz 2) ... 3) ..."),
    ],
    tool=dict(id="reja", short="Reja", h2="4 yillik moliyaviy reja", sub="Hisoblagich: yillik xarajat va manbalarni kiriting, 4 yillik bo'shliq va zaxira avtomatik chiqadi.",
              h3="Moliyaviy reja", tag="5 maydon", ic="money", btn="Rejani saqlash", badge="Moliya rejachisi", min=4,
              pre="""<div class="fld"><label>Hisoblagich <small>bir valyutada, yillik</small></label><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px"><input id="fX" type="number" min="0" placeholder="Yillik xarajat" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"><input id="fS" type="number" min="0" placeholder="Stipendiya / grant" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"><input id="fO" type="number" min="0" placeholder="Oila" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"><input id="fG" type="number" min="0" step="1" placeholder="Yillik o'sish, %" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"></div><div id="fOut" class="out" style="white-space:normal">Raqamlarni kiriting.</div></div>""",
              fields=[dict(k="uni", label="Universitet va valyuta", ph="... universiteti, USD"),
                      dict(k="xarajat", label="To'liq xarajat modeli (yillik)", type="area", ph="O'qish ..., yashash ..., sug'urta ..., viza ..., yo'l ..., yashirin ..."),
                      dict(k="manba", label="Manbalar", hint="stipendiya, grant, oila, boshqa", type="area", ph="..."),
                      dict(k="zaxira", label="Zaxira va valyuta stsenariysi", type="area", ph="Zaxira: ... oy; kurs +20%: ..."),
                      dict(k="himoya", label="Oila uchun \"pul o'tkazishdan oldin\" qoidalari", type="area", ph="1) ... 2) ... 3) ...")]),
    check=dict(h2="Moliyaviy reja nazorati", sub="Rejani yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har universitet uchun yordam siyosati (need-blind/aware) tekshirilgan.", "Stipendiyaning davomiyligi va baho sharti o'qilgan.",
                      "Xarajat 8 qator bo'yicha hisoblangan.", "Hisob asl valyutada va manba bilan.", "4 yilning har biri uchun bo'shliq hisoblangan.",
                      "Valyuta stsenariysi va zaxira bor.", "Talaba ishi asosiy manba qilinmagan.", "Reja oila bilan muhokama qilingan."]),
    art_title="4 yillik moliyaviy reja", art_short="Reja",
    art=[("Universitet va valyuta", ["uni"]), ("Yordam siyosati", ["a1"]), ("Universitet stipendiyalari", ["a2"]), ("To'liq xarajat modeli", ["xarajat", "a3"]),
         ("Manbalar", ["manba"]), ("4 yillik hisob", ["plan4", "a4"]), ("Zaxira va valyuta", ["zaxira"]), ("Firibgarlikdan himoya", ["himoya", "a5"])],
    tip="Moliyaviy rejani oila bilan bitta stol atrofida, raqamlar bilan muhokama qiling. \"Qandaydir hal bo'lar\" degan reja emas.",
    sources=f"{CSS}; {CDS}; {UK_VISA}; {DE_VISA}; {US_SEVIS}; {FTC}. {STD}",
    js="""window.KGTool = { init: function () {
  var ids = ["fX", "fS", "fO", "fG"], o = document.getElementById("fOut");
  function v(id) { var x = parseFloat(document.getElementById(id).value); return isNaN(x) ? 0 : x; }
  function fmt(n) { return Math.round(n).toLocaleString("ru-RU"); }
  function run() {
    var X = v("fX"), S = v("fS"), O = v("fO"), G = v("fG") / 100;
    if (!X) { o.textContent = "Raqamlarni kiriting."; return; }
    var rows = [], tot = 0;
    for (var y = 1; y <= 4; y++) { var x = X * Math.pow(1 + G, y - 1), gap = Math.max(0, x - S - O); tot += gap; rows.push(y + "-yil: xarajat " + fmt(x) + ", boʻshliq " + fmt(gap)); }
    var txt = rows.join("; ") + ". 4 yilda jami boʻshliq: " + fmt(tot) + ".";
    o.innerHTML = "<span class=\\"pill " + (tot > 0 ? "no" : "ok") + "\\">" + (tot > 0 ? "Boʻshliq bor" : "Qoplangan") + "</span> " + KG.esc(txt);
    KG.S.notes.plan4 = txt; KG.S.notes.fin_in = [X, S, O, v("fG")].join("|"); KG.save();
  }
  if (KG.S.notes.fin_in) { var p = String(KG.S.notes.fin_in).split("|"); ids.forEach(function (id, i) { if (p[i] && p[i] !== "0") document.getElementById(id).value = p[i]; }); }
  ids.forEach(function (id) { document.getElementById(id).addEventListener("input", run); });
  run();
} };""",
)
