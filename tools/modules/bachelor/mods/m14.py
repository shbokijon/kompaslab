from common import a, CAMPUSCHINA, SIC, UNIVERSITALY, UNIPI, IT_VISA, NUS, NTU, MOE_SG, HOL, STD

CIMEA = a("https://www.cimea.it", "CIMEA (Italiya, xorijiy malakalarni baholash markazi)")
CISIA = a("https://www.cisiaonline.it", "CISIA (Italiya, TOLC kirish testlari)")

MOD = dict(
    title="Mamlakatlar boʻyicha imkoniyatlar: Xitoy, Italiya, Singapur",
    desc="Bachelor Lab M14: Xitoyda STEM universitetlari, Xitoyga ariza va motivatsion xat, Italiyada STEM va kirish testlari, Universitaly va talaba vizasi, Singapur (NUS, NTU) talablari va ariza strategiyasi. Natija: tanlangan yo'nalish bo'yicha ariza paketi.",
    lead="Bu modul uchta kam tanlanadigan, lekin STEM uchun kuchli yo'nalishni chuqur ko'rib chiqadi. Hammasini o'qing, lekin ariza paketini bittasi uchun tuzing: o'zingizga eng mos bo'lgani uchun.",
    hero="telescope", weeks="2–3", next="M15 Intervyu va qabul qarori", next_href="bachelor-lab-m15.html",
    goals=[("telescope", "Tanlangan yo'nalish", "Xitoy, Italiya yoki Singapur, asos bilan"),
           ("scroll", "Ariza paketi", "universitetlar, hujjatlar, testlar, muddatlar"),
           ("memo", "Motivatsion xat yoki o'qish rejasi rejasi", "yo'nalish formatiga mos")],
    warn=f"Bu mamlakatlarda qabul tartibi, test talablari va viza qoidalari tez-tez yangilanadi. Bu moduldagi ma'lumot {HOL}; ariza paketidagi har bandni universitet va konsullik sahifasidan tekshiring.",
    lessons=[
        dict(t="Xitoyda STEM universitetlari", short="Xitoy", min=25, kind="🗺 Xarita", ic="books",
             hook="Xitoyning ko'p universitetlari muhandislik va informatika bo'yicha jahon reytinglarida yuqori o'rinda. Lekin bakalavr uchun til tanlovi asosiy savol.",
             body=f"""<h4>Universitetlar xaritasi</h4>
<p>Xitoyda kuchli texnik universitetlar bir nechta shaharda: Pekin, Shanxay, Xanchjou, Nankin, Uxan, Sian, Xarbin va boshqalar. Universitet tanlovida M2 qoidasi amal qiladi: avval sohangiz bo'yicha reyting va dastur, keyin shahar va xarajat.</p>
<h4>Til</h4>
<div class="tbl"><table><thead><tr><th>Variant</th><th>Nima kerak</th></tr></thead><tbody>
<tr><td>Xitoy tilida bakalavr</td><td>Odatda HSK sertifikati (daraja universitetga qarab) yoki bir yillik tayyorlov kursi</td></tr>
<tr><td>Ingliz tilida bakalavr</td><td>IELTS/TOEFL; dasturlar soni cheklangan, har universitet ro'yxatini tekshiring</td></tr>
</tbody></table></div>
<h4>Dasturni tekshirish</h4>
<ul><li>Dastur haqiqatan ingliz tilida to'liq o'qitiladimi (faqat birinchi yil emas)?</li><li>Xalqaro talabalar alohida guruhdami yoki mahalliy talabalar bilan birga?</li><li>Bitiruvchilar qayerda ishlaydi yoki o'qiydi?</li></ul>
<div class="srcs">Manba: {SIC}; {CAMPUSCHINA}; universitetlarning xalqaro talabalar sahifalari. {HOL}.</div>""",
             take="Xitoyda kuchli texnik universitetlar ko'p; bakalavr uchun asosiy savol til: xitoy (HSK yoki tayyorlov yili) yoki cheklangan ingliz tilidagi dasturlar.",
             quiz=[("Xitoyda barcha bakalavr dasturlari ingliz tilida.", "n", "Noto'g'ri: ko'pi xitoy tilida; ingliz tilidagi dasturlar cheklangan."),
                   ("Xitoy tilidagi dastur uchun HSK yoki tayyorlov yili talab qilinishi mumkin.", "t", "To'g'ri."),
                   ("Italiyada ba'zi universitetlar xorijiy hujjat uchun CIMEA taqqoslash hujjatini so'rashi mumkin.", "t", "To'g'ri: universitet talabini tekshiring."),
                   ("Singapur MOE Tuition Grant hech qanday majburiyatsiz.", "n", "Noto'g'ri: bitiruvdan keyin Singapurda ishlash majburiyati bor.")],
             task="<ul><li>Sohangiz bo'yicha Xitoydagi 3 universitetni toping.</li><li>Har birida ingliz tilidagi bakalavr dasturi bor-yo'qligini va til talabini yozing.</li></ul>",
             ph="... — ingliz tilida: ..., til talabi: ..."),
        dict(t="Xitoyga ariza va motivatsion xat", short="Xitoy ariza", min=30, kind="🛠 O'qish rejasi", ic="memo",
             hook="Xitoy universitetlari va CSC ko'pincha \"o'qish rejasi\" yoki motivatsion xat so'raydi. Bu AQSh inshosi emas: aniq, rasmiy va reja ko'rinishida.",
             body=f"""<h4>Bosqichlar</h4>
<ol><li>Universitet va dastur tanlash; universitet xalqaro bo'limi sahifasidan muddatlarni yozish.</li><li>Universitet portalida ariza (ko'pincha bepul yoki kichik to'lov).</li><li>Stipendiya bilan bo'lsa: CSC portalida ham ariza (M11), agentlik raqami ([[agency number]]) universitet yoki elchixonadan.</li><li>Hujjatlar: attestat va baholar (notarial tarjima), pasport, tibbiy ko'rik formasi, tavsiya xatlari, o'qish rejasi.</li><li>Qabul xati va JW201/JW202 formasi (talaba vizasi uchun), keyin X1 vizasi.</li></ol>
<h4>O'qish rejasi (Study Plan) formati</h4>
<p>Kompas freymvorki: <b>Hozirgi holat → Bo'shliq → Strategiya → Vaqt</b>.</p>
<ul><li><b>Hozirgi holat</b>: ta'limingiz, yutuqlar, qiziqish sohasi.</li><li><b>Bo'shliq</b>: nimani o'rganishingiz kerak va nega bu Xitoyda, shu universitetda.</li><li><b>Strategiya</b>: til yili, asosiy fanlar, laboratoriya yoki loyiha.</li><li><b>Vaqt</b>: yillar bo'yicha reja va bitiruvdan keyingi maqsad.</li></ul>
<p>Hajm odatda 800–1500 so'z (universitet yoki CSC talabini tekshiring).</p>
<div class="srcs">Manba: {CAMPUSCHINA}; universitet xalqaro bo'limlari. {HOL}.</div>""",
             take="Xitoyga ariza: universitet portali, stipendiya bo'lsa CSC portali, notarial hujjatlar, keyin JW formasi va X1 viza. O'qish rejasi: hozirgi holat, bo'shliq, strategiya, vaqt.",
             task="<ul><li>Bitta Xitoy universiteti uchun ariza bosqichlari va hujjatlarni yozing.</li><li>O'qish rejasining to'rt qismi uchun 2 tadan asosiy fikr yozing.</li></ul>",
             ph="Universitet: ... Bosqichlar: ... Reja: holat — ..., bo'shliq — ..., strategiya — ..., vaqt — ..."),
        dict(t="Italiyada STEM", short="Italiya", min=30, kind="🧭 Dasturlar", ic="seedling",
             hook="Italiya politexnika universitetlari muhandislik va arxitektura bo'yicha Yevropada kuchli, davlat universitetlarida o'qish to'lovi esa ko'pincha oila daromadiga bog'liq.",
             body=f"""<h4>Universitetlar</h4>
<p>Politexnika universitetlari (Milan, Turin, Bari) va muhandislik fakulteti kuchli davlat universitetlari (masalan Bolonya, Padova, Pisa). Ingliz tilidagi bakalavr dasturlari soni magistraturaga nisbatan kam; ro'yxatni har universitet sahifasidan oling.</p>
<h4>Kirish talablari</h4>
<ul><li><b>12 yillik ta'lim</b> (M1): 11 yillik attestat bilan ko'pincha universitetda o'qilgan yil(lar) talab qilinadi.</li><li><b>Kirish testi</b>: ko'p muhandislik dasturlari CISIA TOLC testi yoki universitetning o'z testini talab qiladi; ba'zilari SAT natijasini qabul qiladi. Joylar soni cheklangan dasturlarda ([[numero programmato]]) reyting tuziladi.</li><li><b>Til</b>: ingliz tilidagi dastur uchun IELTS/TOEFL; italyan tilidagi dastur uchun italyan tili sertifikati.</li><li><b>Hujjatlar</b>: attestat, tarjima va legallashtirish; ba'zi universitetlar CIMEA taqqoslash hujjatini yoki Italiya konsulligining qiymat deklaratsiyasini so'raydi.</li></ul>
<h4>Xarajat</h4>
<p>Davlat universitetlarida o'qish to'lovi ko'pincha oila daromadiga qarab hisoblanadi; mintaqaviy DSU stipendiyasi (M11) ham daromad hujjatlari bilan.</p>
<div class="srcs">Manba: {CISIA}; {CIMEA}; {UNIPI}; universitetlarning rasmiy sahifalari. {HOL}.</div>""",
             take="Italiya: politexnikalar kuchli, ingliz tilidagi bakalavr kam. 12 yillik ta'lim, TOLC yoki universitet testi, legallashtirish va daromadga bog'liq to'lovni tekshiring.",
             task="<ul><li>Sohangiz bo'yicha 2 ta Italiya bakalavr dasturini toping (ingliz tilida bo'lsa yaxshi).</li><li>Har biri uchun kirish testi, joylar soni va attestat talabini yozing.</li></ul>",
             ph="... — test: ..., joylar: ..., attestat: ..."),
        dict(t="Italiyaga ariza va viza", short="Universitaly", min=25, kind="🗺 Bosqichlar", ic="calendar",
             hook="Italiyada universitet qabul qilgani yetarli emas: Universitaly orqali oldindan ro'yxatdan o'tmasangiz, talaba vizasi jarayoni boshlanmaydi.",
             body=f"""<h4>Bosqichlar</h4>
<ol><li><b>Universitetga ariza</b>: universitet portalida, uning muddatlarida (ko'pincha qish va bahor).</li><li><b>Universitaly'da oldindan ro'yxatdan o'tish</b> ([[pre-enrolment]]): universitet arizani ko'rib chiqadi va tasdiqlaydi. Pisa universiteti sahifasiga ko'ra 2026/27 uchun muddat 30.09.2026 edi, lekin portal ochilishi bilan erta topshirish tavsiya qilinadi; boshqa universitetlarda muddat boshqacha bo'lishi mumkin.</li><li><b>Konsullik</b>: tasdiqlangandan keyin Italiya diplomatik vakolatxonasi D turidagi o'qish vizasi bo'yicha bog'lanadi. Oldindan ro'yxatdan o'tish vizani kafolatlamaydi.</li><li><b>Viza hujjatlari</b>: odatda moliyaviy imkoniyat dalili, turar joy, tibbiy sug'urta, aviabilet bron. Ro'yxatni Visto per l'Italia saytidan tekshiring.</li><li><b>Kelgandan keyin</b>: belgilangan muddatda yashash ruxsatnomasiga ([[permesso di soggiorno]]) ariza.</li></ol>
<div class="box warn">Viza tayinlanishi va berilishi vaqt oladi. Pisa universiteti 2026/27 uchun 30.11.2026 gacha berilgan vizalarni qabul qilishini yozgan: kech qolsangiz, o'qish yili o'tkazib yuboriladi.</div>
<div class="srcs">Manba: {UNIVERSITALY}; {UNIPI}; {IT_VISA}. {HOL}.</div>""",
             take="Italiya: universitet arizasi → Universitaly oldindan ro'yxat → konsullik va D turidagi viza → kelgach permesso. Hamma bosqichni erta boshlang.",
             task="<ul><li>Italiyadagi tanlangan universitet uchun 5 bosqichli rejani sanalar bilan yozing.</li><li>Viza hujjatlari ro'yxatini rasmiy saytdan ko'chiring.</li></ul>",
             ph="1) Ariza: ... 2) Universitaly: ... 3) Konsullik: ... 4) Hujjatlar: ... 5) Permesso: ..."),
        dict(t="Singapur universitetlari", short="Singapur", min=25, kind="⚖️ Talablar", ic="chart",
             hook="NUS va NTU jahon reytinglarida Osiyoning eng kuchli universitetlari qatorida. Xalqaro bakalavr qabuli juda tanlovli va attestat talabi alohida tekshirilishi kerak.",
             body=f"""<h4>NUS va NTU</h4>
<ul><li>Ikkalasida ham muhandislik, informatika va tabiiy fanlar kuchli; o'qish ingliz tilida.</li><li>Xalqaro malaka bilan ariza: har universitetning mamlakat bo'yicha talablari sahifasi bor. O'zbekiston attestati bilan qanday qo'shimcha talab (masalan SAT yoki ACT, fan testlari, xalqaro malakalar) qo'yilishini shu sahifadan tekshiring.</li><li>Til: IELTS yoki TOEFL (ingliz tilida o'qitilmagan maktablar uchun).</li><li>Ba'zi dasturlarda intervyu yoki qo'shimcha test.</li></ul>
<h4>Raqobat</h4>
<p>Xalqaro o'rinlar soni cheklangan. Singapurni orzu darajasida (M2) ko'ring va ro'yxatni boshqa yo'nalishlar bilan muvozanatlang.</p>
<h4>Xarajat va Tuition Grant</h4>
<p>Singapur Ta'lim vazirligining Tuition Grant'i xalqaro talabalar uchun o'qish to'lovining katta qismini qoplaydi, lekin uni olgan talaba bitiruvdan keyin Singapurdagi tashkilotda bir necha yil (hozirgi qoidada 3 yil) ishlash majburiyatini oladi. Bu M11 dagi \"majburiyat\" mezoniga misol.</p>
<div class="srcs">Manba: {NUS}; {NTU}; {MOE_SG}. {HOL}.</div>""",
             take="NUS va NTU kuchli, lekin juda tanlovli; attestat bo'yicha qo'shimcha talabni mamlakat sahifasidan tekshiring. Tuition Grant bitiruvdan keyin Singapurda ishlash majburiyati bilan keladi.",
             task="<ul><li>NUS yoki NTU ning O'zbekiston (yoki xalqaro) malaka talablarini yozing.</li><li>Tuition Grant majburiyati siz uchun maqbulmi, 2–3 jumlada yozing.</li></ul>",
             ph="NUS: ... talablar: ... Tuition Grant: ..."),
        dict(t="Singapurga ariza strategiyasi", short="Strategiya", min=25, kind="🛠 Paket", ic="compass",
             hook="Singapur arizasi AQSh va Yevropa elementlarini birlashtiradi: test natijalari, insho savollari va moliyaviy yordam alohida ariza bilan.",
             body=f"""<h4>Ariza paketi (umumiy)</h4>
<div class="tbl"><table><thead><tr><th>Qism</th><th>Izoh</th></tr></thead><tbody>
<tr><td>Onlayn ariza</td><td>Universitet portali; dastur tanlovlari tartibi muhim</td></tr>
<tr><td>Akademik hujjatlar</td><td>Baholar, attestat yoki kutilayotgan natija, tarjima</td></tr>
<tr><td>Testlar</td><td>SAT/ACT va boshqalar (agar malaka bo'yicha talab qilinsa), IELTS/TOEFL</td></tr>
<tr><td>Yozma qism</td><td>Qisqa savollar yoki insholar (M9–M10 ko'nikmalari)</td></tr>
<tr><td>Yutuqlar</td><td>Olimpiada va tanlovlar (M6), hujjat bilan</td></tr>
<tr><td>Moliyaviy yordam</td><td>Tuition Grant va universitet stipendiyalari, ehtiyojga asoslangan yordam: alohida ariza va muddatlar</td></tr>
</tbody></table></div>
<h4>Strategiya</h4>
<ul><li>Dastur tanlovlarini o'z kuchli fanlaringizga moslang.</li><li>Olimpiada natijasi kuchli dalil: hujjatlari tayyor bo'lsin.</li><li>Ariza oynasi odatda kuz-qishda; joriy yil sanalarini rasmiy sahifadan oling.</li></ul>
<div class="srcs">Manba: {NUS}; {NTU}; {MOE_SG}. {HOL}.</div>""",
             take="Singapur paketi: portal, hujjatlar, testlar, qisqa insholar, yutuqlar va alohida moliyaviy yordam arizasi. Dastur tanlovlarini kuchli fanlaringizga moslang.",
             task="<ul><li>Uch yo'nalishdan (Xitoy, Italiya, Singapur) birini tanlang va sababini yozing.</li><li>Pastdagi vositada shu yo'nalish uchun ariza paketini to'ldiring.</li></ul>",
             ph="Tanlov: ..., chunki ..."),
    ],
    tool=dict(id="paket", short="Paket", h2="Ariza paketi", sub="Tanlangan yo'nalish bo'yicha: universitetlar, hujjatlar, testlar, muddatlar, yozma qism va moliyalashtirish.",
              h3="Ariza paketi", tag="6 maydon", ic="scroll", btn="Paketni saqlash", badge="Yo'nalish ustasi", min=5,
              fields=[dict(k="yon", label="Tanlangan yo'nalish", type="select", opts=["Xitoy", "Italiya", "Singapur"]),
                      dict(k="uni", label="Universitetlar va dasturlar", hint="2–4 ta, havola bilan", type="area", ph="..."),
                      dict(k="hujjat", label="Hujjatlar va legallashtirish", type="area", ph="Attestat: tarjima + ... ; CIMEA/notarius ..."),
                      dict(k="test", label="Testlar va til", type="area", ph="IELTS ..., TOLC/SAT ..., HSK ..."),
                      dict(k="muddat", label="Muddatlar va viza bosqichlari", hint="manba va sana bilan", type="area", ph="Ariza: ..., Universitaly/JW202: ..., viza: ..."),
                      dict(k="pul", label="Moliyalashtirish", type="area", ph="CSC / DSU / Tuition Grant / oila ...")]),
    check=dict(h2="Paket nazorati", sub="Paketni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Yo'nalish sohamga mos va sababi yozilgan.", "Dastur tili va til talabi tekshirilgan.",
                      "Attestat talabi (12 yil, qo'shimcha test yoki malaka) aniqlangan.", "Kirish testi va ro'yxatdan o'tish sanalari yozilgan.",
                      "Legallashtirish va tarjima talablari aniq.", "Viza bosqichlari va hujjatlari rasmiy saytdan olingan.",
                      "Moliyalashtirish va uning majburiyatlari o'qilgan.", "Har ma'lumot yonida manba va sana bor."]),
    art_title="Ariza paketi", art_short="Paket",
    art=[("Tanlangan yo'nalish", ["yon", "a6"]), ("Universitetlar va dasturlar", ["uni", "a1", "a3", "a5"]), ("Hujjatlar", ["hujjat"]), ("Testlar va til", ["test"]),
         ("Muddatlar va viza", ["muddat", "a4"]), ("O'qish rejasi yoki motivatsion xat rejasi", ["a2"]), ("Moliyalashtirish", ["pul"])],
    tip="Kam tanlanadigan yo'nalishda o'sha universitetning hozirgi talabasini toping (rasmiy talabalar tashkiloti orqali) va 3 ta aniq savol bering.",
    sources=f"{SIC}; {CAMPUSCHINA}; {CISIA}; {CIMEA}; {UNIVERSITALY}; {UNIPI}; {IT_VISA}; {NUS}; {NTU}; {MOE_SG}. {STD}",
)
