# Bakalavr v2 (2026-11-21): M5 = eski M9 + M10 + M3.4.
from common import CA_ESSAY, CA_FRAUD, UCAS_PS, UCAS_AI, UCAS_SIM, HOL, STD
import v1

T = dict(v1.mod(9)["tool"])
T.update(h2="Insholar: qoralama va yakuniy matn", tag="9 maydon", badge="Hikoyachi",
         sub="Qoralamadan yakuniy versiyagacha bitta joyda. Har versiyani saqlang.",
         fields=v1.fields(9) + v1.fields(10, ["yakun", "versiya", "ai", "joylash"]))

MOD = dict(
    title="Insho: yozish va tahrir",
    desc="Bakalavr dasturi M5: shaxsiy bayonot va qiziqish bayoni, hikoya va mavzu, birinchi qoralama, UCAS uch savoli, qo'shimcha insholar, tahrir va AI chegarasi.",
    lead="", hero="bulb", weeks="2–3",
    next="M6 Stipendiya va 4 yillik moliyaviy reja", next_href="bachelor-lab-o.html?m=6",
    goals=[("memo", "Yakuniy asosiy insho", "Common App, 250–650 so'z yoki motivatsion xat"),
           ("scroll", "UCAS bayonoti", "uch savol, jami 4 000 belgigacha (kerak bo'lsa)"),
           ("shield", "Tahrir qaydi va AI bayoni", "nima o'zgardi va yordamdan qanday foydalandingiz")],
    warn=f"Insho mavzulari, belgi chegaralari va AI qoidalari {HOL}; Common App va UCAS rasmiy sahifasidan tekshiring. Kompas Lab insho yozib bermaydi.",
    lessons=[v1.les(5, (9, 1), (3, 4)), v1.les(5, (9, 2)), v1.les(5, (9, 3)), v1.les(5, (9, 4)), v1.les(5, (9, 5)),
             v1.les(5, (10, 1), (10, 2), quiz=False), v1.les(5, (10, 3), (10, 4), (10, 5))],
    tool=T,
    js=v1.mod(9)["js"],
    check=dict(h2="Insho nazorati", sub="Platformaga joylashdan oldin tekshiring.", h3="9 bandlik nazorat",
               items=["Har universitet qaysi yozma hujjatni so'rashi aniq.", "Insho aniq epizoddan boshlanadi, klishe bilan boshlanmaydi.",
                      "Xususiyatlar voqea orqali ko'rsatilgan.", "Insho M3 profilimga mos.",
                      "UCAS javoblarining har biri kamida 350 belgi, jami 4 000 dan oshmaydi (kerak bo'lsa).", "1–2 kishidan aniq savollar bilan fikr olingan.",
                      "AI dan foydalanish platforma va universitet qoidalariga mos.", "Chegara platforma hisoblagichi bilan tekshirilgan, boshqa universitet nomi qolmagan.",
                      "Matn meniki: hech kim uni men uchun yozmagan."]),
    art_title="Yakuniy insholar va tahrir qaydi", art_short="Insho",
    art=[("Talab qilinadigan matnlar va qiziqish bayoni", ["a1"]), ("Mavzu va hikoya", ["a2", "a3"]), ("Common App asosiy inshosi v1", ["ca"]),
         ("UCAS 1-savol", ["uq1"]), ("UCAS 2-savol", ["uq2"]), ("UCAS 3-savol", ["uq3", "a4"]), ("Qo'shimcha insholar", ["qosh", "a5"]),
         ("Yakuniy insho", ["yakun"]), ("Tahrir qaydi", ["versiya", "a6"]), ("AI va yordam bayoni", ["ai", "a7"]), ("Platformaga joylash", ["joylash"])],
    tip="Qoralamani yozgach, uni 2–3 kun ochmang. Keyin ovoz chiqarib o'qing: qoqilgan joyingiz tahrir talab qiladi.",
    sources=f"{CA_ESSAY}; {CA_FRAUD}; {UCAS_PS}; {UCAS_AI}; {UCAS_SIM}. {STD}",
)
