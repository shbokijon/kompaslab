from common import LEEDS, UKRI, MSCA, EURAXESS, DORA, HOL, STD

MOD = dict(
    title="Doktorantura tizimlari va universitet tanlash",
    desc="PhD Lab M2: doktorantura modellari, imkoniyat qidirish, universitet va laboratoriyani baholash, talablar va muddatlar. Natija: 8–12 imkoniyatli saralangan ro'yxat va 4 ta asosiy ariza.",
    lead="“PhD” degan bir xil nom ortida turlicha tizimlar bor. Bu modulda imkoniyatlarni <b>ilmiy moslik, moliya va rasmiy talablar</b> bo'yicha saralaysiz: 8–12 tasini topasiz va ulardan 4 tasini asosiy ariza qilib ajratasiz. Reyting bu yerda faqat qo'shimcha ma'lumot.",
    hero="phd", weeks="2", next="M3 Ilmiy rahbar va laboratoriya bilan aloqa", next_href="phd-lab-o.html?m=3",
    goals=[("chart", "Saralangan ro'yxat (Shortlist)", "8–12 imkoniyat, har birida rasmiy havola va tekshirilgan sana"),
           ("shield", "Talablar jadvali", "majburiy va afzal talablar alohida"),
           ("calendar", "Teskari kalendar", "tashqi va ichki muddatlar, 7 kun zaxira")],
    warn="Universitet tanlashning umumiy usullari Master Lab M1 da. Bu yerda faqat doktoranturaga xos tizimlar. Har bir shartni o'sha dastur sahifasidan tekshiring: mamlakat haqidagi umumiy maqola bunga yetmaydi.",
    lessons=[
        dict(t="To'rtta PhD modeli", short="Modellar", min=30, kind="🧭 Xarita", ic="compass",
             hook="Bitta mamlakat ichida ham PhD turlicha tashkil qilinadi. Modelni bilmasangiz, arizani <b>noto'g'ri joyga</b> yoki <b>noto'g'ri tartibda</b> yuborib qo'yishingiz mumkin.",
             body=f"""<div class="tbl"><table><thead><tr><th>Model</th><th>Ariza kimga beriladi</th><th>Moliya qachon hal bo'ladi</th></tr></thead><tbody>
<tr><td>O'zingiz taklif qilgan loyiha ([[self-proposed]])</td><td>Universitetga, ilmiy loyiha taklifi bilan</td><td>Ko'pincha alohida tanlovda</td></tr>
<tr><td>Moliyalashtirilgan, e'lon qilingan loyiha ([[funded project]])</td><td>E'londagi loyihaga: rahbarga yoki universitetga</td><td>E'lon bilan birga</td></tr>
<tr><td>Doktorlik dasturi ([[doctoral training programme]])</td><td>Dastur yoki markazga</td><td>Dastur o'rinlari bilan birga</td></tr>
<tr><td>Maoshli doktorlik lavozimi</td><td>Ish beruvchiga: universitet yoki institut</td><td>Ish shartnomasi bilan</td></tr>
</tbody></table></div>
<p>Har modelda arizani kim qabul qilishi, rahbarning roli, loyiha chegarasi va moliya qarori qachon chiqishi farq qiladi. Aniq talabni <b>dastur sahifasi</b> belgilaydi.</p>
<div class="box info">UKRI mablag'iga talaba UKRI ga ariza bermaydi: o'qimoqchi bo'lgan universitet yoki tashkilot orqali topshiradi. MSCA doktorlik tarmoqlari ([[Doctoral Networks]]) ham alohida e'lon qilingan o'rinlarga odam oladi.</div>
<div class="box warn"><i>“PhD bo'lsa, stipendiya ham bor”</i> yoki <i>“qabul qilishdi, demak pul ham bor”</i> deb o'ylamang.</div>
<div class="srcs">Manba: {UKRI}; {MSCA}; {LEEDS}. {HOL}.</div>""",
             take="Avval modelni aniqlang: ariza kimga, rahbar qachon tanlanadi, moliya qaysi bosqichda hal bo'ladi.",
             quiz=[("UKRI mablag'i uchun talaba ariza UKRI saytiga beradi.", "n", "Noto'g'ri: ariza universitet yoki tashkilot orqali beriladi (UKRI sahifasi)."),
                   ("MSCA doktorlik tarmog'iga istalgan mamlakat fuqarosi topshira oladi, lekin mobillik qoidasi bor.", "t", "To'g'ri: Yevropa Komissiyasi sahifasidagi qoida."),
                   ("Universitet reytingi yuqori bo'lsa, rahbar va uskuna ham albatta mos keladi.", "n", "Noto'g'ri: reyting aniq loyiha sharoitini ko'rsatmaydi."),
                   ("Universitet va moliya muddatlari doim bir kunga to'g'ri keladi.", "n", "Noto'g'ri: ular har xil bo'lishi, moliya muddati esa oldinroq kelishi mumkin.")],
             task="<ul><li>Har modeldan kamida bitta haqiqiy e'lon toping.</li><li>Har biri uchun ariza yo'lini chizib chiqing.</li><li>Qaysi biri sizga to'g'ri kelishini yozing.</li></ul><p><b>O'zingizga savol:</b> e'londa o'qish (daraja) taklif qilinyaptimi yoki ish shartnomasi?</p>",
             ph="Model 1: ... (havola), ariza ...ga ; Model 2: ... ; Menga mos: ..., chunki ..."),
        dict(t="Imkoniyat qidirish", short="Qidiruv", min=30, kind="🔎 Qidiruv", ic="telescope",
             hook="Stipendiya kanallaridagi tasodifiy e'lonlar o'rniga <b>har yili qayta ishlatsa bo'ladigan</b> qidiruv tartibini tuzing.",
             body=f"""<h4>Qayerdan qidiriladi</h4>
<ul><li>Universitet doktorantura maktabi va kafedra sahifalari.</li><li>Laboratoriya rahbarining shaxsiy sahifasi.</li><li>UKRI mablag'idagi o'rinlar: ularni universitetlar e'lon qiladi.</li><li>EURAXESS va MSCA o'rinlari.</li></ul>
<p>So'rovga soha, usul, ariza turi va moliyaga oid so'zni qo'shing. Har e'lon uchun yozing: kim e'lon qilgan, qachon yopiladi, rasmiy havola va hozirgi holati.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> So'rov: <i>[[funded PhD]] + usul nomi + soha</i>. Chiqqan e'lonni rasmiy sahifada ochib, hali yopilmaganini tekshiring.</div>
<div class="box warn">Yig'uvchi saytlardagi e'lon eskirgan yoki yopilgan bo'lishi mumkin. Doim universitet sahifasiga o'tib tekshiring.</div>
<div class="srcs">Manba: {EURAXESS}; {UKRI}; {MSCA}. {HOL}.</div>""",
             take="4 ta rasmiy manba, aniq so'rovlar va har e'lon yonida tekshirilgan sana: shu tartib har yili qayta ishlaydi.",
             task="<ul><li>4 ta rasmiy sayt tanlang.</li><li>12 ta e'lonni ro'yxatga yozing.</li><li>Har biri hali ochiqligini tekshiring.</li></ul><p><b>O'zingizga savol:</b> oxirgi tekshiruv sanasini yozib qo'ydingizmi?</p>",
             ph="Sayt: ... ; E'lon 1: ..., yopiladi ..., havola ..., tekshirildi ..."),
        dict(t="Universitet va laboratoriya muhiti", short="Muhit", min=30, kind="📊 Baholash", ic="chart",
             hook="Universitet reytingi rahbarning qanday ishlashini va laboratoriyadagi sharoitni ko'rsatmaydi. PhD sifatini ko'pincha <b>rahbar, guruh va resurslar</b> hal qiladi.",
             body=f"""<h4>Ilmiy moslikni ([[research fit]]) nimadan bilasiz</h4>
<ul><li>Rahbar va guruhning so'nggi 3–5 yildagi maqolalari.</li><li>Laboratoriya uskunasi va ma'lumotga kirish.</li><li>Ikkinchi rahbar ([[co-supervisor]]) bo'lishi mumkinmi.</li><li>Seminarlar va ishlash madaniyati.</li><li>Bitiruvchilar hozir qayerda ishlaydi.</li></ul>
<div class="box info">DORA tavsiyasi: jurnalning ta'sir omili ([[impact factor]]) olimning shaxsiy ilmiy darajasini o'lchash uchun yetarli emas.</div>
<div class="box info"><b>Kompas tuzgan namuna.</b> A universitet reytingda yuqori, lekin kerakli uskuna va mos rahbar yo'q. B universitetda mos usul ham, dala hududi ham bor. Ilmiy jihatdan B kuchliroq tanlov bo'lishi mumkin.</div>
<div class="box warn"><i>“Top-100”</i> yorlig'i aniq loyihangiz uchun sharoit borligini isbotlamaydi.</div>
<div class="srcs">Manba: {DORA}. {HOL}.</div>""",
             take="Har mezon uchun rasmiy dalil yozing: maqola, uskuna sahifasi, guruh ro'yxati. Reytingni qo'shimcha ma'lumot sifatida ko'ring.",
             task="<ul><li>5 mezonli jadval tuzing.</li><li>Har mezon uchun rasmiy dalil qo'shing.</li><li>Eng yaxshi 4 imkoniyatni ajrating.</li></ul><p><b>O'zingizga savol:</b> rahbar hozir qaysi muammo ustida ishlayotganini aniq misol bilan ayta olasizmi?</p>",
             ph="Imkoniyat: ...: maqolalar ..., uskuna ..., ikkinchi rahbar ..., bitiruvchilar ..."),
        dict(t="Talablar va rasmiy shartlar", short="Talablar", min=25, kind="✅ Jadval", ic="shield",
             hook="Bitta <b>majburiy</b> shart bajarilmasa, ilmiy jihatdan kuchli ariza ham ko'rib chiqilmasligi mumkin.",
             body=f"""<h4>Alohida tekshiriladigan talablar</h4>
<ul><li>Daraja va oldin o'qilishi kerak bo'lgan fanlar.</li><li>Ingliz tili sertifikati.</li><li>Moliya bo'yicha fuqarolik cheklovlari.</li><li>Yashash joyi va mobillik qoidasi.</li><li>Diplom olinadigan sana.</li><li>Viza cheklovlari.</li></ul>
<p><b>Afzal</b> ([[preferred]]) va <b>majburiy</b> ([[essential]]) talablarni aralashtirmang. Biror talab tushunarsiz bo'lsa, qabul bo'limiga aniq savol yozing.</p>
<div class="box info">MSCA doktorlik tarmog'ida odatda shunday qoida bor: nomzod ishga olinishidan oldingi 36 oyning 12 oyidan ko'prog'ini o'sha mamlakatda yashab yoki ishlab o'tkazmagan bo'lishi kerak. Bu qoida qayerda yashaganingizga bog'liq, fuqarolikka bog'liq emas.</div>
<div class="box warn">Boshqa mamlakat qoidasini yoki o'tgan yilgi yo'riqnomani bu yilgi shart deb olmang.</div>
<div class="srcs">Manba: {MSCA}; {LEEDS}. {HOL}.</div>""",
             take="Har majburiy talab uchun javobingiz yoki rasmiy manba bo'lsin. Tushunarsiz talab qabul bo'limiga savol bo'lib ketadi.",
             task="<ul><li>4 ta asosiy ariza uchun talablar jadvalini to'ldiring.</li><li>Har <i>“?”</i> belgisi yoniga rasmiy manba yoki yuborilgan xatni qo'shing.</li><li>Mos kelmaydigan talablarni ajratib qo'ying.</li></ul><p><b>O'zingizga savol:</b> barcha majburiy talablarga javobingiz bormi?</p>",
             ph="Ariza 1: daraja ✓, til ✓ (IELTS ...), fuqarolik ?, mobillik ✓ ... Qabul bo'limiga xat: ..."),
        dict(t="Muddatlar va teskari kalendar", short="Muddat", min=25, kind="📅 Reja", ic="calendar",
             hook="Kafedra, moliya va kollej muddatlari bir kunga to'g'ri kelmasligi mumkin. Bittasini o'tkazib yuborsangiz, <b>butun yilni</b> yo'qotasiz.",
             body=f"""<h4>Uch xil muddat</h4>
<ul><li><b>Tashqi muddat</b>: portal yopiladigan sana va soat.</li><li><b>Ichki muddat</b>: o'zingiz uchun oldinroq belgilagan nazorat sanasi.</li><li><b>Boshqalarga bog'liq ishlar</b>: tavsiya, tarjima, rahbar javobi.</li></ul>
<p>Tavsiya beruvchiga xabar berish, rasmiy tarjima, test natijasi yetib kelishi, loyiha taklifini qayta yozish va rahbar javobini kalendarga qo'ying. Vaqt mintaqasi, bayram kunlari va portal yopiladigan soat ham ko'p xatoga sabab bo'ladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Moliya muddati universitet arizasidan oldin bo'lsa, <i>“universitetga keyinroq topshiraman”</i> rejasi ishlamaydi. Qaysi bosqich birinchi ekanini rasmiy yo'riqnoma belgilaydi.</div>
<div class="box warn">Muddatni kalendarga vaqt mintaqasiz yozib qo'yish xavfli.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Har ariza uchun tashqi muddat, 2 ta ichki nazorat sanasi va 7 kunlik zaxira yoziladi.",
             task="<ul><li>4 ta ariza muddatini vaqt mintaqasi bilan yozing.</li><li>2 ta ichki nazorat sanasini qo'shing.</li><li>7 kunlik zaxira qoldiring.</li></ul><p><b>O'zingizga savol:</b> qaysi ish boshqa odamning javobiga bog'liq?</p>",
             ph="Ariza 1: tashqi ... (GMT), ichki 1: ..., ichki 2: ..., zaxira: ... ; Bog'liq: tavsiya ..."),
        dict(t="Tanlov va zaxira reja", short="Tanlov", min=25, kind="⚖️ Qaror", ic="scroll",
             hook="Ko'p ariza yuborish sifat va moliyaviy xavfsizlik o'rnini bosmaydi. <b>To'rtta puxta ariza</b> o'nta shoshilib yozilganidan foydaliroq.",
             body=f"""<p>Bakalavriatdagi <i>“orzu, mo'ljal, ishonchli”</i> bo'linishi PhD uchun tor. Bu yerda ilmiy moslik, moliya, talablarga javob berish va rahbarda bo'sh o'rin borligi muhimroq.</p>
<ul><li>4 ta asosiy ariza va 4–8 ta kuzatuvdagi imkoniyatni alohida yuriting.</li><li>Har imkoniyat uchun qancha vaqt ketishi va nima berishini baholang, lekin bu bahoni qabul ehtimoli deb yozmang.</li></ul>
<div class="box info"><b>Kompas tuzgan namuna.</b> Bitta loyiha bilan 4 ta mos laboratoriyaga ham qabul bo'lmasa, ko'proq ariza yuborishdan oldin mavzu va moslikni qayta ko'rib chiqing.</div>
<div class="box warn"><i>“Qabul kafolatlangan”</i>, <i>“100% stipendiya”</i> kabi tekshirilmagan va'dalardan uzoq turing.</div>""",
             take="4 ta asosiy ariza, har biri uchun bitta murosa ([[trade-off]]) va keyingi yil uchun zaxira reja.",
             task="<ul><li>4 ta asosiy variantni tanlang.</li><li>Har birida nimadan voz kechayotganingizni yozing.</li><li>Zaxira reja va keyingi yilgi rejani belgilang.</li></ul><p><b>O'zingizga savol:</b> nega aynan shu to'rttasi?</p>",
             ph="1) ...: murosa ... 2) ... ; Zaxira reja: ... ; Keyingi yil: ..."),
    ],
    tool=dict(id="jadval", short="Jadval", h2="Dasturlar jadvali", sub="4 ta asosiy variantni rasmiy havola va muddat bilan solishtiring.",
              h3="Saralangan ro'yxat", tag="6 maydon", ic="chart", btn="Jadvalni saqlash", badge="Saralovchi", min=5,
              fields=[dict(k="v1", label="1-variant", hint="dastur, model, havola", ph="... universiteti, funded project, https://..."),
                      dict(k="v2", label="2-variant", ph="..."),
                      dict(k="v3", label="3-variant", ph="..."),
                      dict(k="v4", label="4-variant", ph="..."),
                      dict(k="muddat", label="Muddatlar", hint="tashqi va ichki", type="area", ph="1) ... (GMT), ichki ... ; 2) ..."),
                      dict(k="noma", label="Tushunarsiz talablar va savollar", type="area", ph="1-variant: fuqarolik cheklovi bormi? Qabul bo'limiga xat ...")]),
    check=dict(h2="M2 nazorati", sub="Ro'yxatni yakunlashdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Har nomzod uchun alohida rasmiy havola bor.", "E'lon qilingan loyiha va erkin ariza ajratilgan.", "Rahbar, guruh va uskuna haqida dalil yozilgan.",
                      "Tushunarsiz talablar ochiq yozilgan.", "Universitet va moliya muddatlari alohida, vaqt mintaqasi bilan yozilgan.",
                      "Har e'lon ochiqligi tekshirilgan sana bor.", "Zaxira reja yozilgan."]),
    art_title="Saralangan ro'yxat va teskari kalendar", art_short="Ro'yxat",
    art=[("PhD modellari", ["a1"]), ("Qidiruv", ["a2"]), ("Universitet va laboratoriya", ["a3"]), ("Asosiy variantlar", ["v1", "v2", "v3", "v4"]),
         ("Talablar", ["a4", "noma"]), ("Muddatlar", ["muddat", "a5"]), ("Tanlov va zaxira reja", ["a6"])],
    tip="Har e'lon yoniga <i>“tekshirildi: sana”</i> deb yozing. Ikki haftadan keyin ro'yxatdagi ba'zi e'lonlar yopilgan bo'ladi.",
    sources=f"{LEEDS}; {UKRI}; {MSCA}; {EURAXESS}; {DORA}. {STD}",
)
