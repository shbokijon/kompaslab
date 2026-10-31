from common import LEEDS, UKRI_STUD, MSCA, EURAXESS, DORA, HOL, STD

MOD = dict(
    title="Doktorantura tizimlari va universitet tanlash",
    desc="PhD Lab M2: doktoranturaning to'rt modeli, o'rinlarni qidirish tizimi, universitet va ilmiy muhitni baholash, muvofiqlik talablari, muddatlar va teskari kalendar, ustuvor arizalarni tanlash. Natija: 8–12 imkoniyatli saralangan ro'yxat va 4 ta ustuvor ariza.",
    lead="Universitetni nomi va reytingi bo'yicha emas, ilmiy moslik, moliya va rasmiy muvofiqlik bo'yicha tanlaysiz. Modul oxirida 8–12 imkoniyatli saralangan ro'yxat va 4 ta ustuvor ariza bo'ladi.",
    hero="compass", weeks="2", next="M3. Ilmiy rahbar va laboratoriya bilan aloqa", next_href="phd-lab-m3.html",
    goals=[("compass", "Saralangan ro'yxat", "8–12 imkoniyat, har birida rasmiy havola"),
           ("shield", "Muvofiqlik jadvali", "4 ustuvor ariza, \"majburiy\" va \"afzal\" ajratilgan"),
           ("calendar", "Teskari kalendar", "tashqi muddat, ichki nazorat nuqtalari, zaxira vaqt")],
    warn=f"Mamlakatlar bo'yicha umumiy qoidalar misol sifatida beriladi; har bir dasturning amaldagi talabini o'sha dastur sahifasidan oling. Germaniya, Koreya va AQShga xos mexanizm DAAD, GKS va USA Lab'larda. Faktlar {HOL}.",
    lessons=[
        dict(t="Doktoranturaning to'rt modeli", short="Modellar", min=30, kind="🧭 Xarita", ic="compass",
             hook="Bitta mamlakat ichida ham PhD turlicha tashkil qilinadi. Qaysi modelga topshirayotganingizni bilmasangiz, hujjatni noto'g'ri odamga yoki noto'g'ri vaqtda yuborasiz.",
             body=f"""<div class="tbl"><table><thead><tr><th>Model</th><th>Qanday boshlanadi</th><th>Kim qaror qiladi</th></tr></thead><tbody>
<tr><td>O'z loyihangiz bilan ([[self-proposed]])</td><td>Siz loyiha taklifini yozasiz va rahbar topasiz</td><td>Universitet, rahbar roziligi bilan</td></tr>
<tr><td>E'lon qilingan moliyalashtirilgan loyiha</td><td>Tayyor loyiha uchun nomzod izlanadi</td><td>Loyiha rahbari va komissiya</td></tr>
<tr><td>Doktorlik maktabi yoki dasturi ([[cohort]])</td><td>Kafedra yoki dastur belgilangan muddatda qabul qiladi</td><td>Kafedra komissiyasi</td></tr>
<tr><td>Maoshli doktorlik lavozimi</td><td>Ish e'loniga ariza</td><td>Ish beruvchi (universitet yoki institut)</td></tr>
</tbody></table></div>
<p>Har modelda arizani kimga berishingiz, rahbarning roli va moliyalashtirish qarori qachon chiqishi boshqacha. Aniq talabni dastur sahifasi belgilaydi; mamlakat haqidagi umumiy maqola yetarli emas.</p>
<div class="box info">UKRI moliyalashtirgan o'ringa talaba UKRI'ga emas, universitetga ariza beradi. MSCA doktorlik tarmoqlari ham alohida e'lon qilingan o'rinlar orqali nomzod oladi.</div>
<div class="box warn">\"PhD = stipendiya\" yoki \"qabul = moliyalashtirish\" deb hisoblamang: ikkalasi alohida qaror bo'lishi mumkin.</div>
<div class="srcs">Manba: {UKRI_STUD}; {MSCA}; {LEEDS}. {HOL}.</div>""",
             take="To'rt model: o'z loyihangiz, e'lon qilingan loyiha, doktorlik dasturi, maoshli lavozim. Ariza kimga va qachon berilishi modelga bog'liq.",
             task="<ul><li>Har modeldan kamida bitta haqiqiy e'lon yoki dastur toping.</li><li>Har biri uchun ariza yo'lini 3 qadamda yozing.</li><li>Qaysi model sizga mos va nega?</li></ul>",
             ph="O'z loyihasi: ... (havola) → 1) ... 2) ... 3) ...; Menga mos: ..., chunki ..."),
        dict(t="O'rinlarni qidirish tizimi", short="Qidiruv", min=30, kind="🔎 Tizim", ic="telescope",
             hook="Tasodifiy Telegram kanallari o'rniga qayta ishlatiladigan qidiruv tizimini quring. E'lonlar yil davomida chiqadi: tizim bo'lsa, birortasini ham o'tkazib yubormaysiz.",
             body=f"""<h4>Rasmiy qidiruv joylari</h4>
<ul><li>Universitet doktorantura bo'limi va kafedra sahifalari</li><li>Laboratoriya (rahbar) sahifalari</li><li>UKRI moliyalashtirgan o'rinlar: e'lonni universitet beradi</li><li>{EURAXESS} va MSCA doktorlik tarmoqlari o'rinlari</li></ul>
<p>Qidiruv so'rovida soha, metod, ariza turi va moliyalashtirish so'zi bo'lsin. Har topilgan e'lon uchun egasi, yopilish sanasi, rasmiy havola, tekshirgan sanangiz va holatini yozing.</p>
<div class="box info"><b>Kompas tuzgan namuna so'rovi:</b> <span lang="en">\"distributed acoustic sensing funded PhD\"</span>, <span lang="en">\"doctoral candidate geophysics\"</span>. Kalit so'z bilan to'xtamang: e'lonni rasmiy sahifada oching.</div>
<div class="box warn">Yig'uvchi saytlardagi e'lon eskirgan yoki yopilgan bo'lishi mumkin. Ularni faqat qidiruv uchun ishlating; talab va muddatni universitet sahifasidan oling.</div>
<div class="srcs">Manba: {UKRI_STUD}; {EURAXESS}; {MSCA}. {HOL}.</div>""",
             take="Rasmiy manbalar: universitet, kafedra, laboratoriya, UKRI orqali universitet e'lonlari, EURAXESS. Har e'lon uchun egasi, muddat, havola, tekshiruv sanasi.",
             task="<ul><li>4 ta rasmiy qidiruv joyini tanlang.</li><li>12 ta e'lonni jadvalga kiriting.</li><li>Har birining hozir ochiq yoki yopiqligini tekshiring.</li></ul>",
             ph="1) ... — egasi: ... — muddat: ... — havola — tekshirildi: ... — ochiq"),
        dict(t="Universitet va ilmiy muhitni baholash", short="Muhit", min=30, kind="🏛️ Baholash", ic="phd",
             hook="Universitet reytingi rahbarlik sifatini va ish sharoitini to'liq ko'rsatmaydi. PhD davomida kundalik ishingizga rahbar, guruh va resurslar ta'sir qiladi.",
             body=f"""<h4>Besh mezon</h4>
<ol><li><b>Ilmiy moslik:</b> rahbar va guruhning so'nggi 3–5 yildagi ishlari.</li><li><b>Laboratoriya va uskunalar.</b></li><li><b>Ma'lumotga kirish.</b></li><li><b>Ikkinchi rahbar va hamkorlar.</b></li><li><b>Ilmiy muhit:</b> seminarlar, doktorantlar soni, bitiruvchilar qayerda ishlayapti.</li></ol>
<p>Har mezon uchun rasmiy dalil yozing: maqola, laboratoriya sahifasi, kafedra hisoboti.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> A universitet reytingda yuqori, lekin kerakli uskuna va mos rahbar yo'q. B universitetda mos metod va dala ma'lumoti bor. Ilmiy jihatdan B kuchliroq bo'lishi mumkin.</div>
<div class="box warn">Jurnal ko'rsatkichlarini (masalan, impakt-faktor) bitta tadqiqotchining ish sifatini baholashda yagona o'lchov qilmang (DORA deklaratsiyasi).</div>
<div class="srcs">Manba: {DORA}.</div>""",
             take="Reyting emas, besh mezon: ilmiy moslik, uskuna, ma'lumot, hamkorlar, ilmiy muhit. Har mezonga dalil.",
             task="<ul><li>5 mezonli jadval tuzing.</li><li>Har mezonga rasmiy dalil qo'shing.</li><li>Eng mos 4 imkoniyatni ajrating.</li></ul>",
             ph="Imkoniyat A: moslik — ... (maqola); uskuna — ...; ma'lumot — ...; hamkor — ...; muhit — ..."),
        dict(t="Muvofiqlik va rasmiy talablar", short="Talablar", min=30, kind="✅ Tekshiruv", ic="shield",
             hook="Bitta majburiy talab bajarilmasa, kuchli ilmiy moslik ham arizani saqlab qolmasligi mumkin. Muvofiqlikni ([[eligibility]]) tayyorgarlikdan alohida, band-band tekshiring.",
             body=f"""<h4>Alohida tekshiriladigan bandlar</h4>
<ul><li>Oldingi daraja va fan talabi</li><li>Ingliz tili dalili</li><li>Moliyalashtirishning fuqarolik yoki yashash joyi cheklovlari</li><li>Mobillik qoidasi (MSCA kabi)</li><li>Bitirish sanasi</li><li>Viza va ATAS (Buyuk Britaniya, M8)</li></ul>
<p>\"Majburiy\" ([[essential]]) va \"afzal\" ([[preferred]]) talablarni aralashtirmang. Ma'lumot bo'lmasa, \"mos\" ham, \"mos emas\" ham demang: \"tekshirish kerak\" deb yozing va qabul bo'limiga aniq savol yuboring.</p>
<div class="box info">MSCA doktorlik tarmoqlarida nomzod istalgan fuqarolikdan bo'lishi mumkin, lekin odatda ishga olish sanasidan oldingi 36 oyda ishga oluvchi tashkilot mamlakatida 12 oydan ortiq yashamagan yoki asosiy faoliyat yuritmagan bo'lishi kerak va doktorlik darajasiga ega bo'lmasligi kerak. Aniq qoidani e'lon va joriy yo'riqnomadan tekshiring.</div>
<div class="box warn">Boshqa mamlakat yoki o'tgan yil yo'riqnomasini joriy talab deb olmang.</div>
<div class="srcs">Manba: {MSCA}; {LEEDS}. {HOL}.</div>""",
             take="Muvofiqlikni band-band tekshiring: daraja, til, fuqarolik, mobillik, sana, viza. \"Majburiy\" va \"afzal\"ni ajrating; noma'lumni \"tekshirish kerak\" deb yozing.",
             quiz=[("MSCA doktorlik tarmog'iga faqat Yevropa Ittifoqi fuqarolari topshira oladi.", "n", "Noto'g'ri: istalgan fuqarolik, lekin mobillik qoidasi bor."),
                   ("Talablar bir-biriga zid ko'rinsa, universitetdan yozma aniqlik so'raladi.", "t", "To'g'ri."),
                   ("Universitet tanlashda asosiy mezon umumiy reyting.", "n", "Noto'g'ri: ilmiy moslik, rahbarlik, moliya va talablar."),
                   ("Ma'lumot yetmasa, muvofiqlik ustuniga \"tekshirish kerak\" yoziladi.", "t", "To'g'ri: taxmin qilinmaydi.")],
             task="<ul><li>4 ustuvor ariza uchun muvofiqlik jadvalini to'ldiring.</li><li>Har \"?\" bandga rasmiy havola yoki yuborilgan savol qo'shing.</li><li>Mos kelmaydigan bandlarni alohida belgilang.</li></ul>",
             ph="A: daraja — mos (havola); til — tekshirish kerak (savol yuborildi ...); mobillik — mos ..."),
        dict(t="Muddatlar va teskari kalendar", short="Muddatlar", min=25, kind="📅 Reja", ic="calendar",
             hook="Kafedra arizasi, moliyalashtirish va kollej muddatlari bir xil bo'lmasligi mumkin. Bitta sanani o'tkazib yuborsangiz, butun sikl kechikadi.",
             body="""<ul><li><b>Tashqi muddat:</b> rasmiy sahifadagi sana, soat va vaqt mintaqasi bilan.</li><li><b>Ichki nazorat nuqtalari:</b> tavsiya beruvchiga xabar, tarjima, test natijasi kelishi, loyiha taklifining yakuniy versiyasi.</li><li><b>Bog'liqliklar:</b> boshqa odam javobiga bog'liq vazifalar (tavsiya, rahbar roziligi).</li></ul>
<div class="box info">Moliyalashtirish muddati universitet arizasidan oldin bo'lsa, \"universitetga keyinroq topshiraman\" rejasi ishlamaydi: qaysi bosqich birinchi ekanini rasmiy yo'riqnoma belgilaydi.</div>
<div class="box warn">Muddatni kalendarga faqat mahalliy sana bilan yozmang: Toshkent va Buyuk Britaniya orasida 4–5 soat farq bor (yozgi va qishki vaqtga qarab). Portal yopilish soatini va vaqt mintaqasini ham yozing.</div>""",
             take="Tashqi muddat (sana, soat, mintaqa) dan orqaga ichki nazorat nuqtalari va kamida 7 kunlik zaxira vaqt.",
             task="<ul><li>4 ariza uchun tashqi muddatni yozing.</li><li>Har biriga 2 ta ichki nazorat nuqtasi qo'shing.</li><li>7 kunlik zaxira vaqtni belgilang.</li></ul>",
             ph="A: muddat ... (soat ..., Europe/London) → tavsiya so'rovi ...; yakuniy taklif ...; zaxira ..."),
        dict(t="Ustuvor arizalar va B reja", short="Tanlov", min=25, kind="🎯 Qaror", ic="chart",
             hook="Arizalar soni sifat va moliyaviy xavfsizlik o'rnini bosmaydi. To'rtta yaxshi tayyorlangan ariza o'nta shoshilinch arizadan kuchliroq.",
             body="""<p>Bakalavriatdagi \"orzu / mos / xavfsiz\" bo'linmasi PhD uchun tor: bu yerda ilmiy moslik, moliya qamrovi, muvofiqlik va rahbarning bo'sh o'rni hal qiladi.</p>
<ul><li>4 ta asosiy ariza va 4–8 ta kuzatuvdagi imkoniyatni alohida yuriting.</li><li>Har imkoniyatga vaqt sarfi va kutilgan foydani baholang, lekin bu bahoni qabul ehtimoli deb ko'rsatmang.</li><li>B reja: keyingi sikl, magistratura yoki ilmiy assistentlik.</li></ul>
<div class="box info">Bitta tayyor loyiha 4 ta mos laboratoriyaga ham to'g'ri kelmasa, arizalar sonini oshirish emas, mavzu va moslikni qayta ko'rish kerak (M1).</div>
<div class="box warn">\"Qabul kafolatlangan\", \"100% stipendiya\" kabi tekshirilmagan va'dalardan ehtiyot bo'ling.</div>""",
             take="4 asosiy ariza + 4–8 kuzatuvdagi imkoniyat. Har birida bitta murosa ([[trade-off]]) yozilgan. B reja oldindan.",
             task="<ul><li>4 ta ustuvor variantni tanlang.</li><li>Har biriga bitta murosani yozing.</li><li>B reja va keyingi sikl strategiyasini yozing.</li></ul>",
             ph="1) ... — murosa: ...; 2) ...; B reja: ..."),
    ],
    tool=dict(id="matritsa", short="Matritsa", h2="Universitet va dastur matritsasi", sub="Har bir imkoniyatni reyting emas, rasmiy talab va ilmiy moslik bilan saralang.",
              h3="Imkoniyat kartasi", tag="7 maydon", ic="compass", btn="Kartani saqlash", badge="Tanlovchi", min=5,
              fields=[dict(k="uni", label="Universitet yoki institut", ph="..."),
                      dict(k="yol", label="Doktorantura modeli", type="select", opts=["O'z loyihasi bilan", "E'lon qilingan loyiha", "Doktorlik dasturi", "Maoshli lavozim", "MSCA doktorlik tarmog'i", "Boshqa"]),
                      dict(k="moslik", label="Loyiha, rahbar va ilmiy moslik", type="area", ph="Nega aynan shu guruh?"),
                      dict(k="talab", label="Muvofiqlik: manba, band va holat", type="area", ph="Mos / tekshirish kerak / mos emas"),
                      dict(k="moliya", label="Moliyalashtirish qamrovi", type="area", ph="O'qish to'lovi, stipendiya, muddat, shartlar"),
                      dict(k="havola", label="Rasmiy manba (aniq sahifa)", type="url", ph="https://..."),
                      dict(k="sana", label="Shaxsan tekshirilgan sana", type="date")]),
    check=dict(h2="M2 nazorati", sub="Saralangan ro'yxatni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har imkoniyat uchun alohida rasmiy havola bor.", "E'lon qilingan loyiha va o'z loyihasi yo'li ajratilgan.",
                      "Rahbar, guruh va uskuna bo'yicha dalillar yozilgan.", "Muvofiqlikdagi noaniqliklar ochiq yozilgan.",
                      "Universitet va moliyalashtirish muddatlari alohida.", "Muddat soati va vaqt mintaqasi yozilgan.",
                      "B reja bor.", "Har o'zgaruvchan talab yonida sikl va tekshiruv sanasi bor."]),
    art_title="Saralangan ro'yxat va 4 ta ustuvor ariza", art_short="Ro'yxat",
    art=[("Modellar", ["a1"]), ("Qidiruv tizimi", ["a2"]), ("Imkoniyat kartasi", ["uni", "yol", "moslik"]), ("Ilmiy muhit", ["a3"]),
         ("Muvofiqlik", ["talab", "a4"]), ("Moliya", ["moliya"]), ("Kalendar", ["a5"]), ("Tanlov va B reja", ["a6"]), ("Manba", ["havola", "sana"])],
    tip="Universitetni o'zingizga mos rahbar va ma'lumot bor joy sifatida tanlang. Reyting bu savolga javob bermaydi.",
    sources=f"{UKRI_STUD}; {MSCA}; {EURAXESS}; {LEEDS}; {DORA}. {STD}",
)
