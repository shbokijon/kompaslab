from _lib import les, body, lib
from common import STD

V1 = lib(1)

MOD = dict(
    title="Hujjatlar infratuzilmasi",
    desc="GKS Lab M1: GKS hujjatlari xaritasi, apostil va tarjima, tavsiya xati (GKS formasi) va yutuqlar varaqasi, TOPIK va ingliz tili strategiyasi. Natija: hujjatlar nazorat jadvali.",
    lead="GKS arizasi bitta insho emas, o'nlab varaqdan iborat to'plam. Bu modulda yo'riqnomadagi har hujjatni bitta jadvalga tushirasiz, legallashtirish zanjirini rejalaysiz, tavsiya xatini tashkil qilasiz va til strategiyasini tanlaysiz. Uch trek uchun umumiy.",
    hero="scroll", weeks="2–3", next="M2 Universitet va dastur tanlash", next_href="gks-lab-m2.html",
    goals=[("scroll", "Hujjatlar nazorat jadvali", "har hujjat, manbasi, holati va muddati bilan"),
           ("shield", "Legallashtirish yo'l xaritasi", "apostil, tarjima va nusxa qoidasi bo'yicha"),
           ("memo", "Tavsiya beruvchi uchun varaqa va til rejasi", "yutuqlar varaqasi (Brag Sheet), TOPIK yoki ingliz tili qarori")],
    warn=V1["warn"],
    lessons=[
        les(1, 1, t="Hujjatlarning to'liq xaritasi"),
        les(1, 2, t="Apostil, tarjima va tasdiq"),
        les(4, 1, t="Tavsiya xatlari (Core + GKS formasi)", short="Tavsiya", kind="🛠 Brag Sheet", ic="memo", quiz=None,
            body=body(4, 1) + "\n<h4>Yutuqlar varaqasi (Brag Sheet)</h4>\n" + body(4, 2).split("<h4>Yutuqlar varaqasi (Brag Sheet) tarkibi</h4>", 1)[1],
            task="<ul><li>3 ta nomzod tavsiya beruvchini 4 mezon bo'yicha (0–3) ballang va bittasini tanlang.</li><li>Tanlangan tavsiya beruvchi uchun 1 sahifalik yutuqlar varaqasini yozing.</li></ul>",
            ph="Tanlov: ... Varaqa: men ..., birga: ..., yutuqlar: 1) ... 2) ..."),
        les(1, 4, t="Til strategiyasi: TOPIK va ingliz tili"),
    ],
    tool=dict(id="jadval", short="Jadval", h2="Hujjatlar nazorat jadvali", sub="Darslardagi javoblaringizni bitta jadvalga yig'ing.",
              h3="Nazorat jadvali", tag="5 maydon", ic="scroll", btn="Jadvalni saqlash", badge="Jadval ustasi", min=4,
              fields=[dict(k="trek", label="Trekingiz", type="select", opts=["U: bakalavriat (GKS-U)", "M: magistratura (GKS-G)", "D: doktorantura (GKS-G)"]),
                      dict(k="docs", label="Hujjatlar ro'yxati", hint="hujjat · kim beradi · holat · muddat · nusxa", type="area", ph="Ariza formasi · o'zim · boshlanmagan · 1-dekabr · 1"),
                      dict(k="leg", label="Legallashtirish rejasi", type="area", ph="Attestat: tarjima → apostil (my.gov.uz) → ..."),
                      dict(k="rec", label="Tavsiya beruvchi va so'rash sanasi", type="area", ph="Ism, lavozim, nega u, sana"),
                      dict(k="lang", label="Til rejasi", type="area", ph="TOPIK 3: ... sana; IELTS: ...")]),
    check=dict(h2="Hujjatlar nazorati", sub="Topshirishdan oldin har bandni tekshiring.", h3="10 bandlik nazorat",
               items=["Ro'yxat joriy sikl yo'riqnomasidan ko'chirilgan, bandma-band mos.", "Har hujjatda ism pasport bilan harfma-harf mos.",
                      "Rasmiy guvohnomalarga apostil yoki konsullik tasdig'i rejalashtirilgan.", "Notarial yoki oddiy nusxaga tayanilmagan.",
                      "Tarjimadagi fan nomlari, baho shkalasi va daraja nomi tekshirilgan.", "Tavsiya beruvchi meni aniq ish orqali biladi; xat sanasi muddatdan oldingi bir yil ichida.",
                      "Tavsiya beruvchiga faqat faktlar berilgan, tayyor matn emas.", "Til sertifikati ariza kunida amal qiladi (bo'lsa).",
                      "Legallashtirish ariza oynasidan kamida 2 oy oldin boshlanadi.", "Har hujjat uchun mas'ul va sana yozilgan."]),
    art_title="Hujjatlar nazorat jadvali", art_short="Jadval",
    art=[("Trek", ["trek"]), ("Hujjatlar ro'yxati", ["docs", "a1"]), ("Legallashtirish yo'l xaritasi", ["leg", "a2"]),
         ("Tavsiya beruvchi va yutuqlar varaqasi", ["rec", "a3"]), ("Til rejasi", ["lang", "a4"])],
    tip=V1["tip"],
    sources=STD,
)


# Editorial policy (2026-10-31): siklga bogʻliq qoidalar rasmiy NIIED
# Application Guidelines va tanlangan topshirish yoʻlining joriy eʼlonidan tekshiriladi.
# Mazkur izoh dars tarkibiga tushadi; grant yoki qabul kafolatlanmaydi.
MOD["lead"] += " <strong>Muhim:</strong> Ushbu moduldagi muddat, muvofiqlik, hujjat va tanlov shartlarini 2026 GKS-G yoʻriqnomasi hamda Oʻzbekiston uchun tegishli rasmiy eʼlon bilan solishtiring. Boshqa sikldagi qoida avtomatik amal qilmaydi. GKS Lab stipendiya yoki qabulni kafolatlamaydi."

# Editorial source-check notice; follow the current official application guidelines.
MOD["lead"] += " <strong>Rasmiy manbani tekshiring:</strong> 2026 GKS-G qoidalarini va Oʻzbekiston uchun eʼlonni har ariza oldidan tekshiring. Muddat, hujjat va muvofiqlik talablari oʻzgarishi mumkin."
