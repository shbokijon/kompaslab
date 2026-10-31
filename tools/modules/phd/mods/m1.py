from common import KCL, UKRIO, DORA, HOL, STD

MOD = dict(
    title="Ilmiy yo'nalish va tadqiqot savoli",
    desc="PhD Lab M1: keng qiziqishdan aniq tadqiqot savoliga o'tish, adabiyot qidirish tizimi, ilmiy bo'shliqni dalil bilan ko'rsatish, maqsad va vazifalar, bajarilishi mumkinlik. Natija: 2 sahifalik ilmiy yo'nalish qisqa bayoni.",
    lead="Keng qiziqishni tekshiriladigan tadqiqot savoliga aylantirasiz: adabiyotni tizimli qidirasiz, bo'shliqni maqolalar bilan ko'rsatasiz va savolni ma'lumot, vaqt va resurs bilan solishtirasiz.",
    hero="telescope", weeks="2–3", next="M2. Doktorantura tizimlari va universitet tanlash", next_href="phd-lab-m2.html",
    goals=[("telescope", "Tadqiqot savoli", "bitta asosiy savol, 2–3 kichik savol"),
           ("books", "Adabiyot xaritasi", "12 manba, har birida cheklov"),
           ("memo", "Ilmiy yo'nalish qisqa bayoni", "2 sahifa: muammo, bo'shliq, metod, xavf")],
    warn=f"Bu modul PhD arizasi uchun savol va qisqa bayon tayyorlaydi; tizimli adabiyotlar sharhi va statistika chuqur o'rgatilmaydi. Matnni o'zingiz yozasiz: Kompas namunalari faqat o'rganish uchun. Ilmiy halollik qoidalari {HOL}.",
    lessons=[
        dict(t="Qiziqishdan ilmiy muammoga", short="Muammo", min=30, kind="🔎 Toraytirish", ic="telescope",
             hook="\"Sun'iy intellekt\", \"geotermal energiya\", \"ta'lim\" bu mavzular, hali ilmiy muammo emas. Ilmiy rahbar sizdan mavzuni emas, javob izlanadigan aniq savolni kutadi. Bu dars mavzuni toraytirishni o'rgatadi.",
             body="""<p>Mavzuni to'rt o'lchov bo'yicha toraytiring:</p>
<ul><li><b>Hodisa:</b> nimani o'rganasiz (jarayon, xatti-harakat, material, model).</li><li><b>Joy yoki guruh:</b> qaysi tizim, hudud yoki aholi qatlami.</li><li><b>Bo'shliq:</b> hozircha nima noma'lum yoki ishonchsiz.</li><li><b>O'lchanadigan natija:</b> qaysi kattalik yoki dalil javob beradi.</li></ul>
<p>Soha tanlashda faqat \"hozir mashhur\" mavzuga qaramang: oldingi bilimingiz va o'sha mavzuda ishlayotgan laboratoriyalar bormi, shuni ham tekshiring. Bitta savol bir nechta muammoga tegsa, uni bitta asosiy va 2–3 kichik savolga ajrating.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: \"Sun'iy intellekt va iqlim\". Aniqroq: \"Shahar yer osti haroratining vaqt bo'yicha o'zgarishini qaysi kuzatuv usullari ishonchli ajrata oladi?\" Bu namuna ham ma'lumot borligi tekshirilmaguncha taklif emas, faqat toraytirish usuli.</div>
<div class="box warn">Savolni \"hali hech kim qilmagan\" degan tekshirilmagan da'voga qurmang. Yangilik da'vosi faqat adabiyot qidiruvidan keyin, ehtiyotkor so'zlar bilan yoziladi (1.3).</div>""",
             take="Mavzu emas, savol: hodisa, joy yoki guruh, bo'shliq va o'lchanadigan natija. Bitta asosiy savol va 2–3 kichik savol.",
             task="<ul><li>Keng qiziqishingizni bitta jumlada yozing.</li><li>Uni to'rt o'lchov bo'yicha toraytiring.</li><li>Bitta asosiy savol shakllantiring va unga qanday dalil javob berishini yozing.</li></ul>",
             ph="Qiziqish: ... → Hodisa: ...; joy: ...; bo'shliq: ...; natija: ... → Savol: ...?"),
        dict(t="Adabiyot qidirish tizimi", short="Adabiyot", min=35, kind="📚 Qidiruv", ic="books",
             hook="Kuchli PhD g'oyasi blog yoki videodan emas, tekshiriladigan adabiyot xaritasidan boshlanadi. Qidiruvni yozib borsangiz, bir oydan keyin ham nimani topganingizni va nimani o'tkazib yuborganingizni bilasiz.",
             body=f"""<h4>Qidiruv usullari</h4>
<ul><li>Kalit so'zlarning sinonimlari va mantiqiy operatorlar (AND, OR, NOT).</li><li>Iqtiboslar bo'ylab qidiruv: maqola qaysi ishlarga tayanadi va keyin kim unga tayangan.</li><li>Klassik (asos bo'lgan) ishlar va so'nggi 5 yil ishlari muvozanati.</li></ul>
<h4>Qidiruv jurnali</h4>
<p>Har qidiruv uchun yozing: baza (Scopus, Web of Science, Google Scholar yoki universitet kutubxonasi), so'rov, sana, filtr va nechta natija ko'rilgani.</p>
<h4>Manba jadvali</h4>
<div class="tbl"><table><thead><tr><th>Ustun</th><th>Nima yoziladi</th></tr></thead><tbody>
<tr><td>Muallif, yil, DOI</td><td>Aniq bibliografik ma'lumot</td></tr><tr><td>Savol va ma'lumot</td><td>Ish nimani so'ragan va qaysi ma'lumot bilan</td></tr>
<tr><td>Metod va natija</td><td>Qanday tekshirilgan, nima topilgan</td></tr><tr><td>Cheklov</td><td>Mualliflar o'zi yozgan yoki siz ko'rgan zaif joy</td></tr>
<tr><td>Sizga aloqasi</td><td>Savolingizga qanday ta'sir qiladi</td></tr></tbody></table></div>
<div class="box warn">Faqat annotatsiyani o'qib xulosa chiqarmang: metod va cheklov qismini ham o'qing. Iqtiboslar soni yoki jurnal nufuzi ishning sifatini yolg'iz o'zi ko'rsatmaydi (DORA deklaratsiyasi). Shubhali, \"pulga nashr qiladigan\" jurnallardan ehtiyot bo'ling.</div>
<div class="srcs">Manba: {DORA}.</div>""",
             take="Qidiruvni jurnalga yozing, sinonim va iqtiboslar bo'ylab kengaytiring. Har manbada savol, metod, natija va cheklovni ajrating.",
             task="<ul><li>3 ta qidiruv so'rovini yozing (baza, so'rov, sana).</li><li>12 ta asosiy manbani DOI yoki havola bilan jadvalga kiriting.</li><li>Har manbaga bitta cheklov yozing.</li></ul>",
             ph="So'rov 1: Scopus, (\"...\" OR \"...\") AND ..., 31.10.2026, 84 natija. Manbalar: 1) ..., DOI ..., cheklov: ..."),
        dict(t="Ilmiy bo'shliqni dalil bilan ko'rsatish", short="Bo'shliq", min=30, kind="🧩 Dalil", ic="miya",
             hook="\"Bu mavzuda ish yo'q\" degan gap ko'pincha noto'g'ri chiqadi va komissiyada ishonchni pasaytiradi. Bo'shliq aniq, chegaralangan va maqolalar bilan ko'rsatilgan bo'lishi kerak.",
             body="""<h4>Bo'shliq turlari</h4>
<ul><li><b>Ma'lumot bo'shlig'i:</b> kerakli kuzatuv yoki o'lchov yo'q.</li><li><b>Metod bo'shlig'i:</b> mavjud usul ma'lum sharoitda ishlamaydi.</li><li><b>Tekshiruv bo'shlig'i:</b> natija boshqa ma'lumotda sinalmagan.</li><li><b>Kontekst bo'shlig'i:</b> boshqa hudud yoki guruhda o'rganilmagan.</li><li><b>Nazariya bo'shlig'i:</b> tushuntirish qarama-qarshi yoki yetarli emas.</li></ul>
<p>\"Mavjud usullar X sharoitda ishlamaydi\" degan da'vo kamida bir nechta manbadan kelib chiqishi kerak. Yangi ma'lumotlar to'plamining o'zi har doim katta ilmiy hissa bo'lavermaydi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: \"O'zbekistonda bu haqida maqola kam\". Kuchliroq: \"Ko'rib chiqilgan 6 ishda kuzatuv chuqurligi X dan oshmagan, shuning uchun Y savoli ochiq qolmoqda\". Bu fikrlash namunasi, fakt emas.</div>
<div class="box warn">Hududda \"birinchi\" bo'lish o'z-o'zidan ilmiy ahamiyat emas: nima uchun bu kontekst natijani o'zgartirishi mumkinligini ham yozing.</div>""",
             take="Bo'shliq turini nomlang va uni 2+ manba bilan chegaralang. \"Hech kim qilmagan\" o'rniga \"ko'rilgan ishlarda ... yo'q\".",
             quiz=[("Ilmiy bo'shliqni bitta maqolaning sarlavhasidan aniqlash yetarli.", "n", "Noto'g'ri: bir nechta ishning metodi va cheklovlarini solishtirish kerak."),
                   ("\"Hech kim qilmagan\" da'vosi faqat keng qidiruvdan keyin, ehtiyotkor so'zlar bilan yoziladi.", "t", "To'g'ri."),
                   ("Hududda birinchi bo'lish o'z-o'zidan ilmiy ahamiyatni isbotlaydi.", "n", "Noto'g'ri: kontekst natijani nega o'zgartirishi tushuntiriladi."),
                   ("Ma'lumot yetmasa, zaxira ma'lumot yoki metod rejasi yoziladi.", "t", "To'g'ri: bajarilishi mumkinlik savol bilan birga baholanadi (1.5).")],
             task="<ul><li>3 ta bo'shliq gipotezasini yozing.</li><li>Har biriga 2 tadan manba biriktiring.</li><li>Eng yaxshi tekshiriladiganini tanlang va sababini yozing.</li></ul>",
             ph="Bo'shliq 1 (metod): ... — manbalar: ..., ... Tanlovim: ..., chunki ..."),
        dict(t="Savol, gipoteza, maqsad va vazifalar", short="Savol", min=30, kind="🎯 Tuzilma", ic="memo",
             hook="Tadqiqot savoli, maqsad, vazifalar va gipoteza bir xil narsa emas. Ularni aralashtirsangiz, metod tanlash ham chalkashadi va komissiya buni darhol ko'radi.",
             body="""<div class="tbl"><table><thead><tr><th>Atama</th><th>Nima</th><th>Kompas tuzgan namuna</th></tr></thead><tbody>
<tr><td>Maqsad ([[aim]])</td><td>Umumiy ilmiy maqsad</td><td>Kuzatuv usulining chegaralarini baholash</td></tr>
<tr><td>Vazifalar ([[objectives]])</td><td>Tekshiriladigan qadamlar</td><td>1) sintetik ma'lumotda sinov; 2) dala ma'lumotida tekshiruv</td></tr>
<tr><td>Gipoteza ([[hypothesis]])</td><td>Rad etilishi mumkin bo'lgan aniq kutish</td><td>Ma'lum sharoitda sezgirlik oshadi</td></tr>
</tbody></table></div>
<ul><li>Gipoteza har sohada shart emas: sifat tadqiqotlarida ochiq savol yetarli bo'lishi mumkin.</li><li>Metod vazifaga mos bo'lsin: savol sabab-oqibat haqida bo'lsa, faqat korrelyatsiya yetarli dalil emas.</li><li>Ishning muvaffaqiyatini faqat \"kutilgan natija chiqdi\" bilan bog'lamang.</li></ul>
<div class="box warn">\"O'rganish\", \"tadqiq qilish\" kabi umumiy vazifalar natija mezonisiz qoladi. Har vazifa uchun qaysi ma'lumot va qaysi ko'rsatkich javob berishini yozing.</div>""",
             take="Maqsad: umumiy yo'nalish. Vazifalar: tekshiriladigan qadamlar. Gipoteza: rad etilishi mumkin bo'lgan kutish (har sohada shart emas).",
             task="<ul><li>Bitta maqsad yozing.</li><li>3 ta vazifa belgilang, har biriga ma'lumot va ko'rsatkich.</li><li>Kerak bo'lsa, rad etilishi mumkin bo'lgan bitta gipoteza yozing.</li></ul>",
             ph="Maqsad: ... Vazifa 1: ... (ma'lumot: ..., ko'rsatkich: ...). Gipoteza: ..."),
        dict(t="Bajarilishi mumkinlik va resurslar", short="Resurs", min=30, kind="⚖️ Filtr", ic="hourglass",
             hook="Juda yaxshi ilmiy savol ham kerakli ma'lumot yoki uskuna bo'lmasa, 3–4 yillik rejaga sig'maydi. Komissiya savolning qiziqligi bilan birga uni bajarish mumkinligini ham baholaydi.",
             body="""<h4>Tekshiriladigan sakkiz band</h4>
<ul><li>Ma'lumotga kirish va uning egasi</li><li>Uskuna va laboratoriya</li><li>Hisoblash resurslari (GPU, klaster)</li><li>Xarajat</li><li>Ruxsatnomalar (dala, ma'lumot ulashish)</li><li>Etika ruxsati</li><li>Rahbarning tajribasi</li><li>Vaqt</li></ul>
<p>Ikkita dizayn yozing: <b>ideal</b> (hammasi bo'lsa) va <b>minimal</b> (asosiy ma'lumot bo'lmasa ham savolga qisman javob beradigan).</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Xavfli: \"Menga yopiq korporativ ma'lumot kerak\". Xavfni kamaytirish: \"Usulni ochiq ma'lumotda tekshiraman, ruxsat bo'lsa dala ma'lumoti bilan kengaytiraman\".</div>
<div class="box warn">Boshqa tashkilotga tegishli ma'lumotdan foydalanishga yozma ruxsat bo'lmasa, uni rejada kafolat deb yozmang. Etika ruxsati va hisoblash resursini ham avtomatik mavjud deb hisoblamang.</div>""",
             take="Sakkiz band bo'yicha tekshiring va ikki dizayn yozing: ideal va minimal. Yozma ruxsatsiz ma'lumot kafolat emas.",
             task="<ul><li>Ma'lumotga kirish jadvalini tuzing: ma'lumot, egasi, holat (bor / so'ralgan / noma'lum).</li><li>Asosiy va zaxira metodni yozing.</li><li>3 ta katta xavfni yozing.</li></ul>",
             ph="Ma'lumot: ... — egasi: ... — holat: ... Asosiy metod: ...; zaxira: ... Xavflar: 1) ..."),
        dict(t="2 sahifalik ilmiy yo'nalish qisqa bayoni", short="Bayon", min=40, kind="📝 Hujjat", ic="scroll",
             hook="Mavzuni boshqa odam bir daqiqada tushunmasa, uni qayta tuzish kerak. 2 sahifalik qisqa bayon keyingi modullarda rahbar qidirish va loyiha taklifi uchun asos bo'ladi.",
             body=f"""<h4>Tarkib</h4>
<ol><li>Muammo va ahamiyati</li><li>4–6 asosiy maqola</li><li>Bo'shliq</li><li>Tadqiqot savoli</li><li>Metodning qisqa tavsifi</li><li>Kutilgan hissa</li><li>Bajarilishi mumkinlik va xavf</li><li>Qaysi rahbar yoki guruhga mos (M3 da to'ldiriladi)</li></ol>
<p>Bu hujjat ariza matni emas: fikringizni tartibga soladigan ishchi hujjat. M4 da undan loyiha taklifi o'sadi.</p>
<div class="box info">Qoralamada \"nima o'rganaman\" ko'p, \"qanday isbotlayman\" kam bo'lsa, metod va dalil qismini kuchaytiring.</div>
<div class="box warn">Sun'iy intellekt yozgan matnni manbalarini tekshirmay o'zingizniki deb yubormang: to'qima iqtiboslar uchrashi mumkin. Universitetingizning AI siyosatini o'qing (M5.6).</div>
<div class="srcs">Manba: {KCL}; {UKRIO}. {HOL}.</div>""",
             take="Qisqa bayon: muammo, asosiy maqolalar, bo'shliq, savol, metod, hissa, xavf. U ariza emas, keyingi modullar uchun ishchi hujjat.",
             task="<ul><li>2 sahifalik qoralama yozing.</li><li>Uni 90 soniyada og'zaki tushuntirib ko'ring.</li><li>Bir kishidan fikr olib, ikkinchi versiyani yozing.</li></ul>",
             ph="v1 → fikr: ... → v2 da o'zgargani: ..."),
    ],
    tool=dict(id="bayon", short="Bayon", h2="Ilmiy yo'nalish qisqa bayoni", sub="Tadqiqot savoli, bo'shliq, dalillar va bajarilishi mumkinlikni bitta hujjatga bog'lang.",
              h3="Qisqa bayon", tag="5 maydon", ic="telescope", btn="Bayonni saqlash", badge="Savol egasi", min=4,
              fields=[dict(k="mavzu", label="Ilmiy yo'nalish", hint="hodisa va tizim", ph="..."),
                      dict(k="savol", label="Tadqiqot savoli", type="area", ph="Qaysi tekshiriladigan savol?"),
                      dict(k="boshliq", label="Bo'shliq: 3 ta dalil", hint="muallif, yil, topilma, cheklov, DOI", type="area", ph="1) ...\n2) ...\n3) ..."),
                      dict(k="metod", label="Ma'lumot va metod", type="area", ph="Ma'lumotga kirish va tekshiruv"),
                      dict(k="xavf", label="Xavf va zaxira yo'l", type="area", ph="Nima ishlamasligi mumkin va unda nima qilasiz?")]),
    check=dict(h2="M1 nazorati", sub="Qisqa bayonni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Tadqiqot savoli umumiy so'zlarsiz, aniq yozilgan.", "Qidiruv jurnali bor (baza, so'rov, sana).",
                      "12 manba DOI yoki havola bilan, har birida cheklov.", "Bo'shliq turi nomlangan va 2+ manba bilan ko'rsatilgan.",
                      "Maqsad, vazifalar va (kerak bo'lsa) gipoteza ajratilgan.", "Ideal va minimal dizayn yozilgan.",
                      "Yozma ruxsatsiz ma'lumot kafolat deb yozilmagan.", "Matn o'zimniki, AI ishlatilgan bo'lsa manbalar tekshirilgan."]),
    art_title="Ilmiy yo'nalish qisqa bayoni", art_short="Bayon",
    art=[("Muammo", ["mavzu", "a1"]), ("Adabiyot", ["a2"]), ("Bo'shliq", ["boshliq", "a3"]), ("Savol va vazifalar", ["savol", "a4"]),
         ("Metod va resurslar", ["metod", "a5"]), ("Xavf", ["xavf"]), ("Qisqa bayon (v2)", ["a6"])],
    tip="Savolingizni bitta jumlada aytib bera olmasangiz, uni hali toraytirish kerak. Rahbar bilan suhbat ham, loyiha taklifi ham shu jumladan boshlanadi.",
    sources=f"{KCL}; {UKRIO}; {DORA}. {STD}",
)
