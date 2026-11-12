from common import KCL, UKRIO, DORA, HOL, STD

MOD = dict(
    title="Ilmiy yo'nalish va tadqiqot savoli",
    desc="PhD Lab M1: qiziqishdan aniq tadqiqot savoliga o'tish. Adabiyot qidirish, tadqiqot bo'shlig'ini manba bilan ko'rsatish, maqsad va vazifalar, ma'lumot va resurslarni tekshirish. Natija: ikki betlik yo'nalish bayoni.",
    lead="“Geotermal energiya”, “sun'iy intellekt” yoki “ta'lim” deb yozsangiz, soha aniq bo'ladi, lekin savol hali yo'q. Bu modulda qiziqishingizdan <b>dalil bilan javob topsa bo'ladigan savol</b> chiqarasiz va uni ikki betlik bayonga yozasiz. Uni o'qigan odam bir daqiqada nima qilmoqchi ekaningizni tushunishi kerak.",
    hero="telescope", weeks="2–3", next="M2 Doktorantura tizimlari va universitet tanlash", next_href="phd-lab-o.html?m=2",
    goals=[("telescope", "Bitta asosiy tadqiqot savoli", "nima, qayerda, qaysi davrda va natija nimada ko'rinishi yozilgan"),
           ("books", "12 manbali adabiyot jadvali", "har birida DOI yoki havola, usul, natija va cheklov"),
           ("memo", "Ikki betlik yo'nalish bayoni", "M3 da ilmiy rahbarga yozishdan oldin kerak bo'ladi")],
    warn="Bu modul ilmiy uslubni to'liq o'rgatmaydi: tizimli adabiyot sharhi (systematic review) va chuqur statistika bu yerda yo'q. Bu yerda PhD arizasi uchun savol va qisqa bayon tayyorlanadi. Namunalar Kompas tuzgan o'quv misollari; faktlarni o'z sohangiz manbalaridan oling.",
    lessons=[
        dict(t="Qiziqishdan savolga", short="Savol", min=25, kind="🎯 Toraytirish", ic="telescope",
             hook="Professor va qabul komissiyasi sizdan <b>javobini izlab topsa bo'ladigan savol</b> kutadi. Mavzu keng bo'lsa, qaysi ma'lumotni yig'ish va qaysi usulni tanlash ham noaniq qoladi.",
             body=f"""<h4>Savolni to'rt jihatdan toraytiring</h4>
<ul><li><b>Nima</b> o'rganiladi: hodisa yoki jarayon.</li><li><b>Qayerda yoki kimda</b>: hudud, obyekt yoki odamlar guruhi.</li><li><b>Nima noma'lum</b>: hozirgi ishlar javob bermagan joy.</li><li><b>Javob nimada ko'rinadi</b>: o'lchanadigan natija.</li></ul>
<p>Sohani tanlashda faqat ommabop yo'nalishga qaramang. <b>Oldingi bilimingiz</b> va laboratoriyada haqiqatan bor uskuna ko'proq hal qiladi. Savol bir nechta muammoni qamrab olsa, uni bitta asosiy va bir-ikkita yordamchi savolga ajrating.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Keng: <i>“Sun'iy intellekt va iqlim”</i>. Aniqroq: <i>“Shahar ostidagi yer haroratining yillar davomida o'zgarishini qaysi kuzatuvlar ishonchli ko'rsata oladi?”</i> Bu savolni ham ma'lumot borligini tekshirmaguncha taklif sifatida yozmang.</div>
<div class="box warn">Savolni <i>“bu ishni hali hech kim qilmagan”</i> degan da'voga qurmang: buni tekshirish qiyin va ko'pincha noto'g'ri chiqadi.</div>""",
             take="Savolda to'rt narsa bo'lsin: nima o'rganiladi, qayerda, nima noma'lum va javob nimada ko'rinadi.",
             task="<ul><li>Qiziqishingizni bitta jumlada yozing.</li><li>Uni hodisa, hudud yoki guruh va vaqt bo'yicha toraytiring.</li><li>Bitta asosiy savol yozing.</li></ul><p><b>O'zingizga savol:</b> bu savolga qanday ma'lumot javob beradi?</p>",
             ph="Qiziqish: ... → Nima: ..., qayerda: ..., qaysi davr: ... → Savol: ...?"),
        dict(t="Adabiyot qidirish", short="Adabiyot", min=35, kind="🔎 Qidiruv", ic="books",
             hook="PhD g'oyasi ilmiy maqolalarni tartibli o'qishdan boshlanadi. <i>“Ko'p maqola o'qidim”</i> degan gap komissiyaga hech narsa aytmaydi: qaysi maqolalarni o'qib, ulardan nimani olganingizni ko'rsatish kerak.",
             body=f"""<h4>Qanday qidiriladi</h4>
<ul><li><b>Kalit so'zlar va sinonimlar</b>, mantiqiy operatorlar bilan ([[AND]], [[OR]], [[NOT]]).</li><li><b>Iqtibos zanjiri</b> ([[citation chaining]]): maqola qaysi ishlarga tayangan va keyin uni kimlar keltirgan.</li><li><b>Klassik va yangi ishlar</b>: soha asosini qo'ygan maqolalar va so'nggi besh yildagi ishlar.</li></ul>
<h4>Qidiruv daftari</h4>
<p>Har qidiruvdan keyin yozib qo'ying: qaysi baza, qanday so'rov, qaysi sana, qanday filtr va nechta maqola topildi. Bir oydan keyin qidiruvni takrorlash yoki kengaytirish uchun shu yozuv kerak bo'ladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> 12 maqolalik jadval ustunlari: muallif, yil, savol, ma'lumot, usul, natija, cheklov va <i>sizning savolingizga qanday aloqasi bor</i>.</div>
<div class="box warn">Soxta (yirtqich) jurnallardan ([[predatory journals]]) ehtiyot bo'ling. Iqtiboslar soni maqola sifatini <b>yolg'iz o'zi</b> ko'rsatmaydi (DORA tavsiyasi). Faqat annotatsiyani o'qib xulosa chiqarmang: usul va cheklovlar bo'limini ham o'qing.</div>
<div class="srcs">Manba: {DORA}. {HOL}.</div>""",
             take="Har qidiruv daftarga yoziladi: baza, so'rov, sana va filtr. Natijada 12 manbali jadval bo'ladi.",
             quiz=[("Iqtiboslar soni ko'p bo'lsa, maqola albatta sifatli.", "n", "Noto'g'ri: DORA iqtiboslar sonini sifatning yagona o'lchovi qilmaslikni tavsiya qiladi."),
                   ("Qidiruv daftariga baza, so'rov, sana va filtr yoziladi.", "t", "To'g'ri: shunda qidiruvni boshqa odam ham takrorlay oladi."),
                   ("Biror hududda birinchi marta o'rganilgani ishni avtomatik ravishda muhim qiladi.", "n", "Noto'g'ri: yangi hudud o'zi ilmiy hissa bo'lmaydi; bo'shliqni manbalar bilan ko'rsatish kerak."),
                   ("Gipoteza har bir ilmiy sohada majburiy emas.", "t", "To'g'ri: masalan, ko'p sifat tadqiqotlarida gipoteza qo'yilmaydi.")],
             task="<ul><li>Sinonim va operatorlar bilan 3 ta qidiruv so'rovi yozing.</li><li>DOI yoki havolasi bilan 12 ta muhim manba to'plang.</li><li>Har manbaning bitta cheklovini yozing.</li></ul><p><b>O'zingizga savol:</b> so'nggi besh yildagi ishlar va klassik maqolalar ro'yxatda alohida ko'rinadimi?</p>",
             ph="So'rov 1: ... ; So'rov 2: ... ; 1) Muallif, yil, DOI: usul ..., cheklov ..."),
        dict(t="Tadqiqot bo'shlig'ini ko'rsatish", short="Bo'shliq", min=30, kind="🧩 Dalil", ic="miya",
             hook="<i>“Bu mavzuda hali ish yo'q”</i> degan gap ko'pincha noto'g'ri chiqadi. Bo'shliqni aniq yozib, manbalar bilan cheklash kerak: qaysi ishlar nimani qilgan va nima ochiq qolgan.",
             body=f"""<h4>Bo'shliq turlari</h4>
<div class="tbl"><table><thead><tr><th>Tur</th><th>Nimani bildiradi</th></tr></thead><tbody>
<tr><td>Ma'lumot bo'shlig'i</td><td>Kerakli kuzatuv yoki o'lchov yo'q</td></tr>
<tr><td>Usul bo'shlig'i</td><td>Mavjud usullar muayyan sharoitda ishlamaydi</td></tr>
<tr><td>Tekshiruv bo'shlig'i</td><td>Natija boshqa, mustaqil ma'lumotda sinab ko'rilmagan</td></tr>
<tr><td>Kontekst bo'shlig'i</td><td>Boshqa hudud yoki guruhda o'rganilmagan</td></tr>
<tr><td>Nazariya bo'shlig'i</td><td>Kuzatuvni izohlovchi qarashlar bir-biriga zid</td></tr>
</tbody></table></div>
<p><i>“Mavjud usullar X sharoitda ishlamaydi”</i> degan fikr uchun <b>kamida ikki-uch manba</b> kerak. Yangi ma'lumotlar to'plamining o'zi ham har doim katta ilmiy hissa bo'lavermaydi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Zaif: <i>“O'zbekistonda bu haqda maqola kam.”</i> Aniqroq: <i>“Ko'rib chiqilgan 6 ta ishda datchiklar X chuqurlikdan pastga tushmagan, shuning uchun Y savoli ochiq qolmoqda.”</i> Bu fikrlash namunasi, real fakt emas.</div>
<div class="box warn">Biror hududda birinchi bo'lishning o'zi ishga ilmiy ahamiyat bermaydi.</div>""",
             take="Bo'shliqning turi aytilgan va kamida ikkita manba bilan cheklangan bo'lsa, unga ishonish mumkin.",
             task="<ul><li>3 ta bo'shliq taxminini yozing.</li><li>Har biriga 2 tadan manba biriktiring.</li><li>Eng oson tekshiriladiganini tanlang.</li></ul><p><b>O'zingizga savol:</b> bo'shliq haqidagi fikringizni qaysi ikki ish bilan cheklay olasiz?</p>",
             ph="Bo'shliq 1 (usul): ... ; manbalar: ..., ... ; Tanlov: ..."),
        dict(t="Savol, maqsad, vazifa va gipoteza", short="Maqsad", min=25, kind="🧭 Tuzilma", ic="compass",
             hook="Tadqiqot savoli, maqsad, vazifalar va gipoteza har xil narsalar. Ularni aralashtirib yuborsangiz, usul ham noaniq bo'lib qoladi.",
             body=f"""<ul><li><b>Maqsad</b> ([[aim]]): ish oxirida nimaga erishmoqchisiz, bir jumlada.</li><li><b>Vazifalar</b> ([[objectives]]): maqsadga olib boradigan va natijasini tekshirsa bo'ladigan qadamlar.</li><li><b>Gipoteza</b> ([[hypothesis]]): tajriba rad etishi mumkin bo'lgan aniq taxmin. Har sohada shart emas.</li></ul>
<p>Usul vazifalarga mos bo'lsin: savol sabab haqida bo'lsa, faqat korrelyatsiya yetarli dalil bo'lmaydi. Ishning muvaffaqiyatini <i>kutgan natija chiqdimi-yo'qmi</i> degan savolga bog'lab qo'ymang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Maqsad: kuzatuv usuli qaysi sharoitda ishlashini aniqlash. 1-vazifa: sun'iy (sintetik) ma'lumotda sinash. 2-vazifa: dala ma'lumotida tekshirish. Gipoteza: muayyan sharoitda usulning sezgirligi oshadi.</div>
<div class="box warn"><i>“O'rganish”</i> yoki <i>“tadqiq qilish”</i> kabi umumiy vazifalarga natija mezonini qo'shing: vazifa qachon bajarilgan hisoblanadi?</div>""",
             take="Bitta maqsad, 2–3 ta vazifa, har birining natijasi o'lchanadi. Gipoteza faqat uni rad etsa bo'ladigan holda qo'yiladi.",
             task="<ul><li>Bitta maqsad yozing.</li><li>3 ta vazifa belgilang.</li><li>Kerak bo'lsa, rad etsa bo'ladigan bitta gipoteza yozing.</li></ul><p><b>O'zingizga savol:</b> har vazifa uchun ma'lumot va o'lchov ko'rsatkichi bormi?</p>",
             ph="Maqsad: ... ; 1) ... (ko'rsatkich: ...) 2) ... 3) ... ; Gipoteza: ..."),
        dict(t="Reja amalga oshadimi", short="Resurs", min=25, kind="🛠 Tekshiruv", ic="hourglass",
             hook="Juda yaxshi savol ham ma'lumot yoki uskuna bo'lmasa, 3–4 yilga sig'maydi. Buni ariza topshirishdan oldin aniqlab olgan ma'qul.",
             body=f"""<h4>Nimalarni tekshirish kerak</h4>
<p>Ma'lumotga kirish, uskuna, xarajat, ruxsatnomalar, hisoblash quvvati, etika talablari, rahbarning shu mavzudagi tajribasi va vaqt.</p>
<p>Ikki reja yozing: <b>ideal</b> reja va hamma narsa bo'lmaganda ham bajariladigan <b>minimal</b> reja. Boshqa guruhning ma'lumotini ishlatishga yozma ruxsat bo'lmasa, uni bor deb hisoblamang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Xavfli: <i>“Menga korxonaning yopiq ma'lumoti kerak.”</i> Xavfsizroq: <i>“Usulni avval ochiq ma'lumotda sinayman, ruxsat olinsa, dala ma'lumoti bilan kengaytiraman.”</i></div>
<div class="box warn">Yopiq ma'lumot, etika ruxsati yoki kuchli GPU o'z-o'zidan topiladi deb o'ylamang.</div>""",
             take="Har resurs yoniga yozing: bor, so'raladi yoki yo'q. Asosiy va zaxira usul bo'lsa, reja ishlaydi.",
             task="<ul><li>Ma'lumotga kirish jadvalini tuzing.</li><li>Asosiy va zaxira usulni belgilang.</li><li>3 ta katta xavfni yozing.</li></ul><p><b>O'zingizga savol:</b> asosiy ma'lumot bo'lmasa ham savolga qisman javob bera olasizmi?</p>",
             ph="Ma'lumot: ... (bor / so'raladi) ; Asosiy usul: ..., zaxira: ... ; Xavflar: 1) ... 2) ... 3) ..."),
        dict(t="Ikki betlik yo'nalish bayoni", short="Bayon", min=40, kind="📝 Hujjat", ic="memo",
             hook="Mavzuingizni boshqa odam bir daqiqada tushunmasa, matnni qayta tuzish kerak. Bu bayon M3 da ilmiy rahbarga xat yozishdan oldin tayyor bo'lishi kerak.",
             body=f"""<h4>Bayonda nima bo'ladi</h4>
<ol><li>Muammo va uning ahamiyati.</li><li>Tayanch 4–6 maqola.</li><li>Bo'shliq.</li><li>Tadqiqot savoli.</li><li>Usulning qisqa tavsifi.</li><li>Kutilgan hissa.</li><li>Xavflar va ular bilan nima qilinadi.</li><li>Ilmiy rahbar bilan moslik ([[supervisor fit]]).</li></ol>
<p>Bu hujjat arizaga yuborilmasligi ham mumkin: u fikringizni tartibga solish uchun kerak. Qoralamada <i>“nimani o'rganaman”</i> ko'p, <i>“qanday isbotlayman”</i> kam bo'lsa, usul va dalil qismini kuchaytiring.</p>
<div class="box warn">Sun'iy intellekt yozgan matnni manbalarini tekshirmasdan o'zingizniki qilib yubormang.</div>
<div class="srcs">Manba: {KCL}; {UKRIO}. {HOL}.</div>""",
             take="Yaxshi bayonni 90 soniyada og'zaki aytib berish mumkin va unda “qanday isbotlayman” savoliga javob bor.",
             task="<ul><li>Ikki betlik bayon qoralamasini yozing.</li><li>Uni 90 soniyada og'zaki aytib ko'ring.</li><li>Fikr-mulohaza olgach, ikkinchi versiyani yozing.</li></ul><p><b>O'zingizga savol:</b> birinchi katta natijani qanday isbotlaysiz?</p>",
             ph="Muammo: ... Bo'shliq: ... Savol: ... Usul: ... Hissa: ... Xavf: ..."),
    ],
    tool=dict(id="karta", short="Karta", h2="Tadqiqot yo'nalishi kartasi", sub="Savol, bo'shliq, manbalar, usul va resurslarni bitta kartaga yozing.",
              h3="Yo'nalish kartasi", tag="6 maydon", ic="telescope", btn="Kartani saqlash", badge="Yo'nalish", min=5,
              fields=[dict(k="savol", label="Asosiy tadqiqot savoli", type="area", ph="...?"),
                      dict(k="boshliq", label="Bo'shliq", hint="turi va 2 ta manba", type="area", ph="Usul bo'shlig'i: ... (manba 1, manba 2)"),
                      dict(k="dalil", label="Tayanch maqolalar", hint="4–6 ta, DOI bilan", type="area", ph="1) ... 2) ..."),
                      dict(k="usul", label="Usul va zaxira usul", type="area", ph="Asosiy: ... ; zaxira: ..."),
                      dict(k="resurs", label="Ma'lumot va resurslar", type="area", ph="Ma'lumot: ...; uskuna: ...; etika: ..."),
                      dict(k="holat", label="Savol holati", type="select", opts=["Tekshirishga tayyor", "Yana toraytirish kerak", "Ma'lumot masalasi hal bo'lmagan"])]),
    check=dict(h2="M1 nazorati", sub="Bayonni yakunlashdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Savolda noaniq so'z qolmagan.", "Manbalar DOI yoki havola bilan yozilgan.", "Bo'shliq va kutilgan hissa alohida yozilgan.",
                      "Ma'lumot va usulga qanday kirishim yozilgan.", "Etika va xavflar ochiq yozilgan.", "Namuna yoki sun'iy intellekt matnini o'zimniki qilib ko'chirmaganman.",
                      "Bayonni 90 soniyada aytib bera olaman."]),
    art_title="Tadqiqot yo'nalishi bayoni", art_short="Bayon",
    art=[("Tadqiqot savoli", ["savol", "a1"]), ("Adabiyot", ["dalil", "a2"]), ("Bo'shliq", ["boshliq", "a3"]), ("Maqsad va vazifalar", ["a4"]),
         ("Usul va resurslar", ["usul", "resurs", "a5"]), ("Bayon qoralamasi", ["a6"]), ("Holat", ["holat"])],
    tip="Savolingizni do'stingizga 90 soniyada tushuntirib ko'ring. U <i>“qanday isbotlaysan?”</i> deb so'rasa-yu, javob topolmasangiz, usul qismiga qayting.",
    sources=f"{KCL}; {UKRIO}; {DORA}. {STD}",
)
