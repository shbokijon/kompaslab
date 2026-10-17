# Generator chiqargan Lab sahifalariga keyinroq qoʻshilgan umumiy qismlarni qoʻshadi:
# logotip, favicon/PWA, havola rasmi (og:image), jonli panel, "Ilovani oʻrnatish",
# M0 tugmalari (modul fayli mavjud boʻlsa). Takror ishga tushirilsa ham natija oʻzgarmaydi.
import re
from pathlib import Path

HEAD = """<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="img/brand/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="img/brand/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Kompas Lab">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<script src="js/pwa.js" defer></script>
<link rel="stylesheet" href="css/brand.css">
<meta property="og:image" content="https://www.kompaslab.uz/img/brand/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Kompas Lab logotipi: Kuzatuvdan kashfiyotga">
<meta name="twitter:card" content="summary_large_image">
"""
LOGO = '<span class="klogo"><img class="klogo-b" src="img/brand/logo-base.webp" alt="" width="128" height="128"><img class="klogo-a" src="img/brand/logo-arrow.webp" alt="" width="128" height="128"></span>'
TG = '<a href="https://t.me/kompaslab" target="_blank" rel="noopener">Telegram</a>'

# Lab sahifasi -> M0 moduli
M0 = {
    "bachelor-lab.html": "bachelor-lab-m0.html", "master-lab.html": "master-lab-m0.html",
    "phd-lab.html": "phd-lab-m0.html", "gks-lab.html": "gks-lab-m0.html", "usa-lab.html": "usa-lab-m0.html",
    "tadbirkor-talaba.html": "tadbirkor-talaba-m0.html", "musofir-lab.html": "musofir-lab-m0.html",
}
# Musofir M0 hamma uchun ochiq: matnni shunga moslash
MUSOFIR_TEXT = [
    ("M0 roʻyxatdan oʻtmasdan ochiq boʻladi.", "M0 roʻyxatdan oʻtmasdan ochiq."),
    ("M0 hamma uchun bepul va roʻyxatdan oʻtmasdan ochiq boʻladi.", "M0 hamma uchun bepul va roʻyxatdan oʻtmasdan ochiq."),
    ('<div class="pay-status"><span>⏳</span><span><b>M0 tayyorlanmoqda, onlayn toʻlov hali ochilmagan.</b> Ochilganda kutish roʻyxatidagilarga xabar beramiz.</span></div>',
     '<div class="pay-status"><span>✅</span><span><b>M0 ochiq va bepul. Onlayn toʻlov hali ochilmagan.</b> M1–M7 ochilganda kutish roʻyxatidagilarga xabar beramiz.</span></div>'),
    ("M0 ochilganda xabar olish uchun kutish roʻyxatiga yoziling.", "M1–M7 ochilganda xabar olish uchun kutish roʻyxatiga yoziling."),
    ("bepul M0 ochilganda xabar beramiz.", "M1–M7 ochilganda xabar beramiz."),
]


def process(path: Path, root: Path) -> None:
    s = path.read_text(encoding="utf-8")
    s = s.replace('<link rel="icon" href="img/3d/compass.webp" type="image/webp">\n', "")
    if "manifest.webmanifest" not in s:
        s = s.replace("</head>", HEAD + "</head>", 1)
    if "css/motion.css" not in s:
        s = s.replace('<link rel="stylesheet" href="css/brand.css">', '<link rel="stylesheet" href="css/brand.css">\n<link rel="stylesheet" href="css/motion.css">', 1)
    if 'name="theme-color"' not in s:
        s = s.replace('<script src="js/pwa.js" defer></script>\n', '<script src="js/pwa.js" defer></script>\n<meta name="theme-color" content="#2d4a3e">\n', 1)
    s = s.replace('<div class="logo-m"><img src="img/3d/compass.webp" alt="" width="34" height="34"></div>', LOGO)
    if "js/live-bar.js" not in s:
        s = s.replace('<script src="js/config.js"></script>', '<script src="js/config.js"></script>\n<script src="js/live-bar.js"></script>', 1)
    if "data-install" not in s:
        s = s.replace(TG + "</div>", TG + '<a href="#" data-install>📱 Ilovani oʻrnatish</a></div>', 1)

    m0 = M0.get(path.name)
    if m0 and (root / m0).exists():
        s = re.sub(r'<button type="button" class="btn btn-p" style="width:100%;margin-top:14px" data-wl>[^<]*M0 ochilganda xabar bering</button>',
                   f'<a class="btn btn-p" style="width:100%;margin-top:14px" href="{m0}">Bepul M0 ni boshlash</a>', s)
        s = re.sub(r'(<h3>M0, qaror moduli</h3>.*?)<button type="button" class="btn btn-g" data-wl>Ochilganda xabar bering</button>',
                   lambda m: m.group(1) + f'<a class="btn btn-g" href="{m0}">M0 ni boshlash</a>', s, count=1, flags=re.S)
        s = s.replace('<a href="#dastur" class="btn btn-p">Bepul M0 ni koʻrish</a>', f'<a href="{m0}" class="btn btn-p">Bepul M0 ni boshlash</a>')
    if path.name == "master-lab.html":
        # Sahifa oxiridagi CTA
        s = s.replace('<button type="button" class="btn btn-p" data-wl>Kutish roʻyxatiga yozilish</button>\n      <a href="https://t.me/kompaslab"',
                      '<a class="btn btn-p" href="master-lab-m0.html">Bepul M0 ni boshlash</a>\n      <a href="https://t.me/kompaslab"', 1)
    if path.name == "musofir-lab.html":
        for a, b in MUSOFIR_TEXT:
            s = s.replace(a, b)
    path.write_text(s, encoding="utf-8")


def run(root: Path, files) -> None:
    for f in files:
        p = root / f
        if p.exists():
            process(p, root)
