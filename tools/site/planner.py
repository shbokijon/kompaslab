#!/usr/bin/env python3
"""Bepul reja (master-planner.html) ni yigʻadi: bitta sahifa, ?lab= bilan 6 ta Lab.

Nazorat roʻyxati Lab modullaridan olinadi (qoʻlda yozilmaydi):
  Bachelor, Master, GKS, USA — tools/landing/mods.json
  DAAD — tools/landing/labs_data.py (DAAD_MODS)
  PhD  — phd-lab-mN.html sarlavhalari
Ishga tushirish: python3 tools/site/planner.py  (Lab modullari oʻzgarsa ham qayta yigʻing)
Mantiq: js/master-planner.js. Master kaliti eski (kompas-master-planner-v1), kabinet uni oʻqiydi.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1].parent
sys.path.insert(0, str(ROOT / "tools" / "site"))
sys.path.insert(0, str(ROOT / "tools" / "landing"))
from shell import head, nav, page, pagehead  # noqa: E402
from labs_data import ON_SALE  # noqa: E402


def fix(s: str) -> str:
    """Manbadagi ASCII apostrofni toʻgʻri belgiga oʻgiradi (labs_data.py eski yozuvi)."""
    s = re.sub(r"([oOgG])['‘’ʼ]", lambda m: m.group(1) + "ʻ", s)
    return s.replace("'", "ʼ")


def tasks(slug: str, mods: list[tuple[str, str]]) -> list[dict]:
    out = []
    for mid, title in mods:
        out.append({"id": mid, "t": fix(title), "h": f"{slug}-{mid.lower()}.html"})
    return out


def build_labs() -> dict:
    mj = json.loads((ROOT / "tools/landing/mods.json").read_text(encoding="utf-8"))
    pick = lambda k: [(m["id"], m["title"]) for m in mj[k]]  # noqa: E731
    import labs_data  # noqa: PLC0415
    daad = [(m["id"], m["title"]) for m in labs_data.DAAD_MODS]
    phd = []
    for i in range(9):
        t = re.search(r"<title>([^<]*)", (ROOT / f"phd-lab-m{i}.html").read_text(encoding="utf-8")).group(1)
        t = re.sub(r"^M\d+\.?\s*", "", t.split(" · ")[0]).strip()
        phd.append((f"M{i}", t))
    gks_all = pick("GKS")
    return {
        "master": {"name": "Master Lab", "slug": "master-lab", "key": "kompas-master-planner-v1",
                   "goal": "Nima uchun magistratura?", "prog": "Dastur",
                   "opts": [["taught", "O'quv magistraturasi (Taught MSc/MA)"], ["research", "Tadqiqot magistraturasi (Research MSc/MRes)"], ["other", "Boshqa yoki noma'lum"]],
                   "tasks": tasks("master-lab", pick("Master"))},
        "bachelor": {"name": "Bachelor Lab", "slug": "bachelor-lab", "key": "kompas-planner-bachelor-v1",
                     "goal": "Nima uchun xorijda bakalavriat va qaysi yo'nalish?", "prog": "Yo'nalish (major)",
                     "opts": [], "tasks": tasks("bachelor-lab", pick("Bachelor"))},
        "phd": {"name": "PhD Lab", "slug": "phd-lab", "key": "kompas-planner-phd-v1",
                "goal": "Qaysi ilmiy savol ustida ishlamoqchisiz?", "prog": "Dastur yoki laboratoriya",
                "opts": [], "tasks": tasks("phd-lab", phd)},
        "gks": {"name": "GKS Lab", "slug": "gks-lab", "key": "kompas-planner-gks-v1",
                "goal": "Nima uchun Koreya va GKS?", "prog": "Dastur",
                "opts": [["U", "Bakalavriat"], ["M", "Magistratura"], ["D", "Doktorantura"]],
                "tasks": tasks("gks-lab", gks_all)},
        "usa": {"name": "USA Lab", "slug": "usa-lab", "key": "kompas-planner-usa-v1",
                "goal": "AQShda qaysi yo'l: bakalavr, UGRAD, Fulbright, magistratura yoki PhD? Oila yiliga qancha bera oladi?", "prog": "Dastur",
                "opts": [], "tasks": tasks("usa-lab", pick("USA"))},
        "daad": {"name": "DAAD Lab", "slug": "daad-lab", "key": "kompas-planner-daad-v1",
                 "goal": "Nima uchun Germaniya va qaysi DAAD dasturi?", "prog": "Dastur",
                 "opts": [["master", "Magistratura"], ["phd", "Doktorantura"]],
                 "tasks": tasks("daad-lab", daad)},
    }


def main() -> None:
    labs = build_labs()
    for k, v in labs.items():
        for t in v["tasks"]:
            if not (ROOT / t["h"]).exists():
                raise SystemExit(f"{k}: modul sahifasi yo'q: {t['h']}")
        v["opts"] = [[a, fix(b)] for a, b in v["opts"]]
        v["goal"], v["prog"] = fix(v["goal"]), fix(v["prog"])
        v["sale"] = v["slug"] in ON_SALE  # sotuvdagi Lab: narx sahifasiga havola
    cfg = json.dumps(labs, ensure_ascii=False, separators=(",", ":"))
    chips = "".join(f'<a href="master-planner.html?lab={k}" data-lab="{k}">{v["name"]}</a>' for k, v in labs.items())
    body = nav("reja", "reja") + pagehead(
        [("Kompas Lab", "index.html"), ("Bepul reja", None)],
        "Bepul reja",
        "Labingizni tanlang: maqsad, saralangan ro'yxat (Shortlist) va tayyorgarlik bosqichlari bir joyda. Ma'lumot faqat shu qurilmada saqlanadi, ro'yxatdan o'tish shart emas.",
        "calendar") + f"""<main><div class="wrap">
<nav class="pl-labs" aria-label="Lab tanlash">{chips}</nav>
<div class="pl-grid">
<section class="pl-card"><h2>1. Maqsad</h2>
<label class="pl-label" for="goal" id="goalQ">Maqsadingiz</label><textarea id="goal" class="pl-ctl" rows="3" maxlength="800"></textarea>
<div class="pl-row"><div id="degreeBox"><label class="pl-label" for="degree">Daraja yoki trek</label><select id="degree" class="pl-ctl"></select></div>
<div><label class="pl-label" for="intake">Qabul yili</label><input id="intake" class="pl-ctl" type="number" min="2026" max="2040" value="2027"></div></div>
<label class="pl-label" for="countries">Mamlakatlar</label><input id="countries" class="pl-ctl" maxlength="140" placeholder="Germaniya, Koreya, Yaponiya…" data-suggest="country">
<div class="pl-btns"><button id="saveProfile" class="btn btn-p btn-sm" type="button">Saqlash</button></div><p id="profileStatus" class="pl-note" role="status"></p>
</section>
<section class="pl-card"><h2>2. Tayyorgarlik bosqichlari</h2>
<p class="pl-note">Lab modullari bo'yicha. Belgi faqat siz bajargan ishni bildiradi, universitet yoki stipendiya tasdig'ini emas.</p>
<div class="pl-bar"><div id="bar"></div></div><p id="progressText" class="pl-note" aria-live="polite"></p>
<ul id="taskList" class="pl-tasks"></ul>
<p id="plSale" class="pl-note" hidden></p>
<div id="next" class="pl-next" hidden></div>
</section>
<section class="pl-card full"><h2>3. Saralangan ro'yxat (Shortlist)</h2>
<p class="pl-note">Rasmiy dastur sahifasini o'zingiz qo'shing. Kompas havolalarni tekshirmaydi; har ma'lumotni rasmiy saytda tekshiring.</p>
<form id="addProgramme"><div class="pl-row">
<div><label for="university" class="pl-label">Universitet</label><input id="university" class="pl-ctl" maxlength="120" required data-suggest="uni"></div>
<div><label for="programme" class="pl-label" id="progLabel">Dastur</label><input id="programme" class="pl-ctl" maxlength="150" required data-suggest="prog"></div>
<div><label for="officialUrl" class="pl-label">Rasmiy havola</label><input id="officialUrl" class="pl-ctl" type="url" required placeholder="https://"></div></div>
<div class="pl-row"><div><label for="deadline" class="pl-label">Oxirgi muddat (ixtiyoriy)</label><input id="deadline" class="pl-ctl" type="date"></div>
<div><label for="funding" class="pl-label">Moliyalashtirish</label><select id="funding" class="pl-ctl"><option value="unknown">Hali noma'lum</option><option value="possible">Tekshirish kerak</option><option value="self-funded">O'z hisobimdan</option></select></div></div>
<div class="pl-btns"><button class="btn btn-p btn-sm" type="submit">Ro'yxatga qo'shish</button></div><p id="addStatus" role="status" class="pl-note"></p></form>
<div id="programmesList" aria-live="polite"></div>
</section>
<section class="pl-card"><h2>4. Rasmiy manbalar</h2>
<p class="pl-note">Avval aynan siz tanlagan dastur sahifasi, stipendiya tashkiloti va immigratsiya idorasini tekshiring.</p>
<div class="pl-btns"><a class="btn btn-g btn-sm" href="sources.html">Manbalar katalogi</a><a class="btn btn-g btn-sm" href="atlas.html">Kompas Atlas</a></div>
<p class="pl-note">Rasmiy saytdagi ma'lumot ham o'zgaradi. Har muddat, talab va to'lovni topshirishdan oldin qayta tekshiring.</p>
</section>
<section class="pl-card"><h2>5. Zaxira nusxa</h2>
<p class="pl-note">Rejani faylga saqlang va boshqa qurilmada qayta yuklang. Kompas serveriga hech narsa yuborilmaydi.</p>
<div class="pl-btns"><button id="export" type="button" class="btn btn-p btn-sm">Faylga saqlash</button><label class="btn btn-g btn-sm" for="importFile">Fayldan yuklash</label><input id="importFile" class="pl-file" type="file" accept="application/json,.json"><button id="clear" type="button" class="btn btn-g btn-sm">Tozalash</button></div>
<p id="dataStatus" class="pl-note" role="status"></p>
<p class="pl-note">Pasport, bank kartasi, manzil yoki sog'liq haqidagi ma'lumotni kiritmang.</p>
</section>
</div></div></main>
"""
    h = head(title="Bepul reja: xorijda o'qishga tayyorgarlik rejasi · Kompas Lab",
             desc="Bepul tayyorgarlik rejasi: Bachelor, Master, PhD, GKS, USA va DAAD uchun maqsad, saralangan ro'yxat va bosqichlar. Ro'yxatdan o'tmasdan, ma'lumot qurilmangizda.",
             path="master-planner")
    scripts = (f'<script type="application/json" id="pl-cfg">{cfg}</script>\n'
               '<script src="js/master-planner.js" defer></script><script src="js/suggest.js" defer></script>\n')
    html = page(head_html=h, body=body, scripts=scripts)
    if "'" in html:
        raise SystemExit("ASCII apostrof qoldi")
    (ROOT / "master-planner.html").write_text(html, encoding="utf-8")
    print("yozildi: master-planner.html,", ", ".join(f"{k}: {len(v['tasks'])}" for k, v in labs.items()))


if __name__ == "__main__":
    main()
