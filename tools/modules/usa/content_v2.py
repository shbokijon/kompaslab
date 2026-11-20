# USA dasturi M1–M8 v2 kontenti (2026-11-20, Magistratura v2 andozasi).
# YANGI alifboda yoziladi (Ö, Ğ, Ş, Ç, ʼ); engine.py manbaga amaldagi alifboda (oʻ, gʻ, sh, ch) yozadi.
# [[...]] → <span lang="en">. Har dars: t, short, min, hook, fun (ixtiyoriy), main, info, info_t, take,
# task_b, task (röyxat), ph (ixtiyoriy), src (manba havolalari, common.py dan).
# Berilmagan kalit mods/m<N>.py dagi eski qiymatda qoladi (quiz, ic, kind, vositalar, nazorat, js).
from common import *

SUB = "Har dars 4 qism: Diqqat, Asosiy qism, Xulosa, Topşiriq. Har qism 1–3 daqiqa."
DISCLAIMER = ("Kompas Lab universitet, elchixona yoki konsul örnida qaror qabul qilmaydi va qabul, yordam yoki vizani kafolatlamaydi. "
              "Vositalar sana va talablarni siz uçun tekşirmaydi: har faktni rasmiy sahifadan özingiz tasdiqlaysiz. "
              "Viza va soliq böyiça yuridik maslahat berilmaydi. Sanasi körsatilgan maʼlumot şu sanadagi holat.")

M_TITLES = {
    1: ["Universitet turlari", "Universitet haqiqiymi?", "AQŞ darajasi qanday tuzilgan?", "Sohangiz qayerda kuçli?", "Universitetni raqam bilan öqiş"],
    2: ["Töliq narx qança?", "I-20 uçun mablağ hujjatlari", "Qaysi mablağ manbalari sizga oçiq?", "Ehtiyoj granti va natija granti", "Budjetingiz çegarasi"],
    3: ["Tört xil yordam siyosati", "Rasmiy sahifa iboralari", "CDS H6: kim qança oldi?", "Net Price Calculator va grantlar", "Ikki öqli röyxat"],
    4: ["Qaysi universitet qaysi forma", "Ota-ona daromadini hujjatlaş", "Forma tölovi", "Yordam xatini öqiş", "Qayta körib çiqişni söraş"],
    5: ["Global UGRAD nima?", "Sizga mos keladimi?", "Sikl eʼlonini kuzatiş", "Ariza va tanlov", "Boşqa almaşinuvlar va J-1"],
    6: ["Fulbright kimga mos keladi?", "Tanlov qanday ötadi?", "Ariza va halollik", "Sikl kalendari", "J-1 va 2 yillik talab"],
    7: ["Mablağ qayerdan keladi: magistratura va PhD", "PhD moliya paketi", "Kafedra sahifasi: 10 savol", "Taşqi grantlar kimga oçiq?", "Takliflarni soliştiriş"],
    8: ["F-1 yoki J-1?", "Toşkentda viza", "Maqomni saqlaş", "F-1 da işlaş", "Siyosat özgarişini kuzatiş"],
}


def lock(items):
    return '<ul class="mv-lock">' + "".join('<li><img src="img/3d/lock.webp" alt="" width="22" height="22">%s</li>' % x for x in items) + "</ul>"


def bar(p, label):
    return '<div class="mv-bar"><i style="width:%d%%"></i></div><p class="mv-small">%s</p>' % (p, label)


def tl(n):
    return ["%d.%d %s" % (n, i + 1, t) for i, t in enumerate(M_TITLES[n])]


TARIF = ('<p class="mv-small">Keyingi bosqiç 1 ta bosqiç tarifida navbatdagi tölov bilan oçiladi. '
         'Töliq dastur tarifida hamma modul allaqaçon oçiq.</p>')

MODULES = {}

# ───────────────────────────── M1 ─────────────────────────────
MODULES[1] = dict(
    lead="Bu modulda AQŞ universitetlarini turiga ajratasiz va har birining haqiqiyligini tekşirasiz. "
         "Oxirida sizda <strong>universitet tekşiruv kartasi</strong> böladi: tur, akkreditatsiya, SEVP, soha böyiça kuç va asosiy raqamlar.",
    weeks="1", pass_time="~1 hafta (darslar ~1 soat + karta)",
    next=("<h2>Keyingi qadam: narx</h2>" + bar(13, "I bosqiç: 1 / 2 modul · Rejangiz 13% tayyor") +
          '<div class="mv-k" data-mn="m1"><b>Kartangizdagi universitet haqiqiy va viza bera oladi.</b> Endi savol boşqa: '
          "bir yili qançaga tuşadi va <b>budjetingiz</b> bunga yetadimi? M2 da şuni raqam bilan hisoblaymiz.</div>"
          '<p>M2.1 dan: <i>Öqiş tölovi universitet söraydigan <b>mablağning</b> faqat bir qismi. I-20 töliq narxga qarab yoziladi.</i></p>'
          '<div class="mv-row"><a class="btn btn-p" href="usa-lab-o.html?m=2">M2: töliq narxni hisoblaş</a></div>'),
    lessons=[
        dict(t=M_TITLES[1][0], short="Turlar", min=10,
             hook="«AQŞ universiteti» degan söz ikki yillik kollejni ham, yiliga yuzlab doktor tayyorlaydigan markazni ham bildiradi. "
                  "Turini bilmasangiz, arzon yölni körmay qolasiz. Bu darsda tört turni ajratamiz.",
             fun="Hammasining sayti bir xil çiroyli, bu ham bir sinov 🙂",
             main="""<div class="tbl"><table><thead><tr><th>Tur</th><th>Nima beradi</th><th>Kimga mos</th></tr></thead><tbody>
<tr><td>Ikki yillik kollej ([[community college]])</td><td>2 yillik dastur, keyin tört yillik universitetga ötiş ([[transfer]])</td><td>Xarajatni kamaytirmoqçi bölgan bakalavr</td></tr>
<tr><td>Liberal sanʼat kolleji</td><td>Asosan bakalavriat, kiçik guruhlar</td><td>Fanlar orasida izlanayotgan bakalavr</td></tr>
<tr><td>Tadqiqot universiteti</td><td>Bakalavr, magistratura, köp doktorantura, laboratoriyalar</td><td>Magistratura, PhD, ilmiy tajriba istagan bakalavr</td></tr>
<tr><td>Davlat yoki xususiy</td><td>Davlat universiteti ştat budjetiga, xususiysi öz jamğarmasiga tayanadi</td><td>Narx va yordam siyosati har xil (M2–M3)</td></tr>
</tbody></table></div>""",
             info_t="R1 va R2 nima",
             info="<p>[[Carnegie Classification]] universitetlarni ilmiy faolligi böyiça guruhlaydi. 2025-yilgi metodologiyada R1 uçun yiliga kamida 50 million dollar ilmiy xarajat va 70 ta ilmiy doktorlik darajasi, R2 uçun 5 million dollar va 20 ta daraja çegarasi bor. 2025-yilda 187 ta muassasa R1 bölgan.</p>"
                  "<p>R1 ilmiy faollik ölçovi. PhD va tadqiqot magistraturasi uçun muhim, bakalavr uçun hal qiluvçi signal hisoblanmaydi. EducationUSA ikki yillik kollej orqali ötişni xarajatni kamaytiriş yöllaridan biri sifatida körsatadi; kreditlar qaysi universitetda qabul qilinişini öşa universitet sahifasidan tekşiring.</p>",
             take="Avval turini aniqlang, keyin narxi va yordamini soliştiring. R1 belgisi ilmiy faollik haqida, öqitiş sifati haqida emas.",
             task_b="Sizning uçta muassasangiz",
             task=["Qiziqqan 3 ta muassasani yozing va har birining turini belgilang.", "PhD yoki tadqiqot magistraturasini közlasangiz, R1 yoki R2 ekanini Carnegie sahifasidan tekşiring."],
             src=f"{CARNEGIE}; {EDUSA_UG}. {HOL}."),
        dict(t=M_TITLES[1][1], short="Tekşiruv", min=10,
             hook="Har yili kimdir «AQŞ universiteti» nomidagi saytga tölov qiladi, keyin diplom tan olinmasligini biladi. "
                  "Ikki tekşiruv buni 15 daqiqada oldini oladi. Bu darsda öşa ikkalasini qilamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Tekşiruv</th><th>Qayerda</th><th>Topilmasa</th></tr></thead><tbody>
<tr><td>Akkreditatsiya</td><td>[[CHEA]] bazasi yoki DAPIP (Taʼlim vazirligi)</td><td>Diplom tan olinmasligi mumkin: röyxatdan çiqaring</td></tr>
<tr><td>SEVP sertifikati</td><td>[[Study in the States]] qidiruvi (DHS)</td><td>I-20 bera olmaydi, talaba vizasi bölmaydi</td></tr>
<tr><td>Rasmiy sayt</td><td>Domen odatda .edu; manzilni özingiz qidirib oçasiz</td><td>Xabardagi havolaga işonmang</td></tr>
</tbody></table></div>
<p>«Kafolatli qabul» yoki «I-20 3 kunda» deb reklama qilgan muassasaga ikkala bazada tekşirmaguncha tölov qilmang.</p>""",
             info_t="Akkreditatsiya kim beradi",
             info="<p>AQŞda universitet sifatini hukumat emas, maxsus xususiy taşkilotlar tekşiradi. [[CHEA]] bazasida 8 200 dan ortiq muassasa va 44 000 dan ortiq dastur bor; nom, ştat yoki akkreditatsiya taşkiloti böyiça qidiriladi. Talaba vizasi (F-1) uçun avval SEVP tasdiqlagan muassasaga qabul qilinasiz: aynan şu muassasa Form I-20 beradi.</p>",
             take="Tölovdan oldin uçta tekşiruv:<ul><li><b>akkreditatsiya</b>;</li><li><b>SEVP</b>;</li><li><b>rasmiy sayt</b>.</li></ul>Bittasi topilmasa, muassasa röyxatdan çiqadi.",
             task_b="Uçta muassasani tekşiring",
             task=["Röyxatingizdagi 3 muassasani CHEA yoki DAPIP da va SEVP qidiruvida tekşiring.", "Har biri uçun yozing: akkreditatsiya taşkiloti, SEVP ha yoki yöq, tekşirilgan sana."],
             ph="... — akkreditatsiya: ... (CHEA), SEVP: ha, 20.11.2026",
             src=f"{CHEA}; {DAPIP}; {SITS_SEARCH}; {DOS_VISA}. {HOL}."),
        dict(t=M_TITLES[1][2], short="Darajalar", min=10,
             hook="Özbekistonda yönaliş qabulda tanlanadi. AQŞ bakalavriatida mutaxassislik köpinça keyinroq tanlanadi, magistratura esa ikki xil böladi. "
                  "Bu darsda dastur sahifasini töğri öqişni örganamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Daraja</th><th>Nimani bilib qöyiş kerak</th></tr></thead><tbody>
<tr><td>Bakalavriat</td><td>Asosiy mutaxassislik ([[major]]) köp universitetda birinçi kursdan keyin tanlanadi; muhandislik kabi dasturlar qabulda söraydi. Kredit soni va umumiy fanlar katalogda ([[academic catalog]]) yoziladi</td></tr>
<tr><td>Magistratura</td><td>Dissertatsiyali ([[thesis]]): kurslar + ilmiy iş. Dissertatsiyasiz ([[non-thesis]]): asosan kurslar, moliyalaştiriş odatda kamroq (M7)</td></tr>
<tr><td>PhD</td><td>Köpinça bakalavrdan keyin töğridan-töğri qabul; kurslar, malaka imtihoni ([[qualifying exam]]), dissertatsiya</td></tr>
</tbody></table></div>""",
             info="<p>Aniq tartib kafedra qöllanmasida ([[graduate handbook]]) yoziladi. «Magistraturasiz PhD mumkin» degan qoida hamma kafedraga tegişli bölmasligi mumkin: dastur sahifasidan tekşiring.</p>",
             take="Har qoidani dastur katalogi yoki kafedra qöllanmasidan oling. Bitta universitetda ham kafedralar har xil işlaydi.",
             task_b="Bitta dasturning katalogi",
             task=["Bitta bakalavriat yoki magistratura dasturining katalog sahifasini toping.", "Yozing: kredit soni, majburiy kurslar, dissertatsiya bormi, major qaçon tanlanadi."],
             src=f"{NAV}; {CDS}. {HOL}."),
        dict(t=M_TITLES[1][3], short="Soha", min=12,
             hook="Umumiy reytingda 50-örindagi universitet sizning sohangizda birinçi önlikda bölişi mumkin. "
                  "Bu darsda kuçli joyni reytingdan emas, ilmiy xarajat maʼlumotidan topamiz.",
             main="""<p>NSF qoşidagi NCSES har yili universitetlarning soha böyiça ilmiy xarajatini yiğadi. Bu [[HERD]] sörovi: yiliga 150 ming dollardan köp ilmiy xarajati bor hamma muassasa qamrab olinadi.</p>
<ol><li>HERD jadvalidan sohangizni tanlang.</li><li>Şu sohada xarajati eng katta 15–20 muassasani yozib oling.</li><li>Har birining kafedra sahifasini oçing: professorlar, laboratoriyalar, songgi maqolalar.</li><li>Darajangizga qarab saralang: PhD uçun ilmiy xarajat muhim, bakalavr uçun bitta signal.</li></ol>""",
             info="<p>Ilmiy xarajat laboratoriya va grant hajmini körsatadi, öqitiş sifatini töğridan-töğri ölçamaydi. Xarajat katta bölsa ham, bakalavr talabaga laboratoriyaga kiriş kafolatlanmaydi. Bakalavr uçun bu maʼlumotni yordam siyosati (M3) bilan birga köring.</p>",
             take="Soha böyiça kuçni HERD jadvali va kafedra sahifasi bilan tekşiring. Ikkalasi mos kelsa, muassasa röyxatda qoladi.",
             task_b="Sohangiz böyiça 10 ta joy",
             task=["HERD dan sohangiz böyiça 10 ta muassasani yozing.", "Ulardan 3 tasining kafedrasida sizga yaqin mavzudagi professor yoki laboratoriyani toping."],
             src=f"{HERD}. {HOL}."),
        dict(t=M_TITLES[1][4], short="Raqamlar", min=12,
             hook="Universitet sayti özini eng yaxşi tomondan körsatadi. Rasmiy statistik bazalar esa hamma universitetga bir xil şablondagi raqamni beradi. "
                  "Bu darsda kartangizni şu raqamlar bilan töldiramiz.",
             main="""<p>[[College Navigator]] (NCES, Taʼlim vazirligi) har muassasa böyiça narx, talabalar soni, bitiriş darajasi va akkreditatsiyani bir sahifada beradi. Köp universitet har yili [[Common Data Set]] (CDS) ni bir xil şaklda çop etadi.</p>
<div class="tbl"><table><thead><tr><th>CDS bölimi</th><th>Nima bor</th></tr></thead><tbody>
<tr><td>B</td><td>Talabalar soni, qoliş va bitiriş darajasi</td></tr>
<tr><td>C</td><td>Bakalavriat qabuli, test siyosati</td></tr>
<tr><td>G</td><td>Narxlar</td></tr>
<tr><td>H</td><td>Moliyaviy yordam, jumladan xalqaro talabaga (M3)</td></tr>
</tbody></table></div>""",
             info="<p>CDS ni topiş: qidiruvga «universitet nomi + Common Data Set» yozing va natija universitet domenida (.edu) ekanini tekşiring.</p><p><b>Kartaning 6 qatori:</b></p><ol><li>tur va R darajasi;</li><li>akkreditatsiya va SEVP;</li><li>soha kuçi;</li><li>talabalar soni va xalqaro uluş;</li><li>bitiriş darajasi;</li><li>xalqaro talaba uçun narx.</li></ol>",
             take="Har raqam yonida manba va yil tursin. Şunda bir neça universitetni bir jadvalda soliştira olasiz.",
             task_b="Bitta universitet kartasi",
             task=["Röyxatingizdagi bitta universitet uçun 6 qatorli kartani töldiring.", "Har raqam yonida manba (Navigator yoki CDS yili) va sana yozing."],
             src=f"{NAV}; {CDS}. {STD}"),
    ])

# ───────────────────────────── M2 ─────────────────────────────
MODULES[2] = dict(
    lead="AQŞda qabul xati yetarli emas: I-20 uçun birinçi yil xarajatini <b>mablağ hujjati</b> bilan körsatasiz. "
         "Bu modulda <b>töliq narxni</b>, sizga yopiq <b>mablağ manbalarini</b> va yiliga qança tölay olişingizni raqam bilan aniqlaysiz. "
         "Oxirida sizda <strong>xarajat va budjet rejasi</strong> böladi.",
    weeks="1", pass_time="~1 hafta (darslar ~1 soat + hisoblagiç)",
    next=("<h2>I bosqiç yakunlandi: keyingi qadam yordam</h2>" + bar(25, "I bosqiç: 2 / 2 modul · Rejangiz 25% tayyor") +
          '<div class="mv-k" data-mn="m2"><b>Xarajat va budjet rejangiz tayyor.</b> Endi kerakli yordam uluşini qoplaydigan universitetlarni topiş qoladi. '
          "II bosqiçda (M3–M4) ularni rasmiy sahifa va CDS H6 bilan saralaysiz, keyin yordam arizasini tayyorlaysiz.</div>"
          "<p>II bosqiç darslari:</p>" + lock(tl(3) + tl(4)[:2]) + TARIF +
          '<div class="mv-row"><a class="btn btn-p" href="usa-lab-o.html?m=3">II bosqiç: M3 ni oçiş</a><a class="btn btn-g" href="usa-lab-narxlar.html">Tariflar</a></div>'),
    lessons=[
        dict(t=M_TITLES[2][0], short="Narx", min=12,
             hook="Öqiş tölovi ([[tuition]]) universitet söraydigan mablağning faqat bir qismi. <b>Töliq narx</b> [[Cost of Attendance]] deb eʼlon qilinadi, yordam ham, I-20 ham şunga qarab hisoblanadi. "
                  "Bu darsda narxni qatorlarga ajratamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Qator</th><th>Qayerdan olinadi</th></tr></thead><tbody>
<tr><td>Öqiş tölovi va yiğimlar</td><td>[[tuition and fees]] sahifasi, xalqaro yoki ştatdan taşqari ([[nonresident]]) narx</td></tr>
<tr><td>Yaşaş (yotoqxona, ovqat)</td><td>[[Cost of Attendance]] yoki [[housing]] sahifasi</td></tr>
<tr><td>Tibbiy suğurta</td><td>Xalqaro talabalar bölimi</td></tr>
<tr><td>Kitob, transport, şaxsiy</td><td>[[Cost of Attendance]] sahifasi</td></tr>
<tr><td>Bir martalik: viza yiğimi, SEVIS, aviabilet</td><td>Elçixona va ICE (M8)</td></tr>
</tbody></table></div>
<p>EducationUSA öqiş tölovining har yili taxminan 6–10 foiz oşişini hisobga olişni maslahat beradi.</p>""",
             info="<p>Kennesaw State universiteti bir yillik xarajatni uç qatorga ajratadi: öqiş va yiğimlar, yaşaş, boşqa xarajatlar (majburiy suğurta, transport, kitob). Boşqa universitetlarda qator nomlari farq qiladi. Summa qaysi öquv yili uçun ekanini yozib qöying: kelasi yil narxi hali eʼlon qilinmagan bölişi mumkin.</p>",
             take="Töliq narx = öqiş + yaşaş + suğurta + kitob va şaxsiy xarajat + bir martalik tölovlar. Keyingi yillarga 6–10 foiz qöşing.",
             task_b="Bitta universitet narxi",
             task=["Bitta universitetning xalqaro talaba uçun Cost of Attendance summasini qatorlari bilan yozing.", "Öquv yili, havola va tekşirilgan sanani qöşing."],
             src=f"{KSU}; {EDUSA_UG}; {SEVIS}. {HOL}."),
        dict(t=M_TITLES[2][1], short="I-20", min=12,
             hook="Köpçilik: uy bor, maşina bor, demak mablağ bor, deb öylaydi. I-20 berişda universitet mulkni körmaydi, <b>hozir işlatsa böladigan mablağni</b> köradi. "
                  "Bu darsda qaysi hujjat qabul qilinişini ajratamiz.",
             main="""<p>Kamida birinçi öquv yilining taxminiy xarajati körsatiladi (Kennesaw State, San José State).</p>
<div class="tbl"><table><thead><tr><th>Qabul qilinadi</th><th>Qabul qilinmaydi</th></tr></thead><tbody>
<tr><td>Bank xati yoki köçirmasi</td><td>Iş joyidan maoş haqida xat</td></tr>
<tr><td>Muddatli omonat, jarimasiz oliş mumkinligi yozilgan bölsa</td><td>Uy, oltin, zargarlik baholaş hujjati</td></tr>
<tr><td>Tasdiqlangan kredit xati</td><td>Aksiya va fond köçirmasi</td></tr>
<tr><td>Stipendiya xati</td><td>Kredit liniyasi xati</td></tr>
</tbody></table></div>
<p class="mv-small">Namuna: San José State. Öz universitetingiz sahifasini öqing.</p>""",
             info="<p>San José State da hujjat AQŞ dollarida, ingliz tilida, bank blankida, muhr yoki imzo bilan va arizadan oldingi 6 oy içida berilgan bölişi kerak. Qoidalar universitetga qarab farq qiladi: [[financial documents]] yoki [[I-20 request]] sahifasini oçing.</p>"
                  "<p>Begona mablağni vaqtinça hisobga qöyib turiş halollik va viza suhbati uçun xavfli: konsul mablağ manbasini söraşi mumkin.</p>",
             take="I-20 uçun birinçi yil narxini <b>işlatsa böladigan mablağ</b> bilan körsatasiz. <b>Mulk</b> va <b>maoş xati</b> köpinça hisobga olinmaydi.",
             task_b="Sizning mablağ hujjatlaringiz",
             task=["Qaysi hujjatni bera olişingizni yozing: bank köçirmasi, omonat, stipendiya, kredit (oila yordami bölsa, uning hujjati ham).", "Ular birinçi yil narxini qoplaşini yoki qoplamasligini hisoblang."],
             src=f"{KSU}; {SJSU}. {HOL}."),
        dict(t=M_TITLES[2][2], short="Manbalar", min=10,
             hook="AQŞ talabalarining köpi federal grant va kreditdan foydalanadi. Bu yordam xalqaro talabaga yopiq, şuning uçun AQŞ talabalariga yozilgan maslahatlarning yarmi sizga töğri kelmaydi. "
                  "Bu darsda sizga oçiq manbalarni ajratamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Manba</th><th>Xalqaro talabaga</th></tr></thead><tbody>
<tr><td>Federal grant va kredit</td><td>Yopiq (Taʼlim vazirligi)</td></tr>
<tr><td>Universitetning ehtiyoj granti</td><td>Ayrim universitetlarda (M3)</td></tr>
<tr><td>Universitetning natija granti</td><td>Köpinça qisman (2.4)</td></tr>
<tr><td>Sport stipendiyasi</td><td>Sport bilan şuğullanuvçilarga (EducationUSA)</td></tr>
<tr><td>Davlat dasturlari</td><td>Global UGRAD, Fulbright (M5–M6)</td></tr>
<tr><td>Kafedra moliyasi</td><td>Asosan PhD (M7)</td></tr>
<tr><td>Kampusda işlaş</td><td>Haftasiga 20 soatgaça, qöşimça daromad (M8)</td></tr>
</tbody></table></div>""",
             info="<p>AQŞ Taʼlim vazirligi böyiça, talaba AQŞ fuqarosi yoki belgilangan toifadagi fuqaro bölmagan şaxs ([[eligible noncitizen]]) bölmasa, federal yordam olmaydi. Ohio State yozişiça, xalqaro talabalar odatda federal, ştat va köp universitet yordamini ololmaydi.</p>"
                  "<p>«AQŞda işlab öqiş tölovini qoplayman» rejasi qonun böyiça mumkin bölmaydi: kampusdan taşqari iş yozma ruxsat bilan, kampusda esa soat çeklangan.</p>",
             take="<b>Federal yordam</b> yopiq. Sizga oçiq manbalar:<ul><li>universitet yordami va stipendiya;</li><li>davlat dasturi;</li><li>kafedra moliyasi;</li><li>öz <b>budjetingiz</b>.</li></ul>",
             task_b="Sizga real manbalar",
             task=["Jadvaldagi manbalardan sizga real bölganlarini belgilang.", "Har biri uçun bir jumla: nega real yoki nega yöq."],
             src=f"{ED_AID}; {OSU}; {EDUSA_UG}; {GMU}. {HOL}."),
        dict(t=M_TITLES[2][3], short="Yordam turi", min=10,
             hook="«Grant oldim» degan gap ikki xil narsa bölişi mumkin: siz tölay olmaydigan qism qoplandi yoki yaxşi natija uçun çegirma berildi. "
                  "Bu darsda ikkalasini farqlaymiz.",
             main="""<div class="tbl"><table><thead><tr><th></th><th>Ehtiyoj granti ([[need-based]])</th><th>Natija granti ([[merit-based]])</th></tr></thead><tbody>
<tr><td>Nimaga qarab</td><td>Narx bilan siz tölay oladigan summa farqiga</td><td>Baho, test, yutuqqa</td></tr>
<tr><td>Qanday söraladi</td><td>Yordam arizasi: CSS Profile yoki universitet formasi (M4)</td><td>Qabul arizasi bilan yoki alohida ariza</td></tr>
<tr><td>Kimga mos</td><td>Budjeti kiçik talabaga</td><td>Natijasi kuçli, qisman tölay oladigan talabaga</td></tr>
<tr><td>Xavf</td><td>Xalqaro talabaga oçiq universitet kam</td><td>Köpinça narxning bir qismi</td></tr>
</tbody></table></div>""",
             info="<p>EducationUSA maʼlumotiga köra, köp stipendiya öqiş va yaşaşning faqat bir qismini qoplaydi va birinçi kurs xalqaro talabasiga berilmasligi mumkin. Şartini öqing: bir yilgami yoki butun öqişgami, keyingi yillarda baho şarti bormi, summa qatʼiymi yoki foizmi, boşqa yordam bilan birga beriladimi.</p>",
             take="<b>Ehtiyoj granti</b> siz tölay olmaydigan farqni qoplaydi. <b>Natija granti</b> yutuq uçun beriladi va köpinça qisman.",
             task_b="Sizga qaysi tur mos keladi?",
             task=["Sizga qaysi tur köproq mos keladi? Ikki dalil bilan yozing."],
             src=f"{EDUSA_UG}. {HOL}."),
        dict(t=M_TITLES[2][4], short="Çegara", min=12,
             hook="«Yiliga qança tölay olaman?» degan savolga aniq raqam bilan javob bermasdan ariza boşlaş xato. Bu raqam qaysi universitet sizga real ekanini belgilaydi. "
                  "Bu darsda raqamni topamiz va yölni tanlaymiz.",
             main="""<p><b>Kerakli yordam uluşi</b> = (töliq narx − budjetingiz) ÷ töliq narx.</p>
<div class="tbl"><table><thead><tr><th>Uluş</th><th>Kompas tavsiyasi (qoida emas)</th></tr></thead><tbody>
<tr><td>0</td><td>Töliq tölay olasiz; natija grantini baribir qidiring</td></tr>
<tr><td>50 foizgaça</td><td>Natija grantlari va arzon yöllar: ikki yillik kollej, arzon hududlar</td></tr>
<tr><td>50 foizdan köp</td><td>Faqat töliq ehtiyojni qoplaydigan universitetlar (M3) yoki davlat dasturlari; parallel boşqa mamlakat</td></tr>
</tbody></table></div>""",
             info="<p>Çegara qanday aniqlanadi: yillik daromad va har oylik majburiy xarajat; jamğarmaning öqişga ajratiladigan qismi; yiliga dollarda maksimal summa (raqam bilan); bu summa 4 yil (bakalavr) yoki 2 yil (magistratura) takrorlanadimi. EducationUSA arzonroq hududlar (janub, Örta Ğarb, qişloq joylar) va ikki yillik kollejdan ötiş yölini ham körib çiqişni maslahat beradi.</p>",
             take="<b>Budjetingizni</b> dollarda, yillik raqam bilan aniqlang. Kerakli yordam uluşi qaysi yöldan borişingizni körsatadi.",
             task_b="Budjetingiz raqami",
             task=["Yillik maksimal summani yozing (oila yordami bölsa, u bilan kelişib).", "Bitta universitet uçun kerakli yordam uluşini hisoblang va yölni yozing."],
             src=f"{EDUSA_UG}. {HOL}."),
    ])

# ───────────────────────────── M3 ─────────────────────────────
MODULES[3] = dict(
    lead="AQŞ bakalavriatida yordam oliş uçun avval yordam beradigan universitetni topiş kerak. "
         "Bu modulda universitetlarni yordam siyosatiga qarab tört guruhga ajratasiz va har birini rasmiy hujjat bilan tekşirasiz. "
         "Oxirida sizda <strong>yordam böyiça saralangan röyxat</strong> böladi.",
    weeks="1", pass_time="~1 hafta (darslar ~1 soat + röyxat)",
    next=("<h2>Keyingi qadam: yordam arizasi</h2>" + bar(38, "II bosqiç: 1 / 2 modul · Rejangiz 38% tayyor") +
          '<div class="mv-k" data-mn="m3"><b>Röyxatingizdagi har universitet yordamni boşqa formada söraydi.</b> '
          "M4 da ularni bitta jadvalga yiğasiz va daromad hujjatlarini universitet tuşunadigan hujjatga aylantirasiz.</div>"
          '<p>M4.2 dan: <i>Hamma formada bir xil raqam, bir xil kurs va bir xil sana böliği şart.</i></p>'
          '<div class="mv-row"><a class="btn btn-p" href="usa-lab-o.html?m=4">M4: formalar jadvali</a></div>'),
    lessons=[
        dict(t=M_TITLES[3][0], short="Siyosatlar", min=12,
             hook="Bir universitet yordam söraganingizni qabul qaroriga qöşmaydi va kerakli summani töliq beradi. Boşqasi xalqaro talabaga deyarli yordam bermaydi. Ikkalasining sayti bir xil çiroyli. "
                  "Bu darsda ularni guruhlarga ajratamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Guruh</th><th>Maʼnosi</th><th>Rasmiy misol</th></tr></thead><tbody>
<tr><td>A</td><td>Xalqaro talabaga ham [[need-blind]] va töliq ehtiyoj</td><td>MIT; Dartmouth (2026-yil bitiruvçilari kursidan)</td></tr>
<tr><td>B</td><td>Yordam qabulga taʼsir qilmaydi, xalqaro talaba alohida yozilmagan</td><td>Harvard, Princeton</td></tr>
<tr><td>C</td><td>[[need-aware]]: yordam söraş qabulga taʼsir qilişi mumkin</td><td>Northwestern</td></tr>
<tr><td>D</td><td>Xalqaro talabaga yordam juda çeklangan</td><td>Ohio State</td></tr>
</tbody></table></div>""",
             info="<p>Dartmouth {HOL2} barça qabul qilingan bakalavrlarning hisoblangan ehtiyojini fuqarolikdan qatʼi nazar 100 foiz qoplaydi. Jadval töliq röyxat emas, misollar. A guruhi eng tanlovli universitetlar qatorida: röyxatni faqat A guruhidan tuziş xavfli. Budjetingiz kiçik bölsa ham, C va D guruhidagi arzon variantlar va boşqa mamlakat parallel bölsin.</p>".replace("{HOL2}", HOL2),
             take="Har universitetni A–D guruhiga rasmiy jumla bilan qöying. Siyosat özgaradi, şuning uçun har yili qayta tekşiring.",
             task_b="Beşta universitet guruhi",
             task=["Röyxatingizdagi 5 universitetni A–D guruhlariga qöying.", "Har biri uçun rasmiy sahifadan bir jumla va havola."],
             src=f"{MIT}; {DARTMOUTH}; {DARTMOUTH_FA}; {HARVARD}; {PRINCETON}; {NORTHWESTERN}; {OSU}. {HOL}."),
        dict(t=M_TITLES[3][1], short="Luğat", min=10,
             hook="«Generous aid» degan ibora heç narsa vaʼda qilmaydi. «Meets 100% of demonstrated need for all admitted students, regardless of citizenship» esa aniq majburiyat. "
                  "Bu darsda 8 ta iborani öqişni örganamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Ibora</th><th>Maʼnosi</th><th>Signal</th></tr></thead><tbody>
<tr><td>[[need-blind for all applicants]]</td><td>Yordam söraş qabulga taʼsir qilmaydi; xalqaro talaba kiradimi, tekşiring</td><td>Kuçli</td></tr>
<tr><td>[[regardless of citizenship]]</td><td>Fuqarolikdan qatʼi nazar</td><td>Kuçli</td></tr>
<tr><td>[[meets 100% of demonstrated need]]</td><td>Hisoblangan ehtiyoj töliq qoplanadi</td><td>Kuçli</td></tr>
<tr><td>[[no-loan]], [[grant aid]]</td><td>Qaytarilmaydigan grant</td><td>Kuçli</td></tr>
<tr><td>[[merit scholarships]]</td><td>Natija granti; ariza kerakmi, tekşiring</td><td>Qisman</td></tr>
<tr><td>[[need-aware for international students]]</td><td>Xalqaro talabada yordam söraş qabulga taʼsir qiladi</td><td>Ehtiyot</td></tr>
<tr><td>[[limited aid for international students]]</td><td>Yordam juda kam</td><td>Kuçsiz</td></tr>
<tr><td>[[expected family contribution]]</td><td>Oila tölaydigan deb hisoblangan qism</td><td>M4</td></tr>
</tbody></table></div>""",
             info="<p>«Xalqaro talabalarga ham oçiq» degan jumlani sahifada körmaguningizça uni bor deb hisoblamang. Savol bölsa, xalqaro qabul yoki moliyaviy yordam bölimiga yozma söring va javobni saqlang.</p>",
             take="Kuçli ibora majburiyat beradi: need-blind, regardless of citizenship, 100% of demonstrated need, no-loan. Qolgani tavsif.",
             task_b="Ikki universitet iborasi",
             task=["2 universitetning xalqaro yordam sahifasidan aynan iborani köçiring va maʼnosini özbekça yozing."],
             src=f"{MIT}; {HARVARD}; {NORTHWESTERN}. {HOL}."),
        dict(t=M_TITLES[3][2], short="H6", min=12,
             hook="Universitet «xalqaro talabaga yordam beramiz» deyişi mumkin. CDS ning H6 bandi esa ötgan yili neçta xalqaro talaba qança olganini körsatadi. "
                  "Bu darsda H6 ni öqiymiz.",
             main="""<p>H6 bandi bakalavriatdagi xalqaro talabalar ([[nonresidents]]) uçun universitet grantlari haqida: ehtiyoj granti beriladimi, natija granti beriladimi, olganlar soni, örtaça va jami summa.</p>
<p><b>Namuna:</b> Nebraska universiteti, CDS 2025–2026: 120 nafar xalqaro bakalavr yordam olgan, örtaça 10 391 dollar, jami 1 246 965 dollar.</p>
<ol><li>Örtaça summani töliq narx (M2) bilan soliştiring.</li><li>Olganlar sonini xalqaro bakalavrlar soni (CDS B) bilan soliştiring.</li><li>2–3 yillik CDS ni köring: raqam barqarormi?</li></ol>""",
             info="<p>Örtaça summa sizga beriladigan summa emas: u universitetning xalqaro talabaga yordam hajmini körsatadi.</p>",
             take="H6 ni töliq narx va xalqaro talabalar soni bilan soliştiring. Şunda yordam qança keng ekanini körasiz.",
             task_b="Ikki universitetning H6",
             task=["2 universitetning songgi CDS ida H6 ni toping.", "Yozing: siyosat, olganlar soni, örtaça summa, töliq narxning neça foizi."],
             src=f"{CDS_H6}; {CDS}. {HOL}."),
        dict(t=M_TITLES[3][3], short="Kalkulyator", min=12,
             hook="Saytdagi narx röyxat narxi. Siz tölaydigan narx yordamdan keyin qolgan summa. Uni arizadan oldin taxminan biliş mumkin. "
                  "Bu darsda kalkulyator va natija grantlari bilan işlaymiz.",
             main="""<p>[[Net Price Calculator]] universitet saytida turadi va yordamdan keyingi taxminiy narxni hisoblaydi (Taʼlim vazirligi tuşuntiradi).</p>
<ul><li>Ota-ona daromadi, jamğarma va oila tarkibini dollarda kiriting, M4 dagi hisob bilan bir xil.</li><li>Kalkulyator xalqaro talaba uçun işlaşini sahifadan tekşiring.</li><li>Natija taxmin, rasmiy yordam xati emas.</li></ul>
<p>Natija granti uçun universitetning [[scholarships]] sahifasini oçing: avtomatikmi yoki alohida ariza, bir yilmi yoki 4 yil, qaysi baho saqlaniği kerak.</p>""",
             info="<p>H6 dagi ikkinçi siyosat bandi ([[non-need-based]] grant) universitet natija granti berişini körsatadi. Alohida ariza muddati köpinça qabul muddatidan oldin böladi. EducationUSA eslatişiça, köp stipendiya narxning faqat bir qismini qoplaydi.</p>",
             take="Kalkulyator taxminiy narxni beradi, grant sahifasi esa şartni. Ikkalasini ham sana bilan yozib qöying.",
             task_b="Ikki kalkulyator, bitta grant",
             task=["2 universitet kalkulyatorida taxminiy narxni hisoblang (xalqaro talabaga işlasa).", "Bitta universitetning xalqaro talabaga oçiq natija grantini toping: summa, muddat, şart."],
             src=f"{NPC}; {CDS_H6}; {EDUSA_UG}. {HOL}."),
        dict(t=M_TITLES[3][4], short="Röyxat", min=12,
             hook="Orzu, möljal va işonçli röyxat qabul ehtimoliga qarab tuziladi. AQŞda unga ikkinçi öq qöşiladi: qabul qilsa, <b>tölay olasizmi</b>? "
                  "Bu darsda ikkala öqni bitta jadvalga qöyamiz.",
             main="""<div class="tbl"><table><thead><tr><th></th><th>Siz tölay olasiz</th><th>Faqat yordam bilan</th></tr></thead><tbody>
<tr><td>Qabul ehtimoli yuqori</td><td>Işonçli tanlov</td><td>Yordam real bölsa (A, B, kuçli H6)</td></tr>
<tr><td>Örtaça</td><td>Möljal</td><td>Faqat A guruhi yoki kuçli natija granti</td></tr>
<tr><td>Past</td><td>Orzu</td><td>Faqat A guruhi, bir neçtasidan köp emas</td></tr>
</tbody></table></div>
<p>Kamida bitta universitet «tölay olasiz + ehtimol yuqori» katagida bölsin. Bunday universitet yöq bölsa, parallel boşqa mamlakat kerak.</p>""",
             info="<p>D guruhidagi universitetga faqat töliq tölay olsangiz ariza bering. Har ariza narxi (ariza yiğimi, CSS Profile, testlar) budjetga kiradi. «Qabul qilsa, keyin mablağ topamiz» rejasi işlamaydi: I-20 uçun mablağ hujjati qabuldan keyin darhol söraladi (M2).</p>",
             take="Röyxat ikki öq bilan tuziladi: qabul ehtimoli va tölay oliş. Böş katak bölsa, uni qanday töldirişingizni oldindan yozing.",
             task_b="Sizning ikki öqli röyxatingiz",
             task=["8–12 universitetni ikki öqli jadvalga joylang.", "Böş katakni qanday töldirişingizni yozing."],
             src=""),
    ])

# ───────────────────────────── M4 ─────────────────────────────
MODULES[4] = dict(
    lead="<b>Ehtiyoj granti</b> sizning va ota-onangizning daromadiga qarab hisoblanadi. Bu modulda qaysi universitet qaysi formani söraşini aniqlaysiz, "
         "Özbekistondagi daromadni universitet tuşunadigan hujjatga aylantirasiz va yordam xatini öqiysiz. "
         "Oxirida sizda <strong>moliyaviy yordam arizasi paketi</strong> böladi.",
    weeks="1", pass_time="~1 hafta (darslar ~1 soat + paket)",
    next=("<h2>II bosqiç yakunlandi: keyingi qadam davlat dasturlari</h2>" + bar(50, "II bosqiç: 2 / 2 modul · Rejangiz 50% tayyor") +
          '<div class="mv-k" data-mn="m4"><b>Yordam arizasi paketingiz tayyor.</b> Muddatlarini kalendarga qöying. '
          "III bosqiçda (M5–M6) davlat dasturlari: Özbekistonda bakalavriatda öqiyotganlar uçun Global UGRAD, 2+ yillik tajribalilar uçun Fulbright magistraturasi.</div>"
          "<p>III bosqiç darslari:</p>" + lock(tl(5) + tl(6)[:2]) + TARIF +
          '<div class="mv-row"><a class="btn btn-p" href="usa-lab-o.html?m=5">III bosqiç: M5 ni oçiş</a><a class="btn btn-g" href="usa-lab-narxlar.html">Tariflar</a></div>'),
    lessons=[
        dict(t=M_TITLES[4][0], short="Formalar", min=10,
             hook="Har universitet öz hujjatlar röyxatini söraydi va muddat köpinça qabul arizasi bilan bir kunda. Birida yetgan hujjat boşqasiga yetmasligi mumkin. "
                  "Bu darsda hammasini bitta jadvalga yiğamiz.",
             main="""<p>[[CSS Profile]] (College Board) universitetlar öz yordamini taqsimlaş uçun işlatadigan forma. Xalqaro abituriyentlar uçun alohida savollar bölimi bor.</p>
<p><b>Northwestern namunasi:</b></p><ul><li>CSS Profile yoki, topşirib bölmasa, universitetning öz formasi (ISAFA);</li><li>ota-onaning <b>soliq hujjati</b> yoki iş beruvçidan muhr va imzoli <b>daromad xati</b>;</li><li>har hujjatda ismingiz va tuğilgan sanangiz;</li><li><b>rasmiy tarjima</b> va kurs bilan dollarga ögirilgan summa.</li></ul>
<div class="tbl"><table><thead><tr><th>Universitet</th><th>Forma</th><th>Qöşimça hujjat</th><th>Muddat</th></tr></thead><tbody>
<tr><td>...</td><td>CSS Profile yoki öz formasi</td><td>Daromad xati, tarjima</td><td>Rasmiy sahifadan</td></tr>
</tbody></table></div>""",
             info="<p>CSS Profile sahifasida xalqaro oilalar uçun savollar bor: valyuta, ikki valyutadagi daromad, AQŞ soliq deklaratsiyasini topşirmaydigan oilalar IDOC ga nima yuborişi. Har universitetning [[international applicants]] yoki [[how to apply for aid]] sahifasini oçing.</p>",
             take="Har universitet uçun alohida qator: forma, hujjat, muddat, havola. Bitta universitetga yetgan hujjat boşqasiga yetmasligi mumkin.",
             task_b="Formalar jadvalingiz",
             task=["Yordam söraladigan har universitet uçun qatorni töldiring: forma, qöşimça hujjat, muddat, havola."],
             src=f"{CSS}; {CSS_INT}; {NORTHWESTERN}. {HOL}."),
        dict(t=M_TITLES[4][1], short="Daromad", min=15,
             hook="AQŞ universiteti Özbekistonda daromad qanday şakllanişini bilmaydi. U faqat hujjatingiz va izohingizni köradi. "
                  "Bu darsda <b>daromad varaqasini</b> tuzamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Qator</th><th>Hujjat</th></tr></thead><tbody>
<tr><td>Rasmiy daromad (har ota-ona, yillik)</td><td>Iş beruvçi xati yoki soliq maʼlumotnomasi</td></tr>
<tr><td>Tadbirkorlik (YATT, korxona)</td><td>Soliq hisoboti</td></tr>
<tr><td>Jamğarma</td><td>Bank köçirmasi</td></tr>
<tr><td>Mulk</td><td>Formadagi körsatmaga qarab</td></tr>
<tr><td>Majburiy xarajat</td><td>Izohli varaq</td></tr>
</tbody></table></div>
<ol><li>Hamma summa bitta sanadagi rasmiy kurs bilan dollarga ögiriladi; kurs va sana yoziladi.</li><li>CSS Profile, universitet formasi va hujjatlarda raqam bir xil.</li><li>Norasmiy daromad yaşirilmaydi va töqilmaydi: qöşimça izohda qisqa yoziladi.</li></ol>""",
             info="<p>Daromadni kamaytirib körsatiş yoki mulkni yaşiriş firibgarlik hisoblanişi mumkin. Universitet qöşimça hujjat söraydi; nomuvofiqlik yordamni ham, qabulni ham xavf ostiga qöyadi. Rasmiy maʼlumotnomalar röyxatini my.gov.uz dan tekşiring, qaysi biri qabul qilinişini universitetdan yozma söring.</p>",
             take="Har daromad turiga rasmiy hujjat, bitta kurs va sana, hamma formada bir xil raqam.",
             task_b="Sizning daromad varaqangiz",
             task=["Varaqni 5 qator böyiça töldiring; ota-ona daromadini ular bilan tekşiring.", "Kurs va sanani yozing."],
             src=f"{NORTHWESTERN}. {HOL}."),
        dict(t=M_TITLES[4][2], short="Tölov", min=8,
             hook="Yordam söraşning ham narxi bor. Bir neça universitetga forma tölovi kiçik budjetda sezilarli böladi. "
                  "Bu darsda tölov va undan ozod qiliş qoidasini aniqlaymiz.",
             main="""<p>CSS Profile sahifasida: yillik daromadi 100 000 dollargaça bölgan oilalar uçun forma ozod qiliş orqali bepul. Xalqaro talabaga bu qoida universitetga qarab farq qiladi: Northwestern xalqaro talaba CSS Profile tölovidan ozod bölmasligini yozadi.</p>
<ol><li>Har universitet sahifasida [[fee waiver]] bandini qidiring.</li><li>Yozilmagan bölsa, yordam bölimidan yozma söring.</li><li>Tölovlarni budjet jadvaliga qöşing (M2).</li></ol>""",
             info="<p>Qabul arizasi tölovi va undan ozod qiliş Bakalavr dasturi M13 da. Bu dars faqat yordam formasi tölovi haqida.</p>",
             take="Ozod qiliş xalqaro talabaga hamma joyda işlamaydi. Har universitetdan aniqlang va tölovni budjetga yozing.",
             task_b="Forma tölovlari",
             task=["Har universitet uçun yozing: forma tölovi bormi, ozod qiliş mumkinmi, dalil."],
             src=f"{CSS}; {NORTHWESTERN}. {HOL}."),
        dict(t=M_TITLES[4][3], short="Xat", min=12,
             hook="«Sizga 40 000 dollar yordam» degan xat quvonarli. Uning qança qismi grant, qança qismi qaytariladigan kredit yoki iş ekanini hisoblamaguningizça qaror qilmang. "
                  "Bu darsda xatni qismlarga ajratamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Qism</th><th>Qaytariladimi</th></tr></thead><tbody>
<tr><td>Grant yoki stipendiya</td><td>Yöq</td></tr>
<tr><td>Kredit</td><td>Ha: kafil, foiz va qaytariş şartini öqing</td></tr>
<tr><td>Iş ([[student employment]])</td><td>Yöq, lekin işlab topiladi (M8)</td></tr>
<tr><td>Oila hissasi</td><td>Universitet siz va ota-onangizdan kutgan tölov</td></tr>
</tbody></table></div>
<p><b>Qolgan summa</b> = töliq narx − grant − kredit − iş. Siz uçun haqiqiy narx: qolgan summa + kredit.</p>""",
             info="<p>Harvard talabadan ham öz iş haqi va jamğarmasidan hissa kutişini yozadi: «ota-ona hissasi nol» Siz heç narsa tölamaysiz degani emas. Yordam keyingi yillarda qayta hisoblanadimi va har yili ariza kerakmi, xatda yoki sahifada yoziladi.</p>",
             take="Xatni 4 qismga ajrating:<ul><li><b>grant</b>;</li><li><b>kredit</b>;</li><li><b>iş</b>;</li><li><b>oila hissasi</b>.</li></ul> Qolgan summa va kredit birga sizning haqiqiy narxingiz.",
             task_b="Namuna xat hisobi",
             task=["Namuna yordam xati uçun qolgan summani hisoblang.", "Keyingi yillar şartini yozing."],
             src=f"{HARVARD}. {HOL}."),
        dict(t=M_TITLES[4][4], short="Qayta", min=8,
             hook="Yordam xati baʼzan sizning hozirgi moliyaviy holatingizni töliq körsatmaydi. Holat haqiqatan özgargan bölsa, hujjatli va xuşmuomala sörov qiliş mumkin. "
                  "Bu darsda qaçon va qanday söraşni körib çiqamiz.",
             main="""<p>Qaçon örinli: arizadan keyin daromad kamaygan (iş yöqotiş, kasallik), formada körinmagan majburiy xarajat bor, hisobda xato bor (masalan, kurs notöğri).</p>
<ol><li>Universitet sahifasida [[appeal]], [[review]] yoki [[special circumstances]] bandini toping.</li><li>Qisqa xat: nima özgardi, qaçon, raqam bilan, hujjat ilova.</li><li>Boşqa universitet taklifini körsatiş mumkinmi, sahifadan tekşiring.</li></ol>""",
             info="<p>Qayta körib çiqiş sörovi savdolaşiş emas. Hujjatsiz yoki töqilgan holat yordamni yöqotişga olib kelişi mumkin. Dartmouth kabi universitetlarda xalqaro talaba uçun alohida sahifa bor: savolni öşa sahifadagi manzilga yuboring.</p>",
             take="Haqiqiy özgariş yoki xato bölsa, universitet tartibi böyiça qisqa va hujjatli sörov yozing.",
             task_b="Qayta körib çiqiş tartibi",
             task=["Bitta universitetning tartibini havola bilan yozing.", "Holatingizga mos 3 jumlalik sörov rejasini özingiz yozing."],
             src=f"{DARTMOUTH}. {HOL}."),
    ])

# ───────────────────────────── M5 ─────────────────────────────
MODULES[5] = dict(
    lead="Global UGRAD Özbekistonda bakalavriatda öqiyotgan talabani AQŞ universitetiga bir semestrga olib boradi. "
         "Daraja bermaydi, lekin AQŞ taʼlimini içidan körsatadi. Bu modulda muvofiqlikni va sikl eʼlonini kuzatişni örganasiz. "
         "Oxirida sizda <strong>almaşinuv dasturi kartasi</strong> böladi.",
    weeks="1", pass_time="~1 hafta (darslar ~1 soat + karta)",
    next=("<h2>Keyingi qadam: Fulbright</h2>" + bar(63, "III bosqiç: 1 / 2 modul · Rejangiz 63% tayyor") +
          '<div class="mv-k" data-mn="m5"><b>UGRAD böyiça qaroringiz kartada.</b> Bakalavrni tugatib, 2 yillik iş tajribasi yiğilgaç, keyingi davlat dasturi Fulbright magistraturasi. '
          "M6 da uning şartlarini va J-1 majburiyatini kelajak rejangiz bilan soliştirasiz.</div>"
          '<div class="mv-row"><a class="btn btn-p" href="usa-lab-o.html?m=6">M6: Fulbright şartlari</a></div>'),
    lessons=[
        dict(t=M_TITLES[5][0], short="UGRAD", min=10,
             hook="«AQŞga grant bilan bakalavr» degan eʼlonlar köpinça Global UGRAD haqida böladi. U diplom bermaydi va universitetni siz tanlamaysiz. "
                  "Bu darsda dastur nima berişini aniq bilib olamiz.",
             main="""<ul><li>AQŞ Davlat departamenti dasturi, World Learning boşqaradi.</li><li>AQŞ kolleji yoki universitetida bir semestr daraja bermaydigan ([[non-degree]]) öqiş.</li><li>Kampusda yaşaş, kunduzgi kurslar (bittasi AQŞ haqida), 20 soat jamoat işi; oxirida Vaşingtonda seminar.</li><li>Universitetni dastur tanlaydi: akademik qiziqişingizga qarab.</li><li>Kreditni öz universitetingizga ötkaziş sizning masʼuliyatingiz.</li></ul>
<p><b>Qoplanadi:</b></p><ul><li>aviabilet;</li><li>öqiş, kampusda yaşaş va ovqat;</li><li>suğurta va kitoblar;</li><li>oylik kiçik stipendiya;</li><li>finalistlarga TOEFL.</li></ul>""",
             info="<p>Klinik yönalişlarda (tibbiyot, hamşiralik, veterinariya, farmakologiya) J-1 qoidalari tufayli kurslar çeklanişi mumkin. World Learning sahifasiga köra, AQŞning 60 dan ortiq oliy taʼlim muassasasi har yili talaba qabul qiladi, arizalar odatda noyabr boşidan dekabrgaça oçiladi.</p>",
             take="UGRAD: bir semestr, diplomsiz, universitetni dastur tanlaydi. Xarajatni dastur qoplaydi, kredit ötkaziş sizning işingiz.",
             task_b="UGRAD sizga nima beradi",
             task=["UGRAD nima beradi va nima bermaydi: 3 tadan band yozing.", "Kredit ötkaziş tartibini öz universitetingizda kimdan söraşingizni yozing."],
             src=f"{EMB_UGRAD}; {UGRAD_WL}. {HOL}."),
        dict(t=M_TITLES[5][1], short="Muvofiqlik", min=10,
             hook="UGRAD da bitta şartga mos kelmaslik arizani boşidan yopadi. Eng köp uçraydigan xato: oxirgi kurs talabasining ariza berişi. "
                  "Bu darsda har şartni özingizga qöyib köramiz.",
             main="""<div class="tbl"><table><thead><tr><th>Şart (oxirgi eʼlon, 2024–2025)</th><th>Tekşiriş</th></tr></thead><tbody>
<tr><td>Dastur boşida kamida 18 yoş</td><td>Tuğilgan sana</td></tr>
<tr><td>Özbekiston fuqarosi, hozir Özbekistonda yaşaydi va öqiydi</td><td>Pasport, öqiş joyi</td></tr>
<tr><td>Akkreditatsiyalangan universitetda kunduzgi bakalavriat, yaxşi holat</td><td>Maʼlumotnoma</td></tr>
<tr><td>Dasturdan keyin kamida bir öquv yili qoladi</td><td>Kurs va öquv reja</td></tr>
<tr><td>Yetakçilik salohiyati va ingliz tili</td><td>Dalillar</td></tr>
<tr><td>Dasturdan keyin Özbekistonga qaytiş</td><td>Majburiyat</td></tr>
</tbody></table></div>""",
             info="<p>Ariza bera olmaydiganlar: AQŞ fuqarolari va doimiy rezidentlari; hozir Özbekistondan taşqarida yaşayotganlar; oxirgi kurs talabalari; UGRAD bitiruvçilari; AQŞ hukumati homiyligidagi 6 haftadan uzun almaşinuvdan keyin 2 yillik talabni bajarmaganlar; songgi 3 yilda AQŞ doimiy yaşaş huquqiga ariza berganlar. AQŞ yoki xorijda tajribasi kam nomzodlarga ustunlik beriladi. Yangi sikl eʼlonida şartlar özgarişi mumkin.</p>",
             take="Asosiy şartlar: 18+, Özbekistonda yaşaş va kunduzgi öqiş, kamida bir yil öqiş qoliği, ingliz tili, qaytiş. Bittasi mos kelmasa, 5.5 dagi muqobilga öting.",
             task_b="Sizning muvofiqligingiz",
             task=["Har şart böyiça özingizni belgilang: mos, tekşiriş kerak, mos emas.", "Bitta «mos emas» bölsa, 5.5 dagi muqobilni oçing."],
             src=f"{EMB_UGRAD}. Şartlar oxirgi eʼlondan."),
        dict(t=M_TITLES[5][2], short="Kuzatuv", min=8,
             hook="UGRAD ning har sikli alohida eʼlon qilinadi. Eʼlon çiqmagan sikl uçun «muddat» aytayotgan post rasmiy manba hisoblanmaydi. "
                  "Bu darsda holatni qanday kuzatişni körib çiqamiz.",
             main=f"""<div class="tbl"><table><thead><tr><th>Manba</th><th>Nima körsatadi</th></tr></thead><tbody>
<tr><td>AQŞ elçixonasi (Toşkent), UGRAD sahifasi</td><td>Oxirgi eʼlon 2024–2025 sikli uçun, muddat 15.12.2024</td></tr>
<tr><td>Elçixonaning almaşinuv dasturlari röyxati</td><td>UGRAD röyxatda bor, joriy ariza holati körsatilmagan (31.10.2026)</td></tr>
<tr><td>World Learning</td><td>Arizalar odatda noyabr boşidan dekabrgaça</td></tr>
</tbody></table></div>
<p>{HOL2}: qidiruvda Özbekiston uçun yangi UGRAD eʼloni topilmadi. Elçixona sahifasini özingiz oçib tekşiring.</p>""",
             info="<ol><li>Elçixonaning UGRAD va almaşinuv sahifalarini oyiga bir marta oçing, sana bilan yozing.</li><li>Elçixonaning rasmiy ijtimoiy tarmoq kanallarini kuzating; boşqa kanaldagi xabarni elçixona sahifasi bilan soliştiring.</li><li>Savolni oxirgi eʼlondagi rasmiy manzilga yozing (mavzuda «Global UGRAD»).</li><li>Noyabr–dekabrda tekşirişni haftalik qiling.</li></ol>"
                  "<p>Sikl eʼlon qilinmaguncha UGRAD uçun pullik «tayyorlov» xizmati sotib olmang. Bu vaqtda bepul tayyorlaning: ingliz tili, yetakçilik dalillari, öqiş natijalari.</p>",
             take="Rasmiy eʼlon çiqmaguncha muddat yöq. Elçixona sahifasini oyiga bir marta, noyabr–dekabrda haftasiga bir marta tekşiring.",
             task_b="Bugungi holat",
             task=["Elçixonaning UGRAD sahifasini oçing va bugungi holatni sana bilan yozing.", "Telefoningizga oylik eslatma qöying."],
             ph="20.11.2026: UGRAD sahifasi — oxirgi sikl ..., yangi e'lon: yo'q / bor. Eslatma: har oyning ... kuni",
             src=f"{EMB_UGRAD}; {EMB_EXCH}; {UGRAD_WL}. {HOL2}."),
        dict(t=M_TITLES[5][3], short="Ariza", min=12,
             hook="UGRAD arizasi ingliz tilida, onlayn topşiriladi va muddatdan keyin özgartirilmaydi. Tayyorgarlik eʼlondan oldin boşlanadi, ariza esa faqat eʼlon körsatmasi böyiça töldiriladi. "
                  "Bu darsda hozir nima tayyorlaşni ajratamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Dalil</th><th>Qayerda örganiladi</th></tr></thead><tbody>
<tr><td>Yetakçilik va jamoat işi holatlari (STAR)</td><td>Bakalavr dasturi M7</td></tr>
<tr><td>Inşo yoziş va tahrir</td><td>Bakalavr dasturi M9–M10</td></tr>
<tr><td>Tavsiya söraş</td><td>Bakalavr dasturi M8</td></tr>
<tr><td>Ingliz tili</td><td>Mustaqil; test strategiyasi Bakalavr dasturi M5</td></tr>
<tr><td>Öqiş natijalari</td><td>Öz universitetingiz</td></tr>
</tbody></table></div>
<p>UGRAD ga xos ikki savol: qaysi yönalişdagi kurslarga joylaşiş kerak va nega; qaytgandan keyin tajribani Özbekistonda qanday işlatasiz.</p>""",
             info="<p>Oxirgi eʼlondagi tartib: ariza World Learning portali orqali, faqat ingliz tilida; muddatdan keyin tahrirlanmaydi; finalistlar va zaxiradagilar TOEFL iBT topşiradi, xarajatni dastur qoplaydi. Inşo savollari va hajmi har siklda eʼlonda beriladi: ötgan yilgi savollarni yod olib tayyorlanmang.</p>",
             take="Hozir dalillarni yiğing. Inşoni faqat yangi eʼlondagi savol böyiça yozasiz.",
             task_b="Dalillaringiz holati",
             task=["5 ta dalilning har biri böyiça hozirgi holatingizni yozing.", "Akademik qiziqiş va qaytgandan keyingi reja böyiça 2–3 jumlalik fikr yozing."],
             src=f"{EMB_UGRAD}; {UGRAD_WL}. {HOL}."),
        dict(t=M_TITLES[5][4], short="Boşqalar", min=10,
             hook="UGRAD yopiq yoki mos kelmasa, AQŞ tajribasiga yöl qolmadi degani emas. Elçixona röyxatida turli yoş va kasb uçun boşqa dasturlar bor. "
                  "Bu darsda B rejangizni tanlaymiz.",
             main="""<div class="tbl"><table><thead><tr><th>Dastur</th><th>Kimga</th></tr></thead><tbody>
<tr><td>FLEX</td><td>Maktab öquvçilari: AQŞ maktabida bir yil</td></tr>
<tr><td>SUSI ([[Young Women Leaders]])</td><td>Talaba yetakçi qizlar: qisqa yozgi dastur</td></tr>
<tr><td>[[TechGirls]], [[TechWomen]]</td><td>Fan va texnologiyaga qiziqqan qizlar va ayollar</td></tr>
<tr><td>Fulbright Foreign Student</td><td>Bakalavr diplomli mutaxassislar: magistratura (M6)</td></tr>
<tr><td>Hubert H. Humphrey</td><td>Martaba örtasidagi mutaxassislar: 10 oy</td></tr>
<tr><td>Fulbright [[Visiting Scholar]]</td><td>Olimlar va öqituvçilar: 3–5 oy</td></tr>
</tbody></table></div>""",
             info_t="J-1 va 2 yillik talab",
             info="<p>Davlat dasturlari J-1 vizasi bilan. Harvard xalqaro ofisi tuşuntirişiça, J-1 egasi AQŞ hukumati, öz hukumati yoki xalqaro taşkilot mablağida bölsa, 212(e) talabi qöllanadi: vatanga qaytib 2 yil yaşamaguncha immigratsion viza, H yoki L vizasi olinmaydi va AQŞ içida boşqa maqomga ötilmaydi. AQŞda qolib işlaşni rejalaştirgan nomzodga bu yöl mos kelmaydi: unga F-1 yöli (M3–M4 yoki M7).</p>",
             take="UGRAD dan taşqari maktab, yozgi, kasbiy va ilmiy almaşinuvlar bor. Hukumat mablağidagi J-1 dasturlarida 2 yillik talab qöllanadi.",
             task_b="Sizning B rejangiz",
             task=["Röyxatdan sizga mos keladigan 1–2 dasturni tanlang.", "B rejangizni yozing: UGRAD bölmasa nima qilasiz."],
             src=f"{EMB_EXCH}; {HARVARD_212E}; {EMB_UGRAD}. {HOL}."),
    ])

# ───────────────────────────── M6 ─────────────────────────────
MODULES[6] = dict(
    lead="Fulbright Özbekistondan AQŞda magistratura uçun asosiy davlat stipendiyasi. "
         "Bu modulda dastur Özbekiston uçun nimani talab qilişini, tanlov qanday ötişini va J-1 majburiyati rejangizga qanday taʼsir qilişini örganasiz. "
         "Oxirida sizda <strong>Fulbright muvofiqlik va reja kartasi</strong> böladi.",
    weeks="1", pass_time="~1 hafta (darslar ~1 soat + karta)",
    next=("<h2>III bosqiç yakunlandi: keyingi qadam magistratura va PhD moliyasi</h2>" + bar(75, "III bosqiç: 2 / 2 modul · Rejangiz 75% tayyor") +
          '<div class="mv-k" data-mn="m6"><b>Fulbright böyiça qaroringiz tayyor.</b> Fulbright bölmasa ham AQŞ magistraturasi va PhD ga yöl bor: kafedra moliyasi. '
          "IV bosqiçda (M7–M8) moliya paketini soliştirasiz va viza tartibini örganasiz.</div>"
          "<p>IV bosqiç darslari:</p>" + lock(tl(7) + tl(8)[:2]) + TARIF +
          '<div class="mv-row"><a class="btn btn-p" href="usa-lab-o.html?m=7">IV bosqiç: M7 ni oçiş</a><a class="btn btn-g" href="usa-lab-narxlar.html">Tariflar</a></div>'),
    lessons=[
        dict(t=M_TITLES[6][0], short="Şartlar", min=12,
             hook="Köpçilik Fulbright ni «eng aʼloçilar uçun PhD granti» deb öylaydi. Özbekistonda u iş tajribasi bor mutaxassislar uçun magistratura dasturi. "
                  "Bu darsda şartlarni özingizga qöyib köramiz.",
             main="""<div class="tbl"><table><thead><tr><th>Şart (2027–2028 eʼloni)</th><th>Izoh</th></tr></thead><tbody>
<tr><td>Özbekiston fuqarosi, ariza va tanlov davomida Özbekistonda yaşaydi</td><td>Hozir xorijdagilar mos emas</td></tr>
<tr><td>Bakalavr diplomi bor</td><td>Diplom qölda bölişi kerak</td></tr>
<tr><td>Kamida 2 yillik kasbiy tajriba</td><td>Eng köp uçraydigan tösiq</td></tr>
<tr><td>Bemor bilan bevosita işlaydigan tibbiy dasturlar yopiq</td><td>Jamoat salomatligi kabi sohalar mumkin</td></tr>
</tbody></table></div>
<p><b>Nima beradi:</b></p><ul><li>2 yilgaça magistratura;</li><li>J-1 viza kömagi;</li><li>öqiş, yiğimlar va suğurta;</li><li>oylik stipendiya, kitob, aviabilet.</li></ul>""",
             info_t="Ustuvor sohalar (2027–2028)",
             info="<p><b>Ustuvor sohalar:</b> sunʼiy intellekt va maʼlumotlar fani; yarimötkazgiçlar, geologiya, kon muhandisligi, materialşunoslik, energetika tizimlari; yadro muhandisligi; kosmos va masofadan zondlaş; quriliş, ekologiya va energetika muhandisligi, qayta tiklanadigan energiya, qişloq xöjaligi. Dastur boşqa sohalarga ham oçiq. 2026-yil 5-iyunda elçixona Fulbright ni muhim minerallar, energetika va ilğor texnologiya sohalarida kengaytiriş va El-yurt umidi jamğarmasining şerik moliyalaştirişini eʼlon qilgan. AQŞda yaqinda uzoq tajribasi yöq nomzodlarga ustunlik beriladi.</p>",
             take="Özbekiston uçun Fulbright: magistratura, 2 yilgaça; diplom, 2 yillik tajriba, Özbekistonda yaşaş. Ustuvor sohalar STEM, lekin boşqalar ham oçiq.",
             task_b="Sizning muvofiqligingiz",
             task=["Har şart böyiça belgilang: mos, tekşiriş kerak, mos emas.", "Sohangiz ustuvor röyxatdami? Qaysi band?"],
             src=f"{EMB_FUL}; {EMB_FUL_EXP}. {HOL}."),
        dict(t=M_TITLES[6][1], short="Tanlov", min=10,
             hook="Fulbright da universitetga özingiz ariza bermaysiz. Tanlov va joylaştiriş boşqa tartibda işlaydi, buni biliş kutiş davridagi xavotirni kamaytiradi. "
                  "Bu darsda olti bosqiçni körib çiqamiz.",
             main="""<ol><li>Muddatdan keyin texnik tekşiruv.</li><li>Mustaqil öquvçilar paneli standart mezon bilan baholaydi.</li><li>Eng yuqori ball olganlar elçixonada intervyuga çaqiriladi.</li><li>Intervyudan ötganlardan nomzodlar körsatiladi.</li><li>Nomzodlar TOEFL va GRE yoki GMAT topşiradi, xarajat vaucher bilan.</li><li>Yakuniy tanlov: Fulbright kengaşi tasdiği, mablağ va joylaştiriş.</li></ol>""",
             info="<p>Elçixona sahifasiga köra, nomzodlar joylaştirişda qatnaşmaydi va yakuniy natija haqida xabar oladi. IIE umumiy tavsifida ikki tur bor: IIE nomzod uçun ariza beradigan va nomzod özi ariza beradigan. Özbekiston uçun qaysi biri, elçixona eʼlonidan oling. Intervyu usullari (STAR, özini tanitiş) Magistratura dasturi M8 da; bu yerda Fulbright ga xos savol: qaytgandan keyin Özbekistonga nima olib kelasiz?</p>",
             take="Olti bosqiç: texnik tekşiruv, panel, intervyu, nomzodlik, testlar, kengaş tasdiği. Joylaştirişda nomzod qatnaşmaydi.",
             task_b="Har bosqiçga tayyorgarlik",
             task=["Olti bosqiçning har biri uçun nima tayyorlaşingizni bir jumlada yozing."],
             src=f"{EMB_FUL}; {FUL_IIE}. {HOL}."),
        dict(t=M_TITLES[6][2], short="Ariza", min=12,
             hook="Fulbright arizasidagi har inşo original bölişi şart. Elçixona plagiat yoki AI yozgan matn arizani muvofiq emas deb topişga olib kelişini aniq yozgan. "
                  "Bu darsda ariza tarkibini tekşiramiz.",
             main="""<div class="tbl"><table><thead><tr><th>Qism</th><th>Izoh</th><th>Qayerda örganiladi</th></tr></thead><tbody>
<tr><td>Onlayn ariza (IIE portali)</td><td>Kech yoki töliq bölmagan ariza körilmaydi</td><td>Şu modul</td></tr>
<tr><td>Inşolar</td><td>Original; elçixona körsatmasini öqing</td><td>Magistratura M5</td></tr>
<tr><td>Rezyume</td><td>Elçixona maslahatlari böyiça</td><td>Magistratura M3</td></tr>
<tr><td>Tavsiya xati</td><td>Elçixonaning formasi bilan</td><td>Magistratura M4</td></tr>
<tr><td>TOEFL va GRE yoki GMAT</td><td>Nomzodlar topşiradi, vaucher bilan</td><td>Kursga kirmaydi</td></tr>
</tbody></table></div>""",
             info="<p>Inşo soni, hajmi va savollari faqat joriy sikl körsatmasidan olinadi. AI dan matn yozdiriş va boşqa birovning inşosini moslaş arizani yopadi. Kompas Lab ham tayyor matn bermaydi: inşoni özingiz yozasiz, tuzilma va mezon Magistratura dasturida.</p>",
             take="Ariza: onlayn şakl, original inşo, rezyume, elçixona formasidagi tavsiya, nomzodlarga testlar. Plagiat yoki AI matni arizani yopadi.",
             task_b="Tayyorlik holati",
             task=["Joriy sikl inşo körsatmasini toping va savollar sonini yozing.", "Har qism uçun tayyorlik holatini belgilang."],
             src=f"{EMB_FUL}. {HOL}."),
        dict(t=M_TITLES[6][3], short="Kalendar", min=10,
             hook="Fulbright muddati bilan safar orasida taxminan bir yil bor. Muddatdan orqaga hisoblamasangiz, tavsiya va tajriba hujjatini oxirgi haftada yiğasiz. "
                  "Bu darsda teskari rejani tuzamiz.",
             main=f"""<div class="tbl"><table><thead><tr><th>Bosqiç (2027–2028 sikli)</th><th>Sana</th></tr></thead><tbody>
<tr><td>Ariza muddati</td><td>30.06.2026 (yopilgan)</td></tr>
<tr><td>Intervyu, nomzodlik, testlar</td><td>Muddatdan keyin; aniq sana körsatilmagan</td></tr>
<tr><td>Safar</td><td>2027-yil bahor–kuz</td></tr>
</tbody></table></div>
<p>{HOL2}: keyingi sikl (2028–2029) eʼloni topilmadi. Ötgan siklda muddat iyun oxiri bölgan; bu keyingi sikl uçun kafolat bölmaydi.</p>""",
             info="<p>Teskari reja (taxminiy, eʼlondan keyin aniqlanadi): muddatdan 6 oy oldin muvofiqlik va tajriba hujjatlari; 4 oy oldin tavsiya beruvçilar bilan kelişiş; 3 oy oldin inşo qoralamalari; 1 oy oldin tahrir va töliq ariza; 1 hafta oldin topşiriş. Elçixona sahifasini oyiga bir marta tekşiring va yangilaniş sanasini yozib boring.</p>",
             take="Ötgan sikl yopilgan, keyingisi eʼlon qilinmagan. Eʼlon çiqqaç muddatdan orqaga 6 oylik reja tuzing.",
             task_b="Faraz bilan reja",
             task=["Keyingi muddat iyun oxiri deb faraz qilib, 6 oylik teskari reja yozing va uni «faraz» deb belgilang."],
             src=f"{EMB_FUL}; {EMB_EXCH}. {HOL2}."),
        dict(t=M_TITLES[6][4], short="J-1", min=10,
             hook="Fulbright tugagaç AQŞda işlab qolişni rejalaştirgan nomzod qonuniy tösiqqa duç keladi. Bu tösiqni arizadan oldin biliş kerak. "
                  "Bu darsda 212(e) talabini körib çiqamiz.",
             main="""<p>Elçixona eʼloniga köra, grant J-1 vizasi bilan; tugagaç kamida 2 yil Özbekistonga qaytiş kerak.</p>
<div class="tbl"><table><thead><tr><th>Savol</th><th>Javob (Harvard xalqaro ofisi)</th></tr></thead><tbody>
<tr><td>Qaçon qöllanadi</td><td>Hukumat yoki xalqaro taşkilot mablaği; [[Exchange Visitor Skills List]]; AQŞda klinik tibbiy taʼlim</td></tr>
<tr><td>Nimani çeklaydi</td><td>Immigratsion viza, H yoki L vizasi, AQŞ içida maqom özgartiriş</td></tr>
<tr><td>Qanday bilinadi</td><td>DS-2019 va vizadagi belgi; noaniq bölsa, [[Advisory Opinion]]</td></tr>
</tbody></table></div>""",
             info="<p>Davlat departamenti sahifasida ozod qiliş asoslaridan biri favqulodda qiyinçilik yoki taʼqib; bunda DS-3035 bilan birga USCIS ga Form I-612 topşiriladi. Ozod qiliş oddiy yöl hisoblanmaydi, rejani unga qurmang. Şaxsiy holat böyiça universitet xalqaro ofisi yoki immigratsiya advokati bilan maslahatlaşing.</p>",
             take="Fulbright J-1 bilan: grantdan keyin 2 yil vatanda yaşaş talabi. AQŞda qoliş rejasi bölsa, Fulbright mos kelmaydi.",
             task_b="5 yillik rejangiz",
             task=["Magistraturadan keyingi 5 yillik rejangizni yozing.", "Bu reja 2 yillik talab bilan mos keladimi? Ha yoki yöq va nega."],
             src=f"{EMB_FUL}; {HARVARD_212E}; {DOS_WAIVER}. {HOL}."),
    ])

# ───────────────────────────── M7 ─────────────────────────────
MODULES[7] = dict(
    lead="AQŞda PhD köpinça iş kabi moliyalaştiriladi: kafedra öqiş tölovini qoplaydi va oylik beradi. Magistratura esa köpinça öz hisobidan. "
         "Bu modulda dasturlarni şu farqqa qarab tanlaysiz va takliflarni raqam bilan soliştirasiz. "
         "Oxirida sizda <strong>moliya paketi taqqoslagiçi</strong> böladi.",
    weeks="1", pass_time="~1 hafta (darslar ~1 soat + taqqoslagiç)",
    next=("<h2>Keyingi qadam: viza</h2>" + bar(88, "IV bosqiç: 1 / 2 modul · Rejangiz 88% tayyor") +
          '<div class="mv-k" data-mn="m7"><b>Moliya taqqoslaşi tayyor.</b> Taklifni qabul qilgaç, universitet I-20 yoki DS-2019 beradi. '
          "M8 da Toşkentdagi viza tartibini, maqomni saqlaşni va işlaş qoidalarini örganasiz.</div>"
          '<div class="mv-row"><a class="btn btn-p" href="usa-lab-o.html?m=8">M8: viza va maqom</a></div>'),
    lessons=[
        dict(t=M_TITLES[7][0], short="Farq", min=10,
             hook="Bir kafedrada PhD talabasi oylik oladi, magistratura talabasi öqiş tölovini özi tölaydi. Bu farqni bilmasangiz, qabul xati bilan katta hisob ham keladi. "
                  "Bu darsda yölni <b>mablağ manbasiga</b> qarab tanlaymiz.",
             main="""<div class="tbl"><table><thead><tr><th></th><th>Magistratura</th><th>PhD</th></tr></thead><tbody>
<tr><td>Odatiy moliya</td><td>Köpinça öz hisobidan</td><td>Köpinça kafedra paketi</td></tr>
<tr><td>Rasmiy misol</td><td>Buffalo: asosan öz hisobidan. Princeton markazdan moliyalaştirmaydi, ayrim kafedralar qisman yoki töliq</td><td>EducationUSA: assistentlik, öqiş tölovidan ozod qiliş va stipendiya keng tarqalgan</td></tr>
<tr><td>Kimga mos</td><td>Özi tölay oladigan yoki taşqi stipendiyasi bor (Fulbright, M6)</td><td>Ilmiy tajribasi bor, 5 yillik tadqiqotga tayyor</td></tr>
</tbody></table></div>""",
             info="<p>Moliyasiz magistratura va budjetingiz yetmaydi: bu yöl real bölmaydi. Muqobil: Fulbright, moliyalaştiradigan magistratura kafedralari yoki töğridan-töğri PhD. AQŞ PhD ga köpinça bakalavrdan keyin ham kiriş mumkin (M1); kafedra qoidasini tekşiring.</p>",
             take="Magistratura köpinça öz hisobidan, PhD köpinça kafedra paketi bilan. Yölni <b>mablağ manbasiga</b> qarab tanlang.",
             task_b="Sizning maqsadingiz",
             task=["Maqsadingiz magistraturami yoki PhD? Moliya böyiça ikki dalil bilan yozing."],
             src=f"{BUFFALO}; {PRINCETON_MS}; {EDUSA_GR}. {HOL}."),
        dict(t=M_TITLES[7][1], short="Paket", min=12,
             hook="«Töliq moliyalaştirilgan» degan söz kafedradan kafedraga har xil maʼno beradi: neça yil, yozda stipendiya bormi, suğurta kimdan, neça soat dars berasiz. "
                  "Bu darsda paketni beş qismga ajratamiz.",
             fun="Stipendiya 9 oylik bölsa, yoz ham ovqatsiz qolmasin 🙂",
             main="""<div class="tbl"><table><thead><tr><th>Qism</th><th>Savol</th></tr></thead><tbody>
<tr><td>Stipendiya ([[stipend]])</td><td>Qança; 9 oylikmi yoki 12 oylik?</td></tr>
<tr><td>Öqiş tölovidan ozod qiliş ([[tuition remission]])</td><td>Töliqmi; yiğimlar ([[fees]]) kiradimi?</td></tr>
<tr><td>Tibbiy suğurta</td><td>Kim tölaydi; oila aʼzolari uçun?</td></tr>
<tr><td>Kafolatlangan yillar</td><td>Neça yil; keyin nima?</td></tr>
<tr><td>Majburiyat</td><td>TA yoki RA; haftasiga neça soat?</td></tr>
</tbody></table></div>""",
             info_t="Ikki rasmiy misol",
             info="<p><b>Duke Graduate School:</b> birinçi 5 yil stipendiya, öqiş tölovi va majburiy yiğimlar kafolatlangan; stipendiya 12 oylik; birinçi 6 yil suğurta badali qoplanadi; oila aʼzolari suğurtasi öz hisobingizdan. Sahifada kafedralar farq qilişi yozilgan.</p>"
                  "<p><b>Boston universiteti, Earth &amp; Environment:</b> yaxşi holatdagi talabaga 5 yilgaça stipendiya va suğurta; TA, RA va birinçi yilda majburiyatsiz [[fellowship]]; öqiş va yiğimlar töliq qoplanadi. Summani har doim manba yili bilan yozing.</p>",
             take="Paketni beş qismda tekşiring: stipendiya, öqiş tölovi, suğurta, yillar, majburiyat. Har qism kafedra sahifasidan alohida.",
             task_b="Bitta PhD paketi",
             task=["Bitta PhD dasturining paketini 5 qism böyiça yozing, manba va yil bilan."],
             src=f"{DUKE}; {BU}. {HOL}."),
        dict(t=M_TITLES[7][2], short="Kafedra", min=12,
             hook="Kafedra sahifasida eng muhim maʼlumot köpinça [[FAQ]] yoki [[handbook]] içida turadi. 15 daqiqalik tekşiruv ariza tölovini behuda tölaşdan saqlaydi. "
                  "Bu darsda 10 savolga javob qidiramiz.",
             main="""<ol><li>PhD ga qabul qilinganlarning hammasi moliyalaştiriladimi?</li><li>Neça yil kafolatlanadi?</li><li>Stipendiya summasi va davri?</li><li>Xalqaro talabaga ham şu paketmi?</li><li>GRE talab qilinadimi?</li><li>Ingliz tili testi va minimal ball?</li><li>Ariza tölovi va ozod qiliş?</li><li>Kafedra muddati?</li><li>Professor bilan oldindan boğlaniş tavsiya qilinadimi?</li><li>Içki [[fellowship]] uçun alohida ariza kerakmi?</li></ol>""",
             info="<p>EducationUSA maʼlumotiga köra, stipendiya va grant muddatlari dastur boşlanişidan 18 oy oldin bölişi mumkin; professorlar köpinça grant oluvçilarni tanlaşda qatnaşadi, şuning uçun kafedra professorlari bilan boğlaniş foydali. Professorga xat yoziş usuli PhD dasturi M3 da. Javob topilmasa, kafedraning [[graduate coordinator]] manziliga qisqa savol yozing va javobni saqlang.</p>",
             take="Har kafedrada 10 savolga javob toping. Javobsiz qolgan savolni koordinatorga yozma yuboring.",
             task_b="Ikki kafedra tekşiruvi",
             task=["2 kafedra sahifasini 10 savol böyiça tekşiring.", "Javobsiz qolgan savollarni yozing."],
             src=f"{EDUSA_GR}. {HOL}."),
        dict(t=M_TITLES[7][3], short="Grantlar", min=8,
             hook="Internetdagi «AQŞdagi eng yaxşi PhD grantlari» röyxatining katta qismi faqat AQŞ fuqarolari uçun. Ularga vaqt sarflaşdan oldin bitta qatorni tekşiring. "
                  "Bu darsda öşa qatorni topamiz.",
             main="""<p>Har grant sahifasida [[eligibility]] bölimini oçing va fuqarolik talabini toping. Misol: NSF ning GRFP talabi AQŞ fuqarosi yoki doimiy rezidenti. Demak Özbekiston fuqarosiga yopiq.</p>
<div class="tbl"><table><thead><tr><th>Grant manbasi</th><th>Xalqaro talabaga</th></tr></thead><tbody>
<tr><td>AQŞ federal agentliklari</td><td>Köpinça yopiq</td></tr>
<tr><td>Kafedra va universitet [[fellowship]]lari</td><td>Köpinça qabul paketi içida (7.2)</td></tr>
<tr><td>Öz mamlakati moliyasi</td><td>Mumkin (Boston universiteti)</td></tr>
<tr><td>Fulbright</td><td>Magistratura (M6)</td></tr>
</tbody></table></div>""",
             info="<p>Grant sahifasida «[[U.S. citizen]]», «[[permanent resident]]» yoki «[[eligible noncitizen]]» sözlari bölsa, u sizga yopiq bölişi ehtimoli yuqori. Bunday grantni röyxatdan çiqaring.</p>",
             take="Har grantni fuqarolik qatori bilan filtrlang. Federal grantlar köpinça faqat AQŞ fuqarolari va rezidentlari uçun.",
             task_b="Uç grant filtri",
             task=["Topgan 3 grantingizni fuqarolik qatori böyiça tekşiring: oçiq yoki yopiq, dalil bilan."],
             src=f"{NSF_GRFP}; {BU}. {HOL}."),
        dict(t=M_TITLES[7][4], short="Taklif", min=12,
             hook="Ikki moliyalaştirilgan PhD taklifi bir xil körinadi: biri qimmat şaharda, boşqasi yozda stipendiya bermaydi. Raqam bilan soliştirmasangiz, kamomadni birinçi qişda bilasiz. "
                  "Bu darsda takliflarni oylik qoldiq bilan soliştiramiz.",
             main="""<p><b>Oylik sof qoldiq</b> = (yillik stipendiya − qoplanmagan yiğim va suğurta) ÷ 12 − oylik ijara va yaşaş.</p>
<ul><li>Stipendiya 9 oylik bölsa, yozgi oylarga manba bormi?</li><li>Kafolatlangan yillar soni bir xilmi?</li><li>TA soatlari tadqiqot vaqtini qançalik kamaytiradi?</li></ul>
<p><b>15-aprel qarori (CGS):</b> kuzgi semestrga qabul qilingan talaba moliya takliflarini 15-aprelgaça qabul qiliş yoki rad etişga majbur emas. Qaror faqat moliya takliflariga va uni imzolagan universitetlarga tegişli.</p>""",
             info="<p>CGS hujjatiga köra, 2027-yil kuzidan boşlanadigan dasturlar uçun universitetlar qarorni qayta imzolaşi kerak. Universitet imzolaganini tekşiring. 15-aprelgaça taklifni qabul qilib, keyin boşqasini tanlasangiz, voz keçişni yozma bildiring.</p>",
             take="Takliflarni oylik qoldiq, yozgi stipendiya, kafolat yillari va majburiyat böyiça soliştiring. 15-aprel qarori imzolagan universitetlarda amal qiladi.",
             task_b="Ikki taklif hisobi",
             task=["2 taklif (yoki 2 kafedra sahifasi) uçun oylik sof qoldiqni hisoblang.", "Universitetlar CGS qarorini imzolaganini tekşiring."],
             src=f"{CGS}; {DUKE}; {BU}. {HOL}."),
    ])

# ───────────────────────────── M8 ─────────────────────────────
MODULES[8] = dict(
    lead="Qabul va moliya hal bölgaç, oxirgi tösiq viza. Bu modulda Toşkentdagi viza tartibini, AQŞga kelgandan keyin maqomni saqlaşni va öqiş davrida qayerda, qança işlaş mumkinligini örganasiz. "
         "Oxirida sizda <strong>viza va maqom nazorat röyxati</strong> böladi.",
    weeks="1", pass_time="~1 hafta (darslar ~1 soat + nazorat röyxati)",
    next=("<h2>USA dasturi yakunlandi</h2>" + bar(100, "IV bosqiç: 2 / 2 modul · Rejangiz 100% tayyor") +
          '<div class="mv-k" data-mn="m8"><b>Sizda AQŞ paketi bor:</b> universitet kartasi, xarajat va budjet rejasi, yordam röyxati, ariza paketi, dastur kartasi, moliya taqqoslaşi va viza röyxati. '
          "Endi siyosat özgarişini oyiga bir marta kuzatasiz.</div>"
          "<p>Hujjatlarni (inşo, CV, tavsiya, maqsad bayonnomasi) Bakalavr, Magistratura yoki PhD dasturida özingiz yozasiz.</p>"
          '<div class="mv-row"><a class="btn btn-p" href="dashboard.html">Mening kabinetim</a><a class="btn btn-g" href="index.html#labs">Boşqa dasturlar</a></div>'),
    lessons=[
        dict(t=M_TITLES[8][0], short="F-1 / J-1", min=10,
             hook="Viza turini siz tanlamaysiz, u qabul qilingan dasturdan kelib çiqadi. Lekin har birining qoidasi kelajak rejangizga boşqaça taʼsir qiladi. "
                  "Bu darsda ikkalasini soliştiramiz.",
             main="""<div class="tbl"><table><thead><tr><th></th><th>F-1</th><th>J-1</th></tr></thead><tbody>
<tr><td>Kimga</td><td>Daraja uçun öqiydigan talaba</td><td>Almaşinuv qatnaşçisi (UGRAD, Fulbright)</td></tr>
<tr><td>Hujjat</td><td>Form I-20 (SEVP tasdiqlagan muassasa)</td><td>DS-2019 (dastur homiysi)</td></tr>
<tr><td>2 yillik talab</td><td>Yöq</td><td>Hukumat mablaği bölsa, 212(e) (M5–M6)</td></tr>
</tbody></table></div>
<p>Davlat departamenti böyiça, yangi talabaga viza öqiş boşlanişidan 365 kun oldingaça berilişi mumkin, AQŞga esa 30 kundan oldin kirilmaydi. Kiriş haqida qarorni çegarada CBP xodimi qabul qiladi.</p>""",
             info="<p>F-1 ketma-ketligi: SEVP tasdiqlagan muassasaga qabul (M1); muassasa sizni SEVIS ga kiritadi va I-20 beradi (mablağ hujjati, M2); SEVIS I-901 tölovi (ICE); DS-160 va viza suhbati (8.2).</p>",
             take="F-1: daraja, I-20. J-1: almaşinuv, DS-2019, baʼzan 2 yillik talab. Viza 365 kun oldin, kiriş 30 kun oldin.",
             task_b="Sizning sanalaringiz",
             task=["Yölingizda qaysi viza va qaysi hujjat böladi?", "Öqiş boşlanişidan 365 va 30 kunlik sanalarni hisoblang."],
             src=f"{DOS_VISA}; {SEVIS}; {SITS_SEARCH}; {HARVARD_212E}. {HOL}."),
        dict(t=M_TITLES[8][1], short="Ariza", min=12,
             hook="Viza suhbati bir neça daqiqa davom etadi, tayyorgarlik esa oylar oldin boşlanadi. Elçixona qaysi hujjat foydali ekanini oçiq yozgan. "
                  "Bu darsda Toşkentdagi bosqiçlarni va tölovlarni körib çiqamiz.",
             main=f"""<ol><li>Viza turini aniqlang (F yoki J).</li><li>DS-160: har arizaçiga, yoşidan qatʼi nazar, alohida forma.</li><li>Viza yiğimini tölang; tasdiq 2 iş kunigaça olişi mumkin.</li><li>Suhbatga yoziling.</li><li>Hujjatlar: talaba hujjatlari va Özbekiston bilan boğliqlik dalillari.</li><li>Suhbat: natija odatda darhol aytiladi.</li></ol>
<div class="tbl"><table><thead><tr><th>Tölov</th><th>Summa ({HOL2})</th></tr></thead><tbody>
<tr><td>Viza ariza yiğimi (MRV)</td><td>185 dollar</td></tr>
<tr><td>SEVIS I-901</td><td>F-1: 350 dollar; J-1: 220 dollar</td></tr>
<tr><td>[[Visa Integrity Fee]]</td><td>250 dollar; ayrim konsulliklar 2026-yil maydan undira boşlagan</td></tr>
</tbody></table></div>""",
             info="<p>Elçixona sahifasiga köra, mehmonxona bandi, aviabilet va bank köçirmalari odatda foydali emas, konsul özi kerak deb bilgan hujjatni köradi. I-20 dagi mablağ hujjati universitetga oldindan topşirilgan (M2). Toşkentda Visa Integrity Fee undirilişini elçixonaning tölov sahifasidan tekşiring.</p>"
                  "<p>2025-yil iyunida Davlat departamenti F, M va J arizaçilarini onlayn mavjudlikni ham öz içiga olgan kengaytirilgan tekşiruvdan ötkazişini eʼlon qildi; ijtimoiy tarmoq profillarini «public» holatga ötkaziş körsatmasi beriladi (MIT xalqaro ofisi). Suhbatda faqat haqiqatni gapiring: muhim faktni notöğri körsatiş doimiy rad javobiga olib kelişi mumkin.</p>",
             take="Toşkentdagi tartib:<ol><li>DS-160;</li><li>yiğim;</li><li>navbat;</li><li>hujjatlar;</li><li>suhbat.</li></ol>Budjetingizga MRV, SEVIS va Visa Integrity Fee ni qöşing.",
             task_b="Viza bosqiçlari va tölovlar",
             task=["6 bosqiç uçun sana va masʼulni yozing; tölovlar summasini hisoblang.", "Özbekiston bilan boğliqligingizni körsatadigan 3 haqiqiy dalilni yozing."],
             src=f"{EMB_VISA}; {EMB_DOCS}; {DS160}; {DOS_VISA}; {SEVIS}; {BU_VIF}; {MIT_VET}. {HOL2}."),
        dict(t=M_TITLES[8][2], short="Maqom", min=10,
             hook="Viza AQŞga kiriş uçun. AQŞ içida sizni maqom (F-1 yoki J-1 status) qoidalari himoya qiladi. Maqomni yöqotiş öqişni ham, keyingi vizani ham xavf ostiga qöyadi. "
                  "Bu darsda asosiy qoidalarni yiğamiz.",
             main=f"""<div class="tbl"><table><thead><tr><th>Band</th><th>Kim bilan tekşiriladi</th></tr></thead><tbody>
<tr><td>Har semestr töliq öquv yuklamasi</td><td>Xalqaro talabalar bölimi (ISSS, OIS)</td></tr>
<tr><td>I-20 yoki DS-2019 muddati va maʼlumoti töğri</td><td>Şu bölim, özgariş bölsa oldindan</td></tr>
<tr><td>Ruxsatsiz işlamaslik (8.4)</td><td>Işdan oldin yozma tasdiq</td></tr>
<tr><td>Manzil va dastur özgarişi haqida xabar</td><td>Bölim körsatgan muddatda</td></tr>
<tr><td>AQŞdan çiqib qaytişdan oldin hujjatlar</td><td>Bölim</td></tr>
</tbody></table></div>
<p>{HOL2}: F-1 va J-1 talabalar avvalgidek öqiş davomiga (D/S) kiritiladi. 4 yillik çeklov qoidasini sud 16.11.2026 da bekor qilgan, DHS apellyatsiya berişi kutilmoqda.</p>""",
             info="<p>DHS 17.07.2026 da D/S örniga belgilangan muddat (dastur oxiri yoki 4 yil + 30 kun) va muddatni uzaytiriş tartibini kirituvçi qoidani çiqargan; F-1 uçun bitiruvdan keyingi muhlat 60 kundan 30 kunga qisqarardi. Sud uni 14.09.2026 da töxtatgan va 16.11.2026 da bekor qilgan (Massaçusets federal okrug sudi). Yuqori sud boşqaça qaror qilsa, qoidalar özgarişi mumkin: universitetingiz xalqaro bölimini kuzating.</p>",
             take="<b>Maqom</b> qoidalari:<ul><li>töliq yuklama;</li><li>töğri hujjat;</li><li>ruxsatsiz iş yöq;</li><li>özgarişlar haqida xabar.</li></ul> Har savolga xalqaro bölimdan yozma javob oling.",
             task_b="Maqom qoidalari",
             task=["Közlagan universitetingiz xalqaro talabalar bölimi sahifasini toping.", "Undagi maqom qoidalaridan 5 tasini yozing."],
             src=f"{BERKELEY_DS}; {FR_DS}; {GMU}. {HOL2}."),
        dict(t=M_TITLES[8][3], short="Iş", min=12,
             hook="«AQŞda öqib işlayman» rejasi qaysi iş, qayerda va qaçon ekaniga boğliq. Notöğri iş bir martaning özida maqomni yöqotişga olib kelişi mumkin. "
                  "Bu darsda ruxsat etilgan iş turlarini ajratamiz.",
             main="""<div class="tbl"><table><thead><tr><th>Tur</th><th>Qoida (George Mason universiteti)</th></tr></thead><tbody>
<tr><td>Kampusda işlaş</td><td>Semestr davomida haftasiga 20 soatgaça; dastur tugagaç töxtaydi</td></tr>
<tr><td>Kampusdan taşqari</td><td>Faqat yozma ruxsat bilan: xalqaro bölim yoki USCIS</td></tr>
<tr><td>CPT</td><td>Öquv reja bilan boğliq amaliyot, alohida ruxsat bilan</td></tr>
<tr><td>OPT</td><td>Har daraja uçun 12 oy; öqiş davomidagi OPT keyingisini qisqartiradi</td></tr>
<tr><td>STEM OPT</td><td>DHS röyxatidagi STEM bitiruvçisiga qöşimça 24 oy</td></tr>
</tbody></table></div>""",
             info="<p>DHS 08.10.2026 da OPT uçun universitet tölaydigan yangi tölovni taklif qilgan (Wyoming universiteti: 70 000 dollar). Bu taklif, amalda emas: şarhlar 09.11.2026 da yopilgan, yakuniy qoida va sana nomaʼlum (Yale OISS). Yale yana yozadi: DHS 2026-yil avgustida CPT ga çeklov qöygan yöriqnoma çiqargan. Kampusdagi iş öqiş tölovini qoplamaydi. J-1 qatnaşçilari uçun iş qoidalarini dastur homiysidan söraysiz.</p>",
             take="F-1: kampusda haftasiga 20 soatgaça, taşqarida faqat yozma ruxsat bilan; OPT 12 oy, STEM OPT qöşimça 24 oy. OPT tölovi taklifini kuzating.",
             task_b="Sizning iş rejangiz",
             task=["Sohangiz STEM bölsa, OPT va STEM OPT bilan bitiruvdan keyingi umumiy muddatni yozing.", "Kampusdagi işdan kutilgan oylik daromad M2 dagi narxning neça foizi?"],
             src=f"{GMU}; {YALE_OPT}; {UWYO_OPT}. {HOL2}."),
        dict(t=M_TITLES[8][4], short="Kuzatuv", min=8,
             hook="AQŞ viza siyosati tez özgaradi va har özgariş haqida ijtimoiy tarmoqlarda notöğri talqin çiqadi. Faqat rasmiy manba va sana bilan işlang. "
                  "Bu darsda kuzatuv jadvalini tuzamiz.",
             main=f"""<div class="tbl"><table><thead><tr><th>{HOL2}</th><th>Holat</th></tr></thead><tbody>
<tr><td>Kiriş çeklovlari (proklamatsiyalar 10949, 10998)</td><td>Özbekiston röyxatlarda yöq (Brown ISSS, 27.01.2026)</td></tr>
<tr><td>D/S örniga 4 yillik muddat</td><td>Sud bekor qilgan (16.11.2026)</td></tr>
<tr><td>OPT tölovi</td><td>Taklif bosqiçida</td></tr>
<tr><td>Visa Integrity Fee</td><td>Ayrim konsulliklarda undirilmoqda</td></tr>
</tbody></table></div>
<p>Har özgariş uçun yozing: sana, manba, kimga tegişli, sizga taʼsiri.</p>""",
             info="<div class=\"tbl\"><table><thead><tr><th>Manba</th><th>Qança tez-tez</th></tr></thead><tbody>"
                  "<tr><td>AQŞ elçixonasi (Toşkent) viza sahifalari</td><td>Oyiga bir marta, ariza davrida haftalik</td></tr>"
                  "<tr><td>Davlat departamenti talaba vizasi sahifasi</td><td>Oyiga bir marta</td></tr>"
                  "<tr><td>Universitetingiz xalqaro bölimi</td><td>Har yangilikda</td></tr></tbody></table></div>"
                  "<p>Kompas Lab USA dasturi sahifasida holatni sana bilan yangilaydi. Siyosat talaba vizasini yopsa, faol obunaçilarga boşqa dasturga ötiş taklif qilinadi.</p>",
             take="Siyosatni rasmiy manba va sana bilan kuzating. Ijtimoiy tarmoqdagi xabarni rasmiy sahifada topmaguningizça qaror qilmang.",
             task_b="Kuzatuv jadvalingiz",
             task=["Jadvalingizga 3 manba va eslatma sanasini qöşing.", "Bugungi holatni sana bilan yozing."],
             ph="20.11.2026: O'zbekiston proklamatsiya ro'yxatlarida yo'q (Brown ISSS). Eslatma: har oy ... kuni",
             src=f"{BROWN_TB}; {BERKELEY_DS}; {YALE_OPT}; {BU_VIF}; {EMB_VISA}; {DOS_VISA}. {HOL2}."),
    ])
