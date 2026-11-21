# Bakalavr v2 (2026-11-21): M6 = eski M11 + M12. Koreya/Yaponiya tafsiloti GKS dasturida, AQSh formalari USA dasturida.
from common import SIK, MEXT, CAMPUSCHINA, SH, SH_UZ, DSU, TB, CSS, CDS, FTC, HOL, STD
import v1

T = dict(v1.mod(12)["tool"])
T.update(h2="4 yillik moliyaviy reja", tag="6 maydon",
         fields=v1.fields(11, ["s13"]) + v1.fields(12))

MOD = dict(
    title="Stipendiya va 4 yillik moliyaviy reja",
    desc="Bakalavr dasturi M6: stipendiya manbalari va muvofiqlik, davlat stipendiyalari saralash jadvali, universitet yordami va grantlari, to'liq xarajat modeli, 4 yillik reja va firibgarlikdan himoya.",
    lead="", hero="money", weeks="1–2",
    next="M7 Topshirish: platformalar va mamlakat yo'llari", next_href="bachelor-lab-o.html?m=7",
    goals=[("money", "4 yillik moliyaviy reja", "har yil: xarajat, qoplanadigan qism, bo'shliq"),
           ("shield", "Stipendiyalar saralashi", "2–3 ustuvor dastur, muvofiqlik bilan"),
           ("chart", "To'liq xarajat modeli", "o'qish, yashash, sug'urta, viza, yo'l")],
    warn=f"Stipendiya shartlari, kvotalar, muddatlar va narxlar har sikl o'zgaradi. Bu moduldagi ma'lumot {HOL}; har dasturni joriy rasmiy e'londan tekshiring.",
    lessons=[v1.les(6, (11, 1)), v1.les(6, (11, 2), (11, 3), (11, 4), (11, 5), quiz=False), v1.les(6, (12, 2), (12, 1), quiz=False),
             v1.les(6, (12, 3)), v1.les(6, (12, 4)), v1.les(6, (12, 5))],
    tool=T,
    js=v1.mod(12)["js"],
    check=dict(h2="Reja nazorati", sub="Rejani yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har stipendiya rasmiy saytdan olingan, Telegram e'lonidan olinmagan.", "Muvofiqlik har dastur uchun tekshirilgan.",
                      "Majburiyatlar (qaytish, til yili, soha) o'qilgan.", "Universitet stipendiyasining davomiyligi va baho sharti o'qilgan.",
                      "Xarajat 8 qator bo'yicha, asl valyutada va manba bilan hisoblangan.", "4 yilning har biri uchun bo'shliq hisoblangan.",
                      "Valyuta stsenariysi va zaxira bor, talaba ishi asosiy manba qilinmagan.", "Hech qanday agentga to'lov qilinmaydi."]),
    art_title="4 yillik moliyaviy reja", art_short="Reja",
    art=[("Stipendiya manbalari", ["a1"]), ("Ustuvor stipendiyalar", ["s13", "a2"]), ("Universitet va valyuta", ["uni"]), ("Universitet yordami", ["a3"]),
         ("To'liq xarajat modeli", ["xarajat", "a4"]), ("Manbalar", ["manba"]), ("4 yillik hisob", ["plan4", "a5"]), ("Zaxira va valyuta", ["zaxira"]),
         ("Firibgarlikdan himoya", ["himoya", "a6"])],
    tip="Moliyaviy rejani raqamlar bilan, ota-onangiz bilan birga ko'rib chiqing.",
    sources=f"{SIK}; {MEXT}; {CAMPUSCHINA}; {SH}; {SH_UZ}; {DSU}; {TB}; {CSS}; {CDS}; {FTC}. {STD}",
)
