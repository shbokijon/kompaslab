# Bakalavr v2 (2026-11-21): M4 = eski M8 + M6.5.
from common import CA, UCAS, APO, MYGOV, HOL, STD
import v1

T = dict(v1.mod(8)["tool"])
T.update(h2="Yutuqlar varaqasi, aloqalar va hujjatlar", tag="6 maydon",
         fields=v1.fields(8) + [dict(k="zanjir", label="Hujjatlar zanjiri", hint="asl · tarjima · notarius yoki apostil · nusxa soni", type="area",
                                     ph="Attestat: asl, tarjima, apostil, 2 nusxa. Transkript: ...")])

MOD = dict(
    title="Tavsiya xatlari va hujjatlar",
    desc="Bakalavr dasturi M4: kuchli tavsiya xati, o'qituvchidan so'rash, yutuqlar varaqasi, platformada tavsiya va maktab maslahatchisi roli, tarjima, notarius va apostil.",
    lead="", hero="memo", weeks="1–2",
    next="M5 Insho: yozish va tahrir", next_href="bachelor-lab-o.html?m=5",
    goals=[("memo", "Yutuqlar varaqasi", "tavsiya beruvchiga beriladigan faktlar va epizodlar"),
           ("bell", "2–3 tavsiya so'rovi", "kimga, qachon, qanday"),
           ("shield", "Hujjatlar zanjiri", "asl, tarjima, notarius yoki apostil, nusxa soni")],
    warn=f"Platformalardagi tavsiya tartibi va apostil yig'imi {HOL}; Common App, UCAS va gov.uz sahifalaridan qayta tekshiring.",
    lessons=[v1.les(4, (8, 1)), v1.les(4, (8, 2)), v1.les(4, (8, 3)), v1.les(4, (8, 4), (8, 5)), v1.les(4, (6, 5))],
    tool=T,
    check=dict(h2="Tavsiya nazorati", sub="So'rov yuborishdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Tavsiya beruvchilar meni aniq epizodlar orqali biladi.", "So'rov muddatdan kamida 6–8 hafta oldin.",
                      "Har biriga yutuqlar varaqasi berilgan, tayyor matn berilmagan.", "Platformada email manzillar to'g'ri kiritilgan.",
                      "Maslahatchi roli kelishilgan va zaxira odam bor.", "Tarjima kerak bo'lsa, uni men qilmayman.",
                      "Har hujjat uchun tasdiq turi (tarjima, notarius, apostil) aniqlangan.", "Apostil zanjiri muddatdan 8–10 hafta oldin boshlanadi."]),
    art_title="Yutuqlar varaqasi, aloqalar jadvali va hujjatlar zanjiri", art_short="Varaqa",
    art=[("Tavsiya beruvchilar tanlovi", ["a1"]), ("1-tavsiya beruvchi", ["t1"]), ("2-tavsiya beruvchi", ["t2"]), ("Maslahatchi yoki 3-tavsiya", ["t3", "a4"]),
         ("So'rov", ["a2"]), ("Yutuqlar varaqasi", ["brag", "a3"]), ("Eslatma va rahmat", ["eslatma"]), ("Hujjatlar zanjiri", ["zanjir", "a5"])],
    tip="O'qituvchiga so'rovni tanaffusda yo'l-yo'lakay emas, oldindan kelishilgan qisqa uchrashuvda ayting.",
    sources=f"{CA}; {UCAS}; {APO}; {MYGOV}. {STD}",
)
