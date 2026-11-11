from common import LEEDS, UKRIEXP, DORA, HOL, STD

MOD = dict(
    title="Ilmiy rahbar va laboratoriya bilan aloqa",
    desc="PhD Lab M3: ilmiy rahbar topish, moslikni baholash, professorga birinchi xat, ilovalar, eslatma xat odobi, birinchi suhbat va yordam tizimi. Natija: 6 ta rahbar kartasi va aloqalar daftari.",
    lead="Sizga kerakli ilmiy rahbar, avvalo, aynan sizning mavzuingizga rahbarlik qila oladigan odam; uning mashhurligi ikkinchi darajali. Bu modulda rahbarlarni <b>maqolalari va bo'sh o'rni</b> bo'yicha tanlaysiz, ularga qisqa va aniq xat yozasiz va birinchi suhbatga tayyorlanasiz.",
    hero="master", weeks="2–3", next="M4 Ilmiy loyiha taklifi va metodologiya", next_href="phd-lab-o.html?m=4",
    goals=[("telescope", "6 ta rahbar kartasi", "har birida 2 ta real ilmiy bog'liqlik"),
           ("memo", "Aloqalar daftari", "sana, holat, eslatma va javob"),
           ("bulb", "Suhbat rejasi", "90 soniyalik bayon va 6 ta savol")],
    warn="Professorga dastlabki xat (Cold email) yozishning umumiy usuli Master Lab da. Bu modulda faqat PhD ga xos qism: rahbar bilan moslik, uning bo'sh o'rni va ilmiy muhit. Namunalar Kompas tuzgan tuzilma; ularni tayyor xat sifatida ko'chirmang.",
    lessons=[
        dict(t="Ilmiy rahbarni qayerdan topish", short="Qidiruv", min=30, kind="🔎 Qidiruv", ic="telescope",
             hook="Birinchi bosqichda 100 ta xat yuborish shart emas. Avval <b>har biri bo'yicha dalil yig'ilgan</b> qisqa ro'yxat tuzing.",
             body=f"""<h4>Qayerdan qidiriladi</h4>
<ul><li>Kafedra professorlari sahifalari.</li><li>So'nggi grantlar va laboratoriya loyihalari.</li><li>Professor birinchi yoki oxirgi muallif bo'lgan maqolalar.</li><li>Bo'sh o'rinlar va e'lon qilingan loyihalar.</li></ul>
<p>Rahbarning usul bo'yicha tajribasini, ma'lumotga kirish imkonini, <b>yangi doktorant ola olishini</b> va ikkinchi rahbar topilishini o'rganing.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Zaif: <i>“Siz dunyodagi eng buyuk olimsiz.”</i> Aniqroq: <i>“2025-yilgi X usuli haqidagi maqolangizda aytilgan Y cheklov men o'rganmoqchi bo'lgan savolga bevosita bog'liq.”</i> Faqat haqiqiy maqola ma'lumotini yozing.</div>
<div class="box warn">Professor javob bermasa, bu qobiliyatingizga berilgan baho bo'lmaydi: ko'pincha unda vaqt yoki o'rin yetishmaydi.</div>""",
             take="12 ta nom toping, 6 tasiga karta yozing va har biri yangi doktorant olishini tekshiring.",
             task="<ul><li>12 ta nom toping.</li><li>6 tasiga karta yozing.</li><li>Qaysi guruh hozir doktorant olishini tekshiring.</li></ul><p><b>O'zingizga savol:</b> uning qaysi maqolasi savolingizga bevosita bog'liq?</p>",
             ph="1) Prof. ..., ... universiteti; maqola: ... (yil, DOI); ochiq o'rin: ..."),
        dict(t="Rahbar mosligini baholash", short="Baholash", min=25, kind="📊 Baholash", ic="chart",
             hook="Moslikni dalil bilan baholang: maqola, loyiha, bo'sh o'rin. Ballar faqat <b>dastlabki saralash</b> uchun kerak, odamga baho berish uchun ishlatilmaydi.",
             body=f"""<h4>5 ta mezon, har biri 0–2 ball</h4>
<ol><li>Mavzu mosligi.</li><li>Usul mosligi.</li><li>Rahbarda bo'sh o'rin bormi.</li><li>Moliya aniqmi.</li><li>Laboratoriya muhiti va ikkinchi rahbar imkoni.</li></ol>
<p>Ma'lumot topilmasa, 0 qo'ymang, <i>“noma'lum”</i> deb yozing: demak, shu haqda so'rash kerak.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> <i>“Maqolalar 2/2, moliya noma'lum”</i> yomon belgi bo'lmaydi: u xatda nimani so'rash kerakligini ko'rsatadi.</div>
<div class="box warn">Ballarni odam haqida qat'iy xulosaga aylantirmang.</div>
<div class="srcs">Manba: {DORA}. {HOL}.</div>""",
             take="Jadval nimani bilmasligingizni ko'rsatadi. Xat va suhbat shu bo'shliqlarni to'ldiradi.",
             task="<ul><li>6 ta rahbarni 5 mezon bo'yicha solishtiring.</li><li>Har biri uchun noma'lum qolgan bandni yozing.</li><li>3 ta eng mosini ajrating.</li></ul><p><b>O'zingizga savol:</b> professor doktorant olishini o'zi tasdiqlaganmi?</p>",
             ph="Prof. ...: mavzu 2, usul 1, o'rin ?, moliya ?, muhit 2 ; Noma'lum: ..."),
        dict(t="Birinchi xat tuzilmasi", short="Xat", min=35, kind="✉️ Xat", ic="memo",
             hook="Birinchi xat professor bilan <b>aniq akademik suhbatni</b> boshlash uchun yoziladi. Professor uni bir necha soniyada ko'zdan kechiradi, shuning uchun qisqa va aniq bo'lsin.",
             body=f"""<h4>Xat tuzilmasi</h4>
<ul><li><b>Mavzu qatori</b>: [[PhD enquiry]] va ilmiy yo'nalish.</li><li><b>Kimsiz va nega aynan shu laboratoriya.</b></li><li><b>Aniq ilmiy bog'liqlik</b>: uning bitta ishi va sizning savolingiz.</li><li><b>Tegishli tajriba</b>: 1–2 jumla, dalil bilan.</li><li><b>Aniq so'rov</b>: bo'sh o'rin bormi, ariza qanday beriladi.</li><li><b>Ilova</b>: so'ralgan bo'lsa, CV yoki qisqa bayon.</li></ul>
<p>Universitet ko'rsatmasini o'qing: e'lon qilingan loyihalarda ba'zan rahbarga oldindan yozish talab qilinmaydi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Zaif: <i><span lang="en">“Please accept me to your university, I am highly motivated.”</span></i> Kuchliroq tartib: bitta real ish, bitta aniq savol, tegishli tajriba va bo'sh o'rin haqida savol.</div>
<div class="box warn">Sun'iy intellekt yordamida maqola mazmunini yoki laboratoriya bilan aloqani to'qib chiqarmang.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Qisqa xat: bitta real ish, bitta aniq savol, bitta dalil va bitta aniq so'rov.",
             quiz=[("Professorning og'zaki “ha” deyishi qabul yoki moliya tasdig'i hisoblanadi.", "n", "Noto'g'ri: rasmiy taklif va moliya hujjati alohida keladi."),
                   ("E'lon qilingan loyihada rahbarga oldindan yozish doim majburiy.", "n", "Noto'g'ri: ba'zi e'lonlarda bu talab qilinmaydi; e'lonni o'qing."),
                   ("Jadvalda ma'lumot topilmasa, “noma'lum” deb yoziladi.", "t", "To'g'ri: 0 ball qo'yilmaydi; bu so'rash kerakligini bildiradi."),
                   ("Javob kelmasa, bir marta qisqa eslatma xat yozish mumkin.", "t", "To'g'ri: keyin boshqa mos yo'llarni davom ettiring.")],
             task="<ul><li>Professorning sizga tegishli bitta ishini tanlang.</li><li>5 jumlalik xat qoralamasini yozing.</li><li>Faqat tekshirilgan faktlar bilan yuboring.</li></ul><p><b>O'zingizga savol:</b> xatda faqat shu professorga tegishli bitta dalil bormi?</p>",
             ph="Mavzu: PhD enquiry, ... ; 1) ... 2) ... 3) ... 4) ... 5) ..."),
        dict(t="Portfolio va ilovalar", short="Ilova", min=25, kind="📎 Hujjat", ic="books",
             hook="Rahbar siz haqingizdagi asosiy dalilni tez topishi kerak. 30 betlik <i>“yutuqlar to'plami”</i> bunga xalaqit beradi.",
             body=f"""<ul><li>Akademik CV, 2 bet atrofida.</li><li>1–2 betlik tadqiqot bayoni (M1).</li><li>Mos bo'lsa: ishchi maqola, kod omborxonasi, poster yoki ma'lumot namoyishi.</li></ul>
<p>Havola ochilishini va kim ko'ra olishini tekshiring. PDF nomi tartibli, sahifalar o'qiladigan, hajmi katta bo'lmasin.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Zaif: 30 betlik <i>“Mening yutuqlarim”</i>. Kuchliroq: 2 betlik CV va qisqa bayon; ularda <b>qaysi usulni o'zingiz bajarganingiz</b> aniq yozilgan.</div>
<div class="box warn">Keraksiz shaxsiy ma'lumot, pasport nusxasi va hali e'lon qilinmagan natijalarni yubormang.</div>""",
             take="Ilovalar kam va aniq: CV, bayon va tekshirsa bo'ladigan bitta dalil.",
             task="<ul><li>2 betlik CV ni qayta ko'rib chiqing.</li><li>Portfolio uchun 3 ta dalil tanlang.</li><li>Fayllarga versiya va sana qo'ying.</li></ul><p><b>O'zingizga savol:</b> 60 soniyada qaysi usulni yaxshi bilishingizni ko'rsata olasizmi?</p>",
             ph="CV_v3_2026-11.pdf ; Dalil 1: ... (havola) ; 2: ... ; 3: ..."),
        dict(t="Eslatma xat va muloqot odobi", short="Odob", min=20, kind="🤝 Muloqot", ic="bell",
             hook="Ketma-ket xat yuborish va bosim o'tkazish akademik aloqani buzadi. Professorning vaqti kam; javob kechikishi ko'pincha shundan.",
             body=f"""<p>Universitetning yozishma qoidalariga amal qiling. Birinchi xatdan keyin biroz kuting, so'ng <b>bir marta</b> qisqa eslatma xat ([[follow-up]]) yozish mumkin. Javob bo'lmasa, boshqa mos yo'llarni davom ettiring.</p>
<p>Rad javobi yoki <i>“bo'sh o'rin yo'q”</i> degan javob odatda laboratoriyadagi o'rin va mablag' bilan bog'liq bo'ladi; uni shaxsiy qabul qilmang.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Qo'pol: <i><span lang="en">“Dear Professor, why don't you answer?”</span></i> Odobli: <i><span lang="en">“Thank you for considering my enquiry; I understand if no openings are available.”</span></i></div>
<div class="box warn">Bir xil xatni bir nechta professorga CC bilan yubormang.</div>""",
             take="Bitta xat, bitta eslatma, keyin boshqa yo'l. Hammasi sana bilan aloqalar daftariga yoziladi.",
             task="<ul><li>Xat sanasini daftarga yozing.</li><li>Eslatma xat nima uchun kerakligini o'ylab ko'ring.</li><li>Javobga qarab holatni belgilang.</li></ul><p><b>O'zingizga savol:</b> bu xatdan professor nimani aniq bilib oladi?</p>",
             ph="Prof. ...: xat ..., eslatma ..., holat: javob kutilmoqda / suhbat / o'rin yo'q"),
        dict(t="Rahbar bilan suhbat", short="Suhbat", min=30, kind="🎙 Suhbat", ic="miya",
             hook="Birinchi 20 daqiqalik suhbat rasmiy intervyu bo'lmasligi mumkin, lekin aynan unda moslik va reja <b>qanchalik real</b> ekani ko'rinadi.",
             body=f"""<h4>Nimani tayyorlash kerak</h4>
<ul><li>Mavzuingizning 90 soniyalik qisqa bayoni.</li><li>Unga tegishli dalil.</li><li>2 ta ilmiy savol.</li><li>Rahbarlik va moliya haqida 3 ta savol.</li></ul>
<p>Savollarga misol: <i><span lang="en">“How many students do you supervise?”</span></i>, <i><span lang="en">“How is feedback structured?”</span></i>, <i><span lang="en">“What happens if the project scope changes?”</span></i> Suhbatdan keyin yuborilgan qisqa xulosa xati nimani kelishganingizni aniqlab qo'yadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Professor savolingizdan ko'ra ma'lumot bor-yo'qligini ko'proq so'rasa, usulda muammo bo'lishi mumkin. Bayonni qayta ko'rib chiqing.</div>
<div class="box warn">Professorning og'zaki ijobiy javobi rasmiy taklif ham, moliya tasdig'i ham hisoblanmaydi.</div>""",
             take="Suhbatga 90 soniyalik bayon va 6 ta savol bilan kiring, keyin yozma xulosa yuboring.",
             task="<ul><li>90 soniyalik bayonni mashq qiling.</li><li>6 ta savolni muhimlik tartibida joylang.</li><li>Suhbatdan keyin qaror daftariga yozing.</li></ul><p><b>O'zingizga savol:</b> suhbatdan keyin qaysi taxminlaringiz o'zgardi?</p>",
             ph="Bayon: ... ; Savollar: 1) ... 2) ... ; Suhbatdan keyin: ..."),
        dict(t="Ikkinchi rahbar va yordam tizimi", short="Tizim", min=20, kind="🧭 Muhit", ic="shield",
             hook="Ilmiy ishning muvaffaqiyati faqat bitta rahbarga bog'liq bo'lmaydi. Muammo chiqsa, <b>kimga murojaat qilishni</b> oldindan bilib qo'ying.",
             body=f"""<p>Ikkinchi rahbar, maslahatchilar, o'quv rejasi, fikr-mulohaza qanchalik tez-tez berilishi, shikoyat yo'llari va ko'nikma rivoji universitet qoidalarida yoziladi. UKRI ning doktorlik ta'limi bo'yicha kutilmalar bayoni ([[Statement of Expectations]]) talaba, rahbar va universitet nimalarga javobgar ekanini ko'rsatadi.</p>
<div class="box info"><b>Kompas tuzgan namuna.</b> Rahbar kuchli, lekin dala ishiga kirish imkoni yo'q: qo'shimcha rahbar yoki sanoat hamkori kerak bo'lishi mumkin.</div>
<div class="box warn">Rahbarning og'zaki va'dasiga ishonib, universitetning rasmiy o'quv shartlarini o'qimaslik xavfli.</div>
<div class="srcs">Manba: {UKRIEXP}. {HOL}.</div>""",
             take="Jamoangizni chizib chiqing: rahbar, ikkinchi rahbar, talabalar xizmatlari va muammo chiqqanda kimga borish.",
             task="<ul><li>Bo'lajak jamoangizni chizib chiqing.</li><li>Talabalarga yordam xizmatlarini toping.</li><li>Hal bo'lmagan 2 ta xavfni yozing.</li></ul><p><b>O'zingizga savol:</b> muammo chiqsa, kimga borishni bilasizmi?</p>",
             ph="Rahbar: ... ; ikkinchi rahbar: ... ; xizmatlar: ... ; xavflar: 1) ... 2) ..."),
    ],
    tool=dict(id="daftar", short="Daftar", h2="Aloqalar daftari", sub="Professor, moslik dalili, holat va eslatma sanasini bir joyda yuriting.",
              h3="Rahbar kartasi va daftar", tag="6 maydon", ic="memo", btn="Daftarni saqlash", badge="Muloqot", min=5,
              fields=[dict(k="prof", label="Professor va universitet", ph="Prof. ..., ... universiteti, kafedra ..."),
                      dict(k="fit", label="2 ta ilmiy bog'liqlik", type="area", ph="1) Maqola ... (yil, DOI): ... ; 2) Loyiha ..."),
                      dict(k="sorov", label="Xatdagi aniq so'rov", type="area", ph="20..-yilda doktorant oladimi; ariza qanday beriladi ..."),
                      dict(k="holat", label="Holat", type="select", opts=["Xat yozilmagan", "Xat yuborilgan", "Eslatma yuborilgan", "Suhbat belgilangan", "Bo'sh o'rin yo'q", "Ariza berish tavsiya qilindi"]),
                      dict(k="sana", label="Sanalar", hint="xat, eslatma, javob", ph="Xat ..., eslatma ..., javob ..."),
                      dict(k="keyingi", label="Keyingi qadam", type="area", ph="...")]),
    check=dict(h2="M3 nazorati", sub="Xat yuborishdan oldin tekshiring.", h3="7 bandlik nazorat",
               items=["Har rahbar uchun 2 ta real ilmiy bog'liqlik yozilgan.", "Dalillar havola va sana bilan.", "Xat ko'chirma emas va ommaviy yuborilmaydi.",
                      "Xatdagi har fakt tekshirilgan.", "Ilovalarda keraksiz shaxsiy ma'lumot yo'q.", "Eslatma xatlar me'yorida.",
                      "Rahbarlik haqida aniq savollar tayyor."]),
    art_title="Rahbar kartalari va aloqalar daftari", art_short="Daftar",
    art=[("Rahbarlar ro'yxati", ["a1"]), ("Moslik jadvali", ["a2"]), ("Asosiy rahbar", ["prof", "fit"]), ("Xat qoralamasi", ["a3", "sorov"]),
         ("Ilovalar", ["a4"]), ("Holat va sanalar", ["holat", "sana", "a5"]), ("Suhbat va jamoa", ["a6", "a7", "keyingi"])],
    tip="Xatni yuborishdan oldin professorning o'sha maqolasini yana bir bor oching: yili, sarlavhasi va xulosasi xatdagi bilan bir xilmi?",
    sources=f"{LEEDS}; {UKRIEXP}; {DORA}. {STD}",
)
