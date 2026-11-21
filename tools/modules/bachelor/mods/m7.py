# Bakalavr v2 (2026-11-21): M7 = eski M13 + M14 (bitta dars).
from common import CA, UCAS, UCAS_INT, UNIASSIST, UNIVERSITALY, CAMPUSCHINA, SIC, NUS, NTU, MOE_SG, IT_VISA, HOL, STD
import v1

T = dict(v1.mod(13)["tool"])
T.update(tag="5 maydon", fields=v1.fields(14, ["yon"]) + v1.fields(13))

MOD = dict(
    title="Topshirish: platformalar va mamlakat yo'llari",
    desc="Bakalavr dasturi M7: Common App, UCAS, universitet portallari, Xitoy, Italiya va Singapur yo'llari, fayllar va topshirishdan oldingi 40 bandli tekshiruv. Natija: kamida bitta topshirilgan ariza.",
    lead="", hero="scroll", weeks="1–2",
    next="M8 Intervyu, qaror va jo'nash", next_href="bachelor-lab-o.html?m=8",
    goals=[("scroll", "Topshirilgan ariza", "tasdiq xati saqlangan"),
           ("shield", "40 bandli nazorat ro'yxati", "har ariza oldidan"),
           ("calendar", "Kuzatuv rejasi", "portal, email, hujjat holati")],
    warn=f"Platforma bo'limlari, to'lovlar va muddatlar {HOL}; joriy yil sahifasidan tekshiring.",
    lessons=[v1.les(7, (13, 1)), v1.les(7, (13, 2)), v1.les(7, (13, 3)), v1.les(7, (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), quiz=False),
             v1.les(7, (13, 4), (13, 5))],
    tool=T,
    check=v1.mod(13)["check"],
    art_title="Arizalar jurnali", art_short="Jurnal",
    art=[("Common App", ["a1"]), ("UCAS", ["a2"]), ("Universitet portallari", ["a3"]), ("Mamlakat yo'li", ["yon", "a4"]),
         ("Topshirilgan arizalar", ["topsh", "a5"]), ("Hujjatlar holati", ["holat"]), ("Portallar", ["portal"]), ("Topilgan va tuzatilgan xatolar", ["xato"])],
    tip="Topshirish tugmasini bosishdan oldin bir kecha uxlang. Ertalab ko'rib chiqish sahifasini yana bir bor o'qing.",
    sources=f"{CA}; {UCAS}; {UCAS_INT}; {UNIASSIST}; {UNIVERSITALY}; {CAMPUSCHINA}; {SIC}; {NUS}; {NTU}; {MOE_SG}; {IT_VISA}. {STD}",
)
