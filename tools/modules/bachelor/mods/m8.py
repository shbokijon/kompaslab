# Bakalavr v2 (2026-11-21): M8 = eski M15 + M16.
from common import UCAS, SIK, TB, US_VISA, US_SEVIS, UK_VISA, DE_VISA, IT_VISA, KR_VISA, HOL, STD
import v1

F = v1.fields(15) + [dict(k="jonash", label="Jo'nash sanangiz", hint="taxminiy bo'lsa ham", type="date")] + v1.fields(16, ["viza", "uy", "royxat", "yil"])
T = dict(v1.mod(15)["tool"])
T.update(h2="Intervyu javoblari va jo'nash rejasi", tag="10 maydon", fields=F)

MOD = dict(
    title="Intervyu, qaror va jo'nash",
    desc="Bakalavr dasturi M8: intervyu turlari, \"o'zingiz haqingizda\" javobi, akademik intervyu, yozib olish va baholash, qabul, rad va kutish ro'yxati, qabul xati va talaba vizasi, uy-joy, sug'urta va birinchi yil.",
    lead="", hero="bell", weeks="2",
    next="", next_href="",
    goals=[("bell", "3 ta yozib olingan javob", "o'zingiz haqingizda, akademik masala, motivatsiya"),
           ("compass", "Qaror jadvali", "bir nechta taklif, kutish ro'yxati yoki rad bo'lsa"),
           ("shield", "Jo'nash ro'yxati", "viza, uy-joy, sug'urta, 30 kun, birinchi yil")],
    warn=f"Viza talablari va to'lovlari {HOL}; har mamlakatning rasmiy viza sahifasidan tekshiring. Viza qarorini konsullik chiqaradi.",
    lessons=[v1.les(8, (15, 1), (15, 2)), v1.les(8, (15, 3)), v1.les(8, (15, 4)), v1.les(8, (15, 5)),
             v1.les(8, (16, 1), (16, 2), quiz=False), v1.les(8, (16, 3), (16, 4), (16, 5))],
    tool=T,
    js=v1.mod(15)["js"],
    check=dict(h2="Jo'nash nazorati", sub="Natija va jo'nashdan oldin tekshiring.", h3="9 bandlik nazorat",
               items=["3 ta javob yozib olingan va mezon bilan baholangan.", "Eng zaif 2 band tuzatilib, qayta yozilgan.",
                      "Qaror jadvali mezonlari natijalardan oldin yozilgan.", "Javob va depozit muddatlari xatdan o'qilgan.",
                      "Qabul sharti bajarilgan, depozit rasmiy kanal orqali to'langan.", "Viza bosqichlari rasmiy sahifadan, sanalar bilan yozilgan.",
                      "Uy-joy tasdiqlangan va sug'urta talabi bajarilgan.", "Asl hujjatlar qo'l yukida, skan nusxalar bulutda.",
                      "Elchixona va favqulodda aloqalar yozilgan."]),
    art_title="Intervyu tayyorgarligi va jo'nash rejasi", art_short="Jo'nash",
    art=[("Intervyu turlari", ["a1"]), ("O'zingiz haqingizda", ["j1"]), ("Akademik masala", ["j2", "a2"]), ("Nega shu dastur", ["j3"]),
         ("Mezon natijalari", ["rb", "a3"]), ("Qaror jadvali", ["qaror", "a4"]), ("Zaxira reja", ["zaxira"]), ("Jo'nash sanasi", ["jonash"]),
         ("Viza bosqichlari", ["viza", "a5"]), ("Uy-joy va sug'urta", ["uy"]), ("30 kunlik ro'yxat", ["royxat", "a6"]), ("Birinchi yil rejasi", ["yil"])],
    tip="Intervyudan keyin 10 daqiqa ichida berilgan savollarni yozib qo'ying. Keyingi intervyuga eng yaxshi tayyorgarlik shu.",
    sources=f"{UCAS}; {SIK}; {TB}; {US_VISA}; {US_SEVIS}; {UK_VISA}; {DE_VISA}; {IT_VISA}; {KR_VISA}. {STD}",
)
