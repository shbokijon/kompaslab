# Bakalavr v2 (2026-11-21): M1 = eski M1 + M2 + M3.2–3.3. Matn: content_v2.py; vositalar va test eski modullardan.
from common import CA, UCAS, CDS, ANABIN, DAAD_ADM, UNIPI, QS, THE, USN, HOL, STD
import v1

T = dict(v1.mod(2)["tool"])
T.update(h2="Saralangan ro'yxat", sub="Darslardagi javoblaringizni bitta ro'yxatga yig'ing: uch daraja, moslik bali, narx va ochiq savollar.",
         tag="6 maydon", fields=v1.fields(2) + v1.fields(1, ["savol"]))

MOD = dict(
    title="Qabul mantig'i va universitet ro'yxati",
    desc="Bakalavr dasturi M1: qabul komissiyasi qanday qaror qiladi, attestat xorijda, reytingni o'qish, soha va mamlakat tanlovi, uch darajali ro'yxat va arizalar byudjeti. Natija: 8–12 universitetdan iborat saralangan ro'yxat.",
    lead="", hero="compass", weeks="1–2",
    next="M2 Muddatlar va testlar rejasi", next_href="bachelor-lab-o.html?m=2",
    goals=[("compass", "Saralangan ro'yxat", "8–12 universitet, uch daraja bo'yicha"),
           ("chart", "Moslik bali", "dastur, xarajat, til, shahar bo'yicha"),
           ("scroll", "Attestat va qabul modeli", "har universitet uchun rasmiy havola bilan")],
    warn=f"Kirish talablari, testlar siyosati va reytinglar har yili yangilanadi. Bu moduldagi misollar {HOL}; o'z universitetingiz talabini uning rasmiy qabul sahifasidan tekshiring.",
    lessons=[v1.les(1, (1, 1), (1, 2)), v1.les(1, (1, 3)), v1.les(1, (1, 4), (1, 5)), v1.les(1, (3, 2), (3, 3), quiz=False),
             v1.les(1, (2, 3), (2, 4)), v1.les(1, (2, 1), (2, 2), quiz=False), v1.les(1, (2, 5))],
    tool=T,
    check=dict(h2="Ro'yxat nazorati", sub="Ro'yxatni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har universitet uchun rasmiy qabul sahifasini ochdim.", "Qabul modeli (yaxlit yoki ball asosidagi) belgilangan.",
                      "11 yillik attestat bo'yicha talab aniqlangan yoki universitetga savol yuborilgan.", "Reyting faqat saralash uchun ishlatilgan, soha bo'yicha o'rin tekshirilgan.",
                      "Ro'yxatda 8–12 universitet va uch daraja bor, ishonchli daraja bo'sh qolmagan.", "Moslik bali olti mezon bo'yicha hisoblangan.",
                      "Arizalar narxi asl valyutada yozilgan.", "Ishonchli universitetga borishga va to'lashga tayyorman."]),
    art_title="Saralangan ro'yxat", art_short="Ro'yxat",
    art=[("Qabul komissiyasi va model", ["a1"]), ("Attestat bo'yicha xulosa", ["a2"]), ("Reyting tahlili", ["a3"]), ("Soha tanlovi", ["a4"]),
         ("Mamlakatlar", ["a5"]), ("Orzu darajasi", ["orzu"]), ("Mo'ljal darajasi", ["moljal"]), ("Ishonchli daraja", ["ishonchli"]),
         ("Moslik tahlili", ["a6"]), ("Stipendiya imkoniyati", ["stip"]), ("Arizalar byudjeti", ["byudjet", "a7"]), ("Ochiq savollar", ["savol"])],
    tip="Har qatorni \"bu ma'lumotni qayerdan oldim?\" degan savol bilan tekshiring. Havolasiz qator taxmin hisoblanadi.",
    sources=f"{CA}; {UCAS}; {CDS}; {ANABIN}; {DAAD_ADM}; {UNIPI}; {QS}; {THE}; {USN}. {STD}",
)
