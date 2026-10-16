# ═══════════════════════════════════════════════════════════════
#  Kompas Lab modullarini yigʻish
#
#  Ishga tushirish (repo ildizidan):
#    python3 tools/modules/build.py                 # hammasi
#    python3 tools/modules/build.py usa-lab-m0      # bittasi
#
#  Har modul uchun ikki natija:
#    1) sayt versiyasi  -> repo ildizida <nom>.html (faqat site=True boʻlsa)
#       CSS ichida, rasmlar img/3d/ dan, config.js + live-bar.js (+ protect.js),
#       logotip, favicon, PWA; kirish darvozasi config.js mijozidan foydalanadi
#    2) yuklab olinadigan versiya -> tools/modules/dist/<nom>.html
#       hamma rasm fayl ichida (base64), internetsiz ochiladi; file:// da darvoza ochiq
#
#  Manba: tools/modules/src/<nom>.src.html ({{CSS}} oʻrniga m0.css qoʻyiladi)
#  master-lab-m0.html manbasiz: toʻgʻridan-toʻgʻri tahrirlanadi.
# ═══════════════════════════════════════════════════════════════
import base64, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DIST = HERE / "dist"

# site: saytga chiqadimi; protect: nusxa olishdan himoya va suv belgisi; og: havola rasmi matni
MODULES = {
    "bachelor-lab-m0":     dict(lab="bachelor-lab.html", site=True, protect=True),
    "gks-lab-m0":          dict(lab="gks-lab.html", site=True, protect=True),
    "phd-lab-m0":          dict(lab="phd-lab.html", site=True, protect=True),
    "tadbirkor-talaba-m0": dict(lab="tadbirkor-talaba.html", site=True, protect=True),
    "usa-lab-m0":          dict(lab="usa-lab.html", site=True, protect=True),
    # Musofir M0 hamma uchun ochiq (xavfsizlik maʼlumoti): darvoza va himoya yoʻq, ulashish bor
    "musofir-lab-m0":      dict(lab="musofir-lab.html", site=True, protect=False,
                                og=("Musofir Lab M0: rasmiy yoʻl va firibgarlikdan himoya",
                                    "Xorijga ishga ketishdan oldin: firibgarlik belgilari, 4 mamlakatning rasmiy yoʻllari, xarajat va qarz xavfi. Bepul.")),
    # Pullik modullar: hozircha faqat yuklab olinadigan fayl
    "master-lab-m1":       dict(lab="master-lab.html", site=False),
    "master-lab-m2":       dict(lab="master-lab.html", site=False),
    "master-lab-m3":       dict(lab="master-lab.html", site=False),
    "master-lab-m4":       dict(lab="master-lab.html", site=False),
    "master-lab-m5":       dict(lab="master-lab.html", site=False),
    "master-lab-m6":       dict(lab="master-lab.html", site=False),
    "master-lab-m7":       dict(lab="master-lab.html", site=False),
    "master-lab-m8":       dict(lab="master-lab.html", site=False),
}

SB = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js"></script>'
HEAD = """<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="img/brand/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="img/brand/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Kompas Lab">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<script src="js/pwa.js" defer></script>
<link rel="stylesheet" href="css/brand.css">
"""
OG = """<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="https://www.kompaslab.uz/img/brand/og.jpg">
<meta name="twitter:card" content="summary_large_image">
"""
LOGO = '<span class="klogo klogo-sm"><img class="klogo-b" src="img/brand/logo-base.webp" alt="" width="128" height="128"><img class="klogo-a" src="img/brand/logo-arrow.webp" alt="" width="128" height="128"></span>'
# Toast va boshqa JS chaqiradigan ikonkalar: yuklab olinadigan versiyada yashirin <img data-icon> sifatida
TOAST_ICONS = ["bulb", "lock", "shield", "compass", "money", "seedling", "memo", "chart", "hourglass", "scroll", "calendar", "telescope", "bell"]


def site(name, src, cfg):
    s = src.replace('<link rel="icon" href="img/3d/compass.webp" type="image/webp">\n', "")
    head = HEAD + (OG.format(t=cfg["og"][0], d=cfg["og"][1]) if cfg.get("og") else "")
    s = s.replace("</head>", head + "</head>", 1)
    s = re.sub(r'(<a class="logo" href="[^"]+">)<img src="img/3d/compass\.webp" width="160" height="160" alt="">', lambda m: m.group(1) + LOGO, s, count=1)
    if SB in s:
        extra = '\n<script src="js/config.js"></script>\n<script src="js/live-bar.js"></script>' + ('\n<script src="js/protect.js"></script>' if cfg.get("protect") else "")
        s = s.replace(SB, SB + extra, 1)
    # Darvoza: oʻz mijozini yaratish oʻrniga config.js yaratgan window.supabase dan foydalanadi
    s = re.sub(r'  var lib = window\.supabase;\n  if \(!lib \|\| !lib\.createClient\) \{(.*?)\}\n  var sb = lib\.createClient\([^\n]*\n',
               lambda m: "  var sb = window.supabase;\n  if (!sb || !sb.auth) {" + m.group(1) + "}\n", s, flags=re.S)
    return s


def standalone(name, src, cfg):
    t = src
    used = set(re.findall(r"img/3d/([a-z0-9-]+)\.webp", t))
    hidden = [i for i in TOAST_ICONS if (HERE.parent.parent / "img/3d" / (i + ".webp")).exists() and ('"' + i + '"') in t]
    if hidden and 'data-icon="' not in t:
        t = t.replace('<div class="toast"', "<div hidden>" + "".join('<img data-icon="%s" src="img/3d/%s.webp" alt="">' % (i, i) for i in hidden) + '</div>\n<div class="toast"', 1)
    cache = {}
    def rep(m):
        n = m.group(1)
        if n not in cache:
            cache[n] = "data:image/webp;base64," + base64.b64encode((ROOT / "img/3d" / (n + ".webp")).read_bytes()).decode()
        return cache[n]
    t = re.sub(r"img/3d/([a-z0-9-]+)\.webp", rep, t)
    # Ichki havolalar saytga olib borsin
    t = re.sub(r'href="([a-z0-9-]+)\.html"', lambda m: 'href="https://kompaslab.uz/' + ("" if m.group(1) == "index" else m.group(1)) + '"', t)
    return t


def build(name):
    cfg = MODULES[name]
    src = (HERE / "src" / (name + ".src.html")).read_text(encoding="utf-8").replace("{{CSS}}", (HERE / "m0.css").read_text(encoding="utf-8"))
    out = []
    if cfg.get("site"):
        (ROOT / (name + ".html")).write_text(site(name, src, cfg), encoding="utf-8"); out.append(name + ".html")
    DIST.mkdir(exist_ok=True)
    (DIST / (name + ".html")).write_text(standalone(name, src, cfg), encoding="utf-8"); out.append("dist/" + name + ".html")
    print(name, "->", ", ".join(out))


if __name__ == "__main__":
    names = sys.argv[1:] or list(MODULES)
    for n in names:
        if n not in MODULES:
            sys.exit("Nomaʼlum modul: " + n + ". Mavjud: " + ", ".join(MODULES))
        build(n)
