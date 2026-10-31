from _lib import les, body, lib
from common import G26, STD

PROF = dict(t="Professorni tanlash", short="Professor", min=40, kind="🔎 Tahlil", ic="telescope",
    hook="Universitet tanlangan, lekin magistraturada siz kunlaringizni muayyan laboratoriyada o'tkazasiz. Professorni nomi uchun emas, ishi uchun tanlang.",
    body=f"""<h4>Nimani tekshirasiz</h4>
<div class="tbl"><table><thead><tr><th>Manba</th><th>Savol</th></tr></thead><tbody>
<tr><td>Laboratoriya sahifasi</td><td>Hozir qaysi mavzular ustida ishlaydi? Sahifa yangilanganmi?</td></tr>
<tr><td>So'nggi 3 yil nashrlari</td><td>Qaysi usullar takrorlanadi? Mening savolimga eng yaqin maqola qaysi?</td></tr>
<tr><td>Joriy loyihalar</td><td>Loyihada magistrant uchun joy bo'lishi mumkinmi?</td></tr>
<tr><td>Guruh</td><td>Nechta magistrant va doktorant bor? Xalqaro talabalar bormi? Guruhda qaysi tilda ishlashadi?</td></tr>
</tbody></table></div>
<h4>Saralash</h4>
<ul><li>Har universitetdan 1–2 professor; jami 3–5 nomzod.</li>
<li>Har biri uchun bitta \"aloqa nuqtasi\": uning aniq maqolasi va sizning tajribangiz orasidagi bog'liqlik.</li>
<li>Universitet trekida professor tanlovi ayniqsa muhim, chunki ariza bitta universitet orqali ketadi.</li></ul>
<div class="box info">2026 GKS-G yo'riqnomasi professor bilan oldindan aloqani majburiy qilmaydi. Bu darsdagi ish moslikni tekshirish va o'quv rejasini aniqlashtirish uchun.</div>
<div class="srcs">Manba: {G26}.</div>""",
    take="Professorni so'nggi nashrlari, joriy loyihasi va guruhi bo'yicha tanlang; har biri uchun bitta aniq aloqa nuqtasi yozing.",
    task="<ul><li>3–5 professor nomzodini jadvalga yozing: universitet · laboratoriya · eng yaqin maqola · aloqa nuqtasi.</li></ul>",
    ph="1) Prof. ..., ... universiteti · maqola: ... · aloqa nuqtasi: ...")

PITCH = """<h4>60 soniyalik taqdimot</h4>
<p>Magistratura intervyusida ko'pincha birinchi savol: \"Tadqiqotingizni qisqacha tushuntiring.\" 60 soniyalik tuzilma:</p>
<ol><li><b>Muammo</b> (15 soniya): nima noma'lum yoki ishlamayapti.</li><li><b>Savol va usul</b> (20 soniya): aniq savolingiz va qanday yondashasiz.</li>
<li><b>Nega shu dastur</b> (15 soniya): laboratoriya yoki fan nomi bilan.</li><li><b>Keyin</b> (10 soniya): natija kimga foyda beradi.</li></ol>"""

MOD = dict(
    title="Professor, paket va intervyu",
    desc="GKS Lab M5-M (magistratura): professorni tanlash, professorga dastlabki xat, GKS-G shaxsiy bayonoti, izchillik auditi, intervyu va keyingi bosqich. Natija: shaxsiy bayonot, 2 professorga xat, izchillik auditi jadvali, 60 soniyalik taqdimot yozuvi.",
    lead="Oxirgi modulda aloqa va hujjatlar bir-biriga ulanadi: professorga xat, o'quv rejasini takrorlamaydigan shaxsiy bayonot, barcha hujjatlarda bir xil faktlar va intervyuda 60 soniyalik taqdimot.",
    hero="bell", weeks="3", next="", next_href="",
    goals=[("bell", "2 professorga xat", "har biri uning aniq ishiga tayangan"),
           ("memo", "Shaxsiy bayonot", "o'quv rejasini takrorlamaydi, unga zid emas"),
           ("shield", "Izchillik auditi va 60 soniyalik taqdimot", "barcha hujjatlarda bir xil faktlar")],
    warn="Xat, bayonot va taqdimotni o'zingiz yozasiz; namunalar Kompas tuzgan o'quv materiali. Sanalar va qoidalar 2026 GKS-G yo'riqnomasidan, 31.10.2026 holatiga; 2027 GKS-G yo'riqnomasi chiqqach yangilanadi.",
    lessons=[
        PROF,
        les(4, 3, t="Professorga dastlabki xat (Core)", short="Xat", body=body(4, 3) + "\n" + body(4, 4), kind="🎯 Mini-test",
            quiz=[("2026 GKS-G yo'riqnomasi professor bilan oldindan aloqani majburiy qiladi.", "n", "Noto'g'ri: majburiy emas, lekin moslikni aniqlashtiradi."),
                  ("Xat professorning aniq ishiga (maqola, yil) tayanishi kerak.", "t", "To'g'ri."),
                  ("Bir xil xatni 30 ta professorga yuborish imkonni oshiradi.", "n", "Noto'g'ri: 3–5 ta shaxsiy xat."),
                  ("Javob bo'lmasa, 7–10 ish kunidan keyin bitta eslatma yuboriladi.", "t", "To'g'ri.")],
            task="<ul><li>2 professor uchun alohida xat qoralamasini yozing (120–200 so'z, ingliz tilida).</li></ul>"),
        les(5, 2, t="GKS-G shaxsiy bayonoti", short="Bayonot", body=body(5, 1) + "\n" + body(5, 2),
            task="<ul><li>Bayonotning to'rt bloki uchun skelet yozing, keyin to'liq matnni vositaga kiriting.</li><li>O'quv rejasi bilan takrorlanayotgan joylarni belgilang va olib tashlang.</li></ul>",
            ph="Takrorlanayotgan joylar: ..."),
        les(6, 5, t="Izchillik auditi", short="Audit", quiz=None,
            body=body(6, 5) + """
<h4>To'rt hujjat bo'yicha audit</h4>
<div class="tbl"><table><thead><tr><th>Fakt</th><th>Qayerda tekshiriladi</th></tr></thead><tbody>
<tr><td>Ism, sana, baho, daraja nomi</td><td>Ariza formasi, CV, transkript, tavsiya xati</td></tr>
<tr><td>Soha, yo'nalish, dastur nomi</td><td>Bayonot, o'quv rejasi, professorga xat</td></tr>
<tr><td>Tajriba va yutuqlar</td><td>CV, bayonot, yutuqlar varaqasi (tavsiya beruvchiga berilgan)</td></tr>
<tr><td>Maqsad</td><td>Bayonot, o'quv rejasi, intervyu taqdimoti</td></tr>
</tbody></table></div>""",
            task="<ul><li>Izchillik auditi jadvalini to'ldiring: har fakt uchun qaysi hujjatlarda bor va mos keladimi.</li></ul>",
            ph="Fakt · hujjatlar · mos/mos emas · tuzatish"),
        les(8, 2, t="Intervyu va keyingi bosqich", short="Intervyu", body=PITCH + "\n" + body(8, 2) + "\n" + body(8, 5),
            task="<ul><li>60 soniyalik taqdimotni yozing va ovoz yozib mashq qiling.</li><li>B-rejangizni yozing.</li></ul>",
            ph="Taqdimot: ... B-reja: ..."),
    ],
    tool=dict(id="paket", short="Paket", h2="Xatlar, bayonot va taqdimot", sub="Yakuniy materiallar bir joyda.",
              h3="Yakuniy paket", tag="5 maydon", ic="bell", btn="Paketni saqlash", badge="Aloqachi", min=4,
              fields=[dict(k="mail1", label="1-professorga xat", type="area", wc="120-200", ph="Subject: ..."),
                      dict(k="mail2", label="2-professorga xat", type="area", wc="120-200", ph="Subject: ..."),
                      dict(k="full", label="Shaxsiy bayonot (to'liq matn)", type="area", wc="450-900", ph=""),
                      dict(k="audit", label="Izchillik auditi jadvali", type="area", ph="Fakt · hujjatlar · mos/mos emas"),
                      dict(k="pitch", label="60 soniyalik taqdimot", type="area", wc="120-170", ph="Muammo · savol va usul · nega shu dastur · keyin")]),
    check=dict(h2="Yakuniy nazorat", sub="Yuborish va intervyudan oldin.", h3="10 bandlik nazorat",
               items=["Har professorga xat uning aniq ishiga tayanadi.", "Xatlarda bitta aniq savol; kafolat so'ralmagan.",
                      "Bayonot forma bandlariga javob beradi, hajm chegarasida.", "Bayonot o'quv rejasini takrorlamaydi va unga zid emas.",
                      "Ism, baho, sana barcha hujjatlarda bir xil.", "Soha va dastur nomi barcha hujjatlarda bir xil.",
                      "Barcha muddatlar Toshkent vaqtiga o'girilgan.", "Paket yo'riqnoma tartibida, ikkinchi shaxs tekshirgan.",
                      "60 soniyalik taqdimot ovoz yozib mashq qilingan.", "B-reja yozilgan."]),
    art_title="Professor, bayonot va intervyu paketi", art_short="Paket",
    art=[("Professorlar tanlovi", ["a1"]), ("1-professorga xat", ["mail1"]), ("2-professorga xat", ["mail2", "a2"]),
         ("Shaxsiy bayonot", ["full", "a3"]), ("Izchillik auditi", ["audit", "a4"]), ("60 soniyalik taqdimot va B-reja", ["pitch", "a5"])],
    tip=lib(4)["tip"], sources=STD,
)

# Editorial source-check notice; follow the current official application guidelines.
MOD["lead"] += " <strong>Rasmiy manbani tekshiring:</strong> 2026 GKS-G qoidalarini va Oʻzbekiston uchun eʼlonni har ariza oldidan tekshiring. Muddat, hujjat va muvofiqlik talablari oʻzgarishi mumkin."
