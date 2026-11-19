# Magistratura M1–M8 v2 kontenti (2026-11-19). YANGI alifboda yoziladi; apply.py manbaga
# amaldagi alifboda (oʻ, gʻ, sh, ch) yozadi. Tutuq belgisi ʼ (U+02BC).
# Kalitlar: t (dars nomi), min (daqiqa), hook (Diqqat), fun (kiçik hazil, ixtiyoriy),
# main (Asosiy qism HTML), info/info_t (ⓘ ostidagi qöşimça), take (Xulosa),
# task_b / task (Topşiriq sarlavhasi va röyxati). Berilmagan kalit eski matnda qoladi.

SUB = "Har dars 4 qism: Diqqat, Asosiy qism, Xulosa, Topşiriq. Har qism 1–3 daqiqa."
DISCLAIMER = ("Javoblaringiz faqat şu brauzerda saqlanadi, boşqa qurilmaga özi ötmaydi. "
              "Vositalar universitet sanasi va talablarini Siz uçun tekşirmaydi, xat yubormaydi va qabulni kafolatlamaydi. "
              "Ball va belgilar Sizning ichki tekşiruvingiz, qabul ehtimoli emas. "
              "Har faktni dastur sahifasidan özingiz tasdiqlaysiz; sanasi körsatilgan maʼlumot şu sanadagi holat.")


def lock(items):
    return '<ul class="mv-lock">' + "".join('<li><img src="img/3d/lock.webp" alt="" width="22" height="22">%s</li>' % x for x in items) + "</ul>"


def bar(p, label):
    return '<div class="mv-bar"><i style="width:%d%%"></i></div><p class="mv-small">%s</p>' % (p, label)


M_TITLES = {
    1: ["Sizda nima bor?", "Qiziqişingizni bitta jumlaga siğdiring", "Reyting nimani körsatadi", "Dastur Sizga mosmi",
        "Röyxatni uç guruhga bölamiz", "Pul qayerdan keladi", "Sizning hikoyangiz"],
    2: ["Bitta arizada bir neçta sana", "Sanadan orqaga hisoblaymiz", "Hamma ariza bitta jadvalda", "Bir neçta arizani birga yuritiş",
        "I bosqiç yakuni: bir sahifalik reja"],
    3: ["CV kerakmi va qanday?", "Taʼlim bölimi va baholar", "Tajribani STAR bilan yoziş", "Naşr, çiqiş va loyihalar",
        "Könikma, til va sertifikat", "Yuborişdan oldingi tekşiruv"],
    4: ["Kuçli tavsiya xati nimadan iborat", "Kimdan va qaçon söraş", "Ustozga Yutuqlar varaqasi", "Professorga xat: qaçon va qanday",
        "Javob kelsa ham, kelmasa ham", "Xatlar daftari"],
    5: ["Maqsad bayonnomasi nima", "Tuzilma: törtta savolga javob", "«Nega aynan şu dastur?»", "Dalil bilan yoziş",
        "Birinçi qoralama", "Tahrir", "Namunalarni soliştiriş"],
    6: ["Taklif qaçon söraladi", "Muammo bayoni", "Adabiyotlar şarhi", "Metodologiya", "Iş rejasi va vaqt jadvali",
        "Kutilayotgan natija", "Format va iqtibos"],
    7: ["Stipendiya turlari va majburiy şartlar", "Buyuk Britaniya", "AQŞ", "Yevropa Ittifoqi", "Osiyo",
        "Turkiya va boşqa yönalişlar", "Özbekiston dasturlari va universitet grantlari", "Stipendiyalar röyxati"],
    8: ["Suhbat turlari", "Suhbatdagi 10 ta savol", "Stipendiya suhbatlari", "5 daqiqalik ilmiy taqdimot",
        "Javobni yozib oliş va baholaş", "Qabul xati kelgaç: birinçi ikki hafta", "Viza, suğurta, uy-joy, bank",
        "Birinçi 90 kun va öqişdan keyin"],
}


def tl(n):
    return ["M%d.%d %s" % (n, i + 1, t) for i, t in enumerate(M_TITLES[n])]


MODULES = {}

# ───────────────────────────── M1 ─────────────────────────────
MODULES[1] = dict(
    lead="Bu modulda qaysi dasturlarga topşirişingizni hal qilamiz. Oxirida Sizda uçta narsa böladi: "
         "<strong>saralangan dasturlar röyxati</strong>, <strong>bir jumlalik ilmiy qiziqiş</strong> va "
         "<strong>hikoyangizning qoralamasi</strong>. CV va maqsad bayonnomasi keyin aynan şularga tayanadi.",
    weeks="1", pass_time="~1 hafta (dars ~1,5 soat + vositalar)",
    mentor="Röyxatni reytingdan emas, kurslar röyxatidan boşlang. Tadqiqot magistraturasida professorning işi, öquv magistraturasida modullar va kasbiy natija hal qiladi.",
    next=("<h2>Keyingi qadam: sanalar</h2>" + bar(30, "I bosqiç: 1 / 2 modul · Rejangiz 30% tayyor") +
          '<div class="mv-k" data-mn="m1"><b>Röyxatingizdagi dasturlar har xil kunda yopiladi.</b> Qaysi biri birinçi? '
          "M2 da röyxatingiz Arizalar jadvaliga bitta tugma bilan köçadi, Siz faqat sanalarni qöyasiz.</div>"
          '<p>M2.1 dan: <i>Dastur arizasi hali oçiq, lekin stipendiya sanasi ötib ketgan bölişi mumkin. '
          "Şuning uçun har dasturda ikki sana alohida yoziladi.</i></p>"
          '<div class="mv-row"><a class="btn btn-p" href="master-lab-o.html?m=2">M2: sanalarni qöyiş</a></div>'),
    lessons={
        "l1": dict(t=M_TITLES[1][0], min=10,
            hook="Köp talaba profilini «Naşrim yöq» deb boşlaydi va şu yerda töxtaydi. Öquv magistraturasiga topşirayotgan odamdan naşr odatda söralmaydi. "
                 "Komissiya qaysi fanni öqiganingiz va qanday iş qilganingizga qaraydi. Bu darsda bor narsangizni yiğamiz.",
            main="<p>Profilingiz törtta qutidan iborat:</p>"
                 '<div class="tbl"><table><thead><tr><th>Quti</th><th>Nima yoziladi</th><th>Misol</th></tr></thead><tbody>'
                 "<tr><td>Fanlar</td><td>Yaxşi bilgan 3–5 fan</td><td>Gidrologiya, GIS, statistika</td></tr>"
                 "<tr><td>Işlar</td><td>Kurs işi, bitiruv işi, amaliyot, iş joyidagi vazifa</td><td>Suğoriş suvi şörlanişi haqida bitiruv işi</td></tr>"
                 "<tr><td>Könikmalar</td><td>Hozir qila oladigan narsalar</td><td>QGIS da xarita, Excel da tahlil</td></tr>"
                 "<tr><td>Savollar</td><td>Sizni qiziqtiradigan muammo</td><td>Nega dalada suv tez şörlanyapti?</td></tr>"
                 "</tbody></table></div>"
                 "<p>Guruh loyihasida faqat öz qismingizni yozing.</p>",
            info="<p>Sohani özgartirmoqçi bölsangiz ham profil kerak: u qaysi fan va könikma yetişmasligini körsatadi. "
                 "Öquv magistraturasida (<em lang=\"en\">taught</em>) kurslar va kasbiy maqsad, tadqiqot magistraturasida (<em lang=\"en\">research</em>) ilmiy savol ham tekşiriladi.</p>",
            take="Ikki va undan köp qutida takrorlangan mavzu Sizning yönalişingizga birinçi işora.",
            task_b="Sizning profilingiz",
            task=["Har qutiga kamida bitta qator yozing. Yöq narsani böş qoldiring.",
                  "Takrorlangan mavzuni oxirgi qatorga yozing."]),
        "l2": dict(t=M_TITLES[1][1], min=12,
            hook="«Men energetikani öqimoqçiman» degan odamga yuzlab dastur mos keladi va u qaysi birini tanlaşni bilmaydi. "
                 "«Men binolarni yer issiqligi bilan isitişni öqimoqçiman» degan odam bir neçta dasturni bir oqşomda körib çiqadi. Bu darsda Sizning jumlangizni toraytiramiz.",
            fun="Hamma narsa qiziq degan javob faqat tuğilgan kun tilagida yaxşi eşitiladi.",
            main="<p>Qiziqişni uç pillada yozamiz, har pillada torroq:</p>"
                 '<div class="tbl"><table><thead><tr><th>Pilla</th><th>Savol</th><th>Misol</th></tr></thead><tbody>'
                 "<tr><td>Soha</td><td>Qaysi fan?</td><td>Energetika</td></tr>"
                 "<tr><td>Yönaliş</td><td>Uning qaysi qismi?</td><td>Geotermal isitiş</td></tr>"
                 "<tr><td>Savol</td><td>Aniq nimani bilmoqçisiz?</td><td>Yer osti harorati qişda va yozda isitiş tizimiga qanday taʼsir qiladi?</td></tr>"
                 "</tbody></table></div>"
                 "<p><b>Tekşiruv:</b> ikkita dastur sahifasida şu mavzu bormi? Bölsa, jumla töğri. Yöq bölsa, bir pilla kengaytiring.</p>",
            info="<p>Öquv magistraturasi uçun «Soha» va «Yönaliş» yetadi. Tadqiqot magistraturasi uçun «Savol» ham kerak: unda obyekt (nimani), usul (qanday) va sabab (nega muhim) bölsin.</p>",
            take="Yaxşi jumla dastur qidirişga yetadigan darajada tor. Mukammal ilmiy savolni keyin rahbar bilan aniqlaştirasiz.",
            task_b="Sizning qiziqişingiz bitta jumlada"),
        "l3": dict(t=M_TITLES[1][2], min=10,
            hook="Umumiy reytingda yuqorida turgan universitetning Sizga kerakli dasturi zaif bölişi mumkin, pastroqdagisida esa aynan Sizning sohangiz kuçli bölişi mumkin. "
                 "Umumiy reyting butun universitetni baholaydi. Bu darsda reytingdan töğri foydalanamiz.",
            main="<p><b>Bitta fakt yetadi:</b> QS reytingida balning 30% akademik obrödan, 15% iş beruvçilar fikridan keladi. Ikkalasi sörovnoma.</p>"
                 "<p>Şuning uçun tartib şunday:</p>"
                 "<ol><li>Fan böyiça reyting (masalan, <em lang=\"en\">QS by Subject</em>).</li><li>Dastur sahifasi.</li><li>Kurslar va qabul şartlari.</li><li>Pul.</li></ol>"
                 "<p>Reytingda yöq, lekin kurslari mos dastur röyxatdan çiqmaydi.</p>",
            info="<p>THE öqitiş va tadqiqot muhitiga, ARWU mukofot va maqolalarga köproq qaraydi. Uçalasi boşqa-boşqa narsani ölçaydi, ularni bir xil öqib bölmaydi.</p>",
            take="Reytingdan röyxatni boşlaysiz, qarorni dastur sahifasiga qarab qilasiz.",
            task_b="Tez test: töğri yoki notöğri?"),
        "l4": dict(t=M_TITLES[1][3], min=12,
            hook="Arizada «Bu universitet nufuzli» deb yozsangiz, komissiya yangi heç narsa bilmaydi. "
                 "«Bu dasturda suv resurslarini modellaştiriş kursi bor, men aynan şuni örganmoqçiman» degan gapni esa ular tekşira oladi. Bu darsda har dastur uçun şunday dalil topamiz.",
            main="<p>Dastur sahifasida törtta narsani qidiring:</p>"
                 '<div class="tbl"><table><thead><tr><th>Nima</th><th>Qayerda</th><th>Kimga kerak</th></tr></thead><tbody>'
                 "<tr><td>Kurslar</td><td>«<em lang=\"en\">Course structure</em>» yoki «<em lang=\"en\">Modules</em>» bölimi</td><td>Hammaga</td></tr>"
                 "<tr><td>Rahbar</td><td>Kafedra xodimlari sahifasi</td><td>Tadqiqot magistraturasiga</td></tr>"
                 "<tr><td>Laboratoriya yoki guruh</td><td>«<em lang=\"en\">Research</em>» bölimi</td><td>Tadqiqotga</td></tr>"
                 "<tr><td>Usul va resurslar</td><td>Kurs tavsifi, dala işi, amaliyot</td><td>Hammaga</td></tr>"
                 "</tbody></table></div>"
                 "<p>Professor talaba olayotganini taxmin qilmang. Uning işini öqimaguncha ismini arizaga yozmang.</p>",
            take="Dalil topilmagan dastur röyxatdan çiqadi. Öquv magistraturasida rahbar belgilanmasa, bu kamçilik emas.",
            task_b="Har dastur uçun dalilingiz",
            task=["Dastlabki röyxatdagi har dastur uçun topgan dalilingizni yozing: kurs, rahbar, laboratoriya yoki usul.",
                  "Pastdagi <a href=\"#shortlist\">Saralangan röyxat</a>ga qöşganda dalil turlarini belgilaysiz."]),
        "l5": dict(t=M_TITLES[1][4], min=12,
            hook="Faqat eng maşhur beşta universitetga topşirgan odam bahorda bitta ham taklifsiz qolişi mumkin. "
                 "Faqat oson joylarga topşirgan odam esa yuqoriroğiga urinib körmaganiga afsuslanadi. Bu darsda röyxatni muvozanatga keltiramiz.",
            fun="Buvilarimiz hamma tuxumni bitta savatga solmang deganda arizalarni ham nazarda tutgan bölsa kerak.",
            main='<div class="tbl"><table><thead><tr><th>Guruh</th><th>Nimani bildiradi</th><th>Neçta</th></tr></thead><tbody>'
                 '<tr><td><span class="pill d">Orzu</span></td><td>Raqobat yuqori, lekin majburiy şartlarga mos kelasiz</td><td>2–3</td></tr>'
                 '<tr><td><span class="pill t">Möljal</span></td><td>Şartlar va kurslar Sizga yaxşi mos</td><td>3–4</td></tr>'
                 '<tr><td><span class="pill s">Nisbatan mos</span></td><td>Şartlarga bemalol mos, xarajati qulayroq</td><td>1–3</td></tr>'
                 "</tbody></table></div>"
                 "<p><b>Birinçi filtr:</b> majburiy şartlar (diplom, baho, til, tajriba). Bittasi bajarilmasa, dastur qaysi guruhda turişidan qatʼi nazar röyxatga kirmaydi.</p>",
            info="<p>Raqamlar tavsiya: neçta arizaga vaqtingiz va pulingiz yetsa, şunça yozing. «Nisbatan mos» guruhda ham qabul kafolatlanmaydi. "
                 "Dastur qabul statistikasini bermasa, raqobatni «nomaʼlum» deb belgilang.</p>",
            take="Uç guruhda ham kamida bittadan dastur bölsa, röyxat muvozanatli.",
            task_b="Sizning saralangan röyxatingiz",
            task=["Pastdagi <a href=\"#shortlist\">Saralangan röyxat</a>ga 6–10 dastur qöşing va har biriga guruh tanlang."]),
        "l6": dict(t=M_TITLES[1][5], min=10,
            hook="Qabul xati keldi, quvonç katta. Keyin hisob keladi: öqiş puli, yotoqxona, viza, suğurta, çipta. "
                 "Stipendiya faqat öqiş pulini qoplasa, qolganini kim tölaydi? Bu darsda har dastur uçun şu savolga javob yozamiz.",
            main="<p>Har dastur uçun uç savol:</p>"
                 "<ol><li>Bir yilga jami qança kerak? (öqiş puli, yaşaş, viza, suğurta, yöl)</li>"
                 "<li>Grant yoki stipendiya aynan nimani qoplaydi?</li><li>Qolganini kim tölaydi?</li></ol>"
                 "<p>Bir xil nomli grant har xil narsani qoplaşi mumkin. Grantni nomiga qarab tanlamang, bu yilgi şartini öqing.</p>",
            info="<p>Pul turlari: töliq stipendiya, qisman grant, öqiş pulidan çegirma, assistentlik (TA/RA), arzon yoki bepul öqiş, öz puli yoki kredit. "
                 "Universitet va grant sanalari har xil bölişi mumkin: ularni M2 da alohida yozasiz.</p>",
            take="Pul aniq bölmagan dastur röyxatda qoladi, lekin «?» belgisi bilan. Aniq bölmagan narsani «tasdiqlangan» demang.",
            task_b="Sizning pul rejangiz",
            task=["Röyxatdagi har dastur uçun pul turini tanlang (vosita içida). Bilmasangiz, «?» qöying.",
                  "Har grant uçun rasmiy havola va qamrovni yozing."]),
        "l7": dict(t=M_TITLES[1][6], min=12,
            hook="CV da geologiya, maqsad bayonnomasida iqtisod, intervyuda dasturlaş. Uç hujjatni öqigan komissiya bu odam aslida nima qilmoqçi ekanini tuşunmaydi. "
                 "Bu darsda hamma hujjat tayanadigan bitta hikoyani yozamiz.",
            main='<div class="tbl"><table><thead><tr><th>Qism</th><th>Savol</th><th>Qayerdan</th></tr></thead><tbody>'
                 "<tr><td>Ötmiş</td><td>Bu yönalişga oid nima qilgansiz?</td><td>1.1 dagi işlar</td></tr>"
                 "<tr><td>Hozir</td><td>Nima qila olasiz, nima yetişmaydi?</td><td>1.1 könikmalar</td></tr>"
                 "<tr><td>Maqsad</td><td>Dasturda nimani örganasiz va nega?</td><td>1.2 jumla, 1.4 dalil</td></tr>"
                 "</tbody></table></div>"
                 "<p><b>Misol:</b> Kurs loyihamda suv maʼlumotlarini Excel da tahlil qildim → statistik modellaşni bilmayman → bu dasturdagi gidrologik modellaş kursi aynan şuni öqitadi.</p>"
                 "<p>Tavsiya xatini boşqa odam yozadi. Uni bu hikoyaga moslab Siz yozib bermaysiz.</p>",
            take="Ötmiş, hozir va maqsad bitta çiziqda tursa, CV va maqsad bayonnomasi bir-biriga zid bölmaydi.",
            task_b="Sizning hikoyangiz (qoralama)"),
    },
)

# ───────────────────────────── M2 ─────────────────────────────
MODULES[2] = dict(
    lead="Bu modulda sanalarni yiğamiz va ulardan orqaga reja tuzamiz. Oxirida Sizda <strong>Arizalar jadvali</strong>, "
         "<strong>vaqt jadvali</strong> va <strong>bir sahifalik tayyorgarlik rejasi</strong> böladi.",
    weeks="1", pass_time="~1 hafta (dars ~1 soat + vositalar)",
    mentor="Köp yaxşi ariza sanadan keç qolgani uçun öqilmay qoladi. Har yakşanba 20 daqiqa jadvalga qarang.",
    next=("<h2>I bosqiç tugadi</h2>" + bar(40, "I bosqiç: 2 / 2 modul · Rejangiz 40% tayyor") +
          '<div class="mv-k" data-mn="m2rec"><b>Tavsiya xatini söraş kuningiz</b> eng erta muddatingizdan 8 hafta oldin. '
          "Jadvalga sana kiritsangiz, aniq kun şu yerda çiqadi.</div>"
          '<div class="mv-k" data-mn="m2cv"><b>CV ning Taʼlim bölimi</b> uçun M1 dagi fanlaringiz va işlaringiz tayyor turibdi.</div>'
          "<p><b>II bosqiçda (M3–M4) Sizni kutayotgan 12 dars:</b></p>" + lock(tl(3) + tl(4)) +
          '<div class="mv-row"><a class="btn btn-p" href="master-lab-o.html?m=3">II bosqiçni boşlaş</a>'
          '<a class="btn btn-g" href="master-lab-narxlar.html">Tariflarni soliştiriş</a></div>'
          '<p class="mv-small">«1 ta bosqich» tarifida II bosqiç navbatdagi tölov bilan, tölov qilingan zahoti oçiladi.</p>'),
    lessons={
        "l1": dict(t=M_TITLES[2][0], min=10,
            hook="Dastur arizasi hali oçiq bölişi mumkin, stipendiya uçun kerakli sana esa ötib ketgan bölişi mumkin. "
                 "Bu darsda har dasturda qaysi sanalar borligini ajratamiz.",
            main="<p>Bitta arizada odatda bir neçta sana bor: universitet arizasi, stipendiya yoki grant, tavsiya xatlari, til natijasi.</p>"
                 '<div class="tbl"><table><thead><tr><th>Atama</th><th>Maʼnosi</th></tr></thead><tbody>'
                 "<tr><td>Yakuniy muddat (<em lang=\"en\">deadline</em>)</td><td>Ariza qaysi kun, qaysi soatgaça va qaysi vaqt mintaqasida qabul qilinadi</td></tr>"
                 "<tr><td>Ustuvor muddat (<em lang=\"en\">priority</em>)</td><td>Grant yoki birinçi körib çiqiş uçun. Undan keyin ariza qabul qilinişi kafolatlanmaydi</td></tr>"
                 "<tr><td>Navbatma-navbat (<em lang=\"en\">rolling</em>)</td><td>Arizalar kelişi bilan körib çiqiladi, erta topşiriş foydali</td></tr>"
                 "<tr><td>Bosqiçlar (<em lang=\"en\">rounds</em>)</td><td>Har bosqiçning öz sanasi va baʼzan öz granti bor</td></tr>"
                 "</tbody></table></div>"
                 "<p><b>Soatga qarang.</b> Oxford da baʼzi magistratura sanalari Britaniya vaqti bilan tuşlik, 12:00 da yopiladi.</p>",
            info="<p>Yangi yil sanasi eʼlon qilinmagan bölsa, eski sanani tasdiqlangan deb yozmang: «nomaʼlum» deb qoldiring. "
                 "Telegram kanaldagi sana eskirgan bölişi mumkin, faqat rasmiy sahifa.</p>",
            take="Har dasturda universitet, stipendiya va hujjat sanalarini alohida yozasiz va eng erta sanaga qarab reja tuzasiz.",
            task_b="Tez test: töğri yoki notöğri?"),
        "l2": dict(t=M_TITLES[2][1], min=12,
            hook="Muddatga ikki hafta qolganda ustozingizdan tavsiya söradingiz. U şu hafta konferensiyada ekan. "
                 "Boşqa odamga boğliq iş eng ertadan boşlanadi. Bu darsda sanadan orqaga hisoblaymiz.",
            main="<p><b>Avval boşqalarga boğliq iş:</b></p>"
                 "<ul><li>Tavsiya xati: 8 hafta oldin söraymiz. Bu bizning ehtiyot tavsiyamiz, universitet talabi emas.</li>"
                 "<li>Til imtihoni: imtihon kuni, natija çiqişi va universitetga yetib boriş muddati.</li>"
                 "<li>Tarjima va tasdiq: diplom yoki qaydnoma uçun kerakmi, dastur sahifasidan bilasiz.</li></ul>"
                 "<p><b>Keyin özingiz qiladigan iş:</b> CV (M3), maqsad bayonnomasi (M5), kerak bölsa tadqiqot loyihasi taklifi (M6). Har biri: qoralama → tahrir → tekşiruv → yakuniy fayl.</p>"
                 "<p><b>Zaxira:</b> topşiriş kunidan kamida bir hafta oldin tayyor böling. Oxford arizani imkon qadar kamida ikki hafta oldin yuborişni tavsiya qiladi.</p>",
            take="Reja topşiriş sanasidan orqaga hisoblanadi: avval boşqa odamga boğliq iş, oxirida zaxira hafta.",
            task_b="Sanadan orqaga reja"),
        "l3": dict(t=M_TITLES[2][2], min=10,
            hook="Bitta dasturning sanasi telefonda, ikkinçisiniki daftarda, uçinçisi emailda. Bir kuni uçinçisi esdan çiqadi. "
                 "Bu darsda hamma arizani bitta jadvalga yiğamiz.",
            main="<p>Jadvalda har qator bitta dastur yoki stipendiya. Ustunlar:</p>"
                 "<ul><li><b>Nom va tur:</b> universitet dasturi yoki stipendiya, qabul yili.</li>"
                 "<li><b>Sana:</b> kun, soat, vaqt mintaqasi.</li>"
                 "<li><b>Holat:</b> Rejada → Tayyorlanmoqda → Yuborildi → Natija kutilmoqda → Yakuniy qaror.</li>"
                 "<li><b>Hujjatlar:</b> CV, maqsad bayonnomasi, qaydnoma, til, tavsiya.</li>"
                 "<li><b>Pul va havola:</b> ariza tölovi, grant, rasmiy sahifa.</li></ul>"
                 "<p><b>Haftasiga bir marta</b> har qatorni körib çiqing va keyingi haftaning 3 ta işini yozing.</p>",
            take="Jadval Sizning yagona işçi röyxatingiz. Rasmiy sana doim universitet portalida.",
            task_b="Sizning arizalar jadvalingiz",
            task=["Pastdagi <a href=\"#tracker\">Arizalar jadvali</a>ga M1 röyxatingizni import qiling yoki dasturlarni qölda qöşing.",
                  "Har qatorga maʼlum bölgan sana va havolani yozing.",
                  "Jadvalni yangilaydigan kun va soatni tanlang."]),
        "l4": dict(t=M_TITLES[2][3], min=10,
            hook="Bitta stipendiya natijasini kutib, keyingisiga keyin kirişgan odam ikkinçi sanani boy beradi. "
                 "Lekin ariza qança köp bölsa, şunça yaxşi degan qoida ham yöq. Bu darsda bir neçta arizani birga yuritamiz.",
            main="<p>Boşlanğiç misol: 6–10 dastur va 3 tagaça stipendiya. Vaqtingiz va pulingizga moslang.</p>"
                 "<p><b>Qayta işlatiladigan qismlar:</b></p>"
                 "<ul><li>CV: asosi bir xil, dasturga mos yutuqlar tanlanadi.</li>"
                 "<li>Maqsad bayonnomasi: bitta qoralama, lekin har dasturga kurslar va maqsad moslanadi. Faqat universitet nomini almaştiriş yetmaydi.</li>"
                 "<li>Tavsiya xatlari: ustozga dasturlar va sanalar jadvalini berasiz.</li></ul>"
                 "<p><b>Töqnaşuv:</b> vosita 14 kun içidagi sanalarni belgilaydi. Bunday juftlikda birinçi arizani ertaroq tayyorlang yoki ariza sonini kamaytiring.</p>",
            take="Hamma ariza bitta vaqt jadvalida körinsa, qaysi haftada qiyin bölişini oldindan bilasiz.",
            task_b="Sizning vaqt jadvalingiz",
            task=["Jadvalga sana kiritilgaç, pastdagi <a href=\"#gantt\">vaqt jadvali</a> özi çiziladi.",
                  "14 kunlik töqnaşuvlarni körib çiqing va har biri uçun ichki tayyor böliş sanasini yozing."]),
        "l5": dict(t=M_TITLES[2][4], min=12,
            hook="M1 da dasturlarni tanladingiz, M2 da sanalarni qöydingiz. Endi hammasini bir sahifaga yiğamiz: "
                 "kim, qayerga, qaçon va qanday pul bilan.",
            main='<div class="tbl"><table><thead><tr><th>Savol</th><th>Qayerdan</th></tr></thead><tbody>'
                 "<tr><td>Kim?</td><td>M1.1 profil va M1.7 hikoya</td></tr>"
                 "<tr><td>Qayerga?</td><td>M1 saralangan röyxat va Arizalar jadvali</td></tr>"
                 "<tr><td>Qaçon?</td><td>Eng erta sana, ichki tayyor böliş sanalari</td></tr>"
                 "<tr><td>Qanday pul bilan?</td><td>M1.6 pul rejasi</td></tr>"
                 "</tbody></table></div>"
                 "<p>Yana ikkita narsa qöşasiz: haftasiga haqiqatan ajrata oladigan soatingiz va eng katta xavf (til, tavsiya, grant yoki pul).</p>",
            info="<p>Vosita M1 va M2 javoblarini şu brauzerdan oladi. M1 boşqa qurilmada qilingan bölsa, ayrim qatorlar böş çiqadi: ularni qölda yozing.</p>",
            take="Bu reja har oy yangilanadi. II bosqiçdagi CV va tavsiya xatlari şunga tayanadi.",
            task_b="Sizning tayyorgarlik rejangiz"),
    },
)

# ───────────────────────────── M3 ─────────────────────────────
MODULES[3] = dict(
    lead="Bu modulda <strong>1–2 sahifalik akademik CV</strong> yozamiz: taʼlim, tajriba va könikmalar faqat isbotlanadigan dalil bilan. "
         "Oxirida PDF va Word da oçiladigan fayl böladi.",
    weeks="1–2", pass_time="~1–2 hafta (dars ~1 soat + CV yoziş)",
    next=("<h2>Keyingi qadam: tavsiya xatlari</h2>" + bar(50, "II bosqiç: 1 / 2 modul · Rejangiz 50% tayyor") +
          '<div class="mv-k" data-mn="m3"><b>CV dagi tajribangiz endi ustozingizga kerak.</b> M4 CV maʼlumotingizni öqiydi: '
          "tavsiya beruvçiga beriladigan Yutuqlar varaqasini noldan yozmaysiz.</div>"
          '<div class="mv-row"><a class="btn btn-p" href="master-lab-o.html?m=4">M4: tavsiya söraş</a></div>'),
    lessons={
        "l1": dict(t=M_TITLES[3][0], min=10,
            hook="Oxford dagi köp magistratura dasturi alohida CV sörmaydi, Cambridge esa magistratura arizasida CV yuklaşni talab qiladi. "
                 "Bitta qoida hammaga yöq. Bu darsda Sizning dasturingiz nima söraşini aniqlaymiz.",
            main="<p>Dastur sahifasidan törtta javobni toping:</p>"
                 "<ul><li><b>Kerakmi?</b> Alohida fayl söraladimi yoki tajriba ariza formasiga yoziladimi?</li>"
                 "<li><b>Hajm:</b> sahifa yoki söz çegarasi bormi? Yöq bölsa, 1–2 sahifa.</li>"
                 "<li><b>Format:</b> PDF, maxsus andoza?</li>"
                 "<li><b>Mazmun:</b> qaysi tajriba şu dasturga tegişli?</li></ul>"
                 "<p>Magistratura CV si iş rezyumesidan farq qiladi: öqiş, loyiha va tadqiqotga urğu beradi.</p>",
            info="<p>Europass ixtiyoriy format. Dastur andoza bersa, şuni işlating. Rasm, tuğilgan sana va oilaviy holatni dastur sörmasa qöşmang.</p>",
            take="Avval dastur nima söraşini bilasiz, keyin yozasiz.",
            task_b="Tez test: töğri yoki notöğri?"),
        "l2": dict(t=M_TITLES[3][1], min=10,
            hook="«GPA: 4.2» degan yozuvdan komissiya qaysi şkala ekanini bilmaydi. «4.2 / 5.0» yozuvi esa aniq. Bu darsda taʼlim bölimini töğri yozamiz.",
            main="<p>Taʼlim qatorida: daraja, yönaliş, universitet, yillar va dasturga yaqin fanlar.</p>"
                 '<div class="box info"><b>Namuna (öquv misoli):</b><br><span lang="en">BSc in Geology, Example University, 2021–2025<br>GPA: 4.6/5.0; Thesis: Groundwater salinity mapping; Relevant coursework: Hydrogeology, GIS, Statistics.</span></div>'
                 "<ul><li><b>GPA:</b> qaydnomada qanday bölsa, şunday. Şkalalarni özingiz tenglaştirmang.</li>"
                 "<li><b>Örin va mukofot:</b> «top 10%» faqat hujjat bilan tasdiqlansa.</li>"
                 "<li><b>Hali öqiyotgan bölsangiz:</b> tugaş yilini <em lang=\"en\">expected</em> deb yozing.</li></ul>",
            take="Taʼlim bölimida faqat qaydnoma bilan tasdiqlanadigan raqam turadi.",
            task_b="Sizning taʼlim bölimingiz",
            task=["Pastdagi <a href=\"#cvtool\">CV quruvçi</a>ning «Taʼlim» qismiga kamida bitta qator kiriting.",
                  "Dasturingizga eng yaqin 3–6 fanni tanlang va nega aynan şular ekanini qisqa yozing."]),
        "l3": dict(t=M_TITLES[3][2], min=12,
            hook="«Responsible for laboratory work» degan qatordan komissiya Siz aslida nima qilganingizni bilmaydi. "
                 "Qaysi işni qanday usul bilan qilganingizni yozsangiz, raqam bölmasa ham hissangiz körinadi. Bu darsda tajribani şunday yozamiz.",
            main="<p>STAR: vaziyat, vazifa, harakat, natija (<em lang=\"en\">Situation, Task, Action, Result</em>). CV ga odatda qisqa şakli yoziladi: <b>harakat + usul + natija</b>.</p>"
                 '<div class="tbl"><table><thead><tr><th>Qator</th><th>Baho</th></tr></thead><tbody>'
                 '<tr><td lang="en">Helped with data analysis.</td><td>Umumiy: qanday maʼlumot va usul, nomaʼlum</td></tr>'
                 '<tr><td lang="en">Cleaned groundwater monitoring records using Python and documented missing-value handling for a course project.</td><td>Harakat, usul va loyiha aniq</td></tr>'
                 "</tbody></table></div>"
                 "<p>Kurs işi va mustaqil loyiha ham tajriba. Kurs işini ilmiy assistentlik lavozimiga aylantirmang.</p>",
            take="Har tajriba qatori feʼl bilan boşlanadi va Siz aynan nima qilganingizni körsatadi.",
            task_b="3 ta STAR qatori",
            task=["Pastdagi <a href=\"#startool\">STAR generatori</a>da 3 ta qator yasang va «Tajriba» bölimiga qöşing.",
                  "Raqamni faqat haqiqatan bölsa yozing."]),
        "l4": dict(t=M_TITLES[3][3], min=8,
            hook="Konferensiyada tinglovçi böliş, poster bilan çiqiş va jurnalda maqola çop etiş: uç xil narsa. "
                 "CV da hammasini «naşr» deb yozsangiz, komissiya birinçi tekşiruvdayoq buni sezadi.",
            main='<div class="tbl"><table><thead><tr><th>Tur</th><th>Nima yoziladi</th></tr></thead><tbody>'
                 "<tr><td>Naşr</td><td>Mualliflar, nom, jurnal, yil, DOI. Holati: çop etilgan, qabul qilingan yoki taqrizda</td></tr>"
                 "<tr><td>Çiqiş</td><td>Maʼruza yoki poster, konferensiya, sana, Sizning rolingiz</td></tr>"
                 "<tr><td>Loyiha</td><td>Vazifa, usul, natija, Sizning hissangiz, havola</td></tr>"
                 "</tbody></table></div>"
                 "<p><em lang=\"en\">Under review</em> çop etilgan degani emas. DOI va jurnal nomini töqimang.</p>"
                 "<p>Naşr yöq bölsa, böş «<em lang=\"en\">Publications</em>» bölimini qöymang: loyihalaringizni yozing.</p>",
            take="Naşr, çiqiş va loyiha alohida turadi, har yozuvni tekşirib böladi.",
            task_b="Naşr, çiqiş va loyihalar",
            task=["CV quruvçiga haqiqiy yozuv bölsa qöşing (loyiha ham hisoblanadi).",
                  "Heç narsa bölmasa: keyingi 4 haftada qanday kiçik loyiha qila olasiz? Yozing."]),
        "l5": dict(t=M_TITLES[3][4], min=8,
            hook="«Python ★★★★☆» yoki «Leadership 90%» degan yozuvning mezoni yöq. "
                 "Komissiyani könikma qaysi işda işlatilgani qiziqtiradi. Bu darsda könikma bölimini yozamiz.",
            main='<div class="tbl"><table><thead><tr><th>Guruh</th><th>Misol</th></tr></thead><tbody>'
                 "<tr><td>Dasturlaş va tahlil</td><td>Python, R, statistika: amalda işlatganlaringiz</td></tr>"
                 "<tr><td>GIS va modellaş</td><td>QGIS, geostatistika: loyiha bilan boğlang</td></tr>"
                 "<tr><td>Laboratoriya va dala</td><td>Ölçov, namuna tayyorlaş, aniq asbob</td></tr>"
                 "<tr><td>Tillar</td><td>Til, sertifikat natijasi va yili</td></tr>"
                 "</tbody></table></div>"
                 "<p><b>Til:</b> natijani asl şaklida yozing, masalan <span lang=\"en\">English: IELTS Academic 7.5 (2026)</span>. IELTS ballini özingizça CEFR darajasiga aylantirmang.</p>",
            take="Har könikma yonida u köringan iş turadi; yulduzça va foiz yöq.",
            task_b="Könikma, til, sertifikat",
            task=["CV quruvçining «Könikmalar, tillar, sertifikatlar» qismini töldiring.",
                  "Har könikma uçun mos loyihani eslang."]),
        "l6": dict(t=M_TITLES[3][5], min=10,
            hook="CV tayyor, «Yuboriş» tugmasi yonida turibsiz. Portal Word faylini qabul qilmasligi yoki ikkinçi sahifa kesilib qolişi mumkin. "
                 "Bu darsda yuborişdan oldin uç bosqiçda tekşiramiz.",
            main='<div class="tbl"><table><thead><tr><th>Bosqiç</th><th>Tekşiruv</th></tr></thead><tbody>'
                 "<tr><td>Mazmun</td><td>Daraja, GPA, sana, tajriba va hissa rost va izçilmi?</td></tr>"
                 "<tr><td>Tuzilma</td><td>Bölim tartibi, xronologiya, havolalar, sahifa çegarasi</td></tr>"
                 "<tr><td>Til va fayl</td><td>Imlo, fayl nomi, format, hajm</td></tr>"
                 "</tbody></table></div>"
                 "<p>Oxford da dastur CV sörasa, 1–2 sahifa tavsiya qilinadi va qöşimça hujjatlar PDF, JPG yoki PNG da qabul qilinadi.</p>"
                 "<p>Bu yerdagi Word fayli oddiy .doc. Yuborişdan oldin oçib körin.</p>",
            take="CV ni tanişingizga 30 soniya körsating: u qaysi yönalişni tuşunsa, CV şuni aytyapti.",
            task_b="Yuborişdan oldingi tekşiruv",
            task=["Pastdagi Tahrir nazoratidan 12 bandni tekşiring.",
                  "Tanişingiz CV dan qaysi yönalişni tuşundi? Portal qaysi fayl formatini söraşini ham yozing."]),
    },
)

# ───────────────────────────── M4 ─────────────────────────────
MODULES[4] = dict(
    lead="Bu modulda tavsiya beruvçilarni tanlaymiz, ularga işingiz haqidagi faktlarni beramiz va kerak bölsa professorga birinçi xatni yozamiz. "
         "Oxirida Sizda <strong>Yutuqlar varaqasi</strong>, <strong>söraş xatlari</strong> va <strong>Xatlar daftari</strong> böladi.",
    weeks="2", pass_time="~2 hafta (dars ~1 soat + xatlar)",
    mentor="Ustozingizga hamma narsani bitta paketda, erta va aniq sana bilan bering. Xat sifatiga Siz şu yöl bilan taʼsir qila olasiz.",
    next=("<h2>II bosqiç tugadi</h2>" + bar(60, "II bosqiç: 2 / 2 modul · Rejangiz 60% tayyor") +
          '<div class="mv-k" data-mn="m4"><b>Maqsad bayonnomangizning tayanç qismi allaqaçon bor.</b> M1 dagi hikoyangiz (ötmiş, hozir, maqsad) M5 ga özi köçadi va 4 savolli tuzilmaga joylanadi.</div>'
          "<p><b>III bosqiçda (M5–M6) Sizni kutayotgan darslar:</b></p>" + lock(tl(5) + tl(6)) +
          '<p class="mv-small">M5 va M6 ga taxminan 4 hafta ajrating. Dasturingiz tadqiqot loyihasi taklifini sörmasa, M6 dan faqat birinçi darsni körasiz.</p>'
          '<div class="mv-row"><a class="btn btn-p" href="master-lab-o.html?m=5">III bosqiçni boşlaş</a>'
          '<a class="btn btn-g" href="master-lab-narxlar.html">Tariflarni soliştiriş</a></div>'
          '<p class="mv-small">«1 ta bosqich» tarifida III bosqiç navbatdagi tölov bilan, tölov qilingan zahoti oçiladi.</p>'),
    lessons={
        "l1": dict(t=M_TITLES[4][0], min=10,
            hook="Dekan Sizni bir marta körgan, kurs rahbaringiz esa bir yil bilan işlagan. Komissiya uçun ikkinçisining xati foydaliroq: "
                 "unda aniq voqealar böladi. Bu darsda kuçli tavsiya xati nimadan iboratligini köramiz.",
            main="<p>Tavsiya xatini işingizni körgan odam öz nomidan yozadi. Yaxşi xatda:</p>"
                 "<ul><li><b>Taniş:</b> qaçondan, qaysi kurs yoki loyihada.</li>"
                 "<li><b>Körilgan dalil:</b> mustaqil iş, tahlil, taşabbus, natija.</li>"
                 "<li><b>Dasturga mos könikma.</b></li>"
                 "<li><b>Soliştirma baho</b> faqat tavsiya beruvçi asoslay olsa. «Eng yaxşi 5%» raqamini Siz taklif qilmaysiz.</li></ul>"
                 "<p><b>Kim yuklaydi:</b> Oxford va Cambridge da tavsiya beruvçi özi portalga yuklaydi. Chevening da keyingi bosqiçga ötsangiz, xatni özingiz yuklaysiz.</p>",
            info="<p>Ustozga CV, baholar va eslatma berişingiz mumkin. Uning örniga tayyor xat yozib berib, uni mustaqil baho deb körsatmang. "
                 "Portalda <em lang=\"en\">FERPA waiver</em> kabi tanlov bölsa, maʼnosini tuşunib, özingiz qaror qiling.</p>",
            take="Tavsiya xatini işingizni körgan odam yozsin. Unvon ikkinçi örinda.",
            task_b="Tez test: töğri yoki notöğri?"),
        "l2": dict(t=M_TITLES[4][1], min=10,
            hook="Ustozingiz rozi, lekin xatni ertaga yuborişi kerakligini bugun bildi. Şoşilib yozilgan xat qisqa va umumiy çiqadi. "
                 "Bu darsda kimdan va qaçon söraşni rejalaymiz.",
            main="<p>Avval dastur nechta tavsiya, qaysi turda (akademik yoki kasbiy) va qaysi yöl bilan söraşini aniqlang.</p>"
                 "<ul><li><b>Akademik:</b> kurs öqituvçisi, bitiruv işi rahbari.</li>"
                 "<li><b>Kasbiy:</b> bevosita iş rahbari, agar dastur qabul qilsa.</li>"
                 "<li><b>Zaxira:</b> birinçisi rad etsa, ikkinçi nomzod tayyor tursin.</li></ul>"
                 '<div class="tbl"><table><thead><tr><th>Qaçon</th><th>Nima qilasiz</th></tr></thead><tbody>'
                 "<tr><td>6–8 hafta oldin</td><td>Roziligini söraysiz, dastur va sanani aytasiz</td></tr>"
                 "<tr><td>Rozilikdan keyin</td><td>CV, dastur havolasi va Yutuqlar varaqasini yuborasiz</td></tr>"
                 "<tr><td>Sanaga yaqin</td><td>Portalni tekşirasiz, kerak bölsa muloyim eslatasiz</td></tr>"
                 "<tr><td>Oxirida</td><td>Rahmat aytasiz va natijani ulaşasiz</td></tr>"
                 "</tbody></table></div>",
            info="<p>6–8 hafta bizning ehtiyot tavsiyamiz, universitet talabi emas. Vosita nomzodlarni Siz kiritgan 4 mezon böyiça tartiblaydi; bu ball xat sifatini bildirmaydi.</p>",
            take="Ruxsatni erta söraysiz, materialni bitta paketda berasiz va zaxira nomzodni tayyor tutasiz.",
            task_b="Tavsiya beruvçilaringiz",
            task=["Pastdagi Tavsiya beruvçi tanloviga kamida 2 ta nomzod kiriting va söraş sanasini hisoblang.",
                  "Birinçi nomzodga söraş xatining 3–4 jumlali qoralamasini yozing."]),
        "l3": dict(t=M_TITLES[4][2], min=12,
            hook="Ustozingiz Sizni yaxşi eslaydi, lekin uç yil oldingi loyihangiz tafsilotini unutgan. "
                 "Bitta sahifalik eslatma xatni aniq qiladi. Bu darsda şu sahifani tayyorlaymiz.",
            main="<p>Yutuqlar varaqasi ustozga faktlarni eslatadi. Xatni u baribir öz fikri bilan yozadi.</p>"
                 '<div class="tbl"><table><thead><tr><th>Bölim</th><th>Nima yoziladi</th></tr></thead><tbody>'
                 "<tr><td>1. Dastur va sana</td><td>Universitet, qabul yili, havola, xat yuboriş yöli</td></tr>"
                 "<tr><td>2. Qanday tanişasiz</td><td>Fan, loyiha yoki iş davri</td></tr>"
                 "<tr><td>3. Maqsad</td><td>Nega şu dasturga topşiryapsiz</td></tr>"
                 "<tr><td>4. Dalillar</td><td>Baho, sertifikat, mukofot, iş natijasi</td></tr>"
                 "<tr><td>5. Voqealar</td><td>U özi körgan 1–3 vaziyat</td></tr>"
                 "<tr><td>6. Könikmalar</td><td>Urğu berişi mumkin bölgan sifatlar; tanlovi unda</td></tr>"
                 "</tbody></table></div>",
            info="<p>Ustozning şaxsiy telefon va emailini faqat rasmiy portalga kiriting. Bu vositaga boşqa odamning ortiqça şaxsiy maʼlumotini yozmang.</p>",
            take="Varaqada faqat rost fakt va voqea turadi. Bahoni ustozingiz özi beradi.",
            task_b="Birinçi ustoz uçun Yutuqlar varaqasi",
            task=["Pastdagi Yutuqlar varaqasi quruvçisida 6 bölimni töldiring.",
                  "Ikkinçi ustozga qaysi boşqa loyihani eslatasiz? Yozing."]),
        "l4": dict(t=M_TITLES[4][3], min=12,
            hook="Öquv magistraturasiga topşirayotgan odam professorga xat yozib, javob kutib ikki hafta yöqotdi. Dastur bunday xatni talab qilmagan ekan. "
                 "Bu darsda xat qaçon kerakligini va qanday yozilişini köramiz.",
            main="<p><b>Avval tekşiring:</b> dastur sahifasida «<em lang=\"en\">Do I need to contact anyone before I apply?</em>» kabi bölim bormi? "
                 "Professor bilan oldindan gaplaşiş köpinça tadqiqot magistraturasida kerak, öquv magistraturasida odatda şart emas.</p>"
                 '<div class="tbl"><table><thead><tr><th>Qism</th><th>Mazmun</th></tr></thead><tbody>'
                 "<tr><td>Mavzu qatori</td><td>Dastur, qabul yili, yönaliş</td></tr>"
                 "<tr><td>Taniştiriş</td><td>Kimsiz, nima öqigansiz, nega yozyapsiz</td></tr>"
                 "<tr><td>Moslik</td><td>Uning aniq işi va Sizning tegişli tajribangiz</td></tr>"
                 "<tr><td>Savol</td><td>Bitta, javob beriş oson savol</td></tr>"
                 "<tr><td>Yakun</td><td>Rahmat, ism, CV havolasi</td></tr>"
                 "</tbody></table></div>"
                 "<p>Hajm 150–200 söz atrofida. Bu bizning tavsiyamiz.</p>",
            take="Xatni faqat dastur ruxsat bersa va haqiqiy sabab bölsa yozasiz. Uning işini öqimay yozilgan xatga odatda javob kelmaydi.",
            task_b="Professorga xat",
            task=["Pastdagi Xat quruvçida bitta professor uçun qisqa xat yarating.",
                  "Yuborişdan oldin uning amaldagi işini rasmiy sahifadan öqing."]),
        "l5": dict(t=M_TITLES[4][4], min=8,
            hook="Xat yubordingiz, bir hafta jimlik. Bu arizangiz rad etildi degani emas: professor safarda yoki xatlari köp bölişi mumkin. "
                 "Bu darsda har javobga tayyor turamiz.",
            main="<p><b>Eslatma:</b> 7–10 iş kunidan keyin bitta qisqa xat. Kafedraning öz qoidasi bölsa, şunga amal qiling.</p>"
                 '<div class="tbl"><table><thead><tr><th>Javob</th><th>Keyingi qadam</th></tr></thead><tbody>'
                 "<tr><td>Suhbatga taklif</td><td>Vaqtni kelişasiz, uning işini va dastur şartini öqiysiz</td></tr>"
                 "<tr><td>«Ariza topşiring»</td><td>Rahmat aytasiz va portal orqali topşirasiz</td></tr>"
                 "<tr><td>Joy yöq</td><td>Rahmat aytasiz, boşqa guruhlarni qidirasiz</td></tr>"
                 "<tr><td>Javob yöq</td><td>Bitta eslatma, keyin boşqa variantlar</td></tr>"
                 "</tbody></table></div>"
                 "<p><b>Suhbatga:</b> 60 soniyalik taniştiruv, uning 1–2 işi, 3 ta savol (loyiha hajmi, usul, kerak bölsa pul), vaqt mintaqasi.</p>",
            take="Bitta eslatma yuborasiz va kutib qolmasdan boşqa variantlar bilan davom etasiz. Professorning ijobiy javobi rasmiy qabul emas.",
            task_b="Suhbat rejasi"),
        "l6": dict(t=M_TITLES[4][5], min=8,
            hook="Uç ustoz, ikki professor, beşta xat. Kimga qaçon yozganingiz va kim javob bergani bir oydan keyin esdan çiqadi. "
                 "Bu darsda hammasini bitta daftarga yozamiz.",
            main='<div class="tbl"><table><thead><tr><th>Ustun</th><th>Nima yoziladi</th></tr></thead><tbody>'
                 "<tr><td>Ism va rol</td><td>Ustoz yoki professor</td></tr>"
                 "<tr><td>Dastur</td><td>Qaysi ariza bilan boğliq</td></tr>"
                 "<tr><td>Sana</td><td>Xat yuborilganmi yoki rejadami</td></tr>"
                 "<tr><td>Holat</td><td>Yuborildi, javob kutilmoqda, rozi, rad, yakunlandi</td></tr>"
                 "<tr><td>Keyingi qadam</td><td>Yuborilgan kundan 10 kun keyin</td></tr>"
                 "</tbody></table></div>"
                 "<p>Daftar 10 kalendar kunini sanaydi (dam oliş kunlari bilan). M4.5 dagi 7–10 iş kuni bilan farqini hisobga oling.</p>",
            info="<p>CSV faylni boşqa odamga yuborişdan oldin içidagi şaxsiy maʼlumotni tekşiring. Tavsiya xati kelgan-kelmaganini rasmiy portaldan bilasiz.</p>",
            take="Hamma xat bitta daftarda bölsa, eslatma vaqtini ötkazib yubormaysiz.",
            task_b="Sizning Xatlar daftaringiz",
            task=["Pastdagi Xatlar daftariga kamida 4 ta reja yoki haqiqiy aloqa kiriting. Öquv magistraturasida professorni sunʼiy qöşmang.",
                  "Daftarni CSV qilib saqlang."]),
    },
)

# ───────────────────────────── M5 ─────────────────────────────
# M5–M8 da Diqqat qismlari voqea bilan boşlanadi va yaxşi işlaydi: asosan saqlanadi.
MODULES[5] = dict(
    lead="Bu modulda <strong>700–1 000 sözlik maqsad bayonnomasi</strong>ni yozamiz va uni ikki dasturga moslaymiz. "
         "Asosi M1 dagi hikoyangiz va M3 dagi tajriba qatorlari.",
    weeks="2", pass_time="~2 hafta (dars ~1,5 soat + 4 ta yoziş seansi)",
    next=("<h2>Keyingi qadam: taklif kerakmi?</h2>" + bar(70, "III bosqiç: 1 / 2 modul · Rejangiz 70% tayyor") +
          '<div class="mv-k" data-mn="m5"><b>Dasturlaringiz tadqiqot loyihasi taklifini söraydimi?</b> M6.1 da 2 daqiqada bilib olasiz. '
          "Söramasa, M6 ni ötkazib, M7 ga öting: vaqtingiz stipendiyalarga qoladi.</div>"
          '<div class="mv-row"><a class="btn btn-p" href="master-lab-o.html?m=6">M6: taklif kerakmi?</a>'
          '<a class="btn btn-g" href="master-lab-o.html?m=7">Kerak emas, M7 ga</a></div>'),
    lessons={
        "l1": dict(t=M_TITLES[5][0], min=10, take="Har dastur söragan hujjat nomi, savoli va çegarasi alohida yoziladi."),
        "l2": dict(t=M_TITLES[5][1], min=10, take="4 savol bitta çiziqda: kimsiz, nima isbotlaydi, nimaga erişmoqçisiz, nega aynan şu dastur."),
        "l3": dict(t=M_TITLES[5][2], min=12, take="Moslik paragrafida aniq kurs, professor yoki laboratoriya va u bilan nima qilişingiz turadi."),
        "l4": dict(t=M_TITLES[5][3], min=10, take="Har sifat bitta voqea bilan isbotlanadi: vaziyat, harakat, natija va undan çiqqan fikr."),
        "l5": dict(t=M_TITLES[5][4], min=10, take="Örtadan boşlaysiz, kirişni oxirida yozasiz. Yoziş va tahrir alohida kunlarda."),
        "l6": dict(t=M_TITLES[5][5], min=12, take="Tahrir uç bosqiçda: tuzilma, dalil, til. Universitet nomini har versiyada qayta tekşirasiz."),
        "l7": dict(t=M_TITLES[5][6], min=8, take="Namunadan jumla olmaysiz, qanday tuzilganini olasiz."),
    },
    fix=[
        ("Komissiya sifatlarni emas, ular köringan hodisalarni qidiradi.", "Komissiya har sifatning orqasidagi voqeani qidiradi."),
        ("Asosiy qoida: sifat emas, hodisa (show, don’t tell).", "Asosiy qoida: sifat örniga voqea yozing (<em lang=\"en\">show, don’t tell</em>)."),
        ("Namunadan nusxa emas, mexanizm olinadi.", "Namunadan jumla olmang, qanday tuzilganini köring."),
        ("Bu matn yaxşiligidan emas: miyangiz nima yozganingizni biladi va körgan narsani emas, eslagan narsani öqiydi.",
         "Sabab oddiy: miyangiz matnni yod biladi va sahifadagini emas, esidagini öqiydi."),
        ("Maqsad aniq bölsin: “dunyoni özgartiriş” emas, “suv resurslari agentligida monitoring tizimini loyihalaş”.",
         "Maqsad aniq bölsin: “suv resurslari agentligida monitoring tizimini loyihalaş” kabi."),
        ("“Siz kimsiz?” qismi bolalikdan emas, hozirgi savolingizdan boşlanadi.", "“Siz kimsiz?” qismi hozirgi savolingizdan boşlanadi, bolalikdan boşlanmaydi."),
    ],
)

# ───────────────────────────── M6 ─────────────────────────────
MODULES[6] = dict(
    lead="Tadqiqot loyihasi taklifi hamma magistraturada söralmaydi. Birinçi dars 10 daqiqada buni aniqlaydi. "
         "Kerak bölsa, <strong>1 500–3 000 sözlik taklif</strong>ni savol, adabiyot, usul va reja bilan yozamiz.",
    weeks="2", pass_time="~2 hafta, agar taklif kerak bölsa (dars ~1,5 soat + yoziş)",
    next=("<h2>III bosqiç tugadi</h2>" + bar(80, "III bosqiç: 2 / 2 modul · Rejangiz 80% tayyor") +
          '<div class="mv-k" data-mn="m6"><b>Endi pul masalasi.</b> Arizalar jadvalingizdagi stipendiyalar va ularning sanalari şu yerda körinadi.</div>'
          "<p><b>IV bosqiçda (M7–M8) Sizni kutayotgan darslar:</b></p>" + lock(tl(7) + tl(8)) +
          '<div class="mv-row"><a class="btn btn-p" href="master-lab-o.html?m=7">IV bosqiçni boşlaş</a>'
          '<a class="btn btn-g" href="master-lab-narxlar.html">Tariflarni soliştiriş</a></div>'
          '<p class="mv-small">«1 ta bosqich» tarifida IV bosqiç navbatdagi tölov bilan, tölov qilingan zahoti oçiladi.</p>'),
    lessons={
        "l1": dict(t=M_TITLES[6][0], min=8,
            take="Dasturingiz taklif sörmasa, bu modulni şu yerda tugatib M7 ga ötasiz. Sörasa, keyingi darslar Sizga."),
        "l2": dict(t=M_TITLES[6][1], min=10, take="Voronka: global muammo → kontekst → böşliq → aniq savol."),
        "l3": dict(t=M_TITLES[6][2], min=15, take="Şarh maqolalarni birma-bir aytib bermaydi: ularni mavzu böyiça guruhlab, böşliqqa olib keladi."),
        "l4": dict(t=M_TITLES[6][3], min=12, take="Dizayn, maʼlumot, usul va çeklov: har biri magistratura muddatiga siğadi."),
        "l5": dict(t=M_TITLES[6][4], min=10, take="4–6 bosqiç, har biri aniq natija bilan, umumiy vaqtning 10–15% zaxira."),
        "l6": dict(t=M_TITLES[6][5], min=8, take="Natijani ehtiyotkor til bilan yozasiz: «tekşiradi», «kutiladi»."),
        "l7": dict(t=M_TITLES[6][6], min=10, take="Bitta iqtibos uslubi oxirigaça, har manba DOI yoki naşriyot sahifasi bilan tekşirilgan."),
    },
    fix=[
        ("Bu mavzu emas, butun soha.", "Bu butun soha, mavzu hali yöq."),
        ("Komissiya buni körib, rejani emas, reja tuziş tajribasi yöqligini köradi.", "Bunday rejani körgan komissiya muallif hali tadqiqot qilmaganini tuşunadi."),
        ("Taklif — reja, vaʼda emas.", "Taklif reja hisoblanadi, vaʼda hisoblanmaydi."),
        ("Sharh = sintez, xulosa emas", "Şarh: guruhlaş va soliştiriş"),
    ],
)

# ───────────────────────────── M7 ─────────────────────────────
MODULES[7] = dict(
    lead="Bu modulda profilingizga mos <strong>3 ta stipendiya</strong> tanlaymiz: avval majburiy şartlar, keyin moslik va sana. "
         "Faktlar sana va rasmiy havola bilan berilgan.",
    weeks="2", pass_time="~2 hafta (dars ~1,5 soat + qidiruv)",
    next=("<h2>Keyingi qadam: suhbat</h2>" + bar(90, "IV bosqiç: 1 / 2 modul · Rejangiz 90% tayyor") +
          '<div class="mv-k" data-mn="m7"><b>Tanlagan stipendiyalaringiz böyiça suhbat savollari</b> M8 da. '
          "Komissiya savollarining köpi Siz yozgan jumlalardan tuğiladi: javobni ovoz çiqarib maşq qilasiz.</div>"
          '<div class="mv-row"><a class="btn btn-p" href="master-lab-o.html?m=8">M8: suhbatga tayyorlaniş</a></div>'),
    lessons={
        "l1": dict(t=M_TITLES[7][0], min=10, take="Majburiy şart filtr, moslik esa baho. Avval har şartni rasmiy matndan tekşirasiz: fuqarolik, ish tajribasi, daraja sanasi, yoş, til, qaytiş majburiyati."),
        "l2": dict(t=M_TITLES[7][1], min=10), "l3": dict(t=M_TITLES[7][2], min=8), "l4": dict(t=M_TITLES[7][3], min=10),
        "l5": dict(t=M_TITLES[7][4], min=10), "l6": dict(t=M_TITLES[7][5], min=8),
        "l7": dict(t=M_TITLES[7][6], min=8,
            hook="El-yurt umidi haqida «har kimga beriladi» degan gapni eşitdingiz va tanlov eʼloni yopilgandan keyin bildingiz. "
                 "Mahalliy dasturning ham öz sanasi va filtri bor. Bu darsda Özbekiston dasturlari va universitet grantlarini körib çiqamiz."),
        "l8": dict(t=M_TITLES[7][7], min=12),
    },
)

# ───────────────────────────── M8 ─────────────────────────────
MODULES[8] = dict(
    lead="Bu modulda suhbatga tayyorlanamiz, qabul xatini öqiymiz va jönaş rejasini tuzamiz. "
         "Oxirida Sizda <strong>3 ta baholangan javob</strong>, <strong>5 daqiqalik taqdimot</strong> va <strong>jönaş röyxati</strong> böladi.",
    weeks="2", pass_time="~2 hafta (dars ~1,5 soat + maşq)",
    next=("<h2>Magistratura dasturi tugadi</h2>" + bar(100, "IV bosqiç: 2 / 2 modul · Rejangiz 100% tayyor") +
          '<div class="mv-k" data-mn="m8"><b>Sizning ariza paketingiz:</b> dasturlar röyxati (M1), sanalar (M2), CV (M3), tavsiya sörövlari (M4), '
          "maqsad bayonnomasi (M5), kerak bölsa taklif (M6), stipendiyalar (M7), suhbat va jönaş (M8).</div>"
          "<p>Kabinetdagi «Mening yölim» da topşiriş kunigaça qolgan vaqt va keyingi qadam turadi.</p>"
          '<div class="mv-row"><a class="btn btn-p" href="dashboard.html">Kabinetga ötiş</a></div>'),
    lessons={
        "l1": dict(t=M_TITLES[8][0], min=8), "l2": dict(t=M_TITLES[8][1], min=12),
        "l3": dict(t=M_TITLES[8][2], min=10), "l4": dict(t=M_TITLES[8][3], min=12),
        "l5": dict(t=M_TITLES[8][4], min=10), "l6": dict(t=M_TITLES[8][5], min=8),
        "l7": dict(t=M_TITLES[8][6], min=12), "l8": dict(t=M_TITLES[8][7], min=8),
    },
    fix=[
        ("Bu savol tarjimai hol emas, suhbatning xaritasi.", "Bu savolga 1 daqiqada javob bering: kimsiz, nima qilgansiz, nega şu dastur."),
    ],
)
