# Bir martalik: uzun index.html ni (2026-10-18 gacha) toʻrt sahifaga ajratish.
#   index.html           Bosh sahifa: kompas testi, jonli hisob, globus, Lablar katalogi
#   qanday-ishlaydi.html "Nega Lab" va ishlash qoidalari
#   narxlar.html         Narxlar jadvali, kalkulyator, agentlik bilan solishtirish
#   savollar.html        Koʻp soʻraladigan savollar
# Natija sahifalari keyin qoʻlda yuritiladi; CSS css/home.css da umumiy.
# Ishga tushirish (faqat uzun index.html ustida): python3 tools/site/split_index.py
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
s = (ROOT / "index.html").read_text(encoding="utf-8")
if 'data-kpage="home"' in s:
    sys.exit("index.html allaqachon ajratilgan")

# 1. CSS umumiy faylga
st = re.search(r"<style>(.*?)</style>", s, flags=re.S)
(ROOT / "css/home.css").write_text("/* Bosh sahifa va umumiy sayt sahifalari (index, qanday-ishlaydi, narxlar, savollar) */\n" + st.group(1).strip() + "\n", encoding="utf-8")
s = s.replace(st.group(0), '<link rel="stylesheet" href="css/home.css">', 1)

# 2. JS: boshqa sahifalarda yoʻq elementlarga chidamli
def R(a, b):
    global s
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
R('  var amt = document.getElementById("amt"), labSel = document.getElementById("cmpLab");', '  var amt = document.getElementById("amt") || document.createElement("input"), labSel = document.getElementById("cmpLab") || document.createElement("select");')
R('  var big = document.getElementById("cmpBig"), cmpT = document.getElementById("cmpT"), cmpS = document.getElementById("cmpS");', '  var big = document.getElementById("cmpBig") || document.createElement("b"), cmpT = document.getElementById("cmpT") || document.createElement("p"), cmpS = document.getElementById("cmpS") || document.createElement("p");')
R('  var mcLab = document.getElementById("mcLab"), mcM = document.getElementById("mcM");\n  function mcalc() {\n    var l = bySlug[mcLab.value]', '  var mcLab = document.getElementById("mcLab"), mcM = document.getElementById("mcM");\n  function mcalc() {\n    if (!mcLab || !mcM) return;\n    var l = bySlug[mcLab.value]')
R('  mcLab.addEventListener("change", mcalc); mcM.addEventListener("input", mcalc); mcalc();', '  if (mcLab && mcM) { mcLab.addEventListener("change", mcalc); mcM.addEventListener("input", mcalc); mcalc(); }')
R('      document.getElementById("stNoteT").textContent = t + ".";\n      document.getElementById("stNote").hidden = false;', '      var sn = document.getElementById("stNote"); if (sn) { document.getElementById("stNoteT").textContent = t + "."; sn.hidden = false; }')

# 3. Bloklar
bi = s.index("<body"); head = s[:bi]; body = s[bi:]
bopen = re.match(r"<body[^>]*>", body).group(0); body = body[len(bopen):]
end = body.rindex("</body>"); tail = body[end:]; body = body[:end]
parts = [p.strip("\n") for p in re.split(r'\n(?=<(?:nav class="nav"|header|section|footer|div class="ovl"|script)\b)', body)]
B, order, scripts, pre = {}, [], [], []
for p in parts:
    if not p: continue
    m = re.match(r'<(nav|header|section|footer|div|script)\b([^>]*)>', p)
    if not m: pre.append(p); continue
    tag, attrs = m.groups(); idm = re.search(r'id="([^"]+)"', attrs)
    key = {"nav": "nav", "header": "hero", "footer": "footer", "div": "modal"}.get(tag)
    if tag == "script": scripts.append(p); continue
    if not key: key = "cta" if "cta" in attrs else (idm.group(1) if idm else "stats")
    B[key] = p; order.append(key)
print(order)

PAGES = [("index.html#labs", "Lablar", None), ("master-planner.html", "Bepul reja", None), ("qanday-ishlaydi.html", "Qanday ishlaydi", "qanday"), ("narxlar.html", "Narxlar", "narxlar"), ("savollar.html", "Savollar", "savollar")]
def nav(cur):
    tabs = '<div class="kl-tabs" role="navigation" aria-label="Sayt boʻlimlari">' + "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == cur else ""}>{t}</a>' for h, t, k in PAGES) + "</div>"
    n = re.sub(r'<div class="nav-links">.*?</div>', tabs, B["nav"], count=1, flags=re.S)
    n = n.replace('<a href="login.html" class="btn btn-g btn-sm" style="margin-left:auto">', '<span class="kl-sfx" data-sfx-slot></span><a href="login.html" class="btn btn-g btn-sm">', 1)
    return n.replace('<nav class="nav">', '<nav class="nav" data-sfx>', 1) + '\n<div class="kl-tabbar" data-sfx>' + tabs + "</div>"

def head_of(sec):
    m = re.search(r'\s*<div class="head"[^>]*>\s*<h2>(.*?)</h2>\s*(?:<p class="sub">(.*?)</p>)?\s*</div>', sec, flags=re.S)
    return (m.group(1), m.group(2) or "", sec[:m.start()] + sec[m.end():]) if m else (None, "", sec)

def pagehead(crumb, h1, lead, art):
    return f'''<header class="kl-pagehead">
  <div class="wrap">
    <nav class="kl-crumb" aria-label="Yoʻl"><a href="index.html">Kompas Lab</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>
    <div class="kl-head-row"><div><h1>{h1}</h1>{f'<p class="lead">{lead}</p>' if lead else ""}</div><img class="kl-head-art float" src="img/3d/{art}.webp" alt="" width="160" height="160"></div>
  </div>
</header>'''

UI = '<link rel="stylesheet" href="css/kompas-ui.css">\n<script src="js/kompas-ui.js"></script>\n'
def emit(fn, kind, title, desc, main):
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head, count=1)
    if desc:
        h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', h, count=1)
    h = h.replace("</head>", f'<link rel="canonical" href="https://www.kompaslab.uz/{"" if fn == "index.html" else fn[:-5]}">\n' + UI + "</head>", 1)
    b = bopen.replace("<body", f'<body data-kpage="{kind}"', 1)
    out = h + b + "\n" + "\n".join(pre) + "\n" + nav(kind) + "\n" + main + "\n" + B["cta"] + "\n" + B["footer"] + "\n" + B.get("modal", "") + "\n" + "\n".join(scripts) + "\n" + tail
    for a, t in [("#nega-lab", "qanday-ishlaydi.html"), ("#qoidalar", "qanday-ishlaydi.html#qoidalar"), ("#solishtirish", "narxlar.html#solishtirish"), ("#narx", "narxlar.html"), ("#savollar", "savollar.html")]:
        if not (kind == "qanday" and a in ("#nega-lab", "#qoidalar")) and not (kind == "narxlar" and a in ("#narx", "#solishtirish")) and not (kind == "savollar" and a == "#savollar"):
            out = out.replace(f'href="{a}"', f'href="{t}"')
    if kind != "home":
        out = out.replace('href="#labs"', 'href="index.html#labs"').replace('href="#globus"', 'href="index.html#globus"')
    (ROOT / fn).write_text(out, encoding="utf-8")
    print(fn, len(out))

NEXT = '''<section class="alt" id="keyingi">
  <div class="wrap">
    <div class="head"><h2>Batafsil</h2></div>
    <nav class="kl-next" aria-label="Sayt sahifalari">
      <a href="qanday-ishlaydi.html"><b>Qanday ishlaydi</b><span>Bepul M0, Tayyorgarlik koʻrsatkichi, modullar va ishlash qoidalari</span></a>
      <a href="narxlar.html"><b>Narxlar</b><span>Barcha Lablar narxi, eng arzon tarif kalkulyatori, agentlik bilan solishtirish</span></a>
      <a href="savollar.html"><b>Savollar</b><span>Qachon boshlash, toʻlov, kafolat va boshqa savollar</span></a>
      <a href="master-planner.html"><b>Bepul reja</b><span>Maqsad, qabul yili, saralangan roʻyxat va vazifalar</span></a>
    </nav>
  </div>
</section>'''

home = [B["hero"], B["stats"], B["globus"], B["labs"], NEXT]
emit("index.html", "home", re.search(r"<title>(.*?)</title>", head).group(1), None, "\n".join(home))

h1, lead, nega = head_of(B["nega-lab"])
emit("qanday-ishlaydi.html", "qanday", "Qanday ishlaydi · Kompas Lab", "Kompas Lab qanday ishlaydi: bepul M0, Tayyorgarlik koʻrsatkichi, modullar, topshiriqlar va ishlash qoidalari.",
     pagehead("Qanday ishlaydi", "Kompas Lab qanday ishlaydi", "Har Lab bepul qaror modulidan boshlanadi. Darslar Topshiriq bilan tugaydi, modullar tayyor hujjat bilan yopiladi.", "compass") + "\n" + nega + "\n" + B["qoidalar"])

h1, lead, narx = head_of(B["narx"])
emit("narxlar.html", "narxlar", "Narxlar · Kompas Lab", "Kompas Lab narxlari: har Lab uchun oylik va 6 oylik obuna. M0 bepul. Agentlik narxi bilan solishtirish.",
     pagehead("Narxlar", h1 or "Narxlar", lead, "money") + "\n" + narx + "\n" + B["solishtirish"])

h1, lead, sav = head_of(B["savollar"])
emit("savollar.html", "savollar", "Savollar · Kompas Lab", "Kompas Lab haqida koʻp soʻraladigan savollar: boshlash, toʻlov, obuna, kafolat va M0.",
     pagehead("Savollar", h1 or "Koʻp soʻraladigan savollar", lead, "bulb") + "\n" + sav)
