from _lib import les, body, lib
from common import G26, STD

L1 = dict(t="Bakalavrdan magistraturaga", short="Pozitsiya", min=30, kind="✍ Bayon", ic="compass",
    hook="\"Koreyada magistraturada o'qishni xohlayman\" degan nomzod ko'p. Komissiya boshqa savolga javob izlaydi: siz aynan nimani o'rganmoqchisiz va nega hozir?",
    body="""<h4>Bakalavriat va magistratura arizasi farqi</h4>
<div class="tbl"><table><thead><tr><th></th><th>Bakalavriat</th><th>Magistratura (GKS-G)</th></tr></thead><tbody>
<tr><td>Asosiy savol</td><td>Bu odam o'sadimi?</td><td>Bu odam nimani o'rganadi va uni qayerda ishlatadi?</td></tr>
<tr><td>Og'irlik markazi</td><td>Shaxsiy bayonot</td><td>O'quv rejasi</td></tr>
<tr><td>Dalil</td><td>Maktab yutuqlari, qiziqish</td><td>Kurs ishi, bitiruv ishi, amaliyot, ish tajribasi</td></tr>
<tr><td>Yo'nalish</td><td>Soha</td><td>Soha ichidagi aniq yo'nalish va dastur</td></tr>
</tbody></table></div>
<h4>Takrorlanuvchi mavzuni topish</h4>
<p>Bakalavr yillaringizdagi ishlarni yonma-yon qo'ying: kurs ishlari, bitiruv ishi, amaliyot, ishdagi loyihalar. Bir mavzu yoki usul 2–3 marta qaytadimi? Masalan, turli fanlarda hamisha ma'lumot tahlilini tanlagansiz. Shu takror sizning magistraturadagi yo'nalishingizning eng ishonchli dalili.</p>
<h4>Pozitsiya bayoni (bir jumla)</h4>
<div class="out" style="white-space:normal">Men <b>[soha]</b> bo'yicha <b>[aniq yo'nalish]</b>ni o'rganmoqchiman, chunki <b>[dalil: bakalavrdagi ish]</b> davomida <b>[ochiq qolgan savol yoki ko'nikma bo'shlig'i]</b>ga duch keldim; <b>[dastur]</b> shu bo'shliqni <b>[aniq fan yoki laboratoriya]</b> orqali yopadi.</div>
<p style="margin-top:8px">Bu Kompas tuzgan qolip. Qavslarni o'z faktlaringiz bilan to'ldiring; qolipning o'zini hujjatga ko'chirmang.</p>""",
    take="Magistratura arizasi \"nimani o'rganaman va nega hozir\" savoliga javob beradi. Bakalavr ishlaridagi takrorlanuvchi mavzu eng kuchli dalil.",
    task="<ul><li>Bakalavr ishlaringizni ro'yxat qiling va takrorlanuvchi mavzu yoki usulni toping.</li><li>Pozitsiya bayonini bir jumlada yozing.</li></ul>",
    ph="Takrorlanuvchi mavzu: ... Pozitsiya: Men ...")

L3 = dict(t="Akademik CV (Core)", short="CV", min=40, kind="🎯 Mini-test", ic="scroll",
    hook="CV komissiya ochadigan birinchi hujjatlardan biri. Ish uchun yozilgan rezyumeda ta'lim pastda, tezis umuman yo'q bo'lsa, asosiy savolga javob topilmaydi: bu odam magistraturaga tayyormi?",
    body=f"""<h4>Akademik CV va ishchi rezyume (Academic CV vs Resume)</h4>
<div class="tbl"><table><thead><tr><th></th><th>Ishchi rezyume</th><th>Akademik CV</th></tr></thead><tbody>
<tr><td>Birinchi bo'lim</td><td>Ish tajribasi yoki profil</td><td>Ta'lim</td></tr>
<tr><td>Hajm</td><td>Odatda 1 sahifa</td><td>Odatda 2 sahifagacha; universitet chegara qo'ysa, o'sha</td></tr>
<tr><td>Asosiy dalil</td><td>Savdo, KPI natijalari</td><td>Kurslar, tezis, tadqiqot tajribasi, nashr va taqdimotlar</td></tr>
</tbody></table></div>
<h4>Bo'limlar tartibi</h4>
<ol><li><b>Ta'lim:</b> daraja, universitet, yillar, baho asl shkalada (\"4.6 / 5.0\"), bitiruv ishi nomi va rahbar, 4–6 tegishli kurs.</li>
<li><b>Tadqiqot va loyiha tajribasi:</b> STAR bandlari (3.2 dagi inventardan), harakat fe'li bilan boshlanadi, natija raqam bilan.</li>
<li><b>Nashrlar va taqdimotlar</b> (bo'lsa): to'liq bibliografik ma'lumot.</li>
<li><b>Mukofotlar:</b> nomi, darajasi, yil.</li>
<li><b>Ko'nikmalar va tillar:</b> dasturiy vositalar va daraja bilan; til sertifikatlari ball va sana bilan.</li></ol>
<h4>Bitta tajriba qatori</h4>
<div class="out" style="white-space:normal"><span lang="en">Built a Python script that cleaned 4 years of well-level records (12,000 rows) and cut the monthly reporting time from 3 days to 4 hours.</span></div>
<p style="margin-top:8px">Namuna Kompas tomonidan tuzilgan; raqamlar shartli.</p>
<div class="box warn">GKS-G arizasining o'z formalari bor. CV faqat universitet yoki forma so'rasa alohida ilova qilinadi; har holda u formalardagi ma'lumot bilan bir xil bo'lishi shart.</div>
<div class="srcs">Manba: {G26}.</div>""",
    take="Akademik CV ta'limdan boshlanadi, 2 sahifagacha bo'ladi va har qatori tekshiriladigan dalil. Formalardagi ma'lumot bilan to'liq mos.",
    quiz=[("Akademik CV da birinchi bo'lim odatda ta'lim.", "t", "To'g'ri."),
          ("Bahoni CV da o'zingiz 4.0 shkalaga aylantirib yozasiz.", "n", "Noto'g'ri: asl shkalada yozing."),
          ("Tajriba qatori harakat fe'li bilan boshlanib, natijaga ega bo'lishi kerak.", "t", "To'g'ri."),
          ("CV dagi ma'lumot GKS formalaridagidan farq qilsa ham bo'ladi.", "n", "Noto'g'ri: farq ishonchni yo'qotadi.")],
    task="<ul><li>Pastdagi vositada CV ning ta'lim va tajriba bo'limlarini yozing (ingliz tilida).</li></ul>",
    ph="CV bo'yicha qaydlar: ...")

L4 = dict(t="Yo'nalish o'zgarishini asoslash", short="Ko'prik", min=30, kind="✍ Ko'prik", ic="shield",
    hook="Geologiyadan ma'lumotlar fani magistraturasiga o'tmoqchimisiz? Komissiya birinchi navbatda \"bu odam yangi sohani uddalaydimi?\" deb so'raydi. Javobni siz oldindan berishingiz kerak.",
    body="""<h4>Yo'nalish ko'prigi (uch qism)</h4>
<ol><li><b>Olib kelinadigan ko'nikma:</b> eski sohadan yangisiga o'tadigan aniq bilim yoki usul (masalan, statistik tahlil, laboratoriya amaliyoti, dala ishi).</li>
<li><b>To'ldiriladigan bo'shliq:</b> yangi soha uchun hali yetishmaydigan asos (masalan, chiziqli algebra, dasturlash).</li>
<li><b>Reja va dalil:</b> bo'shliqni yopish uchun allaqachon qilingan qadamlar (onlayn kurs + sertifikat, loyiha) va til yilida qilinadiganlar.</li></ol>
<div class="tbl"><table><thead><tr><th>Kuchsiz</th><th>Kuchli</th></tr></thead><tbody>
<tr><td>\"Geologiya qiziq emas edi, endi IT ga qiziqaman\"</td><td>\"Bitiruv ishimda quduq ma'lumotlarini tahlil qilib, Python o'rgandim; endi shu usullarni ilmiy darajada o'rganmoqchiman. Chiziqli algebra bo'shlig'ini yopish uchun ... kursini tugatdim (sertifikat).\"</td></tr>
</tbody></table></div>
<p>Jadvaldagi kuchli namuna Kompas tuzgan o'quv namunasi.</p>
<div class="box info">Yo'nalish o'zgarmagan bo'lsa, bu darsda ko'prik o'rniga \"chuqurlashtirish\" bayonini yozing: bakalavrda nima o'rgandingiz va magistraturada qaysi qismini chuqurlashtirasiz.</div>
<div class="box warn">Agar yangi soha uchun hech qanday dalil bo'lmasa, avval dalil yarating (kurs, loyiha), keyin topshiring. Dalilsiz ko'prik intervyuda birinchi savolda yiqiladi.</div>""",
    take="Ko'prik: olib kelinadigan ko'nikma, to'ldiriladigan bo'shliq, allaqachon qilingan qadamlar. Yo'nalish o'zgarmagan bo'lsa, chuqurlashtirish bayoni.",
    task="<ul><li>Yo'nalish ko'prigi (yoki chuqurlashtirish bayoni) matnini 80–120 so'zda yozing.</li></ul>",
    ph="Olib kelaman: ... Bo'shliq: ... Qadamlar: ...")

MOD = dict(
    title="Magistratura nomzodining pozitsiyasi",
    desc="GKS Lab M3-M (magistratura): bakalavrdan magistraturaga pozitsiya, dalillar inventari (STAR), akademik CV va yo'nalish o'zgarishini asoslash. Natija: STAR inventari, akademik CV v1.0, yo'nalish ko'prigi matni.",
    lead="Magistratura nomzodi o'quv rejasi bilan baholanadi, o'quv rejasi esa siz kimligingiz va nima qila olishingizga tayanadi. Bu modulda pozitsiyangizni, dalillaringizni va akademik CV ni tayyorlaysiz.",
    hero="compass", weeks="2", next="M4-M O'quv rejasi", next_href="gks-lab-m4-m.html",
    goals=[("bulb", "STAR inventari", "kamida 3 yozuv: kurs ishi, bitiruv ishi, amaliyot yoki ish"),
           ("scroll", "Akademik CV v1.0", "ta'lim oldinda, har qator dalil"),
           ("compass", "Yo'nalish ko'prigi matni", "yo'nalish o'zgargan bo'lsa; aks holda chuqurlashtirish bayoni")],
    warn="Bu modul GKS-G formalari uchun material tayyorlaydi. Formalar, hajm va til talablari joriy yo'riqnomadan (2026 GKS-G, 31.10.2026 holatiga).",
    lessons=[L1, les(3, 1, t="Dalillar inventari"), L3, L4],
    tool=dict(id="cv", short="CV", h2="Inventar va CV", sub="Eng kuchli dalillar va akademik CV ning asosiy bo'limlari.",
              h3="STAR + CV", tag="5 maydon", ic="scroll", btn="CV ni saqlash", badge="CV ustasi", min=4,
              fields=[dict(k="s1", label="1-dalil (STAR)", type="area", ph="V: ... V: ... H: ... N: ... Hujjat: ..."),
                      dict(k="s2", label="2-dalil (STAR)", type="area", ph=""),
                      dict(k="cvEdu", label="CV: Education", hint="ingliz tilida", type="area", ph="BSc in ..., University, City · 2021–2025; GPA ... / ...; Thesis: ..."),
                      dict(k="cvExp", label="CV: Research and project experience", type="area", ph="Role, organisation, years; bullet points"),
                      dict(k="bridge", label="Yo'nalish ko'prigi yoki chuqurlashtirish bayoni", type="area", wc="80-120", ph="")]),
    check=dict(h2="CV va pozitsiya nazorati", sub="Yakunlashdan oldin.", h3="10 bandlik nazorat",
               items=["Pozitsiya bir jumlada: soha, yo'nalish, dalil, dastur.", "Har STAR yozuvida shaxsiy harakat va tekshiriladigan natija bor.",
                      "CV da ta'lim birinchi, baho asl shkalada.", "Tajriba qatorlari harakat fe'li bilan boshlanadi.",
                      "Har bo'lim ichida teskari xronologiya.", "2 sahifadan oshmaydi.",
                      "Fotosurat, tug'ilgan sana kabi so'ralmagan ma'lumot yo'q.", "CV formalardagi ma'lumot bilan bir xil.",
                      "Yo'nalish ko'prigida allaqachon qilingan qadam (dalil) bor.", "Bitta imlo tizimi (British yoki American)."]),
    art_title="STAR inventari va akademik CV", art_short="CV v1.0",
    art=[("Pozitsiya bayoni", ["a1"]), ("STAR inventari", ["s1", "s2", "a2"]), ("CV: Education", ["cvEdu"]),
         ("CV: Experience", ["cvExp", "a3"]), ("Yo'nalish ko'prigi", ["bridge", "a4"])],
    tip="CV ning har qatorini o'qib, o'zingizdan so'rang: komissiya bu qatordan men haqimda qanday yangi fakt bilib oladi? Javob bo'lmasa, qator kerak emas.",
    sources=STD,
)

# Editorial source-check notice; follow the current official application guidelines.
MOD["lead"] += " <strong>Rasmiy manbani tekshiring:</strong> GKS-G joriy sikli qoidalarini va Oʻzbekiston uchun eʼlonni har ariza oldidan tekshiring. Muddat, hujjat va muvofiqlik talablari oʻzgarishi mumkin."
