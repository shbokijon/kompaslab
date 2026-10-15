# Kompas Lab — Lab sahifalari generatori (umumiy qism)
# Ishga tushirish: python3 tools/landing/build.py  (repo ildizidan)
import re, json, html as H
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASE_CSS = (HERE / "base.css").read_text(encoding="utf-8")

EXTRA_CSS = """
.trk-h{margin:26px 0 10px;font-size:16px;font-weight:800;color:var(--accent);}
.tk{display:inline-block;font-size:11px;font-weight:700;padding:1px 6px;border-radius:5px;background:var(--accent-lit);color:var(--accent);margin-left:6px;vertical-align:1px;}
.banner{display:flex;gap:12px;align-items:flex-start;border-radius:14px;padding:14px 18px;font-size:14px;margin-bottom:22px;}
.banner.warn{background:var(--gold-lit);border:1px solid #e8d48a;}
.banner.red{background:var(--red-lit);border:1px solid #f3c3bd;}
.banner.green{background:var(--green-lit);border:1px solid #bfe3cd;}
.cmp{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--border);font-size:14px;margin-top:18px;}
.cmp th,.cmp td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--border);vertical-align:top;}
.cmp th{background:var(--accent);color:#fff;font-size:13px;}
.cmp tr:last-child td{border-bottom:none;}
.tblwrap{overflow-x:auto;border-radius:14px;max-width:100%;-webkit-overflow-scrolling:touch;}
.help{background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--red);border-radius:12px;padding:14px 18px;font-size:14px;margin-top:18px;}
.soon{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:24px;max-width:760px;}
.soon p{color:var(--muted);margin-bottom:14px;}
.phases.c4{grid-template-columns:repeat(4,minmax(0,1fr));}
@media(max-width:1000px){.phases.c4,.phases.c5{grid-template-columns:repeat(2,minmax(0,1fr));}}
@media(max-width:720px){.phases.c4,.phases.c5{grid-template-columns:minmax(0,1fr);}.cmp{min-width:520px;}}
"""

# AI-shablon belgilarini olib tashlaydigan va mobil muammolarni yopadigan qatlam
POLISH_CSS = """
:root{--bg:#f4f3ef;--border:#e2ded3;--surface:#fffefb;--gold:#8a6a10;--gold-lit:#f8f0d6;}
body{background:var(--bg);-webkit-text-size-adjust:100%;}
.nav{background:rgba(244,243,239,.94);}
h1 em,h2 em{font-style:normal;color:inherit;}
h1{letter-spacing:-.5px;}
.label{display:none;}
.badge{font-family:"Outfit",sans-serif;font-size:13px;letter-spacing:0;}
.fact b,.packet li::before,.mod-n,.mod-c,.mod li .num,.tl-when,.chk,.price,.calc b,.score-n,.tk,.lc-p,.lc-t,.st::before{font-family:"Outfit",sans-serif;font-variant-numeric:tabular-nums;letter-spacing:0;}
.packet-top small,.phase small,.art small,.plan.main .tag-top{font-family:"Outfit",sans-serif;letter-spacing:0;text-transform:none;font-size:12.5px;}
.phase small{color:var(--accent2);font-weight:700;}
.price{font-weight:800;letter-spacing:-.5px;}
.reveal{opacity:1;transform:none;transition:none;}
input,select,textarea{font-size:16px;}
.q select,.mdl input,.mdl select{font-size:16px;min-height:46px;}
.btn{min-height:44px;}
.btn-sm{min-height:40px;}
.nav .btn-p{white-space:nowrap;}
.logo-m{background:none;width:36px;height:36px;}
.logo-m img{width:34px;height:34px;display:block;}
.i3d{width:64px;height:64px;display:block;}
.hero-i{width:76px;height:76px;margin-bottom:10px;}
@media (prefers-reduced-motion: no-preference){
  .float{animation:float 6s ease-in-out infinite;}
  @keyframes float{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-6px) rotate(-3deg)}}
}
.live{display:none;align-items:center;gap:8px;font-size:13.5px;color:var(--muted);margin-top:12px;}
.live.on{display:flex;}
.live i{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 0 0 rgba(26,122,74,.5);}
@media (prefers-reduced-motion: no-preference){.live i{animation:pulse 2s infinite;}@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(26,122,74,.45)}70%{box-shadow:0 0 0 8px rgba(26,122,74,0)}100%{box-shadow:0 0 0 0 rgba(26,122,74,0)}}}
.method{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:36px;align-items:start;}
.who{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:22px;}
.who h3{font-size:16px;font-weight:800;margin-bottom:10px;}
.who ul{list-style:none;display:grid;gap:8px;}
.who li{font-size:14px;padding-left:18px;position:relative;}
.who li::before{content:"";position:absolute;left:0;top:9px;width:7px;height:7px;border-radius:2px;background:var(--accent2);}
.why-lab{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:16px 18px;font-size:14px;margin-top:18px;display:flex;gap:14px;align-items:flex-start;}
.why-lab img{width:44px;height:44px;flex-shrink:0;}
.plan .per{min-height:18px;}
.refund{margin-top:18px;background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--accent2);border-radius:12px;padding:14px 18px;font-size:14px;}
footer .wrap > div:last-child{color:rgba(255,255,255,.55);}
@media(max-width:1000px){.method{grid-template-columns:minmax(0,1fr);}}
@media(max-width:720px){
  .logo-t span{display:none;}
  .hero{padding:96px 0 48px;}
  h1{font-size:34px;}
  .lead{font-size:16px;}
  .packet li{font-size:14px;}
  .packet li span{font-size:12.5px;}
  .mod li small{font-size:13px;}
  .src p,.rules div,.calc div,.fit-col li{font-size:14.5px;}
  .nav .btn-p{padding:8px 12px;font-size:13px;}
  .cta-row .btn{width:100%;}
}
"""

ICONS = {"Bachelor": "bachelor", "Master": "master", "PhD": "phd", "GKS": "gks", "USA": "usa", "DAAD": "daad", "TT": "tt", "Musofir": "musofir"}

def esc(s):
    return H.escape(s, quote=False)

def attr(s):
    return s.replace('"', "&quot;")

def icon(name, cls="i3d", alt=""):
    return f'<img class="{cls}" src="img/3d/{name}.webp" width="160" height="160" alt="{alt}" loading="lazy" decoding="async">'

KEEP_CAPS = {"I", "II", "III", "IV", "U", "M", "D", "B", "M0", "GKS", "AQSh"}
def smallcase(s):
    s = s.replace(" · ", ", ")
    words = [w if w in KEEP_CAPS else w.lower() for w in s.split(" ")]
    out = " ".join(words)
    return out[:1].upper() + out[1:]

def fmt(n):
    return f"{n:,}".replace(",", "\u00a0")

def nav(lab):
    links = "".join(f'<a href="#{a}">{t}</a>' for a, t in lab["nav"])
    return f'''<nav class="nav">
  <div class="wrap">
    <a href="index.html" class="logo"><div class="logo-m"><img src="img/3d/compass.webp" alt="" width="34" height="34"></div><span class="logo-t">Kompas Lab <span>{lab["short"]}</span></span></a>
    <div class="nav-links">{links}</div>
    <button type="button" class="btn btn-p btn-sm" data-wl>Kutish roʻyxati</button>
  </div>
</nav>'''

def hero(lab):
    facts = "".join(f'<span class="fact">{f}</span>' for f in lab["facts"])
    pk = "".join(f"<li><div>{esc(a)}<span>{esc(b)}</span></div></li>" for a, b in lab["packet"])
    banner = ""
    if lab.get("hero_banner"):
        kind, txt = lab["hero_banner"]
        banner = f'<div class="banner {kind}" style="margin-top:4px"><span>{"⚠️" if kind != "green" else "🛡"}</span><span>{txt}</span></div>'
    return f'''<header class="hero">
  <div class="wrap hero-grid">
    <div>
      <div class="crumb"><a href="index.html#labs">Lablar</a> / {lab["axis"]} / {lab["name"]}</div>
      {icon(ICONS[lab["key"]], "hero-i float", lab["name"])}
      <h1>{lab["h1"]}</h1>
      <p class="lead">{lab["lead"]}</p>
      {banner}
      <div class="cta-row">
        <a href="#{lab["cta_anchor"]}" class="btn btn-p">{lab["cta_text"]}</a>
        <a href="#dastur" class="btn btn-g">Dasturni koʻrish</a>
      </div>
      <div class="facts">{facts}</div>
      <div class="live" data-live-wl="{lab["slug"]}"><i></i><span></span></div>
    </div>
    <aside class="packet" aria-label="{attr(lab["packet_title"])}">
      <div class="packet-top"><small>{smallcase(lab["packet_kicker"])}</small><strong>{lab["packet_title"]}</strong></div>
      <ol>{pk}</ol>
      <div class="packet-foot">{lab["packet_foot"]}</div>
    </aside>
  </div>
</header>'''

def dark_block(lab):
    d = lab["dark"]
    paras = "".join(f"<p>{p}</p>" for p in d["paras"])
    cards = "".join(f'<div class="model{" bad" if bad else ""}"><b>{esc(t)}</b><span>{esc(s)}</span></div>' for t, s, bad in d["cards"])
    sid = f' id="{lab["dark_id"]}"' if lab.get("dark_id") else ""
    return f'''<section class="dark"{sid}>
  <div class="wrap rule-box">
    <div>
      <h2>{d["title"]}</h2>
      {paras}
    </div>
    <div class="model-list">{cards}</div>
  </div>
</section>'''

def fit(lab):
    y = "".join(f"<li>{x}</li>" for x in lab["fit_yes"])
    n = "".join(f"<li>{x}</li>" for x in lab["fit_no"])
    return f'''<section>
  <div class="wrap">
    <div class="head">
      <h2>Kimga mos va kimga mos emas</h2>
      <p class="sub">Toʻlashdan oldin ochiq yozamiz. Mos kelmasangiz, toʻgʻri Lab yoki keyingi qadamni koʻrsatamiz.</p>
    </div>
    <div class="fit">
      <div class="fit-col yes"><h3>Mos keladi</h3><ul>{y}</ul></div>
      <div class="fit-col no"><h3>Mos emas</h3><ul>{n}</ul></div>
    </div>
  </div>
</section>'''

def module_html(m, free_ids=("M0",), show_trek=False, extra_tag=None):
    free = m["id"] in free_ids
    meta = m.get("meta", "")
    core = "Core" in meta
    tags = ('<span class="tag tag-free">Bepul</span>' if free else "") + ('<span class="tag tag-core">Asosiy</span>' if core else "")
    if extra_tag and not free:
        tags += f'<span class="tag tag-core">{extra_tag}</span>'
    info = m.get("info", "")
    art = ""
    mm = re.search(r"Artefakt:\s*(.*?)(?:\s*Dasturlar tafsiloti.*)?$", info.strip())
    if mm:
        art = mm.group(1).strip().rstrip(".")
    if m.get("art"):
        art = m["art"]
    sub = f'<div class="mod-a">Natija: {esc(art)}</div>' if art else ""
    lis = []
    for l in m["lessons"]:
        tk = ""
        if show_trek and l.get("trek"):
            tk = "".join(f'<span class="tk">{esc(t.strip())}</span>' for t in re.split(r"[,/ ]+", l["trek"]) if t.strip())
        small = f'<small>{esc(l["content"])}</small>' if l.get("content") else ""
        lis.append(f'<li><span class="num">{esc(l["num"])}</span>{esc(l["title"])}{tk}{small}</li>')
    return f'''<details class="mod{" free" if free else ""}"{" open" if m["id"] == "M0" else ""}>
  <summary><div class="mod-n">{esc(m["id"])}</div><div><div class="mod-t">{esc(m["title"])}</div>{sub}</div><div class="mod-c">{len(m["lessons"])} dars{tags}</div></summary>
  <ol>{"".join(lis)}</ol>
</details>'''

def program(lab, mods):
    ph = "".join(f'<div class="phase"><small>{smallcase(a)}</small><b>{esc(b)}</b><span>{esc(c.replace(" · ", ", "))}</span></div>' for a, b, c in lab["phases"])
    cols = min(len(lab["phases"]), 5)
    groups = lab.get("groups")
    kw = dict(show_trek=lab.get("show_trek", False), extra_tag=lab.get("mod_tag"))
    if groups:
        body = ""
        for title, ids in groups:
            body += f'<div class="trk-h">{title}</div><div class="mods">' + "".join(module_html(m, **kw) for m in mods if m["id"] in ids) + "</div>"
    else:
        body = '<div class="mods">' + "".join(module_html(m, **kw) for m in mods) + "</div>"
    note = f'<p class="note">{lab["program_note"]}</p>' if lab.get("program_note") else ""
    return f'''<section class="alt" id="dastur">
  <div class="wrap">
    <div class="head">
      <h2>{lab["program_title"]}</h2>
      <p class="sub">{lab["program_sub"]}</p>
    </div>
    <div class="phases c{cols}">{ph}</div>
    {body}
    {note}
  </div>
</section>'''

def facts_section(lab):
    f = lab["facts_sec"]
    cards = []
    for c in f["cards"]:
        title, status, kind, text, link = c
        a = f'<a class="s" href="{link[1]}" target="_blank" rel="noopener">{esc(link[0])}</a>' if link else ""
        cards.append(f'<div class="src"><div class="src-h"><b>{esc(title)}</b><span class="chk {kind}">{esc(status)}</span></div><p>{text}</p>{a}</div>')
    excl = f'<div class="excl">{f["excl"]}</div>' if f.get("excl") else ""
    return f'''<section class="alt" id="faktlar">
  <div class="wrap">
    <div class="head">
      <h2>{f["title"]}</h2>
      <p class="sub">{f["sub"]}</p>
    </div>
    <div class="atlas">{"".join(cards)}</div>
    {excl}
    {f.get("extra", "")}
  </div>
</section>'''

def quiz(lab):
    q = lab.get("quiz")
    if not q:
        return ""
    rows = []
    for i, it in enumerate(q["items"]):
        opts = "".join(f'<option value="{v}">{esc(t)}</option>' for t, v in it["options"])
        rows.append(f'<div class="q"><label for="q{i}">{i+1}. {esc(it["label"])} <small>({it["max"]} ball)</small></label><select id="q{i}" data-q><option value="">Tanlang</option>{opts}</select></div>')
    data = {"names": [it["label"] for it in q["items"]], "max": [it["max"] for it in q["items"]], "blockText": q.get("blockText", ""), "warn": q.get("warn", [])}
    warns = "".join(f'<div class="warn" id="w{k}">{esc(w["text"])}</div>' for k, w in enumerate(q.get("warn", [])))
    return f'''<section id="test">
  <div class="wrap">
    <div class="head">
      <h2>Tayyorgarlik darajasi (Readiness Score)</h2>
      <p class="sub">{len(q["items"])} savol, 100 ball. Bu oʻzingizni oʻzingiz baholash, qabul ehtimoli emas. Javoblar hech qayerga yuborilmaydi va saqlanmaydi.</p>
    </div>
    <div class="quiz">
      <form id="rs" autocomplete="off">{"".join(rows)}</form>
      <div class="score" aria-live="polite">
        <div class="score-n"><span id="sN">0</span><small>/100</small></div>
        <div class="bar"><i id="sB"></i></div>
        <div class="verdict" id="sV">Savollarga javob bering</div>
        <div class="verdict-t" id="sT">Natija javoblaringiz boʻyicha shu yerda hisoblanadi.</div>
        <ul class="gaps" id="sG"></ul>
        {warns}
        <button type="button" class="btn btn-p" style="width:100%;margin-top:14px" data-wl>M0 ochilganda xabar bering</button>
      </div>
    </div>
  </div>
  <script type="application/json" id="rsData">{json.dumps(data, ensure_ascii=False)}</script>
</section>'''

WHO_CARD = '''<div class="who">
      <h3>Dasturlarni kim tuzadi</h3>
      <ul>
        <li>Asoschi geofizik, Buyuk Britaniyada (University of Leeds) doktorantura oʻqiydi</li>
        <li>Janubiy Koreyada oʻqigan</li>
        <li>Oʻzbekistonda universitetda dars bergan</li>
        <li>Oʻzi oʻtmagan bosqichlar boʻyicha tajriba daʼvo qilinmaydi</li>
      </ul>
    </div>'''

def method(lab):
    f = lab.get("founder")
    if not f:
        return ""
    paras = "".join(f'<p class="sub" style="margin-bottom:14px">{p}</p>' for p in f["paras"])
    return f'''<section class="alt" id="qanday">
  <div class="wrap method">
    {WHO_CARD}
    <div>
      <h2>{f["title"]}</h2>
      {paras}
    </div>
  </div>
</section>'''

def maker(lab):
    m = lab.get("maker")
    if not m:
        return ""
    paras = "".join(f"<p>{p}</p>" for p in m["paras"])
    return f'''<section class="alt" id="qanday">
  <div class="wrap">
    <div class="soon">
      <h2 style="font-size:28px">{m["title"]}</h2>
      {paras}
    </div>
  </div>
</section>'''

def std_calc(y, m):
    ratio = y / m
    months = int(ratio) + 1
    return [(f"{fmt(m * 12)} soʻm", f"oylik reja 12 oyda ({fmt(m)} × 12)"),
            (f"~{ratio:.1f} oy".replace(".", ","), "yillik reja oylik rejaning shuncha oyiga teng"),
            (f"{months} oy va undan koʻp", "obuna shuncha davom etsa, yillik reja arzonroq")]

REFUND = "<b>Toʻlov qaytarilmaydi.</b> Shuning uchun har Labning M0 qismi bepul: toʻlashdan oldin dastur sizga mosligini tekshirasiz. Oylik obunani istalgan oyda toʻxtatasiz, keyingi oy uchun pul yechilmaydi."

def pricing(lab):
    p = lab["pricing"]
    slug = lab["slug"]
    y, mo = p["yearly"], p["monthly"]
    plans = f'''<div class="plans">
      <div class="plan">
        <h3>M0, qaror moduli</h3><p class="desc">{p["m0_desc"]}</p>
        <div class="price">0</div><div class="per">soʻm, muddatsiz</div>
        <ul>{"".join(f"<li>{x}</li>" for x in p["m0_items"])}</ul>
        <button type="button" class="btn btn-g" data-wl>Ochilganda xabar bering</button>
      </div>
      <div class="plan main">
        <span class="tag-top">Asosiy reja</span>
        <h3>Yillik</h3><p class="desc">{p["y_desc"]}</p>
        <div class="price" data-py="{slug}">{fmt(y)}</div><div class="per">soʻm, 12 oy uchun</div>
        <ul>{"".join(f"<li>{x}</li>" for x in p["y_items"])}</ul>
        <button type="button" class="btn btn-p" data-wl>Kutish roʻyxatiga yozilish</button>
      </div>
      <div class="plan">
        <h3>Oylik</h3><p class="desc">Sinab koʻrish yoki qisqa muddat uchun</p>
        <div class="price" data-pm="{slug}">{fmt(mo)}</div><div class="per">soʻm, har oy</div>
        <ul>{"".join(f"<li>{x}</li>" for x in p["m_items"])}</ul>
        <button type="button" class="btn btn-g" data-wl>Kutish roʻyxatiga yozilish</button>
      </div>
    </div>
    <div class="calc">{"".join(f"<div><b>{a}</b>{b}</div>" for a, b in std_calc(y, mo))}</div>'''
    if p.get("pre_html"):
        plans = p["pre_html"] + plans
    rules = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in p["rules"])
    status = p.get("status", "<b>Onlayn toʻlov hali ochilmagan.</b> Kutish roʻyxatidagilarga ochilish haqida birinchi boʻlib xabar beramiz. Hozir hech qanday toʻlov qabul qilinmaydi.")
    return f'''<section id="narx">
  <div class="wrap">
    <div class="head">
      <h2>Obuna: yillik yoki oylik. M0 bepul.</h2>
      <p class="sub">{p["sub"]}</p>
    </div>
    <div class="pay-status"><span>⏳</span><span>{status}</span></div>
    {plans}
    <div class="refund">{REFUND}</div>
    <div class="rules">{rules}</div>
  </div>
</section>'''

WHY_LAB_FAQ = ("Nega “Lab” deyiladi?", "Lab soʻzi laboratoriyadan olingan. Laboratoriyada bilim tajriba bilan olinadi: savol qoʻyiladi, sinab koʻriladi, natija oʻlchanadi. Kompas Lablari ham shunday ishlaydi: har dars Topshiriq bilan tugaydi, har modul bitta tayyor hujjat bilan yopiladi va hujjat baholash mezoni (rubrika) bilan tekshiriladi.")

def faq(lab):
    items = "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in lab["faq"] + [WHY_LAB_FAQ])
    src = ", ".join(f'<a href="{u}" target="_blank" rel="noopener">{esc(t)}</a>' for t, u in lab.get("sources", []))
    srcp = f'<p class="sources" style="text-align:center">Manbalar: {src}</p>' if src else ""
    return f'''<section id="savollar">
  <div class="wrap">
    <div class="head" style="text-align:center">
      <h2>Koʻp soʻraladigan savollar</h2>
    </div>
    <div class="faq">{items}</div>
    {srcp}
  </div>
</section>'''

FOOTER = '''<footer>
  <div class="wrap">
    <div><a href="index.html">Kompas Lab</a><a href="index.html#labs">Lablar</a><a href="login.html">Kirish</a><a href="https://t.me/kompaslab" target="_blank" rel="noopener">Telegram</a></div>
    <div>© 2026 Kompas Lab, Oʻzbekiston</div>
  </div>
</footer>'''

def cta(lab):
    return f'''<section class="dark cta">
  <div class="wrap">
    <h2>{lab["cta_title"]}</h2>
    <p class="sub">{lab["cta_sub"]}</p>
    <div class="cta-row" style="justify-content:center">
      <button type="button" class="btn btn-p" data-wl>Kutish roʻyxatiga yozilish</button>
      <a href="https://t.me/kompaslab" class="btn btn-g" target="_blank" rel="noopener">Telegramda savol berish</a>
    </div>
  </div>
</section>
{FOOTER}'''

def modal(lab):
    return f'''<div class="ovl" id="wl" role="dialog" aria-modal="true" aria-labelledby="wlT">
  <div class="mdl">
    <button type="button" class="x" id="wlX" aria-label="Yopish">×</button>
    {icon(ICONS[lab["key"]], "i3d", "")}
    <h3 id="wlT" style="margin-top:6px">{lab["name"]}: kutish roʻyxati</h3>
    <p>{lab["wl_text"]} Email boshqa maqsadda ishlatilmaydi.</p>
    <input type="email" id="wlE" placeholder="email@gmail.com" aria-label="Email" autocomplete="email" inputmode="email">
    <div id="wlMsg"></div>
    <button type="button" class="btn btn-p" id="wlB">Roʻyxatga yozilish</button>
  </div>
</div>'''

# Jonli narx va kutish roʻyxati soni: Supabase kompas_public_stats() dan.
# Ulanish boʻlmasa, sahifadagi statik qiymatlar qoladi.
LIVE_JS = '''
  var LIVE_MIN = 10;
  function nf(n) { return String(Math.round(n)).replace(/\\B(?=(\\d{3})+(?!\\d))/g, "\\u00a0"); }
  function applyStats(d) {
    var pr = d.prices || {};
    document.querySelectorAll("[data-py]").forEach(function (el) { var p = pr[el.getAttribute("data-py")]; if (p && p.y) el.textContent = nf(p.y); });
    document.querySelectorAll("[data-pm]").forEach(function (el) { var p = pr[el.getAttribute("data-pm")]; if (p && p.m) el.textContent = nf(p.m); });
    var wl = d.waitlist_by_lab || {};
    document.querySelectorAll("[data-live-wl]").forEach(function (el) {
      var n = wl[el.getAttribute("data-live-wl")] || 0;
      if (n >= LIVE_MIN) { el.querySelector("span").textContent = "Kutish roʻyxatida " + nf(n) + " kishi"; el.classList.add("on"); }
    });
    if (window.onKompasStats) window.onKompasStats(d);
  }
  if (window.supabase && typeof window.supabase.rpc === "function") {
    window.supabase.rpc("kompas_public_stats").then(function (r) { if (!r.error && r.data) applyStats(r.data); });
  }
'''

WL_JS = '''
  var ovl = document.getElementById("wl"), sel = document.getElementById("wlL"), inp = document.getElementById("wlE"), msg = document.getElementById("wlMsg"), btn = document.getElementById("wlB");
  var BTN = "Roʻyxatga yozilish";
  function openWl(slug) {
    if (sel) sel.value = slug || "";
    inp.value = ""; msg.textContent = ""; btn.disabled = false; btn.textContent = BTN;
    ovl.classList.add("open"); document.body.style.overflow = "hidden";
    setTimeout(function () { (sel && !sel.value ? sel : inp).focus(); }, 120);
  }
  function closeWl() { ovl.classList.remove("open"); document.body.style.overflow = ""; }
  document.querySelectorAll("[data-wl]").forEach(function (b) { b.addEventListener("click", function () { openWl(b.getAttribute("data-wl")); }); });
  document.getElementById("wlX").addEventListener("click", closeWl);
  ovl.addEventListener("click", function (e) { if (e.target === ovl) closeWl(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeWl(); });
  inp.addEventListener("keydown", function (e) { if (e.key === "Enter") submit(); });
  btn.addEventListener("click", submit);
  function submit() {
    var slug = sel ? sel.value : SLUG, email = inp.value.trim();
    if (!slug) { msg.style.color = "var(--red)"; msg.textContent = "Labni tanlang"; return; }
    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) { msg.style.color = "var(--red)"; msg.textContent = "Email manzilni tekshiring: masalan, ism@gmail.com"; return; }
    if (!window.supabase || typeof window.supabase.from !== "function") { msg.style.color = "var(--red)"; msg.textContent = "Ulanib boʻlmadi. Telegram orqali yozing: t.me/kompaslab"; return; }
    btn.disabled = true; btn.textContent = "Saqlanmoqda...";
    window.supabase.from("waitlist")
      .upsert({ email: email, course_slug: slug, source: SOURCE }, { onConflict: "email,course_slug", ignoreDuplicates: true })
      .then(function (r) {
        if (r.error && r.error.code !== "23505") throw r.error;
        msg.style.color = "var(--green)"; msg.textContent = "Yozildingiz. Lab ochilganda shu emailga xabar beramiz.";
        btn.textContent = "Yozildingiz"; setTimeout(closeWl, 2400);
      })
      .catch(function () { msg.style.color = "var(--red)"; msg.textContent = "Saqlanmadi. Internetni tekshirib, qayta urinib koʻring."; btn.disabled = false; btn.textContent = BTN; });
  }
'''

QUIZ_JS = '''
  var dataEl = document.getElementById("rsData");
  if (dataEl) {
    var D = JSON.parse(dataEl.textContent);
    var sels = Array.prototype.slice.call(document.querySelectorAll("select[data-q]"));
    var shown = 0, raf = null;
    function animateTo(n) {
      var el = document.getElementById("sN"), from = shown, t0 = null;
      if (raf) cancelAnimationFrame(raf);
      if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) { el.textContent = n; shown = n; return; }
      function step(ts) { if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / 400); shown = Math.round(from + (n - from) * k); el.textContent = shown; if (k < 1) raf = requestAnimationFrame(step); }
      raf = requestAnimationFrame(step);
    }
    var calc = function () {
      var total = 0, answered = 0, gaps = [], blocked = false;
      sels.forEach(function (s, i) {
        if (s.value === "") return;
        answered++;
        if (s.value === "x") { blocked = true; gaps.push(D.names[i]); return; }
        var v = parseInt(s.value, 10); total += v;
        if (v < D.max[i] * 0.5) gaps.push(D.names[i]);
      });
      var bar = document.getElementById("sB"), V = document.getElementById("sV"), T = document.getElementById("sT"), G = document.getElementById("sG");
      animateTo(total);
      bar.style.width = total + "%"; G.innerHTML = ""; V.style.color = "";
      if (blocked) {
        V.textContent = "Bu siklda topshira olmaysiz"; V.style.color = "var(--red)";
        T.textContent = D.blockText; bar.style.background = "var(--red)";
      } else if (answered < sels.length) {
        V.textContent = "Javoblar: " + answered + " / " + sels.length;
        T.textContent = "Barcha savollarga javob bering."; bar.style.background = "var(--muted2)";
      } else if (total >= 70) {
        V.textContent = "Hozir boshlash mumkin"; V.style.color = "var(--green)";
        T.textContent = "Asosiy yoʻnalishlar yetarli. M0 da shaxsiy vaqt chizigʻingizni tuzasiz."; bar.style.background = "var(--green)";
      } else if (total >= 45) {
        V.textContent = "Avval boʻshliqlarni yoping"; V.style.color = "var(--gold)";
        T.textContent = "Boshlash mumkin, lekin quyidagi yoʻnalishlarga reja kerak:"; bar.style.background = "var(--gold)";
      } else {
        V.textContent = "Bu siklga erta"; V.style.color = "var(--red)";
        T.textContent = "Hozir toʻlash tavsiya etilmaydi. Avval quyidagi boʻshliqlarni yoping:"; bar.style.background = "var(--red)";
      }
      if (answered === sels.length && (blocked || total < 70)) {
        gaps.forEach(function (g) { var li = document.createElement("li"); li.textContent = g; G.appendChild(li); });
      }
      (D.warn || []).forEach(function (w, k) {
        var el = document.getElementById("w" + k);
        if (el) el.style.display = (sels[w.q] && sels[w.q].value === w.v) ? "block" : "none";
      });
    };
    sels.forEach(function (s) { s.addEventListener("change", calc); });
  }
'''

def script(slug, source):
    return ('<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js"></script>\n'
            '<script src="js/config.js"></script>\n<script>\n(function () {\n'
            f'  var SLUG = "{slug}", SOURCE = "{source}";\n' + QUIZ_JS + WL_JS + LIVE_JS + '})();\n</script>')

# ── Matn qatlami: oʻzbek tili qoidalari va AI-shablonlarni tozalash ──
TERMS = [  # (inglizcha atama, oʻzbekcha izoh) — matnda birinchi oʻzbekcha, keyin qavsda inglizcha
    ("Readiness Score", "tayyorgarlik darajasi"),
]

def _term_fix(text):
    for en, uz in TERMS:
        def rep(m):
            start = m.start()
            before = text[max(0, start - 40):start]
            if before.rstrip().endswith("(") or uz.lower() in before.lower():
                return m.group(0)
            cap = start == 0 or re.search(r"[.!?:]\s*$|^\s*$", text[:start]) is not None
            u = uz[:1].upper() + uz[1:] if cap else uz
            return f"{u} ({en})"
        text = re.sub(re.escape(en), rep, text)
    return text

def polish(html):
    # 1) eyebrow yorliqlarini olib tashlash
    html = re.sub(r'\s*<div class="label"[^>]*>.*?</div>', "", html)
    # 2) sarlavhalardagi alohida urgʻu (em) ni olib tashlash
    def unem(m):
        return re.sub(r"</?em>", "", m.group(0)).replace(" — ", ": ")
    html = re.sub(r"<h[12][^>]*>.*?</h[12]>|<title>.*?</title>", unem, html, flags=re.S)
    # 3) faqat koʻrinadigan matnda: tugmadagi strelka, " · " ajratgich, atamalar
    parts = re.split(r"(<script\b.*?</script>|<style\b.*?</style>)", html, flags=re.S)
    for i in range(0, len(parts), 2):
        def txt(m):
            t = m.group(1)
            t = re.sub(r"\s*→\s*$", "", t)
            t = t.replace(" · ", ", ")
            if len(t.strip()) <= 48 or "qoldiring — " in t or "yoziling — " in t:
                t = t.replace(" — ", ": ")
            t = _term_fix(t)
            return ">" + t + "<"
        parts[i] = re.sub(r">([^<>]+)<", txt, parts[i])
    return "".join(parts)

def uz_fix(s):
    # kod faqat qoʻsh qoʻshtirnoq ishlatadi; har ASCII bitta qoʻshtirnoq — oʻzbekcha matn
    s = s.replace("&#x27;", "'")
    s = re.sub(r"([oOgG])['\u2018\u2019\u02BC`]", "\\1\u02BB", s)
    return s.replace("'", "\u02BC").replace("\u2019", "\u02BC")

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=DM+Serif+Display&display=swap" rel="stylesheet">'

def head(title, meta, og_title, css):
    return f'''<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#2d4a3e">
<title>{title}</title>
<meta name="description" content="{attr(meta)}">
<meta property="og:title" content="{attr(og_title)}">
<meta property="og:description" content="{attr(meta)}">
<meta property="og:type" content="website">
<link rel="icon" href="img/3d/compass.webp" type="image/webp">
{FONTS}
<style>{css}</style>
</head>
<body>
'''

def page(lab, mods):
    body = "\n".join([
        nav(lab), hero(lab), dark_block(lab), fit(lab), program(lab, mods),
        lab.get("extra_after_program", ""), facts_section(lab), quiz(lab),
        method(lab), maker(lab), pricing(lab), faq(lab), cta(lab), modal(lab),
        script(lab["slug"], lab["source"]),
    ])
    h = head(lab["title"], lab["meta"], lab["name"] + " | Kompas Lab", BASE_CSS + EXTRA_CSS + POLISH_CSS)
    return uz_fix(polish(h + body + "\n</body>\n</html>\n"))
