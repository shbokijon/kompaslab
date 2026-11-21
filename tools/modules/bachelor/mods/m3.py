# Bakalavr v2 (2026-11-21): M3 = eski M3.1, M3.5, M6.1–6.4, M7.
from common import CA, HOL, STD
import v1

T = dict(v1.mod(7)["tool"])
T.update(h2="Faoliyatlar ro'yxati va CV", tag="10 maydon", badge="Profil me'mori",
         sub="Profil, 10 ta faoliyat va CV bo'limlarini bitta joyga yig'ing.",
         fields=v1.fields(3, ["profil"]) + v1.fields(7, ["f13", "f46", "f710", "xarita"]) + v1.fields(6, ["ism", "talim", "yutuq", "loyiha", "konikma"]) + v1.fields(7, ["reja"]))

MOD = dict(
    title="Yutuqlar, faoliyat va CV",
    desc="Bakalavr dasturi M3: bir jumlali profil, darsdan tashqari faoliyat, olimpiada, kurs va loyiha, yetakchilik, Common App faoliyatlar ro'yxati, STAR usulidagi CV va izchil hikoya xaritasi.",
    lead="", hero="seedling", weeks="2",
    next="M4 Tavsiya xatlari va hujjatlar", next_href="bachelor-lab-o.html?m=4",
    goals=[("seedling", "10 ta faoliyat yozuvi", "har biri 150 belgigacha, natija bilan"),
           ("memo", "Bakalavr CV", "1–2 sahifa, har band STAR usulida"),
           ("compass", "Izchil hikoya xaritasi", "fanlar, faoliyat, insho va tavsiya bitta yo'nalishda")],
    warn=f"Platformalar formati (belgi chegarasi, faoliyatlar soni) {HOL}; ariza yili Common App va universitet sahifasidan tekshiring. Har yutuq va raqam hujjat yoki guvoh bilan tasdiqlanadigan bo'lsin.",
    lessons=[v1.les(3, (3, 1)), v1.les(3, (7, 1)), v1.les(3, (6, 1), (6, 2), (6, 3), (7, 2), quiz=False), v1.les(3, (7, 3), (7, 4)),
             v1.les(3, (7, 5)), v1.les(3, (6, 4)), v1.les(3, (3, 5))],
    tool=T,
    js=v1.mod(7)["js"],
    check=dict(h2="Profil nazorati", sub="Ro'yxat va CV ni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Profil bitta jumla va unda ikkita dalil bor.", "Ro'yxat muhimlik tartibida, har tavsif fe'l bilan boshlanadi.",
                      "Tavsiflar 150 belgidan oshmaydi va natija yoki raqam bor.", "Soat va yillar real, oshirilmagan.",
                      "Oilaviy majburiyat va ish ham hisobga olingan.", "CV 1–2 sahifa, har band natijani ko'rsatadi.",
                      "Yutuqlar nomi, daraja, natija va yil bilan yozilgan.", "Izchil hikoya jadvalidagi eng zaif ustun aniqlangan."]),
    art_title="Faoliyatlar ro'yxati, CV va hikoya xaritasi", art_short="Profil",
    art=[("Bir jumlali profil", ["profil", "a1"]), ("Faoliyatlar 1–3", ["f13"]), ("Faoliyatlar 4–6", ["f46"]), ("Faoliyatlar 7–10", ["f710"]),
         ("Yutuqlar va loyihalar", ["yutuq", "loyiha", "a3"]), ("Yetakchilik", ["a4"]), ("Ism va aloqa", ["ism"]), ("Ta'lim", ["talim"]),
         ("Ko'nikmalar", ["konikma"]), ("CV qatorlari (STAR)", ["a6"]), ("Izchil hikoya xaritasi", ["xarita", "a7"]), ("Keyingi 6 oy rejasi", ["reja"])],
    tip="Tavsifni yozib bo'lgach, undan bitta so'zni olib tashlang. Ma'no o'zgarmasa, so'z ortiqcha edi.",
    sources=f"{CA}. {STD}",
)
