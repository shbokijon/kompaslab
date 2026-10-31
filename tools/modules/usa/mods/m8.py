from common import DOS_VISA, SEVIS, SITS_SEARCH, EMB_VISA, EMB_DOCS, DS160, MIT_VET, GMU, HARVARD_212E, BROWN_TB, SJSU, HOL, STD

MOD = dict(
    title="Viza, maqom va ishlash huquqi",
    desc="USA Lab M8: F-1 va J-1 farqi, I-20 va DS-2019, SEVIS to'lovi, Toshkentda viza arizasi bosqichlari, onlayn mavjudlik tekshiruvi, maqomni saqlash, F-1 da ishlash (kampus, CPT, OPT, STEM OPT) va siyosat o'zgarishini kuzatish. Natija: viza va maqom nazorat ro'yxati.",
    lead="Qabul va moliya hal bo'lgach, oxirgi to'siq viza. Bu modulda AQSh vizasining Toshkentdagi tartibini, AQShga kelgandan keyin maqomni saqlash qoidalarini va o'qish davrida qayerda, qancha ishlash mumkinligini o'rganasiz.",
    hero="shield", weeks="1–2", next="", next_href="",
    goals=[("shield", "Viza va maqom nazorat ro'yxati", "hujjatlar, sanalar, majburiyatlar"),
           ("calendar", "Viza kalendari", "I-20 dan joʻnashgacha"),
           ("bell", "Siyosat kuzatuv jadvali", "rasmiy manbalar va oylik tekshiruv")],
    warn=f"Kompas Lab viza bo'yicha yuridik maslahat bermaydi va viza natijasiga ta'sir qilmaydi: qarorni konsul qabul qiladi. Mamlakatlararo umumiy viza va jo'nash bosqichlari Bachelor Lab M16 va Master Lab M8 da; bu modul faqat AQSh tartibi. Qoidalar {HOL}; rasmiy sahifadan qayta tekshiring.",
    lessons=[
        dict(t="F-1 va J-1: qaysi viza, qaysi hujjat", short="F-1 / J-1", min=25, kind="🧭 Xarita", ic="usa",
             hook="Viza turi qabul qilingan dasturingizdan kelib chiqadi, siz tanlamaysiz. Lekin har birining qoidasi kelajak rejangizga boshqacha ta'sir qiladi.",
             body=f"""<div class="tbl"><table><thead><tr><th></th><th>F-1</th><th>J-1</th></tr></thead><tbody>
<tr><td>Kimga</td><td>Universitet yoki kollejda daraja uchun o'qiydigan talaba</td><td>Almashinuv dasturi qatnashchisi (UGRAD, Fulbright va boshqalar)</td></tr>
<tr><td>Hujjat</td><td>Form I-20 (SEVP tasdiqlagan muassasa beradi)</td><td>DS-2019 (dastur homiysi beradi)</td></tr>
<tr><td>2 yillik talab</td><td>Yo'q</td><td>Hukumat moliyalashtirgan bo'lsa, 212(e) qo'llanadi (M5–M6)</td></tr>
</tbody></table></div>
<h4>Ketma-ketlik (F-1)</h4>
<ol><li>SEVP tasdiqlagan muassasaga qabul (M1 dagi tekshiruv).</li><li>Muassasa sizni SEVIS ga kiritadi va Form I-20 beradi (pul dalili, M2).</li><li>SEVIS I-901 to'lovi (ICE sahifasi).</li><li>DS-160 va viza suhbati (8.2).</li></ol>
<h4>Sanalar</h4>
<p>Davlat departamenti: yangi talabaga viza o'qish boshlanishidan 365 kun oldingacha berilishi mumkin, lekin AQShga boshlanishdan 30 kundan oldin kirish mumkin emas. Viza AQShga kirishni kafolatlamaydi: qarorni chegaradagi CBP xodimi qabul qiladi.</p>
<div class="srcs">Manba: {DOS_VISA}; {SEVIS}; {SITS_SEARCH}; {HARVARD_212E}. {HOL}.</div>""",
             take="F-1: daraja uchun, I-20 bilan. J-1: almashinuv uchun, DS-2019 bilan, ba'zan 2 yillik talab. Viza 365 kun oldin berilishi mumkin, kirish 30 kun oldin.",
             quiz=[("F-1 uchun hujjat DS-2019.", "n", "Noto'g'ri: F-1 uchun I-20, J-1 uchun DS-2019."),
                   ("Yangi talaba AQShga o'qish boshlanishidan 30 kundan oldin kira olmaydi.", "t", "To'g'ri: Davlat departamenti."),
                   ("Viza AQShga kirishni kafolatlaydi.", "n", "Noto'g'ri: chegarada CBP qaror qiladi."),
                   ("I-20 ni faqat SEVP tasdiqlagan muassasa beradi.", "t", "To'g'ri.")],
             task="<ul><li>Sizning yo'lingizda qaysi viza va qaysi hujjat bo'ladi?</li><li>O'qish boshlanish sanasidan 365 va 30 kunlik sanalarni hisoblang.</li></ul>",
             ph="Viza: F-1, hujjat: I-20. Boshlanish: ... → viza ... dan, kirish ... dan erta emas"),
        dict(t="Toshkentda viza arizasi", short="Ariza", min=30, kind="📑 Bosqichlar", ic="scroll",
             hook="Viza suhbati bir necha daqiqa davom etadi, lekin unga tayyorgarlik oylar oldin boshlanadi. Elchixona qaysi hujjat foydali, qaysi biri foydasiz ekanini ochiq yozgan.",
             body=f"""<h4>Elchixona sahifasidagi bosqichlar</h4>
<ol><li>Viza turini aniqlang (F yoki J).</li><li>DS-160 ni to'ldiring: har bir arizachi, yoshidan qat'i nazar, alohida forma.</li><li>Viza yig'imini onlayn yoki elchixona ko'rsatgan bank orqali to'lang; to'lov tasdig'i 2 ish kunigacha olishi mumkin.</li><li>Suhbatga yoziling (elchixona ko'rsatgan onlayn tizim).</li><li>Tayyorlaning: talaba va almashinuv qatnashchilari uchun hujjatlar ro'yxati; O'zbekiston bilan iqtisodiy va ijtimoiy bog'liqlik hujjatlari.</li><li>Suhbat: natija odatda darhol aytiladi; pasport tayyor bo'lganda email keladi.</li></ol>
<div class="box info">Elchixona sahifasida aytilishicha, mehmonxona bandi, aviabilet va bank ko'chirmalari odatda foydali emas: konsul o'zi kerakli deb bilgan hujjatnigina ko'radi. I-20 dagi pul dalili esa universitetga oldindan topshirilgan (M2).</div>
<h4>Onlayn mavjudlik tekshiruvi</h4>
<p>2025-yil iyunida Davlat departamenti F, M va J arizachilarini onlayn mavjudlikni ham o'z ichiga olgan kengaytirilgan tekshiruvdan o'tkazishini e'lon qildi; arizachilarga barcha ijtimoiy tarmoq profillarini \"public\" holatga o'tkazish ko'rsatmasi beriladi (MIT xalqaro ofisi xabari).</p>
<div class="box warn">Suhbatda faqat haqiqatni gapiring. Davlat departamenti: muhim faktni noto'g'ri ko'rsatish doimiy rad javobiga olib kelishi mumkin.</div>
<div class="srcs">Manba: {EMB_VISA}; {EMB_DOCS}; {DS160}; {DOS_VISA}; {MIT_VET}. {HOL}.</div>""",
             take="Toshkentda: DS-160, yig'im, navbat, hujjatlar, suhbat. Konsul faqat foydali deb bilgan hujjatni ko'radi. Ijtimoiy tarmoqlar tekshiriladi; faqat haqiqat.",
             task="<ul><li>6 bosqich uchun sana va mas'ulni yozing.</li><li>O'zbekiston bilan bog'liqligingizni ko'rsatadigan 3 haqiqiy dalilni yozing (o'qish rejasi, oila, ish va hokazo).</li></ul>",
             ph="DS-160: ... ; yig'im: ...; navbat: ...; dalillar: 1) ... 2) ... 3) ..."),
        dict(t="Maqomni saqlash", short="Maqom", min=25, kind="✅ Qoidalar", ic="shield",
             hook="Viza AQShga kirish uchun; AQSh ichida esa sizni maqom (F-1 yoki J-1 status) qoidalari himoya qiladi. Maqomni yo'qotish o'qishni ham, keyingi vizani ham xavf ostiga qo'yadi.",
             body=f"""<h4>Xalqaro bo'limda tekshiriladigan bandlar</h4>
<p>Quyidagi bandlar odatda maqom bilan bog'liq; aniq talab va muddatni universitetingiz xalqaro talabalar bo'limi sahifasidan oling.</p>
<div class="tbl"><table><thead><tr><th>Band</th><th>Kim bilan tekshiriladi</th></tr></thead><tbody>
<tr><td>To'liq o'quv yuklamasi (har semestr)</td><td>Universitetning xalqaro talabalar bo'limi (ISSS yoki OIS)</td></tr>
<tr><td>I-20 yoki DS-2019 muddati va ma'lumotlari to'g'ri</td><td>Shu bo'lim; o'zgarish bo'lsa oldindan</td></tr>
<tr><td>Ruxsatsiz ishlamaslik (8.4)</td><td>Ishga kirishdan oldin bo'limdan yozma tasdiq</td></tr>
<tr><td>Yashash manzili va dastur o'zgarishlari haqida xabar berish</td><td>Bo'lim ko'rsatgan muddatda</td></tr>
<tr><td>AQShdan chiqib qaytishdan oldin hujjatlarni tekshirish</td><td>Bo'lim</td></tr>
</tbody></table></div>
<p>Har universitetning xalqaro talabalar bo'limi o'z talablarini sahifasida yozadi: kelishingiz bilan shu sahifani o'qing va bo'lim xodimining (DSO yoki RO) aloqasini saqlang.</p>
<div class="box warn">Maqom qoidalari bo'yicha savolni do'stdan emas, universitetning xalqaro bo'limidan so'rang va javobni yozma oling.</div>
<div class="srcs">Manba: universitetingiz xalqaro talabalar bo'limi sahifasi; ish qoidalari: {GMU}. {HOL}.</div>""",
             take="Maqom: to'liq yuklama, hujjatlar to'g'ri, ruxsatsiz ish yo'q, o'zgarishlar haqida xabar. Har savol bo'yicha xalqaro talabalar bo'limiga yozma murojaat.",
             task="<ul><li>Qabul qilingan yoki ko'zlagan universitetingizning xalqaro talabalar bo'limi sahifasini toping.</li><li>Undagi maqom qoidalaridan 5 tasini yozing.</li></ul>",
             ph="... universiteti ISSS (havola): 1) ... 2) ... 3) ... 4) ... 5) ..."),
        dict(t="F-1 da ishlash huquqi", short="Ish", min=30, kind="💼 Qoidalar", ic="money",
             hook="\"AQShda o'qib ishlayman\" rejasi qaysi ish, qayerda va qachon ekaniga bog'liq. Noto'g'ri ish bir martaning o'zida maqomni yo'qotishga olib kelishi mumkin.",
             body=f"""<h4>George Mason universiteti tushuntirishi</h4>
<div class="tbl"><table><thead><tr><th>Tur</th><th>Qoida</th></tr></thead><tbody>
<tr><td>Kampusda ishlash</td><td>Kuz va bahor semestrlarida haftasiga 20 soatgacha; yozgi darslar davrida ham 20 soatdan oshirmaslik tavsiya etiladi; dastur tugagach to'xtatiladi</td></tr>
<tr><td>Kampusdan tashqari ish</td><td>Har doim yozma ruxsat kerak: xalqaro bo'lim (I-20 ning 2-sahifasiga yoziladi) yoki USCIS</td></tr>
<tr><td>CPT ([[Curricular Practical Training]])</td><td>O'quv rejasi bilan bog'liq amaliyot; alohida ruxsat bilan</td></tr>
<tr><td>OPT ([[Optional Practical Training]])</td><td>Har daraja uchun 12 oy; o'qish davomidagi OPT keyingisini qisqartiradi (har 2 oy uchun 1 oy)</td></tr>
<tr><td>STEM OPT</td><td>DHS tasdiqlagan STEM yo'nalishi bitiruvchisi uchun qo'shimcha 24 oy</td></tr>
</tbody></table></div>
<h4>Rejaga ta'siri</h4>
<ul><li>Kampusdagi ish o'qish to'lovini qoplamaydi: uni M2 dagi asosiy manba qilmang.</li><li>Sohangiz DHS ning STEM ro'yxatida bo'lsa, bitirgandan keyin amaliy tajriba muddati uzunroq bo'lishi mumkin; ro'yxatni rasmiy manbadan tekshiring.</li><li>J-1 qatnashchilari uchun ish qoidalari boshqacha: dastur homiysidan so'raladi.</li></ul>
<div class="srcs">Manba: {GMU}. {HOL}.</div>""",
             take="F-1: kampusda semestr davomida haftasiga 20 soatgacha; kampusdan tashqarida faqat yozma ruxsat bilan; OPT 12 oy, STEM OPT qo'shimcha 24 oy. J-1 da qoidalar boshqa.",
             task="<ul><li>Sohangiz STEM bo'lsa, OPT va STEM OPT bilan bitirgandan keyingi umumiy amaliy tajriba muddatini yozing.</li><li>Kampusdagi ishdan kutilgan oylik daromad M2 dagi narxning necha foizi?</li></ul>",
             ph="Soha: ... (STEM: ha/yo'q). OPT ... oy + STEM OPT ... oy. Kampus ishi: ... USD/oy = narxning ...%"),
        dict(t="Siyosat o'zgarishini kuzatish", short="Kuzatuv", min=20, kind="🔔 Kuzatuv", ic="bell",
             hook="AQShning viza siyosati tez o'zgaradi va har o'zgarish haqida ijtimoiy tarmoqlarda noto'g'ri talqinlar chiqadi. Faqat rasmiy manba va sana bilan ishlang.",
             body=f"""<h4>{HOL} holat</h4>
<p>Brown universiteti ISSS sahifasi (27.01.2026 yangilangan): 2026-yil 1-yanvardan amal qiluvchi prezident proklamatsiyalarida to'liq va qisman cheklangan mamlakatlar ro'yxati bor; qisman cheklangan mamlakatlar uchun F-1 va J-1 vizalari ham cheklangan. O'zbekiston ikkala ro'yxatda ham yo'q.</p>
<h4>Kuzatuv manbalari</h4>
<div class="tbl"><table><thead><tr><th>Manba</th><th>Nima uchun</th><th>Qanchalik tez-tez</th></tr></thead><tbody>
<tr><td>AQSh elchixonasi (Toshkent) viza sahifalari</td><td>Mahalliy tartib, navbat, yig'im</td><td>Oyiga bir marta; ariza davrida haftalik</td></tr>
<tr><td>Davlat departamenti talaba vizasi sahifasi</td><td>Umumiy qoidalar</td><td>Oyiga bir marta</td></tr>
<tr><td>Universitetingiz xalqaro bo'limi</td><td>O'zgarishning sizga ta'siri</td><td>Har yangilikda</td></tr>
</tbody></table></div>
<ol><li>Har o'zgarish uchun yozing: sana, manba, kimga tegishli, sizga ta'siri.</li><li>Ijtimoiy tarmoqdagi xabarni rasmiy sahifada topmaguningizcha qaror qilmang.</li></ol>
<div class="box info">Kompas Lab USA Lab sahifasida siyosat holatini sana bilan yangilaydi. Siyosat talaba vizasini yopsa, faol obunachilarga boshqa Labga o'tish taklif qilinadi.</div>
<div class="srcs">Manba: {BROWN_TB}; {EMB_VISA}; {DOS_VISA}. {HOL}.</div>""",
             take="Siyosatni faqat rasmiy manba va sana bilan kuzating: elchixona, Davlat departamenti, universitet xalqaro bo'limi. 31.10.2026 holatiga O'zbekiston proklamatsiya ro'yxatlarida yo'q.",
             task="<ul><li>Kuzatuv jadvalingizga 3 manba va eslatma sanasini qo'shing.</li><li>Bugungi holatni sana bilan yozing.</li></ul>",
             ph="31.10.2026: O'zbekiston proklamatsiya ro'yxatlarida yo'q (Brown ISSS). Eslatma: har oy ... kuni"),
    ],
    tool=dict(id="viza", short="Ro'yxat", h2="Viza va maqom nazorat ro'yxati", sub="Viza kalendari, hujjatlar va maqom qoidalari bir joyda.",
              h3="Nazorat ro'yxati", tag="6 maydon", ic="shield", btn="Ro'yxatni saqlash", badge="Viza tayyor", min=5,
              fields=[dict(k="tur", label="Viza turi va hujjat", type="select", opts=["F-1, I-20", "J-1, DS-2019", "Hali aniq emas"]),
                      dict(k="boshlanish", label="O'qish boshlanish sanasi", type="date"),
                      dict(k="kalendar", label="Viza kalendari", hint="I-20 → SEVIS → DS-160 → yig'im → suhbat → jo'nash", type="area", ph="I-20: ...; SEVIS: ...; DS-160: ...; suhbat: ...; jo'nash: ..."),
                      dict(k="hujjat", label="Suhbat hujjatlari", hint="elchixona ro'yxati bo'yicha", type="area", ph="Pasport, I-20, DS-160 tasdig'i, ..."),
                      dict(k="maqom", label="Maqom qoidalari va xalqaro bo'lim aloqasi", type="area", ph="..."),
                      dict(k="kuzatuv", label="Siyosat kuzatuv jadvali", type="area", ph="Manba — sana — holat — ta'siri")]),
    check=dict(h2="M8 nazorati", sub="Ro'yxatni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Viza turi va hujjati aniqlangan.", "365 va 30 kunlik sanalar hisoblangan.", "SEVIS to'lovi rejada bor.",
                      "Elchixonaning hujjatlar ro'yxati o'qilgan.", "Ijtimoiy tarmoq profillari ko'rsatmaga muvofiq tekshirilgan.",
                      "Maqom qoidalari universitet sahifasidan yozilgan.", "Ish qoidalari bilan rejadagi daromad mos.", "Siyosat kuzatuv eslatmasi qo'yilgan."]),
    art_title="Viza va maqom nazorat ro'yxati", art_short="Ro'yxat",
    art=[("Viza turi", ["tur", "a1"]), ("O'qish boshlanishi", ["boshlanish"]), ("Viza kalendari", ["kalendar", "a2"]), ("Suhbat hujjatlari", ["hujjat"]),
         ("Maqom qoidalari", ["maqom", "a3"]), ("Ishlash huquqi", ["a4"]), ("Siyosat kuzatuvi", ["kuzatuv", "a5"])],
    tip="Viza suhbatida eng kuchli dalil izchil haqiqat: o'qish rejangiz, moliyangiz va qaytish yoki keyingi rejangiz bir-biriga mos bo'lsin.",
    sources=f"{DOS_VISA}; {SEVIS}; {SITS_SEARCH}; {EMB_VISA}; {EMB_DOCS}; {DS160}; {MIT_VET}; {GMU}; {HARVARD_212E}; {BROWN_TB}. {STD}",
)
