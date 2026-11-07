from common import KCL, UKRIO, DORA, HOL, STD

MOD = dict(
    title="Ilmiy yo'nalish va tadqiqot savoli",
    desc="PhD Lab M1: keng qiziqishdan aniq va tekshiriladigan tadqiqot savoliga o'tish: adabiyot qidiruvi, tadqiqot bo'shlig'ini dalillash, maqsad va vazifalar, bajarilishi mumkinlik. Natija: 2 sahifalik yo'nalish bayoni.",
    lead="“Sun'iy intellekt”, “geotermal energiya”, “ta'lim” mavzu, lekin hali ilmiy savol emas. Bu modulda qiziqishingizni dalil bilan javob berib bo'ladigan savolga aylantirasiz va uni boshqa odam bir daqiqada tushunadigan 2 sahifalik bayonga yig'asiz.",
    hero="telescope", weeks="2–3", next="M2 Doktorantura tizimlari va universitet tanlash", next_href="phd-lab-o.html?m=2",
    goals=[("telescope", "Bitta asosiy tadqiqot savoli", "fenomen, joy yoki populyatsiya, o'lchanadigan natija bilan"),
           ("books", "12 manbalik adabiyot jadvali", "DOI yoki havola, usul, natija va cheklov bilan"),
           ("memo", "2 sahifalik yo'nalish bayoni", "M3 da ilmiy rahbarga yozishdan oldingi asosiy hujjat")],
    warn="Chegara: bu modul ilmiy uslubni to'liq o'rgatmaydi. Tizimli adabiyotlar sharhi (systematic review) va chuqur statistika Research Lab da. Bu yerda PhD arizasi uchun savol va qisqa bayon tayyorlanadi. Namunalar Kompas tuzgan o'quv misollari: faktlarni o'z sohangizdagi manbalardan oling.",
    lessons=[
        dict(t="Qiziqishdan muammoga", short="Muammo", min=25, kind="🎯 Toraytirish", ic="telescope",
             hook="“Sun'iy intellekt”, “geotermal”, “ta'lim” so'zlari mavzu, lekin ilmiy muammo emas. Professor va komissiya sizdan mavzuni emas, javob berib bo'ladigan savolni kutadi.",
             body=f"""<h4>Toraytirishning to'rt o'qi</h4>
<p>Tadqiqot yo'nalishini to'rtta narsaga qisqartiring: <b>fenomen</b> (nima o'rganiladi), <b>joy yoki populyatsiya</b> (qayerda, kimda), <b>bo'shliq</b> (nima noma'lum) va <b>o'lchanadigan natija</b> (javob nimada ko'rinadi).</p>
<ul><li>Soha tanlashda faqat trendga qaramang: avvalgi bilimingiz va real laboratoriya imkoniyati muhimroq.</li><li>Savol bir nechta muammoga tegsa, uni asosiy va yordamchi savollarga ajrating.</li></ul>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: “Sun'iy intellekt va iqlim”. Kuchliroq: “Shahar yer osti haroratining vaqt bo'yicha o'zgarishini qaysi kuzatuvlar ishonchli ajrata oladi?” Bu ham ma'lumot borligi tekshirilmaguncha taklif emas.</div>
<div class="box warn">Savolni “hali hech kim qilmagan” degan tekshirilmagan yangilik da'vosiga qurmang.</div>""",
             take="Mavzu emas, savol kerak: fenomen, joy, bo'shliq va o'lchanadigan natija aniq bo'lsa, savolga dalil bilan javob berish mumkin.",
             task="<ul><li>Keng qiziqishingizni bitta jumlada yozing.</li><li>Uni fenomen, joy yoki populyatsiya va vaqt bo'yicha toraytiring.</li><li>Bitta asosiy savolni yozing.</li></ul><p><b>O'zingizga savol:</b> savolingizga qanday dalil javob bera oladi?</p>",
             ph="Qiziqish: ... → Fenomen: ..., joy: ..., vaqt: ... → Savol: ...?"),
        dict(t="Adabiyot izlash strategiyasi", short="Adabiyot", min=35, kind="🔎 Qidiruv", ic="books",
             hook="Kuchli PhD fikri bloglardan emas, tekshiriladigan adabiyot xaritasidan boshlanadi. “Ko'p maqola o'qidim” degan gap natija emas.",
             body=f"""<h4>Qidiruv usullari</h4>
<ul><li>Kalit so'zlar va ularning sinonimlari; mantiqiy operatorlar ([[AND]], [[OR]], [[NOT]]).</li><li>Iqtibos zanjiri ([[citation chaining]]): maqola kimga tayangan va uni kim keltirgan.</li><li>Asosiy (klassik) va so'nggi besh yildagi ishlar muvozanati.</li></ul>
<h4>Qidiruv jurnali</h4>
<p>Har qidiruvda bazani, so'rovni, sanani, filtrni va topilganlarni yozing. Shunda qidiruvni qaytarish va kengaytirish mumkin bo'ladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> 12 maqolalik boshlang'ich jadval ustunlari: muallif, yil, savol, ma'lumot, usul, natija, cheklov, sizning savolingizga aloqasi.</div>
<div class="box warn">Yirtqich jurnallardagi ([[predatory journals]]) maqolalardan ehtiyot bo'ling. Iqtiboslar soni ilmiy sifatning yagona o'lchovi emas (DORA). Faqat annotatsiyani o'qib xulosa chiqarmang: usul va cheklovlarni ham o'qing.</div>
<div class="srcs">Manba: {DORA}. {HOL}.</div>""",
             take="Adabiyot qidiruvi qaytarib bo'ladigan jarayon: so'rov, sana va filtr yozilgan jurnal va 12 manbalik jadval.",
             quiz=[("Iqtiboslar soni ko'p bo'lsa, maqola albatta sifatli.", "n", "Noto'g'ri: DORA ko'rsatkichlarni yagona sifat o'lchovi sifatida ishlatmaslikni tavsiya qiladi."),
                   ("Qidiruv jurnalida baza, so'rov, sana va filtr yoziladi.", "t", "To'g'ri: shunda qidiruvni boshqa odam ham qaytara oladi."),
                   ("Geografik “birinchi”lik avtomatik ravishda ilmiy ahamiyat beradi.", "n", "Noto'g'ri: yangi joy o'zi ilmiy hissa emas; bo'shliqni dalil bilan ko'rsatish kerak."),
                   ("Gipoteza har bir ilmiy sohada majburiy emas.", "t", "To'g'ri: masalan, ko'p sifatli tadqiqotlarda gipoteza qo'yilmaydi.")],
             task="<ul><li>3 ta qidiruv so'rovini yozing (sinonim va operatorlar bilan).</li><li>12 ta muhim manbani DOI yoki havola bilan to'plang.</li><li>Har manbaga bitta cheklov yozing.</li></ul><p><b>O'zingizga savol:</b> so'nggi besh yildagi ishlar bilan klassik maqolalarni ajratdingizmi?</p>",
             ph="So'rov 1: ... ; So'rov 2: ... ; 1) Muallif, yil, DOI — usul ..., cheklov ..."),
        dict(t="Tadqiqot bo'shlig'ini isbotlash", short="Bo'shliq", min=30, kind="🧩 Dalil", ic="miya",
             hook="“Bu mavzuda hali ish yo'q” deyish ko'pincha noto'g'ri chiqadi. Bo'shliq aniq, chegaralangan va manbalar bilan ko'rsatilgan bo'lishi kerak.",
             body=f"""<h4>Bo'shliq turlari</h4>
<div class="tbl"><table><thead><tr><th>Tur</th><th>Nimani bildiradi</th></tr></thead><tbody>
<tr><td>Ma'lumot bo'shlig'i</td><td>Kerakli kuzatuv yoki o'lchov yo'q</td></tr>
<tr><td>Usul bo'shlig'i</td><td>Mavjud usullar ma'lum sharoitda ishlamaydi</td></tr>
<tr><td>Tekshiruv bo'shlig'i</td><td>Natija mustaqil ma'lumotda sinalmagan</td></tr>
<tr><td>Kontekst bo'shlig'i</td><td>Boshqa joy yoki populyatsiyada o'rganilmagan</td></tr>
<tr><td>Nazariya bo'shlig'i</td><td>Kuzatuvni tushuntiradigan izohlar qarama-qarshi</td></tr>
</tbody></table></div>
<p>“Mavjud usullar X sharoitda ishlamaydi” degan da'vo bir nechta manbadan kelib chiqishi kerak. Yangi ma'lumotlar to'plami ham o'zi yuqori ilmiy hissa bo'lmasligi mumkin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: “O'zbekistonda bu haqida maqola kam.” Kuchliroq: “Ko'rilgan 6 ishda sensor qamrovi X chuqurlikdan o'tmagan, shuning uchun Y savol ochiq qoladi.” Bu mantiq namunasi, fakt emas.</div>
<div class="box warn">Geografik “birinchi”likni avtomatik ravishda ilmiy ahamiyat deb olmang.</div>""",
             take="Bo'shliq turi nomlangan va kamida ikkita manba bilan cheklangan bo'lsa, u da'vo emas, dalilga aylanadi.",
             task="<ul><li>3 ta bo'shliq farazini yozing.</li><li>Har biriga 2 tadan manba biriktiring.</li><li>Eng tekshiriladiganini tanlang.</li></ul><p><b>O'zingizga savol:</b> bo'shliq haqidagi da'voingizni qaysi ikki ish bilan cheklay olasiz?</p>",
             ph="Bo'shliq 1 (usul): ... — manbalar: ..., ... ; Tanlov: ..."),
        dict(t="Savol, maqsad, vazifa va gipoteza", short="Maqsad", min=25, kind="🧭 Tuzilma", ic="compass",
             hook="Tadqiqot savoli, maqsad, vazifalar va gipoteza bir xil narsa emas. Ularni aralashtirsangiz, usul ham noaniq bo'ladi.",
             body=f"""<ul><li><b>Maqsad</b> ([[aim]]): umumiy ilmiy niyat.</li><li><b>Vazifalar</b> ([[objectives]]): tekshiriladigan qadamlar.</li><li><b>Gipoteza</b> ([[hypothesis]]): rad etilishi mumkin bo'lgan aniq kutilma. Har sohada majburiy emas.</li></ul>
<p>Usul vazifalarga mos bo'lishi kerak: savol sababiy bo'lsa, yolg'iz korrelyatsiya yetarli dalil emas. Ishning muvaffaqiyati faqat kutilgan natija chiqishiga bog'lanmasin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Maqsad: kuzatuv usulining chegarasini baholash. 1-vazifa: sintetik sinov. 2-vazifa: dala ma'lumotida tekshiruv. Gipoteza: ma'lum sharoitda sezgirlik oshadi.</div>
<div class="box warn">“O'rganish”, “tadqiq qilish” kabi umumiy vazifa natija mezonisiz qolmasin.</div>""",
             take="Maqsad bitta, vazifalar 2–3 ta va har biri o'lchanadigan; gipoteza faqat rad etish mumkin bo'lsa qo'yiladi.",
             task="<ul><li>Bitta maqsad yozing.</li><li>3 ta vazifa belgilang.</li><li>Kerak bo'lsa, bitta rad etilishi mumkin bo'lgan gipoteza yozing.</li></ul><p><b>O'zingizga savol:</b> har vazifaga javob beradigan ma'lumot va ko'rsatkich bormi?</p>",
             ph="Maqsad: ... ; 1) ... (ko'rsatkich: ...) 2) ... 3) ... ; Gipoteza: ..."),
        dict(t="Bajarilishi mumkinlik va resurslar", short="Resurs", min=25, kind="🛠 Tekshiruv", ic="hourglass",
             hook="Juda yaxshi savol ham ma'lumot yoki uskuna bo'lmasa 3–4 yillik rejaga sig'maydi. Buni ariza oldidan aniqlash kerak.",
             body=f"""<h4>Tekshiruv bandlari</h4>
<p>Ma'lumotga kirish, uskuna, xarajat, ruxsatlar, hisoblash resurslari, tadqiqot etikasi, ilmiy rahbar tajribasi va vaqt.</p>
<p>Ideal tadqiqot dizayni va minimal ishlaydigan dizaynni alohida yozing. Boshqa guruhga tegishli ma'lumotga ruxsat xati bo'lmasa, uni kafolat deb hisoblamang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Xavf: “Menga yopiq korxona ma'lumoti kerak.” Xavfni kamaytirish: “Usulni ochiq ma'lumotda tekshiraman, ruxsat bo'lsa dala ma'lumoti bilan kengaytiraman.”</div>
<div class="box warn">Yopiq ma'lumot, etika ruxsati yoki GPU imkoniyatini avtomatik mavjud deb hisoblamang.</div>""",
             take="Har resurs uchun “bor / so'raladi / yo'q” holatini yozing; asosiy va zaxira usul bo'lsa, reja bajariladi.",
             task="<ul><li>Ma'lumotga kirish jadvalini tuzing.</li><li>Asosiy va zaxira usulni belgilang.</li><li>3 ta katta xavfni yozing.</li></ul><p><b>O'zingizga savol:</b> asosiy ma'lumot bo'lmasa ham savolga qisman javob bera olasizmi?</p>",
             ph="Ma'lumot: ... (bor / so'raladi) ; Asosiy usul: ..., zaxira: ... ; Xavflar: 1) ... 2) ... 3) ..."),
        dict(t="2 sahifalik yo'nalish bayoni", short="Bayon", min=40, kind="📝 Hujjat", ic="memo",
             hook="Mavzuni boshqa odam bir daqiqada tushunmasa, uni qayta tuzish kerak. Bayon M3 da ilmiy rahbarga yozishdan oldingi asosiy hujjat.",
             body=f"""<h4>Bayon tarkibi</h4>
<ol><li>Muammo va ahamiyati.</li><li>4–6 ta asosiy maqola.</li><li>Bo'shliq.</li><li>Tadqiqot savoli.</li><li>Usul eskizi.</li><li>Kutilgan hissa.</li><li>Bajarilishi mumkinlik va xavf.</li><li>Ilmiy rahbar bilan moslik ([[supervisor fit]]).</li></ol>
<p>Bu ariza matni emas, fikringizni tartibga soluvchi ishchi hujjat. Qoralamada “nima o'rganaman” ko'p, “qanday isbotlayman” kam bo'lsa, usul va dalil qismini kuchaytiring.</p>
<div class="box warn">Sun'iy intellekt yozgan “original” matnni manbalarini tekshirmasdan o'zingizniki deb yubormang.</div>
<div class="srcs">Manba: {KCL}; {UKRIO}. {HOL}.</div>""",
             take="Yaxshi bayon 90 soniyada aytib beriladi va “qanday isbotlayman” savoliga javob beradi.",
             task="<ul><li>2 sahifalik bayon qoralamasini yozing.</li><li>Uni 90 soniyada og'zaki aytib ko'ring.</li><li>Fikr olgandan keyin ikkinchi versiyani yozing.</li></ul><p><b>O'zingizga savol:</b> birinchi katta natija qanday isbotlanadi?</p>",
             ph="Muammo: ... Bo'shliq: ... Savol: ... Usul: ... Hissa: ... Xavf: ..."),
    ],
    tool=dict(id="kanvas", short="Kanvas", h2="Tadqiqot yo'nalishi kanvasi", sub="Savol, bo'shliq, dalil, usul va bajarilishi mumkinlikni bir kartaga yig'ing.",
              h3="Yo'nalish kanvasi", tag="6 maydon", ic="telescope", btn="Kanvasni saqlash", badge="Yo'nalish", min=5,
              fields=[dict(k="savol", label="Asosiy tadqiqot savoli", type="area", ph="...?"),
                      dict(k="boshliq", label="Bo'shliq", hint="turi va 2 manba", type="area", ph="Usul bo'shlig'i: ... (manba 1, manba 2)"),
                      dict(k="dalil", label="Asosiy maqolalar", hint="4–6 ta, DOI bilan", type="area", ph="1) ... 2) ..."),
                      dict(k="usul", label="Usul va zaxira usul", type="area", ph="Asosiy: ... ; zaxira: ..."),
                      dict(k="resurs", label="Ma'lumot va resurslar", type="area", ph="Ma'lumot: ...; uskuna: ...; etika: ..."),
                      dict(k="holat", label="Savol holati", type="select", opts=["Tekshirishga tayyor", "Yana toraytirish kerak", "Ma'lumot masalasi hal bo'lmagan"])]),
    check=dict(h2="M1 nazorati", sub="Bayonni yakunlashdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Tadqiqot savolida noaniq ibora yo'q.", "Adabiyot dalillari DOI yoki havola bilan yozilgan.", "Bo'shliq va hissa alohida ko'rsatilgan.",
                      "Ma'lumot va usulga kirish rejasi bor.", "Etika va xavflar ochiq yozilgan.", "Namuna va sun'iy intellekt matni o'zimniki deb ko'chirilmagan.",
                      "Bayonni 90 soniyada aytib bera olaman."]),
    art_title="Tadqiqot yo'nalishi bayoni", art_short="Bayon",
    art=[("Tadqiqot savoli", ["savol", "a1"]), ("Adabiyot", ["dalil", "a2"]), ("Bo'shliq", ["boshliq", "a3"]), ("Maqsad va vazifalar", ["a4"]),
         ("Usul va resurslar", ["usul", "resurs", "a5"]), ("Bayon qoralamasi", ["a6"]), ("Holat", ["holat"])],
    tip="Savolingizni do'stingizga 90 soniyada tushuntiring. U “qanday isbotlaysan?” deb so'rasa va javob bera olmasangiz, usul qismiga qayting.",
    sources=f"{KCL}; {UKRIO}; {DORA}. {STD}",
)
