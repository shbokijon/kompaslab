from common import CDS, DAAD_ADM, UNIPI, SIK, CAMPUSCHINA, SH, TB, NUS, NTU, MEXT, HOL, STD

MOD = dict(
    title="Universitet tanlash va ariza portfeli",
    desc="Bachelor Lab M2: uch darajali ro'yxat, moslik tahlili, an'anaviy va boshqa yo'nalishlar, ariza portfelini xavf va narx bo'yicha muvozanatlash. Natija: Saralangan ro'yxat v1.0 (8–12 universitet).",
    lead="Ko'p abituriyent 2–3 ta \"orzu\" universitetga ariza berib, hammasidan rad oladi. Bu modulda ro'yxatni xavf darajasi bo'yicha muvozanatlaysiz, har universitetni moslik bo'yicha tekshirasiz va arizalar narxini oldindan hisoblaysiz.",
    hero="compass", weeks="2", next="M3 Yo'nalish va akademik kimlik", next_href="bachelor-lab-m3.html",
    goals=[("compass", "Saralangan ro'yxat v1.0", "8–12 universitet, uch daraja bo'yicha"),
           ("chart", "Moslik baholari", "dastur, xarajat, til, shahar bo'yicha"),
           ("money", "Arizalar byudjeti", "ariza to'lovlari, testlar va hujjatlar narxi")],
    warn=f"Ariza to'lovlari, o'qish narxi va stipendiyalar har yili o'zgaradi. Bu moduldagi raqamlar o'rniga {HOL} rasmiy sahifadan o'zingiz topgan qiymatni yozing.",
    lessons=[
        dict(t="Uch darajali ro'yxat", short="Uch daraja", min=25, kind="🎯 Mini-test", ic="compass",
             hook="Faqat eng kuchli universitetlarga ariza berish ham, faqat oson universitetlarga ariza berish ham xavfli. Birinchisi rad bilan, ikkinchisi afsus bilan tugashi mumkin.",
             body="""<h4>Uch daraja</h4>
<div class="tbl"><table><thead><tr><th>Daraja</th><th>Ma'nosi</th><th>Qancha</th></tr></thead><tbody>
<tr><td><b>Orzu</b> ([[reach]])</td><td>Talablardan pastroqsiz yoki qabul juda tanlovli; qabul ehtimoli past</td><td>2–3 ta</td></tr>
<tr><td><b>Mo'ljal</b> ([[target]])</td><td>Baho va test natijangiz shu universitetga qabul qilinganlar o'rtasida</td><td>3–5 ta</td></tr>
<tr><td><b>Ishonchli</b> ([[likely]])</td><td>Talablardan yuqorisiz, dastur va narx ham sizga to'g'ri keladi</td><td>2–3 ta</td></tr>
</tbody></table></div>
<p>Muhim shart: <b>ishonchli daraja ham siz haqiqatan borishga tayyor joy bo'lishi kerak</b>. Borishni xohlamagan va to'lay olmaydigan universitet ishonchli emas, u shunchaki ro'yxatni to'ldiradi.</p>
<h4>Darajani qanday aniqlash</h4>
<ul><li>AQShda: universitetning Common Data Set'idagi qabul foizi va test ballari oralig'i (C9, C11 bo'limlari).</li>
<li>Ball asosidagi tizimlarda: o'tgan yilgi minimal ball yoki talab qilingan o'rtacha baho.</li>
<li>Xalqaro talabalar uchun qabul foizi umumiy foizdan past bo'lishi mumkin; bu ma'lumot har doim ochiq emas.</li></ul>
<div class="box warn">Qabul foizi 10 foizdan past universitet hamma uchun orzu darajasi, hatto eng kuchli abituriyent uchun ham.</div>""",
             take="Ro'yxatda 2–3 orzu, 3–5 mo'ljal va 2–3 ishonchli universitet bo'lsin. Ishonchli universitet ham siz borishga va to'lashga tayyor joy bo'lishi shart.",
             quiz=[("Qabul foizi 5 foiz bo'lgan universitet kuchli abituriyent uchun ishonchli daraja.", "n", "Noto'g'ri: juda tanlovli universitet hamma uchun orzu darajasi."),
                   ("Ishonchli universitet moliyaviy jihatdan ham sizga to'g'ri kelishi kerak.", "t", "To'g'ri: to'lay olmaydigan joy aslida variant emas."),
                   ("Faqat orzu universitetlariga ariza berish vaqt va pulni tejaydi.", "n", "Noto'g'ri: hammasidan rad olish xavfi yuqori."),
                   ("AQShda daraja aniqlashda Common Data Set'dagi test ballari oralig'idan foydalanish mumkin.", "t", "To'g'ri: C9 bo'limida qabul qilinganlarning ball oralig'i bor.")],
             task="<ul><li>Hozirgi ro'yxatingizdagi universitetlarni uch darajaga ajrating.</li><li>Har daraja uchun sababini bir jumlada yozing (ball, qabul foizi yoki talab).</li></ul>",
             ph="Orzu: ... (qabul foizi ...). Mo'ljal: ... Ishonchli: ..."),
        dict(t="Moslik tahlili", short="Moslik", min=30, kind="🛠 Moslik bali", ic="bulb",
             hook="Ikki universitet bir xil reytingda bo'lishi mumkin, lekin biri sizga 4 yil davomida mos keladi, ikkinchisi yo'q. Moslik reytingdan keyin keladigan asosiy filtr.",
             body="""<h4>Olti mezon</h4>
<div class="tbl"><table><thead><tr><th>Mezon</th><th>Nimani tekshirasiz</th></tr></thead><tbody>
<tr><td>Dastur tarkibi</td><td>1–4 kursdagi majburiy fanlar, tanlov fanlari, amaliyot, bitiruv loyihasi. O'quv rejasini ([[curriculum]] yoki [[module catalogue]]) oching.</td></tr>
<tr><td>Laboratoriya va tadqiqot</td><td>Bakalavrlar laboratoriyaga qo'yiladimi? Yozgi tadqiqot dasturi bormi?</td></tr>
<tr><td>Til</td><td>Butun dastur ingliz tilidami yoki yuqori kurslarda mahalliy til kerakmi?</td></tr>
<tr><td>Xarajat</td><td>O'qish to'lovi + yashash; stipendiya imkoniyati (M11–M12)</td></tr>
<tr><td>Shahar va iqlim</td><td>Katta shahar yoki kichik shaharcha; qish, issiq, oziq-ovqat</td></tr>
<tr><td>Xavfsizlik va qo'llab-quvvatlash</td><td>Xalqaro talabalar ofisi, yotoqxona kafolati, sog'liq xizmati</td></tr>
</tbody></table></div>
<p>Har mezonni 0–3 ball bilan baholang. Umumiy ball 18 dan; 12 dan past universitet ro'yxatda qolishi uchun alohida sabab kerak.</p>
<h4>Ma'lumot qayerdan</h4>
<ul><li>Dastur sahifasi va o'quv rejasi PDF fayli.</li><li>Xalqaro talabalar bo'limi ([[international office]]) sahifasi.</li><li>Talabalar tashkiloti va universitet rasmiy ijtimoiy tarmoqlari.</li></ul>
<div class="box info">Talabalar forumi tajriba haqida foydali, lekin talab va narx haqida faqat rasmiy sahifaga tayaning.</div>""",
             take="Dastur, laboratoriya, til, xarajat, shahar va qo'llab-quvvatlashni 0–3 ball bilan baholang. Moslik bali reytingdan keyingi asosiy filtr.",
             task="<ul><li>Ro'yxatingizdagi 3 universitetni olti mezon bo'yicha 0–3 ball bilan baholang.</li><li>Eng past ball olgan mezonni va uni qanday tekshirishingizni yozing.</li></ul>",
             ph="... universiteti: dastur 3, laboratoriya 2, til 3, xarajat 1, shahar 2, qo'llab-quvvatlash 2 = 13/18 ..."),
        dict(t="An'anaviy yo'nalishlar", short="An'anaviy", min=35, kind="🗺 Taqqoslash", ic="books",
             hook="AQSh, Buyuk Britaniya, Germaniya, Koreya va Yaponiya o'zbek abituriyentlari eng ko'p tanlaydigan yo'nalishlar. Ularning har birida tizim, til va pul mantig'i boshqacha.",
             body=f"""<div class="tbl"><table><thead><tr><th>Mamlakat</th><th>Tizim</th><th>Til</th><th>Pul mantig'i</th></tr></thead><tbody>
<tr><td>AQSh</td><td>4 yil, birinchi 1–2 yil umumiy fanlar, mutaxassislik keyinroq tanlanadi</td><td>Ingliz</td><td>O'qish narxi yuqori; ayrim universitetlar xalqaro talabalarga ehtiyojga asoslangan yordam beradi (M12)</td></tr>
<tr><td>Buyuk Britaniya</td><td>Odatda 3 yil (Shotlandiyada 4), birinchi kundan mutaxassislik</td><td>Ingliz</td><td>Xalqaro talaba to'lovi yuqori; bakalavr uchun to'liq stipendiya kam</td></tr>
<tr><td>Germaniya</td><td>3–4 yil; universitet va amaliy fanlar universiteti ([[Hochschule]])</td><td>Bakalavr asosan nemis tilida, ingliz tilidagi dasturlar cheklangan</td><td>Ko'p davlat universitetlarida o'qish deyarli bepul, lekin yashash xarajati va bloklangan hisob talab qilinadi; ayrim yerlarda xalqaro talabalardan to'lov olinadi</td></tr>
<tr><td>Koreya</td><td>4 yil</td><td>Koreys, ayrim dasturlar ingliz</td><td>GKS-U to'liq stipendiya (M11); universitet stipendiyalari</td></tr>
<tr><td>Yaponiya</td><td>4 yil</td><td>Yapon, ingliz tilidagi dasturlar soni o'sib bormoqda</td><td>MEXT stipendiyasi (M11); universitet chegirmalari</td></tr>
</tbody></table></div>
<h4>Savollar ro'yxati</h4>
<ul><li>Ingliz tilidagi bakalavr dasturi bormi va u to'liqmi?</li><li>11 yillik attestat bilan kirish mumkinmi (M1)?</li><li>4 yillik umumiy xarajat qancha va uni nima qoplaydi?</li><li>Bitiruvdan keyin ishlash yoki magistraturaga o'tish imkoniyati qanday?</li></ul>
<div class="srcs">Manba: {DAAD_ADM}; {SIK}; {MEXT}; universitetlarning rasmiy sahifalari. {HOL}.</div>""",
             take="Har an'anaviy yo'nalishning o'z tizimi, tili va pul mantig'i bor. Avval ingliz tilidagi dastur, attestat talabi va 4 yillik xarajatni tekshiring.",
             task="<ul><li>Ikki an'anaviy mamlakatni tanlang va jadvaldagi to'rt savolga rasmiy manbadan javob yozing.</li></ul>",
             ph="AQSh: ... Germaniya: ..."),
        dict(t="Boshqa yo'nalishlar", short="Boshqalar", min=30, kind="🧭 Yangi xarita", ic="seedling",
             hook="Xitoy, Italiya, Vengriya, Turkiya va Singapur kamroq tanlanadi, lekin ayrim sohalarda kuchli dasturlar va davlat stipendiyalari bor. Raqobat ham ba'zan pastroq.",
             body=f"""<div class="tbl"><table><thead><tr><th>Mamlakat</th><th>Nima uchun ko'rib chiqish mumkin</th><th>E'tibor bering</th></tr></thead><tbody>
<tr><td>Xitoy</td><td>Muhandislik va texnologiyada kuchli universitetlar; Xitoy hukumati stipendiyasi (CSC)</td><td>Ko'p dastur xitoy tilida; ingliz tilidagi dasturni alohida tekshiring</td></tr>
<tr><td>Italiya</td><td>Politexnika universitetlari, davlat universitetlarida to'lov daromadga bog'liq, mintaqaviy stipendiyalar (DSU)</td><td>12 yillik ta'lim talabi (M1); kirish testlari</td></tr>
<tr><td>Vengriya</td><td>Stipendium Hungaricum: O'zbekiston hamkor davlat</td><td>Dastur va universitet sifatini alohida tekshiring</td></tr>
<tr><td>Turkiya</td><td>Türkiye Bursları; madaniy yaqinlik</td><td>Ko'p dasturlar turk tilida; til yili beriladi</td></tr>
<tr><td>Singapur</td><td>NUS va NTU jahon miqyosida kuchli</td><td>Raqobat juda yuqori; xarajat va Tuition Grant shartlari (M14)</td></tr>
</tbody></table></div>
<h4>Sifatni tekshirish</h4>
<p>Kam tanlanadigan yo'nalishda xavf: universitet nomi tanish emas, sifatini baholash qiyin. Tekshiring: soha bo'yicha reyting, akkreditatsiya, ingliz tilidagi dastur haqiqatan ishlayaptimi, bitiruvchilar qayerda.</p>
<div class="box info">Yo'nalishni \"arzon\" yoki \"oson\" deb emas, sohangiz bo'yicha kuchli joy sifatida tanlang.</div>
<div class="srcs">Manba: {CAMPUSCHINA}; {SH}; {TB}; {NUS}; {NTU}. {HOL}.</div>""",
             take="Xitoy, Italiya, Vengriya, Turkiya va Singapur ayrim sohalarda kuchli va stipendiyali. Kam tanish yo'nalishda sifatni soha reytingi va dastur tarkibi bilan tekshiring.",
             task="<ul><li>Bitta kam tanlanadigan mamlakatni tanlang.</li><li>Sohangiz bo'yicha 2 universitet toping va ingliz tilidagi dastur hamda stipendiya bor-yo'qligini yozing.</li></ul>",
             ph="Italiya: Politecnico ... — ingliz tilida ..., DSU ..."),
        dict(t="Ariza portfeli", short="Portfel", min=30, kind="💰 Byudjet", ic="money",
             hook="Har ariza pul turadi: ariza to'lovi, test natijasini yuborish, tarjima, apostil. 12 ta ariza oilaviy byudjetga sezilarli yuk bo'lishi mumkin.",
             body="""<h4>Muvozanat</h4>
<p>8–12 universitetdan iborat portfel tuzing. Har qatorda: daraja (orzu, mo'ljal, ishonchli), moslik bali (L2), ariza turi (Common App, UCAS, portal) va narx.</p>
<h4>Arizalar narxi</h4>
<div class="tbl"><table><thead><tr><th>Xarajat</th><th>Qayerdan aniqlash</th></tr></thead><tbody>
<tr><td>Ariza to'lovi</td><td>Universitet yoki platforma sahifasi; Common App'da to'lovdan ozod qilish so'rovi bor (M13)</td></tr>
<tr><td>Test natijasini yuborish</td><td>SAT, IELTS, TOEFL rasmiy saytlari</td></tr>
<tr><td>Tarjima va apostil</td><td>Tarjima idorasi narxi; apostil yig'imi gov.uz'da</td></tr>
<tr><td>Hujjat baholash</td><td>uni-assist kabi xizmatlar to'lovi</td></tr>
</tbody></table></div>
<h4>Qisqartirish qoidasi</h4>
<p>Byudjet yetmasa, avval moslik bali eng past universitetni olib tashlang, darajalar muvozanatini saqlang. Ishonchli darajani hech qachon nolga tushirmang.</p>
<div class="box warn">Narxlarni so'mda emas, asl valyutada yozing va hisoblagan kuningizdagi kursni qo'shing. Valyuta kursi o'zgarsa, byudjetni qayta hisoblang.</div>""",
             take="8–12 universitetli portfel uch darajani muvozanatlaydi va har arizaning narxini oldindan hisoblaydi. Qisqartirish kerak bo'lsa, moslik bali pastidan boshlang.",
             task="<ul><li>Portfelingizdagi har ariza uchun taxminiy narxni asl valyutada yozing.</li><li>Jami summani va to'lovdan ozod qilish mumkin bo'lgan arizalarni belgilang.</li></ul>",
             ph="1) ... — Common App, $... 2) ... — UCAS, £... Jami: ..."),
    ],
    tool=dict(id="royxat", short="Ro'yxat", h2="Saralangan ro'yxat v1.0", sub="8–12 universitet: daraja, talab, xarajat, stipendiya imkoniyati, qabul modeli.",
              h3="Saralangan ro'yxat (Shortlist)", tag="5 maydon", ic="compass", btn="Ro'yxatni saqlash", badge="Ro'yxat ustasi", min=4,
              fields=[dict(k="orzu", label="Orzu darajasi (2–3)", hint="nomi · dastur · model · moslik bali · narx", type="area", ph="... · Computer Science · yaxlit · 14/18 · $..."),
                      dict(k="moljal", label="Mo'ljal darajasi (3–5)", type="area", ph="..."),
                      dict(k="ishonchli", label="Ishonchli daraja (2–3)", type="area", ph="..."),
                      dict(k="byudjet", label="Arizalar byudjeti", hint="jami, valyuta va kurs sanasi", ph="Jami: $... (kurs: ...)"),
                      dict(k="stip", label="Stipendiya imkoniyati bor universitetlar", type="area", ph="... — universitet granti; ... — davlat stipendiyasi")]),
    check=dict(h2="Ro'yxat nazorati", sub="Ro'yxatni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Ro'yxatda 8–12 universitet bor.", "Uch daraja ham bor, ishonchli daraja bo'sh emas.",
                      "Har universitet uchun dastur sahifasi va o'quv rejasi ko'rilgan.", "Moslik bali olti mezon bo'yicha hisoblangan.",
                      "Attestat talabi (M1) har biri uchun tekshirilgan.", "Arizalar narxi asl valyutada yozilgan.",
                      "Ishonchli universitetga borishga va to'lashga tayyorman.", "Oila bilan ro'yxat va byudjet muhokama qilingan."]),
    art_title="Saralangan ro'yxat v1.0", art_short="Ro'yxat",
    art=[("Orzu darajasi", ["orzu"]), ("Mo'ljal darajasi", ["moljal"]), ("Ishonchli daraja", ["ishonchli"]),
         ("Moslik tahlili", ["a2"]), ("Yo'nalishlar bo'yicha izoh", ["a3", "a4"]), ("Stipendiya imkoniyati", ["stip"]), ("Arizalar byudjeti", ["byudjet", "a5"])],
    tip="Ro'yxatni oila bilan birga ko'rib chiqing. Ota-onangiz to'lov va masofa haqida bilishi kerak; kech chiqqan e'tiroz yakuniy tanlovni buzadi.",
    sources=f"{CDS}; {DAAD_ADM}; {UNIPI}; {SIK}; {CAMPUSCHINA}; {SH}; {TB}; {NUS}; {NTU}. {STD}",
)
