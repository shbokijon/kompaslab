from common import LEEDS, UKRIEXP, DORA, HOL, STD

MOD = dict(
    title="Ilmiy rahbar va laboratoriya bilan aloqa",
    desc="PhD Lab M3: ilmiy rahbar topish, moslik matritsasi, professorga dastlabki xat, ilovalar, qayta yozish odobi, birinchi suhbat va qo'llab-quvvatlash tizimi. Natija: 6 ta rahbar moslik kartasi va aloqalar jurnali.",
    lead="Mos ilmiy rahbar mashhur olim emas, aynan sizning ishingizni boshqara oladigan odam. Bu modulda rahbarlarni dalil bilan tanlaysiz, ularga aniq va qisqa xat yozasiz va suhbatga tayyorlanasiz.",
    hero="master", weeks="2–3", next="M4 Ilmiy loyiha taklifi va metodologiya", next_href="phd-lab-o.html?m=4",
    goals=[("telescope", "6 ta rahbar moslik kartasi", "har biri 2 ta real ilmiy dalil bilan"),
           ("memo", "Aloqalar jurnali", "sana, holat, qayta yozish va javob"),
           ("bulb", "Suhbat rejasi", "90 soniyalik bayon va 6 ta savol")],
    warn="Professorga dastlabki xat (Cold email) yozishning umumiy texnikasi Master Lab da. Bu modul faqat PhD rahbari bilan moslik, uning bo'sh o'rni va ilmiy muhitga oid qatlamni o'rgatadi. Namunalar Kompas tuzgan tuzilma: tayyor xat emas.",
    lessons=[
        dict(t="Ilmiy rahbar topish usullari", short="Qidiruv", min=30, kind="🔎 Qidiruv", ic="telescope",
             hook="Birinchi qadamda 100 ta xat emas, dalilli qisqa ro'yxat kerak. Mos rahbar aynan sizning savolingizni boshqara oladigan odam.",
             body=f"""<h4>Qidiruv manbalari</h4>
<ul><li>Kafedra professorlari sahifalari.</li><li>So'nggi grantlar va laboratoriya loyihalari.</li><li>Birinchi yoki oxirgi muallif bo'lgan maqolalar.</li><li>Bo'sh o'rin va e'lon qilingan loyihalar.</li></ul>
<p>Rahbarning usul bo'yicha tajribasi, ma'lumotga kirishi, yangi doktorant olish imkoniyati va ikkinchi rahbar imkoniyatini o'rganing.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz moslik: “Siz dunyodagi eng buyuk olimsiz.” Kuchli moslik: “Sizning 2025-yilgi X usuldagi maqolangizdagi Y cheklov men taklif qilayotgan savolga bog'liq.” Faqat haqiqiy bibliografik ma'lumot yozing.</div>
<div class="box warn">Professor javob bermasligi qobiliyatingiz haqidagi yakuniy baho emas.</div>""",
             take="12 ta nom toping, 6 tasiga moslik kartasi yozing; har biri uchun “yangi doktorant oladimi?” savolini tekshiring.",
             task="<ul><li>12 ta nom toping.</li><li>6 tasiga moslik kartasi yozing.</li><li>Qaysi guruh ochiq loyiha olishini tekshiring.</li></ul><p><b>O'zingizga savol:</b> savolingizga uning qaysi maqolasi bevosita aloqador?</p>",
             ph="1) Prof. ..., ... universiteti — maqola: ... (yil, DOI); ochiq o'rin: ..."),
        dict(t="Rahbar moslik matritsasi", short="Matritsa", min=25, kind="📊 Baholash", ic="chart",
             hook="Moslikni “yoqdi” hissidan dalilga o'tkazing. Ball faqat boshlang'ich saralash, odam haqida hukm emas.",
             body=f"""<h4>5 mezon (har biri 0–2 ball)</h4>
<ol><li>Mavzu mosligi.</li><li>Usul mosligi.</li><li>Rahbarning bo'sh o'rni.</li><li>Moliya aniqligi.</li><li>Laboratoriya muhiti va ikkinchi rahbar imkoniyati.</li></ol>
<p>Ma'lumot yo'q bo'lsa, 0 emas, “noma'lum” yozing: bu savol berish kerakligini ko'rsatadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> “Maqolalar 2/2, moliya noma'lum” yomon belgi emas: xatda nima so'rashni ko'rsatadi.</div>
<div class="box warn">Ballni odamga nisbatan qat'iy haqiqatga aylantirmang.</div>
<div class="srcs">Manba: {DORA}. {HOL}.</div>""",
             take="Matritsa “nimani bilmayman” degan ro'yxatni beradi; xat va suhbat shu bo'shliqlarni yopadi.",
             task="<ul><li>6 ta rahbarni 5 mezon bo'yicha solishtiring.</li><li>Har biri uchun noma'lum bandni yozing.</li><li>3 ta ustuvorni ajrating.</li></ul><p><b>O'zingizga savol:</b> professor “doktorant olaman” deb shaxsan tasdiqlaganmi?</p>",
             ph="Prof. ...: mavzu 2, usul 1, o'rin ?, moliya ?, muhit 2 ; Noma'lum: ..."),
        dict(t="Birinchi xat tuzilmasi", short="Xat", min=35, kind="✉️ Xat", ic="memo",
             hook="Xatning vazifasi o'zingizni maqtash emas, aniq akademik aloqani boshlash. Professor uni bir necha soniyada o'qiydi.",
             body=f"""<h4>Tuzilma</h4>
<ul><li><b>Mavzu qatori</b>: [[PhD enquiry]] va ilmiy yo'nalish.</li><li><b>Kim va nega aynan shu laboratoriya</b>.</li><li><b>Aniq ilmiy bog'liqlik</b>: uning bitta ishi va sizning savolingiz.</li><li><b>Tegishli tajriba</b>: 1–2 jumla, dalil bilan.</li><li><b>Aniq so'rov</b>: ochiq o'rin bormi, ariza yo'li qanday.</li><li><b>Ilova</b>: CV yoki qisqa bayon, agar so'ralgan bo'lsa.</li></ul>
<p>Universitet ko'rsatmasini tekshiring: e'lon qilingan loyihada ba'zan rahbarga oldindan yozish talab qilinmaydi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: <span lang="en">“Please accept me to your university, I am highly motivated.”</span> Kuchliroq tuzilma: bitta real ish → bitta aniq savol → tegishli tajriba → mavjud imkoniyat haqida savol.</div>
<div class="box warn">Sun'iy intellekt yordamida soxta maqola xulosasi yoki laboratoriya bilan aloqa to'qimang.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Qisqa xat: bitta real ish, bitta aniq savol, bitta dalil va bitta aniq so'rov.",
             quiz=[("Professorning norasmiy ijobiy javobi qabul yoki moliya tasdig'i hisoblanadi.", "n", "Noto'g'ri: rasmiy taklif va moliya hujjati alohida keladi."),
                   ("E'lon qilingan loyihada rahbarga oldindan yozish har doim majburiy.", "n", "Noto'g'ri: ba'zi e'lonlarda bu talab qilinmaydi; e'lon ko'rsatmasini o'qing."),
                   ("Moslik matritsasida ma'lumot yo'q bo'lsa, “noma'lum” yoziladi.", "t", "To'g'ri: 0 ball emas, savol berish kerakligi belgisi."),
                   ("Javob bo'lmasa, bir marta qisqa qayta yozish mumkin.", "t", "To'g'ri: keyin boshqa mos yo'llarni davom ettiring.")],
             task="<ul><li>Professorning bitta tegishli ishini tanlang.</li><li>5 jumlalik xat qoralamasini yozing.</li><li>Faqat tekshirilgan fakt bilan yuboring.</li></ul><p><b>O'zingizga savol:</b> xatda shu professorga xos bitta dalil bormi?</p>",
             ph="Mavzu: PhD enquiry — ... ; 1) ... 2) ... 3) ... 4) ... 5) ..."),
        dict(t="Portfolio va ilovalar", short="Ilova", min=25, kind="📎 Hujjat", ic="books",
             hook="Rahbar siz haqingizdagi dalilni tez topa olishi kerak. 30 betlik “yutuqlar to'plami” buni qiyinlashtiradi.",
             body=f"""<ul><li>Akademik CV (2 bet atrofida).</li><li>1–2 betlik tadqiqot bayoni (M1).</li><li>Ishchi maqola, kod omborxonasi, poster yoki ma'lumot namoyishi, agar mos bo'lsa.</li></ul>
<p>Havolaning ochiqligi va ruxsatlarini tekshiring. PDF nomi tartibli, sahifalar o'qiladigan, hajm oqilona bo'lsin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchsiz: 30 betlik “Mening yutuqlarim”. Kuchliroq: 2 betlik CV va qisqa bayon, unda qaysi usulni o'zingiz bajarganingiz aniq.</div>
<div class="box warn">Keraksiz shaxsiy ma'lumot, pasport nusxasi va hali e'lon qilinmagan maxfiy natijalarni yubormang.</div>""",
             take="Ilovalar kam, aniq va tekshiriladigan: CV, bayon va bitta ochiq dalil.",
             task="<ul><li>2 betlik CV ni qayta ko'rib chiqing.</li><li>Portfolio uchun 3 ta dalil tanlang.</li><li>Fayllarga versiya va sana belgilang.</li></ul><p><b>O'zingizga savol:</b> 60 soniyada qaysi usul bo'yicha kuchli ekaningizni kim aniqlay oladi?</p>",
             ph="CV_v3_2026-11.pdf ; Dalil 1: ... (havola) ; 2: ... ; 3: ..."),
        dict(t="Qayta yozish va muloqot odobi", short="Odob", min=20, kind="🤝 Muloqot", ic="bell",
             hook="Takroriy xat va bosim akademik aloqaga zarar yetkazadi. Professor vaqti cheklangan, bu shaxsiy munosabat emas.",
             body=f"""<p>Universitetning yozishma siyosatiga amal qiling. Birinchi xatdan keyin oqilona muddat kuting, keyin bir marta qisqa qayta xat ([[follow-up]]) yozish mumkin. Javob bo'lmasa, boshqa mos yo'llarni davom ettiring.</p>
<p>Rad javobi va “bo'sh o'rin yo'q” — haqorat emas, tashkiliy signal.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Qo'pol: <span lang="en">“Dear Professor, why don't you answer?”</span> Professional: <span lang="en">“Thank you for considering my enquiry; I understand if no openings are available.”</span></div>
<div class="box warn">Bir xil xatni bir nechta professorga CC bilan yubormang.</div>""",
             take="Bitta xat, bitta qayta xat, keyin boshqa yo'l: barchasi aloqalar jurnalida sana bilan.",
             task="<ul><li>Aloqa sanasini jurnalga yozing.</li><li>Qayta xat sababini tekshiring.</li><li>Javobga mos holat belgilang.</li></ul><p><b>O'zingizga savol:</b> bu xatdan professor qanday aniqlik oladi?</p>",
             ph="Prof. ...: xat ..., qayta xat ..., holat: javob kutilmoqda / suhbat / o'rin yo'q"),
        dict(t="Rahbar bilan suhbat", short="Suhbat", min=30, kind="🎙 Suhbat", ic="miya",
             hook="Birinchi 20 daqiqalik suhbat rasmiy intervyu bo'lmasligi mumkin, lekin unda moslik va bajarilishi mumkinlik aniqlanadi.",
             body=f"""<h4>Tayyorlanadi</h4>
<ul><li>Mavzuning 90 soniyalik bayoni.</li><li>Tegishli dalil.</li><li>2 ta ilmiy savol.</li><li>Qo'llab-quvvatlash va moliya haqida 3 ta savol.</li></ul>
<p>Savollar namunasi: <span lang="en">“How many students do you supervise?”</span>, <span lang="en">“How is feedback structured?”</span>, <span lang="en">“What happens if the project scope changes?”</span> Suhbatdan keyin qisqa xulosa xati kelishuvni aniq qiladi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Professor savolingizdan ko'ra ma'lumot borligi bilan ko'proq qiziqsa, bu usul xavfi signali. Bayonni yangilang.</div>
<div class="box warn">Professorning norasmiy ijobiy javobi rasmiy taklif yoki moliya tasdig'i emas.</div>""",
             take="Suhbatga 90 soniyalik bayon va 6 ta savol bilan kiring; keyin yozma xulosa yuboring.",
             task="<ul><li>90 soniyalik bayonni mashq qiling.</li><li>6 ta savolni ustuvorlik bo'yicha tartiblang.</li><li>Suhbatdan keyin qaror jurnaliga yozing.</li></ul><p><b>O'zingizga savol:</b> suhbatdan keyin qaysi farazlaringiz o'zgardi?</p>",
             ph="Bayon: ... ; Savollar: 1) ... 2) ... ; Suhbatdan keyin: ..."),
        dict(t="Ikkinchi rahbar va qo'llab-quvvatlash", short="Tizim", min=20, kind="🧭 Muhit", ic="shield",
             hook="Ilmiy muvaffaqiyat ko'pincha bitta rahbardan tashqari muhitga bog'liq. Muammo chiqqanda kimga borishni oldindan bilish kerak.",
             body=f"""<p>Ikkinchi rahbar, mentorlar, trening rejasi, fikr berish chastotasi, shikoyat kanallari va ko'nikma rivoji institut qoidalarida yoziladi. UKRI ning doktorlik ta'limi bo'yicha kutilmalar bayoni ([[Statement of Expectations]]) talabalar, rahbarlar va tashkilotlar uchun asosiy tamoyillarni belgilaydi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Kuchli rahbar, lekin dala ishiga kirish yo'q: qo'shimcha rahbar yoki sanoat hamkori kerak bo'lishi mumkin.</div>
<div class="box warn">Faqat rahbarning og'zaki va'dasiga tayanib, rasmiy trening shartlarini o'qimaslik xavfli.</div>
<div class="srcs">Manba: {UKRIEXP}. {HOL}.</div>""",
             take="Jamoa sxemasi: rahbar, ikkinchi rahbar, talaba xizmatlari va muammo chiqqandagi kanal.",
             task="<ul><li>Potensial jamoani sxemaga joylang.</li><li>Talabalarni qo'llab-quvvatlash kanallarini toping.</li><li>Hal bo'lmagan 2 ta xavfni yozing.</li></ul><p><b>O'zingizga savol:</b> muammo chiqqanda kimga murojaat qilishni bilasizmi?</p>",
             ph="Rahbar: ... ; ikkinchi rahbar: ... ; xizmatlar: ... ; xavflar: 1) ... 2) ..."),
    ],
    tool=dict(id="jurnal", short="Jurnal", h2="Aloqalar jurnali", sub="Professor, moslik dalili, holat va qayta yozish sanasini bir joyda yuriting.",
              h3="Rahbar kartasi va jurnal", tag="6 maydon", ic="memo", btn="Jurnalni saqlash", badge="Aloqachi", min=5,
              fields=[dict(k="prof", label="Professor va universitet", ph="Prof. ..., ... universiteti, kafedra ..."),
                      dict(k="fit", label="2 ta ilmiy moslik dalili", type="area", ph="1) Maqola ... (yil, DOI) — ... ; 2) Loyiha ..."),
                      dict(k="sorov", label="Xatdagi aniq so'rov", type="area", ph="20..-yil uchun doktorant oladimi; ariza yo'li ..."),
                      dict(k="holat", label="Holat", type="select", opts=["Xat yozilmagan", "Xat yuborilgan", "Qayta xat yuborilgan", "Suhbat belgilangan", "Bo'sh o'rin yo'q", "Ariza tavsiya qilindi"]),
                      dict(k="sana", label="Sanalar", hint="xat, qayta xat, javob", ph="Xat ..., qayta xat ..., javob ..."),
                      dict(k="keyingi", label="Keyingi qadam", type="area", ph="...")]),
    check=dict(h2="M3 nazorati", sub="Xat yuborishdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Har rahbar uchun 2 ta real ilmiy moslik dalili bor.", "Dalillar havola va sana bilan.", "Xat ko'chirma yoki ommaviy emas.",
                      "Xatdagi har fakt tekshirilgan.", "Ilovalarda keraksiz shaxsiy ma'lumot yo'q.", "Aloqa holati va qayta yozish me'yorli.",
                      "Rahbarlik haqida tekshiriladigan savollar tayyor."]),
    art_title="Rahbar moslik kartalari va aloqalar jurnali", art_short="Jurnal",
    art=[("Rahbarlar ro'yxati", ["a1"]), ("Moslik matritsasi", ["a2"]), ("Asosiy rahbar", ["prof", "fit"]), ("Xat qoralamasi", ["a3", "sorov"]),
         ("Ilovalar", ["a4"]), ("Holat va sanalar", ["holat", "sana", "a5"]), ("Suhbat va jamoa", ["a6", "a7", "keyingi"])],
    tip="Xatni yuborishdan oldin professorning o'sha maqolasini qayta oching: yil, sarlavha va xulosa xatdagi bilan bir xilmi?",
    sources=f"{LEEDS}; {UKRIEXP}; {DORA}. {STD}",
)
