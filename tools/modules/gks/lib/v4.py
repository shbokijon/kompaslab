from common import U27, G26, STD

MOD = dict(
    title="Tavsiya xati va professor bilan aloqa",
    desc="GKS Lab M4: GKS tavsiya xati talablari, tavsiya beruvchi tanlash, yutuqlar varaqasi, professorga dastlabki xat va muloqot etikasi. Natija: aloqa paketi.",
    lead="GKS bitta tavsiya xati so'raydi, shuning uchun u kuchli bo'lishi shart. Magistratura va doktorantura nomzodlari uchun professor bilan oldindan aloqa tanlovni aniqlashtiradi. Bu modulda ikkala aloqani tartib bilan quring.",
    hero="bell", weeks="2", next="Shaxsiy bayonot",
    goals=[("bell", "Tavsiya beruvchi va reja", "kim, nega u, qachon so'raladi"),
           ("memo", "Yutuqlar varaqasi (Brag Sheet)", "tavsiya beruvchiga beriladigan faktlar to'plami"),
           ("telescope", "Professorga dastlabki xat", "M va D uchun; U uchun universitetga savol xati")],
    warn="Tavsiya xatini tavsiya beruvchi o'zi yozadi va imzolaydi. Kompas ham, siz ham uning o'rniga yozmaysiz: bu GKS kelishuviga va akademik halollikka zid. Siz faqat tekshiriladigan faktlar berasiz.",
    lessons=[
        dict(t="GKS tavsiya xati: talablar va tanlov", short="Talab", min=30, kind="🎯 Mini-test", ic="scroll",
             hook="GKS da tavsiya xati bitta. Ikkinchi imkoniyat yo'q: kim yozishi xat matnidan ham muhimroq bo'lishi mumkin.",
             body=f"""<h4>Yo'riqnomada</h4>
<ul><li><span class="trk">U</span> 2027 GKS-U: <b>bitta</b> tavsiya xati, ariza muddatidan oldingi bir yil ichida berilgan; akademik qobiliyatni baholay oladigan shaxsdan (direktor, o'qituvchi).</li>
<li><span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G: <b>bitta</b> tavsiya xati (forma bo'yicha). Elchixona trekida skaner nusxasi yuklanadi, asl nusxa ikkinchi bosqichda topshiriladi. Universitet trekida xat sanasi ariza muddatidan oldingi bir yil ichida bo'lishi kerak. Tavsiya beruvchi professor, kafedra mudiri yoki boshqa tegishli shaxs (afzal, o'z universitetingizdan).</li></ul>
<h4>Kimni tanlash</h4>
<div class="tbl"><table><thead><tr><th>Mezon</th><th>Savol</th></tr></thead><tbody>
<tr><td>Yaqinlik</td><td>U sizni qancha vaqt va qaysi ishda kuzatgan?</td></tr>
<tr><td>Aniq dalil</td><td>U sizning bitta konkret ishingizni misol qilib keltira oladimi?</td></tr>
<tr><td>Tegishlilik</td><td>Uning fani sizning yo'nalishingizga yaqinmi?</td></tr>
<tr><td>Ishonchlilik</td><td>Muddatga va formaga rioya qila oladimi?</td></tr>
</tbody></table></div>
<div class="box warn">Lavozimi baland, lekin sizni tanimaydigan odam umumiy xat yozadi. Sizni yaqindan bilgan o'qituvchi aniq misol bilan yozgan xat kuchliroq.</div>
<div class="srcs">Manba: {U27}; {G26}. 31.10.2026 holatiga.</div>""",
             take="GKS da bitta tavsiya xati; sanasi muddatdan oldingi bir yil ichida. Tavsiya beruvchini lavozim emas, yaqinlik va aniq dalil bo'yicha tanlang.",
             quiz=[("GKS da odatda uchta tavsiya xati talab qilinadi.", "n", "Noto'g'ri: 2027 GKS-U va 2026 GKS-G da bitta."),
                   ("2026 GKS-G elchixona trekida tavsiya xatining asl nusxasi ikkinchi bosqichda topshiriladi.", "t", "To'g'ri: birinchi bosqichda skaner nusxasi yuklanadi."),
                   ("Vaqtni tejash uchun tavsiya xatini nomzod o'zi yozib, imzoga berishi mumkin.", "n", "Noto'g'ri: bu akademik halollikka zid; xatni tavsiya beruvchi yozadi."),
                   ("Sizni yaxshi bilgan o'qituvchi rektordan ko'ra kuchliroq tavsiya beruvchi bo'lishi mumkin.", "t", "To'g'ri: aniq dalil lavozimdan muhimroq.")],
             task="<ul><li>3 ta nomzod tavsiya beruvchini 4 mezon bo'yicha (0–3) ballang va bittasini tanlang.</li></ul>",
             ph="1) ... yaqinlik 3, dalil 2 ... Tanlov: ..."),
        dict(t="Yutuqlar varaqasi va so'rash tartibi", short="So'rash", min=30, kind="🛠 Brag Sheet", ic="memo",
             hook="Tavsiya beruvchi sizning qaysi ishingizni eslaydi? Agar unga faktlarni bermasangiz, u umumiy iboralar bilan yozadi.",
             body="""<h4>Yutuqlar varaqasi (Brag Sheet) tarkibi</h4>
<ul><li>Siz kimsiz va qaysi dasturga topshiryapsiz (2–3 jumla).</li>
<li>U bilan birga qilgan aniq ish: fan, loyiha, sana.</li>
<li>3–5 ta tekshiriladigan yutuq (STAR, M3 dagi inventardan).</li>
<li>Komissiya nimani ko'rishi muhim: masalan, mustaqil ishlash yoki tadqiqot qiziqishi.</li>
<li>Forma, til, muddat va topshirish usuli (elektron, asl nusxa, imzo, muhr) yo'riqnomaga ko'ra.</li></ul>
<h4>So'rash vaqti va usuli</h4>
<ol><li>Ariza oynasidan kamida 6–8 hafta oldin, yuzma-yuz yoki rasmiy xat bilan so'rang.</li>
<li>\"Yo'q\" deyishga imkon qoldiring: istamay yozilgan xat sezilib qoladi.</li>
<li>Rozilik olgach, varaqani, formani va muddatni bitta xatda yuboring.</li>
<li>Muddatdan 10 kun oldin muloyim eslatma.</li>
<li>Natijadan qat'i nazar, rahmat xati.</li></ol>
<div class="box info">Varaqada faqat fakt. Tayyor matn, baholovchi sifatlar yoki \"mendan eng yaxshi o'quvchi\" kabi da'volarni bermang: baho tavsiya beruvchining o'zidan chiqishi kerak.</div>""",
             take="Tavsiya beruvchiga faktlar beriladi, matn emas. 6–8 hafta oldin so'rang, forma va muddatni bitta xatda yuboring.",
             task="<ul><li>Tanlangan tavsiya beruvchi uchun 1 sahifalik yutuqlar varaqasini yozing.</li></ul>",
             ph="Men ... Birga: ... Yutuqlar: 1) ... 2) ... Forma va muddat: ..."),
        dict(t="Professorga dastlabki xat (Cold email)", short="Xat", min=40, kind="✍ Xat", ic="telescope",
             hook="Professor kuniga o'nlab xat oladi. Uning ishini o'qimagan nomzodning xati 10 soniyada o'chiriladi; uning aniq maqolasiga tayangan xat esa o'qiladi.",
             body=f"""<p>2026 GKS-G yo'riqnomasi professor bilan oldindan aloqani majburiy qilmaydi. Lekin magistratura, ayniqsa doktorantura uchun laboratoriya va mavzu mosligini tekshirishning eng to'g'ri yo'li shu.</p>
<h4><span class="trk">M</span> <span class="trk">D</span> Xat tuzilmasi (120–200 so'z)</h4>
<ol><li><b>Mavzu qatori:</b> aniq. <span lang="en">Prospective GKS-G applicant: groundwater modelling (MSc, March 2028)</span></li>
<li><b>Kimsiz:</b> 1 jumla: daraja, universitet, soha.</li>
<li><b>Nega u:</b> uning bitta aniq ishi (maqola nomi, yil) va sizning qiziqishingiz bilan bog'liqligi.</li>
<li><b>Dalil:</b> sizning eng kuchli tegishli tajribangiz, 1–2 jumla.</li>
<li><b>Savol:</b> bitta aniq savol: laboratoriyada shu sikl uchun o'rin bormi, GKS arizasini qo'llab-quvvatlaydimi.</li>
<li><b>Ilova:</b> CV (PDF). O'quv rejasi qoralamasi tayyor bo'lsa, taklif qiling.</li></ol>
<h4><span class="trk">U</span> Bakalavriat uchun</h4>
<p>Bakalavriatda professorga xat odatda kerak emas. Universitetning xalqaro bo'limiga aniq savol (o'qitish tili, yo'nalish ochiqligi) yuborish mumkin, faqat javobi yo'riqnoma va saytda bo'lmasa.</p>
<div class="box warn">Bir xil xatni 30 ta professorga yubormang. 3–5 ta professor, har biriga alohida, uning ishiga tayangan xat.</div>
<div class="srcs">Manba: {G26}.</div>""",
             take="Professorga xat: kimsiz, nega u (aniq ish), dalil, bitta savol. Ommaviy xat emas, 3–5 ta shaxsiy xat.",
             task="<ul><li><span class=\"trk\">M</span> <span class=\"trk\">D</span> Bitta professor uchun xat qoralamasini yozing (120–200 so'z, ingliz tilida).</li><li><span class=\"trk\">U</span> Universitetga bitta aniq savol xatini yozing yoki savol kerak emasligini asoslang.</li></ul>",
             ph="Subject: ... Dear Professor ..."),
        dict(t="Kuzatuv, javob va etik chegaralar", short="Etika", min=25, kind="📋 Qoidalar", ic="shield",
             hook="Javob kelmasa, ikkinchi xatni qachon yozish kerak? Javob kelsa, nimani va'da qilish mumkin emas? Bu yerda xato aloqani buzadi.",
             body="""<h4>Kuzatuv</h4>
<ul><li>Javob bo'lmasa, 7–10 ish kunidan keyin bitta qisqa eslatma. Ikkinchidan keyin to'xtang.</li>
<li>Javob salbiy bo'lsa, rahmat ayting va tavsiya qilishi mumkin bo'lgan hamkasbi haqida so'rang.</li>
<li>Ijobiy javobda: suhbat vaqtini aniqlang, oldindan uning so'nggi 2–3 ishini o'qing.</li></ul>
<h4>Etik chegaralar</h4>
<ul><li>Professordan qabul yoki stipendiya kafolatini so'ramang: qarorni komissiyalar qiladi.</li>
<li>Hech kimga pul yoki sovg'a taklif qilmang; vositachilarga \"tanish orqali\" ish hal qilish uchun murojaat qilmang.</li>
<li>Tavsiya xati yoki professorning javobini tahrirlab, o'zgartirmang.</li>
<li>Professorning javobini boshqa nomzodlar bilan ulashmang.</li></ul>
<div class="box info"><b>Muloqot jurnali.</b> Har xat uchun sana, kimga, mavzu, javob va keyingi qadamni yozib boring. Bu M7 dagi nazorat jadvaliga qo'shiladi.</div>""",
             take="Bitta eslatma, keyin to'xtash; kafolat, sovg'a va vositachi yo'q. Har xatni jurnalga yozing.",
             task="<ul><li>Muloqot jurnali shablonini tuzing va birinchi 2–3 qatorni rejalashtiring.</li></ul>",
             ph="Sana · kimga · mavzu · javob · keyingi qadam"),
    ],
    tool=dict(id="paket", short="Paket", h2="Aloqa paketi", sub="Tavsiya va professor bilan aloqa uchun yakuniy materiallar.",
              h3="Tavsiya + xat", tag="4 maydon", ic="bell", btn="Paketni saqlash", badge="Aloqachi", min=3,
              fields=[dict(k="rec", label="Tavsiya beruvchi", hint="ism, lavozim, nega u, so'rash sanasi", type="area", ph="..."),
                      dict(k="brag", label="Yutuqlar varaqasi", type="area", ph="Faktlar ro'yxati"),
                      dict(k="mail", label="Professorga xat (M, D) yoki universitetga savol (U)", type="area", wc="120-200", ph="Subject: ..."),
                      dict(k="log", label="Muloqot jurnali va kuzatuv rejasi", type="area", ph="Sana · kimga · ...")]),
    check=dict(h2="Aloqa nazorati", sub="Xat yuborishdan va tavsiya so'rashdan oldin.", h3="8 bandlik nazorat",
               items=["Tavsiya beruvchi meni aniq ish orqali biladi.", "Xat sanasi muddatdan oldingi bir yil ichida bo'ladi.",
                      "Varaqada faqat tekshiriladigan faktlar, tayyor matn yo'q.", "Forma, til va topshirish usuli tavsiya beruvchiga aniq yetkazilgan.",
                      "Professorga xat uning aniq ishiga tayanadi.", "Xatda bitta aniq savol bor; kafolat so'ralmagan.",
                      "Bir xil xat ommaviy yuborilmagan.", "Muloqot jurnali yuritilmoqda."]),
    art_title="Aloqa paketi", art_short="Paket",
    art=[("Tavsiya beruvchi", ["rec", "a1"]), ("Yutuqlar varaqasi", ["brag", "a2"]), ("Professorga xat yoki universitetga savol", ["mail", "a3"]), ("Muloqot jurnali", ["log", "a4"])],
    tip="Professorga xat yozishdan oldin uning so'nggi maqolasining xulosasini o'z so'zingiz bilan bir jumlada ayta olasizmi? Ayta olmasangiz, xat hali erta.",
    sources=STD,
)
