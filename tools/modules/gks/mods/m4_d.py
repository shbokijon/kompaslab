from _lib import lib
from common import G26, STD

L1 = dict(t="Tuzilma: Muammo → Yechim → Yangilik → Ta'sir", short="Tuzilma", min=35, kind="🎯 Mini-test", ic="compass",
    hook="Doktorantura nomzodining ilmiy rejasi GKS ning o'quv rejasi formasi ichida beriladi. Forma bandlari bir narsani so'raydi, ilmiy mantiq boshqa tartibni talab qiladi: ikkalasini moslashtirish kerak.",
    body=f"""<h4>To'rt blok</h4>
<div class="tbl"><table><thead><tr><th>Blok</th><th>Savol</th><th>Hajmning taxminiy ulushi</th></tr></thead><tbody>
<tr><td><b>Muammo</b></td><td>Nima noma'lum yoki ishlamayapti, va bu kimga muhim?</td><td>~25%</td></tr>
<tr><td><b>Yechim</b></td><td>Qaysi savol, qaysi ma'lumot va usul bilan?</td><td>~40%</td></tr>
<tr><td><b>Yangilik</b></td><td>Mavjud ishlardan nima bilan farq qiladi?</td><td>~15%</td></tr>
<tr><td><b>Ta'sir</b></td><td>Natija fan va amaliyotga nima beradi?</td><td>~20%</td></tr>
</tbody></table></div>
<p>Ulushlar Kompas tavsiyasi, yo'riqnoma talabi emas.</p>
<h4>GKS formasiga joylash</h4>
<ol><li>Forma shablonidagi bandlarni ko'chiring.</li><li>Har bandga qaysi blok javob berishini belgilang (masalan, \"o'qish maqsadi\" → Muammo + Ta'sir; \"o'qish rejasi\" → Yechim + vaqt).</li>
<li>Bandga javob bermaydigan blokni majburan qo'shmang: forma talabi ustun.</li></ol>
<div class="srcs">Manba: {G26}.</div>""",
    take="Ilmiy reja to'rt blokdan iborat; ularni forma bandlariga joylang, forma talabi ustun.",
    quiz=[("Ilmiy rejaning eng katta qismi odatda Yechim (savol va usul) bloki.", "t", "To'g'ri: Kompas tavsiyasida ~40%."),
          ("Forma bandiga javob bermasa ham to'rt blokning hammasini o'z tartibida yozish kerak.", "n", "Noto'g'ri: forma talabi ustun."),
          ("2026 GKS-G da doktorantura uchun 1 yil koreys tili ham rejaga kiradi.", "t", "To'g'ri: 1 yil til + 3 yil daraja."),
          ("Yangilik bloki \"bu mavzuni hech kim o'rganmagan\" degan da'vo bilan yoziladi.", "n", "Noto'g'ri: yangilik manbalarga tayangan aniq farq.")],
    task="<ul><li>Forma bandlari va to'rt blok xaritasini tuzing.</li></ul>",
    ph="Band 1 → Muammo + Ta'sir ...")

L2 = dict(t="Muammo va adabiyotdagi bo'shliq", short="Bo'shliq", min=60, kind="📚 30 manba", ic="books",
    hook="Doktorlik bo'shlig'i \"menga qiziq\" emas, \"adabiyotda shu yetishmaydi va buni manbalar ko'rsatadi\" degani. Buning uchun 25–40 manbali baza kerak.",
    body="""<h4>Baza qurish</h4>
<ul><li>Google Scholar, Scopus yoki Web of Science (universitet kirishi bo'lsa), sohangiz preprint serverlari, tanlagan laboratoriyaning nashrlari.</li>
<li>Uch qatlam: 5–8 ta sharh maqolasi (review), 15–25 ta asosiy ish, 5–8 ta so'nggi 2 yildagi ish.</li>
<li>Har manba uchun annotatsiya: savol, usul, natija, cheklov, sizning savolingizga aloqasi.</li></ul>
<h4>Bo'shliqni dalil bilan ko'rsatish</h4>
<div class="tbl"><table><thead><tr><th>Bo'shliq turi</th><th>Dalil shakli</th></tr></thead><tbody>
<tr><td>Hudud yoki ma'lumot</td><td>\"A, B, C ishlari X hududida; Y hudud uchun shunga o'xshash tahlil topilmadi (qidiruv: ...)\"</td></tr>
<tr><td>Usul</td><td>\"Mavjud ishlar Z usuliga tayanadi; W usuli sinab ko'rilmagan, lekin D ishida o'xshash vazifada samarali\"</td></tr>
<tr><td>Qarama-qarshi natija</td><td>\"E va F ishlari teskari natija beradi; farq sababi tushuntirilmagan\"</td></tr>
<tr><td>Mualliflar aytgan cheklov</td><td>\"G o'z ishida ... cheklovini tan oladi\"</td></tr>
</tbody></table></div>
<div class="box warn">\"Topilmadi\" deyishdan oldin qidiruv so'zlaringiz va bazalaringizni yozib qo'ying. Har manbani DOI orqali tekshiring; sun'iy intellekt vositalari yo'q maqolalarni \"topishi\" mumkin.</div>""",
    take="25–40 manbali baza uch qatlamda; bo'shliq turi va uni ko'rsatadigan manbalar aniq yozilgan.",
    task="<ul><li>Vositadagi manbalar bazasini boshlang (kamida 15 tasini hozir).</li><li>Bo'shliqni 2–3 jumlada, manbalarga tayanib yozing.</li></ul>",
    ph="Bo'shliq: ... (manbalar: ...)")

L3 = dict(t="Metodologiya", short="Metod", min=50, kind="🔬 Metod", ic="telescope",
    hook="Professor ilmiy rejaning birinchi navbatda metod qismini o'qiydi: savol qiziq bo'lsa ham, uni amalda qanday bajarishingiz aniq bo'lmasa, reja ishlamaydi.",
    body="""<h4>Metod bo'limi tarkibi</h4>
<ul><li><b>Ma'lumot:</b> qayerdan, qancha, qanday ruxsat bilan. Ma'lumot hali yo'q bo'lsa, uni qanday olishingiz.</li>
<li><b>Usul:</b> asosiy usul va nega aynan u (bir–ikki muqobil bilan solishtirib).</li>
<li><b>Vositalar:</b> dasturlar, asboblar, hisoblash resurslari.</li>
<li><b>Tekshirish:</b> natija to'g'riligini qanday sinaysiz (validatsiya, nazorat guruhi, sezgirlik tahlili).</li>
<li><b>Cheklovlar va xavflar:</b> nima ishlamasligi mumkin va B-rejangiz.</li></ul>
<h4>Laboratoriya resurslari bilan moslik</h4>
<p>Metodingiz tanlangan laboratoriyaning asbob-uskunasi, ma'lumotlari va tajribasiga tayanishi kerak. Laboratoriya sahifasidan yoki professor maqolalaridan aniq resursni nomi bilan ko'rsating. Laboratoriyada bo'lmagan resursga tayangan reja ishonchsiz.</p>
<div class="box info">Xavf va cheklovni ochiq yozish zaiflik emas: bu siz loyihani real baholashingizni ko'rsatadi.</div>""",
    take="Metod: ma'lumot, usul, vositalar, tekshirish, cheklov va xavf; hammasi laboratoriya resurslariga mos.",
    task="<ul><li>Metod bo'limini besh qism bo'yicha yozing; laboratoriyaning kamida bitta aniq resursini nomi bilan ko'rsating.</li></ul>",
    ph="Ma'lumot: ... Usul: ... Vositalar: ... Tekshirish: ... Xavf: ...")

L4 = dict(t="Yangilik va ta'sir", short="Ta'sir", min=35, kind="✍ Blok", ic="seedling",
    hook="\"Bu ish mamlakatimiz rivojiga katta hissa qo'shadi\" jumlasini har ikkinchi reja yozadi. Ta'sirni aniq kim, qanday foydalanishi bilan ko'rsating.",
    body="""<h4>Yangilik turlari</h4>
<ul><li><b>Yangi ma'lumot yoki hudud:</b> o'rganilmagan joyda ma'lum usul.</li><li><b>Yangi usul:</b> ma'lum muammoga yangi yondashuv.</li>
<li><b>Yangi bog'lanish:</b> ikki sohani birlashtirish.</li><li><b>Yangi miqyos:</b> kichik tadqiqotni katta ma'lumotga kengaytirish.</li></ul>
<p>Yangilikni 2–3 manba bilan solishtirib bir jumlada ayting: \"X va Y ishlaridan farqli ravishda, bu tadqiqot ...\".</p>
<h4>Ta'sir</h4>
<ul><li><b>Fanga:</b> qaysi savolga javob beradi, kimlar foydalanadi.</li>
<li><b>Amaliyotga:</b> qaysi tashkilot yoki soha natijadan qanday foydalanishi mumkin.</li>
<li><b>O'zbekiston va Koreya aloqasi:</b> faqat dalil bilan (mavjud hamkorlik dasturi, ma'lumot almashuvi, sohadagi aniq ehtiyoj va uning manbasi). Dalil bo'lmasa, umumiy da'vo yozmang.</li></ul>
<div class="box warn">Mubolag'ali ta'sir (\"energetika muammosini hal qiladi\") komissiya ishonchini pasaytiradi. Kichik, lekin aniq va tekshiriladigan ta'sir kuchliroq.</div>""",
    take="Yangilik: tur va 2–3 manba bilan farq. Ta'sir: fanga, amaliyotga, va faqat dalil bilan O'zbekiston–Koreya aloqasi.",
    task="<ul><li>Yangilik jumlasini va ta'sir paragrafini yozing.</li></ul>",
    ph="Yangilik: X va Y dan farqli ravishda ... Ta'sir: ...")

L5 = dict(t="Vaqt va resurs rejasi", short="Gantt", min=40, kind="🗓 Gantt", ic="calendar",
    hook="Doktorantura 3 yil davom etadi, undan oldin 1 yil til. Gantt jadvalisiz reja istak ro'yxatiga o'xshaydi.",
    body=f"""<h4>Gantt jadvali (Gantt chart) tuzilmasi</h4>
<div class="tbl"><table><thead><tr><th>Davr</th><th>Ish</th><th>O'lchanadigan natija</th></tr></thead><tbody>
<tr><td>Til yili</td><td>Koreys tili; adabiyot bazasini kengaytirish; laboratoriya bilan tanishuv</td><td>TOPIK maqsadi, sharh qoralamasi</td></tr>
<tr><td>1-yil</td><td>Majburiy kurslar, usulni sinash, pilot ma'lumot</td><td>Kurslar, pilot natija</td></tr>
<tr><td>2-yil</td><td>Asosiy ma'lumot va tahlil; konferensiya</td><td>Konferensiya ma'ruzasi, 1-maqola qoralamasi</td></tr>
<tr><td>3-yil</td><td>Yakuniy tahlil, maqolalar, dissertatsiya</td><td>Maqola(lar), dissertatsiya himoyasi</td></tr>
</tbody></table></div>
<p>Jadval Kompas tavsiyasi. Universitetning doktorantura talablari (kurslar soni, malaka imtihoni, nashr talabi) dasturdan dasturga farq qiladi: ularni universitet sahifasidan tekshirib jadvalga qo'shing.</p>
<h4>Resurslar</h4>
<ul><li>Hisoblash, asbob-uskuna, dala ishlari va ularning laboratoriyada mavjudligi.</li>
<li>Har yil uchun bitta xavf va zaxira reja.</li></ul>
<div class="srcs">Davomiylik: {G26} (1 yil til + 3 yil).</div>""",
    take="Gantt: til yili + 3 yil, har davrda o'lchanadigan natija va xavf; universitet talablari qo'shilgan.",
    task="<ul><li>Vositada 3–4 yillik Gantt jadvalini yozing: davr · ish · natija · xavf.</li></ul>",
    ph="Qaysi davr eng xavfli va nega: ...")

L6 = dict(t="Tahrir va o'zaro tahrir", short="Tahrir", min=40, kind="📊 Rubric", ic="chart",
    hook="Ilmiy rejani avval sohangizni bilmaydigan odam, keyin mutaxassis o'qiydi. Ikkalasi uchun ham tushunarli bo'lishi kerak.",
    body="""<h4>Baholash mezoni (Rubric), har biri 0–4</h4>
<div class="tbl"><table><thead><tr><th>Mezon</th><th>4 ball</th></tr></thead><tbody>
<tr><td>Forma</td><td>Har bandga javob, hajm chegarasida</td></tr>
<tr><td>Bo'shliq</td><td>Manbalar bilan isbotlangan</td></tr>
<tr><td>Metod</td><td>Bajariladigan, laboratoriya resurslariga mos, xavf ko'rsatilgan</td></tr>
<tr><td>Vaqt</td><td>Gantt real, o'lchanadigan natijalar bilan</td></tr>
<tr><td>Til va atamalar</td><td>Atamalar izchil, birinchi ishlatishda izohlangan</td></tr>
<tr><td>Iqtiboslar</td><td>Bitta uslub, har manba tekshirilgan</td></tr>
</tbody></table></div>
<h4>Tartib</h4>
<ol><li>Mutaxassis bo'lmagan o'quvchi testi: \"nima, nega, qanday\" savollariga javob bera oladimi?</li>
<li>Sohangizdagi bitta mutaxassis (magistratura rahbari yoki hamkasb) rubric bilan baholaydi.</li>
<li>Har izohga qaror va tahrir qaydi.</li></ol>
<div class="box warn">Tahrirchi matnni qayta yozmaydi; izoh beradi. Reja sizniki bo'lishi kerak: professor suhbatida har jumlani himoya qilasiz.</div>""",
    take="Olti mezonli rubric, mutaxassis bo'lmagan va mutaxassis o'quvchi, tahrir qaydi.",
    task="<ul><li>Rejani rubric bo'yicha baholang va o'zaro tahrir natijasini tahrir qaydiga yozing.</li></ul>",
    ph="Baho: ... Izohlar: ... Qarorlar: ...")

MOD = dict(
    title="Ilmiy reja",
    desc="GKS Lab M4-D (doktorantura): Muammo → Yechim → Yangilik → Ta'sir tuzilmasi, adabiyotdagi bo'shliq, metodologiya, yangilik va ta'sir, vaqt va resurs rejasi, o'zaro tahrir. Natija: GKS formasiga moslangan ilmiy reja, 30 manbali baza, 3–4 yillik Gantt jadvali.",
    lead="Doktorantura trekida ilmiy reja asosiy hujjat. Bu modulda uni to'rt blokda qurasiz, bo'shliqni manbalar bilan isbotlaysiz, metodni laboratoriya resurslariga moslaysiz va til yilini hisobga olgan Gantt jadvalini tuzasiz.",
    hero="books", weeks="4–5", next="M5-D Professor bilan muloqot va yakunlash", next_href="gks-lab-m5-d.html",
    goals=[("books", "Ilmiy reja", "GKS o'quv rejasi formasiga moslangan, to'rt blokli"),
           ("scroll", "30 manbali baza", "annotatsiya va bo'shliq jumlasi bilan"),
           ("calendar", "3–4 yillik Gantt jadvali", "til yili, bosqichlar, nashr va konferensiya rejasi")],
    warn="Ilmiy rejani o'zingiz yozasiz; namunalar Kompas tuzgan o'quv materiali. Har manba DOI yoki rasmiy sahifa orqali tekshiriladi. Davomiylik 2026 GKS-G yo'riqnomasidan, 31.10.2026 holatiga.",
    lessons=[L1, L2, L3, L4, L5, L6],
    tool=dict(id="ilmiy", short="Reja", h2="Ilmiy reja quruvchi", sub="To'rt blok, manbalar va Gantt. So'z hisoblagichi mo'ljal; forma chegarasi ustun.",
              h3="Ilmiy reja", tag="6 maydon", ic="books", btn="Rejani saqlash", badge="Rejachi", min=5,
              fields=[dict(k="b1", label="Muammo", type="area", ph=""),
                      dict(k="b2", label="Yechim: savol, ma'lumot, usul", type="area", ph=""),
                      dict(k="b3", label="Yangilik", type="area", ph=""),
                      dict(k="b4", label="Ta'sir", type="area", ph=""),
                      dict(k="lit", label="Manbalar bazasi", hint="25–40 manba", type="area", ph="Muallif, yil, sarlavha, DOI · savol · natija · cheklov"),
                      dict(k="gantt", label="Gantt jadvali", hint="davr · ish · natija · xavf", type="area", ph="Til yili · ... 1-yil · ...")]),
    check=dict(h2="Ilmiy reja nazorati", sub="Yakuniy versiyadan oldin.", h3="10 bandlik nazorat",
               items=["Forma bandlarining hammasiga javob bor, hajm chegarasida.", "Bo'shliq kamida 2–3 manba bilan isbotlangan.",
                      "Manbalar bazasi 25–40 ta, har biri tekshirilgan.", "Metod laboratoriyaning aniq resursiga tayanadi.",
                      "Cheklov va xavf ochiq yozilgan.", "Yangilik manbalar bilan solishtirib aytilgan.",
                      "Ta'sir aniq va mubolag'asiz.", "Gantt til yili va 3 yilni qamraydi, o'lchanadigan natijalar bilan.",
                      "Atamalar izchil, iqtibos uslubi bitta.", "O'zaro tahrir va tahrir qaydi bajarilgan."]),
    art_title="Ilmiy reja", art_short="Reja",
    art=[("Forma bandlari xaritasi", ["a1"]), ("Muammo va bo'shliq", ["b1", "a2"]), ("Yechim va metod", ["b2", "a3"]),
         ("Yangilik va ta'sir", ["b3", "b4", "a4"]), ("Manbalar bazasi", ["lit"]), ("Gantt jadvali", ["gantt", "a5"]), ("Tahrir qaydi", ["a6"])],
    tip="Ilmiy rejani o'qib bo'lgach, o'zingizdan so'rang: agar ertaga laboratoriyaga kelsam, birinchi haftada aynan nima qilaman? Javob rejada bo'lmasa, metod hali umumiy.",
    sources=STD,
)

# Editorial source-check notice; follow the current official application guidelines.
MOD["lead"] += " <strong>Rasmiy manbani tekshiring:</strong> GKS-G joriy sikli qoidalarini va Oʻzbekiston uchun eʼlonni har ariza oldidan tekshiring. Muddat, hujjat va muvofiqlik talablari oʻzgarishi mumkin."
