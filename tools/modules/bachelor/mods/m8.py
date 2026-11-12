from common import CA, UCAS, UCAS_INT, HOL, STD

MOD = dict(
    title="Tavsiya xatlari",
    desc="Bachelor Lab M8: kuchli tavsiya xati, o'qituvchidan so'rash, yutuqlar varaqasi (Brag Sheet), Common App va UCAS'da tavsiya jarayoni, maktab maslahatchisi bo'lmaganda. Natija: yutuqlar varaqasi, 2–3 tavsiya so'rovi va aloqalar jadvali.",
    lead="Tavsiya xati sizni boshqa odam ko'zi bilan ko'rsatadi. Uni o'zingiz yozmaysiz, lekin uning kuchli bo'lishiga ta'sir qila olasiz: to'g'ri odamni tanlash, vaqtida so'rash va faktlar bilan ta'minlash orqali.",
    hero="memo", weeks="2", next="M9 Shaxsiy bayonot va insholar", next_href="bachelor-lab-m9.html",
    goals=[("memo", "Yutuqlar varaqasi (Brag Sheet)", "tavsiya beruvchiga beriladigan faktlar va epizodlar"),
           ("bell", "2–3 tavsiya so'rovi", "kimga, qachon, qanday"),
           ("scroll", "Aloqalar jadvali", "tavsiya beruvchilar, muddatlar, holat")],
    warn="Tavsiya xatini o'zingiz yozib, o'qituvchiga imzolatsangiz, bu akademik halollikni buzadi va platformalar qoidalariga zid. Bu modulda faqat tavsiya beruvchiga faktlar berish o'rgatiladi.",
    lessons=[
        dict(t="Kuchli tavsiya xati", short="Kuchli xat", min=25, kind="🎯 Mini-test", ic="memo",
             hook="\"U a'lochi va mehnatkash o'quvchi\" degan xatni komissiya minglab o'qigan. Kuchli xat aniq epizod va kuzatilgan dalil bilan ajralib turadi.",
             body="""<h4>Kuchsiz va kuchli xat</h4>
<div class="tbl"><table><thead><tr><th>Kuchsiz</th><th>Kuchli</th></tr></thead><tbody>
<tr><td>Umumiy maqtov: \"aqlli, mehnatkash, faol\"</td><td>Aniq epizod: \"Darsdagi masalani uch xil usulda yechib, sinfga tushuntirib berdi\"</td></tr>
<tr><td>Baholarni takrorlash</td><td>Baholarda ko'rinmaydigan sifat: savol berish, xatodan keyin qayta urinish</td></tr>
<tr><td>Solishtirishsiz</td><td>Kontekst bilan: \"20 yillik ishimdagi eng kuchli 5 o'quvchidan biri\" (agar haqiqat bo'lsa)</td></tr>
<tr><td>Qisqa, shablon</td><td>Shaxsiy, tavsiya beruvchi sizni yaqindan bilishi ko'rinadi</td></tr>
</tbody></table></div>
<h4>Kim yozishi kerak</h4>
<ul><li>Sizni darsda yaqindan bilgan o'qituvchi, ayniqsa sohangizga yaqin fan bo'yicha.</li><li>Oxirgi 1–2 yilda dars bergan bo'lsa yaxshiroq.</li><li>Lavozimi baland, lekin sizni bilmaydigan odam (masalan direktor) kuchsizroq xat yozadi.</li></ul>
<div class="box info">Xatni siz ko'rmaysiz: platformalar odatda xatni ko'rish huquqidan voz kechishni ([[waive right to access]]) taklif qiladi. Komissiya voz kechilgan xatga ko'proq ishonadi.</div>""",
             take="Kuchli xat aniq epizod, baholarda ko'rinmaydigan sifat va kontekst bilan yoziladi. Sizni yaqindan biladigan o'qituvchini tanlang.",
             quiz=[("Direktor yozgan xat har doim o'qituvchi xatidan kuchli.", "n", "Noto'g'ri: sizni yaqindan bilgan o'qituvchi aniqroq dalil beradi."),
                   ("Kuchli xatda aniq epizodlar bo'ladi.", "t", "To'g'ri: kuzatilgan voqea umumiy maqtovdan ishonchliroq."),
                   ("Xatni o'zim yozib, o'qituvchiga imzolatsam bo'ladi.", "n", "Noto'g'ri: bu akademik halollikni buzadi."),
                   ("Xatni ko'rish huquqidan voz kechish komissiya ishonchini oshirishi mumkin.", "t", "To'g'ri: xat ochiqroq yozilgan deb hisoblanadi.")],
             task="<ul><li>3 nomzod tavsiya beruvchini yozing.</li><li>Har biri sizni qaysi aniq epizod orqali biladi, yozing.</li></ul>",
             ph="1) ... (fizika o'qituvchisi, 2 yil): epizod — ... 2) ..."),
        dict(t="O'qituvchidan so'rash", short="So'rov", min=25, kind="🛠 So'rov", ic="bell",
             hook="O'qituvchi bir vaqtda bir nechta o'quvchiga xat yozishi mumkin. Kech so'rov shoshilgan va umumiy xatga olib keladi.",
             body="""<h4>Qachon</h4>
<p>Birinchi muddatdan kamida <b>6–8 hafta oldin</b>. Erta qaror yoki UCAS erta muddati bo'lsa, undan ham oldin.</p>
<h4>Qanday</h4>
<ol><li><b>Avval og'zaki</b>: shaxsan so'rang, rad etish imkonini qoldiring: \"Siz menga kuchli xat yoza olasizmi?\"</li>
<li><b>Keyin yozma</b>: qisqa xat bilan yutuqlar varaqasi (L3), universitetlar ro'yxati, muddatlar va topshirish usuli.</li>
<li><b>Eslatma</b>: muddatdan 2 hafta va 3 kun oldin muloyim eslatma.</li>
<li><b>Rahmat</b>: natijadan qat'i nazar yozma rahmat va natija haqida xabar.</li></ol>
<h4>Ingliz tilida xat kerak bo'lsa</h4>
<p>O'qituvchi ingliz tilini bilmasligi mumkin. Variantlar: o'qituvchi o'zbekcha yozadi va xat professional tarjimon tomonidan tarjima qilinadi (ba'zi universitetlar tarjima tasdig'ini so'raydi); yoki ingliz tili o'qituvchisi tarjimada yordam beradi. Tarjimani siz qilmang: bu mustaqillikka shubha uyg'otadi. Universitetning tarjima qoidasini oldindan tekshiring.</p>
<div class="box warn">O'qituvchi \"o'zing yozib kel, men imzolayman\" desa, muloyim rad eting va yutuqlar varaqasini taklif qiling. Bu sizni ham, o'qituvchini ham himoya qiladi.</div>""",
             take="Muddatdan 6–8 hafta oldin, avval og'zaki, keyin yozma so'rang; eslatma va rahmat yuboring. Tarjima kerak bo'lsa, uni o'zingiz qilmang.",
             task="<ul><li>Tanlagan tavsiya beruvchilar uchun so'rov sanasini belgilang.</li><li>Yozma so'rov xatining asosiy 5 jumlasini yozing.</li></ul>",
             ph="So'rov sanasi: ... Xat: Hurmatli ..., ... universitetlariga ariza beryapman ..."),
        dict(t="Yutuqlar varaqasi", short="Brag Sheet", min=30, kind="📋 1 sahifa", ic="scroll",
             hook="O'qituvchi sizni yaxshi biladi, lekin hamma narsani eslamaydi. Yutuqlar varaqasi unga aniq faktlar va epizodlarni eslatadi.",
             body="""<h4>Yutuqlar varaqasi ([[Brag Sheet]]) tarkibi</h4>
<ol><li><b>Asosiy ma'lumot</b>: ism, sinf, sohangiz, universitetlar va muddatlar.</li>
<li><b>Bir jumlali profil</b> (M3).</li>
<li><b>Siz va o'qituvchi</b>: qaysi fan, necha yil, qaysi loyiha yoki tanlovda birga ishlagansiz.</li>
<li><b>2–3 epizod</b>: o'qituvchi o'zi ko'rgan aniq voqealar (sana yoki dars bilan). O'qituvchi tasdiqlay oladigan voqealarni yozing.</li>
<li><b>Yutuqlar</b>: eng muhim 3–5 tasi (M6 formatida).</li>
<li><b>Nima ta'kidlanishi foydali</b>: masalan \"mustaqil o'rganish\" yoki \"jamoada ishlash\", lekin tayyor jumla emas.</li></ol>
<p>Hajmi: 1 sahifa. Ko'proq bo'lsa, o'qituvchi uni o'qimaydi.</p>
<div class="box info">Varaqa faktlar beradi, matn emas. O'qituvchi o'z so'zlari bilan yozadi. Varaqadagi har gap o'qituvchi tasdiqlay oladigan narsa bo'lsin.</div>""",
             take="Yutuqlar varaqasi 1 sahifa: profil, o'qituvchi bilan aloqangiz, 2–3 epizod, yutuqlar. Faktlar beradi, tayyor matn emas.",
             task="<ul><li>Bitta tavsiya beruvchi uchun yutuqlar varaqasini yozing.</li><li>O'qituvchi o'zi ko'rgan 2–3 epizodni sanasi bilan kiriting.</li></ul>",
             ph="Ism: ... Soha: ... Siz va men: ... Epizod 1: ... Epizod 2: ... Yutuqlar: ..."),
        dict(t="Platformalarda tavsiya jarayoni", short="Platforma", min=25, kind="🗺 Jarayon", ic="compass",
             hook="Common App'da uch xil rol bor, UCAS'da bitta umumiy tavsiya. Kim nimani yuborishini bilmasangiz, ariza to'liq bo'lmaydi.",
             body=f"""<div class="tbl"><table><thead><tr><th>Platforma</th><th>Kim nima yuboradi</th></tr></thead><tbody>
<tr><td>Common App</td><td><b>Maktab maslahatchisi</b> ([[school counselor]]): maktab hisoboti ([[school report]]), maktab haqida ma'lumot ([[school profile]]), transkript va maslahatchi tavsiyasi. <b>O'qituvchilar</b> ([[teacher evaluations]]): odatda 1–2 ta. <b>Boshqa tavsiya beruvchilar</b>: ba'zi universitetlarda ixtiyoriy (masalan murabbiy, ish beruvchi)</td></tr>
<tr><td>UCAS</td><td>Bitta umumiy tavsiya ([[reference]]) maktab yoki tavsiya beruvchi tomonidan UCAS tizimiga kiritiladi. Xalqaro abituriyent maktabi UCAS'ga ulanmagan bo'lsa, \"individual\" ariza va tashqi tavsiya beruvchi orqali</td></tr>
<tr><td>To'g'ridan-to'g'ri portallar</td><td>Universitet havola yuboradi yoki skanerlangan imzolangan xatni yuklashni so'raydi</td></tr>
</tbody></table></div>
<h4>Texnik qadamlar</h4>
<ul><li>Platformada tavsiya beruvchining email manzilini aniq kiriting; u havola orqali yuklaydi.</li><li>Tavsiya beruvchiga platforma qanday ishlashini qisqa yo'riqnoma bilan tushuntiring.</li><li>Nazorat jadvalida holatni kuzating: taklif yuborildi, qabul qilindi, yuklandi.</li></ul>
<div class="srcs">Manba: {CA}; {UCAS}; {UCAS_INT}. {HOL}.</div>""",
             take="Common App: maslahatchi, 1–2 o'qituvchi va ixtiyoriy boshqa tavsiya; UCAS: bitta umumiy tavsiya; portallar: havola yoki yuklash. Holatni jadvalda kuzating.",
             task="<ul><li>Har platformangiz uchun kim qaysi rolni bajarishini yozing.</li><li>Tavsiya beruvchilar uchun 5 qadamlik qisqa yo'riqnoma tuzing.</li></ul>",
             ph="Common App: maslahatchi — ..., o'qituvchi 1 — ..., o'qituvchi 2 — ... UCAS: ..."),
        dict(t="Maktab maslahatchisi bo'lmasa", short="Maslahatchi", min=25, kind="🧭 Yechim", ic="shield",
             hook="O'zbekiston maktablarining ko'pida \"maktab maslahatchisi\" lavozimi yo'q. Lekin Common App bu rolni so'raydi. Kimdir uni bajarishi kerak.",
             body="""<h4>Kim bajarishi mumkin</h4>
<ul><li>Direktor yoki direktor o'rinbosari (o'quv ishlari bo'yicha).</li><li>Sinf rahbari.</li><li>Maktab psixologi yoki karyera bo'yicha mas'ul xodim.</li></ul>
<p>Muhimi: bu odam maktab nomidan rasmiy hujjat (transkript, maktab hisoboti) yubora olishi va platformada hisob ochishi kerak.</p>
<h4>Maktabni qanday tayyorlash</h4>
<ol><li>Erta uchrashing (birinchi muddatdan 2–3 oy oldin): maqsadingiz va platformani tushuntiring.</li>
<li>Maktab haqida ma'lumot ([[school profile]]) qoralamasini birga tayyorlang: maktab turi, o'quvchilar soni, baholash shkalasi, fanlar. Uni maktab tasdiqlaydi va yuboradi.</li>
<li>Bitta mas'ul odam va zaxira odamni kelishib oling.</li>
<li>Platforma yo'riqnomasini o'zbek tilida qisqa qilib bering.</li></ol>
<div class="box warn">Maslahatchi hisobini o'zingiz ochib, o'zingiz to'ldirmang. Rasmiy hujjat maktab vakili tomonidan yuborilishi kerak; aks holda bu firibgarlik deb baholanishi mumkin.</div>""",
             take="Maslahatchi rolini direktor o'rinbosari yoki sinf rahbari bajarishi mumkin. Erta uchrashing, maktab ma'lumotini birga tayyorlang, lekin hisobni o'zingiz to'ldirmang.",
             task="<ul><li>Maktabingizda maslahatchi rolini kim bajarishi mumkinligini aniqlang.</li><li>U bilan uchrashuv sanasi va olib boradigan hujjatlar ro'yxatini yozing.</li></ul>",
             ph="Mas'ul: ... Zaxira: ... Uchrashuv: ... Olib boraman: ..."),
    ],
    tool=dict(id="aloqa", short="Aloqalar", h2="Aloqalar jadvali va so'rovlar", sub="Tavsiya beruvchilar, rollar, muddatlar va holat bitta joyda.",
              h3="Aloqalar jadvali", tag="5 maydon", ic="scroll", btn="Jadvalni saqlash", badge="Tavsiya rejachisi", min=4,
              fields=[dict(k="t1", label="1-tavsiya beruvchi", hint="ism · lavozim · fan · necha yil · rol · so'rov sanasi · holat", type="area", ph="..."),
                      dict(k="t2", label="2-tavsiya beruvchi", type="area", ph="..."),
                      dict(k="t3", label="Maslahatchi yoki 3-tavsiya beruvchi", type="area", ph="..."),
                      dict(k="brag", label="Yutuqlar varaqasi (qisqa)", type="area", wc="150-400", ph="Profil ... Epizodlar ... Yutuqlar ..."),
                      dict(k="eslatma", label="Eslatma va rahmat rejasi", ph="Muddatdan 2 hafta va 3 kun oldin; natijadan keyin rahmat")]),
    check=dict(h2="Tavsiya nazorati", sub="Topshirishdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Tavsiya beruvchilar meni aniq epizodlar orqali biladi.", "So'rov muddatdan kamida 6–8 hafta oldin.",
                      "Har biriga yutuqlar varaqasi berilgan, tayyor matn emas.", "Platformada email manzillar to'g'ri kiritilgan.",
                      "Maslahatchi roli kelishilgan va zaxira odam bor.", "Tarjima kerak bo'lsa, uni men qilmayman.",
                      "Holat nazorat jadvalida kuzatiladi.", "Natijadan qat'i nazar rahmat yuboriladi."]),
    art_title="Yutuqlar varaqasi va aloqalar jadvali", art_short="Varaqa",
    art=[("Tavsiya beruvchilar tanlovi", ["a1"]), ("1-tavsiya beruvchi", ["t1"]), ("2-tavsiya beruvchi", ["t2"]), ("Maslahatchi yoki 3-tavsiya", ["t3", "a5"]),
         ("Yutuqlar varaqasi", ["brag", "a3"]), ("So'rov va platforma jarayoni", ["a2", "a4"]), ("Eslatma va rahmat", ["eslatma"])],
    tip="O'qituvchiga so'rovni tanaffusda yo'l-yo'lakay emas, oldindan kelishilgan qisqa uchrashuvda ayting. Bu sizning jiddiyligingizni ko'rsatadi.",
    sources=f"{CA}; {UCAS}; {UCAS_INT}. {STD}",
)
