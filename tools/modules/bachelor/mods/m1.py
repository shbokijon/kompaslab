from common import CA, CDS, UCAS, ANABIN, DAAD_ADM, QS, THE, USN, UNIPI, HOL, STD

MOD = dict(
    title="Qabul qanday qaror qabul qiladi",
    desc="Bachelor Lab M1: qabul komissiyasi ishi, yaxlit va ball asosidagi qabul, 11 yillik attestat xorijda, reyting tuzog'i, QS/THE/US News metodologiyasi. Natija: 3 universitet talablari jadvali.",
    lead="Ariza yozishdan oldin uni kim o'qishini va qaysi mantiq bilan qaror chiqarishini bilish kerak. Bu modulda qabulning ikki usulini ajratasiz, attestatingiz xorijda qanday baholanishini tekshirasiz va reytinglarni to'g'ri o'qishni o'rganasiz.",
    hero="telescope", weeks="1–2", next="M2 Universitet tanlash va roʻyxat tuzish", next_href="bachelor-lab-m2.html",
    goals=[("telescope", "Qabul usulini aniqlash", "har universitet uchun: yaxlit yoki ball asosidagi"),
           ("scroll", "3 universitet talablari jadvali", "rasmiy sahifadan, havola va sana bilan"),
           ("chart", "Reytingni o'qish ko'nikmasi", "umumiy va fan bo'yicha reyting farqi")],
    warn=f"Kirish talablari, testlar siyosati va reytinglar har yili yangilanadi. Bu moduldagi misollar {HOL}; o'z universitetingiz talabini uning rasmiy qabul sahifasidan tekshiring.",
    lessons=[
        dict(t="Qabul komissiyasi qanday ishlaydi", short="Komissiya", min=25, kind="🎯 Mini-test", ic="telescope",
             hook="Arizangizni universitetning qabul bo'limidagi odamlar o'qiydi, ko'pincha bir necha daqiqa ichida. Ular nimaga qarashini bilsangiz, hujjatlarni shu ko'z bilan tayyorlaysiz.",
             body="""<p>Har universitetda qabul boshqacha tashkil qilingan, lekin umumiy tuzilma o'xshash.</p>
<h4>Kim o'qiydi</h4>
<ul><li><b>Qabul xodimlari ([[admissions officers]])</b>: odatda mintaqa bo'yicha taqsimlanadi. Markaziy Osiyo arizalarini o'qiydigan xodim sizning maktab tizimingizni bilishi ham, bilmasligi ham mumkin.</li>
<li><b>Fakultet o'qituvchilari</b>: ayniqsa Yevropa va Osiyoda dastur talablari va akademik tayyorgarlikni ko'radi.</li>
<li><b>Komissiya ([[committee]])</b>: AQShning tanlovli kollejlarida chegaradagi arizalar guruhda muhokama qilinadi.</li></ul>
<h4>Nimani ko'radi</h4>
<div class="tbl"><table><thead><tr><th>Qism</th><th>Savol</th></tr></thead><tbody>
<tr><td>Akademik tayyorgarlik</td><td>Baholar, fanlar og'irligi, test natijalari: dasturda ulgurasizmi?</td></tr>
<tr><td>Kontekst</td><td>Maktabingizda qanday imkoniyat bor edi va siz undan qanday foydalandingiz?</td></tr>
<tr><td>Shaxsiy sifatlar</td><td>Insho, tavsiya xati, faoliyatlar: siz qanday odamsiz?</td></tr>
<tr><td>Moslik</td><td>Nega aynan shu dastur? Universitet sizga nima beradi, siz unga nima berasiz?</td></tr>
</tbody></table></div>
<h4>Qaror turlari</h4>
<p>Qabul ([[admit]]), shartli qabul ([[conditional offer]], masalan til testi yoki attestat sharti bilan), kutish ro'yxati ([[waitlist]]), rad ([[reject]]) va AQShda erta arizada keyinga qoldirish ([[defer]]). M15 da har biri bilan nima qilishni ko'rasiz.</p>
<div class="box info"><b>Asosiy fikr.</b> Komissiya sizni tanimaydi. U faqat hujjatlarda yozilganni ko'radi. Shuning uchun har hujjat aniq, tekshiriladigan va bir-biriga mos bo'lishi kerak.</div>""",
             take="Arizani mintaqa bo'yicha xodim yoki fakultet o'qiydi va to'rt savolga javob izlaydi: akademik tayyorgarlik, kontekst, shaxsiy sifatlar, moslik.",
             quiz=[("Hamma universitetlarda arizani faqat kompyuter dasturi baholaydi.", "n", "Noto'g'ri: arizani odamlar o'qiydi; ba'zi tizimlar ball hisoblashni avtomatlashtiradi, lekin qarorni qabul bo'limi chiqaradi."),
                   ("Shartli qabul odatda til testi yoki attestat kabi shart bajarilishini talab qiladi.", "t", "To'g'ri: shart bajarilmasa, qabul kuchini yo'qotadi."),
                   ("Komissiya sizning maktabingiz imkoniyatlarini ham hisobga olishi mumkin.", "t", "To'g'ri: AQShda kontekst baholashning bir qismi; maktab hisoboti ([[school profile]]) shu uchun kerak."),
                   ("Kutish ro'yxati rad javobi bilan bir xil.", "n", "Noto'g'ri: kutish ro'yxatidan joy bo'shasa qabul qilinishi mumkin, lekin kafolat yo'q.")],
             task="<ul><li>Tanlagan uchta universitetingizning qabul sahifasini oching.</li><li>Har biri arizani kim o'qishi va qaysi qismlarga qarashi haqida nima deyishini 2–3 jumlada yozing.</li></ul>",
             ph="1) ... universiteti: qabul bo'limi ..., qaraydi: ... 2) ..."),
        dict(t="Yaxlit va ball asosidagi qabul", short="Ikki mantiq", min=30, kind="🧭 Qabul usulini aniqlash", ic="compass",
             hook="Bir universitet uchun insho hal qiluvchi, boshqasi uni umuman so'ramaydi. Vaqtingizni qayerga sarflashni qabul mantig'i belgilaydi.",
             body=f"""<h4>Ikki mantiq</h4>
<div class="tbl"><table><thead><tr><th></th><th>Yaxlit ([[holistic]])</th><th>Ball asosidagi ([[numbers-based]])</th></tr></thead><tbody>
<tr><td>Qayerda ko'p</td><td>AQShning tanlovli kollejlari, ba'zi UK universitetlari (masalan Oksford, Kembrij intervyu bilan)</td><td>Germaniya, Italiya, Xitoy, Turkiya va ko'p Yevropa davlat universitetlari</td></tr>
<tr><td>Nima hal qiladi</td><td>Baholar + insho + tavsiya + faoliyatlar + kontekst birgalikda</td><td>Attestat bahosi, kirish testi, til sertifikati</td></tr>
<tr><td>Insho</td><td>Muhim</td><td>Ko'pincha yo'q yoki qisqa motivatsion xat</td></tr>
<tr><td>Vaqtingiz</td><td>Hikoya va hujjatlarga</td><td>Baho va testga</td></tr>
</tbody></table></div>
<p>Buyuk Britaniya o'rtada: asosan baho va bashorat qilingan natijalar ([[predicted grades]]) hal qiladi, shaxsiy bayonot va tavsiya qo'shimcha dalil.</p>
<h4>Universitet modelini qanday aniqlash</h4>
<ol><li><b>Rasmiy qabul sahifasi</b>: \"what we look for\", \"selection criteria\" bo'limi. Insho, intervyu, tavsiya so'raladimi?</li>
<li><b>AQShda Common Data Set (CDS)</b>: C7 bo'limida har omil (baholar, insho, tavsiya, faoliyat, intervyu) \"Very Important\" dan \"Not Considered\" gacha belgilangan. Universitet nomi + \"Common Data Set\" deb qidiring.</li>
<li><b>Yevropada</b>: dastur sahifasidagi \"admission requirements\" va kirish testi bor-yo'qligi.</li></ol>
<div class="box warn">CDS fayllari har yili chiqadi va kechikishi mumkin. Eng oxirgi yilni oling va yilini yozib qo'ying.</div>
<div class="srcs">Manba: {CDS}; universitetlarning rasmiy qabul sahifalari. {HOL}.</div>""",
             take="Yaxlit qabulda vaqtni hikoya va hujjatlarga, ball asosidagi qabulda baho va testga sarflang. Modelni rasmiy sahifa va AQShda Common Data Set aniqlaydi.",
             task="<ul><li>3 universitet uchun modelni aniqlang: yaxlit, ball asosidagi yoki aralash.</li><li>AQSh universiteti bo'lsa, CDS C7 dan 3 ta \"Very Important\" omilni yozing.</li></ul>",
             ph="... universiteti: yaxlit; CDS 2025–26 C7: Very Important — ..., ..., ..."),
        dict(t="Mamlakatlar bo'yicha kirish talablari", short="Attestat", min=35, kind="🗺 Talablar xaritasi", ic="scroll",
             hook="O'zbekiston maktabi 11 yil. Ko'p mamlakatlar 12 yillik ta'limni kutadi. Bu farq ariza strategiyasini butunlay o'zgartirishi mumkin.",
             body=f"""<p>Attestatingiz xorijda qanday tan olinishi har mamlakatda va ko'pincha har universitetda alohida hal qilinadi. Quyidagi jadval umumiy yo'nalish; aniq javobni faqat rasmiy manba beradi.</p>
<div class="tbl"><table><thead><tr><th>Mamlakat</th><th>Umumiy holat</th><th>Qayerdan tekshirish</th></tr></thead><tbody>
<tr><td>AQSh</td><td>Ko'pincha attestat bilan to'g'ridan-to'g'ri birinchi kursga ariza; qaror yaxlit</td><td>Universitet xalqaro qabul sahifasi</td></tr>
<tr><td>Buyuk Britaniya</td><td>Ko'p universitetlar 11 yillik attestatni yetarli deb hisoblamaydi va tayyorlov yilini ([[foundation year]]) yoki qo'shimcha malaka (A-level, IB yoki boshqa) so'raydi; ba'zilari yuqori baho bilan to'g'ridan-to'g'ri qabul qiladi</td><td>Universitetning \"country-specific requirements\" sahifasi (Uzbekistan)</td></tr>
<tr><td>Germaniya</td><td>Maktab attestati odatda to'g'ridan-to'g'ri kirishga yetmaydi: Studienkolleg (bir yillik tayyorlov) va kirish imtihoni ([[Feststellungsprüfung]]) yoki O'zbekistonda 1–2 yil universitet o'qishi talab qilinishi mumkin</td><td>{ANABIN}; {DAAD_ADM}; uni-assist</td></tr>
<tr><td>Italiya</td><td>Bakalavr uchun kamida 12 yillik maktab ta'limi talab qilinadi; 11 yillik attestat yetishmasa, universitet o'qishi bilan to'ldiriladi</td><td>{UNIPI}</td></tr>
<tr><td>Koreya, Xitoy, Turkiya</td><td>Odatda attestat bilan ariza, universitet o'z imtihoni yoki hujjatlar asosida tanlaydi</td><td>Universitet va stipendiya yo'riqnomasi</td></tr>
</tbody></table></div>
<h4>Akademik litsey va kollej</h4>
<p>Akademik litsey yoki kollejni bitirganlar hujjatida o'qish yillari boshqacha yozilishi mumkin. Universitetga attestat bilan birga baholar varaqasini va yillar sonini aniq ko'rsating.</p>
<div class="box warn"><b>Tekshirishsiz qaror qilmang.</b> Forumdagi \"Germaniyaga attestat bilan kirsa bo'ladi\" degan gap sizning holatingizga mos kelmasligi mumkin. Universitet xalqaro bo'limiga yozma savol yuboring va javobni saqlang.</div>
<div class="srcs">Manba: {ANABIN}; {DAAD_ADM}; {UNIPI}. {HOL}.</div>""",
             take="11 yillik attestat AQShda ko'pincha yetarli, UK, Germaniya va Italiyada ko'pincha qo'shimcha yil yoki malaka talab qiladi. Har universitet uchun rasmiy sahifadan tekshiring.",
             task="<ul><li>3 nishon mamlakat uchun attestatingiz bilan to'g'ridan-to'g'ri kirish mumkinmi yoki qo'shimcha yil kerakmi, rasmiy manbadan aniqlang.</li><li>Havola va tekshirilgan sanani yozing.</li></ul>",
             ph="Germaniya: anabin bo'yicha ... ; havola: ... ; sana: ..."),
        dict(t="Reytingga aldanmaslik", short="Reyting", min=20, kind="⚖️ Tahlil", ic="chart",
             hook="Reytingdagi 50-o'rin sizning fakultetingiz uchun 150-o'rin bo'lishi mumkin. Umumiy reyting butun universitetni o'lchaydi, sizning dasturingizni emas.",
             body="""<h4>Umumiy va fan bo'yicha reyting</h4>
<p>Umumiy reyting ([[overall ranking]]) universitetning hamma fakultetlarini, ilmiy maqolalar, obro' so'rovlari va xalqarolikni birga hisoblaydi. Fan bo'yicha reyting ([[subject ranking]]) aniq soha bo'yicha tuziladi. Muhandislik yoki informatikada o'qimoqchi bo'lsangiz, aynan shu sohadagi o'rinni qarang.</p>
<h4>Reyting nimani ko'rsatmaydi</h4>
<ul><li><b>Bakalavr ta'lim sifati</b>: ko'p ko'rsatkichlar tadqiqotga qaratilgan, bakalavr darsiga emas.</li>
<li><b>Guruh hajmi va o'qituvchi bilan aloqa</b>.</li>
<li><b>Xarajat va stipendiya</b>: reytingi yuqori universitet sizga moliyaviy jihatdan erishib bo'lmas bo'lishi mumkin.</li>
<li><b>Sizga moslik</b>: dastur tarkibi, laboratoriya, til, shahar.</li></ul>
<h4>Amaliy qoida</h4>
<p>Reytingdan faqat birinchi saralash uchun foydalaning. Keyin dastur sahifasini, o'quv rejasini ([[curriculum]]) va bitiruvchilar qayerga ketishini ko'ring.</p>
<div class="box info">Masalan, ba'zi texnika universitetlari umumiy reytingda o'rtada, lekin muhandislik bo'yicha yuqori. Kompas Lab'ning yondashuvi: mamlakat bo'yicha emas, soha bo'yicha kuchli joyni izlash.</div>""",
             take="Umumiy reyting butun universitetni, fan reytingi sizning sohangizni o'lchaydi. Reyting saralash uchun, qaror dastur tarkibi va moslik bo'yicha.",
             task="<ul><li>Sohangizni yozing (masalan: informatika).</li><li>3 universitetning umumiy va shu soha bo'yicha o'rnini solishtiring; farq katta bo'lganini belgilang.</li></ul>",
             ph="Soha: ... ; ... universiteti: umumiy ..., soha bo'yicha ..."),
        dict(t="QS, THE va US News'ni o'qish", short="Metodologiya", min=25, kind="📊 Solishtirish", ic="books",
             hook="Uchta mashhur reyting bir universitetni turli o'ringa qo'yadi. Sabab oddiy: ular turli narsalarni o'lchaydi.",
             body=f"""<p>Har reyting o'z metodologiyasini e'lon qiladi. Ularni o'qish reytingni to'g'ri ishlatishning yagona yo'li.</p>
<div class="tbl"><table><thead><tr><th>Reyting</th><th>Asosiy urg'u</th><th>E'tibor bering</th></tr></thead><tbody>
<tr><td>QS World University Rankings</td><td>Akademik va ish beruvchilar orasidagi obro' so'rovlari katta ulushga ega</td><td>Obro' so'rovi mashhur nomlarni yuqoriga tortadi</td></tr>
<tr><td>THE World University Rankings</td><td>O'qitish muhiti, tadqiqot, iqtiboslar, sanoat, xalqarolik</td><td>Tadqiqot va iqtibosga og'ir; bakalavr darsini bevosita o'lchamaydi</td></tr>
<tr><td>US News (Best Colleges, AQSh)</td><td>Bitiruv darajasi, ijtimoiy mobillik, moliyaviy resurslar va boshqalar</td><td>Faqat AQSh kollejlari; Best Global Universities alohida reyting</td></tr>
</tbody></table></div>
<p>Ko'rsatkichlar va ularning ulushi deyarli har yili o'zgaradi. Shuning uchun aniq foizlarni yodlamang, har safar metodologiya sahifasini oching.</p>
<h4>Uch savol</h4>
<ol><li>Bu reyting nimani o'lchaydi?</li><li>Bu ko'rsatkich mening bakalavr o'qishimga ta'sir qiladimi?</li><li>Yillar bo'yicha o'rin barqarormi yoki metodologiya o'zgargani uchun sakradimi?</li></ol>
<div class="srcs">Manba: {QS}; {THE}; {USN}. {HOL}.</div>""",
             take="QS obro'ga, THE tadqiqotga, US News AQSh kollejlarining natijalariga ko'proq urg'u beradi. Metodologiyani o'qimasdan o'rinni solishtirmang.",
             task="<ul><li>Bitta universitetni uch reytingda toping va o'rinlarini yozing.</li><li>Farqning sababini metodologiyadan bir jumlada tushuntiring.</li></ul>",
             ph="... universiteti: QS ..., THE ..., US News ... Farq sababi: ..."),
    ],
    tool=dict(id="jadval", short="Jadval", h2="3 universitet talablari jadvali", sub="Darslardagi javoblaringizni bitta jadvalga yig'ing. Har qatorga rasmiy havola qo'ying.",
              h3="Talablar jadvali", tag="5 maydon", ic="scroll", btn="Jadvalni saqlash", badge="Talab tahlilchisi", min=4,
              fields=[dict(k="soha", label="Sohangiz va daraja", ph="Masalan: informatika, bakalavr"),
                      dict(k="u1", label="1-universitet", hint="nomi · model · attestat talabi · til · test · havola", type="area", ph="... · yaxlit · to'g'ridan-to'g'ri · IELTS 6.5 · SAT ixtiyoriy · https://..."),
                      dict(k="u2", label="2-universitet", type="area", ph="... · ball asosidagi · Studienkolleg · ... · https://..."),
                      dict(k="u3", label="3-universitet", type="area", ph="..."),
                      dict(k="savol", label="Ochiq savollar", hint="universitetga yoziladigan", type="area", ph="11 yillik attestat bilan qabul qilasizmi? ...")]),
    check=dict(h2="Talablar nazorati", sub="Jadvalni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har universitet uchun rasmiy qabul sahifasi ochilgan, forum emas.", "Qabul modeli (yaxlit yoki ball asosidagi) belgilangan.",
                      "11 yillik attestat bo'yicha talab aniqlangan yoki savol yuborilgan.", "Til talabi va qabul qilinadigan testlar yozilgan.",
                      "Test (SAT, ACT yoki kirish imtihoni) talabi yozilgan.", "Har ma'lumot yonida havola va tekshirilgan sana bor.",
                      "Reyting faqat saralash uchun ishlatilgan, soha bo'yicha o'rin tekshirilgan.", "Jadvaldagi ma'lumotlar o'zim tekshirgan, taxmin emas."]),
    art_title="3 universitet talablari jadvali", art_short="Jadval",
    art=[("Soha va daraja", ["soha"]), ("Qabul komissiyasi va model", ["a1", "a2"]), ("1-universitet", ["u1"]), ("2-universitet", ["u2"]),
         ("3-universitet", ["u3"]), ("Attestat bo'yicha xulosa", ["a3"]), ("Reyting tahlili", ["a4", "a5"]), ("Ochiq savollar", ["savol"])],
    tip="Har jadval qatorini \"bu ma'lumotni qayerdan oldim?\" degan savol bilan tekshiring. Havolasiz qator taxmin hisoblanadi.",
    sources=f"{CA}; {UCAS}; {CDS}; {ANABIN}; {DAAD_ADM}; {UNIPI}; {QS}; {THE}; {USN}. {STD}",
)
