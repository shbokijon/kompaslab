from common import CSS, CSS_INT, NORTHWESTERN, HARVARD, DARTMOUTH, HOL, STD

MOD = dict(
    title="Moliyaviy yordam arizasi",
    desc="USA Lab M4: CSS Profile va universitet formalari, O'zbekistondan oila daromadini hujjatlash, valyuta va tarjima, to'lovdan ozod qilish, yordam xatini o'qish va qayta ko'rib chiqishni so'rash. Natija: moliyaviy yordam arizasi paketi.",
    lead="Ehtiyojga asoslangan yordam oila haqidagi raqamlarga qarab hisoblanadi. Bu modulda qaysi universitet qaysi formani so'rashini aniqlaysiz, O'zbekistondagi daromadni AQSh universiteti tushunadigan hujjatlarga aylantirasiz va kelgan yordam xatini to'g'ri o'qiysiz.",
    hero="scroll", weeks="2", next="M5 Global UGRAD va almashinuv dasturlari", next_href="usa-lab-o.html?m=5",
    goals=[("scroll", "Yordam arizasi paketi", "har universitet: forma, hujjat, muddat"),
           ("money", "Oila moliyaviy varaqasi", "daromad, jamg'arma, mulk; dollarda, kurs bilan"),
           ("shield", "Yordam xatini o'qish usuli", "grant, kredit, ish va qolgan summa")],
    warn=f"Kompas Lab oila hujjatlarini to'ldirib bermaydi va yuridik yoki soliq maslahati bermaydi. Har qanday raqam oila hujjatiga mos bo'lishi shart: noto'g'ri ma'lumot yordamni bekor qilishiga olib kelishi mumkin. Forma va to'lovlar {HOL}; universitet sahifasidan qayta tekshiring.",
    lessons=[
        dict(t="Formalar xaritasi", short="Formalar", min=25, kind="🗺 Xarita", ic="memo",
             hook="Har universitet o'z hujjatlar ro'yxatini so'raydi. Bir universitetga yuborgan hujjatingiz boshqasiga yetarli bo'lmasligi mumkin, muddat esa ko'pincha qabul arizasi bilan bir vaqtda.",
             body=f"""<h4>CSS Profile</h4>
<p>College Board ning [[CSS Profile]] tizimi: kollejlar va stipendiya dasturlari uni federal bo'lmagan, universitetning o'z yordamini taqsimlash uchun ishlatadi. Uning sahifasida xalqaro abituriyentlar uchun alohida bo'lim bor: valyuta, ikki valyutadagi daromad, ota-ona soliq holati va AQSh soliq deklaratsiyasini topshirmaydigan oilalar uchun IDOC ga nima yuborish haqida savollar.</p>
<h4>Universitet formasi va qo'shimcha hujjatlar (Northwestern namunasi)</h4>
<ul><li>CSS Profile; uni o'z mamlakatingizdan topshira olmasangiz yoki jiddiy moliyaviy qiyinchilik bo'lsa, universitetning o'z formasi (ISAFA).</li><li>Ota-onaning so'nggi yil soliq hujjati yoki, mamlakatda yillik soliq deklaratsiyasi bo'lmasa, ish beruvchidan rasmiy imzo yoki muhr bilan daromad haqida xat.</li><li>Har hujjatda talabaning ismi va tug'ilgan sanasi, to'ldirilgan muqova varaq.</li><li>Barcha soliq va daromad hujjatlari rasmiy tarjima bilan va AQSh dollariga o'girilgan holda, kurs ko'rsatilib.</li></ul>
<div class="tbl"><table><thead><tr><th>Universitet</th><th>Forma</th><th>Qo'shimcha hujjat</th><th>Muddat</th></tr></thead><tbody>
<tr><td>...</td><td>CSS Profile / o'z formasi</td><td>Soliq yoki daromad xati, tarjima</td><td>Rasmiy sahifadan</td></tr>
</tbody></table></div>
<div class="box info">Har universitetning [[international applicants]] yoki [[how to apply for aid]] sahifasini oching. Bu jadval siz uchun Asosiy nazorat jadvalining (Master Tracker) moliya qismi.</div>
<div class="srcs">Manba: {CSS}; {CSS_INT}; {NORTHWESTERN}. {HOL}.</div>""",
             take="CSS Profile ko'p universitetlarda asosiy forma; ba'zilari o'z formasini va daromad hujjatlarini rasmiy tarjima va dollar kursi bilan so'raydi. Har universitet uchun alohida qator.",
             task="<ul><li>Ro'yxatingizdagi yordam so'raladigan har universitet uchun jadval qatorini to'ldiring: forma, qo'shimcha hujjat, muddat, havola.</li></ul>",
             ph="... — CSS Profile + daromad xati (tarjima, USD), muddat ...; havola ..."),
        dict(t="O'zbekistondan oila daromadini hujjatlash", short="Daromad", min=35, kind="📑 Hujjat", ic="scroll",
             hook="AQSh universiteti O'zbekistondagi daromad qanday shakllanishini bilmaydi. U faqat sizning hujjat va izohingizni ko'radi. Aniq, izchil va tekshiriladigan hujjat yordam olishning asosi.",
             body="""<h4>Oila moliyaviy varaqasi</h4>
<div class="tbl"><table><thead><tr><th>Qator</th><th>Nima yoziladi</th><th>Qanday hujjat</th></tr></thead><tbody>
<tr><td>Rasmiy daromad</td><td>Har ishlaydigan ota-ona, yillik</td><td>Ish beruvchi xati (imzo, muhr) yoki soliq ma'lumotnomasi</td></tr>
<tr><td>Tadbirkorlik daromadi</td><td>YATT yoki korxona, yillik foyda</td><td>Soliq hisoboti</td></tr>
<tr><td>Jamg'arma</td><td>Bank hisoblari, omonatlar</td><td>Bank ko'chirmasi</td></tr>
<tr><td>Mulk</td><td>Uy, yer, mashina, chorva: formaga qanday yozilishini ko'rsatmadan o'qing</td><td>Ko'rsatmaga qarab</td></tr>
<tr><td>Majburiy xarajatlar</td><td>Boshqa farzandlarning o'qishi, kasallik, qarz to'lovi</td><td>Izohli varaq</td></tr>
</tbody></table></div>
<h4>Uch qoida</h4>
<ol><li><b>Bir kurs, bir sana.</b> Barcha so'mdagi summalarni bitta sanadagi rasmiy kurs bilan dollarga o'giring va kurs va sanani yozing.</li><li><b>Izchillik.</b> CSS Profile, universitet formasi va hujjatlardagi raqamlar bir xil bo'lishi kerak.</li><li><b>Halollik.</b> Norasmiy yoki mavsumiy daromad bo'lsa, uni yashirmang va o'ylab topmang; formaning qo'shimcha izoh qismida qisqa tushuntiring.</li></ol>
<div class="box warn">Daromadni kamaytirib ko'rsatish yoki mulkni yashirish firibgarlik hisoblanishi mumkin. Universitet qo'shimcha hujjat so'rab tekshiradi; nomuvofiqlik yordamni va qabulni xavf ostiga qo'yadi.</div>
<div class="box info">O'zbekistonda olinadigan rasmiy ma'lumotnomalar ro'yxatini davlat xizmatlari portalidan (my.gov.uz) tekshiring. Kompas qaysi ma'lumotnoma qabul qilinishini universitet o'rniga hal qilmaydi: universitetdan yozma so'rang.</div>""",
             take="Har daromad turi uchun rasmiy hujjat, bitta sana va kurs, barcha formalarda bir xil raqam. Norasmiy daromad halol izoh bilan.",
             quiz=[("So'mdagi summalarni dollarga o'girganda kurs va sanani yozish kerak.", "t", "To'g'ri: Northwestern kursni ko'rsatishni talab qiladi."),
                   ("Turli formalarda turli raqam yozish muammo emas.", "n", "Noto'g'ri: nomuvofiqlik yordamni xavf ostiga qo'yadi."),
                   ("Norasmiy daromadni umuman yozmaslik eng xavfsiz yo'l.", "n", "Noto'g'ri: halol izoh bilan ko'rsatiladi."),
                   ("Qaysi ma'lumotnoma qabul qilinishini universitetdan yozma so'rash mumkin.", "t", "To'g'ri.")],
             task="<ul><li>Oila moliyaviy varaqasini 5 qator bo'yicha to'ldiring (raqamlarni oila bilan birga).</li><li>Kurs va sanani yozing.</li></ul>",
             ph="Rasmiy daromad: ... so'm = ... USD; tadbirkorlik: ...; jamg'arma: ...; mulk: ...; xarajatlar: ...; kurs: ... (sana ...)"),
        dict(t="Yordam formasi to'lovi va ozod qilish", short="To'lov", min=20, kind="💳 To'lov", ic="money",
             hook="Yordam so'rashning ham narxi bor. Bir nechta universitet uchun forma to'lovi kichik oila byudjetida sezilarli bo'lishi mumkin.",
             body=f"""<h4>CSS Profile to'lovi</h4>
<p>CSS Profile sahifasida aytilishicha, yillik daromadi 100 000 dollargacha bo'lgan oilalar uchun forma to'lovdan ozod qilish orqali bepul. Lekin xalqaro talabaga bu qoida qo'llanishi universitetga qarab farq qiladi: masalan, Northwestern xalqaro talabalar CSS Profile to'lovidan ozod bo'la olmasligini yozadi.</p>
<h4>Nima qilish kerak</h4>
<ol><li>Har universitet sahifasida [[fee waiver]] bandini qidiring.</li><li>Yozilmagan bo'lsa, moliyaviy yordam bo'limiga yozma so'rang.</li><li>To'lovlarni byudjet jadvaliga qo'shing (M2).</li></ol>
<div class="box info">Qabul arizasi to'lovi (Common App yig'imi va undan ozod qilish) Bachelor Lab M13 da. Bu dars faqat moliyaviy yordam formasi to'lovi haqida.</div>
<div class="srcs">Manba: {CSS}; {NORTHWESTERN}. {HOL}.</div>""",
             take="CSS Profile to'lovidan ozod qilish xalqaro talabaga hamma joyda qo'llanmaydi. Har universitetdan aniqlang va to'lovlarni byudjetga qo'shing.",
             task="<ul><li>Yordam so'raladigan har universitet uchun: forma to'lovi bormi, ozod qilish mumkinmi, dalil.</li></ul>",
             ph="... — CSS to'lovi: bor, ozod qilish: xalqaro talabaga yo'q (havola ...)"),
        dict(t="Yordam xatini o'qish", short="Xat", min=30, kind="🔍 Tahlil", ic="bulb",
             hook="\"Sizga 40 000 dollar yordam\" degan xat quvonarli. Lekin uning qancha qismi grant, qancha qismi qaytariladigan kredit yoki ish va sizga qancha to'lash qolishini hisoblamaguningizcha qaror qilmang.",
             body=f"""<h4>Xatning qismlari</h4>
<div class="tbl"><table><thead><tr><th>Qism</th><th>Qaytariladimi</th><th>Izoh</th></tr></thead><tbody>
<tr><td>Grant yoki stipendiya</td><td>Yo'q</td><td>Asosiy qism</td></tr>
<tr><td>Kredit</td><td>Ha</td><td>Taklif qilinsa, kafil talabi, foizi va qaytarish shartini o'qing</td></tr>
<tr><td>Ish ([[student employment]])</td><td>Yo'q, lekin ishlab topiladi</td><td>Kampusda, soat cheklangan (M8)</td></tr>
<tr><td>Oila hissasi</td><td>—</td><td>Universitet hisoblagan oila to'lovi</td></tr>
</tbody></table></div>
<h4>Hisob</h4>
<p>Qolgan summa = to'liq narx − grant − kredit − ish. Siz va oila uchun haqiqiy summa: qolgan summa + kredit (keyin qaytariladi).</p>
<p>Harvard ham talabalardan o'z ish haqi va jamg'armasidan hissa kutishini yozadi: \"ota-ona hissasi nol\" talaba hech narsa to'lamaydi degani emas.</p>
<h4>Har yil uchun</h4>
<ul><li>Yordam keyingi yillarda qayta hisoblanadimi, har yili ariza kerakmi: xatda yoki sahifada.</li><li>Natijaga asoslangan grant bo'lsa, baho sharti.</li></ul>
<div class="srcs">Manba: {HARVARD}. {HOL}.</div>""",
             take="Yordam xatini grant, kredit, ish va oila hissasiga ajrating. Qolgan summa va kredit birga sizning haqiqiy narxingiz.",
             task="<ul><li>Namuna yordam xati uchun (yoki universitet saytidagi namuna) qolgan summani hisoblang.</li><li>Keyingi yillar sharti nima ekanini yozing.</li></ul>",
             ph="Narx ... − grant ... − kredit ... − ish ... = qolgan ...; haqiqiy narx ...; keyingi yillar: ..."),
        dict(t="Qayta ko'rib chiqish va o'zgargan holat", short="Qayta", min=20, kind="✉️ Xat", ic="bell",
             hook="Yordam xati ba'zan oilaning hozirgi holatini to'liq aks ettirmaydi. Holat haqiqatan o'zgargan bo'lsa, xushmuomala va hujjatli so'rov qilish mumkin.",
             body=f"""<h4>Qachon so'rash o'rinli</h4>
<ul><li>Arizadan keyin oila daromadi kamaygan (ish yo'qotish, kasallik, nafaqa).</li><li>Formada ko'rinmagan majburiy xarajat bor.</li><li>Hisobda xato bor (masalan, kurs noto'g'ri olingan).</li></ul>
<h4>Qanday</h4>
<ol><li>Universitet sahifasida [[appeal]], [[review]] yoki [[special circumstances]] bandini toping.</li><li>Qisqa xat: nima o'zgargan, qachon, raqam bilan, hujjat ilova.</li><li>Boshqa universitet takliflarini ko'rsatish mumkinmi, sahifadan tekshiring; hamma universitet buni qabul qilmaydi.</li></ol>
<div class="box warn">Qayta ko'rib chiqish so'rovi savdolashish emas. Hujjatsiz yoki o'ylab topilgan holat yordamni yo'qotishga olib kelishi mumkin.</div>
<div class="box info">Dartmouth kabi universitetlarda xalqaro talabalar uchun alohida yordam yo'li sahifasi bor: savolni o'sha sahifadagi manzilga yuboring.</div>
<div class="srcs">Manba: {DARTMOUTH}. {HOL}.</div>""",
             take="Haqiqiy o'zgarish yoki xato bo'lsa, universitet tartibi bo'yicha hujjatli va qisqa so'rov qiling. Savdolashish emas.",
             task="<ul><li>Bitta universitetning qayta ko'rib chiqish tartibini toping va havola bilan yozing.</li><li>Holatingizga mos 3 jumlalik so'rov rejasini yozing (o'zingiz).</li></ul>",
             ph="... universiteti tartibi: ... (havola). Reja: 1) nima o'zgardi ... 2) raqam ... 3) hujjat ..."),
    ],
    tool=dict(id="paket", short="Paket", h2="Moliyaviy yordam arizasi paketi", sub="Har universitet uchun forma, hujjat va muddat; oila varaqasi va kurs; yordam xati hisobi.",
              h3="Ariza paketi", tag="5 maydon", ic="scroll", btn="Paketni saqlash", badge="Hujjat ustasi", min=4,
              fields=[dict(k="forma", label="Formalar jadvali", hint="universitet — forma — hujjat — muddat", type="area", ph="... — CSS Profile + daromad xati, ...; ..."),
                      dict(k="oila", label="Oila moliyaviy varaqasi", hint="dollarda, kurs va sana bilan", type="area", ph="Daromad ..., jamg'arma ..., mulk ..., xarajat ...; kurs ... (sana)"),
                      dict(k="izoh", label="Qo'shimcha izoh rejasi", hint="norasmiy daromad, maxsus holatlar; o'zingiz yozasiz", type="area", ph="..."),
                      dict(k="tolov", label="Forma to'lovlari", type="area", ph="... — ... USD, ozod qilish: ..."),
                      dict(k="muddat", label="Eng yaqin moliyaviy yordam muddati", type="date")]),
    check=dict(h2="M4 nazorati", sub="Paketni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har universitet uchun forma va muddat rasmiy sahifadan.", "Barcha summalar dollarda, bitta kurs va sana bilan.",
                      "Barcha formalarda raqamlar bir xil.", "Har daromad turi uchun hujjat bor yoki so'ralgan.", "Tarjima talablari aniqlangan.",
                      "Norasmiy daromad halol izohlangan.", "Forma to'lovlari byudjetga kiritilgan.", "Raqamlar oila bilan tekshirilgan."]),
    art_title="Moliyaviy yordam arizasi paketi", art_short="Paket",
    art=[("Formalar jadvali", ["forma", "a1"]), ("Oila moliyaviy varaqasi", ["oila", "a2"]), ("Qo'shimcha izoh rejasi", ["izoh"]),
         ("Forma to'lovlari", ["tolov", "a3"]), ("Yordam xati hisobi", ["a4"]), ("Qayta ko'rib chiqish rejasi", ["a5"]), ("Eng yaqin muddat", ["muddat"])],
    tip="Moliyaviy yordam arizasida eng kuchli dalil izchillik: bir xil raqam, bir xil kurs, har birining ortida hujjat.",
    sources=f"{CSS}; {CSS_INT}; {NORTHWESTERN}; {HARVARD}; {DARTMOUTH}. {STD}",
)
