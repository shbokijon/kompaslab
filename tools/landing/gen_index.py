# Kompas Lab — umumiy bosh sahifa (index.html)
from render import BASE_CSS, EXTRA_CSS, POLISH_CSS, ROOT, head, FOOTER, WL_JS, LIVE_JS, icon, fmt, polish, uz_fix, esc

# Bitta manba: katalog, kompas, narx jadvali va kutish roʻyxati shu roʻyxatdan quriladi.
# Narxlar bu yerda zaxira; jonli qiymat Supabase courses jadvalidan keladi.
LABS = [
    dict(slug="bachelor-lab", name="Bachelor Lab", icon="bachelor", page="bachelor-lab.html", group=0, ang=0,
         who="10–11-sinf, litsey va kollej, 15–19 yosh", chips=["17 modul", "86 dars"], lessons=86,
         text="Universitet tanlash, testlar rejasi, insho, tavsiya xatlari va 4 yillik moliyaviy reja. 18 yoshgacha obunani ota-ona rasmiylashtiradi.",
         why="Xorijiy bakalavriatga: universitet tanlashdan topshirishgacha.", y=899000, m=99000, status="Kutish roʻyxati"),
    dict(slug="master-lab", name="Master Lab", icon="master", page="master-lab.html", group=0, ang=45,
         who="Xorijiy magistraturaga topshiruvchilar", chips=["9 modul", "59 dars"], lessons=59,
         text="Akademik CV, tavsiya xatlari, maqsad bayonnomasi (SoP), ilmiy loyiha taklifi va stipendiya portfeli.",
         why="Magistratura: yoʻnalish, hujjatlar, stipendiya, viza va joʻnash.", y=899000, m=99000, status="Kutish roʻyxati"),
    dict(slug="phd-lab", name="PhD Lab", icon="phd", page="phd-lab.html", group=0, ang=90,
         who="Moliyalashtirilgan doktorantura", chips=["9 modul", "65 dars"], lessons=65,
         text="Ilmiy savol, ilmiy rahbarlar jadvali, professorlarga xat, ilmiy loyiha taklifi va moliyalashtirish atlasi.",
         why="Doktorantura: ilmiy savoldan ilmiy rahbar va loyiha taklifigacha.", y=1499000, m=149000, status="Kutish roʻyxati"),
    dict(slug="gks-lab", name="GKS Lab", icon="gks", page="gks-lab.html", group=1, ang=135,
         who="Koreya: Global Korea Scholarship", chips=["3 trek", "54 dars"], lessons=54,
         text="Muvofiqlik M0 da toʻlovdan oldin tekshiriladi. Umumiy oʻzak va oʻz trekingiz: bakalavriat, magistratura yoki doktorantura.",
         why="Koreya hukumati stipendiyasi: muvofiqlik, hujjatlar va intervyu.", y=899000, m=99000, status="Kutish roʻyxati"),
    dict(slug="usa-lab", name="USA Lab", icon="usa", page="usa-lab.html", group=1, ang=180,
         who="AQSh: Global UGRAD, Fulbright, doktorantura", chips=["12 modul", "72 dars"], lessons=72,
         text="Uch moliyalashtirilgan yoʻl: muvofiqlik, insholar, intervyu va viza. B trek uchun toʻlov UGRAD sikli eʼlon qilingandan keyin.",
         why="AQShda moliyalashtirilgan oʻqishning uch yoʻli.", y=899000, m=99000, status="B trek: sikl kutilmoqda"),
    dict(slug="daad-lab", name="DAAD Lab", icon="daad", page="daad-lab.html", group=1, ang=225,
         who="Germaniya: magistratura va doktorantura", chips=["9 modul", "51 dars"], lessons=51,
         text="Germaniya akademik tizimi, ilmiy rahbarni oldindan topish, motivatsion xat va tadqiqot rejasi, DAAD portali va joʻnash.",
         why="Germaniya va DAAD: ilmiy rahbardan vizagacha.", y=899000, m=99000, status="Kutish roʻyxati"),
    dict(slug="tadbirkor-talaba", name="Tadbirkor Talaba", icon="tt", page="tadbirkor-talaba.html", group=2, ang=270,
         who="Universitet talabalari, 18 yoshdan", chips=["10 modul", "54 dars"], lessons=54,
         text="Oʻqishni toʻxtatmasdan kichik, qonuniy biznes sinovi: muammo, birinchi mijoz, pul hisobi, huquqiy shakl va soliq.",
         why="Oʻqish bilan birga kichik, qonuniy biznes sinovi.", y=299000, m=29000, status="Ishlab chiqilmoqda"),
    dict(slug="miggo", name="Musofir Lab", icon="musofir", page="musofir-lab.html", group=2, ang=315,
         who="Xorijda rasmiy ish: Koreya, Buyuk Britaniya, Germaniya, Polsha", chips=["8 modul", "44 dars"], lessons=44,
         text="Rasmiy yoʻllar va firibgarlik belgilari. M0 bepul, roʻyxatdan oʻtib ochiladi. Kompas ish yoki viza topib bermaydi.",
         why="Xorijda faqat rasmiy yoʻl bilan ishlash va firibgarlikdan himoya.", y=499000, m=49000, status="M0 tayyorlanmoqda"),
]
MIYA = dict(slug="ikki-miya", name="2-Miya", icon="miya", who="Bilimni tizimlashtirish (PKM)",
            text="Ikkinchi miya: oʻqiganlaringizni yozib borish, bogʻlash va qayta topish tizimi.")
GROUPS = ["Daraja boʻyicha", "Davlat va stipendiya boʻyicha", "Talaba hayoti va ish"]
TOTAL_LESSONS = sum(l["lessons"] for l in LABS)

IDX_CSS = """
.hx{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:44px;align-items:start;position:relative;}
.motto{display:inline-block;font-size:13px;font-weight:700;color:var(--accent2);margin-bottom:14px;}
.finder{margin-top:26px;display:grid;gap:18px;}
.fq b{display:block;font-size:14px;font-weight:800;margin-bottom:8px;color:var(--accent);}
.chips{display:flex;flex-wrap:wrap;gap:8px;}
.chip{font-family:"Outfit","IBM Plex Sans",sans-serif;font-size:14px;font-weight:600;padding:9px 14px;min-height:42px;border-radius:999px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;transition:background .15s,border-color .15s,color .15s;}
.chip:hover{border-color:var(--accent);}
.chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#fff;}
.chip:focus-visible,.seg button:focus-visible,.lc-b:focus-visible,.btn:focus-visible{outline:3px solid var(--accent2);outline-offset:2px;}
.dial{position:relative;width:min(340px,82vw);aspect-ratio:1/1;margin:0 auto;}
.dial svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible;}
.pt{position:absolute;width:15%;height:15%;transform:translate(-50%,-50%);transition:transform .35s ease,opacity .35s ease;opacity:.55;}
.pt img{width:100%;height:100%;display:block;}
.pt.on{transform:translate(-50%,-50%) scale(1.3);opacity:1;}
.dial.idle .pt{opacity:.9;}
#needle{transform-box:view-box;transform-origin:170px 170px;transition:transform 1.2s cubic-bezier(.25,1.6,.45,1);}
@media (prefers-reduced-motion: no-preference){
  .dial.idle .sway{animation:sway 4.5s ease-in-out infinite;transform-box:view-box;transform-origin:170px 170px;}
  @keyframes sway{0%,100%{transform:rotate(-14deg)}50%{transform:rotate(16deg)}}
}
@media (prefers-reduced-motion: reduce){#needle{transition:none;}}
.result{margin-top:18px;background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:18px 20px;min-height:132px;}
.result .r-h{display:flex;gap:12px;align-items:center;margin-bottom:8px;}
.result .r-h img{width:52px;height:52px;}
.result .r-n{font-size:20px;font-weight:900;color:var(--accent);line-height:1.15;}
.result .r-w{font-size:13.5px;color:var(--muted);}
.result p{font-size:14.5px;margin-bottom:12px;}
.result .r-p{font-size:14px;font-weight:700;margin-bottom:12px;font-variant-numeric:tabular-nums;}
.result .r-a{display:flex;gap:10px;flex-wrap:wrap;}
.result .empty{color:var(--muted);font-size:14.5px;}
.result .note2{font-size:13px;color:var(--gold);background:var(--gold-lit);border-radius:10px;padding:8px 12px;margin-bottom:12px;}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:0;border:1px solid var(--border);border-radius:18px;background:var(--surface);overflow:hidden;}
.stat{padding:22px 20px;box-shadow:1px 1px 0 var(--border);}
.stat b{display:block;font-family:"Cambria","Caladea","Playfair Display",serif;font-weight:400;font-size:44px;line-height:1;color:var(--accent);font-variant-numeric:tabular-nums;}
.stat span{display:block;font-size:13.5px;color:var(--muted);margin-top:8px;}
.stat[hidden]{display:none;}
.stats-note{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted);margin-top:12px;}
.stats-note[hidden]{display:none;}
.stats-note i{width:8px;height:8px;border-radius:50%;background:var(--green);}
.grp-h{font-size:17px;font-weight:800;color:var(--accent);margin:34px 0 14px;}
.grp-h:first-of-type{margin-top:0;}
.labs-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;}
.lc{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:20px;display:flex;flex-direction:column;gap:10px;}
.lc-h{display:flex;gap:12px;align-items:center;}
.lc-h img{width:56px;height:56px;flex-shrink:0;}
.lc-n{font-weight:900;font-size:18px;color:var(--accent);line-height:1.2;}
.lc-w{font-size:13px;color:var(--muted);}
.lc-m{display:flex;flex-wrap:wrap;gap:6px;}
.lc-t{font-size:12px;font-weight:700;padding:3px 9px;border-radius:7px;background:var(--bg);border:1px solid var(--border);}
.lc-t.free{background:var(--green-lit);color:var(--green);border-color:transparent;}
.lc-t.soon{background:var(--gold-lit);color:var(--gold);border-color:transparent;}
.lc p{font-size:14px;line-height:1.55;}
.lc-f{margin-top:auto;padding-top:12px;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;}
.lc-p{font-weight:800;font-size:15px;color:var(--accent);line-height:1.3;}
.lc-p small{display:block;font-weight:600;font-size:12px;color:var(--muted);}
.lc-b{display:inline-flex;align-items:center;min-height:42px;padding:9px 16px;border-radius:10px;border:1.5px solid var(--accent);background:var(--surface);color:var(--accent);font-weight:800;font-size:14px;text-decoration:none;cursor:pointer;font-family:"Outfit","IBM Plex Sans",sans-serif;white-space:nowrap;}
.lc-b:hover{background:var(--accent);color:#fff;}
.whylab{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:40px;align-items:start;}
.whylab .bulb{width:72px;height:72px;margin-bottom:8px;}
.whylab p{color:var(--muted);margin-bottom:12px;font-size:16px;}
.steps{list-style:none;display:grid;gap:0;counter-reset:s;border-left:2px solid var(--border);}
.steps li{counter-increment:s;position:relative;padding:0 0 22px 26px;}
.steps li:last-child{padding-bottom:0;}
.steps li::before{content:counter(s);position:absolute;left:-15px;top:0;width:28px;height:28px;border-radius:50%;background:var(--accent);color:#fff;font-weight:800;font-size:13px;display:flex;align-items:center;justify-content:center;}
.steps b{display:block;font-size:16px;margin-bottom:2px;}
.steps span{font-size:14.5px;color:var(--muted);}
.cmpc{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:20px;align-items:stretch;}
.cmpc .in{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:22px;}
.cmpc label{display:block;font-size:14px;font-weight:800;color:var(--accent);margin:0 0 8px;}
.cmpc .row{display:flex;gap:8px;margin-bottom:14px;}
.cmpc input,.cmpc select{width:100%;min-height:48px;padding:10px 14px;border:2px solid var(--border);border-radius:12px;font-family:"Outfit","IBM Plex Sans",sans-serif;font-size:17px;background:var(--bg);color:var(--text);}
.cmpc input:focus,.cmpc select:focus{outline:none;border-color:var(--accent);background:#fff;}
.seg{display:inline-flex;border:2px solid var(--border);border-radius:12px;overflow:hidden;flex-shrink:0;background:var(--bg);}
.seg button{font-family:"Outfit","IBM Plex Sans",sans-serif;font-size:15px;font-weight:700;padding:0 14px;min-height:44px;border:none;background:none;color:var(--muted);cursor:pointer;}
.seg button[aria-pressed="true"]{background:var(--accent);color:#fff;}
.quick{display:flex;flex-wrap:wrap;gap:6px;margin:-4px 0 14px;font-size:13px;color:var(--muted);align-items:center;}
.quick button{font-family:"Outfit","IBM Plex Sans",sans-serif;font-size:13px;font-weight:600;padding:6px 10px;border-radius:8px;border:1px solid var(--border);background:var(--bg);cursor:pointer;color:var(--text);min-height:34px;}
.out{background:var(--accent);color:#fff;border-radius:18px;padding:24px;display:flex;flex-direction:column;justify-content:center;}
.out .big{font-family:"Cambria","Caladea","Playfair Display",serif;font-size:56px;line-height:1;font-variant-numeric:tabular-nums;}
.out .big small{font-family:"Outfit","IBM Plex Sans",sans-serif;font-size:18px;font-weight:700;margin-left:6px;}
.out p{color:rgba(255,255,255,.78);font-size:15px;margin-top:10px;}
.out .muted{color:rgba(255,255,255,.6);font-size:13px;}
.honest{margin-top:18px;display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.honest div{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:14px 16px;font-size:14px;}
.honest b{display:block;color:var(--accent);margin-bottom:3px;}
.ptop{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:14px;}
.ptbl td.p{font-weight:800;font-variant-numeric:tabular-nums;white-space:nowrap;}
.ptbl .pm{display:none;}
.ptbl.monthly .py{display:none;}
.ptbl.monthly .pm{display:inline;}
.ptbl td img{width:28px;height:28px;vertical-align:middle;margin-right:8px;}
.ptbl td:first-child{white-space:nowrap;}
.dark .who2{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:16px;padding:18px 20px;margin-top:10px;}
.dark .who2 b{display:block;margin-bottom:8px;}
.dark .who2 li{font-size:14px;color:rgba(255,255,255,.75);margin-left:18px;margin-bottom:4px;}
.mdl select{width:100%;padding:12px 14px;border:2px solid var(--border);border-radius:12px;font-family:"Outfit","IBM Plex Sans",sans-serif;background:var(--bg);margin-bottom:10px;}
@media(max-width:1000px){.hx,.whylab,.cmpc{grid-template-columns:minmax(0,1fr);}.labs-g{grid-template-columns:repeat(2,minmax(0,1fr));}}
@media(max-width:720px){.labs-g,.honest{grid-template-columns:minmax(0,1fr);}.nav .btn-g{display:none;}.stat b{font-size:36px;}.out .big{font-size:46px;}.chip{font-size:14px;padding:8px 12px;}.ptbl{min-width:0;font-size:13.5px;}.ptbl td,.ptbl th{padding:10px 8px;}.ptbl td img{width:22px;height:22px;margin-right:6px;}}
"""

def chips_html(l):
    t = "".join(f'<span class="lc-t">{c}</span>' for c in l["chips"]) + '<span class="lc-t free">M0 bepul</span>'
    if l["status"] not in ("Kutish roʻyxati",):
        t += f'<span class="lc-t soon">{l["status"]}</span>'
    return t

def lab_card(l):
    return f'''<div class="lc"><div class="lc-h">{icon(l["icon"], "", "")}<div><div class="lc-n">{l["name"]}</div><div class="lc-w">{l["who"]}</div></div></div>
<div class="lc-m">{chips_html(l)}</div><p>{l["text"]}</p>
<div class="lc-f"><div class="lc-p"><span data-py="{l["slug"]}">{fmt(l["y"])}</span> soʻm/yil<small>yoki <span data-pm="{l["slug"]}">{fmt(l["m"])}</span> soʻm/oy</small></div><a class="lc-b" href="{l["page"]}">Batafsil</a></div></div>'''

def miya_card():
    return f'''<div class="lc"><div class="lc-h">{icon(MIYA["icon"], "", "")}<div><div class="lc-n">{MIYA["name"]}</div><div class="lc-w">{MIYA["who"]}</div></div></div>
<div class="lc-m"><span class="lc-t soon">Rejalashtirilgan</span></div><p>{MIYA["text"]}</p>
<div class="lc-f"><div class="lc-p">Narx eʼlon qilinadi</div><button type="button" class="lc-b" data-wl="{MIYA["slug"]}">Xabar bering</button></div></div>'''

def catalog():
    out = ""
    for gi, g in enumerate(GROUPS):
        cards = "".join(lab_card(l) for l in LABS if l["group"] == gi)
        if gi == 2:
            cards += miya_card()
        out += f'<h3 class="grp-h">{g}</h3><div class="labs-g">{cards}</div>'
    return out

def dial_html():
    import math
    pts = ""
    for l in LABS:
        a = math.radians(l["ang"])
        x = 50 + 38.5 * math.sin(a)
        y = 50 - 38.5 * math.cos(a)
        pts += f'<span class="pt" data-slug="{l["slug"]}" style="left:{x:.2f}%;top:{y:.2f}%">{icon(l["icon"], "", l["name"])}</span>'
    ticks = ""
    for i in range(72):
        a = math.radians(i * 5)
        r1, r2 = (88, 100) if i % 9 == 0 else (93, 100)
        x1, y1 = 170 + r1 * math.sin(a), 170 - r1 * math.cos(a)
        x2, y2 = 170 + r2 * math.sin(a), 170 - r2 * math.cos(a)
        w = 2 if i % 9 == 0 else 1
        ticks += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#2d4a3e" stroke-opacity=".35" stroke-width="{w}"/>'
    return f'''<div class="dial idle" id="dial" aria-hidden="true">
  <svg viewBox="0 0 340 340" role="presentation">
    <circle cx="170" cy="170" r="166" fill="#fffefb" stroke="#e2ded3" stroke-width="2"/>
    <circle cx="170" cy="170" r="104" fill="none" stroke="#e2ded3" stroke-width="1.5"/>
    {ticks}
    <text x="170" y="94" text-anchor="middle" font-family="Outfit" font-size="12" font-weight="800" fill="#c4622d">N</text>
    <g id="needle"><g class="sway">
      <polygon points="170,92 180,170 160,170" fill="#c4622d"/>
      <polygon points="170,248 180,170 160,170" fill="#2d4a3e"/>
    </g></g>
    <circle cx="170" cy="170" r="9" fill="#fffefb" stroke="#2d4a3e" stroke-width="3"/>
  </svg>
  {pts}
</div>'''

Q1 = [("maktab", "Maktab yoki litsey oʻquvchisi"), ("bakalavr", "Bakalavr talabasi yoki bitiruvchi"), ("magistr", "Magistr yoki tadqiqotchi"), ("ishchi", "Ishlayotgan mutaxassis")]
Q2 = [("oqish", "Xorijda oʻqish, davlat tanlanmagan"), ("korea", "Koreya"), ("usa", "AQSh"), ("germany", "Germaniya"), ("biznes", "Oʻqish bilan birga biznes"), ("ish", "Xorijda rasmiy ish")]

def chips(name, items):
    return "".join(f'<button type="button" class="chip" data-q="{name}" data-v="{v}" aria-pressed="false">{t}</button>' for v, t in items)

def result_blocks():
    out = ""
    for l in LABS:
        out += (f'<div class="r-b" data-r="{l["slug"]}" hidden><div class="r-h">{icon(l["icon"], "", "")}<div><div class="r-n">{l["name"]}</div><div class="r-w">{l["who"]}</div></div></div>'
                f'<p>{l["why"]}</p><div class="r-p"><span data-py="{l["slug"]}">{fmt(l["y"])}</span> soʻm/yil yoki <span data-pm="{l["slug"]}">{fmt(l["m"])}</span> soʻm/oy. M0 bepul.</div>'
                f'<div class="r-a"><a class="btn btn-p" href="{l["page"]}">{l["name"]} sahifasi</a><button type="button" class="btn btn-g" data-wl="{l["slug"]}">Kutish roʻyxati</button></div></div>')
    return out

def price_rows():
    rows = ""
    for l in LABS:
        rows += (f'<tr><td>{icon(l["icon"], "", "")}{l["name"]}</td>'
                 f'<td class="p"><span class="py"><span data-py="{l["slug"]}">{fmt(l["y"])}</span> soʻm</span><span class="pm"><span data-pm="{l["slug"]}">{fmt(l["m"])}</span> soʻm</span></td>'
                 f'<td>{l["status"]}</td></tr>')
    return rows

FAQ = [
    ("Qachon boshlash mumkin?", "Hozir kutish roʻyxati ochiq. Lablar va onlayn toʻlov ishga tushganda roʻyxatdagilarga birinchi boʻlib xabar beramiz. Har Labning M0 moduli bepul."),
    ("Obuna qanday ishlaydi?", "Har Lab alohida obuna: yillik yoki oylik. Yillik reja bitta ariza siklini qamraydi. Oylik obunani istalgan oyda toʻxtatasiz, keyingi oy uchun pul yechilmaydi. Umrbod kirish rejasi yoʻq."),
    ("Toʻlov qaytariladimi?", "Yoʻq. Shuning uchun har Labning M0 qismi bepul: toʻlashdan oldin dastur sizga mos yoki mos emasligini bilasiz."),
    ("Darslar video formatdami?", "Asosiy format: matn, interaktiv vositalar va ish jadvallari. Har dars bir xil tuzilmada: Diqqat 🔥, Asosiy qism, Xulosa va Topshiriq."),
    ("Hujjatlarni oʻrnimga yozib berasizmi?", "Yoʻq. Kompas tuzilma, baholash mezoni va tahlil beradi; matnni oʻzingiz yozasiz. Qabul yoki stipendiya kafolati berilmaydi."),
    ("18 yoshga toʻlmaganman. Qatnasha olamanmi?", "Ha: Bachelor Lab va GKS Lab bakalavriat treki maktab oʻquvchilari uchun. Obunani ota-ona yoki vasiy rasmiylashtiradi; pasport yoki attestat nusxalari yigʻilmaydi."),
    ("Bir nechta Lab kerak boʻlsa-chi?", "Daraja Labi (Bachelor, Master, PhD) va davlat Labi (GKS, USA, DAAD) birga ishlatilishi mumkin; ikkinchi Lab uchun chegirma rejalashtirilgan."),
    ("Darslar qaysi tilda?", "Oʻzbek tilida. Xalqaro atamalar avval oʻzbekcha, keyin qavsda inglizcha beriladi, masalan: ilmiy loyiha taklifi (Research Proposal)."),
]

USD = 11778.45  # Markaziy bank kursi, 2026-10-06

PAGE_JS = """
  var SLUG = "", SOURCE = "index_v4";
  var LABS = __LABS__;
  var bySlug = {}; LABS.forEach(function (l) { bySlug[l.slug] = l; });
  function nf(n) { return String(Math.round(n)).replace(/\\B(?=(\\d{3})+(?!\\d))/g, "\\u00a0"); }
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ── Kompas: ikki savol → Lab ──
  var ans = { who: "", goal: "" }, angle = 0;
  function pick() {
    var w = ans.who, g = ans.goal, note = "";
    if (!w || !g) return null;
    if (g === "ish") return { slug: "miggo" };
    if (g === "biznes") { if (w === "maktab") return { slug: "bachelor-lab", note: "Tadbirkor Talaba Lab 18 yoshdan. Hozir Bachelor Lab mosroq." }; return { slug: "tadbirkor-talaba" }; }
    if (g === "korea") return { slug: "gks-lab" };
    if (g === "usa") return w === "maktab" ? { slug: "bachelor-lab", note: "AQSh bakalavriatiga toʻliq qabul Bachelor Labda. USA Lab talabalar va bitiruvchilar uchun." } : { slug: "usa-lab" };
    if (g === "germany") return w === "maktab" ? { slug: "bachelor-lab", note: "Germaniya bakalavriati (Studienkolleg bilan) Bachelor Labda. DAAD Lab magistratura va doktorantura uchun." } : { slug: "daad-lab" };
    return { slug: { maktab: "bachelor-lab", bakalavr: "master-lab", magistr: "phd-lab", ishchi: "master-lab" }[w] };
  }
  var dial = document.getElementById("dial"), needle = document.getElementById("needle"), res = document.getElementById("result");
  function point(slug) {
    var target = bySlug[slug].ang, cur = ((angle % 360) + 360) % 360, d = target - cur;
    if (d > 180) d -= 360; if (d < -180) d += 360;
    angle += d === 0 ? 360 : d;
    dial.classList.remove("idle");
    needle.style.transform = "rotate(" + angle + "deg)";
    document.querySelectorAll(".pt").forEach(function (p) { p.classList.toggle("on", p.getAttribute("data-slug") === slug); });
  }
  function show(r) {
    document.getElementById("rEmpty").hidden = true;
    var note = document.getElementById("rNote");
    note.hidden = !r.note; note.textContent = r.note || "";
    document.querySelectorAll(".r-b").forEach(function (b) { b.hidden = b.getAttribute("data-r") !== r.slug; });
    var rect = res.getBoundingClientRect();
    if (rect.bottom > window.innerHeight && window.innerWidth < 1000) res.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "end" });
  }
  document.querySelectorAll(".chip").forEach(function (c) {
    c.addEventListener("click", function () {
      var q = c.getAttribute("data-q");
      document.querySelectorAll(".chip[data-q=" + q + "]").forEach(function (o) { o.setAttribute("aria-pressed", o === c ? "true" : "false"); });
      ans[q] = c.getAttribute("data-v");
      var r = pick();
      if (r) { point(r.slug); show(r); }
    });
  });

  // ── Agentlik narxi bilan solishtirish ──
  var USD = __USD__, cur = "uzs";
  var amt = document.getElementById("amt"), labSel = document.getElementById("cmpLab");
  var big = document.getElementById("cmpBig"), cmpT = document.getElementById("cmpT"), cmpS = document.getElementById("cmpS");
  function parseAmt() { return parseFloat((amt.value || "").replace(/[^0-9.,]/g, "").replace(/,/g, ".").replace(/\\.(?=.*\\.)/g, "")) || 0; }
  function recalc() {
    var v = parseAmt(), uzs = cur === "usd" ? v * USD : v, l = bySlug[labSel.value];
    if (!uzs || !l) { big.innerHTML = "–"; cmpT.textContent = "Agentlik aytgan narxni kiriting."; cmpS.textContent = ""; return; }
    var base = l.s6 > 0 ? l.s6 : l.m * 6, r = uzs / base;
    if (r < 1) { big.innerHTML = "–"; cmpT.textContent = "Bu narx " + l.name + " 6 oylik obunasidan (" + nf(base) + " soʻm) past."; cmpS.textContent = ""; return; }
    big.innerHTML = (r >= 10 ? nf(r) : r.toFixed(1).replace(".", ",")) + "<small>barobar</small>";
    cmpT.textContent = l.name + " 6 oylik obunasi (" + nf(base) + " soʻm) bu narxdan shuncha marta arzon.";
    cmpS.textContent = "Farq: " + nf(uzs - base) + " soʻm" + (cur === "usd" ? " (1 $ = " + nf(USD) + " soʻm, Markaziy bank, 2026-10-06)" : "");
  }
  amt.addEventListener("input", function () {
    var raw = amt.value.replace(/[^0-9]/g, "");
    if (cur === "uzs") amt.value = raw ? nf(parseInt(raw, 10)) : "";
    recalc();
  });
  labSel.addEventListener("change", recalc);
  document.querySelectorAll("[data-cur]").forEach(function (b) {
    b.addEventListener("click", function () {
      cur = b.getAttribute("data-cur");
      document.querySelectorAll("[data-cur]").forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
      amt.value = ""; amt.placeholder = cur === "usd" ? "masalan, 1 500" : "masalan, 15 000 000"; recalc(); amt.focus();
    });
  });
  document.querySelectorAll("[data-amt]").forEach(function (b) {
    b.addEventListener("click", function () {
      if (cur !== "uzs") document.querySelector("[data-cur=uzs]").click();
      amt.value = nf(parseInt(b.getAttribute("data-amt"), 10)); recalc();
    });
  });

  // ── Narx jadvali: oylik / 6 oylik ──
  document.querySelectorAll("[data-period]").forEach(function (b) {
    b.addEventListener("click", function () {
      document.querySelectorAll("[data-period]").forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
      document.getElementById("ptbl").classList.toggle("monthly", b.getAttribute("data-period") === "m");
    });
  });

  // ── Jonli hisob ──
  function countUp(el, to) {
    if (reduce || !("IntersectionObserver" in window)) { el.textContent = nf(to); return; }
    var io = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return; io.disconnect();
      var t0 = null; function step(ts) { if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / 1100); el.textContent = nf(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(step); }
      requestAnimationFrame(step);
    }, { threshold: .4 });
    io.observe(el);
  }
  document.querySelectorAll("[data-count]").forEach(function (el) { countUp(el, parseInt(el.getAttribute("data-count"), 10)); });
  window.onKompasStats = function (d) {
    var pr = d.prices || {};
    LABS.forEach(function (l) { var p = pr[l.slug]; if (p) { if (p.y) l.y = p.y; if (p.m) l.m = p.m; } });
    recalc();
    var any = false;
    [["stReg", d.registered], ["stWait", d.waitlist]].forEach(function (x) {
      var box = document.getElementById(x[0]);
      if (box && x[1] >= LIVE_MIN) { box.hidden = false; countUp(box.querySelector("b"), x[1]); any = true; }
    });
    if (any) {
      var t = "Bazadan jonli olinadi";
      if (d.last_signup) { var h = Math.floor((Date.now() - new Date(d.last_signup).getTime()) / 3600000); t += ". Oxirgi roʻyxatdan oʻtish: " + (h < 1 ? "bir soatdan kam vaqt oldin" : h < 24 ? h + " soat oldin" : Math.floor(h / 24) + " kun oldin"); }
      document.getElementById("stNoteT").textContent = t + ".";
      document.getElementById("stNote").hidden = false;
    }
  };
"""

def build():
    import json
    labs_js = json.dumps([{k: l[k] for k in ("slug", "name", "icon", "page", "who", "why", "y", "m", "ang")} for l in LABS], ensure_ascii=False)
    opt_html = "".join(f'<option value="{l["slug"]}">{l["name"]}</option>' for l in LABS) + f'<option value="{MIYA["slug"]}">{MIYA["name"]}</option>'
    cmp_opts = "".join(f'<option value="{l["slug"]}"{" selected" if l["slug"] == "master-lab" else ""}>{l["name"]}</option>' for l in LABS)
    faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in FAQ)
    css = BASE_CSS + EXTRA_CSS + POLISH_CSS + IDX_CSS
    h = head("Kompas Lab — xorijiy universitet va stipendiyaga oʻzbek tilida tayyorgarlik",
             "Bachelor, Master, PhD, GKS, USA va DAAD Lablari: xorijiy universitet va stipendiyaga oʻzbek tilida tayyorgarlik. Har Labda M0 bepul. Obuna: yillik yoki oylik.",
             "Kompas Lab", css)
    body = f'''<nav class="nav">
  <div class="wrap">
    <a href="index.html" class="logo"><div class="logo-m"><img src="img/3d/compass.webp" alt="" width="34" height="34"></div><span class="logo-t">Kompas Lab</span></a>
    <div class="nav-links"><a href="#labs">Lablar</a><a href="#nega-lab">Qanday ishlaydi</a><a href="#solishtirish">Solishtirish</a><a href="#narx">Narxlar</a><a href="#savollar">Savollar</a></div>
    <a href="login.html" class="btn btn-g btn-sm" style="margin-left:auto">Kirish</a>
    <button type="button" class="btn btn-p btn-sm" style="margin-left:0" data-wl="">Kutish roʻyxati</button>
  </div>
</nav>

<header class="hero">
  <div class="wrap hx">
    <div>
      <span class="motto">Kuzatuvdan kashfiyotga</span>
      <h1>Xorijiy universitet va stipendiyaga oʻzbek tilida tayyorlaning.</h1>
      <p class="lead">Kompas Lab STEM yoʻnalishidagi oʻquvchi va talabalar uchun onlayn dasturlar. Universitet va stipendiyani dalil bilan tanlaysiz, hujjatlarni <strong>oʻzingiz</strong> yozasiz. Har fakt rasmiy manba havolasi bilan beriladi.</p>
      <div class="facts"><span class="fact">Har Labda <b>M0 bepul</b></span><span class="fact"><b>Oʻzbek</b> tilida</span><span class="fact">Rasmiy <b>manbalar</b></span><span class="fact">Obuna: <b>yillik</b> yoki <b>oylik</b></span></div>
      <div class="finder" aria-label="Lab tanlash">
        <div class="fq"><b>1. Hozir kimsiz?</b><div class="chips">{chips("who", Q1)}</div></div>
        <div class="fq"><b>2. Maqsadingiz?</b><div class="chips">{chips("goal", Q2)}</div></div>
      </div>
    </div>
    <div>
      {dial_html()}
      <div class="result" id="result" aria-live="polite"><p class="empty" id="rEmpty">Ikki savolga javob bering: kompas sizga mos Labni koʻrsatadi.</p><div class="note2" id="rNote" hidden></div>{result_blocks()}</div>
    </div>
  </div>
</header>

<section style="padding-top:8px">
  <div class="wrap">
    <div class="stats">
      <div class="stat" id="stReg" hidden><b>0</b><span>kishi roʻyxatdan oʻtgan</span></div>
      <div class="stat" id="stWait" hidden><b>0</b><span>kishi kutish roʻyxatida</span></div>
      <div class="stat"><b data-count="{len(LABS)}">{len(LABS)}</b><span>Lab: daraja, davlat va ish boʻyicha</span></div>
      <div class="stat"><b data-count="{TOTAL_LESSONS}">{fmt(TOTAL_LESSONS)}</b><span>dars rejasi barcha Lablarda</span></div>
    </div>
    <div class="stats-note" id="stNote" hidden><i></i><span id="stNoteT"></span></div>
  </div>
</section>

<section class="alt" id="labs">
  <div class="wrap">
    <div class="head"><h2>Lablar</h2><p class="sub">Daraja Labi umumiy akademik tayyorgarlikni beradi. Davlat Labi muayyan stipendiya tizimining talablarini qoʻshadi. Har Lab bepul M0 bilan boshlanadi.</p></div>
    {catalog()}
  </div>
</section>

<section id="nega-lab">
  <div class="wrap whylab">
    <div>
      {icon("bulb", "bulb", "")}
      <h2>Nega «Lab»?</h2>
      <p>Lab soʻzi laboratoriyadan olingan. Laboratoriyada bilim tajriba bilan olinadi: savol qoʻyiladi, sinab koʻriladi, natija oʻlchanadi.</p>
      <p>Kompas Lablari ham shu tartibda ishlaydi. Har dars Topshiriq bilan tugaydi, har modul bitta tayyor hujjat bilan yopiladi va hujjat baholash mezoni (rubrika) bilan tekshiriladi. Dastur oxirida qoʻlingizda ariza paketi boʻladi.</p>
    </div>
    <ol class="steps">
      <li><b>Bepul M0</b><span>Lab nima beradi va nima bermaydi, kimga mos emasligi ochiq yozilgan.</span></li>
      <li><b>Tayyorgarlik darajasi (Readiness Score)</b><span>100 ballik oʻzini oʻzi baholash. Natija “Bu siklga erta” boʻlsa, toʻlov oʻrniga boʻshliqlar roʻyxati va muqobil yoʻl beriladi.</span></li>
      <li><b>Modullar va topshiriqlar</b><span>6 oylik obunada barcha modullar birdaniga ochiq, oylikda har toʻlov bitta fazani ochadi, keyingisi navbatdagi toʻlov bilan. Har dars: Diqqat 🔥, Asosiy qism, Xulosa, Topshiriq.</span></li>
      <li><b>Tayyor hujjatlar</b><span>CV, xatlar, insho yoki ilmiy loyiha taklifi. Matnni siz yozasiz, Kompas tuzilma va mezon beradi.</span></li>
    </ol>
  </div>
</section>

<section class="alt" id="solishtirish">
  <div class="wrap">
    <div class="head"><h2>Agentlik narxi bilan solishtiring</h2><p class="sub">Agentlik yoki konsultant aytgan narxni kiriting. Hisob shu sahifada bajariladi, hech qayerga yuborilmaydi.</p></div>
    <div class="cmpc">
      <div class="in">
        <label for="amt">Agentlik narxi</label>
        <div class="row"><input id="amt" type="text" inputmode="numeric" autocomplete="off" placeholder="masalan, 15 000 000"><div class="seg" role="group" aria-label="Valyuta"><button type="button" data-cur="uzs" aria-pressed="true">soʻm</button><button type="button" data-cur="usd" aria-pressed="false">$</button></div></div>
        <div class="quick"><span>Tez kiritish:</span><button type="button" data-amt="5000000">5 mln</button><button type="button" data-amt="15000000">15 mln</button><button type="button" data-amt="40000000">40 mln</button></div>
        <label for="cmpLab">Qaysi Lab bilan</label>
        <select id="cmpLab">{cmp_opts}</select>
      </div>
      <div class="out" aria-live="polite">
        <div class="big" id="cmpBig">–</div>
        <p id="cmpT">Agentlik aytgan narxni kiriting.</p>
        <p class="muted" id="cmpS"></p>
      </div>
    </div>
    <div class="honest">
      <div><b>Farqi nimada</b>Koʻp agentliklar hujjatni siz bilan birga tayyorlaydi yoki topshirishga yordam beradi. Kompas hujjatni oʻrningizga yozmaydi va topshirmaydi.</div>
      <div><b>Sizda nima qoladi</b>Kompasda oʻrgangan usul oʻzingizda qoladi: keyingi ariza, stipendiya yoki ish uchun ham ishlatasiz.</div>
      <div><b>Agentlik tanlasangiz</b>Shartnoma, litsenziya va “kafolat” vaʼdasini tekshiring. <a href="https://raqobat.gov.uz/uz/xorijda-ishlash-va-oqish-uchun-oson-borishni-vada-qilayotgan-konsalting-firmalardan-ogoh-boling/" target="_blank" rel="noopener">Raqobat qoʻmitasi ogohlantirishi</a></div>
      <div><b>Hisob qanday</b>Narx Lab 6 oylik obunasiga boʻlinadi. Dollar Markaziy bank kursida (2026-10-06): 1 $ = {fmt(round(USD))} soʻm.</div>
    </div>
  </div>
</section>

<section id="narx">
  <div class="wrap">
    <div class="head"><h2>Narxlar</h2><p class="sub">Obuna: yillik yoki oylik. M0 hamma Labda bepul. 6 oylik obuna bitta ariza siklini qamraydi.</p></div>
    <div class="pay-status"><span>⏳</span><span><b>Onlayn toʻlov hali ochilmagan.</b> Kutish roʻyxatidagilarga ochilish haqida birinchi boʻlib xabar beramiz. Hozir hech qanday toʻlov qabul qilinmaydi.</span></div>
    <div class="ptop"><div class="seg" role="group" aria-label="Davr"><button type="button" data-period="y" aria-pressed="true">Yillik</button><button type="button" data-period="m" aria-pressed="false">Oylik</button></div></div>
    <div class="tblwrap"><table class="cmp ptbl" id="ptbl" style="margin-top:0"><thead><tr><th>Lab</th><th>Narx</th><th>Holat</th></tr></thead><tbody>{price_rows()}</tbody></table></div>
    <div class="refund"><b>Toʻlov qaytarilmaydi.</b> Shuning uchun har Labning M0 qismi bepul: toʻlashdan oldin dastur sizga mosligini tekshirasiz.</div>
    <div class="rules">
      <div><b>Bekor qilish</b>Obunani istalgan vaqtda toʻxtatasiz: keyingi davr uchun pul yechilmaydi, toʻlangan davr oxirigacha kirish saqlanadi.</div>
      <div><b>18 yoshgacha</b>Obunani va toʻlovni ota-ona yoki vasiy rasmiylashtiradi. Ota-onaga jarayon haqida qisqa hisobot beriladi.</div>
      <div><b>Toʻlov xavfsizligi</b>Toʻlov Click va Payme orqali. Karta raqami Kompas serverlarida saqlanmaydi.</div>
      <div><b>Kirmaydi</b>Hujjatni oʻrningizga yozish, shaxsiy mentorlik, qabul yoki stipendiya kafolati.</div>
    </div>
  </div>
</section>

<section class="dark" id="qoidalar">
  <div class="wrap rule-box">
    <div>
      <h2>Ishlash qoidalari</h2>
      <p>Har Lab bitta yozma reja asosida quriladi. Metod va mantiq darsda turadi. Muddat, toʻlov, kvota va stipendiya summasi alohida sahifada rasmiy havola va tekshiruv sanasi bilan beriladi va har chorakda yangilanadi.</p>
      <p>Toʻqima statistika, tasdiqlanmagan sharh va natija vaʼdasi ishlatilmaydi. Talaba natijalari faqat uning yozma roziligi va tasdiqlovchi dalil bilan eʼlon qilinadi.</p>
      <div class="who2"><b>Dasturlarni kim tuzadi</b><ul><li>Asoschi geofizik, University of Leeds doktoranti</li><li>Janubiy Koreyada oʻqigan, Oʻzbekistonda universitetda dars bergan</li><li>Oʻzi oʻtmagan bosqichlar boʻyicha tajriba daʼvo qilinmaydi</li></ul></div>
    </div>
    <div class="model-list">
      <div class="model"><b>M0 bepul</b><span>Har Lab bepul qaror moduli bilan boshlanadi: sizga mos yoki mos emasligini toʻlovdan oldin bilasiz.</span></div>
      <div class="model"><b>Rasmiy manba</b><span>Muddat, toʻlov va talablar rasmiy havola va tekshiruv sanasi bilan.</span></div>
      <div class="model"><b>Siz yozasiz</b><span>Insho, xat va CV oʻrningizga yozilmaydi. Kompas tuzilma, mezon va tahlil beradi.</span></div>
      <div class="model bad"><b>Kafolat yoʻq</b><span>Qabul yoki stipendiya vaʼda qilinmaydi.</span></div>
    </div>
  </div>
</section>

<section class="alt" id="savollar">
  <div class="wrap">
    <div class="head" style="text-align:center"><h2>Koʻp soʻraladigan savollar</h2></div>
    <div class="faq">{faq_html}</div>
  </div>
</section>

<section class="dark cta">
  <div class="wrap">
    <h2>Bepul M0 dan boshlang.</h2>
    <p class="sub">Avval Lab sizga mosligini tekshiring, keyin qaror qiling.</p>
    <div class="cta-row" style="justify-content:center">
      <button type="button" class="btn btn-p" data-wl="">Kutish roʻyxatiga yozilish</button>
      <a href="https://t.me/kompaslab" class="btn btn-g" target="_blank" rel="noopener">Telegramda savol berish</a>
    </div>
  </div>
</section>
{FOOTER}

<div class="ovl" id="wl" role="dialog" aria-modal="true" aria-labelledby="wlT">
  <div class="mdl">
    <button type="button" class="x" id="wlX" aria-label="Yopish">×</button>
    {icon("bell", "i3d", "")}
    <h3 id="wlT" style="margin-top:6px">Kutish roʻyxati</h3>
    <p>Lab va email manzilingizni qoldiring: ochilishi bilan xabar beramiz. Email boshqa maqsadda ishlatilmaydi.</p>
    <select id="wlL" aria-label="Lab"><option value="">Labni tanlang</option>{opt_html}</select>
    <input type="email" id="wlE" placeholder="email@gmail.com" aria-label="Email" autocomplete="email" inputmode="email">
    <div id="wlMsg"></div>
    <button type="button" class="btn btn-p" id="wlB">Roʻyxatga yozilish</button>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="js/config.js"></script>
<script>
(function () {{
{WL_JS}
{PAGE_JS.replace("__LABS__", labs_js).replace("__USD__", str(USD))}
{LIVE_JS}
}})();
</script>
</body>
</html>
'''
    html = uz_fix(polish(h + body))
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("index.html", len(html))

if __name__ == "__main__":
    build()
