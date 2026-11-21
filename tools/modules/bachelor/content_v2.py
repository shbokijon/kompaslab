# Bakalavr dasturi M1–M8 v2 kontenti (2026-11-21, Magistratura va USA v2 andozasi; 16 → 8 modul, 32-hujjat).
# YANGI alifboda yoziladi (Ö, Ğ, Ş, Ç, ʼ); engine.py manbaga amaldagi alifboda (oʻ, gʻ, sh, ch) yozadi.
# [[...]] → <i lang="en">. Har dars: t, short, min, hook, fun (ixtiyoriy), main, info_t/info (ixtiyoriy), take, task_b, task (röyxat).
# Eski dars matni mods/m<N>.py da (v1.les) ⓘ "Batafsil" ostiga ötadi; quiz, ic, kind, ph, vositalar va JS şu yerda emas.
# Hazil: Bakalavr örta daraja, darsda bittagaça; muddat, pul, viza, rad javobi va firibgarlik darslarida yöq.

SUB = "Har dars 4 qism: Diqqat, Asosiy qism, Xulosa, Topşiriq. Har qism 1–3 daqiqa."
DISCLAIMER = ("Kompas Lab universitet, stipendiya dasturi yoki konsullik örnida qaror qabul qilmaydi va qabul, stipendiya yoki vizani kafolatlamaydi. "
              "Inşo, xat va hujjatni siz uçun yozmaydi: vositalar faqat sizning matningizni tartibga soladi. "
              "Sana va talablarni rasmiy sahifadan özingiz tasdiqlaysiz. Sanasi körsatilgan maʼlumot şu sanadagi holat.")

M_TITLES = {
    1: ["Arizani kim öqiydi va qanday qaror qiladi?", "Attestatingiz xorijda", "Reytingni töğri öqiş", "Fizika, muhandislik, informatika: farqi nima?",
        "Soha va mamlakat xaritasi", "Uç darajali röyxat va moslik bali", "Arizalar budjeti"],
    2: ["Ariza oynalari: ED, EA, RD, UCAS", "Baholar va transkript", "Ingliz tili testi", "SAT, ACT va test siyosati", "Teskari reja va nazorat jadvali", "Maktab bilan muvozanat"],
    3: ["Men kim sifatida ariza beryapman?", "Nima faoliyat hisoblanadi?", "Olimpiada, kurs va loyiha", "Yetakçilik va yozgi dasturlar", "Faoliyatlar röyxati: 10 yozuv",
        "CV: STAR usuli", "Izçil hikoya xaritasi"],
    4: ["Kuçli tavsiya xati qanday böladi?", "Öqituvçidan qanday söraş kerak?", "Yutuqlar varaqasi", "Platformada tavsiya va maktab maslahatçisi", "Tarjima, notarius, apostil"],
    5: ["Şaxsiy bayonot va qiziqiş bayoni", "Hikoya va mavzu", "Birinçi qoralama", "UCAS: uç savol", "Qöşimça inşolar: «Nega aynan biz?»",
        "Tahrir: mazmun, tuzilma, til", "Fikr oliş, AI çegarasi va yakuniy versiya"],
    6: ["Stipendiya qayerdan keladi?", "Davlat stipendiyalari: saralaş jadvali", "Universitet yordami va grantlari", "Töliq xarajat modeli", "4 yillik reja", "Firibgarlikdan himoya"],
    7: ["Common App", "UCAS", "Universitet portallari", "Xitoy, Italiya, Singapur: kimga qaysi yöl?", "Topşiriş va oxirgi tekşiruv"],
    8: ["Intervyu turlari va «Özingiz haqingizda»", "Akademik intervyu", "Yozib oliş va baholaş", "Qabul, rad, kutiş röyxati", "Qabul xati va talaba vizasi",
        "Uy, suğurta, jönaş va birinçi yil"],
}


def lock(items):
    return '<ul class="mv-lock">' + "".join('<li><img src="img/3d/lock.webp" alt="" width="22" height="22">%s</li>' % x for x in items) + "</ul>"


def bar(p, label):
    return '<div class="mv-bar"><i style="width:%d%%"></i></div><p class="mv-small">%s</p>' % (p, label)


def tl(n):
    return ["%d.%d %s" % (n, i + 1, t) for i, t in enumerate(M_TITLES[n])]


TARIF = ('<p class="mv-small">Keyingi bosqiç 1 ta bosqiç tarifida navbatdagi tölov bilan oçiladi. '
         'Töliq dastur tarifida hamma modul allaqaçon oçiq. 18 yoşga tölmagan bölsangiz, obunani ota-onangiz rasmiylaştiradi.</p>')


def row(a, b):
    return '<div class="mv-row"><a class="btn btn-p" href="bachelor-lab-o.html?m=%d">%s</a>%s</div>' % (a, b, "")


MODULES = {}

# ───────────────────────────── M1 ─────────────────────────────
MODULES[1] = dict(
    lead="Bu modulda qabul qanday qaror qilişini, attestatingiz xorijda qanday baholanişini va reytingni qanday öqişni örganasiz. "
         "Keyin soha va mamlakatni tanlaysiz. Oxirida sizda <strong>saralangan röyxat</strong> böladi: 8–12 universitet, uç daraja, moslik bali va arizalar budjeti.",
    weeks="1–2", pass_time="~1–2 hafta (darslar ~1,5 soat + röyxat)",
    next=("<h2>Keyingi qadam: muddatlar</h2>" + bar(30, "I bosqiç: 1 / 2 modul · Rejangiz 30% tayyor") +
          '<div class="mv-k" data-mn="m1"><b>Saralangan röyxatingiz tayyor.</b> Endi har universitetning muddati va test talabini bitta jadvalga qöyiş qoladi. '
          "M2 da eng erta muddatingizdan orqaga hisoblab, qaysi işni qaçon boşlaşni aniqlaysiz.</div>"
          "<p>M2.1 dan: <i>AQŞda bitta universitetga uç xil muddatda ariza beriş mumkin, har birining majburiyati boşqa.</i></p>"
          + row(2, "M2: muddatlar va testlar")),
    lessons=[
        dict(t=M_TITLES[1][0], short="Komissiya", min=12,
             hook="Arizangizni qabul bölimidagi odam öqiydi, köpinça bir neça daqiqada. U sizni tanimaydi, faqat hujjatda yozilganni köradi. "
                  "Bu darsda u nimaga qaraşini va qabulning ikki mantiqini ajratamiz.",
             main="""<div class="tbl"><table><thead><tr><th></th><th>Yaxlit ([[holistic]])</th><th>Ball asosidagi</th></tr></thead><tbody>
<tr><td>Qayerda köp</td><td>AQŞning tanlovli kollejlari, Oksford va Kembrij</td><td>Germaniya, Italiya, Xitoy, Turkiya, köp Yevropa davlat universitetlari</td></tr>
<tr><td>Nima hal qiladi</td><td>Baholar, inşo, tavsiya, faoliyat va kontekst birga</td><td>Attestat bahosi, kiriş testi, til sertifikati</td></tr>
<tr><td>Vaqtingiz qayerga</td><td>Hikoya va hujjatlarga</td><td>Baho va testga</td></tr>
</tbody></table></div>
<p>Buyuk Britaniya örtada: asosan baho va başorat qilingan natija hal qiladi, bayonot va tavsiya qöşimça dalil. AQŞda modelni [[Common Data Set]] ning C7 bölimidan körasiz.</p>""",
             take="Avval universitetning qabul modelini aniqlang, keyin vaqtingizni şu model talab qilgan qismga sarflang.",
             task_b="Uç universitetning modeli",
             task=["Uçta universitetning rasmiy qabul sahifasini oçing.", "Har biri uçun yozing: yaxlit, ball asosidagi yoki aralaş, va buni qayerdan bildingiz."]),
        dict(t=M_TITLES[1][1], short="Attestat", min=12,
             hook="Özbekiston maktabi 11 yil, köp mamlakat esa 12 yillik taʼlimni kutadi. Bu farq butun rejani özgartirişi mumkin. "
                  "Bu darsda attestatingiz nişon mamlakatlarda qanday qabul qilinişini tekşiramiz.",
             main="""<div class="tbl"><table><thead><tr><th>Mamlakat</th><th>11 yillik attestat bilan</th></tr></thead><tbody>
<tr><td>AQŞ</td><td>Köpinça töğridan-töğri birinçi kursga</td></tr>
<tr><td>Buyuk Britaniya</td><td>Köp universitet tayyorlov yili ([[foundation year]]) yoki qöşimça malaka söraydi</td></tr>
<tr><td>Germaniya</td><td>Odatda Studienkolleg va imtihon yoki Özbekistonda 1–2 yil universitet</td></tr>
<tr><td>Italiya</td><td>12 yil kerak: yetmagan yil universitet öqişi bilan töldiriladi</td></tr>
<tr><td>Koreya, Xitoy, Turkiya</td><td>Odatda attestat bilan, universitet öz tanlovi bilan</td></tr>
</tbody></table></div>
<p>Jadval umumiy yönaliş. Aniq javobni universitetning mamlakat böyiça talablar sahifasi yoki xalqaro bölimining yozma javobi beradi.</p>""",
             fun="Forumdagi «bemalol kirsa böladi» degan gapga işonib qolsak, keyin hammamiz Studienkolleg haqida öqiymiz.",
             take="Har nişon mamlakat uçun attestat talabini rasmiy manbadan tekşiring va havolasini saqlang.",
             task_b="Attestatingiz va 3 mamlakat",
             task=["3 nişon mamlakat uçun töğridan-töğri kiriş mumkinmi yoki qöşimça yil kerakmi, rasmiy manbadan aniqlang.", "Havola va tekşirilgan sanani yozing."]),
        dict(t=M_TITLES[1][2], short="Reyting", min=10,
             hook="Reytingdagi 50-örin sizning fakultetingiz uçun 150-örin bölişi mumkin. "
                  "Bu darsda umumiy va fan böyiça reytingni ajratamiz va metodologiyani öqiymiz.",
             main="""<ul><li><b>Umumiy reyting</b> butun universitetni ölçaydi: maqolalar, obröʼ sörovi, xalqarolik.</li>
<li><b>Fan böyiça reyting</b> aniq sohani ölçaydi. Sizga keraklisi şu.</li>
<li>QS obröʼ sörovlariga, THE tadqiqot va iqtiboslarga, US News AQŞ kollejlarining bitiriş natijalariga köproq tayanadi.</li>
<li>Reyting bakalavr darsining sifatini, guruh hajmini va narxni körsatmaydi.</li></ul>
<p>Reytingni birinçi saralaş uçun işlating. Keyin dastur sahifasi va öquv rejasini ([[curriculum]]) oçing.</p>""",
             take="Reyting saralaşga yordam beradi, tanlovni esa dastur tarkibi va moslik hal qiladi.",
             task_b="Uç universitetning ikki örni",
             task=["Sohangizni yozing.", "3 universitetning umumiy va şu soha böyiça örnini soliştiring; farqi katta bölganini belgilang."]),
        dict(t=M_TITLES[1][3], short="STEM tanlovi", min=12,
             hook="Fizikani yaxşi körgan öquvçi muhandislikka, matematikani yaxşi körgan informatikaga boriş şart emas. "
                  "Bu darsda uç sohani asosiy savoli va keyingi yöli böyiça soliştiramiz.",
             main="""<div class="tbl"><table><thead><tr><th></th><th>Fizika</th><th>Muhandislik</th><th>Informatika</th></tr></thead><tbody>
<tr><td>Asosiy savol</td><td>Tabiat qanday işlaydi?</td><td>Buni qanday quriş mumkin?</td><td>Buni qanday hisoblaş va avtomatlaştiriş mumkin?</td></tr>
<tr><td>Kundalik iş</td><td>Model, tajriba, tahlil</td><td>Loyiha, hisob, sinov, jamoa</td><td>Kod, tizim, maʼlumot</td></tr>
<tr><td>Keyingi yöl</td><td>Köpinça magistratura va tadqiqot</td><td>Sanoat yoki magistratura</td><td>Sanoat yoki tadqiqot</td></tr>
</tbody></table></div>
<p>Tanlagan sohangiz bakalavrdan keyin kamida ikkita yölni oçiq qoldirsin: iş, magistratura, tadqiqot yoki Vatanga qaytiş.</p>""",
             take="Sohani tanlaşdan oldin birinçi kurs öquv rejasini oçing va şu sohada işlaydigan odam bilan 15 daqiqa gaplaşing.",
             task_b="Ikki soha orasida",
             task=["Ikkalasining birinçi kurs fanlarini yozing.", "Qaysi biri sizga yaqinroq va nega, 3 jumlada yozing."]),
        dict(t=M_TITLES[1][4], short="Mamlakatlar", min=12,
             hook="AQŞ, Buyuk Britaniya va Germaniyani hamma biladi. Xitoy, Italiya, Vengriya va Turkiyada ham ayrim sohada kuçli dastur va davlat stipendiyasi bor. "
                  "Bu darsda mamlakatlarni tizim, til va xarajat böyiça soliştiramiz.",
             main="""<div class="tbl"><table><thead><tr><th>Mamlakat</th><th>Tizim va til</th><th>Xarajat mantiqi</th></tr></thead><tbody>
<tr><td>AQŞ</td><td>4 yil, mutaxassislik keyinroq; ingliz</td><td>Narx yuqori, ayrim universitetlar ehtiyojga qarab yordam beradi</td></tr>
<tr><td>Buyuk Britaniya</td><td>3 yil (Şotlandiyada 4); ingliz</td><td>Narx yuqori, bakalavrga töliq stipendiya kam</td></tr>
<tr><td>Germaniya</td><td>3–4 yil; asosan nemis</td><td>Köp joyda öqiş deyarli bepul, yaşaş xarajati uçun bloklangan hisob</td></tr>
<tr><td>Koreya, Yaponiya</td><td>4 yil; koreys, yapon</td><td>GKS va MEXT töliq stipendiyasi (M6, GKS dasturi)</td></tr>
<tr><td>Xitoy, Italiya, Vengriya, Turkiya</td><td>Ingliz tilidagi dasturni alohida tekşiring</td><td>CSC, DSU, Stipendium Hungaricum, Türkiye Bursları (M6)</td></tr>
</tbody></table></div>""",
             take="Kam tanlanadigan mamlakatda dastur sifatini soha reytingi, akkreditatsiya va bitiruvçilar qayerga ketişi bilan tekşiring.",
             task_b="Ikki mamlakat",
             task=["Bitta taniş va bitta kam tanlanadigan mamlakatni tanlang.", "Har biri uçun sohangizda ingliz tilidagi dastur, attestat talabi va stipendiya bor-yöqligini yozing."]),
        dict(t=M_TITLES[1][5], short="Röyxat", min=15,
             hook="Faqat eng kuçli universitetlarga ariza beriş ham, faqat osonlariga beriş ham xavfli. Birinçisi rad bilan, ikkinçisi afsus bilan tugaşi mumkin. "
                  "Bu darsda röyxatni uç darajaga ajratib, har universitetga moslik bali qöyamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Daraja</th><th>Maʼnosi</th><th>Qança</th></tr></thead><tbody>
<tr><td>Orzu ([[reach]])</td><td>Qabul ehtimoli past</td><td>2–3</td></tr>
<tr><td>Möljal ([[target]])</td><td>Ballingiz qabul qilinganlar örtasida</td><td>3–5</td></tr>
<tr><td>Işonçli ([[likely]])</td><td>Talabdan yuqorisiz, narx ham töğri keladi</td><td>2–3</td></tr>
</tbody></table></div>
<p><b>Moslik bali:</b> dastur tarkibi, laboratoriya, til, xarajat, şahar va qöllab-quvvatlaşni 0–3 ball bilan baholang. 18 dan 12 dan past universitet röyxatda qoliş uçun alohida sabab kerak.</p>""",
             take="Röyxatda 2–3 orzu, 3–5 möljal va 2–3 işonçli universitet bölsin. Işonçli universitet ham siz borişga tayyor joy bölişi şart.",
             task_b="Röyxatingiz uç darajada",
             task=["Universitetlaringizni uç darajaga ajrating va har birining sababini bir jumlada yozing.", "3 universitetni olti mezon böyiça 0–3 ball bilan baholang."]),
        dict(t=M_TITLES[1][6], short="Budjet", min=10,
             hook="Har ariza xarajat talab qiladi: ariza tölovi, test natijasini yuboriş, tarjima, apostil. 12 ta ariza sezilarli summaga yetadi. "
                  "Bu darsda arizalar budjetini oldindan hisoblaymiz.",
             main="""<div class="tbl"><table><thead><tr><th>Xarajat</th><th>Qayerdan aniqlanadi</th></tr></thead><tbody>
<tr><td>Ariza tölovi</td><td>Universitet yoki platforma sahifasi; ozod qiliş sörovi bölişi mumkin (M7)</td></tr>
<tr><td>Test natijasini yuboriş</td><td>SAT, IELTS, TOEFL rasmiy saytlari</td></tr>
<tr><td>Tarjima va apostil</td><td>Tarjima idorasi narxi; apostil yiğimi gov.uz da</td></tr>
<tr><td>Hujjat baholaş</td><td>uni-assist kabi xizmatlar tölovi</td></tr>
</tbody></table></div>
<p>Narxni asl valyutada yozing va hisoblagan kuningizdagi kursni qöşing.</p>""",
             take="Budjet yetmasa, avval moslik bali eng past universitetni olib taşlang. Işonçli darajani nolga tuşirmang.",
             task_b="Arizalar budjeti",
             task=["Har ariza uçun taxminiy narxni asl valyutada yozing.", "Jami summani va tölovdan ozod qiliş mumkin bölgan arizalarni belgilang."]),
    ])

# ───────────────────────────── M2 ─────────────────────────────
MODULES[2] = dict(
    lead="Bu modulda har universitetning ariza oynasini, test talabini va hujjatlar muddatini bitta jadvalga yiğasiz. "
         "Keyin eng erta muddatdan orqaga hisoblab, qaysi işni qaçon boşlaşni aniqlaysiz. Oxirida sizda <strong>vaqt jadvali va test kalendari</strong> böladi.",
    weeks="1–2", pass_time="~1–2 hafta (darslar ~1,2 soat + jadval)",
    next=("<h2>I bosqiç yakunlandi: keyingi qadam profil</h2>" + bar(40, "I bosqiç: 2 / 2 modul · Rejangiz 40% tayyor") +
          '<div class="mv-k" data-mn="m2"><b>Vaqt jadvalingiz tayyor.</b> Endi jadvaldagi bandlarni töldiradigan hujjatlar kerak: faoliyatlar röyxati, CV va tavsiya xatlari. '
          "Tavsiyani eng erta muddatdan kamida 8 hafta oldin söraysiz, uni II bosqiçda tayyorlaysiz.</div>"
          "<p>II bosqiç darslari:</p>" + lock(tl(3) + tl(4)[:2]) + TARIF +
          '<div class="mv-row"><a class="btn btn-p" href="bachelor-lab-o.html?m=3">II bosqiç: M3 ni oçiş</a><a class="btn btn-g" href="bachelor-lab-narxlar.html">Tariflar</a></div>'),
    lessons=[
        dict(t=M_TITLES[2][0], short="Oynalar", min=12,
             hook="AQŞda bitta universitetga uç xil muddatda ariza beriş mumkin, har biri boşqa majburiyat bilan keladi. "
                  "Bu darsda ariza oynalarini va ularning şartini ajratamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Oyna</th><th>Qaçon (odatda)</th><th>Majburiyat</th></tr></thead><tbody>
<tr><td>Erta qaror ([[Early Decision]], ED)</td><td>Kuz, köpinça noyabr</td><td>Majburiy: qabul qilinsangiz, boşqa arizalarni qaytarib olasiz</td></tr>
<tr><td>Erta ariza ([[Early Action]], EA)</td><td>Kuz</td><td>Majburiy emas; çeklangan turi boşqa erta arizani taqiqlaydi</td></tr>
<tr><td>Oddiy muddat ([[Regular Decision]], RD)</td><td>Qiş, köpinça yanvar</td><td>Majburiy emas</td></tr>
<tr><td>UCAS</td><td>Oksford, Kembrij, köp tibbiyot: oktabr örtasi; qolganlari: yanvar</td><td>Bitta ariza, 5 tagaça tanlov</td></tr>
<tr><td>Universitet portallari</td><td>Har universitetning öz sanasi</td><td>Universitet qoidasiga qarab</td></tr>
</tbody></table></div>
<p>Xalqaro talaba uçun ED xavfli bölişi mumkin: yordam taklifini boşqa universitet bilan soliştira olmaysiz.</p>""",
             take="Har sanani universitetning rasmiy sahifasidan oling va yonida manba bilan tekşirilgan kunni yozing.",
             task_b="Röyxatingiz muddatlari",
             task=["Har universitet uçun ariza oynasi va muddatni rasmiy sahifadan yozing.", "ED yoki EA ni körib çiqayotgan bölsangiz, sababini yozing."]),
        dict(t=M_TITLES[2][1], short="Baholar", min=12,
             hook="Komissiya Özbekiston baholaş tizimini bilmasligi mumkin. «4.7» deb yoziş yetmaydi: qaysi şkala, qaysi fanlar, qaysi yillar? "
                  "Bu darsda baholar va transkriptni töğri taqdim qilamiz.",
             main="""<ol><li><b>Asl şkalada yozing:</b> «4.7 / 5» yoki «86 / 100». Özingiz GPA ga aylantirmang.</li>
<li><b>Şkalani tuşuntiring:</b> 5 eng yuqori, 3 ötiş bahosi.</li>
<li><b>Sohangizga yaqin fanlarni körsating:</b> matematika, fizika, informatika.</li>
<li><b>Hujjatlar:</b> ariza vaqtida transkript va maktabdan maʼlumotnoma, asl attestat odatda qabuldan keyin.</li>
<li><b>Ism:</b> pasport, attestat, test sertifikati va formada harfma-harf bir xil.</li></ol>""",
             take="Baholarni asl şkalada, izoh bilan yozing. Hujjatlardagi ism pasportdagidek bölsin.",
             task_b="Baholaringiz jadvali",
             task=["Oxirgi 3 yildagi baholaringizni asl şkalada fanlar böyiça yozing.", "Maktabdan qaysi hujjatni qaçon oliş mumkinligini aniqlang."]),
        dict(t=M_TITLES[2][2], short="Til testi", min=10,
             hook="Uç xil test bor, har biri boşqa universitetlarda qabul qilinadi. Notöğri test tanlansa, yaxşi natija ham iş bermaydi. "
                  "Bu darsda röyxatingizga mos bitta testni tanlaymiz.",
             main="""<div class="tbl"><table><thead><tr><th>Test</th><th>Qayerda köp qabul qilinadi</th></tr></thead><tbody>
<tr><td>IELTS Academic</td><td>Buyuk Britaniya va köp mamlakat; UK vizasi uçun UKVI varianti kerak bölişi mumkin</td></tr>
<tr><td>TOEFL iBT</td><td>AQŞ</td></tr>
<tr><td>Duolingo English Test</td><td>Köp AQŞ universitetlari; UK va Yevropada har universitetda alohida tekşiring</td></tr>
</tbody></table></div>
<p>Har universitetning umumiy va qism böyiça minimal ballini yozing. Sertifikat odatda 2 yil amal qiladi.</p>""",
             take="Birinçi uriniş muddatdan kamida 3–4 oy oldin bölsin, qayta topşirişga vaqt qolsin.",
             task_b="Bitta test va sana",
             task=["Röyxatingizdagi universitetlar qabul qiladigan testlar va minimal ballarni yozing.", "Tanlagan testingiz va birinçi uriniş sanasini belgilang."]),
        dict(t=M_TITLES[2][3], short="SAT/ACT", min=12,
             hook="SAT yoki ACT asosan AQŞ uçun kerak. «Test ixtiyoriy» degan yozuv esa testni keraksiz qilib qöymaydi. "
                  "Bu darsda testni topşiriş va ballni yuboriş qarorini qabul qilamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Siyosat</th><th>Nima qilasiz</th></tr></thead><tbody>
<tr><td>Talab qilinadi ([[test-required]])</td><td>Albatta topşiring</td></tr>
<tr><td>Ixtiyoriy ([[test-optional]])</td><td>Ballingiz universitet oraliğining örtasi yoki yuqorisida bölsa, yuboring</td></tr>
<tr><td>Hisobga olinmaydi ([[test-blind]])</td><td>Vaqtni boşqa qismga sarflang</td></tr>
</tbody></table></div>
<p>Oraliqni CDS ning C9 bölimidan oling: qabul qilinganlarning 25- va 75-persentil ballari. Tayyorgarlik odatda 2–4 oy, Özbekistonda test joylari tez tölişi mumkin.</p>""",
             fun="SAT ga tayyorlanayotganda «bir kunda 3 ta sinov testi» degan reja tuzsak, odatda ikkinçisidayoq çoy ham sovib qoladi.",
             take="Test siyosatini har yili universitet sahifasidan tekşiring va ixtiyoriy siyosatda qarorni CDS oraliği bilan qabul qiling.",
             task_b="Test qarorlari",
             task=["Har universitetingizning test siyosatini yozing.", "Kerak bölsa, bitta rasmiy sinov testini topşirib natijani yozing."]),
        dict(t=M_TITLES[2][4], short="Teskari reja", min=15,
             hook="«Qaçon boşlaşim kerak?» degan savolga eng erta muddatdan orqaga hisoblaş aniq javob beradi. Köp iş bir-biriga boğliq: test natijasisiz ariza yöq. "
                  "Bu darsda teskari reja va nazorat jadvalini tuzamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Iş</th><th>Muddatdan neça hafta oldin</th></tr></thead><tbody>
<tr><td>Arizani topşiriş</td><td>1 (zaxira)</td></tr>
<tr><td>Inşoning yakuniy versiyasi</td><td>2–3</td></tr>
<tr><td>Tavsiya sörovi</td><td>6–8</td></tr>
<tr><td>Til testi natijasi</td><td>8–12</td></tr>
<tr><td>Tarjima va apostil</td><td>8–10</td></tr>
<tr><td>Inşoning birinçi qoralamasi</td><td>10–12</td></tr>
<tr><td>SAT yoki ACT (kerak bölsa)</td><td>10–16</td></tr>
</tbody></table></div>
<p>Nazorat jadvalida har universitet uçun: platforma, oyna, muddat, hujjatlar, tölov, holat.</p>""",
             take="Teskari rejani bir marta tuzasiz, nazorat jadvalini esa har hafta bir xil kunda yangilaysiz.",
             task_b="Sizning teskari rejangiz",
             task=["Eng erta muddatingizdan orqaga 7 ta asosiy işni haftalar böyiça joylaştiring.", "Nazorat jadvalini yarating, kamida 5 universitetni kiriting va yangilaş kunini tanlang."]),
        dict(t=M_TITLES[2][5], short="Ritm", min=8,
             hook="Ariza jarayoni maktabning eng oğir yiliga töğri keladi. Baholar tuşsa, ariza ham zaiflaşadi. "
                  "Bu darsda haftalik ritmni tuzamiz.",
             main="""<ul><li><b>Blok 1 (1–2 soat):</b> darslar va topşiriqlar.</li>
<li><b>Blok 2 (1–2 soat):</b> hujjat ustida iş.</li>
<li><b>Blok 3 (30–60 daqiqa):</b> jadvalni yangilaş va keyingi hafta rejasi.</li></ul>
<p>Imtihon va olimpiada haftalarini rejada oldindan «yengil hafta» deb belgilang. Haftada bir kun ariza işisiz qolsin.</p>""",
             fun="Uyqusiz yozilgan inşoni ertalab öqisak, uni kim yozganini özimiz ham tanimay qolamiz.",
             take="Reja 3 hafta ketma-ket bajarilmasa, rejani qisqartiring: universitetlar sonini yoki qöşimça işni kamaytiring.",
             task_b="Haftalik ritm",
             task=["3 blok uçun aniq kun va vaqtni belgilang.", "Keyingi 3 oydagi imtihon haftalarini yozing."]),
    ])

# ───────────────────────────── M3 ─────────────────────────────
MODULES[3] = dict(
    lead="Bu modulda bitta jumlali profilingizni yozasiz, darsdan taşqari faoliyatlaringizni yiğasiz va CV tuzasiz. "
         "Oxirida sizda <strong>10 ta faoliyat yozuvi, CV va izçil hikoya xaritasi</strong> böladi.",
    weeks="2", pass_time="~2 hafta (darslar ~1,5 soat + röyxat va CV)",
    next=("<h2>Keyingi qadam: tavsiya xatlari</h2>" + bar(50, "II bosqiç: 1 / 2 modul · Rejangiz 50% tayyor") +
          '<div class="mv-k" data-mn="m3"><b>Faoliyatlar röyxatingiz va CV tayyor.</b> Endi öqituvçingiz şu faktlarni öz xatida tasdiqlaşi kerak. '
          "M4 da ulardan eng yaxşi 3–5 tasi Yutuqlar varaqasiga ötadi.</div>"
          "<p>M4.1 dan: <i>«Aʼloçi va mehnatkaş» degan xatni komissiya minglab öqigan. Kuçli xatda aniq epizod bor.</i></p>"
          + row(4, "M4: tavsiya xatlari")),
    lessons=[
        dict(t=M_TITLES[3][0], short="Profil", min=12,
             hook="«Men hamma fanni yaxşi köraman» degan abituriyent komissiyaga heç narsa demaydi. "
                  "Bu darsda arizangizning hamma qismini bir-biriga boğlaydigan bitta jumlali profilni yozamiz.",
             main="""<p>Profil formulasi:</p>
<p><i>Men [soha]ga qiziqaman, çunki [savol yoki muammo]; buni [dalil 1] va [dalil 2] körsatadi.</i></p>
<p>Dalilni uç joydan qidiring:</p>
<ul><li><b>Fanlar:</b> qaysi fanda baholaringiz yuqori va qaysi biriga köp vaqt sarflaysiz?</li>
<li><b>Loyihalar:</b> olimpiada, dastur, tajriba, töğarak.</li>
<li><b>Qiziqişlar:</b> darsdan taşqari ham öylantiradigan savol.</li></ul>""",
             take="Profil soha, sabab va ikkita dalildan iborat. Dalil kam bölsa, uni şu modulda yiğasiz.",
             task_b="Sizning profilingiz",
             task=["Fanlar, loyihalar va qiziqişlar böyiça 3 tadan fakt yozing.", "Formula böyiça bitta jumlali profilingizni tuzing."]),
        dict(t=M_TITLES[3][1], short="Faoliyat", min=10,
             hook="Köp öquvçi «menda faoliyat yöq» deydi, çunki faqat töğarak va tanlovni hisoblaydi. Ukangizga har kuni qaraş ham faoliyat. "
                  "Bu darsda faoliyat turlarini va komissiya nimaga qaraşini ajratamiz.",
             main="""<ul><li>Töğarak va klub</li><li>Sport va sanʼat</li><li>Iş, oilaviy biznesda yordam</li>
<li>Oilaviy majburiyat: Common App buni alohida tur sifatida qabul qiladi</li>
<li>Mustaqil loyiha: dastur, sayt, kanal, tadqiqot</li><li>Köngillilik</li></ul>
<p>Komissiya uç narsaga qaraydi: vaqt (haftasiga soat, yillar soni), rol va natija.</p>""",
             fun="Uyda ukaga matematika tuşuntirgan bölsangiz, bu ham faoliyat. Ukaning roziligini olmasak ham böladi.",
             take="Faoliyat içiga iş va oilaviy majburiyat ham kiradi. Har birida vaqt, rol va natijani yozing.",
             task_b="Hamma faoliyatlaringiz",
             task=["Oxirgi 3–4 yildagi faoliyatlaringizni turlari böyiça yozing, kamida 8 ta.", "Har biriga haftasiga soat va yillar sonini qöşing."]),
        dict(t=M_TITLES[3][2], short="Yutuqlar", min=15,
             hook="Viloyat olimpiadasidagi ğalaba ham, pullik «xalqaro» tanlov sertifikati ham CV ga yoziladi. Komissiya ularni bir xil baholamaydi. "
                  "Bu darsda olimpiada, kurs va loyihani signal kuçi böyiça saralaymiz.",
             main="""<div class="tbl"><table><thead><tr><th>Yutuq</th><th>Signal</th></tr></thead><tbody>
<tr><td>Xalqaro fan olimpiadasi (IMO, IPhO, IOI)</td><td>Juda kuçli</td></tr>
<tr><td>Respublika olimpiadasi ğolibi yoki sovrindori</td><td>Kuçli</td></tr>
<tr><td>2–3 yil davom etgan öz loyihangiz, natijasi bilan</td><td>Kuçli</td></tr>
<tr><td>Viloyat bosqiçi ğolibi</td><td>Örta, kontekst bilan yozing</td></tr>
<tr><td>Natija bilan bitirilgan onlayn kurs</td><td>Örta</td></tr>
<tr><td>Hammaga beriladigan sertifikat, faqat video körilgan kurs</td><td>Juda kam</td></tr>
</tbody></table></div>
<p>Format: nomi, daraja, natija, yil, kontekst. Tekşirib bölmaydigan raqamni yozmang.</p>""",
             take="Bitta çuqur va davomli iş ön ta qisqa işdan kuçliroq. Uni hozirdan boşlang va davom ettiring.",
             task_b="Eng kuçli 3 yutuq",
             task=["Yutuqlaringizni jadvaldagi darajaga qöying.", "Eng kuçli 3 tasini nomi, daraja, natija, yil va kontekst bilan yozing."]),
        dict(t=M_TITLES[3][3], short="Yetakçilik", min=10,
             hook="«Sinf sardori edim» degan gap lavozimni aytadi. Komissiya esa siz tufayli nima özgarganini bilmoqçi. "
                  "Bu darsda yetakçilik va yozgi dasturlarni natija böyiça baholaymiz.",
             main="""<div class="tbl"><table><thead><tr><th>Zaif tavsif</th><th>Kuçli tavsif</th></tr></thead><tbody>
<tr><td>Maktab kengaşi aʼzosi</td><td>Kengaşda kutubxona soatini 2 soatga uzaytiriş taklifini kiritib, maʼmuriyat bilan kelişdim; haftasiga ~40 öquvçi foydalanadi</td></tr>
</tbody></table></div>
<p><b>Yozgi dasturlar:</b> tanlovli dastur (ariza, tanlov, köpinça bepul) kuçli dalil. Pullik dasturning özi faqat tölov qobiliyatini körsatadi. Muqobil: amaliyot, mustaqil loyiha, iş.</p>""",
             take="Yetakçilikni natija bilan yozing: siz tufayli nima özgardi va buni qanday tasdiqlaysiz?",
             task_b="Bitta faoliyat, ikki tavsif",
             task=["Bitta yetakçilik yoki ijtimoiy faoliyatingizni zaif va kuçli körinişda yozing.", "Keyingi yoz uçun 2 ta tanlovli yoki bepul imkoniyatni muddati bilan toping."]),
        dict(t=M_TITLES[3][4], short="10 yozuv", min=15,
             hook="Common App da har faoliyat uçun 150 belgi bor. Şu joyda nima qilganingizni va natijasini aytiş alohida könikma. "
                  "Bu darsda 10 ta yozuvni şu formatda yozamiz.",
             main="""<ul><li><b>Rol:</b> 50 belgigaça.</li><li><b>Taşkilot:</b> 100 belgigaça.</li><li><b>Tavsif:</b> 150 belgigaça.</li>
<li>Sinflar, haftasiga soat, yiliga hafta.</li></ul>
<p>Tavsifni feʼl bilan boşlang ([[Founded]], [[Built]], [[Taught]]), raqam qöşing, eng muhim faoliyatni röyxat boşiga qöying.</p>
<p lang="en">Built a Telegram bot that sends homework reminders to 120 students; maintained it for 2 years; teachers now use it in 4 classes.</p>
<p class="mv-small">Kompas tuzgan namuna, faqat format uçun.</p>""",
             take="Har tavsif feʼl bilan boşlanadi va raqam yoki natijani körsatadi. UCAS da alohida röyxat yöq: faoliyatlar bayonotning 3-savoliga kiradi.",
             task_b="10 ta yozuv",
             task=["Eng muhim 10 faoliyatingizni tartiblang.", "Pastdagi vositada har birining 150 belgilik tavsifini yozing."]),
        dict(t=M_TITLES[3][5], short="CV", min=15,
             hook="CV dagi «jamoada işlaşni bilaman» degan jumla heç narsani isbotlamaydi. "
                  "Bu darsda har bandni aniq voqea va natija bilan yozadigan STAR usulini qöllaymiz.",
             main="""<div class="tbl"><table><thead><tr><th>Harf</th><th>Savol</th></tr></thead><tbody>
<tr><td>S ([[Situation]])</td><td>Qayerda, qaçon?</td></tr>
<tr><td>T ([[Task]])</td><td>Nima qiliş kerak edi?</td></tr>
<tr><td>A ([[Action]])</td><td>Aynan siz nima qildingiz?</td></tr>
<tr><td>R ([[Result]])</td><td>Nima özgardi?</td></tr>
</tbody></table></div>
<p>CV da STAR bitta qatorga siğadi. Namuna: <i>«Maktab robototexnika töğaragini taşkil qildim (8 öquvçi), haftalik mashğulot ötkazdim, jamoa viloyat tanloviga çiqdi.»</i></p>
<p>Tuzilma (1–2 sahifa): ism va aloqa, taʼlim, yutuqlar, loyihalar, faoliyatlar, könikmalar.</p>""",
             take="Bakalavr CV da taʼlim va loyihalar birinçi turadi. Rasm, tuğilgan sana va oilaviy holat şart emas.",
             task_b="CV qatorlari",
             task=["Eng muhim 5 faoliyat yoki yutuqingizni STAR usulida bitta qatordan yozing.", "Pastdagi vositada CV bölimlarini töldiring."]),
        dict(t=M_TITLES[3][6], short="Hikoya", min=10,
             hook="Komissiya arizangizni bir neça qismdan köradi: fanlar, faoliyat, inşo, tavsiya. Ular bir-birini tasdiqlasa, işonç oşadi. "
                  "Bu darsda hammasini bitta xaritaga qöyamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Qism</th><th>Savol</th></tr></thead><tbody>
<tr><td>Fanlar va baholar</td><td>Sohangizga yaqin fanlarda baholaringiz qanday?</td></tr>
<tr><td>Faoliyatlar</td><td>Darsdan taşqari şu yönalişda nima qildingiz?</td></tr>
<tr><td>Inşo (M5)</td><td>Nega bu soha sizga muhim?</td></tr>
<tr><td>Tavsiya (M4)</td><td>Öqituvçi qaysi epizodni yoza oladi?</td></tr>
</tbody></table></div>
<p>Turli faoliyat ham bitta xarakterni körsata oladi. Hikoyani töqimang: komissiya qismlarni bir-biri bilan soliştiradi.</p>""",
             take="Böş qolgan katak keyingi oylardagi işingiz. Eng zaif ustunni kuçaytiradigan bitta harakatni tanlang.",
             task_b="Sizning xaritangiz",
             task=["Tört ustunli jadvalni özingiz uçun töldiring.", "Eng zaif ustunni va uni kuçaytiradigan 1 aniq harakatni yozing."]),
    ])

# ───────────────────────────── M4 ─────────────────────────────
MODULES[4] = dict(
    lead="Bu modulda kimdan tavsiya söraşni, qaçon va qanday söraşni hal qilasiz va öqituvçiga beriladigan yutuqlar varaqasini yozasiz. "
         "Keyin hujjatlaringiz uçun tarjima va apostil zanjirini tuzasiz. Oxirida sizda <strong>yutuqlar varaqasi, aloqalar jadvali va hujjatlar zanjiri</strong> böladi.",
    weeks="1–2", pass_time="~1–2 hafta (darslar ~1 soat + varaqa)",
    next=("<h2>II bosqiç yakunlandi: keyingi qadam inşo</h2>" + bar(60, "II bosqiç: 2 / 2 modul · Rejangiz 60% tayyor") +
          '<div class="mv-k" data-mn="m4"><b>Tavsiya va hujjatlar yöli tayyor.</b> Endi arizaning eng şaxsiy qismi qoladi: inşo. '
          "III bosqiçda (M5–M6) inşoni yozasiz va 4 yillik moliyaviy rejani tuzasiz.</div>"
          "<p>III bosqiç darslari:</p>" + lock(tl(5) + tl(6)[:2]) + TARIF +
          '<div class="mv-row"><a class="btn btn-p" href="bachelor-lab-o.html?m=5">III bosqiç: M5 ni oçiş</a><a class="btn btn-g" href="bachelor-lab-narxlar.html">Tariflar</a></div>'),
    lessons=[
        dict(t=M_TITLES[4][0], short="Kuçli xat", min=10,
             hook="«U aʼloçi va mehnatkaş öquvçi» degan xatni komissiya minglab öqigan. Kuçli xatda öqituvçi özi körgan aniq voqea bor. "
                  "Bu darsda zaif va kuçli xatni ajratamiz va kim yozişini tanlaymiz.",
             main="""<div class="tbl"><table><thead><tr><th>Zaif</th><th>Kuçli</th></tr></thead><tbody>
<tr><td>Umumiy maqtov: «aqlli, faol»</td><td>Aniq epizod: «masalani uç usulda yeçib, sinfga tuşuntirdi»</td></tr>
<tr><td>Baholarni takrorlaydi</td><td>Baholarda körinmaydigan sifat: savol beriş, xatodan keyin qayta urinish</td></tr>
<tr><td>Soliştirişsiz</td><td>Kontekst bilan, faqat haqiqat bölsa</td></tr>
</tbody></table></div>
<p>Yozuvçi: sizni darsda yaqindan bilgan öqituvçi, sohangizga yaqin fandan, oxirgi 1–2 yilda dars bergan. Lavozimi baland, lekin sizni bilmaydigan odam zaifroq xat yozadi.</p>""",
             take="Tavsiyaçini lavozimiga qarab tanlamang. Sizni aniq epizod orqali biladigan öqituvçini tanlang.",
             task_b="3 nomzod",
             task=["3 nomzod tavsiyaçini yozing.", "Har biri sizni qaysi aniq epizod orqali bilişini yozing."]),
        dict(t=M_TITLES[4][1], short="Sörov", min=10,
             hook="Öqituvçi bir vaqtda bir neça öquvçiga xat yozişi mumkin. Keç sörov şoşilgan va umumiy xatga olib keladi. "
                  "Bu darsda sörovni vaqtida va töğri tartibda yuboramiz.",
             main="""<ol><li><b>Qaçon:</b> birinçi muddatdan kamida 6–8 hafta oldin.</li>
<li><b>Avval oğzaki:</b> «Menga kuçli xat yoza olasizmi?» deb söraysiz, rad etiş imkonini qoldirasiz.</li>
<li><b>Keyin yozma:</b> qisqa xat, yutuqlar varaqasi, universitetlar, muddatlar va topşiriş usuli.</li>
<li><b>Eslatma:</b> muddatdan 2 hafta va 3 kun oldin.</li>
<li><b>Rahmat:</b> natijadan qatʼi nazar.</li></ol>
<p>Xat inglizça kerak bölsa, öqituvçi özbekça yozadi va professional tarjimon tarjima qiladi. Tarjimani siz qilmaysiz.</p>""",
             fun="Öqituvçini tanaffusda, qöli bilan jurnal kötarib ketayotganda töxtatib söramaymiz: u ham bir kuni çoy içişi kerak.",
             take="Öqituvçi «özing yozib kel, men imzolayman» desa, rad eting va faktlar varaqasini taklif qiling.",
             task_b="Sörov sanasi va xat",
             task=["Tanlagan tavsiyaçilar uçun sörov sanasini belgilang.", "Yozma sörov xatining asosiy 5 jumlasini yozing."]),
        dict(t=M_TITLES[4][2], short="Varaqa", min=12,
             hook="Öqituvçi sizni yaxşi biladi, lekin hamma narsani eslamaydi. "
                  "Bu darsda unga aniq faktlarni eslatadigan bir sahifali yutuqlar varaqasini ([[Brag Sheet]]) yozamiz.",
             main="""<ol><li>Ism, sinf, soha, universitetlar va muddatlar.</li>
<li>Bitta jumlali profil (M3).</li>
<li>Siz va öqituvçi: qaysi fan, neça yil, qaysi loyiha yoki tanlovda birga işlagansiz.</li>
<li>2–3 epizod: öqituvçi özi körgan voqea, sana yoki dars bilan.</li>
<li>Eng muhim 3–5 yutuq.</li></ol>""",
             take="Varaqaga faqat öqituvçi tasdiqlay oladigan faktni yozing. Xatning matnini u öz sözlari bilan yozadi.",
             task_b="Bitta varaqa",
             task=["Bitta tavsiyaçi uçun yutuqlar varaqasini yozing.", "Öqituvçi özi körgan 2–3 epizodni sanasi bilan kiriting."]),
        dict(t=M_TITLES[4][3], short="Platforma", min=12,
             hook="Common App da uç xil rol bor, UCAS da bitta umumiy tavsiya. Özbekiston maktabining köpida esa «maktab maslahatçisi» lavozimi yöq. "
                  "Bu darsda kim nimani yuborişini kelişib olamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Platforma</th><th>Kim nima yuboradi</th></tr></thead><tbody>
<tr><td>Common App</td><td>Maktab maslahatçisi ([[school counselor]]): maktab hisoboti, maktab profili, transkript. Öqituvçilar: odatda 1–2 ta</td></tr>
<tr><td>UCAS</td><td>Bitta umumiy tavsiya ([[reference]]); maktab ulanmagan bölsa, mustaqil ariza va taşqi tavsiyaçi</td></tr>
<tr><td>Portallar</td><td>Havola yuboriladi yoki imzolangan xat yuklanadi</td></tr>
</tbody></table></div>
<p>Maslahatçi rolini direktor örinbosari yoki sinf rahbari bajaradi. U maktab nomidan rasmiy hujjat yubora olişi kerak.</p>""",
             take="Maslahatçi hisobini özingiz oçib töldirmang: rasmiy hujjatni maktab vakili yuboradi.",
             task_b="Rollar va uçraşuv",
             task=["Har platformangiz uçun kim qaysi rolni bajarişini yozing.", "Maslahatçi bilan uçraşuv sanasi va olib boradigan hujjatlar röyxatini yozing."]),
        dict(t=M_TITLES[4][4], short="Apostil", min=12,
             hook="Notarial nusxa yetarli deb öylaş qimmatga tuşadigan xato bölişi mumkin. Har mamlakat va universitet boşqa tasdiq söraydi. "
                  "Bu darsda har hujjat uçun zanjir tuzamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Tasdiq</th><th>Nima</th></tr></thead><tbody>
<tr><td>Tarjima</td><td>Hujjatning ingliz yoki boşqa tildagi matni</td></tr>
<tr><td>Notarial tasdiq</td><td>Notarius tarjima yoki nusxaning töğriligini tasdiqlaydi</td></tr>
<tr><td>Apostil</td><td>Hujjat boşqa davlatda rasmiy deb tan olinişi uçun davlat tasdiği</td></tr>
</tbody></table></div>
<p>Özbekistonda apostil uçun ariza my.gov.uz orqali yoki Davlat xizmatlari markazida beriladi. Yiğim va muddat gov.uz sahifasida.</p>""",
             take="Har universitet nima söraşini aniqlang va zanjirni muddatdan 8–10 hafta oldin boşlang.",
             task_b="Hujjatlar zanjiri",
             task=["Har asosiy hujjat uçun zanjir yozing: asl, tarjima, notarius yoki apostil, nusxa soni.", "Qaysi universitet nima talab qilişini qavsda körsating."]),
    ])

# ───────────────────────────── M5 ─────────────────────────────
MODULES[5] = dict(
    lead="Bu modulda qaysi universitet qaysi yozma hujjatni söraşini aniqlaysiz, hikoya topasiz va birinçi qoralamani yozasiz. "
         "Keyin uç bosqiçda tahrir qilasiz. Oxirida sizda <strong>yakuniy inşo va tahrir qaydi</strong> böladi.",
    weeks="2–3", pass_time="~2–3 hafta (darslar ~1,5 soat + yoziş)",
    next=("<h2>Keyingi qadam: moliyaviy reja</h2>" + bar(70, "III bosqiç: 1 / 2 modul · Rejangiz 70% tayyor") +
          '<div class="mv-k" data-mn="m5"><b>Inşongiz tayyor.</b> Endi har universitet uçun 4 yillik xarajatni hisoblaş qoladi. '
          "M6 da stipendiyalarni saralaysiz va bitta universitet uçun 4 yillik rejani tuzasiz.</div>"
          "<p>M6.1 dan: <i>Stipendiyaning şartlari oldindan yozilgan. Avval mosligingizni tekşirasiz, keyin vaqt sarflaysiz.</i></p>"
          + row(6, "M6: stipendiya va reja")),
    lessons=[
        dict(t=M_TITLES[5][0], short="Turlar", min=12,
             hook="«Inşo», «şaxsiy bayonot» va «motivatsion xat» köpinça bir narsa deb öylanadi. Har biri boşqa savolga javob beradi. "
                  "Bu darsda turlarni ajratamiz va hammasiga asos bölgan qiziqiş bayonini tuzamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Hujjat</th><th>Asosiy savol</th><th>Qayerda</th></tr></thead><tbody>
<tr><td>Şaxsiy inşo</td><td>Siz qanday odamsiz?</td><td>Common App</td></tr>
<tr><td>Şaxsiy bayonot</td><td>Nega şu fan va qanday tayyorlangansiz?</td><td>UCAS</td></tr>
<tr><td>Motivatsion xat</td><td>Nega şu dastur va şu universitet?</td><td>Yevropa va Osiyo portallari, stipendiyalar</td></tr>
<tr><td>Qöşimça inşo</td><td>Universitetning aniq savoli</td><td>AQŞ universitetlari</td></tr>
</tbody></table></div>
<p><b>Qiziqiş bayoni</b> (1 sahifa, faqat özingiz uçun): aniq savol, uning kelib çiqişi, dalil, universitetdagi keyingi qadam.</p>""",
             take="Bitta matnni hamma platformaga yubormang. Har hujjat öz savoliga javob beradi, lekin hammasi bitta profilga tayanadi.",
             task_b="Yozma hujjatlar xaritasi",
             task=["Har universitet qaysi yozma hujjatni söraşini yozing.", "Keng soha, yönaliş va aniq savol zanjirini yozing."]),
        dict(t=M_TITLES[5][1], short="Mavzu", min=10,
             hook="Common App ning yetti mavzusidan birini tanlaş köp vaqt oladi. Komissiya esa mavzuga emas, hikoyaga qaraydi. "
                  "Bu darsda avval hikoyani, keyin mavzuni topamiz.",
             main="""<ul><li>Yetti mavzu varianti, biri «özingiz tanlagan mavzu».</li>
<li>Hajm: 250–650 söz.</li>
<li>Bitta inşo Common App orqali ariza beradigan hamma universitetga boradi.</li></ul>
<p>Mavzular har yili eʼlon qilinadi: aniq matnni rasmiy sahifadan öqing. Köp kuçli inşo bir neça mavzuga mos keladi.</p>""",
             take="Avval hikoyani toping, keyin unga mos mavzuni tanlang.",
             task_b="Ikki mavzu, ikki hikoya",
             task=["Joriy yil mavzularini rasmiy sahifadan öqing.", "Sizga yaqin 2 mavzuni tanlang va har biriga bitta hikoya ğoyasini yozing."]),
        dict(t=M_TITLES[5][2], short="Qoralama", min=15,
             hook="Eng yaxşi inşo köpinça katta voqeadan emas, kiçik epizoddan boşlanadi: oşxonadagi suhbat, buzilgan velosiped, ukaga tuşuntirilgan masala. "
                  "Bu darsda epizodni topib, birinçi qoralamani yozamiz.",
             main="""<ol><li><b>Epizod:</b> aniq joy, vaqt va harakat, 2–3 jumla.</li>
<li><b>Fikr:</b> öşa payt nima öyladingiz, nima qiyin edi?</li>
<li><b>Özgariş:</b> keyin nima qildingiz?</li>
<li><b>Maʼno:</b> bu siz haqingizda nima deydi?</li></ol>
<div class="tbl"><table><thead><tr><th>Aytiş</th><th>Körsatiş</th></tr></thead><tbody>
<tr><td>Men qatʼiyatliman.</td><td>Dasturim 40-marta xato berganida, xatolarni daftarga yoziş odatini boşladim.</td></tr>
</tbody></table></div>""",
             fun="Birinçi qoralamani heç kim körmaydi, hatto qabul komissiyasi ham. Bemalol yozavering.",
             take="Birinçi qoralamani bir ötirişda, tahrirsiz yozing. 650 sözdan köp çiqsa, keyin qisqartirasiz.",
             task_b="5 epizod va qoralama",
             task=["Hayotingizdan 5 ta kiçik epizodni bir jumladan yozing.", "Eng kuçlisini tanlab, pastdagi vositada birinçi qoralamani yozing."]),
        dict(t=M_TITLES[5][3], short="UCAS", min=12,
             hook="2026 qabulidan UCAS bayonoti uçta savolga javob. Bitta bayonot Buyuk Britaniyadagi hamma tanlovingizga boradi. "
                  "Bu darsda uç savolga dalil yiğamiz.",
             main="""<div class="tbl"><table><thead><tr><th>№</th><th>Savol</th><th>Nima yozasiz</th></tr></thead><tbody>
<tr><td>1</td><td>Nega şu kurs yoki fan?</td><td>Qiziqiş va uning kelib çiqişi</td></tr>
<tr><td>2</td><td>Öqişingiz sizni qanday tayyorladi?</td><td>Fanlar, loyihalar, olimpiadalar</td></tr>
<tr><td>3</td><td>Taʼlimdan taşqari nima qildingiz?</td><td>Faoliyat, iş, mustaqil öqiş (M3)</td></tr>
</tbody></table></div>
<p>Har javob kamida 350 belgi, jami 4 000 belgigaça. Tanlovlaringiz bitta fan atrofida bölsin.</p>""",
             take="UCAS bayonotida qiziqişni dalil bilan körsating: öqigan kitob, qilgan tajriba, yeçgan masala va undan nima örgandingiz.",
             task_b="Uç savolga dalil",
             task=["Har savolga 3 tadan dalil yozing.", "Vositada uç javobning qoralamasini yozing. UK ga ariza bermasangiz, motivatsion xat rejasini yozing."]),
        dict(t=M_TITLES[5][4], short="Qöşimça", min=12,
             hook="«Nega aynan bizning universitet?» savoliga «reytingi yuqori» deb javob beriş eng zaif yöl. "
                  "Bu darsda universitetni örganganingizni körsatadigan faktlarni yiğamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Manba</th><th>Nima topasiz</th></tr></thead><tbody>
<tr><td>Öquv reja</td><td>Aniq fan nomlari va ular sizga nega kerak</td></tr>
<tr><td>Laboratoriya sahifalari</td><td>Bakalavrlar qatnaşa oladigan loyihalar</td></tr>
<tr><td>Talabalar taşkilotlari</td><td>Siz davom ettiradigan faoliyat</td></tr>
</tbody></table></div>
<p><b>Tekşiruv:</b> javobdagi universitet nomini boşqasiga almaştiring. Matn baribir töğri bölsa, u juda umumiy.</p>""",
             take="Har faktni öz sözingiz bilan va özingizga boğlab yozing. Universitet sahifasidan matn köçirmang.",
             task_b="«Nega biz?» uçun 3 fakt",
             task=["Qöşimça inşo savollarini yozing: universitet, savol, söz çegarasi.", "Bitta «Nega biz?» uçun 3 aniq fakt va ularning sizga boğliqligini yozing."]),
        dict(t=M_TITLES[5][5], short="Tahrir", min=12,
             hook="Köp öquvçi tahrirni vergul va imlodan boşlaydi. Keyin butun paragraf öçirilsa, öşa mehnat behuda ketadi. "
                  "Bu darsda tahrirni yirikdan maydaga qilamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Bosqiç</th><th>Savol</th></tr></thead><tbody>
<tr><td>1. Mazmun</td><td>Inşoni bir jumlada ayta olasizmi?</td></tr>
<tr><td>2. Tuzilma</td><td>Har paragraf bitta vazifa bajaradimi?</td></tr>
<tr><td>3. Til</td><td>Ortiqça söz, klişe, xato bormi?</td></tr>
</tbody></table></div>
<p>Klişe bilan boşlamang («Bolaligimdan …»), özingizni maqtamang, mavhum vaʼda bermang. «Juda», «aslida», «har doim» sözlarini olib körib, maʼno özgarmasa, olib taşlang.</p>""",
             take="Har bosqiçni alohida ötişda bajaring va har yirik özgarişdan keyin yangi versiyani saqlang.",
             task_b="Uç bosqiçli tahrir",
             task=["Inşongizni bir jumlada aytib bering va har paragraf vazifasini 3 sözda yozing.", "3 ta klişe yoki ortiqça jumlani topib, aniq harakat bilan qayta yozing."]),
        dict(t=M_TITLES[5][6], short="Yakun", min=15,
             hook="Siz inşongizni juda yaxşi bilasiz, şuning uçun undagi böşliqni körmaysiz. AI esa bir neça soniyada «çiroyli» matn yozadi. "
                  "Bu darsda fikr oliş, AI çegarasi va platformaga joylaşni hal qilamiz.",
             main="""<ul><li><b>Fikr oliş:</b> 1–2 kişiga aniq savol bilan: qaysi 3 narsani eslab qoldingiz, qayerda zerikdingiz?</li>
<li><b>AI:</b> Common App AI yaratgan matnni öz işi sifatida topşirişni firibgarlik deydi. UCAS bayonotlarni öxşaşlikka tekşiradi.</li>
<li><b>Joylaş:</b> matnni avval oddiy matn muharririga köçiring, platforma hisoblagiçi bilan tekşiring, boşqa universitet nomi qolmaganini köring.</li></ul>""",
             take="AI dan savol va tekşiruv uçun foydalanişingiz mumkin, matnni esa özingiz yozasiz. Körib çiqiş sahifasini PDF qilib saqlang.",
             task_b="Yakuniy versiya",
             task=["2 kişiga uçta aniq savol yuboring va qaysi fikrni qabul qilganingizni yozing.", "Özingizning AI qoidangizni 3 bandda yozing va yakuniy matnni joylab, söz sonini yozing."]),
    ])

# ───────────────────────────── M6 ─────────────────────────────
MODULES[6] = dict(
    lead="Bu modulda sizga oçiq stipendiyalarni saralaysiz, universitet yordamini tekşirasiz va töliq xarajatni hisoblaysiz. "
         "Oxirida sizda <strong>4 yillik moliyaviy reja</strong> böladi: har yil uçun xarajat, qoplanadigan qism va böşliq.",
    weeks="1–2", pass_time="~1–2 hafta (darslar ~1,2 soat + hisoblagiç)",
    next=("<h2>III bosqiç yakunlandi: keyingi qadam topşiriş</h2>" + bar(80, "III bosqiç: 2 / 2 modul · Rejangiz 80% tayyor") +
          '<div class="mv-k" data-mn="m6"><b>4 yillik rejangiz tayyor.</b> Endi hujjatlar, inşo va reja bir joyga kelib, ariza topşiriladi. '
          "IV bosqiçda (M7–M8) arizani platformada topşirasiz, intervyuga tayyorlanasiz va jönaşni rejalaştirasiz.</div>"
          "<p>IV bosqiç darslari:</p>" + lock(tl(7) + tl(8)[:2]) + TARIF +
          '<div class="mv-row"><a class="btn btn-p" href="bachelor-lab-o.html?m=7">IV bosqiç: M7 ni oçiş</a><a class="btn btn-g" href="bachelor-lab-narxlar.html">Tariflar</a></div>'),
    lessons=[
        dict(t=M_TITLES[6][0], short="Manbalar", min=10,
             hook="Stipendiyaning şartlari oldindan yozilgan. Şartni öqimasdan ariza beriş vaqtni oladi, öqib beriş imkoniyatni oşiradi. "
                  "Bu darsda uç manbani va olti muvofiqlik şartini ajratamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Manba</th><th>Misol</th></tr></thead><tbody>
<tr><td>Davlat</td><td>GKS, MEXT, CSC, Stipendium Hungaricum, Türkiye Bursları</td></tr>
<tr><td>Universitet</td><td>Ehtiyoj yoki yutuqqa qarab grant</td></tr>
<tr><td>Taşkilot</td><td>Jamğarma, kompaniya</td></tr>
</tbody></table></div>
<p>Muvofiqlik şartlari:</p>
<ol><li>fuqarolik;</li><li>yoş;</li><li>baho;</li><li>til;</li><li>daraja va soha;</li><li>çeklovlar.</li></ol>""",
             take="Avval olti şartni tekşiring. Bittasi bajarilmasa, öşa dasturga vaqt sarflamang.",
             task_b="6–8 stipendiya",
             task=["Sizga qiziq 6–8 stipendiyaning nomini va rasmiy saytini yozing.", "Har biri uçun qaysi şart sizga tösiq bölişi mumkinligini belgilang."]),
        dict(t=M_TITLES[6][1], short="Davlat", min=15,
             hook="Davlat stipendiyalarining köpi öqiş tölovi, oylik nafaqa va til yilini qoplaydi. Kanal va majburiyat esa har birida boşqa. "
                  "Bu darsda ularni bitta jadvalda soliştiramiz.",
             main="""<div class="tbl"><table><thead><tr><th>Dastur</th><th>Kanal</th><th>Eʼtibor bering</th></tr></thead><tbody>
<tr><td>GKS-U (Koreya)</td><td>Elçixona yoki universitet treki</td><td>Tafsilot GKS dasturida</td></tr>
<tr><td>MEXT (Yaponiya)</td><td>Asosan elçixona tavsiyasi, yozma imtihon</td><td>Bir yillik tayyorlov</td></tr>
<tr><td>CSC (Xitoy)</td><td>Elçixona yoki universitet kanali</td><td>Dasturlarning köpi xitoy tilida</td></tr>
<tr><td>Stipendium Hungaricum</td><td>Tempus platformasi, Özbekiston hamkor davlat</td><td>Kvota va muddat har yil eʼlonda</td></tr>
<tr><td>Türkiye Bursları</td><td>Bitta onlayn ariza</td><td>Bir yillik turk tili kursi</td></tr>
<tr><td>Italiya DSU</td><td>Mintaqaviy agentlik</td><td>Ehtiyojga qarab, daromad hujjatlari kerak</td></tr>
</tbody></table></div>""",
             take="Har dasturni muvofiqlik, qoplov, kanal, muddat, raqobat va majburiyat böyiça baholang. Muvofiqlik bajarilmasa, qolgan ball hisobga olinmaydi.",
             task_b="Saralaş jadvali",
             task=["5–8 dasturni olti mezon böyiça baholang.", "Eng mos 3 tasini ustuvor deb belgilang va joriy eʼlon havolasini yozing."]),
        dict(t=M_TITLES[6][2], short="Universitet", min=12,
             hook="Köp universitet xalqaro talabaga çegirma yoki stipendiya beradi, lekin uni topiş uçun dastur sahifasidan çuqurroq qaraş kerak. "
                  "Bu darsda universitet yordamini turi va şarti böyiça tekşiramiz.",
             main="""<div class="tbl"><table><thead><tr><th>Tur</th><th>Qanday</th><th>Nima qilasiz</th></tr></thead><tbody>
<tr><td>Avtomatik</td><td>Qabulda baho yoki test asosida</td><td>Şartini öqing</td></tr>
<tr><td>Ariza bilan</td><td>Alohida forma, inşo, baʼzan intervyu</td><td>Muddatini jadvalga qöşing</td></tr>
<tr><td>Ehtiyojga qarab (AQŞ)</td><td>Ota-ona daromadi hujjatlari bilan</td><td>Formalar va CDS H6: USA dasturida</td></tr>
</tbody></table></div>
<p>Uç savol: bir yillikmi yoki 4 yilga? Keyingi yillarda baho şarti bormi? Summa qatʼiymi yoki foiz?</p>""",
             take="Faqat birinçi yilga beriladigan stipendiya 4 yillik rejada katta böşliq qoldiradi. Davomiylikni albatta tekşiring.",
             task_b="Uç universitet",
             task=["Röyxatingizdagi 3 universitetning xalqaro talabalar stipendiyalarini toping.", "Har biri uçun tur, summa, davomiylik, şart va muddatni yozing."]),
        dict(t=M_TITLES[6][3], short="Xarajat", min=12,
             hook="Öqiş tölovi xarajatning faqat bir qismi. Yaşaş, suğurta, viza va yöl baʼzan öqiş tölovi bilan teng keladi. "
                  "Bu darsda bitta universitet uçun töliq xarajatni qatorlarga ajratamiz.",
             main="""<ol><li>Öqiş tölovi</li><li>Yaşaş: yotoqxona yoki ijara, ovqat, transport</li><li>Tibbiy suğurta</li><li>Viza va tegişli tölovlar</li>
<li>Moliyaviy kafolat, masalan Germaniyada bloklangan hisob</li><li>Aviabilet, yiliga kamida bir marta</li><li>Ariza va hujjatlar (M1)</li>
<li>Yaşirin xarajatlar: kitob, noutbuk, qişki kiyim, depozit</li></ol>
<p>Universitetning rasmiy xarajat sahifasini ([[cost of attendance]]) asos qiling.</p>""",
             take="Hisobni asl valyutada yuriting va 10–15 foiz zaxira qöşing.",
             task_b="8 qatorli xarajat",
             task=["Bitta universitet uçun 8 qator böyiça yillik xarajatni yozing.", "Har qatorga manba havolasini qöşing."]),
        dict(t=M_TITLES[6][4], short="4 yil", min=12,
             hook="Birinçi yilni qoplaş yetarli emas. Ikkinçi yilda mablağ tugasa, öqiş töxtaydi va viza ham xavf ostida qoladi. "
                  "Bu darsda 4 yillik jadvalni hisoblagiç bilan tuzamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Yil</th><th>Xarajat</th><th>Stipendiya yoki grant</th><th>Oila hissasi</th><th>Böşliq</th></tr></thead><tbody>
<tr><td>1</td><td>…</td><td>…</td><td>…</td><td>…</td></tr>
<tr><td>2</td><td colspan="4">öqiş tölovining yillik öşişini hisobga oling</td></tr>
<tr><td>3–4</td><td colspan="4">stipendiyaning baho şarti saqlanişini rejalang</td></tr>
</tbody></table></div>
<p>Talaba işini asosiy manba qilmang: viza qoidalari haftalik soatni çeklaydi. Valyuta kursi 20 foiz özgarsa, reja qanday özgarişini hisoblang.</p>""",
             take="Reja böşliği 0 dan katta yil bilan tugasa, bu universitet hozirça real variant hisoblanmaydi. Buni ota-onangiz bilan oçiq gaplaşing.",
             task_b="Sizning 4 yilingiz",
             task=["Eng ehtimolli universitetingiz uçun 4 yillik jadvalni hisoblagiçda töldiring.", "Kurs 20 foiz oşganda böşliq qanday özgarişini yozing."]),
        dict(t=M_TITLES[6][5], short="Himoya", min=8,
             hook="Xorijda öqiş atrofida firibgarlik köp: soxta stipendiya, «kafolatli qabul», oldindan tölov söraydigan agent. "
                  "Bu darsda belgilarni va tölovdan oldingi qoidalarni yozamiz.",
             main="""<ul><li>«Stipendiya kafolatlanadi» yoki «qabul 100 foiz».</li>
<li>Stipendiya uçun oldindan tölov: «rasmiylaştiriş tölovi».</li>
<li>Universitet nomidan oddiy poçta manzili.</li>
<li>Şoşiriş: «bugun tölamasangiz, joy ketadi».</li>
<li>Siz ariza bermagan stipendiyani «yutganingiz» haqida xabar.</li></ul>
<p>Rasmiy saytni özingiz qidirib oçing. Mablağni faqat universitetning rasmiy tölov tizimiga ötkazing, şaxsiy kartaga ötkazmang.</p>""",
             take="Kafolat, oldindan tölov, norasmiy email va şoşiriş: bittasini körsangiz, tölovni töxtatib, rasmiy manzil orqali tekşiring.",
             task_b="Tölovdan oldingi 3 qoida",
             task=["Belgilarni ota-onangiz bilan körib çiqing.", "«Tölovdan oldin» degan 3 qoidali röyxat yozing."]),
    ])

# ───────────────────────────── M7 ─────────────────────────────
MODULES[7] = dict(
    lead="Bu modulda arizani platformada töldirasiz, mamlakat yölingizning bosqiçlarini yozasiz va 40 bandli röyxat bilan tekşirib topşirasiz. "
         "Oxirida sizda <strong>kamida bitta topşirilgan ariza va arizalar jurnali</strong> böladi.",
    weeks="1–2", pass_time="~1–2 hafta (darslar ~1 soat + topşiriş)",
    next=("<h2>Keyingi qadam: intervyu va jönaş</h2>" + bar(90, "IV bosqiç: 1 / 2 modul · Rejangiz 90% tayyor") +
          '<div class="mv-k" data-mn="m7"><b>Arizangiz topşirildi.</b> Endi javob kutiladi, baʼzi universitetlar esa intervyuga çaqiradi. '
          "M8 da intervyuga tayyorlanasiz, natijalar uçun qaror jadvalini tuzasiz va jönaşni rejalaştirasiz.</div>"
          "<p>M8.1 dan: <i>«Özingiz haqingizda gapirib bering» deyarli har intervyuning birinçi savoli.</i></p>"
          + row(8, "M8: intervyu va jönaş")),
    lessons=[
        dict(t=M_TITLES[7][0], short="Common App", min=12,
             hook="Common App bitta arizani köp AQŞ universitetiga yuboriş imkonini beradi. Har universitet esa öz qöşimça talabini qöşadi. "
                  "Bu darsda bölimlarni birma-bir töldiramiz.",
             main="""<div class="tbl"><table><thead><tr><th>Bölim</th><th>Nima</th></tr></thead><tbody>
<tr><td>Profile, Family</td><td>Şaxsiy maʼlumot, oila, fuqarolik</td></tr>
<tr><td>Education</td><td>Maktab, baholar; maktab bazada bölmasa, qölda qöşiladi</td></tr>
<tr><td>Testing</td><td>Natijalarni özingiz kiritasiz</td></tr>
<tr><td>Activities</td><td>10 tagaça faoliyat (M3)</td></tr>
<tr><td>Writing</td><td>Asosiy inşo (M5) va qöşimça maʼlumot ([[Additional Information]])</td></tr>
<tr><td>Recommenders</td><td>Maslahatçi va öqituvçilar (M4)</td></tr>
</tbody></table></div>""",
             take="Tölovdan ozod qilişni universitetning özidan söring. Additional Information da kontekstni qisqa yozing: baholaş şkalasi, maktab imkoniyatlari.",
             task_b="Hisobingiz holati",
             task=["Common App hisobingizni oçing va har bölim holatini yozing.", "Additional Information uçun 3 jumlalik kontekst qoralamasini yozing."]),
        dict(t=M_TITLES[7][1], short="UCAS", min=10,
             hook="UCAS orqali bitta ariza bilan Buyuk Britaniyadagi bir neça universitetga ariza berasiz. Bayonot ham, tavsiya ham hamma tanlovga bir xil boradi. "
                  "Bu darsda UCAS arizasini tuzamiz.",
             main="""<ul><li><b>Tanlovlar:</b> odatda 5 tagaça kurs.</li>
<li><b>Bayonot:</b> uç savol (M5).</li>
<li><b>Tavsiya:</b> bitta umumiy (M4); maktab ulanmagan bölsa, mustaqil ariza.</li>
<li><b>Başorat qilingan natija</b> ([[predicted grades]]): odatda tavsiyaçi beradi.</li>
<li><b>Tölov:</b> bitta ariza tölovi, miqdori har yili eʼlon qilinadi.</li></ul>""",
             take="5 tanlov bitta fan atrofida bölsin: 3 ta informatika va 2 ta fizika bayonotni zaiflaştiradi.",
             task_b="UK tanlovlaringiz",
             task=["5 tagaça tanlovingizni yozing va ular bitta fan atrofida ekanini tekşiring.", "Tavsiya va başorat qilingan natijani kim berişini yozing."]),
        dict(t=M_TITLES[7][2], short="Portallar", min=10,
             hook="Germaniya, Italiya, Xitoy va köp Osiyo universitetida yagona platforma yöq. Har portalning öz hisobi, formati va muddati bor. "
                  "Bu darsda portallar bilan xatosiz işlaşni örganamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Portal</th><th>Qayerda</th><th>Eʼtibor bering</th></tr></thead><tbody>
<tr><td>uni-assist</td><td>Germaniyaning köp universiteti</td><td>Hujjatlarni tekşiradi, tölovli</td></tr>
<tr><td>Universitaly</td><td>Italiya</td><td>Viza uçun oldindan röyxatdan ötiş</td></tr>
<tr><td>CSC va universitet portali</td><td>Xitoy</td><td>Ariza ikki joyda bölişi mumkin</td></tr>
<tr><td>Universitet portali</td><td>Koreya, Turkiya, Singapur va boşqalar</td><td>Har birida alohida hisob</td></tr>
</tbody></table></div>""",
             take="Login va parolni xavfsiz joyda saqlang, hisob email ini har kuni tekşiring va yöriqnomani oxirigaça öqing.",
             task_b="Portallaringiz",
             task=["Har portal uçun yozing: hisob oçilganmi, email, fayl talablari.", "Eng murakkab portalning yöriqnomasidan 5 ta talabni yozing."]),
        dict(t=M_TITLES[7][3], short="Mamlakat yöli", min=15,
             hook="Xitoy, Italiya va Singapurda ariza tartibi AQŞ va UK dan farq qiladi. Bitta mamlakatni tanlasangiz, qolganini öqiş şart emas. "
                  "Bu darsda yölingizni tanlab, bosqiçlarini yozamiz.",
             main="""<div class="tbl"><table><thead><tr><th></th><th>Xitoy</th><th>Italiya</th><th>Singapur (NUS, NTU)</th></tr></thead><tbody>
<tr><td>Til</td><td>Köpinça xitoy; ingliz dasturi çeklangan</td><td>Ingliz tilidagi bakalavr kam</td><td>Ingliz</td></tr>
<tr><td>Kiriş</td><td>Universitet portali, stipendiya bölsa CSC</td><td>12 yillik taʼlim, TOLC yoki universitet testi</td><td>Mamlakat böyiça talablar, juda tanlovli</td></tr>
<tr><td>Yozma qism</td><td>Öqiş rejasi ([[Study Plan]])</td><td>Motivatsion xat</td><td>Qisqa inşolar</td></tr>
<tr><td>Viza</td><td>JW201/JW202, keyin X1</td><td>Universitaly, keyin D turi</td><td>Universitet orqali</td></tr>
<tr><td>Xarajat</td><td>CSC stipendiyasi</td><td>Daromadga qarab tölov, DSU</td><td>Tuition Grant: bitiruvdan keyin Singapurda işlaş majburiyati</td></tr>
</tbody></table></div>""",
             take="Yölni sohangizdagi kuçli dastur va uning tili böyiça tanlang, keyin bosqiçlarni rasmiy sahifadagi sanalar bilan yozing.",
             task_b="Sizning yölingiz",
             task=["Uç yönalişdan birini tanlang va sababini yozing (yöq bölsa, bu darsni ötkazib yuboring).", "Tanlangan yöl uçun 5 bosqiçli rejani sanalar bilan yozing."]),
        dict(t=M_TITLES[7][4], short="Topşiriş", min=12,
             hook="Uçuvçi tajribasi qança bölsa ham, har parvozdan oldin nazorat röyxatini öqiydi. Arizada ham şunday: çarçagan köz xatoni körmaydi. "
                  "Bu darsda fayllarni tayyorlab, 40 bandli röyxat bilan topşiramiz.",
             main="""<ul><li><b>Format:</b> odatda PDF, skaner aniq, sahifalar tartibda.</li>
<li><b>Nom:</b> Familiya_Ism_Hujjat.pdf, böş joysiz.</li>
<li><b>Topşirgandan keyin:</b> tasdiq xati va tölov kvitansiyasini saqlang.</li>
<li><b>Holat:</b> 3–7 kun içida hujjatlar «qabul qilindi» bölişi kerak.</li></ul>
<p>Pastdagi 40 bandni har arizadan oldin ketma-ket tekşiring. Bitta band «yöq» bölsa, avval tuzating.</p>""",
             take="Muddatdan kamida 3–5 kun oldin topşiring: oxirgi kuni platforma sekinlaşadi.",
             task_b="Bitta topşirilgan ariza",
             task=["Bitta arizani 40 bandli röyxat böyiça tekşirib topşiring.", "Tasdiq sanasi, hujjatlar holati va topilgan xatolarni yozing."]),
    ])

# ───────────────────────────── M8 ─────────────────────────────
MODULES[8] = dict(
    lead="Bu modulda intervyuga tayyorlanasiz, natijalar uçun qaror jadvalini tuzasiz va qabul xatidan jönaşgaça bölgan qadamlarni yozasiz. "
         "Oxirida sizda <strong>3 ta yozib olingan javob, qaror jadvali va jönaş röyxati</strong> böladi.",
    weeks="2", pass_time="~2 hafta (darslar ~1,2 soat + yozuvlar)",
    next=("<h2>Bakalavr dasturi yakunlandi</h2>" + bar(100, "IV bosqiç: 2 / 2 modul · Rejangiz 100% tayyor") +
          '<div class="mv-k" data-mn="m8"><b>Sizda töliq ariza paketi bor:</b> saralangan röyxat, vaqt jadvali, faoliyatlar va CV, tavsiya varaqasi, inşo, 4 yillik reja, topşirilgan ariza va jönaş röyxati.</div>'
          "<p>Javoblaringiz hisobingizda saqlanadi: keyingi yil yangi muddatlar bilan qaytib kelişingiz mumkin.</p>"
          '<div class="mv-row"><a class="btn btn-p" href="dashboard.html">Mening kabinetim</a><a class="btn btn-g" href="index.html#labs">Boşqa dasturlar</a></div>'),
    lessons=[
        dict(t=M_TITLES[8][0], short="Intervyu", min=12,
             hook="Bitiruvçi bilan suhbat va akademik intervyu butunlay boşqa narsa. Biri sizni taniş uçun, ikkinçisi qanday fikrlaşingizni köriş uçun. "
                  "Bu darsda turlarni ajratib, birinçi savolga 3 daqiqalik javob tuzamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Tur</th><th>Maqsad</th></tr></thead><tbody>
<tr><td>Bitiruvçi bilan suhbat ([[alumni interview]])</td><td>Sizni taniş; qarorga taʼsiri köpinça kiçik</td></tr>
<tr><td>Akademik intervyu</td><td>Fan böyiça fikrlaş, yangi masala</td></tr>
<tr><td>Stipendiya intervyusi</td><td>Motivatsiya, reja, moslik</td></tr>
</tbody></table></div>
<p><b>«Özingiz haqingizda»:</b> hozir (30 soniya), ötmiş (90 soniya: 1–2 epizod), kelajak (60 soniya: nega şu dastur).</p>""",
             fun="Kamera ostidan qarab gapirsak, intervyuçi faqat şiftimizni körib qoladi. Kamerani köz darajasiga qöyamiz.",
             take="Javobda röyxat emas, bitta yönaliş va dalil bölsin. Tuzilmani yodlang, jumlani har safar yangidan tuzing.",
             task_b="Intervyu va 3 daqiqa",
             task=["Arizalaringizda qaysi intervyu turlari kutilişini yozing.", "3 daqiqalik javobni telefonga yozib oling va har qism neça soniya olganini yozing."]),
        dict(t=M_TITLES[8][1], short="Akademik", min=12,
             hook="Akademik intervyuda sizga heç qaçon körmagan masala beriladi. Intervyuçi fikrlaş yölingizni eşitmoqçi. "
                  "Bu darsda masalani ovoz çiqarib, qadamma-qadam yeçişni maşq qilamiz.",
             main="""<ol><li>Savolni qayta ayting.</li><li>Maʼlum va berilganni ajrating.</li><li>Oddiy holatdan boşlang: kiçik son, çizma.</li>
<li>Har qadamni ayting: «Avval … ni köraman, çunki …».</li><li>Xatoni tan oling va qayta köring.</li><li>Intervyuçi yönaltirsa, maslahatni işlating.</li></ol>""",
             take="Bilmasangiz, töqimang: «Buni bilmayman, lekin şunday öylayman …» deb taxminingizni asoslang.",
             task_b="Bitta masala ovoz bilan",
             task=["Sohangiz böyiça bitta yangi masalani ovoz çiqarib yeçib, yozib oling.", "Qaysi qadamda töxtaganingizni va nima yordam berganini yozing."]),
        dict(t=M_TITLES[8][2], short="Mezon", min=12,
             hook="Öz ovozingizni yozuvda eşitiş noqulay, lekin intervyuga tayyorlanişning eng tez yöli. "
                  "Bu darsda yozuvni 8 bandli mezon bilan baholaymiz.",
             main="""<p>Har band 0–2 ball, jami 16:</p>
<ol><li>tuzilma;</li><li>aniq dalil;</li><li>savolga javob;</li><li>vaqt;</li><li>til aniqligi;</li><li>tezlik va pauza;</li><li>köz va kamera;</li><li>halollik va işonç.</li></ol>
<p>Yozib oling, ertasi kuni baholang, eng past 2 bandni tuzatib qayta yozing.</p>""",
             take="Ikki uriniş balini soliştiring. Yozuvni faqat işonçli bir kişiga körsating.",
             task_b="3 ta javob",
             task=["Uç javobni yozib oling: özingiz haqingizda, akademik masala, «nega şu dastur».", "Pastdagi vositada mezon ballarini kiriting."]),
        dict(t=M_TITLES[8][3], short="Natijalar", min=12,
             hook="Natijalar kelganda his-tuyğu kuçli böladi. Oldindan tuzilgan qaror jadvali sizni şoşilinç va qimmat xatodan saqlaydi. "
                  "Bu darsda qabul, rad va kutiş röyxati uçun reja tuzamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Natija</th><th>Nima qilasiz</th></tr></thead><tbody>
<tr><td>Bir neça qabul</td><td>4 yillik xarajat, dastur, viza talablari va javob muddatini soliştiring</td></tr>
<tr><td>UCAS takliflari</td><td>Asosiy ([[firm]]) va zaxira ([[insurance]]) tanlovni belgilaysiz</td></tr>
<tr><td>Kutiş röyxati</td><td>Ruxsat bölsa, qisqa xat yuboring; boşqa taklifni ham qabul qiling</td></tr>
<tr><td>Rad</td><td>Zaxira rejaga ötasiz</td></tr>
</tbody></table></div>
<p>AQŞda bir neça universitetga depozit tölaş ([[double deposit]]) odatda qoidaga zid.</p>""",
             take="Qaror mezonlarini va ularning uluşini natijalardan oldin yozing.",
             task_b="Qaror jadvali",
             task=["Qaror jadvali uçun mezonlaringizni va ularning uluşini yozing.", "Rad javobi kelsa, zaxira rejangizni 3 qadamda yozing."]),
        dict(t=M_TITLES[8][4], short="Viza", min=15,
             hook="Qabul xatidagi bitta jumla, masalan javob muddati yoki şart, keyingi hamma bosqiçni belgilaydi. Viza qarorini esa konsullik çiqaradi. "
                  "Bu darsda xatni röyxatga aylantirib, viza bosqiçlarini yozamiz.",
             main="""<ol><li><b>Qabul turi:</b> şartli yoki şartsiz; şart nima?</li>
<li><b>Javob muddati</b> va <b>depozit</b>.</li>
<li><b>Viza hujjati:</b> AQŞ I-20, UK CAS, Germaniya [[Zulassungsbescheid]], Xitoy JW201/JW202.</li>
<li><b>Viza:</b> rasmiy tölovlar, onlayn forma, moliyaviy imkoniyat dalili, biometrika, baʼzan intervyu va tibbiy talab.</li></ol>
<p>18 yoşga tölmagan abituriyent uçun qöşimça hujjatlar bölişi mumkin.</p>""",
             take="Birinçi 2 hafta içida javob bering, depozitni rasmiy kanal orqali tölang va viza hujjati uçun talablarni bajaring.",
             task_b="Xat va viza bosqiçlari",
             task=["Qabul xatingizdan (yoki namunadan) 4 bandni ajratib yozing.", "Mamlakatingiz böyiça viza bosqiçlarini rasmiy sahifadan sanalar bilan yozing."]),
        dict(t=M_TITLES[8][5], short="Jönaş", min=15,
             hook="Jönaşdan oldingi oy tez ötadi, birinçi semestr esa köp talaba uçun eng qiyin davr. "
                  "Bu darsda uy, suğurta, 30 kunlik röyxat va birinçi yil rejasini tuzamiz.",
             main="""<ul><li><b>Uy-joy:</b> birinçi yil uçun universitet yotoqxonasi eng xavfsiz; ijarada uyni körmasdan tölamang.</li>
<li><b>Suğurta:</b> köp mamlakatda talaba vizasi uçun majburiy.</li>
<li><b>30 kun:</b> hujjatlar (asl va skan), dori va retsept, karta va birinçi oy xarajati, aloqa, birinçi kun yöli.</li>
<li><b>Birinçi yil:</b> mustaqil öqiş, akademik halollik, yordam xizmatlari (xalqaro ofis, yozuv markazi, maslahat xizmati).</li></ul>""",
             fun="Adapterni unutib, birinçi keça telefonni quvvatlay olmay qolganlarning klubi bor. Biz unga aʼzo bölmaymiz.",
             take="Asl hujjatlar qöl yukida, skan nusxalar bulutda tursin. Öqiyotgan mamlakatdagi Özbekiston elçixonasi aloqasini yozib qöying.",
             task_b="Jönaş röyxati",
             task=["Jönaş sanasidan orqaga 4 haftaga işlarni taqsimlang.", "Universitetingizning 5 ta yordam xizmatini va birinçi semestr uçun 3 ta maqsadni yozing."]),
    ])
