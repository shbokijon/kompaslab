from common import a, US_VISA, US_SEVIS, UK_VISA, DE_VISA, IT_VISA, KR_VISA, HOL, STD

UK_TB = a("https://www.gov.uk/tb-test-visa", "GOV.UK: viza uchun sil (TB) testi")
ORCID = a("https://orcid.org", "ORCID")

MOD = dict(
    title="Qabuldan keyin: viza va jo'nash",
    desc="Bachelor Lab M16: qabul xatidan keyingi 2 hafta (shartli/shartsiz qabul, depozit, CAS yoki I-20), talaba vizasi, uy-joy, sug'urta va bank, 30 kunlik jo'nash oldi ro'yxat, birinchi yil. Natija: jo'nash oldi nazorat ro'yxati va birinchi yil rejasi.",
    lead="Qabul xati yo'lning oxiri emas. Viza, uy-joy, sug'urta va pul o'tkazish o'z muddatlari bilan keladi, va bitta kechikish o'qish boshlanishini surishi mumkin. Bu modul qabuldan birinchi semestrgacha bo'lgan yo'lni tartibga soladi.",
    hero="seedling", weeks="2", next="", next_href="",
    goals=[("shield", "Jo'nash oldi nazorat ro'yxati (Pre-departure checklist)", "hujjatlar, sog'liq, pul, aloqa, birinchi kun"),
           ("calendar", "Viza yo'l xaritasi", "mamlakatingiz bo'yicha bosqichlar va sanalar"),
           ("seedling", "Birinchi yil rejasi", "akademik, yordam xizmatlari, salomatlik")],
    warn=f"Viza qoidalari, to'lovlar va moliyaviy talablar tez-tez o'zgaradi. Bu moduldagi ma'lumot {HOL}; har qadamni konsullik va universitetning xalqaro bo'limi bilan tekshiring. Kompas Lab vizani kafolatlamaydi va viza agentligi emas.",
    lessons=[
        dict(t="Qabul xati: birinchi 2 hafta", short="2 hafta", min=25, kind="🎯 Mini-test", ic="scroll",
             hook="Qabul xatidagi bitta jumla, masalan \"javob berish muddati\" yoki \"shart\", keyingi hamma bosqichni belgilaydi. Xatni to'liq o'qing va ro'yxatga aylantiring.",
             body=f"""<h4>Xatni o'qish</h4>
<div class="tbl"><table><thead><tr><th>Band</th><th>Savol</th></tr></thead><tbody>
<tr><td>Qabul turi</td><td>Shartli ([[conditional]]) yoki shartsiz ([[unconditional]])? Shart nima: attestat bahosi, til testi, hujjat?</td></tr>
<tr><td>Javob muddati</td><td>Qachongacha qabul qilish yoki rad etish kerak?</td></tr>
<tr><td>Depozit</td><td>Joyni band qilish uchun to'lov bormi? Qaytariladimi?</td></tr>
<tr><td>Viza hujjati</td><td>Universitet qaysi hujjatni beradi va nimani so'raydi?</td></tr>
</tbody></table></div>
<h4>Viza uchun universitet hujjatlari</h4>
<ul><li><b>AQSh</b>: I-20 forma; universitet moliyaviy imkoniyat dalilini so'raydi.</li><li><b>Buyuk Britaniya</b>: CAS (o'qishga qabul tasdig'i), shartlar bajarilgandan keyin beriladi.</li><li><b>Germaniya</b>: qabul xati ([[Zulassungsbescheid]]).</li><li><b>Italiya</b>: Universitaly tasdig'i va universitet xati (M14).</li><li><b>Koreya, Xitoy</b>: qabul xati va mamlakatga xos forma (Xitoyda JW201/JW202).</li></ul>
<div class="box warn">Birinchi 2 hafta ichida: javob bering, depozitni rasmiy kanal orqali to'lang, viza hujjati uchun talablarni bajaring va nazorat jadvalini yangilang.</div>
<div class="srcs">Manba: {US_VISA}; {UK_VISA}; {DE_VISA}; {IT_VISA}. {HOL}.</div>""",
             take="Qabul xatidan to'rt narsani ajrating: qabul turi va shart, javob muddati, depozit, viza hujjati. Birinchi 2 haftada hammasiga harakat boshlang.",
             quiz=[("Shartli qabulda shart bajarilmasa ham joy saqlanadi.", "n", "Noto'g'ri: shart bajarilmasa qabul kuchini yo'qotishi mumkin."),
                   ("UK talaba vizasi uchun universitet CAS beradi.", "t", "To'g'ri: CAS o'qishga qabul tasdig'i."),
                   ("AQSh talaba vizasi uchun universitet I-20 formasini beradi.", "t", "To'g'ri."),
                   ("Depozitni universitet xodimining shaxsiy kartasiga o'tkazish mumkin.", "n", "Noto'g'ri: faqat rasmiy to'lov kanali orqali.")],
             task="<ul><li>Qabul xatingizdan (yoki namunaviy xatdan) to'rt bandni ajratib yozing.</li><li>Birinchi 2 hafta uchun 5 ta harakatni sanalar bilan yozing.</li></ul>",
             ph="Turi: ... Muddat: ... Depozit: ... Viza hujjati: ... Harakatlar: 1) ... 2) ..."),
        dict(t="Talaba vizasi", short="Viza", min=35, kind="🗺 Bosqichlar", ic="shield",
             hook="Viza qarorini konsullik chiqaradi, universitet emas. Hujjatlar to'liq va izchil bo'lsa, xavf kamayadi, lekin kafolat yo'q.",
             body=f"""<h4>Umumiy bosqichlar</h4>
<ol><li>Universitet viza hujjati (I-20, CAS, qabul xati).</li><li>Rasmiy to'lovlar (masalan AQShda SEVIS I-901 va viza arizasi to'lovi; UK da viza to'lovi va sog'liqni saqlash qo'shimcha to'lovi).</li><li>Onlayn ariza formasi.</li><li>Moliyaviy imkoniyat dalili (bank ko'chirmasi, homiylik xati, stipendiya xati).</li><li>Biometrika va (ba'zi mamlakatlarda) intervyu.</li><li>Tibbiy talablar: masalan UK uchun O'zbekiston fuqarolaridan sil (TB) testi talab qilinadi; ro'yxatni GOV.UK'dan tekshiring.</li></ol>
<h4>Mamlakat bo'yicha manbalar</h4>
<div class="tbl"><table><thead><tr><th>Mamlakat</th><th>Rasmiy manba</th></tr></thead><tbody>
<tr><td>AQSh (F-1)</td><td>{US_VISA}; {US_SEVIS}</td></tr>
<tr><td>Buyuk Britaniya (Student visa)</td><td>{UK_VISA}; {UK_TB}</td></tr>
<tr><td>Germaniya</td><td>{DE_VISA}</td></tr>
<tr><td>Italiya</td><td>{IT_VISA}</td></tr>
<tr><td>Koreya</td><td>{KR_VISA}</td></tr>
</tbody></table></div>
<h4>18 yoshga to'lmaganlar</h4>
<p>Voyaga yetmagan abituriyentlar uchun qo'shimcha talablar bo'lishi mumkin: ota-ona roziligi, vasiylik yoki yashash tartibi haqida hujjat. Mamlakat rasmiy sahifasidan va universitetdan tekshiring.</p>
<div class="box warn">\"Vizani kafolatlaymiz\" yoki \"bank ko'chirmasini tayyorlab beramiz\" degan takliflarni rad eting. Soxta hujjat vizadan bosh tortish va kelajakdagi arizalarga ta'sir qilishi mumkin.</div>""",
             take="Viza: universitet hujjati, rasmiy to'lovlar, forma, moliyaviy dalil, biometrika va tibbiy talablar. 18 yoshgacha bo'lsa qo'shimcha hujjatlar; soxta hujjat yo'q.",
             task="<ul><li>Mamlakatingiz bo'yicha viza bosqichlarini rasmiy sahifadan yozing.</li><li>Har bosqich uchun sana va kerakli hujjatni qo'shing.</li></ul>",
             ph="1) CAS: ... 2) To'lov: ... 3) Forma: ... 4) Moliya: ... 5) Biometrika: ... 6) TB testi: ..."),
        dict(t="Uy-joy, sug'urta va bank", short="Uy, bank", min=30, kind="🏠 Reja", ic="money",
             hook="Ijara firibgarligi xalqaro talabalar orasida keng tarqalgan: uy rasmi chiroyli, narx past, \"faqat oldindan to'lov\". Uy-joy masalasini rasmiy yo'ldan boshlang.",
             body="""<h4>Uy-joy</h4>
<ul><li><b>Universitet yotoqxonasi</b>: birinchi yil uchun eng xavfsiz variant. Ariza muddati qabul xatidan keyin tez keladi; ba'zi universitetlar birinchi kurs talabalariga kafolat beradi.</li><li><b>Ijara</b>: universitetning ijara bo'yicha maslahat sahifasidan foydalaning; shartnomani o'qing, depozitni himoyalangan tizim orqali to'lang (mamlakatga qarab).</li><li><b>Ijara xavf belgilari</b>: uyni ko'rmasdan to'lov, pul o'tkazish xizmati orqali to'lov, egasi \"chet elda\", narx bozordan ancha past.</li></ul>
<h4>Tibbiy sug'urta</h4>
<p>Ko'p mamlakatlarda talaba vizasi uchun sug'urta majburiy: UK da viza bilan to'lanadigan sog'liqni saqlash qo'shimcha to'lovi, AQShda ko'pincha universitet sug'urta rejasi, Germaniyada talabalar uchun davlat yoki xususiy sug'urta. Universitet talabini o'qing.</p>
<h4>Bank va pul o'tkazish</h4>
<ul><li>Birinchi oy uchun naqd pul va xalqaro karta (bojxona qoidalari bo'yicha naqd pul chegarasini tekshiring).</li><li>Mahalliy bank hisobini ochish uchun odatda pasport, viza va universitet ma'lumotnomasi kerak.</li><li>O'zbekistondan pul o'tkazish usullari va komissiyalarini oldindan solishtiring.</li></ul>""",
             take="Birinchi yil uchun yotoqxona eng xavfsiz; ijarada uyni ko'rmasdan to'lamang. Sug'urta talabini o'qing, birinchi oy uchun pul va bank rejasini tuzing.",
             task="<ul><li>Uy-joy variantingizni va ariza muddatini yozing.</li><li>Sug'urta talabi va birinchi oy pul rejasini yozing.</li></ul>",
             ph="Uy: yotoqxona, ariza ... gacha. Sug'urta: ... Birinchi oy: ..."),
        dict(t="Jo'nash oldi tayyorgarlik", short="30 kun", min=25, kind="✅ 30 kun", ic="calendar",
             hook="Jo'nashdan oldingi oy tez o'tadi. Ro'yxatsiz biror muhim hujjat yoki dori uyda qolib ketishi mumkin.",
             body="""<h4>30 kunlik ro'yxat bloklari</h4>
<div class="tbl"><table><thead><tr><th>Blok</th><th>Nima</th></tr></thead><tbody>
<tr><td>Hujjatlar</td><td>Pasport (amal qilish muddati), viza, qabul xati, I-20/CAS, attestat va tarjimalar (asl), sug'urta polisi, emlash guvohnomasi; hammasining skan nusxasi bulutda</td></tr>
<tr><td>Sog'liq</td><td>Shifokor ko'rigi, retsept bo'yicha dorilar (retsept va tarjimasi bilan, mamlakat qoidalarini tekshiring), ko'zoynak</td></tr>
<tr><td>Pul</td><td>Xalqaro karta, birinchi oy uchun naqd pul (bojxona chegarasida), bankka ogohlantirish</td></tr>
<tr><td>Aloqa</td><td>Telefon, xalqaro rouming yoki eSIM, oilaviy aloqa rejasi, favqulodda aloqalar ro'yxati</td></tr>
<tr><td>Birinchi kun</td><td>Aeroportdan yotoqxonagacha yo'l, universitet kutib olish xizmati, kelish vaqti, orientatsiya sanasi</td></tr>
<tr><td>Kiyim va narsalar</td><td>Iqlimga mos kiyim, adapter, kichik zaxira</td></tr>
</tbody></table></div>
<div class="box info">Elchixona va konsullik ro'yxati: o'qiyotgan mamlakatdagi O'zbekiston elchixonasi aloqasini yozib qo'ying.</div>""",
             take="30 kunlik ro'yxat: hujjatlar (asl va skan), sog'liq, pul, aloqa, birinchi kun, narsalar. Hammasining nusxasi bulutda.",
             task="<ul><li>Pastdagi vositada jo'nash oldi ro'yxatini to'ldiring.</li><li>Jo'nash sanasidan orqaga 4 haftaga ishlarni taqsimlang.</li></ul>",
             ph="4-hafta: ... 3-hafta: ... 2-hafta: ... 1-hafta: ..."),
        dict(t="Birinchi yil", short="Birinchi yil", min=25, kind="🌱 Reja", ic="seedling",
             hook="Birinchi semestr ko'p talabalar uchun eng qiyin davr: yangi o'qish uslubi, yangi til muhiti va oiladan uzoqlik. Yordam xizmatlarini oldindan bilish muammo kattalashmasdan hal qilishga yordam beradi.",
             body=f"""<h4>Akademik madaniyat</h4>
<ul><li>Mustaqil o'qish: dars soati kam, mustaqil ish ko'p.</li><li>Akademik halollik ([[academic integrity]]): manbasiz ko'chirish va boshqa odamga ish yozdirish jiddiy jazolanadi. AI qoidalari har kursda alohida bo'lishi mumkin.</li><li>O'qituvchining qabul soatlari ([[office hours]]): savol berish odatiy hol.</li></ul>
<h4>Yordam xizmatlari</h4>
<p>Xalqaro talabalar ofisi, akademik yozuv markazi, kutubxona, sog'liq xizmati, ruhiy salomatlik xizmati (maslahat, [[counselling]]). Ularning joyi va aloqasini birinchi haftada yozib oling.</p>
<h4>Ruhiy salomatlik</h4>
<p>Uyni sog'inish, charchoq va xavotir normal. Bir necha hafta davom etsa yoki o'qishga xalaqit bersa, universitet maslahat xizmatiga murojaat qiling: bu bepul va maxfiy (universitet qoidasiga qarab).</p>
<h4>Onlayn ilmiy profil</h4>
<p>Tadqiqotga qiziqsangiz, birinchi yildayoq {ORCID} identifikatorini oching va ilmiy ishlaringizni bitta joyda yuriting. Bakalavr tadqiqot dasturlari va magistratura arizasida foydali.</p>
<div class="srcs">Manba: {ORCID}; universitetlarning xalqaro talabalar sahifalari. {HOL}.</div>""",
             take="Birinchi yilda mustaqil o'qish va akademik halollik asosiy; yordam xizmatlarini birinchi haftada toping, ruhiy salomatlikka e'tibor bering, ORCID oching.",
             task="<ul><li>Universitetingizning 5 ta yordam xizmatini va aloqasini yozing.</li><li>Birinchi semestr uchun 3 ta akademik va 2 ta shaxsiy maqsad yozing.</li></ul>",
             ph="Xizmatlar: ... Akademik maqsadlar: ... Shaxsiy: ..."),
    ],
    tool=dict(id="jonash", short="Jo'nash", h2="Jo'nash oldi nazorat ro'yxati va birinchi yil rejasi", sub="Hujjatlar, viza, uy-joy, pul, aloqa va birinchi yil bitta joyda.",
              h3="Jo'nash rejasi", tag="6 maydon", ic="shield", btn="Rejani saqlash", badge="Yo'lovchi", min=5,
              fields=[dict(k="uni", label="Universitet, mamlakat, o'qish boshlanishi", ph="... · ... · sentabr 2027"),
                      dict(k="viza", label="Viza yo'l xaritasi", hint="bosqich · sana · hujjat", type="area", ph="CAS ... ; to'lov ... ; biometrika ..."),
                      dict(k="uy", label="Uy-joy va sug'urta", type="area", ph="Yotoqxona ... ; sug'urta ..."),
                      dict(k="pul", label="Pul va bank", type="area", ph="Karta ..., naqd ..., bank hisobi ..."),
                      dict(k="royxat", label="30 kunlik ro'yxat", hint="4 hafta bo'yicha", type="area", ph="4-hafta: ... 1-hafta: ..."),
                      dict(k="yil", label="Birinchi yil rejasi", type="area", ph="Yordam xizmatlari ... ; maqsadlar ...")]),
    check=dict(h2="Jo'nash oldi nazorat", sub="Jo'nashdan oldin tekshiring.", h3="10 bandlik nazorat",
               items=["Qabul sharti bajarilgan va tasdiqlangan.", "Depozit rasmiy kanal orqali to'langan.", "Viza olingan va ma'lumotlari tekshirilgan.",
                      "Pasport kamida o'qishning birinchi yili davomida amal qiladi.", "Uy-joy tasdiqlangan, shartnoma o'qilgan.", "Sug'urta talabi bajarilgan.",
                      "Asl hujjatlar qo'l yukida, skan nusxalar bulutda.", "Dorilar retsepti va tarjimasi bor.", "Birinchi kun yo'li va kutib olish rejalashtirilgan.",
                      "Elchixona va favqulodda aloqalar yozilgan."]),
    art_title="Jo'nash oldi nazorat ro'yxati va birinchi yil rejasi", art_short="Jo'nash",
    art=[("Universitet va o'qish boshlanishi", ["uni"]), ("Qabul xati va birinchi 2 hafta", ["a1"]), ("Viza yo'l xaritasi", ["viza", "a2"]),
         ("Uy-joy va sug'urta", ["uy", "a3"]), ("Pul va bank", ["pul"]), ("30 kunlik ro'yxat", ["royxat", "a4"]), ("Birinchi yil rejasi", ["yil", "a5"])],
    tip="Barcha muhim hujjatlarni bitta papkaga, skan nusxalarini bitta bulut papkasiga qo'ying va papka manzilini ota-onangizga ham bering.",
    sources=f"{US_VISA}; {US_SEVIS}; {UK_VISA}; {UK_TB}; {DE_VISA}; {IT_VISA}; {KR_VISA}; {ORCID}. {STD}",
)
