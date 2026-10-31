from common import MIT, DARTMOUTH, HARVARD, PRINCETON, NORTHWESTERN, OSU, CDS, CDS_H6, NPC, EDUSA_UG, HOL, STD

MOD = dict(
    title="Yordam beradigan universitetlarni topish",
    desc="USA Lab M3: xalqaro bakalavr abituriyentiga moliyaviy yordam siyosatlari, rasmiy sahifa so'zlarini o'qish, Common Data Set H6 bandi, Net Price Calculator va natijaga asoslangan grantlar. Natija: yordam siyosati bo'yicha saralangan ro'yxat.",
    lead="AQSh bakalavriatida yordam olish uchun avval yordam beradigan universitetni topish kerak. Bu modulda universitetlarni moliyaviy siyosatiga qarab to'rt guruhga ajratasiz va har birini rasmiy hujjat bilan tekshirasiz.",
    hero="telescope", weeks="2", next="M4 Moliyaviy yordam arizasi", next_href="usa-lab-o.html?m=4",
    goals=[("telescope", "Yordam ro'yxati", "har universitet: siyosat, H6 raqamlari, manba"),
           ("books", "Siyosat lug'ati", "rasmiy sahifadagi iboralarni to'g'ri o'qish"),
           ("chart", "Net Price taxmini", "kamida 2 universitet uchun")],
    warn=f"Bachelor Lab M2 universitetni moslik va daraja bo'yicha tanlaydi, M12.1 esa need-blind va need-aware atamalarini tanishtiradi. Bu modul AQSh universitetlarini moliyaviy yordam bo'yicha tekshirishning to'liq usuli. Siyosatlar har yili o'zgarishi mumkin; {HOL} rasmiy sahifadan qayta tekshiring.",
    lessons=[
        dict(t="To'rt xil yordam siyosati", short="Siyosatlar", min=30, kind="🧭 Xarita", ic="compass",
             hook="Bir universitet yordam so'raganingizni qabul qaroriga umuman qo'shmaydi va kerakli summani to'liq beradi. Boshqasi xalqaro talabaga deyarli yordam bermaydi. Ikkalasining sayti bir xil chiroyli ko'rinadi.",
             body=f"""<div class="tbl"><table><thead><tr><th>Guruh</th><th>Ma'nosi</th><th>Rasmiy misol ({HOL})</th></tr></thead><tbody>
<tr><td>A. Xalqaro talabaga ham need-blind va to'liq ehtiyoj</td><td>Yordam so'rash qabulga ta'sir qilmaydi; qabul qilinsangiz, hisoblangan ehtiyoj to'liq qoplanadi</td><td>MIT: barcha bakalavrlar, \"domestic and international\", uchun need-blind va full need. Dartmouth: 2026-yil bitiruvchilari kursidan boshlab need-blind siyosati barcha xalqaro fuqarolarga kengaytirilgan va xalqaro talabalarning ehtiyoji ham qoplanadi</td></tr>
<tr><td>B. Yordam qabulga ta'sir qilmaydi, lekin xalqaro talabaga alohida yozilmagan</td><td>Rasmiy so'zlarni diqqat bilan o'qish kerak</td><td>Harvard: yordam arizasi qabul imkoniyatiga ta'sir qilmaydi; xalqaro talabalar AQSh talabalari bilan bir xil yordamga haqli. Princeton: xalqaro talabalarga ham bir xil yordam siyosati; ehtiyojning 100 foizi grant bilan</td></tr>
<tr><td>C. Need-aware</td><td>Yordam so'rash qabul imkoniyatini kamaytirishi mumkin</td><td>Northwestern: yordam so'raganlarning qabul imkoniyati \"less favorable\"</td></tr>
<tr><td>D. Xalqaro talabaga yordam juda cheklangan</td><td>Asosan oila to'laydi</td><td>Ohio State: xalqaro talabalar odatda federal, shtat va ko'p universitet yordamini ololmaydi</td></tr>
</tbody></table></div>
<div class="box info">Bu jadval to'liq ro'yxat emas, misollar. Siyosat o'zgaradi: har universitetni o'zingiz tekshirib, A–D guruhiga qo'ying.</div>
<div class="box warn">A guruhi universitetlari eng tanlovli universitetlar qatorida. Ro'yxatni faqat A guruhidan tuzish xavfli: oila chegarasi past bo'lsa ham, C va D guruhidagi arzon variantlar va boshqa mamlakatlar parallel bo'lishi kerak.</div>
<div class="srcs">Manba: {MIT}; {DARTMOUTH}; {HARVARD}; {PRINCETON}; {NORTHWESTERN}; {OSU}. {HOL}.</div>""",
             take="A: xalqaro talabaga ham need-blind va to'liq ehtiyoj; B: rasmiy so'zlar aniqlashtirishni talab qiladi; C: need-aware; D: yordam juda cheklangan. Har universitetni o'zi tekshiring.",
             task="<ul><li>Ro'yxatingizdagi 5 universitetni A–D guruhlariga qo'ying.</li><li>Har biri uchun rasmiy sahifadan bir jumlalik dalil va havola.</li></ul>",
             ph="... — A, dalil: \"...\", havola ...; ... — C, dalil: ..."),
        dict(t="Rasmiy sahifa so'zlarini o'qish", short="Lug'at", min=25, kind="🎯 Mini-test", ic="books",
             hook="\"Generous aid\" degan ibora hech narsa va\'da qilmaydi. \"Meets 100% of demonstrated need for all admitted students, regardless of citizenship\" esa aniq majburiyat. Farqni ko'rish uchun 8 ta iborani bilish yetarli.",
             body=f"""<div class="tbl"><table><thead><tr><th>Ibora</th><th>Ma'nosi</th><th>Signal</th></tr></thead><tbody>
<tr><td>[[need-blind for all applicants]]</td><td>Yordam so'rash qabulga ta'sir qilmaydi; \"all\" ichida xalqaro talaba ham bormi, tekshiring</td><td>Kuchli, agar xalqaro talaba aniq aytilgan bo'lsa</td></tr>
<tr><td>[[regardless of citizenship]]</td><td>Fuqarolikdan qat'i nazar</td><td>Kuchli</td></tr>
<tr><td>[[meets 100% of demonstrated need]]</td><td>Hisoblangan ehtiyoj to'liq qoplanadi</td><td>Kuchli</td></tr>
<tr><td>[[need-aware for international students]]</td><td>Xalqaro talaba uchun yordam so'rash qabulga ta'sir qiladi</td><td>Ehtiyot</td></tr>
<tr><td>[[limited aid for international students]]</td><td>Yordam juda kam</td><td>Kuchsiz</td></tr>
<tr><td>[[merit scholarships]] / [[automatic consideration]]</td><td>Natijaga asoslangan grant; alohida ariza kerakmi, tekshiring</td><td>Qisman</td></tr>
<tr><td>[[no-loan]] / [[grant aid]]</td><td>Yordam qaytarilmaydigan grant shaklida</td><td>Kuchli</td></tr>
<tr><td>[[expected family contribution]] / [[parent contribution]]</td><td>Oila to'laydigan deb hisoblangan qism</td><td>Hisobni M4 da ko'rasiz</td></tr>
</tbody></table></div>
<div class="box info">\"Xalqaro talabalarga ham ochiq\" degan da'voni ko'rmaguningizcha uni bor deb hisoblamang. Savol bo'lsa, xalqaro qabul yoki moliyaviy yordam bo'limiga yozma so'rang va javobni saqlang.</div>""",
             take="Kuchli iboralar: need-blind for all applicants (xalqaro talaba aniq ko'rsatilgan), regardless of citizenship, meets 100% of demonstrated need, no-loan. Noaniq ibora majburiyat emas.",
             quiz=[("\"Generous financial aid\" iborasi to'liq ehtiyoj qoplanishini kafolatlaydi.", "n", "Noto'g'ri: bu majburiyat emas, tavsif."),
                   ("\"Need-aware for international students\" yordam so'rash qabulga ta'sir qilishi mumkinligini bildiradi.", "t", "To'g'ri."),
                   ("\"Regardless of citizenship\" iborasi xalqaro talabani ham qamrab oladi.", "t", "To'g'ri."),
                   ("\"No-loan\" siyosatida yordam qaytariladigan kredit shaklida beriladi.", "n", "Noto'g'ri: grant shaklida, qaytarilmaydi.")],
             task="<ul><li>2 universitetning xalqaro moliyaviy yordam sahifasidan aynan iborani ko'chirib, ma'nosini o'zbekcha yozing.</li></ul>",
             ph="... universiteti: \"...\" — ma'nosi: ...; signal: kuchli / ehtiyot / kuchsiz"),
        dict(t="Common Data Set: H6 bandi", short="H6", min=30, kind="📊 Ma'lumot", ic="chart",
             hook="Universitet \"xalqaro talabalarga yordam beramiz\" deyishi mumkin. CDS ning H6 bandi esa o'tgan yili nechta xalqaro talaba qancha olganini ko'rsatadi.",
             body=f"""<h4>H6 nima so'raydi</h4>
<p>CDS ning H6 bandi bakalavriatdagi daraja oluvchi xalqaro talabalar ([[nonresidents]]) uchun universitet grantlari haqida:</p>
<ul><li>Siyosat: universitetning ehtiyojga asoslangan granti beriladimi; ehtiyojga asoslanmagan granti beriladimi.</li><li>Yordam olgan xalqaro talabalar soni.</li><li>O'rtacha summa.</li><li>Jami summa.</li></ul>
<h4>Namuna: Nebraska universiteti, CDS 2025–2026</h4>
<p>H6 bandida 120 nafar xalqaro bakalavr yordam olgan, o'rtacha summa 10 391 dollar, jami 1 246 965 dollar deb ko'rsatilgan.</p>
<h4>Qanday o'qiladi</h4>
<ol><li>O'rtacha summani shu universitetning to'liq narxi (M2) bilan solishtiring: qancha qismi qoplanadi?</li><li>Yordam olganlar sonini xalqaro bakalavrlar soni (CDS B bo'limi) bilan solishtiring: taxminan qanchasi oladi?</li><li>Ikki-uch yillik CDS ni ko'ring: raqam barqarormi?</li></ol>
<div class="box warn">O'rtacha summa sizga beriladigan summa emas. U faqat universitetning xalqaro talabaga yordam berish hajmini ko'rsatadi.</div>
<div class="srcs">Manba: {CDS_H6}; {CDS}. {HOL}.</div>""",
             take="H6: xalqaro bakalavrlarga grant siyosati, olganlar soni, o'rtacha va jami summa. O'rtacha summani to'liq narx bilan solishtiring; bu sizning summangiz emas.",
             task="<ul><li>2 universitetning so'nggi CDS ida H6 ni toping.</li><li>Yozing: siyosat, olganlar soni, o'rtacha summa, to'liq narxning necha foizi.</li></ul>",
             ph="... universiteti, CDS 2025–2026: ehtiyojga asoslangan: ha; ... talaba; o'rtacha ... USD = narxning ...%"),
        dict(t="Net Price Calculator va natijaga asoslangan grantlar", short="Kalkulyator", min=30, kind="🧮 Hisob", ic="money",
             hook="Universitet saytidagi narx \"ro'yxat narxi\". Siz to'laydigan narx yordamdan keyin qoladigan summa. Uni ariza berishdan oldin taxminan bilish mumkin.",
             body=f"""<h4>Net Price Calculator</h4>
<p>AQSh Ta'lim vazirligining [[Net Price Calculator Center]] sahifasi tushuntiradi: kalkulyatorlar universitetlar saytida joylashgan va yordamdan keyingi taxminiy narxni hisoblaydi.</p>
<ul><li>Oila daromadi, jamg'arma va oila tarkibini dollarda kiriting (M4 dagi hisob bilan bir xil bo'lsin).</li><li>Kalkulyator xalqaro talaba uchun ishlaydimi yoki faqat AQSh talabasigami, sahifada yozilganini tekshiring.</li><li>Natija taxmin; rasmiy yordam xati emas.</li></ul>
<h4>Natijaga asoslangan grantlar</h4>
<p>H6 dagi ikkinchi siyosat bandi ([[non-need-based]] grant) universitet natijaga asoslangan grant berishini ko'rsatadi. Keyingi qadam: universitetning [[scholarships]] sahifasida xalqaro talabaga ochiq grantlar ro'yxati, shartlari va muddatlari.</p>
<div class="tbl"><table><thead><tr><th>Savol</th><th>Nega muhim</th></tr></thead><tbody>
<tr><td>Avtomatikmi yoki alohida arizami?</td><td>Alohida ariza muddati ko'pincha qabul muddatidan oldin</td></tr>
<tr><td>Bir yilmi yoki 4 yil?</td><td>4 yillik reja (Bachelor M12)</td></tr>
<tr><td>Qaysi baho saqlanishi kerak?</td><td>Grantni yo'qotish xavfi</td></tr>
<tr><td>Ehtiyojga asoslangan yordam bilan birga beriladimi?</td><td>Umumiy summa</td></tr>
</tbody></table></div>
<p>EducationUSA eslatadi: ko'p stipendiyalar narxning faqat bir qismini qoplaydi.</p>
<div class="srcs">Manba: {NPC}; {CDS_H6}; {EDUSA_UG}. {HOL}.</div>""",
             take="Net Price Calculator yordamdan keyingi taxminiy narxni beradi; xalqaro talabaga ishlashini tekshiring. Natijaga asoslangan grantning turi, muddati va shartini o'qing.",
             task="<ul><li>2 universitetning kalkulyatorida taxminiy narxni hisoblang (xalqaro talabaga ishlasa).</li><li>Bitta universitetning xalqaro talabaga ochiq natijaga asoslangan grantini toping: summa, muddat, shart.</li></ul>",
             ph="... kalkulyatori: ... USD/yil (xalqaro uchun: ha). Grant: ... — ... USD, muddat ..., shart ..."),
        dict(t="Yordam bo'yicha saralangan ro'yxat", short="Ro'yxat", min=30, kind="🛠 Ro'yxat", ic="memo",
             hook="Bachelor Lab'dagi orzu-mo'ljal-ishonchli ro'yxat qabul ehtimoliga qarab tuziladi. AQShda unga ikkinchi o'q qo'shiladi: qabul qilsa, oila to'lay oladimi?",
             body="""<h4>Ikki o'qli jadval</h4>
<div class="tbl"><table><thead><tr><th></th><th>Oila to'lay oladi (narx ≤ chegara)</th><th>Faqat yordam bilan</th></tr></thead><tbody>
<tr><td>Qabul ehtimoli yuqori</td><td>Ishonchli tanlov</td><td>Yordam real bo'lsa (A, B yoki kuchli H6) mos</td></tr>
<tr><td>Qabul ehtimoli o'rtacha</td><td>Mo'ljal</td><td>Faqat A guruhi yoki kuchli natijaga asoslangan grant</td></tr>
<tr><td>Qabul ehtimoli past</td><td>Orzu</td><td>Faqat A guruhi; bir nechtasidan ko'p emas</td></tr>
</tbody></table></div>
<h4>Kompas tavsiyasi (qoida emas)</h4>
<ul><li>Kamida bitta universitet \"oila to'lay oladi + qabul ehtimoli yuqori\" katagida bo'lsin. Bunday universitet yo'q bo'lsa, AQSh bilan parallel boshqa mamlakat (Bachelor Lab) majburiy.</li><li>D guruhidagi universitetga faqat oila to'liq to'lay olsa ariza bering.</li><li>Har bir ariza narxi (ariza yig'imi, CSS Profile, testlar) byudjetga kiradi.</li></ul>
<div class="box warn">\"Qabul qilsa, keyin pul topamiz\" degan reja ishlamaydi: I-20 uchun pul dalili qabuldan keyin darhol so'raladi (M2).</div>""",
             take="Ro'yxat ikki o'q bilan tuziladi: qabul ehtimoli va to'lay olish. Kamida bitta \"oila to'lay oladi, qabul ehtimoli yuqori\" variant bo'lmasa, parallel mamlakat kerak.",
             task="<ul><li>8–12 universitetni ikki o'qli jadvalga joylang.</li><li>Bo'sh katakni qanday to'ldirishingizni yozing.</li></ul>",
             ph="Ishonchli + oila to'laydi: ...; Mo'ljal + yordam: ...; Orzu + A guruhi: ...; Bo'sh katak: ..."),
    ],
    tool=dict(id="royxat", short="Ro'yxat", h2="Yordam ro'yxati", sub="Har universitet uchun siyosat guruhi va dalil. Oxirida ikki o'qli jadval xulosasi.",
              h3="Yordam ro'yxati", tag="5 maydon", ic="telescope", btn="Ro'yxatni saqlash", badge="Yordam izlovchi", min=4,
              fields=[dict(k="a_guruh", label="A va B guruhi universitetlari", hint="dalil va havola bilan", type="area", ph="... — A: \"...\" (havola) ..."),
                      dict(k="c_guruh", label="C guruhi (need-aware)", type="area", ph="..."),
                      dict(k="d_guruh", label="D guruhi (yordam cheklangan)", type="area", ph="..."),
                      dict(k="h6", label="H6 va kalkulyator natijalari", type="area", ph="... — H6: ... talaba, o'rtacha ...; kalkulyator: ..."),
                      dict(k="xulosa", label="Ikki o'qli jadval xulosasi", type="area", ph="Ishonchli + oila to'laydi: ...; parallel mamlakat: ...")]),
    check=dict(h2="M3 nazorati", sub="Ro'yxatni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har universitet A–D guruhiga rasmiy jumla bilan qo'yilgan.", "\"Barcha abituriyentlar\" ichida xalqaro talaba borligi aniqlangan.",
                      "Kamida 2 universitet uchun CDS H6 o'qilgan.", "H6 o'rtacha summasi to'liq narx bilan solishtirilgan.",
                      "Kalkulyator xalqaro talabaga ishlashi tekshirilgan.", "Natijaga asoslangan grantning muddati va sharti yozilgan.",
                      "\"Oila to'lay oladi + qabul ehtimoli yuqori\" katagida kamida bitta variant bor yoki parallel mamlakat tanlangan.", "Har manba yonida sana bor."]),
    art_title="Yordam bo'yicha saralangan ro'yxat", art_short="Ro'yxat",
    art=[("Siyosat guruhlari", ["a1"]), ("Rasmiy iboralar", ["a2"]), ("A va B guruhi", ["a_guruh"]), ("C guruhi", ["c_guruh"]), ("D guruhi", ["d_guruh"]),
         ("H6 va kalkulyator", ["h6", "a3", "a4"]), ("Ikki o'qli jadval", ["xulosa", "a5"])],
    tip="Moliyaviy yordam bo'yicha eng ko'p xato: universitet nima deyishini emas, nima deb taxmin qilinishini yozish. Har gapning yonida rasmiy jumla tursin.",
    sources=f"{MIT}; {DARTMOUTH}; {HARVARD}; {PRINCETON}; {NORTHWESTERN}; {OSU}; {CDS_H6}; {CDS}; {NPC}; {EDUSA_UG}. {STD}",
)
