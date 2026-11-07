from common import LEEDS, UKRI, MSCA, EURAXESS, DORA, HOL, STD

MOD = dict(
    title="Doktorantura tizimlari va universitet tanlash",
    desc="PhD Lab M2: PhD modellari (o'zi taklif qilgan loyiha, e'lon qilingan moliyalashtirilgan loyiha, doktorlik dasturi, maoshli lavozim), imkoniyat qidirish tizimi, ilmiy muhitni baholash, muvofiqlik va muddatlar. Natija: 8–12 imkoniyatli saralangan ro'yxat va 4 ta ustuvor ariza.",
    lead="Bir xil “PhD” nomi ortida turli tizimlar turadi. Bu modulda nom va reytingga emas, ilmiy moslik, moliya va rasmiy muvofiqlikka qarab 8–12 imkoniyat topasiz va ulardan 4 tasini ustuvor arizaga ajratasiz.",
    hero="phd", weeks="2", next="M3 Ilmiy rahbar va laboratoriya bilan aloqa", next_href="phd-lab-o.html?m=3",
    goals=[("chart", "Saralangan ro'yxat (Shortlist)", "8–12 imkoniyat, har biri rasmiy havola va tekshirilgan sana bilan"),
           ("shield", "Muvofiqlik matritsasi", "“majburiy” va “afzal” bandlar ajratilgan"),
           ("calendar", "Teskari kalendar", "tashqi va ichki muddatlar, 7 kunlik zaxira")],
    warn="Universitet tanlashning umumiy usullari Master Lab M1 da. Bu yerda faqat doktorantura tizimlari. Har bir shartni tanlangan dastur sahifasidan tekshiring: mamlakat haqidagi umumiy maqola yetarli emas.",
    lessons=[
        dict(t="To'rtta PhD modeli", short="Modellar", min=30, kind="🧭 Xarita", ic="compass",
             hook="Bitta mamlakat ichida ham PhD turlicha tashkil qilinadi. Modelni bilmasangiz, arizani noto'g'ri joyga yoki noto'g'ri tartibda yuborasiz.",
             body=f"""<div class="tbl"><table><thead><tr><th>Model</th><th>Ariza kimga</th><th>Moliya qachon hal bo'ladi</th></tr></thead><tbody>
<tr><td>O'zi taklif qilgan loyiha ([[self-proposed]])</td><td>Universitet, ilmiy loyiha taklifi bilan</td><td>Ko'pincha alohida tanlovda</td></tr>
<tr><td>E'lon qilingan moliyalashtirilgan loyiha ([[funded project]])</td><td>E'londagi loyiha va rahbar</td><td>E'lon bilan birga</td></tr>
<tr><td>Doktorlik dasturi ([[doctoral training programme]], kohorta)</td><td>Dastur yoki markaz</td><td>Dastur o'rinlari bilan</td></tr>
<tr><td>Maoshli doktorlik lavozimi</td><td>Ish beruvchi (universitet yoki institut)</td><td>Ish shartnomasi bilan</td></tr>
</tbody></table></div>
<p>Har modelda arizani kim qabul qiladi, rahbar roli, loyiha doirasi va moliya qarorining tartibi boshqacha bo'lishi mumkin. Aniq talabni dastur sahifasi belgilaydi.</p>
<div class="box info">UKRI moliyasiga talaba to'g'ridan-to'g'ri UKRI ga ariza bermaydi: o'qimoqchi bo'lgan universitet yoki tashkilot orqali topshiradi. MSCA doktorlik tarmoqlari ([[Doctoral Networks]]) ham alohida e'lon qilingan o'rinlar orqali yollaydi.</div>
<div class="box warn">“PhD = stipendiya” yoki “qabul = moliya” deb tenglashtirmang.</div>
<div class="srcs">Manba: {UKRI}; {MSCA}; {LEEDS}. {HOL}.</div>""",
             take="Avval model aniqlanadi: ariza kimga, rahbar qachon, moliya qaysi bosqichda hal bo'ladi.",
             quiz=[("UKRI moliyasi uchun talaba ariza UKRI portaliga to'g'ridan-to'g'ri beradi.", "n", "Noto'g'ri: ariza universitet yoki tashkilot orqali beriladi (UKRI sahifasi)."),
                   ("MSCA doktorlik tarmoqlarida nomzod har qanday fuqarolikda bo'lishi mumkin, lekin mobillik qoidasi bor.", "t", "To'g'ri: Yevropa Komissiyasi sahifasidagi qoida."),
                   ("Universitet reytingi yuqori bo'lsa, rahbar va uskuna ham albatta mos.", "n", "Noto'g'ri: reyting individual loyiha sharoitini ko'rsatmaydi."),
                   ("Universitet va moliya muddatlari har doim bir kun.", "n", "Noto'g'ri: ular alohida bo'lishi va moliya muddati oldinroq kelishi mumkin.")],
             task="<ul><li>Har modeldan kamida bitta haqiqiy e'lon toping.</li><li>Ariza yo'lini sxemaga joylang.</li><li>Qaysi biri sizga mosligini yozing.</li></ul><p><b>O'zingizga savol:</b> daraja (o'qish) va ish shartnomasi o'rtasidagi farqni tekshirdingizmi?</p>",
             ph="Model 1: ... (havola) — ariza ...ga ; Model 2: ... ; Menga mos: ..., chunki ..."),
        dict(t="Imkoniyat qidirish tizimi", short="Qidiruv", min=30, kind="🔎 Qidiruv", ic="telescope",
             hook="Tasodifiy stipendiya kanallari o'rniga har sikl qayta ishlatiladigan qidiruv tizimini yarating.",
             body=f"""<h4>Qayerdan qidiriladi</h4>
<ul><li>Universitet doktorantura maktabi va kafedra sahifalari.</li><li>Laboratoriya rahbarining sahifasi.</li><li>UKRI moliyasidagi o'rinlar (universitetlar e'lon qiladi).</li><li>EURAXESS va MSCA o'rinlari.</li></ul>
<p>So'rovda soha, usul, ariza turi va moliya kalit so'zi bo'lsin. Har e'lon uchun: egasi, yopilish sanasi, rasmiy havola va holat.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> So'rov: [[funded PhD]] + usul nomi + soha. Kalit so'zda to'xtamang: e'lonni rasmiy sahifada oching va yopilmaganini tekshiring.</div>
<div class="box warn">Yig'uvchi saytlardagi e'lon eskirgan yoki yopilgan bo'lishi mumkin. Har doim universitet sahifasiga o'ting.</div>
<div class="srcs">Manba: {EURAXESS}; {UKRI}; {MSCA}. {HOL}.</div>""",
             take="4 ta rasmiy manba, aniq so'rovlar va har e'lon uchun tekshirilgan sana: bu takrorlanadigan qidiruv tizimi.",
             task="<ul><li>4 ta rasmiy portal tanlang.</li><li>12 ta e'lonni ro'yxatga oling.</li><li>Har e'lon ochiqligini tekshiring.</li></ul><p><b>O'zingizga savol:</b> oxirgi tekshiruv sanasini saqladingizmi?</p>",
             ph="Portal: ... ; E'lon 1: ..., yopilish ..., havola ..., tekshirildi ..."),
        dict(t="Universitet va ilmiy muhit", short="Muhit", min=30, kind="📊 Baholash", ic="chart",
             hook="Universitet reytingi rahbarlik muhitini va ish sharoitini to'liq ochmaydi. PhD sifatini ko'pincha rahbar, guruh va resurslar belgilaydi.",
             body=f"""<h4>Ilmiy moslik ([[research fit]]) mezonlari</h4>
<ul><li>Rahbar va guruhning so'nggi 3–5 yildagi maqolalari.</li><li>Laboratoriya uskunasi va ma'lumotga kirish.</li><li>Ikkinchi rahbar ([[co-supervisor]]) imkoniyati.</li><li>Seminarlar, ish madaniyati.</li><li>Bitiruvchilar qayerda ishlaydi.</li></ul>
<div class="box info">DORA tavsiyasi: jurnal ta'sir omilini ([[impact factor]]) olimning individual ilmiy sifatiga yagona o'lchov qilmang.</div>
<div class="box info"><b>Kompas tuzgan namuna.</b> A universitet reytingda yuqori, lekin kerakli uskuna va mos rahbar yo'q. B universitet mos usul va dala hududini beradi. B ilmiy jihatdan kuchliroq bo'lishi mumkin.</div>
<div class="box warn">“Top-100” yorlig'i aniq loyiha sharoitining isboti emas.</div>
<div class="srcs">Manba: {DORA}. {HOL}.</div>""",
             take="Har mezon uchun rasmiy dalil yozing: maqola, uskuna sahifasi, guruh ro'yxati. Reyting faqat bitta signal.",
             task="<ul><li>5 mezonli matritsa tuzing.</li><li>Har mezonga rasmiy dalil qo'shing.</li><li>Eng yaxshi 4 imkoniyatni ajrating.</li></ul><p><b>O'zingizga savol:</b> rahbar hozir qaysi muammo ustida ishlayotganiga aniq misol bera olasizmi?</p>",
             ph="Imkoniyat: ... — maqolalar: ..., uskuna: ..., ikkinchi rahbar: ..., bitiruvchilar: ..."),
        dict(t="Muvofiqlik va rasmiy talablar", short="Muvofiqlik", min=25, kind="✅ Matritsa", ic="shield",
             hook="Bitta “majburiy” band bajarilmasa, kuchli ilmiy moslik ham arizani saqlab qolmasligi mumkin.",
             body=f"""<h4>Alohida tekshiriladigan bandlar</h4>
<ul><li>Daraja va fan bo'yicha oldingi talablar.</li><li>Ingliz tili dalili.</li><li>Moliya bo'yicha fuqarolik cheklovlari.</li><li>Yashash va mobillik qoidasi.</li><li>Bitirish sanasi.</li><li>Viza cheklovlari.</li></ul>
<p>“Afzal” ([[preferred]]) va “majburiy” ([[essential]]) bandlarni aralashtirmang. Noma'lum band bo'lsa, qabul bo'limiga aniq savol yozing.</p>
<div class="box info">MSCA doktorlik tarmog'ida odatda nomzod yollash sanasidan oldingi 36 oyda 12 oydan ko'p o'sha mamlakatda yashamagan yoki ishlamagan bo'lishi kerak. Bu fuqarolikka emas, yashash davriga bog'liq.</div>
<div class="box warn">Boshqa mamlakat qoidasini yoki o'tgan yilgi yo'riqnomani joriy shart deb olmang.</div>
<div class="srcs">Manba: {MSCA}; {LEEDS}. {HOL}.</div>""",
             take="Har “majburiy” band uchun javob yoki rasmiy manba bo'lsin; noma'lum band savolga aylanadi.",
             task="<ul><li>4 ta ustuvor ariza uchun muvofiqlik matritsasini to'ldiring.</li><li>Har “?” bandga rasmiy manba yoki email qo'shing.</li><li>Mos kelmaydigan bandlarni ajrating.</li></ul><p><b>O'zingizga savol:</b> “majburiy” bandlarning barchasiga javobingiz bormi?</p>",
             ph="Ariza 1: daraja ✓, til ✓ (IELTS ...), fuqarolik ?, mobillik ✓ ... Savol emaili: ..."),
        dict(t="Muddatlar va teskari kalendar", short="Muddat", min=25, kind="📅 Reja", ic="calendar",
             hook="Kafedra arizasi, moliya va kollej muddatlari bir xil bo'lmasligi mumkin. Bittasini o'tkazib yuborsangiz, butun sikl yo'qoladi.",
             body=f"""<h4>Uch xil muddat</h4>
<ul><li><b>Tashqi muddat</b>: portal yopiladigan sana va vaqt.</li><li><b>Ichki muddat</b>: o'zingiz uchun oldinroq qo'ygan nazorat nuqtasi.</li><li><b>Bog'liqliklar</b>: boshqa odamga bog'liq ishlar.</li></ul>
<p>Tavsiya beruvchiga xabar, rasmiy tarjima, test natijasi kelishi, loyiha taklifini qayta yozish va rahbar javobini vaqtga bog'lang. Vaqt mintaqasi, bayramlar va portal yopilish soati ham xato manbai.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Moliya muddati universitet arizasidan oldin bo'lsa, “universitetga keyin topshiraman” rejasi ishlamaydi. Qaysi bosqich birinchi ekanini rasmiy yo'riqnoma belgilaydi.</div>
<div class="box warn">Muddatni kalendarga faqat mahalliy sana bilan yozib, vaqt mintaqasini unutish xavfli.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Har ariza uchun tashqi muddat, 2 ta ichki nazorat nuqtasi va 7 kunlik zaxira yoziladi.",
             task="<ul><li>4 ta ariza uchun tashqi muddatni vaqt mintaqasi bilan yozing.</li><li>2 ta ichki nazorat nuqtasini qo'shing.</li><li>7 kunlik zaxira belgilang.</li></ul><p><b>O'zingizga savol:</b> qaysi vazifa boshqa odamning javobiga bog'liq?</p>",
             ph="Ariza 1: tashqi ... (GMT), ichki 1: ..., ichki 2: ..., zaxira: ... ; Bog'liq: tavsiya ..."),
        dict(t="Tanlov va B reja", short="Tanlov", min=25, kind="⚖️ Qaror", ic="scroll",
             hook="Arizalar soni sifat va moliyaviy xavfsizlik o'rnini bosmaydi. To'rtta yaxshi ariza o'nta shoshilinch arizadan kuchliroq.",
             body=f"""<p>Bakalavriatdagi “orzu, mo'ljal, ishonchli” bo'linishi PhD uchun tor: ilmiy moslik, moliya qamrovi, muvofiqlik va rahbarning bo'sh o'rni ustuvor.</p>
<ul><li>4 ta asosiy ariza va 4–8 ta kuzatuvdagi imkoniyatni alohida yuriting.</li><li>Har imkoniyatga vaqt sarfi va kutilgan foyda bahosini bering, lekin taxminni qabul ehtimoli deb ko'rsatmang.</li></ul>
<div class="box info"><b>Kompas tuzgan namuna.</b> Bitta loyiha 4 ta mos laboratoriyaga ham kirmasa, “ko'proq ariza” emas, mavzu va moslikni qayta tekshirish kerak.</div>
<div class="box warn">“Qabul kafolatli”, “100% stipendiya” kabi tekshirilmagan da'volardan qoching.</div>""",
             take="4 ta ustuvor ariza, har biriga bitta murosa ([[trade-off]]) va keyingi sikl uchun B reja.",
             task="<ul><li>4 ta ustuvor variantni tanlang.</li><li>Har biriga bitta murosani yozing.</li><li>B reja va keyingi sikl strategiyasini belgilang.</li></ul><p><b>O'zingizga savol:</b> nega aynan shu to'rttasi va nega boshqa to'rttasi emas?</p>",
             ph="1) ... — murosa: ... 2) ... ; B reja: ... ; Keyingi sikl: ..."),
    ],
    tool=dict(id="matritsa", short="Matritsa", h2="Dasturlar matritsasi", sub="4 ta asosiy variantni rasmiy havola va muddat bilan solishtiring.",
              h3="Saralangan ro'yxat", tag="6 maydon", ic="chart", btn="Matritsani saqlash", badge="Saralovchi", min=5,
              fields=[dict(k="v1", label="1-variant", hint="dastur, model, havola", ph="... universiteti, funded project, https://..."),
                      dict(k="v2", label="2-variant", ph="..."),
                      dict(k="v3", label="3-variant", ph="..."),
                      dict(k="v4", label="4-variant", ph="..."),
                      dict(k="muddat", label="Muddatlar", hint="tashqi + ichki", type="area", ph="1) ... (GMT) / ichki ... ; 2) ..."),
                      dict(k="noma", label="Noma'lum bandlar va savollar", type="area", ph="1-variant: fuqarolik cheklovi? — qabul bo'limiga email ...")]),
    check=dict(h2="M2 nazorati", sub="Ro'yxatni yakunlashdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Har nomzod uchun alohida rasmiy havola bor.", "E'lon qilingan loyiha va ochiq ariza ajratilgan.", "Rahbar, guruh va uskuna dalillari yozilgan.",
                      "Muvofiqlik noaniqliklari ochiq yozilgan.", "Universitet va moliya muddatlari alohida, vaqt mintaqasi bilan.",
                      "Har e'lonning ochiqligi tekshirilgan sanasi bor.", "B reja yozilgan."]),
    art_title="Saralangan ro'yxat va teskari kalendar", art_short="Ro'yxat",
    art=[("PhD modellari", ["a1"]), ("Qidiruv", ["a2"]), ("Ilmiy muhit", ["a3"]), ("Asosiy variantlar", ["v1", "v2", "v3", "v4"]),
         ("Muvofiqlik", ["a4", "noma"]), ("Muddatlar", ["muddat", "a5"]), ("Tanlov va B reja", ["a6"])],
    tip="Har e'lon yonida “tekshirildi: sana” yozing. Ikki hafta o'tgach, ro'yxatning bir qismi yopilgan bo'ladi.",
    sources=f"{LEEDS}; {UKRI}; {MSCA}; {EURAXESS}; {DORA}. {STD}",
)
