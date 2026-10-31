from _lib import les, body, lib
from common import G26, STD

V6 = lib(6)

LIT = dict(t="Adabiyot bilan ishlash minimumi", short="Adabiyot", min=50, kind="📚 12 manba", ic="books",
    hook="O'quv rejasida \"bu sohada tadqiqot kam\" deb yozish oson, isbotlash qiyin. Bo'shliqni ko'rsatish uchun kamida 10–15 manbani o'qigan bo'lishingiz kerak.",
    body="""<h4>Qidiruv</h4>
<ul><li><b>Qayerdan:</b> Google Scholar, universitet kutubxonasi, ochiq kirishli bazalar (DOAJ, arXiv, sohangizga xos preprint serverlar), tanlagan laboratoriyangizning nashrlar sahifasi.</li>
<li><b>Kalit so'zlar:</b> mavzu + usul + hudud (masalan, <span lang="en">groundwater salinity, machine learning, Central Asia</span>). Har qidiruvni yozib boring.</li>
<li><b>Zanjir:</b> bitta yaxshi maqolaning iqtiboslar ro'yxati (orqaga) va uni iqtibos qilganlar (oldinga).</li></ul>
<h4>Tez o'qish tartibi (bitta maqola, 15–20 daqiqa)</h4>
<ol><li>Annotatsiya: savol va asosiy natija.</li><li>Rasmlar va jadvallar: nima o'lchangan.</li><li>Xulosa: cheklovlar va \"kelajakdagi ishlar\" (bo'shliq ko'pincha shu yerda).</li><li>Usul bo'limi faqat kerak bo'lsa.</li></ol>
<h4>Annotatsiyalangan ro'yxat (12 manba)</h4>
<div class="tbl"><table><thead><tr><th>Ustun</th><th>Nima yoziladi</th></tr></thead><tbody>
<tr><td>Manba</td><td>Muallif, yil, sarlavha, jurnal, havola (DOI)</td></tr>
<tr><td>Savol va usul</td><td>Bir jumla</td></tr>
<tr><td>Natija</td><td>Bir jumla</td></tr>
<tr><td>Cheklov</td><td>Mualliflarning o'zi aytgan cheklov</td></tr>
<tr><td>Mening savolimga aloqasi</td><td>Bir jumla</td></tr>
</tbody></table></div>
<h4>Bo'shliqni aniqlash</h4>
<p>Bo'shliq \"hech kim o'rganmagan\" emas. Ko'pincha u: boshqa hudud yoki ma'lumot, boshqa usul, bir nechta ishdagi qarama-qarshi natija, mualliflarning o'zi aytgan cheklov. Bo'shliqni 2–3 manbaga tayanib bir jumlada yozing.</p>
<div class="box warn">Manbani o'qimasdan iqtibos qilmang va mavjud bo'lmagan manbani yozmang. Sun'iy intellekt vositalari ba'zan yo'q maqolalarni \"topadi\": har manbani DOI yoki rasmiy sahifa orqali tekshiring.</div>""",
    take="10–15 manba, tez o'qish tartibi, annotatsiyalangan ro'yxat va 2–3 manbaga tayangan bo'shliq jumlasi. Har manba tekshirilgan.",
    task="<ul><li>Kamida 12 manbali annotatsiyalangan ro'yxatni boshlang (vositadagi maydon).</li><li>Bo'shliqni bir jumlada, 2–3 manbaga tayanib yozing.</li></ul>",
    ph="Bo'shliq: ... (manba 1, manba 2)")

REV = dict(t="Tahrir va o'zaro tahrir", short="Tahrir", min=35, kind="📊 Rubric", ic="chart",
    hook="O'quv rejasini birinchi bo'lib siz sohasini bilmaydigan elchixona xodimi o'qishi mumkin. Agar u tushunmasa, keyingi bosqichdagi mutaxassisga yetib bormasligi mumkin.",
    body="""<h4>Mutaxassis bo'lmagan o'quvchi testi</h4>
<ul><li>Sohangizni bilmaydigan bitta odamga (do'st, oila a'zosi) o'qitib, 3 savol bering: men nimani o'rganmoqchiman? nega? qanday?</li>
<li>U javob bera olmasa, matnda atama ko'p yoki mantiqiy zanjir uzilgan.</li>
<li>Har maxsus atamani birinchi ishlatishda qisqa izohlang.</li></ul>
<h4>Baholash mezoni (Rubric), har biri 0–4</h4>
<div class="tbl"><table><thead><tr><th>Mezon</th><th>4 ball</th></tr></thead><tbody>
<tr><td>Forma</td><td>Har bandga javob, hajm chegarasida</td></tr>
<tr><td>Savol</td><td>O'lchanadigan va dastur muddatida javob beriladigan</td></tr>
<tr><td>Dastur bilan moslik</td><td>Aniq fan, laboratoriya yoki professor nomi bilan</td></tr>
<tr><td>Vaqt jadvali</td><td>Til yili va har semestr uchun o'lchanadigan natija</td></tr>
<tr><td>Tushunarlilik</td><td>Mutaxassis bo'lmagan o'quvchi 3 savolga javob beradi</td></tr>
</tbody></table></div>
<h4>O'zaro tahrir (Peer review)</h4>
<p>Tahrirchi mezon bo'yicha ball va izoh beradi, matnni qayta yozmaydi. Siz har izohga qaror chiqarasiz va tahrir qaydini yuritasiz.</p>""",
    take="Mutaxassis bo'lmagan o'quvchi testi + 5 mezonli rubric + o'zaro tahrir; matnni o'zingiz o'zgartirasiz.",
    task="<ul><li>Rejani mezon bo'yicha o'zingiz ballang, keyin bitta odamga o'zaro tahrirga bering.</li><li>Tahrir qaydini yozing.</li></ul>",
    ph="O'z bahoim: ... Tahrirchi: ... Qaror: ...")

MOD = dict(
    title="O'quv rejasi",
    desc="GKS Lab M4-M (magistratura): o'quv rejasining roli, tadqiqot savoli, adabiyot bilan ishlash minimumi, to'liq o'quv rejasi va o'zaro tahrir. Natija: yakuniy o'quv rejasi, semestrlar jadvali va 12 manbali annotatsiyalangan ro'yxat.",
    lead="Magistratura trekida o'quv rejasi og'irlik markazi. Bu modulda tadqiqot savolini toraytirasiz, adabiyotdan bo'shliqni topasiz va til yili bilan birga semestrlar bo'yicha reja yozasiz.",
    hero="calendar", weeks="3–4", next="M5-M Professor, paket va intervyu", next_href="gks-lab-m5-m.html",
    goals=[("calendar", "Yakuniy o'quv rejasi", "GKS formasi bo'yicha, semestrlar jadvali bilan"),
           ("books", "12 manbali annotatsiyalangan ro'yxat", "bo'shliq jumlasi bilan"),
           ("telescope", "Tadqiqot savoli", "o'lchanadigan va javob beriladigan")],
    warn=V6["warn"].replace("(2027 GKS-U da 3-forma)", "(GKS-G formalari ichida)"),
    lessons=[
        les(6, 1, t="Nega o'quv rejasi markaziy hujjat"),
        les(6, 4, t="Tadqiqot savolini shakllantirish"),
        LIT,
        les(6, 2, t="To'liq o'quv rejasi", short="Reja", kind="🎯 Mini-test", body=body(6, 2) + "\n" + body(6, 3),
            quiz=[("2026 GKS-G da magistratura 1 yil til va 2 yil dasturdan iborat.", "t", "To'g'ri."),
                  ("O'quv rejasida til yilini ko'rsatish shart emas.", "n", "Noto'g'ri: til yilini qanday o'tkazishingiz rejaning qismi."),
                  ("Rejadagi fanlar universitetning rasmiy o'quv rejasidan olinishi kerak.", "t", "To'g'ri."),
                  ("Tadqiqot savoli o'zgarishi mumkinligini rejada aytish zaiflik belgisi.", "n", "Noto'g'ri: \"dastlabki yo'nalish\" deb ko'rsatish halol.")],
            task="<ul><li>Pastdagi vositada to'liq o'quv rejasini yozing: fon → savol → metod → semestrlar → natija → uzoq muddatli maqsad.</li></ul>",
            ph="Qaydlar: ..."),
        REV,
    ],
    tool=dict(id="reja", short="Reja", h2="O'quv rejasi quruvchi", sub="Bloklar, semestrlar jadvali, manbalar va to'liq matn. So'z hisoblagichi mo'ljal; forma chegarasi ustun.",
              h3="O'quv rejasi", tag="5 maydon", ic="calendar", btn="Rejani saqlash", badge="Rejachi", min=4,
              fields=[dict(k="p1", label="Fon va bo'shliq", type="area", ph=""),
                      dict(k="p2", label="Tadqiqot savoli va metod", type="area", ph=""),
                      dict(k="p4", label="Semestrlar jadvali", hint="til yili + 4 semestr", type="area", ph="Til yili: ... 1-semestr: ..."),
                      dict(k="lit", label="Annotatsiyalangan ro'yxat", hint="12 manba", type="area", ph="Muallif, yil, sarlavha, DOI · savol · natija · cheklov · aloqasi"),
                      dict(k="pfull", label="To'liq matn", type="area", wc="500-1000", ph="")]),
    check=dict(V6["check"], items=[i for i in V6["check"]["items"] if not i.startswith(("U:", "D:"))] + ["12 manbaning har biri DOI yoki rasmiy sahifa orqali tekshirilgan."]),
    art_title="O'quv rejasi", art_short="Reja",
    art=[("Forma bandlari xaritasi", ["a1"]), ("Tadqiqot savoli", ["p2", "a2"]), ("Fon va bo'shliq", ["p1", "a3"]),
         ("Semestrlar jadvali", ["p4"]), ("Annotatsiyalangan ro'yxat", ["lit"]), ("To'liq matn", ["pfull", "a4"]), ("Tahrir qaydi", ["a5"])],
    tip=V6["tip"], sources=STD,
)

# Editorial source-check notice; follow the current official application guidelines.
MOD["lead"] += " <strong>Rasmiy manbani tekshiring:</strong> GKS-G joriy sikli qoidalarini va Oʻzbekiston uchun eʼlonni har ariza oldidan tekshiring. Muddat, hujjat va muvofiqlik talablari oʻzgarishi mumkin."
