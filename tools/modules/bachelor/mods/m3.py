from common import HOL, STD

MOD = dict(
    title="Yoʻnalish, qiziqish va maqsad",
    desc="Bachelor Lab M3: fanlar va qiziqishlardan profil, STEM ichida tanlov (fizika, muhandislik, informatika), bakalavrdan keyingi yo'llar, qiziqish sohasi bayoni, izchil hikoya. Natija: 1 sahifalik qiziqish sohasi bayoni va bir jumlali profil.",
    lead="Komissiya sizni hujjatlar orqali taniydi. Agar fanlaringiz, faoliyatingiz va inshoingiz turli tomonga qarasa, kuchli tomonlaringiz ham ko'rinmay qoladi. Bu modulda bitta aniq yo'nalish va uni ko'rsatadigan hikoyani tuzasiz.",
    hero="seedling", weeks="1–2", next="M4 Ariza muddatlari va ish rejasi", next_href="bachelor-lab-m4.html",
    goals=[("seedling", "Bir jumlali profil", "kim, nimaga qiziqasiz, buni nima ko'rsatadi"),
           ("memo", "Qiziqish sohasi bayoni (1 sahifa)", "keng qiziqishdan aniq savolga, dalil bilan"),
           ("compass", "Izchil hikoya xaritasi", "fanlar, faoliyat va insho bitta yo'nalishda")],
    warn="Bu modulda hech qanday tayyor matn berilmaydi. Namunalar \"Kompas tuzgan namuna\" deb belgilangan va faqat tuzilmani ko'rsatish uchun; ularni o'z hujjatingizga ko'chirmang.",
    lessons=[
        dict(t="Men kim sifatida ariza beryapman", short="Profil", min=25, kind="🧭 Profil", ic="seedling",
             hook="\"Men hamma fanni yaxshi ko'raman\" degan abituriyent komissiyaga hech narsa demaydi. Aniq profil arizangizning har qismini bir-biriga bog'laydi.",
             body="""<p>Akademik qiziqish va maqsad ([[academic identity]]) bu siz haqingizdagi bitta aniq fikr: qaysi sohaga qiziqasiz va buni nima ko'rsatadi.</p>
<h4>Uch manba</h4>
<ul><li><b>Fanlar</b>: qaysi fanlarda baholaringiz eng yuqori va qaysi fanga ko'proq vaqt sarflaysiz?</li>
<li><b>Loyihalar</b>: o'zingiz boshlagan yoki qatnashgan ishlar: olimpiada, dasturlash loyihasi, maktab tajribasi, to'garak.</li>
<li><b>Qiziqishlar</b>: kitob, video, savol, sizni darsdan tashqari ham o'ylantiradigan muammo.</li></ul>
<h4>Bir jumlali profil</h4>
<p>Formula: <b>Men [soha]ga qiziqaman, chunki [savol yoki muammo]; buni [dalil 1] va [dalil 2] ko'rsatadi.</b></p>
<div class="box info"><b>Kompas tuzgan namuna (faqat tuzilma uchun):</b> \"Men energiya tizimlariga qiziqaman, chunki qishloqlarda elektr uzilishi nimadan kelib chiqishini tushunmoqchiman; buni fizika olimpiadasidagi ishtirokim va uyda yig'gan quyosh paneli tajribam ko'rsatadi.\"</div>
<p>Dalil bo'lmasa, profil faqat orzu bo'lib qoladi. Hozir dalilingiz kam bo'lsa, M6–M7 da uni yaratish rejasini tuzasiz.</p>""",
             take="Bir jumlali profil: soha, sabab va ikkita dalil. Dalilsiz profil komissiya uchun hech narsa anglatmaydi.",
             task="<ul><li>Uch manbadan (fanlar, loyihalar, qiziqishlar) har biri bo'yicha 3 tadan faktni yozing.</li><li>Formula bo'yicha o'z bir jumlali profilingizni tuzing.</li></ul>",
             ph="Fanlar: ... Loyihalar: ... Qiziqishlar: ... Profil: Men ...ga qiziqaman, chunki ...; buni ... va ... ko'rsatadi."),
        dict(t="Fizika, muhandislik, informatika: real farq", short="STEM tanlovi", min=30, kind="🎯 Mini-test", ic="bulb",
             hook="Fizikani yaxshi ko'rgan o'quvchi muhandislikka, matematikani yaxshi ko'rgan informatikaga borishi shart emas. Har soha boshqa ish turini va boshqa kelajakni beradi.",
             body="""<div class="tbl"><table><thead><tr><th></th><th>Fizika</th><th>Muhandislik</th><th>Informatika</th></tr></thead><tbody>
<tr><td>Asosiy savol</td><td>Tabiat qanday ishlaydi?</td><td>Buni qanday qurish va ishlatish mumkin?</td><td>Buni qanday hisoblash va avtomatlashtirish mumkin?</td></tr>
<tr><td>O'qish tarkibi</td><td>Matematika va nazariya ko'p, laboratoriya</td><td>Matematika, loyiha ishi, chizma, amaliyot</td><td>Dasturlash, algoritmlar, diskret matematika</td></tr>
<tr><td>Kundalik ish</td><td>Model, tajriba, tahlil</td><td>Loyiha, hisob-kitob, sinov, jamoa</td><td>Kod yozish, tizim loyihalash, ma'lumot bilan ishlash</td></tr>
<tr><td>Keyingi yo'l</td><td>Ko'pincha magistratura va tadqiqot</td><td>Sanoat yoki magistratura; ba'zi mamlakatlarda muhandislik litsenziyasi</td><td>Sanoat yoki tadqiqot</td></tr>
</tbody></table></div>
<h4>Tekshiruv usuli</h4>
<ul><li>Uch universitetning birinchi kurs o'quv rejasini oching va qaysi fanlar sizni qiziqtirishini belgilang.</li>
<li>Sohada ishlaydigan odam bilan 15 daqiqa gaplashing: kuni qanday o'tadi?</li>
<li>Bepul onlayn kursning birinchi haftasini o'tib ko'ring.</li></ul>
<div class="box warn">AQShda mutaxassislik ([[major]]) ko'pincha 2-kurs oxirida tanlanadi, UK va Yevropada esa ariza vaqtidayoq. Yevropada noto'g'ri soha tanlash qimmatga tushadi.</div>""",
             take="Fizika tushunishga, muhandislik qurishga, informatika hisoblashga qaratilgan. Tanlovdan oldin o'quv rejasini oching va sohadagi odam bilan gaplashing.",
             quiz=[("Fizikani yaxshi ko'rgan har kim muhandislikka mos keladi.", "n", "Noto'g'ri: muhandislik loyiha va amaliy ishga, fizika nazariya va tajribaga ko'proq qaratilgan."),
                   ("UK da soha odatda ariza vaqtidayoq tanlanadi.", "t", "To'g'ri: UCAS arizasi aniq kursga beriladi."),
                   ("AQShda mutaxassislik ko'pincha birinchi kunning o'zida tanlanishi shart.", "n", "Noto'g'ri: ko'p kollejlarda keyinroq e'lon qilinadi; ayrim muhandislik maktablari bundan mustasno."),
                   ("O'quv rejasini o'qish soha tanlovini tekshirishning ishonchli usuli.", "t", "To'g'ri: unda 4 yil davomida nima o'qishingiz ko'rinadi.")],
             task="<ul><li>Ikkita soha o'rtasida tanlayotgan bo'lsangiz, ikkalasining birinchi kurs fanlarini yozing.</li><li>Qaysi biri sizga yaqinroq va nima uchun, 3 jumlada.</li></ul>",
             ph="Fizika 1-kurs: ... Muhandislik 1-kurs: ... Tanlov: ..., chunki ..."),
        dict(t="Mutaxassislik va keyingi yo'l", short="Keyingi yo'l", min=20, kind="🗺 Yo'l xaritasi", ic="telescope",
             hook="Bakalavr 4 yil davom etadi, lekin tanlovingiz undan keyingi 10 yilga ta'sir qiladi. Keyingi yo'llarni hozirdan bilish soha tanlovini aniqroq qiladi.",
             body="""<h4>Bakalavrdan keyin to'rt yo'l</h4>
<ol><li><b>Sanoatda ishlash</b>: o'qigan mamlakatda (viza qoidalariga qarab) yoki O'zbekistonda.</li>
<li><b>Magistratura</b>: o'sha yoki boshqa mamlakatda. Tafsilotlar Master Lab'da.</li>
<li><b>Tadqiqot va doktorantura</b>: ba'zi mamlakatlarda bakalavrdan to'g'ridan-to'g'ri PhD'ga o'tish mumkin.</li>
<li><b>Vatanga qaytish</b>: ba'zi davlat stipendiyalari qaytish shartini qo'yadi (M11).</li></ol>
<h4>Soha bo'yicha savollar</h4>
<ul><li>Bu soha bo'yicha ish O'zbekistonda bormi va qanday darajadagi ta'lim talab qiladi?</li>
<li>Soha litsenziya yoki sertifikat talab qiladimi (masalan, muhandislik va tibbiyot ayrim mamlakatlarda)?</li>
<li>Tadqiqotga qiziqsangiz, bakalavrda tadqiqot imkoniyati bormi?</li></ul>
<div class="box info">Keyingi yo'lni hozir yakuniy tanlash shart emas. Lekin tanlagan sohangiz kamida ikkita yo'lni ochiq qoldirishi kerak.</div>""",
             take="Bakalavrdan keyin sanoat, magistratura, tadqiqot yoki vatanga qaytish yo'li bor. Tanlagan soha kamida ikkitasini ochiq qoldirsin.",
             task="<ul><li>Sohangiz uchun bakalavrdan keyingi ikki real yo'lni yozing.</li><li>Har biri uchun bitta rasmiy yoki ishonchli manba toping.</li></ul>",
             ph="1-yo'l: ... (manba: ...). 2-yo'l: ..."),
        dict(t="Qiziqish sohasi bayoni", short="Bayon", min=35, kind="🛠 1 sahifa", ic="memo",
             hook="Keng qiziqish (\"men texnologiyani yaxshi ko'raman\") hech kimni ajratib ko'rsatmaydi. Aniq savol esa sizni boshqalardan farqlaydi.",
             body="""<h4>Kenglikdan aniqlikka</h4>
<p>Qiziqish sohasi bayoni 1 sahifali ichki hujjat. U ariza emas, lekin barcha insholar va intervyu uchun asos bo'ladi.</p>
<div class="tbl"><table><thead><tr><th>Daraja</th><th>Misol (Kompas tuzgan namuna)</th></tr></thead><tbody>
<tr><td>Keng soha</td><td>Informatika</td></tr>
<tr><td>Yo'nalish</td><td>Sun'iy intellekt</td></tr>
<tr><td>Aniq savol</td><td>Kam ma'lumotli tillarda (masalan o'zbek tilida) nutqni tanish qanday ishlaydi?</td></tr>
</tbody></table></div>
<h4>Bayon tuzilmasi (4 qism)</h4>
<ol><li><b>Savol</b>: sizni qiziqtiradigan aniq savol.</li>
<li><b>Kelib chiqishi</b>: bu savol qachon va qanday paydo bo'ldi (aniq epizod).</li>
<li><b>Dalil</b>: shu savol ustida nima qildingiz (kitob, loyiha, kurs, tajriba).</li>
<li><b>Keyingi qadam</b>: universitetda bu savol bilan nima qilmoqchisiz.</li></ol>
<div class="box warn">Bayon yuqori ilmiy ish emas. 16–17 yoshli abituriyentdan ilmiy kashfiyot kutilmaydi; aniq savol va o'z qo'lingiz bilan qilingan harakat kutiladi.</div>""",
             take="Qiziqish sohasi bayoni: savol, kelib chiqishi, dalil va keyingi qadam. U barcha insholar va intervyu uchun asos.",
             task="<ul><li>Keng soha → yo'nalish → aniq savol zanjirini yozing.</li><li>Pastdagi vositada 4 qismli bayonni to'ldiring.</li></ul>",
             ph="Soha: ... → yo'nalish: ... → savol: ..."),
        dict(t="Izchil hikoya", short="Hikoya", min=25, kind="🧩 Xarita", ic="scroll",
             hook="Komissiya arizangizni bir necha qism bo'yicha ko'radi: fanlar, faoliyat, insho, tavsiya. Ular bir-birini tasdiqlasa, ishonch oshadi.",
             body="""<h4>Izchillik nima</h4>
<p>Izchil hikoya ([[coherent narrative]]) arizaning hamma qismi bitta yo'nalishni ko'rsatishi. Bu \"hammasi bitta mavzu haqida\" degani emas: turli faoliyatlar ham bitta xarakterni ko'rsata oladi.</p>
<div class="tbl"><table><thead><tr><th>Ariza qismi</th><th>Nimani ko'rsatadi</th><th>Savol</th></tr></thead><tbody>
<tr><td>Fanlar va baholar</td><td>Akademik tayyorgarlik</td><td>Sohangizga yaqin fanlarda baholaringiz qanday?</td></tr>
<tr><td>Faoliyatlar (M7)</td><td>Qiziqishning amaldagi isboti</td><td>Darsdan tashqari shu yo'nalishda nima qildingiz?</td></tr>
<tr><td>Insho (M9)</td><td>Shaxs va motivatsiya</td><td>Nega sizga bu soha muhim?</td></tr>
<tr><td>Tavsiya (M8)</td><td>Boshqa odam ko'zi bilan dalil</td><td>O'qituvchi qaysi epizodni yoza oladi?</td></tr>
</tbody></table></div>
<h4>Bo'shliqni topish</h4>
<p>Jadvalni to'ldirganda bo'sh qolgan katak sizning keyingi oylardagi ishingiz. Masalan, faoliyat ustuni bo'sh bo'lsa, M7 da bitta chuqur loyiha rejalaysiz.</p>
<div class="box info">Hikoyani to'qimang. Komissiya tavsiya xati va faoliyatlar ro'yxati orqali insho bilan solishtiradi.</div>""",
             take="Fanlar, faoliyat, insho va tavsiya bitta yo'nalishni tasdiqlasa, ariza kuchayadi. Bo'sh katak keyingi oylardagi ish rejasi.",
             task="<ul><li>To'rt ustunli jadvalni o'zingiz uchun to'ldiring.</li><li>Eng zaif ustunni va uni kuchaytirish uchun 1 aniq harakatni yozing.</li></ul>",
             ph="Fanlar: ... Faoliyat: ... Insho g'oyasi: ... Tavsiya: ... Zaif: ..., harakat: ..."),
    ],
    tool=dict(id="bayon", short="Bayon", h2="Qiziqish sohasi bayoni", sub="1 sahifa: savol, kelib chiqishi, dalil, keyingi qadam. So'z hisoblagich mo'ljalni ko'rsatadi.",
              h3="Bayon ish varag'i", tag="5 maydon", ic="memo", btn="Bayonni saqlash", badge="Kimlik me'mori", min=4,
              fields=[dict(k="profil", label="Bir jumlali profil", type="area", ph="Men ...ga qiziqaman, chunki ...; buni ... va ... ko'rsatadi."),
                      dict(k="savol", label="1. Aniq savol", type="area", wc="15-60", ph="..."),
                      dict(k="kelib", label="2. Kelib chiqishi (epizod)", type="area", wc="60-150", ph="Qachon, qayerda, nima bo'ldi ..."),
                      dict(k="dalil", label="3. Dalil (nima qildim)", type="area", wc="60-150", ph="O'qigan kitob, loyiha, kurs ..."),
                      dict(k="keyin", label="4. Universitetda keyingi qadam", type="area", wc="40-120", ph="Qaysi fan, laboratoriya yoki loyiha ...")]),
    check=dict(h2="Kimlik nazorati", sub="Bayonni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Profil bitta jumla va unda ikkita dalil bor.", "Savol aniq, \"hamma narsa\" emas.",
                      "Kelib chiqishi aniq epizod bilan yozilgan.", "Har dalil tekshiriladigan (hujjat, natija yoki guvoh).",
                      "Soha tanlovi o'quv rejasi bilan tekshirilgan.", "Bakalavrdan keyingi kamida ikki yo'l yozilgan.",
                      "Izchil hikoya jadvalidagi eng zaif ustun aniqlangan.", "Hech qanday voqea to'qilmagan, tayyor matn ko'chirilmagan."]),
    art_title="Qiziqish sohasi bayoni", art_short="Bayon",
    art=[("Bir jumlali profil", ["profil", "a1"]), ("Soha tanlovi", ["a2", "a3"]), ("Aniq savol", ["savol", "a4"]),
         ("Kelib chiqishi", ["kelib"]), ("Dalil", ["dalil"]), ("Universitetda keyingi qadam", ["keyin"]), ("Izchil hikoya xaritasi", ["a5"])],
    tip="Profilingizni ota-onangiz yoki do'stingizga ayting va ulardan qayta aytib berishni so'rang. Ular boshqa so'z bilan to'g'ri aytsa, profil aniq.",
    sources=f"Universitetlarning rasmiy o'quv rejalari (curriculum) va dastur sahifalari. {STD}",
)
