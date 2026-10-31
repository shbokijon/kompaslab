from common import LEEDS, UKRI_STUD, UKRI_SOE, HOL, STD

MOD = dict(
    title="Ariza, intervyu va qaror",
    desc="PhD Lab M7: topshirishdan oldingi sifat nazorati, tavsiya beruvchi va portal kuzatuvi, ilmiy intervyu, taqdimot va qiyin savollar, taklif, kutish ro'yxati va rad javobi, yakuniy qaror. Natija: topshirilgan arizalar reyestri, intervyu savollari banki va qaror jadvali.",
    lead="Portal, tavsiya beruvchilar, muddatlar va ilmiy suhbatni nazorat ostida olib borasiz, keyin takliflarni dalil bilan solishtirib qaror qilasiz.",
    hero="calendar", weeks="2–4", next="M8. Qabuldan keyingi tayyorgarlik va birinchi 90 kun", next_href="phd-lab-m8.html",
    goals=[("calendar", "Arizalar reyestri", "portal tasdig'i, holat, muddat"),
           ("miya", "Intervyu savollari banki", "10 savol, dalil bilan javob rejasi"),
           ("chart", "Qaror jadvali", "taklif shartlari va murosalar")],
    warn=f"PhD intervyusi har universitetda turlicha: ba'zilarida ilmiy taqdimot, ba'zilarida texnik suhbat yoki faqat rahbar bilan uchrashuv. Portal va dastur qoidasi ustun. Kompas Lab qabul natijasiga ta'sir qilmaydi. Faktlar {HOL}.",
    lessons=[
        dict(t="Topshirishdan oldingi sifat nazorati", short="Nazorat", min=25, kind="✅ Tekshiruv", ic="shield",
             hook="Yaxshi hujjatlar to'plami noto'g'ri portal yoki noto'g'ri fayl sabab kechikishi mumkin. Topshirishdan oldin bir ro'yxat bilan hammasini tekshiring.",
             body=f"""<h4>Ro'yxatga kiradi</h4>
<ul><li>Dastur yo'riqnomasi va yuklanadigan fayl turlari</li><li>Tavsiya so'rovlari</li><li>Ariza to'lovi (bo'lsa)</li><li>Aloqa ma'lumotlari</li><li>Muddat: sana, soat, vaqt mintaqasi</li><li>Deklaratsiya va yakuniy \"topshirish\" tugmasi</li></ul>
<p>Portaldagi \"qoralama saqlandi\" va \"topshirildi\" holatlari farqli. Tasdiq xati va ariza raqamini saqlang.</p>
<div class="box info">Ariza yuborilgan, lekin tavsiya portalida tavsiya beruvchi hali \"kutilmoqda\" holatida. Muddatga qadar nima majburiy ekanini qabul bo'limi yo'riqnomasi belgilaydi.</div>
<div class="box warn">Ekran rasmi borligi ariza qabul qilinganini anglatmasligi mumkin: portal holatini tekshiring.</div>
<div class="srcs">Manba: {LEEDS}. {HOL}.</div>""",
             take="Bitta nazorat ro'yxati, fayllarni ochib tekshirish, \"topshirildi\" holati va tasdiq xati saqlangan.",
             quiz=[("Teskari kalendar rasmiy muddat va uning vaqt mintaqasidan boshlanadi.", "t", "To'g'ri: ichki muddatlar shundan orqaga hisoblanadi."),
                   ("Portalda qoralama saqlanishi ariza topshirilganini bildiradi.", "n", "Noto'g'ri: rasmiy \"topshirildi\" tasdig'i kerak."),
                   ("Intervyuda tekshirilmagan katta va'da berish yaxshi taassurot qoldiradi.", "n", "Noto'g'ri: metod, xavf, hissa va shaxsiy dalil bilan javob bering."),
                   ("Takliflarni rahbar, moliya, shartlar, resurs va xavf bo'yicha solishtirish kerak.", "t", "To'g'ri.")],
             task="<ul><li>12 bandlik nazoratdan o'ting.</li><li>Fayl nomlari va PDF larni ochib ko'ring.</li><li>Topshirish tasdig'ini saqlang.</li></ul>",
             ph="A: 12/12 tekshirildi; topshirildi ... (ariza raqami maxfiy joyda); B: ..."),
        dict(t="Tavsiya beruvchi va portal kuzatuvi", short="Portal", min=20, kind="🔔 Kuzatuv", ic="bell",
             hook="Tavsiya jarayonini hurmat bilan kuzatish mumkin. Bitta xushmuomala eslatma va qabul bo'limiga aniq savol muammoni ko'pincha hal qiladi.",
             body="""<ul><li>Taklif xati tavsiya beruvchiga yetib borganini, muddatni va spam papkasini tekshiring.</li><li>Portal holatini kuzating.</li><li>Kerak bo'lsa, qabul bo'limidan muqobil tavsiya beruvchi tartibini so'rang.</li></ul>
<div class="box info">Tavsiya beruvchi \"yubordim\" desa-yu, portal \"qabul qilindi\" ko'rsatmasa, qabul bo'limidan professional tarzda aniqlik so'raladi.</div>
<div class="box warn">Tavsiya beruvchining maxfiy xatiga aralashmang va uni tahrir qilishni so'ramang.</div>""",
             take="Har tavsiya uchun holat: taklif yuborildi → yuklandi → qabul qilindi. Bitta eslatma, keyin qabul bo'limi.",
             task="<ul><li>Har tavsiya beruvchi holatini yozing.</li><li>Bitta xushmuomala eslatma rejasini tuzing.</li><li>Muqobil yo'lni tekshiring.</li></ul>",
             ph="1) ... — holat: kutilmoqda; eslatma: ...; muqobil: ..."),
        dict(t="Ilmiy intervyu", short="Intervyu", min=35, kind="🗣️ Mashq", ic="miya",
             hook="PhD intervyusida fakt yodlashdan ko'ra savolingizni ilmiy himoya qila olish tekshiriladi. \"Hali bilmayman, lekin shunday tekshirgan bo'lardim\" degan javob to'qima aniqlikdan kuchliroq.",
             body="""<h4>Tayyorlang</h4>
<ul><li>90 soniyalik tadqiqot bayoni</li><li>Bo'shliqni asoslash</li><li>Metod tanlovi va muqobillar</li><li>Muvaffaqiyatsizlik holatlari</li><li>Vaqt rejasi</li><li>Moslik va moliya bo'yicha savollar</li></ul>
<div class="box info"><b>Kompas tuzgan namuna savoli:</b> <span lang=\"en\">\"Your method fails on noisy data. What would you do?\"</span> Kuchli javob tuzilmasi: shovqin modeli, asosiy taqqoslash, sezgirlik tahlili, noaniqlik, zaxira usul va to'xtash mezoni.</div>
<div class="box warn">Har savolga \"100% ishonch\" bilan javob berish ilmiy noaniqlikni tan olmaslik demak.</div>""",
             take="90 soniyalik bayon, bo'shliq, metod, muqobil, xavf, reja. Noaniqlikni tan oling va qanday tekshirishingizni ayting.",
             task="<ul><li>10 savollik bank tuzing.</li><li>2 ta mashq intervyusini yozib oling va baholang.</li><li>3 ta zaif metodik joyni tuzating.</li></ul>",
             ph="Savol 1: ... — javob rejasi: ...; yozuv bahosi: .../8"),
        dict(t="Taqdimot va qiyin savollar", short="Taqdimot", min=30, kind="🎤 Taqdimot", ic="scroll",
             hook="Ba'zi intervyularda ilmiy taqdimot yoki oldingi dissertatsiyangizni muhokama qilish so'raladi. Slaydda o'qiladigan matn emas, fikrni ko'rsatadigan sxema bo'lsin.",
             body="""<ul><li>5–7 slayd: muammo, dalil, metod, hissa, cheklov, moslik.</li><li>Qiyin savolda avval savolni aniqlashtiring, keyin mavjud dalil chegarasini ayting.</li><li>\"Nega aynan shu rahbar?\" savoliga reyting emas, 2 ta haqiqiy ish va bitta kelajakdagi moslik bilan javob bering.</li></ul>
<div class="box warn">Natijani kafolatlash va boshqa laboratoriyalarni yomonlash professional emas.</div>""",
             take="5–7 slayd, har biri bitta fikr. Qiyin savol: aniqlashtirish → dalil chegarasi → keyingi qadam.",
             task="<ul><li>5 slaydlik reja yozing.</li><li>5 ta qarshi savolga javobni mashq qiling.</li><li>Tushunarsiz joylarni qayta chizing.</li></ul>",
             ph="Slayd 1: muammo ... Qarshi savol 1: ... — javob: ..."),
        dict(t="Taklif, kutish ro'yxati va rad javobi", short="Natija", min=25, kind="📬 Natija", ic="memo",
             hook="Qabul javobi har doim oddiy \"ha\" yoki \"yo'q\" bo'lmaydi. Shartli taklif, kutish ro'yxati va alohida moliya qarorini ajrata olish kerak.",
             body=f"""<ul><li>Shartli taklif va uning shartlari</li><li>Moliyalashtirish qarori (alohida kelishi mumkin)</li><li>Zaxira yoki kutish ro'yxati</li><li>Javob berish muddati</li></ul>
<p>Rad javobidan o'rganish jurnalini yozing, lekin fikr-mulohazani me'yorida so'rang. Boshqa grantni kutayotganda depozit yoki taklifni qabul qilish majburiyati qachon kuchga kirishini tekshiring.</p>
<div class="box info">A taklifga javob muddati 10 kun, B moliyalashtirish hali noaniq. Muddatni uzaytirish mumkinmi, faqat tashkilot qoidasi va yozma javob bilan aniqlanadi.</div>
<div class="box warn">\"Professor ha dedi\" degani shartsiz qabul emas.</div>
<div class="srcs">Manba: {UKRI_STUD}. {HOL}.</div>""",
             take="Har taklif uchun shartlar jadvali va muddatlar. Rad javobi: sabablar tasnifi va 30 kunlik reja.",
             task="<ul><li>Har taklif uchun shartlar jadvalini tuzing.</li><li>Muddatlarni yozing.</li><li>Rad javobi uchun 30 kunlik reja tuzing.</li></ul>",
             ph="A: shartlar ...; javob muddati ...; rad: sabab (moslik/moliya/raqobat/hujjat) → 30 kun: ..."),
        dict(t="Yakuniy qaror", short="Qaror", min=25, kind="⚖️ Qaror", ic="seedling",
             hook="Qabul qarorini nom emas, ilmiy moslik, moliya va yashash sharoiti birgalikda hal qiladi. Ikki yildan keyin ham bu qarorni asoslay olishingiz kerak.",
             body=f"""<ul><li>Ballik jadval faqat murosalarni ko'rsatadi, qarorni siz qabul qilasiz.</li><li>Qaytarib bo'lmaydigan xarajatlardan oldin yozma moliya, qabul, yashash rejasi va oila ehtiyojlarini tasdiqlang.</li><li>Qaror qilgandan keyin rad etgan takliflaringizga o'z vaqtida javob bering.</li></ul>
<p>Rahbarlik va o'qitish bo'yicha kutilmalarni UKRI bayonoti bilan solishtiring: bu sizning huquq va majburiyatlaringizni tushunishga yordam beradi.</p>
<div class="box info">\"Eng yuqori reyting\" o'rniga \"bu rahbarda mos ma'lumot, to'liq moliya va qo'llab-quvvatlovchi jamoa bor\" asosli qaror bo'lishi mumkin.</div>
<div class="box warn">Noaniqlikni yashirib, umumiy ballni faktga aylantirmang.</div>
<div class="srcs">Manba: {UKRI_SOE}.</div>""",
             take="4 mezonli qaror xati: ilmiy moslik, moliya, rahbarlik, hayot sharoiti. Qolgan xavflar ochiq yozilgan.",
             task="<ul><li>4 mezonli qaror xatini yozing.</li><li>Hal bo'lmagan xavflarni belgilang.</li><li>Qabul, kechiktirish yoki rad etish qadamlarini rejalang.</li></ul>",
             ph="Qaror: ... Mezonlar: ... Ochiq xavflar: ... Keyingi qadamlar: ..."),
    ],
    tool=dict(id="reyestr", short="Reyestr", h2="Arizalar reyestri", sub="Portal, muddat, tavsiya va qarorni bir joyda saqlang.",
              h3="Ariza kartasi", tag="5 maydon", ic="calendar", btn="Kartani saqlash", badge="Topshiruvchi", min=4,
              fields=[dict(k="dastur", label="Universitet yoki PhD o'rni", ph="..."),
                      dict(k="muddat", label="Rasmiy muddat", type="date"),
                      dict(k="zona", label="Muddat vaqt mintaqasi", ph="Masalan, Europe/London"),
                      dict(k="tavsiya", label="Tavsiya beruvchilar va tasdiqlar", type="area", ph="Kim, qachon, holat"),
                      dict(k="topshirish", label="Topshirish tasdig'i va intervyu rejasi", type="area", ph="Tasdiq olingan sana (raqamsiz), keyingi qadam")]),
    check=dict(h2="M7 nazorati", sub="Reyestrni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har ariza portal tasdig'i va holati bilan yozilgan.", "Fayl nomlari va versiyalar tekshirilgan.",
                      "Tavsiyalar holati kuzatilmoqda.", "Intervyu savollari dalil bilan tayyorlangan.",
                      "Taqdimot 5–7 slaydda tayyor.", "Taklif moliya va shartlar bo'yicha tekshirilgan.",
                      "Rad javobi uchun B reja yozilgan.", "Rad etilgan takliflarga javob berish rejalangan."]),
    art_title="Topshirilgan arizalar reyestri, intervyu banki va qaror jadvali", art_short="Reyestr",
    art=[("Sifat nazorati", ["a1"]), ("Ariza kartasi", ["dastur", "muddat", "zona"]), ("Tavsiyalar", ["tavsiya", "a2"]), ("Intervyu banki", ["a3"]),
         ("Taqdimot", ["a4"]), ("Takliflar", ["topshirish", "a5"]), ("Qaror", ["a6"])],
    tip="Intervyuda eng kuchli dalil izchillik: savolingiz, metodingiz va nega aynan shu guruh ekani bir-biriga mos bo'lsin.",
    sources=f"{LEEDS}; {UKRI_STUD}; {UKRI_SOE}. {STD}",
)
