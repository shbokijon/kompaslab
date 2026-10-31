from _lib import les, body, lib
from common import U27, JA, STD

PLAN = f"""<p>O'quv rejasi (2027 GKS-U da 3-forma) Koreyada vaqtingizni qanday o'tkazishingizni ko'rsatadi. Bakalavriatda tadqiqot savoli talab qilinmaydi: komissiya aniq vaqt, aniq fanlar va bitiruvdan keyingi aniq yo'lni ko'rmoqchi. Ingliz yoki koreys tilida yoziladi.</p>
<h4>Hozirgi holat → Bo'shliq → Strategiya → Vaqt</h4>
<div class="tbl"><table><thead><tr><th>Qism</th><th>Bakalavriatda nimani yozasiz</th></tr></thead><tbody>
<tr><td><b>Hozirgi holat</b></td><td>Kuchli fanlaringiz, til darajangiz, M3-U dagi eng kuchli dalil</td></tr>
<tr><td><b>Bo'shliq</b></td><td>Maqsadingiz uchun hali yetishmaydigan bilim va ko'nikma</td></tr>
<tr><td><b>Strategiya</b></td><td>Dasturdagi aniq fanlar, to'garak, laboratoriya yoki amaliyot bu bo'shliqni qanday yopadi</td></tr>
<tr><td><b>Vaqt</b></td><td>Til yili va har kurs uchun reja</td></tr>
</tbody></table></div>
<h4>Vaqt jadvali</h4>
<p>2027 GKS-U: 1 yil koreys tili, keyin yo'nalishga qarab 4–6 yil bakalavriat. TOPIK 5 yoki 6 bilan til kursidan ozod bo'linadi; til kursining birinchi 6 oyida 5–6 darajani olsangiz, qolgan 6 oydan ozod qilinasiz.</p>
<div class="tbl"><table><thead><tr><th>Davr</th><th>O'qish</th><th>O'lchanadigan natija</th></tr></thead><tbody>
<tr><td>Til yili</td><td>Koreys tili kursi; sohaga oid lug'at</td><td>TOPIK maqsad darajasi va sanasi</td></tr>
<tr><td>1–2-kurs</td><td>Asosiy fanlar (dastur o'quv rejasidan nomi bilan)</td><td>Baho maqsadi, to'garak yoki loyiha</td></tr>
<tr><td>3-kurs</td><td>Ixtisoslik fanlari, amaliyot yoki laboratoriya</td><td>Amaliyot, birinchi loyiha</td></tr>
<tr><td>4-kurs</td><td>Bitiruv ishi yoki loyiha</td><td>Himoya, keyingi qadam (ish yoki magistratura)</td></tr>
</tbody></table></div>
<h4>Bitiruvdan keyingi yo'l</h4>
<p>Aniq soha va lavozim turini yozing va u shaxsiy bayonotdagi maqsad bilan bir xil bo'lsin. Fanlar va laboratoriyalar universitetning rasmiy o'quv rejasidan olinsin: mavjud bo'lmagan fanni yozish moslik dalilini buzadi.</p>
<div class="srcs">Manba: {U27}; {JA}.</div>"""

TIMELINE = f"""<h4>2027 GKS-U jadvali (31.10.2026 holatiga, Koreya vaqti)</h4>
<ul><li>Elchixona treki: onlayn ariza 15.09.2026, 11:00 – 30.09.2026, 18:00; hujjatlar NIIED ga 30-oktabrgacha.</li>
<li>Universitet treki: muddatni universitet belgilaydi (2026-yil noyabrigacha); hujjatlar NIIED ga 30-noyabrgacha.</li>
<li>Koreya vaqti Toshkentdan 4 soat oldinda: KST 18:00 Toshkentda 14:00.</li></ul>
<div class="srcs">Manba: {U27}.</div>
"""

MOD = dict(
    title="O'quv rejasi, topshirish va intervyu",
    desc="GKS Lab M5-U (bakalavriat): bakalavr o'quv rejasi, paketni yig'ish va ikkinchi shaxs tekshiruvi, elchixona intervyusi va natijadan keyingi qadamlar. Natija: o'quv rejasi, yig'ilgan paket va intervyu javoblari.",
    lead="Oxirgi qadam: o'quv rejasini yozasiz, butun paketni yo'riqnoma tartibida yig'asiz, intervyuga hujjatlaringiz asosida tayyorlanasiz va natijadan keyingi yo'lni rejalaysiz.",
    hero="calendar", weeks="3", next="", next_href="",
    goals=[("calendar", "O'quv rejasi", "til yili va 4 kurs bo'yicha, bitiruvdan keyingi yo'l bilan"),
           ("scroll", "Yig'ilgan paket", "yo'riqnoma tartibida, ikkinchi shaxs tekshiruvi bilan"),
           ("bulb", "Intervyu javoblari", "5 asosiy savolga kalit so'zlar va misol")],
    warn="Sanalar va qoidalar 2027 GKS-U yo'riqnomasidan, 31.10.2026 holatiga. Intervyu shakli va vaqti rasmiy xabardan olinadi; viza va jo'nash talablari taklifnoma va Koreya elchixonasi e'lonidan.",
    lessons=[
        dict(t="Bakalavr o'quv rejasi", short="Reja", min=45, kind="🗓 Jadval", ic="calendar",
             hook="Bakalavriat o'quv rejasida tadqiqot savoli kerak emas, lekin \"yaxshi o'qiyman\" ham yetmaydi. Komissiya til yilining birinchi oyidan bitiruvgacha yo'lingizni ko'rmoqchi.",
             body=PLAN,
             take="O'quv rejasi: hozirgi holat → bo'shliq → strategiya → vaqt; til yili va har kurs uchun aniq fan va natija; maqsad bayonot bilan bir xil.",
             task="<ul><li>Pastdagi vositada o'quv rejasi bloklarini to'ldiring.</li><li>Dastur o'quv rejasidan 4–6 fanni nomi bilan yozing va har biri maqsadingizga qanday xizmat qilishini bir jumlada ayting.</li></ul>",
             ph="Fanlar: 1) ... → ..."),
        les(7, 2, t="Paketni yig'ish va nazorat", short="Paket",
            body=TIMELINE + body(7, 2) + "\n" + body(7, 3),
            quiz=lib(7)["lessons"][0]["quiz"][:3] + [("2027 GKS-U da hujjatlar NIIED ga elchixona trekida 30-oktabrgacha yetib borishi kerak.", "t", "To'g'ri.")],
            task="<ul><li>Paket ro'yxatini fayl nomlari bilan yozing: raqam · fayl nomi · asl yoki nusxa · holat.</li><li>Ikkinchi shaxs tekshiruvchini va sanani belgilang.</li></ul>"),
        les(8, 2, t="Intervyu", short="Intervyu", body=body(8, 1) + "\n" + body(8, 2)),
        les(8, 5, t="Natijadan keyin", short="Natija",
            body=body(8, 3) + "\n" + body(8, 4) + "\n" + body(8, 5),
            task="<ul><li>Natija va universitet tanlovi sanalarini Toshkent vaqtiga o'girib yozing.</li><li>Jo'nash oldi ro'yxatini va B-rejangizni yozing.</li></ul>",
            ph="Sanalar: ... Jo'nash: ... B-reja: ..."),
    ],
    tool=dict(id="yakun-u", short="Yakun", h2="Reja, paket va intervyu", sub="O'quv rejasi, paket ro'yxati va asosiy intervyu javoblari bir joyda.",
              h3="Yakuniy paket", tag="5 maydon", ic="calendar", btn="Paketni saqlash", badge="Topshiruvchi", min=4,
              fields=[dict(k="p1", label="O'quv rejasi: hozirgi holat va bo'shliq", type="area", ph=""),
                      dict(k="p2", label="O'quv rejasi: til yili va kurslar jadvali", type="area", ph="Til yili: ... 1–2-kurs: ..."),
                      dict(k="p3", label="Bitiruvdan keyingi yo'l", type="area", ph=""),
                      dict(k="pk", label="Paket ro'yxati", hint="raqam · fayl nomi · asl/nusxa · holat", type="area", ph=""),
                      dict(k="q2", label="Intervyu: nega Koreya, nega shu universitet", type="area", ph="Javob · misol · bog'lash")]),
    check=dict(h2="Topshirish nazorati", sub="\"Yuborish\" va intervyudan oldin.", h3="10 bandlik nazorat",
               items=["O'quv rejasidagi fanlar universitetning rasmiy o'quv rejasidan.", "Til yili aniq maqsad va sana bilan.",
                      "Bayonot va reja maqsadda bir-biriga zid emas.", "Barcha muddatlar Toshkent vaqtiga o'girilgan.",
                      "Paket yo'riqnoma tartibida; skanerlar aniq; fayl nomlari tushunarli.", "Imzo talab qilingan har forma imzolangan.",
                      "Ikkinchi shaxs tekshiruvi o'tkazilgan.", "Har asosiy intervyu savoliga kalit so'z va misol bor.",
                      "Kamida 3 javob ovoz yozib mashq qilingan.", "B-reja yozilgan."]),
    art_title="O'quv rejasi, paket va intervyu javoblari", art_short="Yakun",
    art=[("O'quv rejasi", ["p1", "p2", "a1"]), ("Bitiruvdan keyingi yo'l", ["p3"]), ("Paket ro'yxati", ["pk", "a2"]),
         ("Intervyu javoblari", ["q2", "a3"]), ("Natija, jo'nash va B-reja", ["a4"])],
    tip=lib(8)["tip"], sources=STD,
)

# Editorial source-check notice; follow the current official application guidelines.
MOD["lead"] += " <strong>Rasmiy manbani tekshiring:</strong> 2027 GKS-U qoidalarini va Oʻzbekiston uchun eʼlonni har ariza oldidan tekshiring. Muddat, hujjat va muvofiqlik talablari oʻzgarishi mumkin."
