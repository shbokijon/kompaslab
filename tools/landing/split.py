# ═══════════════════════════════════════════════════════════════
#  Lab sahifalarini alohida sahifalarga ajratish (2026-10-18)
#
#  Generator (render.py, phd_polish.py, postprocess.py) avval bitta uzun Lab
#  sahifasini yozadi. Bu skript uni build.py oxirida quyidagilarga ajratadi:
#    <lab>.html            Umumiy: hero, A→B, modullar yoʻli, keyingi sahifalar
#    <lab>-dastur.html     Dastur: fazalar, modullar va darslar, metod, faktlar
#    <lab>-test.html       Moslik testi (Tayyorgarlik koʻrsatkichi), boʻlsa
#    <lab>-narxlar.html    Narxlar va obuna shartlari
#    <lab>-savollar.html   Kimga mos, savollar
#    <lab>-mN.html         Har modul sahifasi: darslar roʻyxati (M0 interaktiv
#                          moduli tools/modules/ da yigʻilgan boʻlsa, u ishlatiladi)
#  Faqat build.py dan chaqiriladi (kirish: uzun sahifa).
# ═══════════════════════════════════════════════════════════════
import html as H
import json
import re
from pathlib import Path

UI_HEAD = '<link rel="stylesheet" href="css/kompas-ui.css">\n<script src="js/kompas-ui.js"></script>\n'
SITE = "https://www.kompaslab.uz/"

# Lab boʻyicha qoʻshimcha tab (sahifa mavjud boʻlsa)
EXTRA_TABS = {"master-lab": [("master-lab-manbalar.html", "Manbalar"), ("master-planner.html", "Shaxsiy reja")]}


def text(s):
    return H.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def esc(s):
    return H.escape(s, quote=True)


def blocks(body):
    """Body ni yuqori darajadagi bloklarga ajratadi: [(kalit, html)]."""
    parts = re.split(r'\n(?=<(?:nav class="nav"|header|section|footer|div class="ovl"|script)\b)', body)
    out = []
    for p in parts:
        p = p.strip("\n")
        if not p:
            continue
        m = re.match(r'<(nav|header|section|footer|div|script)\b([^>]*)>', p)
        if not m:
            out.append(("pre", p)); continue
        tag, attrs = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if tag == "nav": key = "nav"
        elif tag == "header": key = "hero"
        elif tag == "footer": key = "footer"
        elif tag == "script": key = "script"
        elif tag == "div": key = "modal"
        elif "cta" in attrs: key = "cta"
        elif 'class="dark"' in attrs and not any(k == "dark" for k, _ in out): key = "dark"
        elif idm: key = idm.group(1)
        elif "Kimga mos" in p[:600]: key = "fit"
        else: key = "extra"
        out.append((key, p))
    return out


def modules(dastur):
    """#dastur dan modullar va guruhlar."""
    res, group = [], None
    phases = []
    for small, b, span in re.findall(r'<div class="phase"><small>(.*?)</small><b>(.*?)</b><span>(.*?)</span></div>', dastur):
        r = re.match(r"M(\d+)(?:[–-]M(\d+))?", text(span))
        if r:
            phases.append((int(r.group(1)), int(r.group(2) or r.group(1)), text(small).split(",")[0] + ": " + text(b)))
    for m in re.finditer(r'<div class="trk-h">(.*?)</div>|<details class="mod( free)?"[^>]*>(.*?)</details>', dastur, flags=re.S):
        if m.group(1) is not None:
            group = text(m.group(1)); continue
        d = m.group(3)
        mid = text(re.search(r'<div class="mod-n">(.*?)</div>', d).group(1))
        title = text(re.search(r'<div class="mod-t">(.*?)</div>', d).group(1))
        art = re.search(r'<div class="mod-a">(.*?)</div>', d)
        art = text(art.group(1)) if art else ""
        art = re.sub(r"^Natija:\s*", "", art)
        lessons = []
        for li in re.findall(r"<li>(.*?)</li>", re.search(r"<ol>(.*?)</ol>", d, flags=re.S).group(1), flags=re.S):
            num = re.search(r'<span class="num">(.*?)</span>', li)
            small = re.search(r"<small>(.*?)</small>", li, flags=re.S)
            tks = [text(t) for t in re.findall(r'<span class="tk">(.*?)</span>', li)]
            title_l = re.sub(r'<span class="num">.*?</span>|<small>.*?</small>|<span class="tk">.*?</span>', "", li, flags=re.S)
            lessons.append(dict(num=text(num.group(1)) if num else "", title=text(title_l), small=text(small.group(1)) if small else "", trek=tks))
        n = int(re.sub(r"\D", "", mid) or 0)
        ph = group
        if ph is None:
            for a, b, lab in phases:
                if a <= n <= b: ph = lab; break
        res.append(dict(id=mid, n=n, slug=re.sub(r"[^a-z0-9]+", "-", mid.lower()).strip("-"), title=title, art=art, free=bool(m.group(2)), core="tag-core" in d, lessons=lessons, group=ph))
    return res


def tabs_html(stem, have_test, cur, extra):
    items = [(stem + ".html", "Umumiy"), (stem + "-dastur.html", "Dastur")]
    if have_test:
        items.append((stem + "-test.html", "Moslik testi"))
    items += [(stem + "-narxlar.html", "Narxlar"), (stem + "-savollar.html", "Savollar")] + extra
    return '<div class="kl-tabs" role="navigation" aria-label="Lab sahifalari">' + "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in items) + "</div>"


def page_head(crumbs, h1, lead="", art=""):
    cr = '<span aria-hidden="true">/</span>'.join(f'<a href="{h}">{t}</a>' if h else f"<span>{t}</span>" for h, t in crumbs)
    lead = f'<p class="lead">{lead}</p>' if lead else ""
    art = f'<img class="kl-head-art float" src="img/3d/{art}.webp" alt="" width="160" height="160">' if art else ""
    return f'''<header class="kl-pagehead">
  <div class="wrap">
    <nav class="kl-crumb" aria-label="Yoʻl">{cr}</nav>
    <div class="kl-head-row"><div><h1>{h1}</h1>{lead}</div>{art}</div>
  </div>
</header>'''


def strip_head(sec):
    """Boʻlimning birinchi .head blokini olib, (h2, sub, qolgan html) qaytaradi."""
    m = re.search(r'\s*<div class="head">\s*<h2>(.*?)</h2>\s*(?:<p class="sub">(.*?)</p>)?\s*</div>', sec, flags=re.S)
    if not m:
        return None, None, sec
    return m.group(1), m.group(2) or "", sec[:m.start()] + sec[m.end():]


def route(stem, mods, m0_page, here=None):
    lis, last = [], None
    for m in mods:
        if m["group"] and m["group"] != last:
            lis.append(f'<li class="kl-phase">{esc(m["group"])}</li>'); last = m["group"]
        href = m0_page if (m["slug"] == "m0" and m0_page) else f'{stem}-{m["slug"]}.html'
        n = len(m["lessons"])
        if m["free"]:
            cls, st = "is-free", ("Bepul, ochiq" if (m["slug"] == "m0" and m0_page) else "Bepul")
        else:
            cls, st = "is-locked", "Obuna"
        if here is not None and m["slug"] == here:
            cls += " is-here"
        sub = f'{n} dars' + (f'. Natija: {esc(m["art"])}' if m["art"] else "")
        lis.append(f'<li class="kl-st {cls}"><a href="{href}"><span class="kl-st-n{" sm" if len(m["id"]) > 3 else ""}">{esc(m["id"])}</span><span class="kl-st-b"><b>{esc(m["title"])}</b><small>{sub}</small></span><span class="kl-st-s">{st}</span></a></li>')
    return '<ol class="kl-route"' + (' data-needle' if here is not None else "") + ">" + "".join(lis) + "</ol>"


def hash_map(stem, have_test):
    pages = {"dastur": stem + "-dastur.html", "qanday": stem + "-dastur.html#qanday", "faktlar": stem + "-dastur.html#faktlar",
             "atlas": stem + "-dastur.html#atlas", "narx": stem + "-narxlar.html", "savollar": stem + "-savollar.html",
             "kimga": stem + "-savollar.html"}
    if have_test:
        pages["test"] = stem + "-test.html"
    else:
        pages["test"] = stem + "-dastur.html"
    return pages


def relink(s, stem, hmap, own):
    """Sahifa ichidagi #langar havolalarini tegishli sahifaga yoʻnaltiradi."""
    def rep(m):
        h = m.group(1)
        if h in own:
            return m.group(0)
        t = hmap.get(h)
        return f'href="{t}"' if t else m.group(0)
    s = re.sub(r'href="#([a-z0-9-]+)"', rep, s)
    s = re.sub(r'href="' + re.escape(stem) + r'\.html#([a-z0-9-]+)"', lambda m: f'href="{hmap.get(m.group(1), stem + ".html")}"', s)
    return s


def run(root: Path, files):
    made = []
    for f in files:
        p = root / f
        src = p.read_text(encoding="utf-8")
        if 'data-kpage=' in src:
            raise SystemExit(f"{f}: allaqachon ajratilgan. Avval generatorni (build.py) toʻliq ishga tushiring.")
        made += split(root, f, src)
    return made


def split(root, f, src):
    stem = f[:-5]
    bi = src.index("<body")
    head, body = src[:bi], src[bi:]
    bopen = re.match(r"<body[^>]*>", body).group(0)
    body = body[len(bopen):]
    end = body.rindex("</body>")
    tail_after = body[end:]
    body = body[:end]
    bl = blocks(body)
    B = {}
    order = []
    for k, h in bl:
        if k in ("script", "pre"):
            continue
        if k in B:
            k = k + "_" + str(len(order))
        B[k] = h; order.append(k)
    scripts = "\n".join(h for k, h in bl if k == "script")
    pre = "\n".join(h for k, h in bl if k == "pre")
    have_test = "test" in B
    mods = modules(B["dastur"])
    lab_name = text(re.search(r'<span class="logo-t">(.*?)</span>\s*</a>', B["nav"], flags=re.S).group(1)) if False else None
    crumb = re.search(r'<div class="crumb">(.*?)</div>', B["hero"], flags=re.S)
    lab_name = text(crumb.group(1)).split("/")[-1].strip() if crumb else stem
    icon = re.search(r'src="img/3d/([a-z0-9-]+)\.webp"', B["hero"])
    icon = icon.group(1) if icon else "compass"
    m0_page = stem + "-m0.html" if (root / (stem + "-m0.html")).exists() else None
    title0 = re.search(r"<title>(.*?)</title>", head).group(1)
    hmap = hash_map(stem, have_test)
    did = re.search(r'<section class="dark" id="([^"]+)"', B.get("dark", ""))
    if did:
        hmap[did.group(1)] = stem + ".html#" + did.group(1)
    extra = [(h, t) for h, t in EXTRA_TABS.get(stem, []) if (root / h).exists()]
    nlessons = sum(len(m["lessons"]) for m in mods)

    def nav(cur):
        n = B["nav"]
        tabs = tabs_html(stem, have_test, cur, extra)
        n = re.sub(r'<div class="nav-links">.*?</div>', tabs, n, count=1, flags=re.S)
        n = n.replace('<button type="button" class="btn btn-p btn-sm" data-wl>', '<span class="kl-sfx" data-sfx-slot></span><button type="button" class="btn btn-p btn-sm" data-wl>', 1)
        n += '\n<div class="kl-tabbar">' + tabs + "</div>"
        return n

    def emit(fn, kind, title, desc, main, own=()):
        h = head
        h = re.sub(r"<title>.*?</title>", "<title>" + title + "</title>", h, count=1)
        if desc:
            h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">', h, count=1)
            h = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(desc)}">', h, count=1)
        h = h.replace("</head>", f'<link rel="canonical" href="{SITE}{fn[:-5]}">\n' + UI_HEAD + "</head>", 1)
        b = bopen.replace("<body", f'<body data-kpage="{kind}"', 1)
        foot = "\n".join(B[k] for k in order if k in ("footer", "modal") or k.startswith("footer") or k.startswith("modal"))
        html = h + b + "\n" + pre + "\n" + nav(stem + "-dastur.html" if kind == "modul" else fn) + "\n" + main + "\n" + foot + "\n" + scripts + '\n<script src="js/sfx.js"></script>\n' + tail_after
        if kind == "hub":
            html = html.replace("</body>", HUB_JS.replace("{{MAP}}", json.dumps(hmap)) + "</body>", 1)
        html = relink(html, stem, hmap, set(own))
        (root / fn).write_text(html, encoding="utf-8")
        return fn

    made = []
    # ── 1. Umumiy ──
    hero = B["hero"].replace('href="#dastur" class="btn btn-g">Dasturni koʻrish</a>', f'href="{stem}-dastur.html" class="btn btn-g">Dasturni koʻrish</a>')
    hero = hero.replace('<a href="index.html#labs">Lablar</a>', '<a href="index.html#labs">Lablar</a>')
    m0_btn = f'<a class="btn btn-p" href="{m0_page}">Bepul M0 ni boshlash</a>' if m0_page else (f'<a class="btn btn-p" href="{stem}-m0.html">M0 dasturini koʻrish</a>')
    test_btn = f'<a class="btn btn-g" href="{stem}-test.html">Moslik testini topshirish</a>' if have_test else f'<a class="btn btn-g" href="{stem}-narxlar.html">Narxlarni koʻrish</a>'
    path = f'''<section id="yol">
  <div class="wrap">
    <div class="head"><h2>Dastur yoʻli: {len(mods)} modul, {nlessons} dars</h2><p class="sub">Har modulning oʻz sahifasi bor: darslar roʻyxati, natija va kirish holati. Darslar tartib bilan qurilgan, har biri bitta Topshiriq bilan tugaydi.</p></div>
    <div class="kl-path">
      {route(stem, mods, m0_page)}
      <aside aria-label="Qisqacha">
        <h3>{esc(lab_name)}</h3>
        <p>M0 bepul: toʻlashdan oldin dastur sizga mosligini tekshirasiz.</p>
        <dl><dt>Modullar</dt><dd>{len(mods)}</dd><dt>Darslar</dt><dd>{nlessons}</dd><dt>Bepul qism</dt><dd>M0</dd></dl>
        {m0_btn}
        {test_btn}
      </aside>
    </div>
  </div>
</section>'''
    nxt = [(stem + "-dastur.html", "Dastur", "Fazalar, modullar va har darsning mavzusi")]
    if have_test:
        nxt.append((stem + "-test.html", "Moslik testi", "6 savol: hozir boshlash kerakmi yoki avval boʻshliqlarni yopishmi"))
    nxt += [(stem + "-narxlar.html", "Narxlar", "Oylik, 4 oylik Mavsum va yillik obuna"), (stem + "-savollar.html", "Savollar", "Kimga mos, kimga mos emas va koʻp soʻraladigan savollar")]
    nxt_html = '<section class="alt"><div class="wrap"><div class="head"><h2>Keyingi qadam</h2></div><nav class="kl-next" aria-label="Lab sahifalari">' + "".join(
        f'<a href="{h}"><b>{t}</b><span>{d}</span></a>' for h, t, d in nxt) + "</nav></div></section>"
    main = "\n".join(x for x in [hero, B.get("dark", ""), path, nxt_html, B.get("cta", "")] if x)
    made.append(emit(stem + ".html", "hub", title0, None, main, own=("yol",) + ((did.group(1),) if did else ())))

    # ── 2. Dastur ──
    h2, sub, sec = strip_head(B["dastur"])
    # Har modul kartasiga modul sahifasi havolasi
    def addlink(m):
        d = m.group(0)
        mid = text(re.search(r'<div class="mod-n">(.*?)</div>', d).group(1))
        sl = re.sub(r"[^a-z0-9]+", "-", mid.lower()).strip("-")
        href = m0_page if (sl == "m0" and m0_page) else f"{stem}-{sl}.html"
        return d.replace("</details>", f'<a class="kl-modlink" href="{href}">{esc(mid)} modul sahifasi</a></details>')
    sec = re.sub(r'<details class="mod[^"]*"[^>]*>.*?</details>', addlink, sec, flags=re.S)
    parts = [page_head([("index.html", "Kompas Lab"), (stem + ".html", esc(lab_name)), (None, "Dastur")], h2, sub, icon), sec]
    for k in order:
        if k in ("faktlar", "atlas", "qanday", "extra") or k.startswith("extra"):
            parts.append(B[k])
    made.append(emit(stem + "-dastur.html", "dastur", f"Dastur: {len(mods)} modul, {nlessons} dars · {lab_name} | Kompas Lab", f"{lab_name} dasturi: fazalar, {len(mods)} modul va {nlessons} dars mavzulari. M0 bepul.", "\n".join(parts), own=("dastur", "qanday", "faktlar", "atlas")))

    # ── 3. Test ──
    if have_test:
        h2, sub, sec = strip_head(B["test"])
        main = page_head([("index.html", "Kompas Lab"), (stem + ".html", esc(lab_name)), (None, "Moslik testi")], h2 or "Moslik testi", sub, "chart") + "\n" + sec
        made.append(emit(stem + "-test.html", "test", f"Moslik testi · {lab_name} | Kompas Lab", f"{lab_name}: 6 savollik tayyorgarlik koʻrsatkichi. Toʻlashdan oldin boshlash vaqti kelganini tekshiring.", main, own=("test",)))

    # ── 4. Narxlar ──
    h2, sub, sec = strip_head(B["narx"])
    main = page_head([("index.html", "Kompas Lab"), (stem + ".html", esc(lab_name)), (None, "Narxlar")], h2 or "Narxlar", sub, "money") + "\n" + sec
    made.append(emit(stem + "-narxlar.html", "narxlar", f"Narxlar · {lab_name} | Kompas Lab", f"{lab_name} narxlari: oylik, Mavsum (4 oy) va yillik obuna. M0 bepul.", main, own=("narx",)))

    # ── 5. Savollar ──
    h2, sub, sec = strip_head(B["savollar"])
    main = page_head([("index.html", "Kompas Lab"), (stem + ".html", esc(lab_name)), (None, "Savollar")], h2 or "Savollar", sub, "bulb") + "\n" + B.get("fit", "") + "\n" + sec
    made.append(emit(stem + "-savollar.html", "savollar", f"Savollar · {lab_name} | Kompas Lab", f"{lab_name}: kimga mos va kimga mos emas, koʻp soʻraladigan savollar.", main, own=("savollar",)))

    # ── 6. Modul sahifalari ──
    for i, m in enumerate(mods):
        if m["slug"] == "m0" and m0_page:
            continue
        fn = f"{stem}-{m['slug']}.html"
        lis = []
        for l in m["lessons"]:
            tk = (" " + ", ".join(l["trek"]) + " treki uchun.") if l["trek"] else ""
            lis.append(f'<li class="kl-st {"is-free" if m["free"] else "is-locked"}"><div><span class="kl-st-n">{esc(l["num"])}</span><span class="kl-st-b"><b>{esc(l["title"])}</b><small>{esc(l["small"])}{esc(tk)}</small></span><span class="kl-st-s">{"Bepul" if m["free"] else "Obuna"}</span></div></li>')
        prev = mods[i - 1] if i > 0 else None
        nx = mods[i + 1] if i + 1 < len(mods) else None
        def mlink(x, rel):
            href = m0_page if (x["slug"] == "m0" and m0_page) else f"{stem}-{x['slug']}.html"
            cls = "pv" if rel == "prev" else "nx"
            lab = "Oldingi modul" if rel == "prev" else "Keyingi modul"
            return f'<a class="{cls}" rel="{rel}" data-kkey data-dir="{rel}" href="{href}"><small>{lab}</small><b>{esc(x["id"])}: {esc(x["title"])}</b></a>'
        pager = '<div class="kl-pager">' + (mlink(prev, "prev") if prev else f'<a class="pv" rel="prev" data-kkey data-dir="prev" href="{stem}-dastur.html"><small>Dastur</small><b>Barcha modullar</b></a>') + (mlink(nx, "next") if nx else f'<a class="nx primary" rel="next" data-kkey data-dir="next" href="{stem}-narxlar.html"><small>Oxirgi modul</small><b>Narxlar va obuna</b></a>') + "</div>"
        if m["free"]:
            lock = f'''<div class="kl-lock"><img src="img/3d/seedling.webp" alt="" width="160" height="160"><div><b>{esc(m["id"])} bepul boʻladi.</b><p>Interaktiv versiyasi tayyorlanmoqda. Ochilganda kutish roʻyxatidagilarga xabar beramiz.</p><div class="row"><button type="button" class="btn btn-p" data-wl>Ochilganda xabar bering</button><a class="btn btn-g" href="{stem}-dastur.html">Butun dastur</a></div></div></div>'''
        else:
            first = f'<a class="btn btn-g" href="{m0_page}">Bepul M0 dan boshlash</a>' if m0_page else f'<a class="btn btn-g" href="{stem}-dastur.html">Butun dastur</a>'
            lock = f'''<div class="kl-lock"><img src="img/3d/lock.webp" alt="" width="160" height="160"><div><b>Darslar obuna bilan ochiladi.</b><p>Har dars alohida sahifada: Diqqat 🔥, Asosiy qism, Xulosa va Topshiriq. Onlayn toʻlov hali ochilmagan; ochilganda kutish roʻyxatidagilarga birinchi xabar beramiz.</p><div class="row"><a class="btn btn-p" href="{stem}-narxlar.html">Narxlar va obuna</a>{first}</div></div></div>'''
        art = f'<div class="kl-mod-art"><img src="img/3d/memo.webp" alt="" width="28" height="28" style="width:28px;height:28px;flex:none"><span><b>Modul natijasi:</b> {esc(m["art"])}</span></div>' if m["art"] else ""
        lead = f'{len(m["lessons"])} dars' + (f'. {esc(m["group"])}' if m["group"] else "") + "."
        main = page_head([("index.html", "Kompas Lab"), (stem + ".html", esc(lab_name)), (stem + "-dastur.html", "Dastur"), (None, esc(m["id"]))], f'{esc(m["id"])}. {esc(m["title"])}', lead, icon)
        main += f'''
<section style="padding-top:8px">
  <div class="wrap">
    {art}
    <h2 style="margin:34px 0 14px">Darslar</h2>
    <ol class="kl-route kl-lessons">{"".join(lis)}</ol>
    {lock}
    <div class="kl-modnav">{pager}</div>
    <div class="head" style="margin-top:46px"><h2>Butun dastur</h2></div>
    {route(stem, mods, m0_page, here=m["slug"])}
  </div>
</section>'''
        main = main.replace('<div class="kl-modnav"><div class="kl-pager">', '<div class="kl-modnav" style="display:block"><div class="kl-pager">')
        desc = f'{lab_name}, {m["id"]}: {m["title"]}. {len(m["lessons"])} dars' + (f'. Natija: {m["art"]}' if m["art"] else "") + "."
        made.append(emit(fn, "modul", f'{m["id"]}. {m["title"]} · {lab_name} | Kompas Lab', desc[:300], main))
    return made


# Eski havolalar (masalan gks-lab.html#narx) yangi sahifaga oʻtadi
HUB_JS = '''<script>(function(){var M={{MAP}};var h=location.hash.slice(1);if(h&&M[h]){location.replace(M[h]);}})();</script>
'''
