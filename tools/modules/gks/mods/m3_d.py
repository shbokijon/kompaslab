from _lib import les, body, lib
from common import G26, STD

L1 = dict(t="PhD nomzodi nimani taklif qiladi", short="Taklif", min=30, kind="✍ Bayon", ic="telescope",
    hook="Magistratura nomzodi \"o'rganmoqchiman\" deydi. Doktorantura nomzodidan komissiya va professor boshqa narsani kutadi: siz laboratoriyaga qanday bilim, usul va ish qobiliyati olib kelasiz?",
    body=f"""<h4>Magistratura va doktorantura arizasi farqi</h4>
<div class="tbl"><table><thead><tr><th></th><th>Magistratura</th><th>Doktorantura</th></tr></thead><tbody>
<tr><td>Asosiy savol</td><td>Nimani o'rganadi?</td><td>Qanday yangi bilim yaratadi va uni uddalaydimi?</td></tr>
<tr><td>Og'irlik markazi</td><td>O'quv rejasi</td><td>Ilmiy reja (o'quv rejasi formasi ichida) va professor bilan moslik</td></tr>
<tr><td>Dalil</td><td>Kurs ishi, bitiruv ishi</td><td>Magistrlik dissertatsiyasi, nashr, konferensiya, mustaqil tadqiqot</td></tr>
<tr><td>Davomiylik (2026 GKS-G)</td><td>1 yil til + 2 yil</td><td>1 yil til + 3 yil</td></tr>
</tbody></table></div>
<h4>Laboratoriyaga keltiriladigan qiymat</h4>
<ul><li><b>Usul:</b> siz mustaqil bajara oladigan aniq usul yoki vosita (masalan, raqamli modellash, laboratoriya tahlili, dala o'lchovi).</li>
<li><b>Ma'lumot yoki hudud:</b> laboratoriyada yo'q, lekin sizda kirish imkoni bor ma'lumot yoki tadqiqot hududi (rasmiy ruxsat bilan).</li>
<li><b>Mustaqillik:</b> o'z savolingizni qo'yib, loyihani oxiriga yetkazganingiz dalili.</li></ul>
<div class="box warn">Bu \"o'zingizni sotish\" emas. Har bandni hujjat yoki nashr bilan isbotlay olmasangiz, uni yozmang: doktorantura suhbatida texnik savollar beriladi.</div>
<div class="srcs">Manba: {G26}.</div>""",
    take="Doktorantura nomzodi o'qishni emas, laboratoriyaga qiymat taklif qiladi: usul, ma'lumot yoki hudud, mustaqillik dalili.",
    task="<ul><li>Laboratoriyaga keltiradigan qiymatingizni uch band bo'yicha yozing; har bandga dalil qo'shing.</li></ul>",
    ph="Usul: ... (dalil) Ma'lumot: ... Mustaqillik: ...")

L2 = dict(t="Ilmiy portfel auditi", short="Portfel", min=40, kind="🎯 Mini-test", ic="scroll",
    hook="Doktorantura nomzodining ilmiy portfeli professor va komissiya uchun eng ishonchli dalil. Lekin uni tartibsiz taqdim etsangiz, kuchli ish ham ko'rinmay qoladi.",
    body="""<h4>Portfel tarkibi</h4>
<div class="tbl"><table><thead><tr><th>Element</th><th>Nima yoziladi</th><th>Holat</th></tr></thead><tbody>
<tr><td>Nashrlar</td><td>Mualliflar (siz ajratilgan), yil, sarlavha, jurnal, DOI</td><td>Chop etilgan / qabul qilingan / ko'rib chiqilmoqda</td></tr>
<tr><td>Konferensiyalar</td><td>Ma'ruza yoki poster, nomi, joyi, yil</td><td>Faqat haqiqatda taqdim etilgan</td></tr>
<tr><td>Preprint</td><td>Server (masalan, arXiv), havola</td><td>Taqriz qilinmaganini aniq ayting</td></tr>
<tr><td>Magistrlik ishi</td><td>Mavzu, rahbar, asosiy natija, himoya yili</td><td>Himoya qilingan / jarayonda</td></tr>
<tr><td>Kod va ma'lumotlar</td><td>Ochiq repozitoriy, ma'lumotlar to'plami, litsenziya</td><td>Faqat o'zingiz yozgan yoki hissangiz aniq bo'lgan</td></tr>
</tbody></table></div>
<h4>Halollik qoidalari</h4>
<ul><li>\"Ko'rib chiqilmoqda\" maqolani \"chop etilgan\" deb yozmang.</li><li>Mualliflik tartibini o'zgartirmang; hissangizni bir jumlada aniq ayting.</li><li>Konferensiya tezislari to'plamidagi qisqa matnni to'liq maqola deb ko'rsatmang.</li></ul>
<div class="box info">Nashr yo'q bo'lsa ham doktoranturaga topshirish mumkin: u holda magistrlik ishi, kod va ma'lumotlar, ilmiy reja sifati og'irroq vazn oladi.</div>""",
    take="Portfel: nashrlar, konferensiyalar, preprint, magistrlik ishi, kod va ma'lumotlar; har biri aniq holati va hissangiz bilan.",
    quiz=[("Ko'rib chiqilayotgan maqolani CV da \"chop etilgan\" deb yozish mumkin.", "n", "Noto'g'ri: holatini aniq yozing."),
          ("2026 GKS-G da doktorantura 1 yil til va 3 yil dasturdan iborat.", "t", "To'g'ri."),
          ("Preprint taqriz qilinmagan ish ekanini aniq ko'rsatish kerak.", "t", "To'g'ri."),
          ("Nashrsiz nomzod doktoranturaga umuman topshira olmaydi.", "n", "Noto'g'ri: boshqa dalillar og'irroq vazn oladi.")],
    task="<ul><li>Portfel auditi jadvalini to'ldiring: element · ma'lumot · holat · sizning hissangiz.</li></ul>",
    ph="Element · ma'lumot · holat · hissa")

L3 = dict(t="PhD darajasidagi CV (Core)", short="CV", min=35, kind="🛠 CV", ic="memo",
    hook="Doktorantura CV si magistratura CV sining kengaytmasi emas: unda nashrlar, usullar va ilmiy faoliyat birinchi qatorlarda turadi.",
    body="""<h4>Bo'limlar tartibi</h4>
<ol><li><b>Ta'lim:</b> magistratura (dissertatsiya nomi, rahbar), bakalavriat; baho asl shkalada.</li>
<li><b>Tadqiqot qiziqishlari:</b> 2–3 qator, ilmiy rejangiz bilan bir xil atamalarda.</li>
<li><b>Nashrlar:</b> bitta iqtibos uslubi (masalan, APA yoki sohangiz jurnalining uslubi), ismingiz qalin, holati bilan.</li>
<li><b>Konferensiyalar va taqdimotlar.</b></li>
<li><b>Tadqiqot tajribasi:</b> loyiha, rol, usul, natija.</li>
<li><b>Metodik ko'nikmalar:</b> asboblar, dasturlar, usullar; darajasi bilan (mustaqil ishlatganman / tanishman).</li>
<li><b>O'qitish, grantlar, mukofotlar, tillar.</b></li></ol>
<h4>Nashr qatori</h4>
<div class="out" style="white-space:normal"><span lang="en">Karimov, A., <b>Surname, N.</b>, &amp; Lee, J. (2025). Title of the article. <i>Journal Name</i>, 12(3), 45–60. https://doi.org/...</span></div>
<p style="margin-top:8px">Namuna Kompas tomonidan tuzilgan; mualliflar va jurnal shartli.</p>
<div class="box warn">CV dagi har nashr, konferensiya va ko'nikma ilmiy reja, bayonot va tavsiya xati bilan bir xil bo'lsin. M5-D da izchillik auditi qilasiz.</div>""",
    take="PhD CV: ta'lim, tadqiqot qiziqishlari, nashrlar (bitta uslub, holati bilan), konferensiyalar, tajriba, metodik ko'nikmalar.",
    task="<ul><li>Vositada CV ning nashrlar va metodik ko'nikmalar bo'limlarini yozing.</li></ul>",
    ph="CV bo'yicha qaydlar: ...")

L4 = dict(t="Magistrlik ishidan doktorlik yo'nalishiga", short="Yo'nalish", min=40, kind="🔬 Savol", ic="bulb",
    hook="Eng ishonchli doktorlik savoli ko'pincha magistrlik ishingiz tugagan joydan boshlanadi: siz javob bera olmagan savol yoki cheklov.",
    body="""<h4>Kengaytirish yo'llari</h4>
<div class="tbl"><table><thead><tr><th>Manba</th><th>Savol</th><th>Doktorlik yo'nalishi</th></tr></thead><tbody>
<tr><td>Cheklov</td><td>Ishimda nima o'lchanmadi yoki soddalashtirildi?</td><td>Cheklovni olib tashlaydigan usul</td></tr>
<tr><td>Javobsiz savol</td><td>Natijalar qaysi yangi savolni tug'dirdi?</td><td>Shu savolga bag'ishlangan tadqiqot</td></tr>
<tr><td>Ko'lam</td><td>Natija boshqa hudud, vaqt yoki ma'lumotda ishlaydimi?</td><td>Umumlashtirish yoki taqqoslash</td></tr>
<tr><td>Usul</td><td>Yangi usul (masalan, mashinali o'rganish) natijani yaxshilaydimi?</td><td>Usulni ishlab chiqish va sinash</td></tr>
</tbody></table></div>
<h4>3 ta potensial doktorlik savoli</h4>
<p>Uchta savol yozing va har biri uchun: qaysi kengaytirish yo'lidan kelgani, javob uchun kerakli ma'lumot va usul, Koreyadagi qaysi laboratoriya shu usulda ishlaydi (M2 dan). Keyin bittasini asosiy deb tanlang, qolganlari professor bilan suhbatda zaxira.</p>
<div class="box info">Savolni hozir yakuniy qilmang. Doktoranturada mavzu professor va laboratoriya resurslari bilan birga aniqlashadi; ilmiy rejada buni ochiq ayting.</div>""",
    take="Doktorlik savoli magistrlik ishining cheklovi, javobsiz savoli, ko'lami yoki usulidan kengaytiriladi. Uchta savol, bittasi asosiy.",
    task="<ul><li>3 ta potensial doktorlik savolini yozing va har birining manbasini (cheklov, savol, ko'lam, usul) belgilang.</li></ul>",
    ph="1) ... (cheklovdan) 2) ... 3) ...")

MOD = dict(
    title="Doktorantura nomzodining ilmiy pozitsiyasi",
    desc="GKS Lab M3-D (doktorantura): PhD nomzodi nimani taklif qiladi, ilmiy portfel auditi, PhD darajasidagi CV va magistrlik ishidan doktorlik yo'nalishiga. Natija: portfel auditi, PhD CV, 3 ta potensial doktorlik savoli.",
    lead="Doktorantura trekida siz o'quvchi emas, kichik tadqiqotchi sifatida baholanasiz. Bu modulda ilmiy portfelingizni tekshirasiz, PhD darajasidagi CV yozasiz va magistrlik ishingizdan doktorlik savollarini chiqarasiz.",
    hero="telescope", weeks="2–3", next="M4-D Ilmiy reja", next_href="gks-lab-m4-d.html",
    goals=[("scroll", "Portfel auditi", "har element holati va hissangiz bilan"),
           ("memo", "PhD darajasidagi CV", "nashrlar va metodik ko'nikmalar oldinda"),
           ("bulb", "3 ta potensial doktorlik savoli", "bittasi asosiy")],
    warn="Nashr, konferensiya va ko'nikmalar faqat haqiqatdagi holati bilan yoziladi. Davomiylik va qoidalar 2026 GKS-G yo'riqnomasidan, 31.10.2026 holatiga.",
    lessons=[L1, L2, L3, L4],
    tool=dict(id="portfel", short="Portfel", h2="Portfel, CV va savollar", sub="Doktorlik pozitsiyangizning asosiy materiallari.",
              h3="Ilmiy pozitsiya", tag="5 maydon", ic="telescope", btn="Pozitsiyani saqlash", badge="Tadqiqotchi", min=4,
              fields=[dict(k="val", label="Laboratoriyaga keltiradigan qiymat", type="area", ph="Usul · ma'lumot · mustaqillik"),
                      dict(k="port", label="Portfel auditi", hint="element · holat · hissa", type="area", ph=""),
                      dict(k="cvPub", label="CV: Publications", hint="ingliz tilida", type="area", ph=""),
                      dict(k="cvSkill", label="CV: Methods and skills", type="area", ph=""),
                      dict(k="qs", label="3 ta doktorlik savoli", type="area", ph="1) ... 2) ... 3) ... Asosiy: ...")]),
    check=dict(h2="Pozitsiya nazorati", sub="Yakunlashdan oldin.", h3="9 bandlik nazorat",
               items=["Har nashr holati aniq (chop etilgan, qabul qilingan, ko'rib chiqilmoqda).", "Mualliflik tartibi o'zgartirilmagan, hissam aniq.",
                      "Preprint taqriz qilinmagan deb ko'rsatilgan.", "CV da bitta iqtibos uslubi.",
                      "Metodik ko'nikmalar darajasi bilan.", "Har \"qiymat\" bandi dalil bilan.",
                      "Doktorlik savollari magistrlik ishidan mantiqan kelib chiqadi.", "Asosiy savol uchun mos laboratoriya bor (M2).",
                      "CV formalardagi ma'lumot bilan bir xil."]),
    art_title="Ilmiy pozitsiya: portfel, CV va savollar", art_short="Pozitsiya",
    art=[("Laboratoriyaga keltiradigan qiymat", ["val", "a1"]), ("Portfel auditi", ["port", "a2"]), ("CV: Publications", ["cvPub"]),
         ("CV: Methods and skills", ["cvSkill", "a3"]), ("Doktorlik savollari", ["qs", "a4"])],
    tip="Har nashr yoki loyiha yoniga \"mening hissam\" deb bitta jumla yozing. Professor birinchi suhbatda aynan shuni so'raydi.",
    sources=STD,
)
