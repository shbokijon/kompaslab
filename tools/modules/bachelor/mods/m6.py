from common import APO, MYGOV, CA, HOL, STD

MOD = dict(
    title="Yutuqlar, CV va hujjatlar",
    desc="Bachelor Lab M6: olimpiada va tanlovlar, onlayn kurslar, maktab yoshida ilmiy loyiha, bakalavr CV (STAR usuli), tarjima, notarius va apostil. Natija: Bakalavr CV v1.0 va hujjatlar nazorat ro'yxati.",
    lead="Yutuqlaringiz faqat hujjatda to'g'ri yozilganda ko'rinadi. Bu modulda qaysi yutuq qabulda ahamiyatli ekanini ajratasiz, CV ni STAR usulida yozasiz va hujjatlarni legallashtirish zanjirini rejalaysiz.",
    hero="memo", weeks="2", next="M7 Darsdan tashqari faoliyat", next_href="bachelor-lab-m7.html",
    goals=[("memo", "Bakalavr CV v1.0", "1–2 sahifa, har band STAR usulida"),
           ("shield", "Hujjatlar nazorat ro'yxati", "har hujjat: asl, tarjima, notarius yoki apostil, nusxa soni"),
           ("bulb", "Yutuqlar saralashi", "qaysi yutuq ahamiyatli, qaysi biri uncha foydali emas")],
    warn=f"Apostil tartibi va yig'imi, notarial tarjima talablari o'zgarishi mumkin. Bu moduldagi ma'lumot {HOL} gov.uz manbasidan; topshirishdan oldin qayta tekshiring.",
    lessons=[
        dict(t="Olimpiadalar va tanlovlar", short="Olimpiada", min=25, kind="🎯 Mini-test", ic="chart",
             hook="Viloyat olimpiadasidagi g'alaba ham, xalqaro tanlovdagi ishtirok ham CV ga yoziladi. Lekin komissiya ularni bir xil baholamaydi.",
             body="""<h4>Qaysi darajadagi yutuqlar muhim</h4>
<div class="tbl"><table><thead><tr><th>Daraja</th><th>Signal</th><th>Izoh</th></tr></thead><tbody>
<tr><td>Xalqaro fan olimpiadasi (IMO, IPhO, IOI va boshqalar) ishtiroki yoki medali</td><td>Juda kuchli</td><td>Juda kam o'quvchi erishadi</td></tr>
<tr><td>Respublika olimpiadasi g'olibi yoki sovrindori</td><td>Kuchli</td><td>O'zbekistonda tanlovning eng yuqori ichki darajasi</td></tr>
<tr><td>Viloyat bosqichi g'olibi</td><td>O'rta</td><td>Kontekst bilan yozing: nechta ishtirokchi</td></tr>
<tr><td>Tuman yoki maktab bosqichi</td><td>Past</td><td>Faqat boshqa yutuq yo'q bo'lsa</td></tr>
<tr><td>Pullik \"xalqaro\" tanlov, hamma qatnashuvchiga sertifikat</td><td>Deyarli yo'q</td><td>Tanlov tanlovli bo'lmasa, signal bermaydi</td></tr>
</tbody></table></div>
<h4>To'g'ri yozish</h4>
<p>Format: <b>nomi, daraja, natija, yil, kontekst</b>. Masalan (Kompas tuzgan namuna): \"Fizika bo'yicha respublika olimpiadasi, 2-o'rin (2026), viloyatdan tanlangan 3 o'quvchidan biri\".</p>
<div class="box warn">Ishtirokchilar sonini yoki o'rinni bilmasangiz, yozmang. Tekshirib bo'lmaydigan raqam ishonchni pasaytiradi.</div>""",
             take="Xalqaro va respublika darajasidagi yutuqlar muhim dalil; pullik ommaviy tanlovning oʻzi ustunlik bermaydi. Har yutuqni nomi, daraja, natija, yil va kontekst bilan yozing.",
             quiz=[("Hamma qatnashuvchiga beriladigan pullik \"xalqaro\" sertifikat muhim dalil.", "n", "Noto'g'ri: saralashsiz oʻtkaziladigan tanlovning oʻzi ustunlik bermaydi."),
                   ("Respublika olimpiadasi sovrindori kuchli yutuq.", "t", "To'g'ri: bu ichki tanlovning eng yuqori darajasi."),
                   ("Ishtirokchilar sonini taxminan yozib qo'yish mumkin.", "n", "Noto'g'ri: tekshirib bo'lmaydigan raqamni yozmang."),
                   ("Yutuq yozuvida yil va daraja bo'lishi kerak.", "t", "To'g'ri: komissiya vaqt va miqyosni ko'radi.")],
             task="<ul><li>Barcha yutuqlaringizni ro'yxatlang va har birini jadvaldagi darajaga qo'ying.</li><li>Eng kuchli 3 tasini to'liq formatda yozing.</li></ul>",
             ph="1) ... olimpiadasi, ..., ..., 2026, ... 2) ..."),
        dict(t="Onlayn kurslar va sertifikatlar", short="Kurslar", min=20, kind="⚖️ Saralash", ic="books",
             hook="10 ta onlayn kurs sertifikati CV ni to'ldiradi, lekin kuchaytirmaydi. Bitta chuqur o'zlashtirilgan va amalda qo'llangan kurs ko'proq gapiradi.",
             body="""<h4>Qachon foydali</h4>
<ul><li>Maktabda o'tilmaydigan fanni o'rganganingizni ko'rsatsa (masalan, dasturlash, chiziqli algebra).</li>
<li>Kurs natijasida biror narsa qilgan bo'lsangiz: loyiha, dastur, tadqiqot.</li>
<li>Kurs universitet darajasida va baholangan topshiriqlari bo'lsa.</li></ul>
<h4>Qachon ahamiyati kam maʼlumot</h4>
<ul><li>Faqat videolarni ko'rib olingan \"tugatish sertifikati\".</li><li>Sohangizga aloqasi yo'q ko'p qisqa kurslar.</li><li>Pullik sertifikat, lekin hech qanday natija yo'q.</li></ul>
<h4>Yozish usuli</h4>
<p>CV da kursni alohida qator qilib emas, u bilan qilgan ishingiz bilan birga yozing: \"Onlayn kurs asosida maktab uchun dars jadvali dasturini yozdim (Python)\".</p>
<div class="box info">2–3 ta kurs yetarli. Ularni M3 dagi qiziqish sohasi bayoni bilan bog'lang.</div>""",
             take="Onlayn kurs natija bilan birga yozilsa foydali, yolg'iz sertifikat ahamiyati kam maʼlumot. 2–3 ta sohaga yaqin kurs yetarli.",
             task="<ul><li>Olgan kurslaringizni \"foydali\" va \"ahamiyati kam maʼlumot\" deb ajrating.</li><li>Foydali kurslar uchun ular bilan qilgan aniq ishingizni yozing.</li></ul>",
             ph="Foydali: ... → natija: ... Ahamiyati kam maʼlumot: ..."),
        dict(t="Maktab yoshida ilmiy loyiha", short="Loyiha", min=30, kind="🔬 Reja", ic="telescope",
             hook="Ilmiy loyiha maktab o'quvchisi uchun eng kuchli dalillardan biri, chunki u sizning savol berish va javob izlash qobiliyatingizni ko'rsatadi. Lekin uni boshlash 6–12 oy oladi.",
             body="""<h4>Mavzu topish</h4>
<ul><li>M3 dagi aniq savolingizdan boshlang.</li><li>Mavzu kichik va tekshiriladigan bo'lsin: \"suv tozaligi\" emas, \"mahallamizdagi uchta quduq suvining pH va qattiqligi\".</li><li>Ma'lumot yig'ish mumkinligini tekshiring: asbob, ruxsat, vaqt.</li></ul>
<h4>Ustoz topish</h4>
<p>Maktab o'qituvchisi, mahalliy universitet o'qituvchisi yoki laboratoriya xodimi. Xat qisqa bo'lsin: kim siz, qanday savol, nima qilib bo'ldingiz, ulardan nima so'rayapsiz (masalan, oyiga bir marta 30 daqiqa maslahat).</p>
<h4>Natijani hujjatlash</h4>
<ul><li>Ish daftari: sana, nima qildingiz, natija.</li><li>Yakuniy 3–5 sahifali hisobot yoki poster.</li><li>Maktab konferensiyasi, tanlov yoki onlayn ochiq joyda taqdimot.</li></ul>
<div class="box warn"><b>Halollik.</b> Loyihani boshqa odam qilib bergan bo'lsa yoki natija to'qilgan bo'lsa, tavsiya xati va intervyuda bu ochilib qoladi. Kichik, lekin o'zingizniki bo'lgan loyiha kuchliroq.</div>""",
             take="Kichik, tekshiriladigan savol + ustoz + ish daftari + yakuniy hisobot. Kichik, lekin o'zingizniki bo'lgan loyiha katta va qarzga olingandan kuchli.",
             task="<ul><li>Loyiha uchun 2 ta kichik, tekshiriladigan savol yozing.</li><li>Ustoz sifatida 2 nomzodni va ularga yuboradigan xatning asosiy 4 jumlasini yozing.</li></ul>",
             ph="Savol 1: ... Savol 2: ... Ustoz: ... Xat: Men ..., savolim ..., qilganim ..., so'rovim ..."),
        dict(t="Bakalavr CV (STAR usuli)", short="CV", min=35, kind="🛠 CV v1.0", ic="memo",
             hook="CV dagi \"jamoada ishlashni bilaman\" degan jumla hech narsani isbotlamaydi. STAR usuli har bandni aniq voqea va natija bilan yozadi.",
             body="""<h4>STAR usuli</h4>
<div class="tbl"><table><thead><tr><th>Harf</th><th>Ma'nosi</th><th>Savol</th></tr></thead><tbody>
<tr><td><b>V</b>aziyat ([[Situation]])</td><td>Qayerda, qachon</td><td>Qanday sharoit edi?</td></tr>
<tr><td><b>V</b>azifa ([[Task]])</td><td>Nima qilish kerak edi</td><td>Maqsad nima edi?</td></tr>
<tr><td><b>H</b>arakat ([[Action]])</td><td>Siz nima qildingiz</td><td>Aynan siz nima qildingiz?</td></tr>
<tr><td><b>N</b>atija ([[Result]])</td><td>Nima o'zgardi</td><td>Raqam yoki aniq natija bormi?</td></tr>
</tbody></table></div>
<p>CV da STAR bitta qatorga siqiladi. Kompas tuzgan namuna: \"Maktab robototexnika to'garagini tashkil qildim (8 o'quvchi); haftalik mashg'ulotlar o'tkazdim; jamoa viloyat tanloviga chiqdi.\"</p>
<h4>Bakalavr CV tuzilmasi (1–2 sahifa)</h4>
<ol><li>Ism, aloqa (email, telefon), shahar.</li><li>Ta'lim: maktab, yillar, baholar (asl shkalada).</li><li>Yutuqlar va mukofotlar (L1 formatida).</li><li>Loyihalar va tadqiqot.</li><li>Faoliyatlar va yetakchilik (M7).</li><li>Ko'nikmalar: tillar (daraja bilan), dasturlar.</li></ol>
<div class="box info">Akademik CV va ishchi rezyume ([[Academic CV vs Resume]]) farqi: bakalavr arizasida ish tajribasidan ko'ra ta'lim, loyiha va faoliyat birinchi turadi. Rasm, tug'ilgan sana va oilaviy holat odatda kerak emas.</div>""",
             take="Har CV bandi STAR: vaziyat, vazifa, harakat, natija; bitta qatorda. Bakalavr CV 1–2 sahifa, ta'lim va loyihalar birinchi.",
             task="<ul><li>Eng muhim 5 faoliyat yoki yutuqingizni STAR usulida bitta qatordan yozing.</li><li>Pastdagi vositada CV v1.0 bo'limlarini to'ldiring.</li></ul>",
             ph="1) ... ni tashkil qildim (...); ...; natija: ... 2) ..."),
        dict(t="Tarjima, notarius, apostil", short="Apostil", min=30, kind="🗺 Zanjir", ic="shield",
             hook="Notarial tasdiqlangan nusxa yetarli deb o'ylash qimmat xato bo'lishi mumkin. Har mamlakat va universitet boshqa tasdiq turini so'raydi.",
             body=f"""<h4>Uch xil tasdiq</h4>
<div class="tbl"><table><thead><tr><th>Tasdiq</th><th>Nima</th><th>Qachon so'raladi</th></tr></thead><tbody>
<tr><td>Tarjima</td><td>Hujjatning ingliz (yoki boshqa) tiliga tarjimasi</td><td>Deyarli har doim</td></tr>
<tr><td>Notarial tasdiq</td><td>Notarius tarjima yoki nusxaning to'g'riligini tasdiqlaydi</td><td>Ko'p universitetlar va viza markazlari</td></tr>
<tr><td>Apostil</td><td>Hujjat boshqa davlatda rasmiy deb tan olinishi uchun davlat tasdig'i (Apostil konvensiyasi a'zolari orasida)</td><td>Ba'zi universitetlar, stipendiyalar (masalan GKS), viza</td></tr>
</tbody></table></div>
<h4>O'zbekistonda apostil</h4>
<p>Apostil uchun ariza my.gov.uz orqali elektron yoki Davlat xizmatlari markazida beriladi. gov.uz ma'lumotiga ko'ra so'rov ikki ish kuni ichida ko'rib chiqiladi, ta'lim muassasalari bergan hujjatlar uchun yig'im bazaviy hisoblash miqdorining 20 foizi. Rad etilsa, xatoni tuzatib 30 kun ichida qayta topshirish mumkin.</p>
<h4>Ketma-ketlik</h4>
<ol><li>Asl hujjatdagi ism pasport bilan mosligini tekshiring.</li><li>Universitet nima so'rashini aniqlang: tarjima, notarius, apostil yoki hammasi.</li><li>Apostil asl hujjatga yoki tarjimaga qo'yilishini universitet talabidan o'qing.</li><li>Nechta nusxa kerakligini yozing.</li></ol>
<div class="box warn">Apostil tez, lekin undan oldingi qadamlar (maktabdan hujjat olish, tarjima, xatoni tuzatish) haftalab cho'ziladi. Zanjirni muddatdan kamida 8–10 hafta oldin boshlang.</div>
<div class="srcs">Manba: {APO}; {MYGOV}. {HOL}; yig'im va muddat o'zgarishi mumkin.</div>""",
             take="Tarjima, notarius va apostil turli talablar. Har universitet nima so'rashini aniqlang va zanjirni muddatdan 8–10 hafta oldin boshlang.",
             task="<ul><li>Har asosiy hujjat uchun zanjir yozing: asl → tarjima → notarius/apostil → nusxa soni.</li><li>Qaysi universitet nima talab qilishini qavsda ko'rsating.</li></ul>",
             ph="Attestat: asl → tarjima (...) → apostil (...) → 2 nusxa. Transkript: ..."),
    ],
    tool=dict(id="cv", short="CV", h2="Bakalavr CV v1.0", sub="Har bandni STAR usulida bitta qatorda yozing. Natija 1–2 sahifalik CV.",
              h3="CV ish varag'i", tag="6 maydon", ic="memo", btn="CV ni saqlash", badge="CV ustasi", min=5,
              fields=[dict(k="ism", label="Ism va aloqa", hint="pasportdagidek", ph="Ism Familiya · email · telefon · shahar"),
                      dict(k="talim", label="Ta'lim", type="area", ph="... maktabi, 2020–2027; baholar: 4.8/5"),
                      dict(k="yutuq", label="Yutuqlar va mukofotlar", hint="nomi, daraja, natija, yil", type="area", ph="..."),
                      dict(k="loyiha", label="Loyihalar va tadqiqot", hint="STAR, bitta qator", type="area", ph="..."),
                      dict(k="faoliyat", label="Faoliyatlar va yetakchilik", type="area", ph="..."),
                      dict(k="konikma", label="Ko'nikmalar", hint="tillar daraja bilan, dasturlar", ph="O'zbek (ona tili), ingliz (IELTS ...), rus ...; Python ...")]),
    check=dict(h2="CV va hujjatlar nazorati", sub="Topshirishdan oldin tekshiring.", h3="9 bandlik nazorat",
               items=["CV 1–2 sahifa.", "Har band harakat fe'li bilan boshlanadi va natijani ko'rsatadi.",
                      "Yutuqlar nomi, daraja, natija va yil bilan yozilgan.", "Tekshirib bo'lmaydigan raqam yo'q.",
                      "Ism pasport bilan harfma-harf bir xil.", "Har hujjat uchun tasdiq turi (tarjima, notarius, apostil) aniqlangan.",
                      "Apostil zanjiri muddatdan 8–10 hafta oldin boshlanadi.", "Nusxalar soni yozilgan.", "CV dagi har band hujjat yoki guvoh bilan tasdiqlanadi."]),
    art_title="Bakalavr CV v1.0 va hujjatlar ro'yxati", art_short="CV",
    art=[("Ism va aloqa", ["ism"]), ("Ta'lim", ["talim"]), ("Yutuqlar va mukofotlar", ["yutuq", "a1"]), ("Loyihalar va tadqiqot", ["loyiha", "a3"]),
         ("Faoliyatlar va yetakchilik", ["faoliyat", "a4"]), ("Ko'nikmalar va kurslar", ["konikma", "a2"]), ("Hujjatlar zanjiri", ["a5"])],
    tip="CV ni ovoz chiqarib o'qing. Har bandda \"xo'sh, natija nima bo'ldi?\" degan savolga javob bo'lmasa, bandni qayta yozing.",
    sources=f"{APO}; {MYGOV}; {CA}. {STD}",
)
