from common import CA, CA_FEE, UCAS, UCAS_INT, UNIASSIST, UNIVERSITALY, CAMPUSCHINA, HOL, STD

MOD = dict(
    title="Ariza platformalari",
    desc="Bachelor Lab M13: Common App, UCAS, to'g'ridan-to'g'ri portallar (uni-assist, Universitaly, CSC, universitet portallari), amaliy topshirish va 40 bandli topshirish oldi nazorat ro'yxati. Natija: kamida bitta topshirilgan ariza.",
    lead="Oylar davomida tayyorlangan hujjatlar oxirgi bosqichda texnik xato tufayli to'liq yetib bormasligi mumkin. Bu modulda har platformaning tuzilmasini o'rganasiz va kamida bitta arizani tekshirib topshirasiz.",
    hero="scroll", weeks="2–3", next="M14 Mamlakatlar boʻyicha imkoniyatlar: Xitoy, Italiya, Singapur", next_href="bachelor-lab-m14.html",
    goals=[("scroll", "Kamida bitta topshirilgan ariza", "tasdiq xati saqlangan"),
           ("shield", "40 bandli nazorat ro'yxati", "har ariza oldidan"),
           ("calendar", "Kuzatuv rejasi", "portal, email, hujjat holati")],
    warn=f"Platformalar interfeysi, ariza to'lovlari va qoidalari har yili yangilanadi. Bu modul tuzilmani o'rgatadi ({HOL}); har qadamni platformaning joriy yo'riqnomasi bilan solishtiring.",
    lessons=[
        dict(t="Common App", short="Common App", min=30, kind="🎯 Mini-test", ic="scroll",
             hook="Common App bir arizani yuzlab AQSh universitetlariga yuborish imkonini beradi. Lekin har universitet o'z qo'shimcha talablarini qo'shadi.",
             body=f"""<h4>Bo'limlar</h4>
<div class="tbl"><table><thead><tr><th>Bo'lim</th><th>Nima</th></tr></thead><tbody>
<tr><td>Profile, Family</td><td>Shaxsiy ma'lumot, oila, fuqarolik</td></tr>
<tr><td>Education</td><td>Maktab, baholar, fanlar; maktab Common App bazasida bo'lmasa, qo'lda qo'shiladi</td></tr>
<tr><td>Testing</td><td>Test natijalari (o'zingiz kiritasiz; rasmiy natijani universitet talab qilsa alohida yuborasiz)</td></tr>
<tr><td>Activities</td><td>10 tagacha faoliyat (M7)</td></tr>
<tr><td>Writing</td><td>Asosiy insho (M9–M10) va qo'shimcha ma'lumot ([[Additional Information]])</td></tr>
<tr><td>Universitetga xos qism</td><td>Qo'shimcha savollar va insholar, ariza oynasi (ED/EA/RD)</td></tr>
<tr><td>Recommenders</td><td>Maslahatchi va o'qituvchilar (M8)</td></tr>
</tbody></table></div>
<h4>To'lov</h4>
<p>Har universitetning o'z ariza to'lovi bor. Common App'ning umumiy to'lovdan ozod qilish mezonlari asosan AQSh abituriyentlari uchun; ba'zi universitetlar xalqaro abituriyentlarga alohida so'rov orqali ozod qilish beradi. Universitet sahifasidan yoki qabul bo'limidan so'rang.</p>
<h4>Additional Information</h4>
<p>Bu bo'limda kontekstni qisqa tushuntiring: O'zbekiston baholash shkalasi, maktabda maslahatchi yo'qligi, oilaviy majburiyat. Ikkinchi insho yozmang.</p>
<div class="srcs">Manba: {CA}; {CA_FEE}. {HOL}.</div>""",
             take="Common App: umumiy bo'limlar + universitetga xos qism + tavsiyalar. To'lovdan ozod qilishni universitetdan so'rang; Additional Information'da kontekstni qisqa yozing.",
             quiz=[("Common App'da asosiy insho har universitet uchun alohida yoziladi.", "n", "Noto'g'ri: asosiy insho bitta, qo'shimcha insholar universitetga xos."),
                   ("Additional Information bo'limida baholash shkalasini tushuntirish mumkin.", "t", "To'g'ri: kontekst uchun mos joy."),
                   ("Maktabingiz Common App bazasida bo'lmasa, ariza berib bo'lmaydi.", "n", "Noto'g'ri: maktabni qo'lda qo'shish mumkin."),
                   ("Ariza oynasi (ED, EA, RD) universitetga xos qismda tanlanadi.", "t", "To'g'ri.")],
             task="<ul><li>Common App hisobingizni oching (yoki mavjudini tekshiring) va har bo'lim holatini yozing.</li><li>Additional Information uchun 3 jumlalik kontekst qoralamasini yozing.</li></ul>",
             ph="Profile ✓, Education ..., Activities ..., Writing ... Additional Info: ..."),
        dict(t="UCAS", short="UCAS", min=25, kind="🗺 Jarayon", ic="compass",
             hook="UCAS orqali bitta ariza bilan Buyuk Britaniyadagi bir nechta universitetga ariza berasiz. Lekin bayonot ham, tavsiya ham hamma tanlovga bir xil boradi.",
             body=f"""<h4>Tuzilma</h4>
<ul><li><b>Tanlovlar</b>: odatda 5 tagacha kurs (ba'zi tibbiyot kabi sohalarda cheklovlar bor).</li><li><b>Shaxsiy bayonot</b>: 2026 qabulidan uch savol (M9).</li><li><b>Tavsiya</b>: bitta umumiy tavsiya (M8). Maktabingiz UCAS'ga ulanmagan bo'lsa, mustaqil abituriyent sifatida ariza berasiz va tavsiya beruvchini o'zingiz kiritasiz.</li><li><b>Baholar va bashorat qilingan natija</b>: maktab tizimingizdagi baholar; bashorat qilingan natija ([[predicted grades]]) odatda tavsiya beruvchi tomonidan.</li><li><b>To'lov</b>: bitta ariza to'lovi (miqdori har yili e'lon qilinadi).</li></ul>
<h4>Kuzatuv</h4>
<p>Topshirgandan keyin UCAS tizimida har universitetning javobi ko'rinadi: shartli, shartsiz, rad. Javob berish muddatlari va asosiy hamda zaxira tanlov ([[firm and insurance]]) qoidalari M15 da.</p>
<div class="box info">Bitta bayonot hamma tanlovga borgani uchun 5 tanlov bir fan atrofida bo'lsin. Masalan, 3 ta informatika va 2 ta fizika bayonotni zaiflashtiradi.</div>
<div class="srcs">Manba: {UCAS}; {UCAS_INT}. {HOL}.</div>""",
             take="UCAS: 5 tagacha tanlov, bitta bayonot, bitta tavsiya, bitta to'lov. Tanlovlar bir fan atrofida bo'lsin; javoblarni UCAS tizimida kuzating.",
             task="<ul><li>UK tanlovlaringizni (5 tagacha) yozing va ular bir fan atrofida ekanini tekshiring.</li><li>Tavsiya beruvchi va bashorat qilingan natija kim tomonidan berilishini yozing.</li></ul>",
             ph="1) ... 2) ... Fan: ... Tavsiya: ... Predicted grades: ..."),
        dict(t="To'g'ridan-to'g'ri portallar", short="Portallar", min=30, kind="🧭 Portallar", ic="books",
             hook="Germaniya, Italiya, Xitoy va ko'p Osiyo universitetlarida yagona platforma yo'q. Har portalning o'z hisob qaydnomasi, formati va muddati bor.",
             body=f"""<div class="tbl"><table><thead><tr><th>Portal</th><th>Qayerda</th><th>E'tibor bering</th></tr></thead><tbody>
<tr><td>uni-assist</td><td>Germaniyaning ko'p universitetlari</td><td>Xorijiy hujjatlarni tekshiradi va baholaydi; to'lovli; ba'zi universitetlar o'z portalidan foydalanadi</td></tr>
<tr><td>Universitaly</td><td>Italiya</td><td>Viza uchun oldindan ro'yxatdan o'tish ([[pre-enrolment]]); universitetga ariza ko'pincha uning o'z portalida alohida</td></tr>
<tr><td>CSC portali va universitet portali</td><td>Xitoy</td><td>Stipendiya va universitet arizasi ikki joyda bo'lishi mumkin (M11, M14)</td></tr>
<tr><td>Universitet portali</td><td>Koreya, Yaponiya, Turkiya, Vengriya, Singapur va boshqalar</td><td>Har birida alohida hisob va hujjatlar formati</td></tr>
</tbody></table></div>
<h4>Portal bilan ishlash qoidalari</h4>
<ul><li>Har portal uchun login, parol va email'ni xavfsiz joyda saqlang (parolni boshqa odamga bermang).</li><li>Hisob ochilgan email'ni har kuni tekshiring; spam papkasini ham.</li><li>Yo'riqnomani to'liq o'qing: fayl formati (PDF), hajm, nom, tasdiq turi.</li></ul>
<div class="srcs">Manba: {UNIASSIST}; {UNIVERSITALY}; {CAMPUSCHINA}. {HOL}.</div>""",
             take="To'g'ridan-to'g'ri portallarda har universitetning o'z qoidasi. uni-assist hujjatlarni tekshiradi, Universitaly viza bosqichi, Xitoyda ikki portal bo'lishi mumkin.",
             task="<ul><li>Roʻyxatingizdagi har portal uchun: hisob ochilganmi, email, fayl talablari.</li><li>Eng murakkab portalning yo'riqnomasidan 5 ta talabni yozing.</li></ul>",
             ph="uni-assist: hisob ✓, email ..., talablar: ..."),
        dict(t="Amaliy topshirish", short="Topshirish", min=25, kind="🛠 Topshirish", ic="memo",
             hook="Arizani topshirish tugmasini bosish oxirgi qadam emas. Tasdiq xati, to'lov kvitansiyasi va hujjatlar holatini kuzatish arizaning to'liq yetib borishini ta'minlaydi.",
             body="""<h4>Fayllar</h4>
<ul><li><b>Format</b>: odatda PDF; skaner aniq, rangli, sahifalar to'g'ri tartibda.</li><li><b>Nom</b>: \"Familiya_Ism_Hujjat.pdf\" (masalan, Karimov_Aziz_Transcript.pdf). Bo'sh joy va o'zbekcha maxsus belgisiz.</li><li><b>Hajm</b>: portal chegarasidan oshmasin; kerak bo'lsa siqing, lekin o'qilishini tekshiring.</li><li><b>Tarjima</b>: asl hujjat va tarjima bitta faylda yoki alohida, yo'riqnomaga qarab.</li></ul>
<h4>Topshirgandan keyin</h4>
<ol><li><b>Tasdiq xati</b>: email va portaldagi tasdiqni PDF qilib saqlang.</li><li><b>To'lov kvitansiyasi</b>: saqlang.</li><li><b>Hujjatlar holati</b>: 3–7 kun ichida portal yoki universitet portalida hujjatlar \"qabul qilindi\" bo'lishi kerak. Yetishmagan hujjat ko'rinsa, darhol harakat qiling.</li><li><b>Universitet portali</b>: AQShda ko'p universitetlar topshirilgandan keyin alohida \"applicant portal\" ochadi; unga kiring.</li></ol>
<div class="box warn">Muddatning oxirgi kuniga qoldirmang: platformalar yuklanadi, to'lov o'tmasligi mumkin. Muddatdan kamida 3–5 kun oldin topshiring.</div>""",
             take="PDF, aniq nom, hajm chegarasi. Topshirgach tasdiq va kvitansiyani saqlang, hujjatlar holatini va universitet portalini kuzating.",
             task="<ul><li>Bitta arizani 40 bandli ro'yxat bo'yicha tekshirib topshiring.</li><li>Tasdiq sanasi va hujjatlar holatini yozing.</li></ul>",
             ph="Topshirildi: ... (sana). Tasdiq: saqlandi. Holat: ..."),
        dict(t="Topshirish oldi tekshiruv", short="40 band", min=20, kind="✅ Nazorat", ic="shield",
             hook="Uchuvchilar har parvozdan oldin nazorat ro'yxatini o'qiydi, tajribasi qancha bo'lsa ham. Ariza ham shunday: charchagan ko'z xatoni ko'rmaydi, ro'yxat ko'radi.",
             body="""<h4>Ro'yxat qanday ishlaydi</h4>
<p>Pastdagi nazorat bo'limida 40 band bor. Har arizadan oldin ularni ketma-ket tekshiring. Bir band \"yo'q\" bo'lsa, topshirmang: avval tuzating.</p>
<h4>Bloklar</h4>
<ol><li><b>Shaxsiy ma'lumot</b> (1–8): ism, sana, pasport, aloqa.</li><li><b>Ta'lim va testlar</b> (9–16): baholar, shkala, test natijalari va yuborilishi.</li><li><b>Yozma hujjatlar</b> (17–26): insho, qo'shimcha insholar, chegara, universitet nomi.</li><li><b>Tavsiyalar</b> (27–31).</li><li><b>Fayllar va to'lov</b> (32–36).</li><li><b>Topshirishdan keyin</b> (37–40).</li></ol>
<div class="box info">Ro'yxatni ikkinchi odam bilan birga o'qing: biri o'qiydi, ikkinchisi ekranda tekshiradi.</div>""",
             take="40 bandli nazorat ro'yxatini har ariza oldidan ketma-ket o'qing; bitta \"yo'q\" ham topshirishni to'xtatadi.",
             task="<ul><li>Pastdagi 40 bandni bitta haqiqiy arizangiz bo'yicha tekshiring.</li><li>Topilgan xatolarni va ularni qanday tuzatganingizni yozing.</li></ul>",
             ph="Topilgan xatolar: 1) ... → tuzatildi 2) ..."),
    ],
    tool=dict(id="ariza", short="Ariza", h2="Topshirilgan ariza va kuzatuv", sub="Har topshirilgan ariza: platforma, sana, tasdiq, hujjatlar holati.",
              h3="Arizalar jurnali", tag="4 maydon", ic="scroll", btn="Jurnalni saqlash", badge="Topshiruvchi", min=3,
              fields=[dict(k="topsh", label="Topshirilgan arizalar", hint="universitet · platforma · sana · tasdiq raqami/fayli", type="area", ph="... · Common App · ... · saqlandi"),
                      dict(k="holat", label="Hujjatlar holati", type="area", ph="... — transkript qabul qilindi, tavsiya kutilmoqda"),
                      dict(k="portal", label="Universitet portallari va loginlar qayerda saqlanadi", hint="parolni yozmang", ph="Parol menejerida / daftarda"),
                      dict(k="xato", label="Nazorat ro'yxatida topilgan xatolar", type="area", ph="...")]),
    check=dict(h2="40 bandli topshirish oldi nazorat ro'yxati", sub="Har ariza oldidan. Bitta \"yo'q\" ham topshirishni to'xtatadi.", h3="40 band",
               items=["Ism pasport bilan harfma-harf bir xil.", "Tug'ilgan sana to'g'ri formatda (kun/oy/yil yoki oy/kun/yil).", "Fuqarolik va pasport raqami to'g'ri.",
                      "Email faol va har kuni tekshiriladi.", "Telefon xalqaro formatda (+998 ...).", "Manzil to'g'ri, transliteratsiya bir xil.",
                      "Ota-ona ma'lumoti forma talabiga mos.", "Favqulodda aloqa kiritilgan.",
                      "Maktab nomi va manzili to'g'ri.", "Baholar asl shkalada.", "Shkala izohi berilgan.", "Fanlar ro'yxati to'liq.",
                      "Test natijalari to'g'ri kiritilgan.", "Rasmiy test natijalari yuborilgan (kerak bo'lsa).", "Til sertifikati amalda.", "Test siyosatiga mos qaror qabul qilingan.",
                      "Asosiy insho yakuniy versiyada.", "Insho chegarasi platformada tekshirilgan.", "Qo'shimcha insholar har universitet savoliga javob beradi.", "Boshqa universitet nomi qolib ketmagan.",
                      "Faoliyatlar ro'yxati to'liq va chegaraga mos.", "Additional Information qisqa va kontekst haqida.", "Motivatsion xat dastur nomi bilan mos.", "CV oxirgi versiyada.",
                      "Matn meniki; AI va boshqa yordam qoidalarga mos.", "Imlo va grammatika tekshirilgan.",
                      "Tavsiya beruvchilar email manzili to'g'ri.", "Tavsiya beruvchilar taklifni qabul qilgan.", "Maslahatchi maktab hujjatlarini yuklagan yoki rejalashtirgan.", "Tavsiya tarjimasi (kerak bo'lsa) tayyor.", "Tavsiya beruvchilarga muddat eslatilgan.",
                      "Fayllar PDF, aniq va o'qiladi.", "Fayl nomlari aniq va qoidaga mos.", "Fayl hajmi chegarada.", "Ariza to'lovi to'langan yoki ozod qilish tasdiqlangan.", "Ko'rib chiqish sahifasi PDF qilib saqlangan.",
                      "Tasdiq xati saqlangan.", "To'lov kvitansiyasi saqlangan.", "Universitet portaliga kirilgan.", "Nazorat jadvalida holat yangilangan."]),
    art_title="Arizalar jurnali", art_short="Jurnal",
    art=[("Common App", ["a1"]), ("UCAS", ["a2"]), ("To'g'ridan-to'g'ri portallar", ["a3"]), ("Topshirilgan arizalar", ["topsh", "a4"]),
         ("Hujjatlar holati", ["holat"]), ("Portallar", ["portal"]), ("Topilgan va tuzatilgan xatolar", ["xato", "a5"])],
    tip="Topshirish tugmasini bosishdan oldin bir kecha uxlang. Ertalab ko'rib chiqish sahifasini yana bir marta o'qing.",
    sources=f"{CA}; {CA_FEE}; {UCAS}; {UCAS_INT}; {UNIASSIST}; {UNIVERSITALY}; {CAMPUSCHINA}. {STD}",
)
