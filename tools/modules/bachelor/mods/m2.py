# Bakalavr v2 (2026-11-21): M2 = eski M4 + M5.
from common import CA, UCAS_DATES, IELTS, TOEFL, DET, SAT, ACT, CDS, APO, HOL, STD
import v1

F = [dict(k="erta", label="Eng erta ariza muddatingiz", hint="rasmiy sahifadan; bilmasangiz taxminiy sana", type="date")]
F += v1.fields(4, ["qachon"]) + v1.fields(5, ["tiltest", "sat", "baho", "hujjat"]) + v1.fields(4, ["tracker", "xavf"])
T = dict(v1.mod(4)["tool"])
T.update(id="jadval", short="Jadval", h2="Vaqt jadvali va test kalendari", h3="Vaqt jadvali", tag="8 maydon", badge="Vaqt ustasi",
         sub="Muddatlar, testlar va hujjatlarni bitta jadvalga yig'ing. Har sanaga manba qo'ying.", fields=F, ic="calendar")

MOD = dict(
    title="Muddatlar va testlar rejasi",
    desc="Bakalavr dasturi M2: ariza oynalari (ED, EA, RD, UCAS, portallar), baholar va transkript, ingliz tili testi, SAT/ACT va test siyosati, teskari reja va maktab bilan muvozanat. Natija: vaqt jadvali va test kalendari.",
    lead="", hero="calendar", weeks="1–2",
    next="M3 Yutuqlar, faoliyat va CV", next_href="bachelor-lab-o.html?m=3",
    goals=[("calendar", "Vaqt jadvali", "eng erta muddatdan orqaga hisoblangan"),
           ("books", "Test kalendari", "til testi va SAT/ACT: sana va zaxira urinish"),
           ("chart", "Baholar jadvali", "asl shkalada, sohaga yaqin fanlar bilan")],
    warn=f"Ariza muddatlari, test siyosati va narxlar har yili o'zgaradi. Bu moduldagi sanalar {HOL}; har sanani universitet yoki test tashkilotining rasmiy sahifasidan tekshiring.",
    lessons=[v1.les(2, (4, 1)), v1.les(2, (5, 1), (5, 2), quiz=False), v1.les(2, (5, 3)), v1.les(2, (5, 4), (5, 5)),
             v1.les(2, (4, 2), (4, 3)), v1.les(2, (4, 4))],
    tool=T,
    check=dict(h2="Jadval nazorati", sub="Jadvalni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har universitet uchun ariza oynasi va muddat manba bilan yozilgan.", "ED ni tanlasam, uning majburiyatini va moliyaviy yordam qoidasini o'qidim.",
                      "Baholar asl shkalada, shkala izohi bilan yozilgan.", "Har universitet qabul qiladigan til testi tekshirilgan, qayta topshirish uchun zaxira bor.",
                      "SAT/ACT kerak yoki kerak emasligi har universitet uchun aniq.", "Teskari rejada test, tavsiya, tarjima va insho haftalari bor.",
                      "Nazorat jadvali yaratilgan va haftalik yangilash kuni belgilangan.", "Hujjatlardagi ism pasport bilan harfma-harf bir xil."]),
    art_title="Vaqt jadvali va test kalendari", art_short="Jadval",
    art=[("Eng erta muddat", ["erta"]), ("Ariza oynalari", ["qachon", "a1"]), ("Baholar va transkript", ["baho", "hujjat", "a2"]),
         ("Til testi rejasi", ["tiltest", "a3"]), ("SAT/ACT va test siyosati", ["sat", "a4"]), ("Teskari reja va nazorat jadvali", ["tracker", "a5"]),
         ("Haftalik ritm", ["a6"]), ("Xavflar va zaxira", ["xavf"])],
    tip="Test sanasini tanlaganda natija kelish muddatini ham qo'shing. Natija universitetga muddatdan oldin yetib borishi kerak.",
    sources=f"{CA}; {UCAS_DATES}; {IELTS}; {TOEFL}; {DET}; {SAT}; {ACT}; {CDS}; {APO}. {STD}",
)
