# PhD Lab sotuvda (2026-11-11): sahifalardagi "Kutish roʻyxati" matnlarini sotuv holatiga keltiradi.
# split.py dan keyin ishlaydi (build.py chaqiradi); qayta ishga tushirish xavfsiz.
#   python3 tools/landing/phd_sale.py
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

HEADER_OLD = '<button type="button" class="btn btn-p btn-sm" data-wl>Kutish roʻyxati</button>'
HEADER_NEW = '<a class="btn btn-p btn-sm" href="register.html" data-snd="nav">Roʻyxatdan oʻtish</a>'
CTA_OLD = '<button type="button" class="btn btn-g" data-wl>🔔 Kutish roʻyxati</button>'
CTA_NEW = '<a class="btn btn-g" href="phd-lab-narxlar.html" data-snd="nav">Narxlar va obuna</a>'
CTA2_OLD = '<button type="button" class="btn btn-g" data-wl>Kutish roʻyxati</button>'
PAY_OLD = re.compile(r'(<span data-paystatus="phd-lab">).*?(</span></div>)', re.S)
PAY_NEW = r'\1<b>Toʻlov Click orqali.</b> Toʻlov sahifasida tarif, aniq summa va ochiladigan modullar koʻrsatiladi; kirish toʻlov tasdiqlangan zahoti ochiladi.\2'
LABEL = {"monthly": "Oylik obunani toʻlash", "6m": "6 oylik obunani toʻlash"}


def buy(m):
    cls, plan = m.group(1), m.group(2)
    return f'<a class="{cls.replace("btn-g", "btn-p")}" href="tolov.html?lab=phd-lab&amp;plan={plan}" data-buy="phd-lab|{plan}" data-snd="nav">{LABEL[plan]}</a>'


def run():
    changed = []
    for f in sorted(ROOT.glob("phd-lab*.html")):
        if f.name.startswith("phd-lab-m0"):
            continue
        s0 = s = f.read_text(encoding="utf-8")
        s = s.replace(HEADER_OLD, HEADER_NEW).replace(CTA_OLD, CTA_NEW).replace(CTA2_OLD, CTA_NEW)
        s = PAY_OLD.sub(PAY_NEW, s).replace("<span>⏳</span><span data-paystatus", "<span>💳</span><span data-paystatus")
        s = re.sub(r'<button type="button" class="(btn [^"]*)" data-wl data-buy="phd-lab\|(monthly|6m)">[^<]*</button>', buy, s)
        if s != s0:
            f.write_text(s, encoding="utf-8")
            changed.append(f.name)
    return changed


if __name__ == "__main__":
    print(run())
