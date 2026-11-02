from common import CA, UCAS_PS, HOL, STD

MOD = dict(
    title="Darsdan tashqari faoliyat",
    desc="Bachelor Lab M7: darsdan tashqari faoliyat turlari, STEM uchun kuchli faoliyatlar, ijtimoiy faoliyat va yetakchilik, yozgi dasturlar, faoliyatlar ro'yxatini yozish. Natija: 10 yozuvli faoliyatlar ro'yxati va izchil hikoya xaritasi.",
    lead="Darsdan tashqari faoliyat sizning vaqtingizni qanday ishlatishingizni ko'rsatadi. Ko'p faoliyat emas, chuqur va davomli faoliyat kuchli. Bu modulda faoliyatlaringizni saralaysiz va ularni Common App formatida yozasiz.",
    hero="seedling", weeks="1–2", next="M8 Tavsiya xatlari", next_href="bachelor-lab-m8.html",
    goals=[("seedling", "Faoliyatlar ro'yxati", "10 yozuv, har biri qisqa tavsif bilan"),
           ("compass", "Izchil hikoya xaritasi", "faoliyatlar M3 profilingiz bilan qanday bog'langan"),
           ("calendar", "Keyingi 6 oy rejasi", "bitta faoliyatni chuqurlashtirish")],
    warn=f"Common App faoliyatlar bo'limining belgi chegaralari va formati yillar bo'yicha o'zgarishi mumkin; yozishdan oldin joriy yil yo'riqnomasini tekshiring ({HOL}).",
    lessons=[
        dict(t="Nima darsdan tashqari faoliyat hisoblanadi", short="Faoliyat", min=20, kind="🎯 Mini-test", ic="seedling",
             hook="Ko'p o'quvchilar \"menda faoliyat yo'q\" deydi, chunki faqat to'garak va tanlovlarni hisoblaydi. Aslida oilaviy majburiyat va ish ham faoliyat.",
             body="""<h4>Faoliyat turlari</h4>
<ul><li><b>To'garak va klub</b>: maktab yoki tashqi.</li><li><b>Sport va san'at</b>: muntazam mashg'ulot, jamoa, musobaqa.</li>
<li><b>Ish</b>: haq to'lanadigan ish, oilaviy biznesda yordam.</li><li><b>Oilaviy majburiyat</b>: ukalarga qarash, uy ishlarida katta mas'uliyat. Common App bu turni alohida qabul qiladi.</li>
<li><b>Mustaqil loyiha</b>: dastur, sayt, tadqiqot, kanal.</li><li><b>Ko'ngillilik</b>: mahalla, xayriya, maktab tadbirlari.</li></ul>
<h4>Komissiya nimaga qaraydi</h4>
<p>Vaqt (haftasiga necha soat, necha yil), rol va mas'uliyat, natija. Haftasiga 10 soat oila biznesida ishlagan o'quvchi bir martalik tadbirga borgan o'quvchidan ko'ra kuchliroq dalil beradi.</p>
<div class="box info">Oilaviy majburiyat tufayli to'garaklarga vaqtingiz bo'lmagan bo'lsa, buni faoliyat sifatida yozing. Bu kontekst, uzr emas.</div>""",
             take="Faoliyat faqat to'garak emas: ish, oilaviy majburiyat, mustaqil loyiha ham hisoblanadi. Komissiya vaqt, rol va natijaga qaraydi.",
             quiz=[("Ukalaringizga muntazam qarash darsdan tashqari faoliyat sifatida yozilishi mumkin.", "t", "To'g'ri: Common App oilaviy majburiyatni faoliyat turi sifatida qabul qiladi."),
                   ("Faoliyatlar soni qancha ko'p bo'lsa, ariza shuncha kuchli.", "n", "Noto'g'ri: chuqurlik va davomiylik muhimroq."),
                   ("Haq to'lanadigan ish faoliyat hisoblanmaydi.", "n", "Noto'g'ri: ish ham faoliyat va mas'uliyatni ko'rsatadi."),
                   ("Komissiya faoliyatga sarflangan vaqtni ham ko'radi.", "t", "To'g'ri: haftasiga soat va yillar soni so'raladi.")],
             task="<ul><li>Oxirgi 3–4 yildagi barcha faoliyatlaringizni turlari bo'yicha yozing (kamida 8 ta).</li><li>Har biri uchun haftasiga soat va yillar sonini qo'shing.</li></ul>",
             ph="1) Matematika to'garagi — 3 soat/hafta, 2 yil 2) Oilaviy do'kon — ..."),
        dict(t="STEM uchun kuchli faoliyatlar", short="STEM", min=25, kind="🔬 Chuqurlik", ic="telescope",
             hook="10 ta qisqa faoliyatdan ko'ra 2–3 yil davom etgan bitta loyiha kuchliroq. Chuqurlik qiziqishning haqiqiyligini ko'rsatadi.",
             body="""<h4>Chuqurlik va davomiylik</h4>
<div class="tbl"><table><thead><tr><th>Kuchsiz</th><th>Kuchli</th></tr></thead><tbody>
<tr><td>Bir martalik hackathon ishtiroki</td><td>Hackathon'dan keyin loyihani 6 oy davom ettirib, foydalanuvchilarga chiqarish</td></tr>
<tr><td>Robototexnika to'garagiga a'zolik</td><td>To'garakda kichik guruhni boshqarish va tanlovga tayyorlash</td></tr>
<tr><td>Ko'p onlayn kurs</td><td>Bitta kurs asosida maktab muammosini hal qiluvchi dastur</td></tr>
</tbody></table></div>
<h4>STEM faoliyat g'oyalari</h4>
<ul><li>Maktab yoki mahalla uchun dastur, sayt yoki bot.</li><li>Fan olimpiadasiga tayyorlanish va kichik o'quvchilarni o'qitish.</li><li>Kichik tajriba yoki o'lchov loyihasi (M6 L3).</li><li>O'zbek tilida fan bo'yicha ochiq materiallar yaratish.</li></ul>
<p>Mezon: siz nimani yaratdingiz yoki o'zgartirdingiz, va buni kim ko'ra oladi?</p>
<div class="box warn">Faoliyatni faqat ariza uchun boshlash 2–3 oy oldin ko'rinib qoladi. Qiziqishingiz bilan bog'liq bitta ishni hozirdan boshlang va davom ettiring.</div>""",
             take="Chuqur va davomli faoliyat ko'p qisqa faoliyatdan kuchli. Mezon: nima yaratdingiz yoki o'zgartirdingiz va buni kim ko'ra oladi.",
             task="<ul><li>Faoliyatlaringizdan eng chuqur 2 tasini tanlang.</li><li>Har birini keyingi 6 oyda qanday chuqurlashtirishingizni yozing.</li></ul>",
             ph="1) ... → keyingi 6 oy: ... 2) ..."),
        dict(t="Ijtimoiy faoliyat va yetakchilik", short="Yetakchilik", min=20, kind="🧭 Natija", ic="compass",
             hook="\"Sinf sardori edim\" lavozim, yetakchilik emas. Yetakchilik siz tufayli nima o'zgarganida ko'rinadi.",
             body="""<h4>Lavozim va natija</h4>
<p>Komissiya lavozim nomiga emas, natijaga qaraydi. Bir xil lavozimning ikki tavsifi (Kompas tuzgan namuna):</p>
<div class="tbl"><table><thead><tr><th>Kuchsiz</th><th>Kuchli</th></tr></thead><tbody>
<tr><td>Maktab kengashi a'zosi.</td><td>Maktab kengashida kutubxona ochiq soatlarini 2 soatga uzaytirishni taklif qilib, ma'muriyat bilan kelishdim; haftasiga ~40 o'quvchi foydalanadi.</td></tr>
</tbody></table></div>
<h4>Yetakchilik turlari</h4>
<ul><li><b>Tashkiliy</b>: tadbir, to'garak, guruhni tashkil qilish.</li><li><b>Ta'limiy</b>: boshqalarni o'qitish, materiallar yaratish.</li><li><b>Tashabbus</b>: muammoni ko'rib, hal qilishni boshlash.</li></ul>
<h4>Ijtimoiy faoliyat</h4>
<p>Ko'ngillilik soatlarining ko'pligi emas, muntazamligi va natijasi muhim. Bir martalik aksiyadan ko'ra bir yil davom etgan yordam kuchliroq.</p>
<div class="box info">Raqam yozsangiz, uni qanday bilganingizni ayta olishingiz kerak (masalan, ro'yxatga olish daftari).</div>""",
             take="Yetakchilik lavozim emas, siz tufayli bo'lgan o'zgarish. Tashkiliy, ta'limiy yoki tashabbus yetakchiligini natija bilan yozing.",
             task="<ul><li>Bitta yetakchilik yoki ijtimoiy faoliyatingizni \"kuchsiz\" va \"kuchli\" ko'rinishda yozing.</li><li>Natijani qanday tasdiqlay olishingizni yozing.</li></ul>",
             ph="Kuchsiz: ... Kuchli: ... Tasdiq: ..."),
        dict(t="Yozgi dasturlar", short="Yozgi", min=20, kind="⚖️ Saralash", ic="money",
             hook="Ba'zi yozgi dasturlar katta pul turadi va \"top universitetda o'qish\" va'da qiladi. Lekin pullik dasturning o'zi qabul komissiyasi uchun qabulda ustunlik bermaydi.",
             body="""<h4>Ikki tur</h4>
<div class="tbl"><table><thead><tr><th></th><th>Tanlovli dastur</th><th>Pullik dastur</th></tr></thead><tbody>
<tr><td>Kirish</td><td>Ariza, tanlov, ko'pincha past qabul foizi</td><td>To'lov qilgan hamma qatnashadi</td></tr>
<tr><td>Narx</td><td>Ko'pincha bepul yoki stipendiyali</td><td>Qimmat</td></tr>
<tr><td>Signal</td><td>Kuchli: siz tanlovdan o'tgansiz</td><td>Kuchsiz: faqat to'lov qobiliyatini ko'rsatadi</td></tr>
</tbody></table></div>
<h4>Muqobillar</h4>
<ul><li>O'zbekistondagi universitet yoki laboratoriyada yozgi amaliyot.</li><li>Mustaqil loyiha (M6 L3, M7 L2).</li><li>Ish yoki oilaviy biznesda mas'uliyat.</li><li>Bepul onlayn yozgi maktablar (tanlovli bo'lsa).</li></ul>
<div class="box warn">\"Bu dastur qabulni kafolatlaydi\" yoki \"universitet tavsiya xati beradi\" degan va'dalarga ishonmang. Universitet nomi ostida o'tadigan pullik dastur ko'pincha qabul bo'limi bilan bog'liq emas.</div>""",
             take="Tanlovli yozgi dastur muhim dalil, pullik dasturning o'zi qabulda ustunlik bermaydi. Muqobil: amaliyot, mustaqil loyiha, ish.",
             task="<ul><li>Keyingi yoz uchun 2 ta tanlovli yoki bepul imkoniyat toping.</li><li>Ularning ariza muddatini va tanlov mezonini yozing.</li></ul>",
             ph="1) ... — muddat: ..., mezon: ... 2) ..."),
        dict(t="Faoliyatlar ro'yxatini yozish", short="Ro'yxat", min=30, kind="🛠 10 yozuv", ic="memo",
             hook="Common App'da har faoliyat uchun bor-yo'g'i 150 belgi. Shu joyda nima qilganingiz va natijasini aytish alohida ko'nikma.",
             body=f"""<h4>Common App formati</h4>
<ul><li>10 tagacha faoliyat.</li><li>Lavozim yoki rol: qisqa (50 belgigacha).</li><li>Tashkilot nomi: 100 belgigacha.</li><li>Tavsif: 150 belgigacha.</li><li>Sinflar, haftasiga soat, yiliga hafta, kollejda davom ettirish niyati.</li></ul>
<h4>Yozish qoidalari</h4>
<ol><li><b>Fe'l bilan boshlang</b>: \"Tashkil qildim\", \"Yozdim\", \"O'qitdim\". Ingliz tilida: [[Founded, Built, Taught]].</li><li><b>Raqam qo'shing</b>: nechta odam, nechta soat, qanday natija.</li><li><b>\"Men\" va to'liq gaplarni tejang</b>: belgi chegarasi uchun.</li><li><b>Eng muhimini birinchi qo'ying</b>: tartib muhimlik bo'yicha.</li></ol>
<p>Kompas tuzgan namuna (inglizcha, 150 belgigacha): <span lang="en">Built a Telegram bot that sends homework reminders to 120 students; maintained it for 2 years; teachers now use it in 4 classes.</span></p>
<h4>UCAS va boshqa platformalar</h4>
<p>UCAS'da alohida faoliyatlar ro'yxati yo'q: faoliyatlar shaxsiy bayonotning uchinchi savoliga (ta'limdan tashqari tayyorgarlik) kiradi. To'g'ridan-to'g'ri portallar ko'pincha CV so'raydi (M6).</p>
<div class="srcs">Manba: {CA}; {UCAS_PS}. {HOL}.</div>""",
             take="Common App: 10 faoliyat, tavsif 150 belgigacha. Fe'l bilan boshlang, raqam qo'shing, eng muhimini birinchi qo'ying.",
             task="<ul><li>Eng muhim 10 faoliyatingizni tartiblang.</li><li>Pastdagi vositada har birining 150 belgilik tavsifini yozing.</li></ul>",
             ph="1) Rol: ... · Tashkilot: ... · Tavsif: ..."),
    ],
    tool=dict(id="royxat", short="Ro'yxat", h2="Faoliyatlar ro'yxati", sub="10 yozuv, muhimlik tartibida. Har tavsif 150 belgigacha (inglizcha yoki o'zbekcha qoralama).",
              h3="Faoliyatlar ro'yxati (Activities List)", tag="5 maydon", ic="memo", btn="Ro'yxatni saqlash", badge="Faoliyat me'mori", min=4,
              fields=[dict(k="f13", label="1–3 faoliyat (eng muhim)", hint="rol · tashkilot · tavsif · soat/hafta · yil", type="area", ph="..."),
                      dict(k="f46", label="4–6 faoliyat", type="area", ph="..."),
                      dict(k="f710", label="7–10 faoliyat", type="area", ph="..."),
                      dict(k="xarita", label="Izchil hikoya xaritasi", hint="faoliyatlar M3 profilingiz bilan qanday bog'langan", type="area", ph="Profil: ... ; bog'lovchi faoliyatlar: ..."),
                      dict(k="reja", label="Keyingi 6 oy rejasi", type="area", ph="Qaysi faoliyatni qanday chuqurlashtiraman ...")]),
    check=dict(h2="Faoliyatlar nazorati", sub="Ro'yxatni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Ro'yxat muhimlik tartibida.", "Har tavsif fe'l bilan boshlanadi.", "Har tavsifda natija yoki raqam bor.",
                      "Tavsiflar 150 belgidan oshmaydi.", "Soat va yillar real, oshirilmagan.", "Oilaviy majburiyat va ish ham hisobga olingan.",
                      "Kamida bitta faoliyat 1 yildan ortiq davom etgan.", "Har raqamni qanday bilganimni ayta olaman."]),
    art_title="Faoliyatlar ro'yxati va hikoya xaritasi", art_short="Ro'yxat",
    art=[("Faoliyatlar 1–3", ["f13"]), ("Faoliyatlar 4–6", ["f46"]), ("Faoliyatlar 7–10", ["f710"]), ("Yetakchilik va ijtimoiy faoliyat", ["a3"]),
         ("Izchil hikoya xaritasi", ["xarita", "a2"]), ("Keyingi 6 oy rejasi", ["reja", "a4"])],
    tip="Tavsifni yozib bo'lgach, undan bitta so'zni olib tashlang. Agar ma'no o'zgarmasa, o'sha so'z ortiqcha edi.",
    sources=f"{CA}; {UCAS_PS}. {STD}",
    js="""window.KGTool = { check: function () {
  var long = [];
  ["f13", "f46", "f710"].forEach(function (k) {
    String(KG.nv(k)).split(/\\n+/).forEach(function (line) {
      var m = line.match(/tavsif\\s*:\\s*(.+)$/i);
      var t = m ? m[1] : "";
      if (t && t.length > 150) long.push(t.slice(0, 24) + "…");
    });
  });
  return long.length ? ("150 belgidan uzun tavsif: " + long.length + " ta") : "";
} };""",
)
