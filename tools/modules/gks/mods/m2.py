from _lib import les, body, lib
from common import U27, G26, STD

V2 = lib(2)

FILTER = f"""<p>Kuchli nomzodlar ham ko'pincha mazmun emas, takrorlanadigan oddiy xatolar sababli yo'qotadi. Universitet tanlovi va hujjatlarni boshlashdan oldin shu filtrni bilib oling: keyingi modullarda har hujjat undan o'tadi.</p>
<div class="tbl"><table><thead><tr><th>Xato</th><th>Qanday ko'rinadi</th><th>Tuzatish</th></tr></thead><tbody>
<tr><td><b>Shablon matn</b></td><td>Boshqa universitet nomi qolgan, \"[University name]\" kabi qavslar, hamma universitetga bir xil jumla</td><td>Har tanlov uchun alohida moslik dalili (2.3)</td></tr>
<tr><td><b>Mubolag'a</b></td><td>\"Eng iqtidorli\", \"mamlakatimni o'zgartiraman\"</td><td>Sifatni faktga almashtirish</td></tr>
<tr><td><b>Tekshirilmaydigan da'vo</b></td><td>Hujjati yo'q mukofot, aniq bo'lmagan \"yuqori natija\"</td><td>Har raqam yoniga hujjat</td></tr>
<tr><td><b>Format xatosi</b></td><td>Forma o'zgartirilgan, hajm oshgan, imzo yo'q, skaner o'qilmaydi</td><td>Forma shablonida yozish, yo'riqnoma bilan solishtirish</td></tr>
<tr><td><b>Kech hujjat</b></td><td>Apostil, tavsiya yoki sertifikat muddatga ulgurmagan</td><td>Teskari taqvim (M1 jadvali)</td></tr>
<tr><td><b>Mos kelmaydigan yo'nalish</b></td><td>Diplom sohasi, tanlangan dastur va bayonotdagi maqsad bir-biriga ulanmaydi</td><td>Yo'nalish ko'prigi yoki boshqa dastur</td></tr>
</tbody></table></div>
<div class="box warn">Bu jadval Kompas tahlili: NIIED rad sabablari ro'yxatini e'lon qilmaydi. Lekin har band yo'riqnoma talablariga (forma, muddat, apostil, haqiqiylik) bevosita bog'liq.</div>
<div class="srcs">Manba: {U27}; {G26}.</div>"""

MOD = dict(
    title="Universitet va dastur tanlash",
    desc="GKS Lab M2: GKS universitetlari tizimi (yo'llar, A/B turlari, kvota), saralangan ro'yxat, ilmiy moslik va keng tarqalgan xatolar filtri. Natija: 3 ta asoslangan universitet tanlovi.",
    lead="GKS da universitet tanlovi qoidalar bilan cheklangan: qaysi yo'l, nechta universitet, qaysi turdan. Bu modulda shu qoidalar ichida o'zingizga mos 3 ta tanlovni dalil bilan asoslaysiz. Uch trek uchun umumiy; M3 dan boshlab o'z trekingizga o'tasiz.",
    hero="telescope", weeks="2–3", next="trekingizning M3 moduli", next_href="gks-lab-dastur.html",
    goals=V2["goals"], warn=V2["warn"],
    lessons=[
        les(2, 1, t="GKS universitetlari tizimi", short="Tizim",
            body=body(2, 1) + "\n" + body(2, 2),
            task="<ul><li>Ikki yo'lni o'z holatingizga qo'yib solishtiring va bittasini tanlang.</li><li>Joriy (yoki eng so'nggi) yo'riqnoma ilovasidan sohangiz bo'yicha 6–8 universitetni yozing va har birining turini (A/B) belgilang.</li></ul>",
            ph="Yo'l: ... Sabab: ... Universitetlar: 1) ... (A) 2) ... (B)"),
        les(2, 4, t="Saralangan ro'yxat", short="Ro'yxat",
            body=body(2, 4) + "\n" + body(2, 5)),
        les(2, 3, t="Ilmiy moslik", short="Moslik"),
        dict(t="Keng tarqalgan xatolar filtri", short="Filtr", min=25, kind="🔍 Filtr", ic="shield",
             hook="Komissiya bir xil xatoni yuzlab arizada ko'radi. Ular sizning arizangizni o'qishni shu xato bilan to'xtatmasligi kerak.",
             body=FILTER,
             take="Olti xato: shablon, mubolag'a, dalilsiz da'vo, format, kechikish, mos kelmaydigan yo'nalish. Har hujjat shu filtrdan o'tadi.",
             task="<ul><li>Saralangan uchta tanlovingizni filtrdan o'tkazing: qaysi xato xavfi bor va uni qanday oldini olasiz?</li></ul>",
             ph="Tanlov 1: xavf ... oldini olish ..."),
    ],
    tool=V2["tool"], check=V2["check"],
    art_title=V2["art_title"], art_short=V2["art_short"],
    art=[("Ariza yo'li va universitetlar ro'yxati", ["yol", "a1"]), ("1-tanlov", ["u1t", "u1"]), ("2-tanlov", ["u2t", "u2"]), ("3-tanlov", ["u3t", "u3"]),
         ("Saralangan ro'yxat va ballar", ["a2", "a3"]), ("Xavf izohi va xatolar filtri", ["xavf", "a4"])],
    tip=V2["tip"], sources=STD, js=V2["js"],
)

# Editorial source-check notice; follow the current official application guidelines.
MOD["lead"] += " <strong>Rasmiy manbani tekshiring:</strong> 2026 GKS-G qoidalarini va Oʻzbekiston uchun eʼlonni har ariza oldidan tekshiring. Muddat, hujjat va muvofiqlik talablari oʻzgarishi mumkin."
