from common import CA_ESSAY, UCAS_PS, THE_PS, HOL, STD

MOD = dict(
    title="Shaxsiy bayonot va insholar",
    desc="Bachelor Lab M9: insho, shaxsiy bayonot va motivatsion xat farqi, Common App asosiy inshosi, hikoya topish, UCAS shaxsiy bayonoti (2026 qabulidan uch savol), qo'shimcha insholar. Natija: asosiy insho v1, UCAS bayonoti v1 va qo'shimcha insholar rejasi.",
    lead="Insho arizaning siz o'zingiz gapiradigan yagona qismi. Bu modulda platforma nimani so'rashini ajratasiz, kichik epizoddan hikoya topasiz va birinchi qoralamalarni yozasiz. Tahrir M10 da.",
    hero="memo", weeks="3", next="M10 Insho tahriri va yakuniy versiya", next_href="bachelor-lab-m10.html",
    goals=[("memo", "Asosiy insho qoralamasi v1", "Common App, 250–650 so'z"),
           ("scroll", "UCAS shaxsiy bayonoti v1", "uch savol, jami 4 000 belgigacha (kerak bo'lsa)"),
           ("compass", "Qo'shimcha insholar rejasi", "har universitet savoli va manbasi")],
    warn=f"Insho mavzulari, so'z va belgi chegaralari har sikl e'lon qilinadi. Bu moduldagi ma'lumot {HOL}. Kompas faqat freymvork va mezon beradi; insho matnini siz yozasiz.",
    lessons=[
        dict(t="Shaxsiy bayonot nima", short="Turlar", min=20, kind="🎯 Mini-test", ic="books",
             hook="\"Insho\", \"shaxsiy bayonot\", \"motivatsion xat\" ko'pincha bir xil narsa deb o'ylanadi. Aslida har biri boshqa savolga javob beradi.",
             body="""<div class="tbl"><table><thead><tr><th>Hujjat</th><th>Asosiy savol</th><th>Qayerda</th></tr></thead><tbody>
<tr><td>Shaxsiy insho ([[personal essay]])</td><td>Siz qanday odamsiz?</td><td>Common App asosiy inshosi</td></tr>
<tr><td>Shaxsiy bayonot ([[personal statement]])</td><td>Nega shu fan va bunga qanday tayyorlangansiz?</td><td>UCAS</td></tr>
<tr><td>Motivatsion xat ([[motivation letter]])</td><td>Nega shu dastur va shu universitet?</td><td>Yevropa va Osiyo portallari, stipendiyalar</td></tr>
<tr><td>Qo'shimcha insho ([[supplemental essay]])</td><td>Universitetning aniq savoli</td><td>AQSh universitetlari</td></tr>
</tbody></table></div>
<h4>Motivatsion xat freymvorki</h4>
<p>Kompas Lab freymvorki: <b>Kimlik → Dalil → Maqsad → Moslik</b>. Kim siz, buni nima ko'rsatadi, nimaga intilasiz, va nega aynan shu dastur.</p>
<div class="box info">Bitta matnni hamma platformaga yuborish xato. Har hujjat o'z savoliga javob berishi kerak, lekin hammasi M3 dagi bitta profilga tayanadi.</div>""",
             take="Insho shaxsni, UCAS bayonoti fan tanlovini, motivatsion xat dastur tanlovini ko'rsatadi. Hammasi bitta profilga tayanadi, lekin har biri o'z savoliga javob beradi.",
             quiz=[("UCAS shaxsiy bayonoti asosan fan tanlovi va unga tayyorgarlik haqida.", "t", "To'g'ri: 2026 qabulidan uchta savol aynan shu haqda."),
                   ("Common App inshosi va motivatsion xat bir xil matn bo'lishi mumkin.", "n", "Noto'g'ri: ular turli savollarga javob beradi."),
                   ("Motivatsion xat nega shu dastur va universitetni tanlaganingizni tushuntiradi.", "t", "To'g'ri: Kimlik → Dalil → Maqsad → Moslik."),
                   ("Qo'shimcha insholar faqat Yevropa universitetlarida bo'ladi.", "n", "Noto'g'ri: ular asosan AQSh universitetlarida.")],
             task="<ul><li>Portfelingizdagi har universitet qaysi yozma hujjatni so'rashini yozing.</li><li>Ularni to'rt turga ajrating.</li></ul>",
             ph="... — Common App insho + 2 qo'shimcha; ... — UCAS bayonot; ... — motivatsion xat"),
        dict(t="Common App asosiy inshosi", short="Common App", min=25, kind="🧭 Mavzu tanlovi", ic="compass",
             hook="Etti mavzudan qaysi birini tanlash ko'p vaqt oladi. Lekin komissiya mavzuga emas, hikoyaga va siz haqingizda nima bilib olganiga qaraydi.",
             body=f"""<h4>Asosiy faktlar</h4>
<ul><li>Etti mavzu varianti; ulardan biri \"o'zingiz tanlagan mavzu\".</li><li>Hajm: 250–650 so'z.</li><li>Bitta insho Common App orqali ariza beradigan hamma universitetga boradi.</li></ul>
<h4>Mavzular yo'nalishi (qisqacha)</h4>
<ol><li>Siz uchun muhim kelib chiqish, kimlik, qiziqish yoki iste'dod.</li><li>Qiyinchilik, muvaffaqiyatsizlik va undan saboq.</li><li>E'tiqod yoki g'oyani shubha ostiga qo'ygan payt.</li><li>Kimdir siz uchun qilgan va sizni minnatdor qilgan ish.</li><li>O'sishga olib kelgan yutuq yoki voqea.</li><li>Vaqtni unutib qo'yadigan darajada qiziqtiradigan mavzu.</li><li>O'zingiz tanlagan mavzu.</li></ol>
<p>Aniq matnni har yili rasmiy sahifadan o'qing.</p>
<h4>Mavzu emas, hikoya</h4>
<p>Avval hikoyani toping (L3), keyin unga mos mavzuni tanlang. Ko'p kuchli insholar bir nechta mavzuga mos keladi.</p>
<div class="srcs">Manba: {CA_ESSAY}. {HOL}.</div>""",
             take="Common App: 7 mavzu, 250–650 so'z, bitta insho hamma universitetga. Avval hikoyani toping, keyin mavzuni.",
             task="<ul><li>Joriy yil mavzularini rasmiy sahifadan o'qing.</li><li>Sizga yaqin 2 mavzuni tanlang va har biri uchun bitta hikoya g'oyasini yozing.</li></ul>",
             ph="Mavzu ...: hikoya g'oyasi ... Mavzu ...: ..."),
        dict(t="Hikoya topish va birinchi qoralama", short="Qoralama", min=40, kind="🛠 Insho v1", ic="bulb",
             hook="Eng yaxshi insholar ko'pincha katta voqeadan emas, kichik epizoddan boshlanadi: oshxonadagi suhbat, buzilgan velosiped, ukaga tushuntirilgan masala.",
             body="""<h4>Epizoddan ma'noga</h4>
<ol><li><b>Epizod</b>: aniq joy, vaqt va harakat. 2–3 jumla bilan sahna.</li>
<li><b>Fikr</b>: o'sha paytda nima o'ylagansiz, nima qiyin bo'lgan.</li>
<li><b>O'zgarish</b>: undan keyin nima qildingiz yoki qanday o'ylaydigan bo'ldingiz.</li>
<li><b>Ma'no</b>: bu sizning kimligingiz haqida nima deydi va kelajakka qanday bog'lanadi.</li></ol>
<h4>\"Ko'rsat, aytma\"</h4>
<div class="tbl"><table><thead><tr><th>Aytish</th><th>Ko'rsatish (Kompas tuzgan namuna)</th></tr></thead><tbody>
<tr><td>Men qiziquvchanman.</td><td>Radioni uchinchi marta ochganimda, onam vintlarni sanab qo'yadigan bo'ldi.</td></tr>
<tr><td>Men qat'iyatliman.</td><td>Dasturim 40-marta xato berganida, xatolarni daftarga yozishni boshladim.</td></tr>
</tbody></table></div>
<h4>Birinchi qoralama qoidasi</h4>
<p>Birinchi qoralama yaxshi bo'lishi shart emas. 650 so'zdan ko'p yozing, keyin qisqartirasiz. Bir o'tirishda yozing, tahrirni keyinga qoldiring.</p>
<div class="box warn">Boshqalarning inshosini o'qish foydali, lekin undan jumla, tuzilma yoki hikoya olmang. Platformalar o'xshashlikni tekshiradi (M10).</div>""",
             take="Hikoya: epizod → fikr → o'zgarish → ma'no. Xususiyatni aytmang, voqea orqali ko'rsating. Birinchi qoralamani tahrirsiz, bir o'tirishda yozing.",
             task="<ul><li>Hayotingizdan 5 ta kichik epizodni bitta jumladan yozing.</li><li>Eng kuchlisini tanlab, pastdagi vositada birinchi qoralamani yozing.</li></ul>",
             ph="1) ... 2) ... 3) ... 4) ... 5) ... Tanlov: ..."),
        dict(t="UCAS shaxsiy bayonoti", short="UCAS", min=30, kind="🗺 Uch savol", ic="scroll",
             hook="2026 yilda boshlanadigan qabuldan UCAS bayonoti erkin insho emas, uchta savolga javob. Bitta bayonot UK dagi barcha tanlovlaringizga boradi.",
             body=f"""<h4>Uch savol</h4>
<div class="tbl"><table><thead><tr><th>№</th><th>Savol (mazmuni)</th><th>Nima yozasiz</th></tr></thead><tbody>
<tr><td>1</td><td>Nega shu kurs yoki fanni o'qimoqchisiz?</td><td>Qiziqishingiz va uning kelib chiqishi (M3)</td></tr>
<tr><td>2</td><td>Malakalaringiz va o'qishingiz sizni bu kursga qanday tayyorladi?</td><td>Maktab fanlari, loyihalar, olimpiadalar</td></tr>
<tr><td>3</td><td>Ta'limdan tashqari yana nima qildingiz va bu tajriba nega foydali?</td><td>Faoliyatlar, ish, mustaqil o'qish (M7)</td></tr>
</tbody></table></div>
<h4>Chegaralar</h4>
<ul><li>Har javob kamida 350 belgi.</li><li>Jami 4 000 belgigacha (bo'sh joylar bilan).</li><li>Bitta bayonot barcha (odatda 5 tagacha) tanlovga boradi: shuning uchun tanlovlaringiz bir fan atrofida bo'lsin.</li></ul>
<p>Uslub: akademik va aniq. Fanga qiziqish dalil bilan: o'qigan kitob, qilgan tajriba, yechgan masala va undan nima o'rgandingiz.</p>
<div class="srcs">Manba: {UCAS_PS}; {THE_PS}. {HOL}.</div>""",
             take="UCAS 2026 qabulidan: uch savol, har biri kamida 350 belgi, jami 4 000 belgigacha. Bitta bayonot barcha UK tanloviga boradi.",
             task="<ul><li>Har savolga 3 tadan dalil yozing.</li><li>Pastdagi vositada uch javobning birinchi qoralamasini yozing (UK ga ariza bermasangiz, motivatsion xat uchun Kimlik → Dalil → Maqsad → Moslik rejasini yozing).</li></ul>",
             ph="1-savol dalillari: ... 2-savol: ... 3-savol: ..."),
        dict(t="Qo'shimcha insholar", short="Qo'shimcha", min=30, kind="🔎 Universitet tadqiqoti", ic="telescope",
             hook="\"Nega aynan bizning universitet?\" savoliga \"chunki u reytingda yuqori\" deb javob berish eng zaif javob. Komissiya siz universitetni o'rganganingizni ko'rmoqchi.",
             body="""<h4>Ikki asosiy savol</h4>
<ul><li><b>\"Nega aynan biz?\"</b> ([[Why us?]])</li><li><b>\"Nega bu mutaxassislik?\"</b> ([[Why this major?]])</li></ul>
<h4>Kuchli javob uchun manbalar</h4>
<div class="tbl"><table><thead><tr><th>Manba</th><th>Nima topasiz</th></tr></thead><tbody>
<tr><td>O'quv rejasi</td><td>Aniq fan nomlari va ular sizga nega kerak</td></tr>
<tr><td>Laboratoriya va tadqiqot sahifalari</td><td>Bakalavrlar qatnasha oladigan loyihalar</td></tr>
<tr><td>Talabalar tashkilotlari</td><td>Siz qo'shiladigan yoki davom ettiradigan faoliyat</td></tr>
<tr><td>Universitet o'quv modeli</td><td>Masalan, birinchi kurs seminarlari, amaliyot dasturi</td></tr>
</tbody></table></div>
<h4>Tekshiruv</h4>
<p>Javobingizdagi universitet nomini boshqa universitet nomi bilan almashtiring. Agar matn baribir to'g'ri bo'lsa, u juda umumiy.</p>
<div class="box warn">Universitet sahifasidan matnni ko'chirmang. Faktni o'z so'zingiz bilan va o'zingizga bog'lab yozing.</div>""",
             take="\"Nega biz?\" javobida aniq fanlar, laboratoriya va faoliyatlar bo'lsin. Universitet nomini almashtirganda matn noto'g'ri bo'lib qolishi kerak.",
             task="<ul><li>Portfelingizdagi qo'shimcha insho savollarini yozing (universitet, savol, so'z chegarasi).</li><li>Bitta \"Nega biz?\" uchun 3 ta aniq fakt va ularning sizga bog'liqligini yozing.</li></ul>",
             ph="... universiteti: \"...\" (250 so'z). Faktlar: 1) ... — chunki men ..."),
    ],
    tool=dict(id="insho", short="Insholar", h2="Insholar qoralamalari v1", sub="So'z va belgi hisoblagichi mo'ljalni ko'rsatadi. Bu birinchi qoralama: tahrir M10 da.",
              h3="Insho ish varag'i", tag="5 maydon", ic="memo", btn="Qoralamani saqlash", badge="Hikoyachi", min=2,
              pre="""<div class="box info" style="margin-bottom:12px">UCAS belgilarni bo'sh joylar bilan sanaydi. Pastdagi hisoblagich so'zni ko'rsatadi; belgilar soni pastda alohida chiqadi.</div><div id="ucasOut" class="out" style="white-space:normal">UCAS javoblari: 0 belgi</div>""",
              fields=[dict(k="ca", label="Common App asosiy inshosi v1", hint="250–650 so'z", type="area", wc="250-650", ph="..."),
                      dict(k="uq1", label="UCAS 1-savol: nega shu fan?", hint="kamida 350 belgi", type="area", ph="..."),
                      dict(k="uq2", label="UCAS 2-savol: o'qishim qanday tayyorladi?", hint="kamida 350 belgi", type="area", ph="..."),
                      dict(k="uq3", label="UCAS 3-savol: ta'limdan tashqari tayyorgarlik", hint="kamida 350 belgi", type="area", ph="..."),
                      dict(k="qosh", label="Qo'shimcha insholar rejasi", hint="universitet · savol · chegara · manbalar", type="area", ph="...")]),
    check=dict(h2="Insho nazorati", sub="Qoralamani tahrirga berishdan oldin tekshiring.", h3="9 bandlik nazorat",
               items=["Har universitet qaysi yozma hujjatni so'rashi aniq.", "Common App mavzulari joriy yil sahifasidan o'qilgan.",
                      "Insho aniq epizoddan boshlanadi.", "Xususiyatlar aytilmagan, voqea orqali ko'rsatilgan.",
                      "Insho M3 profilimga mos.", "UCAS javoblarining har biri kamida 350 belgi, jami 4 000 dan oshmaydi (kerak bo'lsa).",
                      "Qo'shimcha insholar uchun aniq universitet faktlari yig'ilgan.", "Hech qanday jumla boshqa matndan ko'chirilmagan.", "Matn meniki, AI yoki boshqa odam yozmagan."]),
    art_title="Insholar qoralamalari v1", art_short="Insholar",
    art=[("Platformalar va talab qilinadigan matnlar", ["a1"]), ("Mavzu tanlovi va hikoya", ["a2", "a3"]), ("Common App asosiy inshosi v1", ["ca"]),
         ("UCAS 1-savol", ["uq1"]), ("UCAS 2-savol", ["uq2"]), ("UCAS 3-savol", ["uq3", "a4"]), ("Qo'shimcha insholar rejasi", ["qosh", "a5"])],
    tip="Qoralamani yozgach, uni 2–3 kun ochmang. Keyin ovoz chiqarib o'qing: qoqilgan joylar tahrir talab qiladigan joylar.",
    sources=f"{CA_ESSAY}; {UCAS_PS}; {THE_PS}. {STD}",
    js="""window.KGTool = { init: function () {
  var o = document.getElementById("ucasOut");
  function run() {
    var n = [1, 2, 3].map(function (i) { return String(KG.nv("uq" + i)).length; }), t = n[0] + n[1] + n[2];
    var low = n.filter(function (x) { return x > 0 && x < 350; }).length;
    o.innerHTML = "UCAS javoblari: <b>" + t + "</b> / 4000 belgi (1: " + n[0] + ", 2: " + n[1] + ", 3: " + n[2] + ")" + (t > 4000 ? " <span class=\\"pill no\\">chegaradan oshdi</span>" : "") + (low ? " <span class=\\"pill chk\\">" + low + " ta javob 350 dan qisqa</span>" : "");
  }
  ["uq1", "uq2", "uq3"].forEach(function (k) { var el = document.querySelector("[data-save=\\"" + k + "\\"]"); if (el) el.addEventListener("input", function () { setTimeout(run, 400); }); });
  run();
} };""",
)
