from _lib import les, lib
from common import STD

V5 = lib(5)

MOD = dict(
    title="Shaxsiy bayonot",
    desc="GKS Lab M4-U (bakalavriat): GKS shaxsiy bayonoti formasi, Kimlik → Dalil → Maqsad → Moslik, birinchi qoralama, tahrir va o'zaro tahrir. Natija: yakuniy shaxsiy bayonot va tahrir qaydi.",
    lead="Bakalavriat trekida shaxsiy bayonot og'irlik markazi: komissiya sizni asosan shu matn orqali taniydi. Bu modulda uni M3-U dagi dalillardan qurasiz va baholash mezoni bilan tahrir qilasiz.",
    hero="memo", weeks="3", next="M5-U O'quv rejasi, topshirish va intervyu", next_href="gks-lab-m5-u.html",
    goals=V5["goals"], warn=V5["warn"],
    lessons=[
        les(5, 1, t="GKS shaxsiy bayonoti formasi"),
        les(5, 2, t="Kimlik → Dalil → Maqsad → Moslik"),
        les(5, 3, t="Birinchi qoralama"),
        les(5, 4, t="Tahrir"),
        les(5, 5, t="O'zaro tahrir va yakuniy versiya"),
    ],
    tool=V5["tool"], check=V5["check"], art_title=V5["art_title"], art_short=V5["art_short"], art=V5["art"],
    tip=V5["tip"], sources=STD,
)

# Editorial source-check notice; follow the current official application guidelines.
MOD["lead"] += " <strong>Rasmiy manbani tekshiring:</strong> 2027 GKS-U qoidalarini va Oʻzbekiston uchun eʼlonni har ariza oldidan tekshiring. Muddat, hujjat va muvofiqlik talablari oʻzgarishi mumkin."
