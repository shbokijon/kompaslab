from common import CARNEGIE, CHEA, DAPIP, SITS_SEARCH, DOS_VISA, HERD, NAV, CDS, EDUSA_UG, HOL, STD

MOD = dict(
    title="AQSh oliy ta'limi: tizim va universitetni tekshirish",
    desc="USA Lab M1: AQSh universitet turlari, akkreditatsiya va SEVP sertifikati, daraja tuzilmasi, soha bo'yicha kuchli joyni NSF HERD ma'lumoti bilan topish, universitetni rasmiy ma'lumot bilan tekshirish. Natija: universitet tekshiruv kartasi.",
    lead="AQShdagi oliy ta'lim muassasalari bir xil emas. Bu modulda universitet turlarini ajratasiz, uning haqiqiy va viza beradigan muassasa ekanini tekshirasiz, sohangiz bo'yicha kuchli joylarni reyting emas, ma'lumot bilan topasiz.",
    hero="usa", weeks="1–2", next="M2 Xarajat va pul oqimi", next_href="usa-lab-o.html?m=2",
    goals=[("telescope", "Universitet tekshiruv kartasi", "tur, akkreditatsiya, SEVP, soha kuchi, asosiy raqamlar"),
           ("chart", "Soha bo'yicha 10 ta kuchli joy", "NSF HERD ma'lumotidan, reytingdan emas"),
           ("shield", "Soxta va viza bermaydigan muassasalarni ajratish", "3 bosqichli tekshiruv")],
    warn=f"Bu modulda universitet tanlashning umumiy usullari (orzu, mo'ljal, ishonchli darajalar, reytinglar) qayta o'tilmaydi: ular Bachelor Lab M1–M2 va Master Lab M1 da. Bu yerda faqat AQShga xos tizim va tekshiruv. Raqamlar {HOL}; universitet sahifasidan qayta tekshiring.",
    lessons=[
        dict(t="Universitet turlari", short="Turlar", min=25, kind="🎯 Mini-test", ic="usa",
             hook="\"AQSh universiteti\" degan so'z ikki yillik kollejni ham, yiliga yuzlab doktor tayyorlaydigan tadqiqot markazini ham anglatadi. Turini bilmasangiz, noto'g'ri joyga ariza berasiz yoki arzon yo'lni ko'rmay qolasiz.",
             body=f"""<h4>To'rt asosiy tur</h4>
<div class="tbl"><table><thead><tr><th>Tur</th><th>Nima beradi</th><th>Kimga mos</th></tr></thead><tbody>
<tr><td>Ikki yillik kollej ([[community college]])</td><td>Ikki yillik dastur; keyin to'rt yillik universitetga o'tish ([[transfer]]) mumkin</td><td>Xarajatni kamaytirmoqchi bo'lgan bakalavr abituriyenti</td></tr>
<tr><td>Liberal san'at kolleji ([[liberal arts college]])</td><td>Asosan bakalavriat, kichik guruhlar, o'qituvchi bilan yaqin ish</td><td>Bakalavr; fanlar orasida izlanayotganlar</td></tr>
<tr><td>Tadqiqot universiteti</td><td>Bakalavriat, magistratura va ko'p doktorantura; laboratoriyalar, ilmiy grantlar</td><td>Magistratura, PhD; ilmiy tajriba istagan bakalavr</td></tr>
<tr><td>Davlat va xususiy</td><td>Davlat universiteti shtat byudjetiga tayanadi; xususiy universitet o'z jamg'armasiga</td><td>Narx va yordam siyosati har birida boshqa (M2–M3)</td></tr>
</tbody></table></div>
<h4>Tadqiqot darajasi: R1 va R2</h4>
<p>[[Carnegie Classification]] universitetlarni ilmiy faolligi bo'yicha guruhlaydi. 2025-yilgi metodologiyada eng yuqori daraja (R1) uchun yiliga kamida 50 million dollar ilmiy xarajat va 70 ta ilmiy doktorlik darajasi chegarasi qo'yilgan; R2 uchun 5 million dollar va 20 ta daraja. 2025-yilda 187 ta muassasa R1 bo'lgan.</p>
<div class="box info">R1 bo'lish \"yaxshi universitet\" degani emas. Bu ilmiy faollik o'lchovi. PhD va tadqiqot magistraturasi uchun muhim, bakalavr uchun hal qiluvchi emas.</div>
<h4>Ikki yillik kollej orqali yo'l</h4>
<p>EducationUSA xarajatni kamaytirish yo'llaridan biri sifatida avval ikki yillik kollejda o'qib, keyin to'rt yillik universitetga o'tishni ko'rsatadi. O'tishdan oldin kreditlar qaysi universitetda qabul qilinishini o'sha universitet sahifasidan tekshiring.</p>
<div class="srcs">Manba: {CARNEGIE}; {EDUSA_UG}. {HOL}.</div>""",
             take="To'rt tur: ikki yillik kollej, liberal san'at kolleji, tadqiqot universiteti, davlat va xususiy. R1 ilmiy faollik o'lchovi, sifat bahosi emas.",
             quiz=[("R1 maqomi universitet bakalavriati eng yaxshi ekanini bildiradi.", "n", "Noto'g'ri: R1 ilmiy xarajat va doktorlik darajalari soni bo'yicha o'lchov."),
                   ("Ikki yillik kollejdan keyin to'rt yillik universitetga o'tish mumkin.", "t", "To'g'ri: EducationUSA buni xarajatni kamaytirish yo'li sifatida ko'rsatadi."),
                   ("2025-yilgi R1 chegarasi: yiliga 50 mln dollar ilmiy xarajat va 70 ta ilmiy doktorlik darajasi.", "t", "To'g'ri: Carnegie 2025 metodologiyasi."),
                   ("Liberal san'at kollejlari asosan doktorantura beradi.", "n", "Noto'g'ri: asosan bakalavriat.")],
             task="<ul><li>Qiziqqan 3 ta muassasani yozing va har birining turini aniqlang (ikki yillik kollej, liberal san'at kolleji, tadqiqot universiteti; davlat yoki xususiy).</li><li>Agar PhD yoki tadqiqot magistraturasini ko'zlasangiz, har birining R1 yoki R2 ekanini Carnegie sahifasidan tekshiring.</li></ul>",
             ph="1) ... — tadqiqot universiteti, davlat, R1; 2) ... — liberal san'at kolleji, xususiy; 3) ..."),
        dict(t="Akkreditatsiya va SEVP sertifikati", short="Tekshiruv", min=25, kind="🔎 Tekshiruv", ic="shield",
             hook="Har yili kimdir \"AQSh universiteti\" nomidagi saytga pul to'laydi va keyin bu muassasa diplomi tan olinmasligini yoki I-20 bera olmasligini biladi. Ikki tekshiruv buni 15 daqiqada oldini oladi.",
             body=f"""<h4>1. Akkreditatsiya</h4>
<p>AQShda universitetlarni hukumat emas, maxsus tashkil etilgan xususiy tashkilotlar sifat bo'yicha tekshiradi. Bu jarayon akkreditatsiya deyiladi. Ikki rasmiy baza bor:</p>
<ul><li><b>CHEA bazasi</b>: 8 200 dan ortiq muassasa va 44 000 dan ortiq dastur; nom, shtat yoki akkreditatsiya tashkiloti bo'yicha qidiriladi.</li><li><b>DAPIP</b>: AQSh Ta'lim vazirligining akkreditatsiyalangan muassasalar bazasi.</li></ul>
<h4>2. SEVP sertifikati</h4>
<p>Talaba vizasi (F-1) uchun avval SEVP tomonidan tasdiqlangan muassasaga qabul qilinish kerak: aynan shu muassasa Form I-20 beradi. Muassasa SEVP ro'yxatida bormi, DHS ning [[Study in the States]] saytidagi qidiruvdan tekshiriladi.</p>
<div class="tbl"><table><thead><tr><th>Tekshiruv</th><th>Qayerda</th><th>Natija yo'q bo'lsa</th></tr></thead><tbody>
<tr><td>Akkreditatsiya</td><td>CHEA yoki DAPIP</td><td>Diplom tan olinmasligi mumkin; ro'yxatdan chiqaring</td></tr>
<tr><td>SEVP</td><td>[[Study in the States]] qidiruvi</td><td>I-20 bera olmaydi; talaba vizasi bo'lmaydi</td></tr>
<tr><td>Rasmiy sayt</td><td>Domen odatda .edu; manzilni o'zingiz qidirib oching</td><td>Xabardagi havolaga ishonmang</td></tr>
</tbody></table></div>
<div class="box warn">\"Kafolatli qabul\" yoki \"I-20 3 kunda\" deb reklama qiladigan muassasani ikkala bazada tekshirmaguncha pul o'tkazmang.</div>
<div class="srcs">Manba: {CHEA}; {DAPIP}; {SITS_SEARCH}; {DOS_VISA}. {HOL}.</div>""",
             take="Akkreditatsiya (CHEA yoki DAPIP) va SEVP sertifikati (Study in the States) tekshirilmagan muassasa ro'yxatga kirmaydi.",
             task="<ul><li>Ro'yxatingizdagi 3 muassasani CHEA yoki DAPIP da va SEVP qidiruvida tekshiring.</li><li>Har biri uchun: akkreditatsiya tashkiloti nomi, SEVP: ha/yo'q, tekshirilgan sana.</li></ul>",
             ph="... — akkreditatsiya: ... (CHEA), SEVP: ha, 31.10.2026"),
        dict(t="AQSh darajalari qanday tuzilgan", short="Darajalar", min=25, kind="🧭 Xarita", ic="books",
             hook="O'zbekistonda yo'nalish qabulda tanlanadi. AQSh bakalavriatida esa mutaxassislik ko'pincha keyinroq tanlanadi, magistratura esa ikki xil bo'ladi. Buni bilmasangiz, dastur sahifasini noto'g'ri o'qiysiz.",
             body="""<h4>Bakalavriat</h4>
<ul><li><b>[[Major]]</b>: asosiy mutaxassislik. Ko'p universitetlarda u birinchi kursdan keyin rasman tanlanadi; ba'zi dasturlar (masalan, muhandislik) qabulda tanlashni talab qiladi.</li><li><b>[[Minor]]</b>: ikkinchi, kichikroq yo'nalish.</li><li><b>Kredit soati</b>: har kursning og'irligi. Daraja uchun kerakli kredit soni va umumiy fanlar ([[general education]]) talabi universitet katalogida ([[academic catalog]]) yoziladi.</li></ul>
<h4>Magistratura</h4>
<div class="tbl"><table><thead><tr><th>Tur</th><th>Tuzilma</th><th>Nima uchun muhim</th></tr></thead><tbody>
<tr><td>Dissertatsiyali ([[thesis]])</td><td>Kurslar + ilmiy ish va himoya</td><td>PhD ga o'tish uchun kuchliroq dalil</td></tr>
<tr><td>Dissertatsiyasiz ([[non-thesis]], [[coursework]], [[professional]])</td><td>Asosan kurslar, ba'zan loyiha</td><td>Sanoatga tez chiqish; moliyalashtirish odatda kamroq (M7)</td></tr>
</tbody></table></div>
<h4>PhD</h4>
<p>AQSh PhD ko'pincha magistratura talab qilmaydi: bakalavrdan keyin to'g'ridan-to'g'ri qabul qilinish mumkin. Odatiy bosqichlar: kurslar, malaka imtihoni ([[qualifying exam]]), dissertatsiya mavzusini himoya qilish, tadqiqot va yakuniy himoya. Aniq tartib kafedra qo'llanmasida ([[graduate handbook]]) yoziladi.</p>
<div class="box info">Har bir da'voni dastur sahifasidan tekshiring: \"magistraturasiz PhD mumkin\" degan qoida hamma kafedraga tegishli emas.</div>""",
             take="Bakalavriatda major ko'pincha keyinroq tanlanadi; magistratura dissertatsiyali yoki dissertatsiyasiz; PhD ga bakalavrdan keyin ham kirish mumkin. Qoidalar katalog va kafedra qo'llanmasida.",
             task="<ul><li>Bitta bakalavriat yoki magistratura dasturining katalog sahifasini toping.</li><li>Yozing: daraja uchun kredit soni, majburiy kurslar, dissertatsiya bormi, major qachon tanlanadi.</li></ul>",
             ph="... universiteti, ... dasturi: ... kredit; dissertatsiya: ...; major: ... kursda; havola: ..."),
        dict(t="Soha bo'yicha kuchli joyni topish", short="Soha", min=35, kind="📊 Ma'lumot", ic="chart",
             hook="Umumiy reytingda 50-o'rindagi universitet sizning sohangizda birinchi o'ntalikda bo'lishi mumkin va aksincha. Kompas yondashuvi: mamlakat yoki umumiy reyting emas, aynan sizning sohangiz qayerda kuchli.",
             body=f"""<h4>NSF HERD soʻrovi</h4>
<p>AQSh Milliy ilmiy jamg'armasi (NSF) qoshidagi NCSES har yili universitetlarning ilmiy xarajatini ([[R&amp;D expenditures]]) soha va manba bo'yicha yig'adi. Bu [[HERD]] so'rovi: yiliga 150 ming dollardan ko'p ilmiy xarajati bor muassasalarning hammasi qamrab olinadi. Jadvallar soha va muassasa bo'yicha chiqariladi, [[Table Builder]] vositasi bor.</p>
<h4>Qanday ishlatiladi</h4>
<ol><li>HERD jadvallaridan sohangizni tanlang (masalan, geologiya, kompyuter fanlari, muhandislik turi).</li><li>Shu sohada ilmiy xarajati eng katta 15–20 muassasani yozib oling.</li><li>Har birining kafedra sahifasini oching: professorlar soni, laboratoriyalar, so'nggi yillardagi maqolalar.</li><li>Natijani o'zingizning darajangizga qarab saralang: PhD uchun ilmiy xarajat muhim; bakalavr uchun bu faqat bitta signal.</li></ol>
<div class="tbl"><table><thead><tr><th>Signal</th><th>Nimani ko'rsatadi</th><th>Cheklovi</th></tr></thead><tbody>
<tr><td>Soha bo'yicha ilmiy xarajat (HERD)</td><td>Laboratoriya va grant hajmi</td><td>Ta'lim sifatini to'g'ridan-to'g'ri o'lchamaydi</td></tr>
<tr><td>Kafedra professorlari va maqolalari</td><td>Siz ishlamoqchi bo'lgan mavzu bormi</td><td>Vaqt talab qiladi</td></tr>
<tr><td>Bitiruvchilar qayerda ishlaydi</td><td>Dastur natijasi</td><td>Ko'p dasturlar chop etmaydi</td></tr>
</tbody></table></div>
<div class="box warn">Ilmiy xarajat katta bo'lsa ham, bakalavr talabaga laboratoriyaga kirish kafolatlanmaydi. Bakalavr uchun bu ma'lumotni moliyaviy yordam (M3) va moslik bilan birga ko'ring.</div>
<div class="srcs">Manba: {HERD}. {HOL}.</div>""",
             take="Soha bo'yicha kuchni HERD ilmiy xarajat jadvali va kafedra sahifasi bilan tekshiring. Bu ilmiy faollik signali; ta'lim sifatining yagona o'lchovi emas.",
             task="<ul><li>HERD dan sohangiz bo'yicha 10 ta muassasani yozing.</li><li>Ulardan 3 tasining kafedra sahifasida sizga yaqin mavzudagi professor yoki laboratoriyani toping.</li></ul>",
             ph="Soha: ... HERD bo'yicha: 1) ... 2) ... Kafedra: ... — prof. ..., laboratoriya ..."),
        dict(t="Universitetni raqamlar bilan o'qish", short="Raqamlar", min=30, kind="🛠 Karta", ic="memo",
             hook="Universitet sayti o'zini eng yaxshi tomondan ko'rsatadi. Rasmiy statistik bazalar esa bir xil shablondagi raqamlarni beradi va universitetlarni solishtirishga imkon beradi.",
             body=f"""<h4>College Navigator</h4>
<p>AQSh Ta'lim vazirligi qoshidagi NCES ning [[College Navigator]] vositasi har bir muassasa bo'yicha narx, talabalar soni, bitirish darajasi va akkreditatsiya ma'lumotini bir sahifada beradi.</p>
<h4>Common Data Set</h4>
<p>Ko'p universitetlar har yili [[Common Data Set]] (CDS) ni bir xil shaklda chop etadi. AQShga xos foydali bo'limlar:</p>
<div class="tbl"><table><thead><tr><th>Bo'lim</th><th>Nima bor</th></tr></thead><tbody>
<tr><td>B</td><td>Talabalar soni, birinchi kursdan keyin qolish va bitirish darajasi</td></tr>
<tr><td>C</td><td>Bakalavriat qabuli: arizalar, qabul qilinganlar, test siyosati</td></tr>
<tr><td>G</td><td>Narxlar</td></tr>
<tr><td>H</td><td>Moliyaviy yordam, jumladan xalqaro talabalarga (M3 da chuqur)</td></tr>
</tbody></table></div>
<p>CDS ni topish: qidiruvga \"universitet nomi + Common Data Set\" yozing va natija universitet domenida (.edu) ekanini tekshiring.</p>
<h4>Karta uchun 6 qator</h4>
<ol><li>Tur va R darajasi (1.1).</li><li>Akkreditatsiya va SEVP (1.2).</li><li>Sohangiz bo'yicha kuch (1.4).</li><li>Talabalar soni va xalqaro talabalar ulushi.</li><li>Bitirish darajasi.</li><li>Xalqaro talaba uchun narx (M2 da to'liq).</li></ol>
<div class="srcs">Manba: {NAV}; {CDS}. {STD}</div>""",
             take="College Navigator va CDS bir xil shablondagi raqamlarni beradi. Har universitet uchun 6 qatorli karta tuzing.",
             task="<ul><li>Ro'yxatingizdagi bitta universitet uchun 6 qatorli kartani to'ldiring.</li><li>Har raqam yonida manba (Navigator yoki CDS yili) va sana.</li></ul>",
             ph="... universiteti: tur ..., akkreditatsiya ..., SEVP ..., soha ..., talabalar ..., bitirish ...%, narx ... (CDS 2025–2026)"),
    ],
    tool=dict(id="karta", short="Karta", h2="Universitet tekshiruv kartasi", sub="Bitta universitet uchun to'liq karta. Har universitetga alohida karta tuzing.",
              h3="Tekshiruv kartasi", tag="6 maydon", ic="telescope", btn="Kartani saqlash", badge="Tekshiruvchi", min=5,
              fields=[dict(k="uni", label="Universitet va dastur", ph="... universiteti, ... (bakalavriat / magistratura / PhD)"),
                      dict(k="tur", label="Turi", type="select", opts=["Ikki yillik kollej", "Liberal san'at kolleji", "Tadqiqot universiteti (R1)", "Tadqiqot universiteti (R2)", "Boshqa"]),
                      dict(k="akkr", label="Akkreditatsiya va SEVP", hint="baza nomi va sana", ph="CHEA: ..., SEVP: ha, 31.10.2026"),
                      dict(k="soha", label="Soha bo'yicha kuch", hint="HERD va kafedra", type="area", ph="HERD: ...; kafedra: prof. ..., laboratoriya ..."),
                      dict(k="raqam", label="Asosiy raqamlar", hint="Navigator yoki CDS", type="area", ph="Talabalar ..., xalqaro ...%, bitirish ...%, narx ..."),
                      dict(k="xulosa", label="Xulosa", type="select", opts=["Ro'yxatda qoladi", "Qo'shimcha tekshiruv kerak", "Ro'yxatdan chiqadi"])]),
    check=dict(h2="M1 nazorati", sub="Kartani yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Muassasa turi aniqlangan.", "Akkreditatsiya CHEA yoki DAPIP da tekshirilgan.", "SEVP ro'yxatida borligi tekshirilgan.",
                      "Rasmiy sayt manzili o'zim qidirib topilgan (xabardagi havola emas).", "Dastur katalogidan daraja tuzilmasi o'qilgan.",
                      "Soha bo'yicha kuch HERD va kafedra sahifasi bilan tekshirilgan.", "Raqamlar manbasi va yili yozilgan.", "Har bir raqam yonida tekshirilgan sana bor."]),
    art_title="Universitet tekshiruv kartasi", art_short="Karta",
    art=[("Universitet va dastur", ["uni"]), ("Turi", ["tur", "a1"]), ("Akkreditatsiya va SEVP", ["akkr", "a2"]), ("Daraja tuzilmasi", ["a3"]),
         ("Soha bo'yicha kuch", ["soha", "a4"]), ("Asosiy raqamlar", ["raqam", "a5"]), ("Xulosa", ["xulosa"])],
    tip="Universitetni reklama emas, uchta rasmiy baza tekshiradi: akkreditatsiya, SEVP va statistika. Pul to'lashdan oldin uchalasini ham ko'ring.",
    sources=f"{CARNEGIE}; {CHEA}; {DAPIP}; {SITS_SEARCH}; {DOS_VISA}; {HERD}; {NAV}; {CDS}; {EDUSA_UG}. {STD}",
)
