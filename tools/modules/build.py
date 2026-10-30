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
#  master-lab-m0: tayyor sahifa src/master-lab-m0.page.html (raw=True, faqat sayt).
#
#  Sayt versiyasi (2026-10-18) uch xil sahifaga yigʻiladi, hammasi bitta manbadan:
#    <nom>.html        modul sahifasi (hub): maqsad, darslar yoʻli, nishonlar
#    <nom>-N.html      har dars alohida sahifada
#    <nom>-yakun.html  vositalar, nishonlar, qaror
#  Koʻrinishni js/kompas-module.js tanlaydi (body data-kview), dizayn css/kompas-ui.css.
# ═══════════════════════════════════════════════════════════════
import base64, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DIST = HERE / "dist"
PAID = HERE / "paid"   # pullik sahifalar: git va saytga chiqmaydi, faqat bazaga yuklanadi

# site: saytga chiqadimi; protect: nusxa olishdan himoya va suv belgisi; og: havola rasmi matni
MODULES = {
    "bachelor-lab-m0":     dict(lab="bachelor-lab.html", site=True, protect=True),
    "gks-lab-m0":          dict(lab="gks-lab.html", site=True, protect=True),
    "phd-lab-m0":          dict(lab="phd-lab.html", site=True, protect=True),
    "tadbirkor-talaba-m0": dict(lab="tadbirkor-talaba.html", site=True, protect=True),
    # Tayyor sahifa (avval master-lab-m0.html qoʻlda yuritilgan): faqat sayt versiyasi
    "master-lab-m0":       dict(lab="master-lab.html", site=True, raw=True),
    "usa-lab-m0":          dict(lab="usa-lab.html", site=True, protect=True),
    # Musofir M0 hamma uchun ochiq (xavfsizlik maʼlumoti): darvoza va himoya yoʻq, ulashish bor
    "musofir-lab-m0":      dict(lab="musofir-lab.html", site=True, protect=False,
                                og=("Musofir Lab M0: rasmiy yoʻl va firibgarlikdan himoya",
                                    "Xorijga ishga ketishdan oldin: firibgarlik belgilari, 4 mamlakatning rasmiy yoʻllari, xarajat va qarz xavfi. Bepul.")),
    # Pullik modullar (paid=True): saytda ochiq HTML yoʻq. Toʻliq sahifa tools/modules/paid/ ga
    # yigʻiladi va Supabase paid_pages jadvaliga yuklanadi (tools/modules/paid_upload.py);
    # oʻquvchiga faqat master-lab-o.html?m=N orqali, fn_paid_page() obunani tekshirgandan keyin beriladi.
    "master-lab-m1":       dict(lab="master-lab.html", site=False, paid=True, protect=True),
    "master-lab-m2":       dict(lab="master-lab.html", site=False, paid=True, protect=True),
    "master-lab-m3":       dict(lab="master-lab.html", site=False, paid=True, protect=True),
    "master-lab-m4":       dict(lab="master-lab.html", site=False, paid=True, protect=True),
    "master-lab-m5":       dict(lab="master-lab.html", site=False, paid=True, protect=True),
    "master-lab-m6":       dict(lab="master-lab.html", site=False, paid=True, protect=True),
    "master-lab-m7":       dict(lab="master-lab.html", site=False, paid=True, protect=True),
    "master-lab-m8":       dict(lab="master-lab.html", site=False, paid=True, protect=True),
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


# Suv belgisi: har modulda (sayt va yuklab olinadigan), kirishdan qatʼi nazar; chop etishda koʻrinmaydi
# (CV, SoP kabi hujjatlar PDF ga suv belgisisiz chiqadi). protect.js shu .kp-wm ni qayta ishlatadi.
WATERMARK = """<style>.kp-wm{position:fixed;inset:0;z-index:350;pointer-events:none;background-repeat:repeat;opacity:.06}@media print{.kp-wm{display:none!important}}</style>
<script>(function(){function m(){if(document.querySelector(".kp-wm"))return;var c=document.createElement("canvas"),w=280,h=170,g=c.getContext&&c.getContext("2d");if(!g)return;c.width=w;c.height=h;g.translate(w/2,h/2);g.rotate(-0.4);g.fillStyle="#000";g.font="500 13px Outfit,system-ui,sans-serif";g.textAlign="center";g.fillText("kompaslab.uz",0,0);var d=document.createElement("div");d.className="kp-wm";d.setAttribute("aria-hidden","true");d.style.backgroundImage="url("+c.toDataURL()+")";document.body.appendChild(d);}if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",m);else m();})();</script>
"""


def watermark(s):
    if 'class="kp-wm"' in s or ".kp-wm{" in s:
        return s
    i = s.rfind("</body>")  # oxirgisi: JS ichidagi "</body>" matnlariga tegmaslik uchun
    return s[:i] + WATERMARK + s[i:]


SUGGEST = '<script src="js/suggest.js" defer></script>\n'


def with_suggest(s):
    """Avtomatik taklif (universitet, dastur, davlat…): js/suggest.js, oxirgi </body> oldidan."""
    if "js/suggest.js" in s:
        return s
    i = s.rfind("</body>")
    return s[:i] + SUGGEST + s[i:]


def site(name, src, cfg):
    s = src.replace('<link rel="icon" href="img/3d/compass.webp" type="image/webp">\n', "")
    head = HEAD + (OG.format(t=cfg["og"][0], d=cfg["og"][1]) if cfg.get("og") else "")
    s = s.replace("</head>", head + "</head>", 1)
    s = re.sub(r'(<a class="logo" href="[^"]+">)<img src="img/3d/compass\.webp" width="160" height="160" alt="">', lambda m: m.group(1) + LOGO, s, count=1)
    if SB in s:
        extra = '\n<script src="js/config.js"></script>\n<script src="js/live-bar.js"></script>' + ('\n<script src="js/protect.js"></script>' if cfg.get("protect") else "")
        s = s.replace(SB, SB + extra, 1)
    s = with_suggest(s)
    # Darvoza: oʻz mijozini yaratish oʻrniga config.js yaratgan window.supabase dan foydalanadi
    s = re.sub(r'  var lib = window\.supabase;\n  if \(!lib \|\| !lib\.createClient\) \{(.*?)\}\n  var sb = lib\.createClient\([^\n]*\n',
               lambda m: "  var sb = window.supabase;\n  if (!sb || !sb.auth) {" + m.group(1) + "}\n", s, flags=re.S)
    return s


def sfx_inline():
    return "<script>\n" + (ROOT / "js/sfx.js").read_text(encoding="utf-8") + "</script>"


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
    # Tovush effektlari internetsiz ham ishlasin: js/sfx.js fayl ichiga
    t = t.replace('<script src="js/sfx.js"></script>', sfx_inline(), 1)
    # Ichki havolalar saytga olib borsin
    t = re.sub(r'href="([a-z0-9-]+)\.html"', lambda m: 'href="https://kompaslab.uz/' + ("" if m.group(1) == "index" else m.group(1)) + '"', t)
    return t


# master-lab-o.html sahifasida Supabase mijozi (window.supabase) allaqachon bor va document.write
# oʻsha oynada ishlaydi: supabase-js/config.js qayta yuklansa, "const" eʼlonlari toʻqnashadi.
# Shuning uchun pullik sahifaga faqat protect.js qoʻshiladi.
PAID_JS = '<script src="js/protect.js"></script>\n'


def paid(name, src, cfg):
    """Pullik modulning sayt sahifasi (bitta sahifa). master-lab-o.html uni bazadan olib,
    document.write bilan ochadi: nisbiy yoʻllar (img/, js/, css/) sayt ildiziga mos keladi."""
    s = site(name, src, cfg)
    if "js/config.js" not in s:
        i = s.rfind("</body>")
        s = s[:i] + PAID_JS + s[i:]
    s = s.replace("</head>", '<meta name="robots" content="noindex, nofollow">\n</head>', 1)
    return s


UI_HEAD = '<link rel="stylesheet" href="css/kompas-ui.css">\n<script src="js/kompas-ui.js"></script>\n'


def meta(name, s):
    """Manbadan modul, darslar va yakun maʼlumoti (kompas-module.js uchun)."""
    m = re.search(r'class="crumb"><a href="index\.html">Kompas Lab</a> · <a href="([a-z0-9-]+\.html)">([^<]+)</a> · Modul (\d+)', s)
    assert m, name + ": crumb topilmadi"
    key = re.search(r'var KEY = "([a-z0-9_]+)"', s).group(1)
    short = dict(re.findall(r'<a class="node" href="#(l\d+)" data-node="l\d+"><span class="dot">[^<]*</span>([^<]+)</a>', s))
    lessons = []
    for lid, chunk in re.findall(r'<article class="lesson" id="(l\d+)"[^>]*>(.*?)<div class="l-body">', s, flags=re.S):
        num = re.search(r'<span class="l-n">Dars ([0-9.]+)</span>', chunk).group(1)
        title = re.sub(r"<[^>]+>", "", re.search(r'<span class="l-t"[^>]*>(.*?)</span>', chunk, flags=re.S).group(1)).strip()
        tags = [re.sub(r"<[^>]+>", "", t).strip() for t in re.findall(r'<span class="tag(?: [a-z]+)?">(.*?)</span>', chunk)]
        tags = [t for t in tags if "XP" not in t]
        lessons.append(dict(id=lid, num=num, title=title, short=short.get(lid, "").strip(), meta=", ".join(tags)))
    assert lessons, name + ": darslar topilmadi"
    tools = [re.sub(r"<[^>]+>", "", t) for t in re.findall(r'<div class="tool"[^>]*>\s*<div class="tool-h">.*?<h3>(.*?)</h3>', s, flags=re.S)]
    return dict(base=name, key=key, lab=m.group(1), labName=m.group(2), mod="M" + m.group(3), lessons=lessons,
                yakunMeta=", ".join(tools + ["nishonlar", "qaror va rozilik"]))


def views(name, s):
    """Sayt versiyasini hub, dars va yakun sahifalariga ajratadi: {fayl: html}."""
    info = meta(name, s)
    s = s.replace("</head>", UI_HEAD + "</head>", 1)
    i = s.rfind("</body>")
    s = s[:i] + "<script>window.KMOD=" + json.dumps(info, ensure_ascii=False) + ';</script>\n<script src="js/kompas-module.js"></script>\n' + s[i:]
    tmatch = re.search(r"<title>(.*?)</title>", s)
    pages = [(name + ".html", "hub", "", None)]
    pages += [(name + "-" + str(k + 1) + ".html", "lesson", l["id"], "Dars " + l["num"] + ": " + l["title"] + " · " + info["labName"] + " " + info["mod"] + " | Kompas Lab") for k, l in enumerate(info["lessons"])]
    pages.append((name + "-yakun.html", "yakun", "", "Yakun: vositalar va qaror · " + info["labName"] + " " + info["mod"] + " | Kompas Lab"))
    out = {}
    for fn, view, lid, title in pages:
        t = s
        attrs = ' data-kview="' + view + '"' + (' data-klesson="' + lid + '"' if lid else "")
        t = re.sub(r"<body([^>]*)>", lambda m: "<body" + m.group(1) + attrs + ">", t, count=1)
        t = re.sub(r'var RET = "[a-z0-9-]+\.html";', 'var RET = "' + fn + '";', t, count=1)
        if title and tmatch:
            t = t.replace(tmatch.group(0), "<title>" + title + "</title>", 1)
        canon = '<link rel="canonical" href="https://www.kompaslab.uz/' + fn[:-5] + '">\n'
        t = t.replace("</head>", canon + "</head>", 1)
        out[fn] = t
    return out


def build(name):
    cfg = MODULES[name]
    if cfg.get("raw"):
        src = with_suggest(watermark((HERE / "src" / (name + ".page.html")).read_text(encoding="utf-8")))
        for fn, html in views(name, src).items():
            (ROOT / fn).write_text(html, encoding="utf-8")
        print(name, "-> sayt (raw)")
        return
    src = watermark((HERE / "src" / (name + ".src.html")).read_text(encoding="utf-8").replace("{{CSS}}", (HERE / "m0.css").read_text(encoding="utf-8")))
    out = []
    if cfg.get("site"):
        for fn, html in views(name, site(name, src, cfg)).items():
            (ROOT / fn).write_text(html, encoding="utf-8"); out.append(fn)
    if cfg.get("paid"):
        PAID.mkdir(exist_ok=True)
        (PAID / (name + ".html")).write_text(paid(name, src, cfg), encoding="utf-8"); out.append("paid/" + name + ".html")
    DIST.mkdir(exist_ok=True)
    (DIST / (name + ".html")).write_text(standalone(name, src, cfg), encoding="utf-8"); out.append("dist/" + name + ".html")
    print(name, "->", ", ".join(out))


if __name__ == "__main__":
    names = sys.argv[1:] or list(MODULES)
    for n in names:
        if n not in MODULES:
            sys.exit("Nomaʼlum modul: " + n + ". Mavjud: " + ", ".join(MODULES))
        build(n)
