# ═══════════════════════════════════════════════════════════════
#  KOMPAS LAB — matn tuzatishlarini manba fayllarga yozish (2026-10-31)
#
#  Admin panel → Darslar → "Matn tuzatishlari" (jadval text_fixes) saytda darhol
#  ishlaydi (js/kompas-ui.js; pullik modulda fn_paid_page()). Bu skript ularni
#  manba fayllarga yozadi, shunda keyingi yigʻishda tuzatish yoʻqolmaydi.
#
#  1) Faol tuzatishlarni JSON ga oling (MCP execute_sql yoki SQL Editor):
#       select json_agg(t order by id) from (select id, page, old_text, new_text
#         from text_fixes where status = 'active') t;
#     natijani fixes.json ga saqlang.
#  2) python3 tools/site/apply_fixes.py fixes.json            # nima oʻzgarishini koʻrsatadi
#     python3 tools/site/apply_fixes.py fixes.json --write    # manbaga yozadi va qayta yigʻadi
#  3) Skript oxirida chiqqan buyruqlar: pullik modul SQL ini bazaga yuklash va
#     "update text_fixes set status='baked'…" (faqat manbaga yozilganlar uchun).
#  4) Odatdagi tekshiruv (site_crawl.js) → commit → deploy.
#
#  Topilmagan tuzatish faol qoladi (saytda ishlayveradi) va roʻyxatda koʻrsatiladi.
# ═══════════════════════════════════════════════════════════════
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "tools" / "modules" / "src"
LANDING = [ROOT / "tools" / "landing" / n for n in ("labs_data.py", "mods.json", "render.py", "phd_source.html", "phd_polish.py", "postprocess.py")]
ATLAS = sorted((ROOT / "tools" / "atlas").glob("*.py"))
PLANNER = [ROOT / "tools" / "site" / "planner.py"]
# Qoʻlda yuritiladigan sahifalar (generator yoʻq)
HAND = ["index.html", "narxlar.html", "savollar.html", "qanday-ishlaydi.html", "maxfiylik.html", "qollab-quvvatlash.html",
        "dashboard.html", "profil.html", "login.html", "register.html", "reset-password.html", "uk-sponsors.html", "lesson.html"]
LAB_PREFIX = ("bachelor-lab", "master-lab", "phd-lab", "gks-lab", "usa-lab", "daad-lab", "musofir-lab", "tadbirkor-talaba")


def module_src(name):
    """'master-lab-m0' -> manba fayl va build.py nomi"""
    for p in (SRC / f"{name}.src.html", SRC / f"{name}.page.html"):
        if p.exists():
            return p, name
    return None, None


def targets(page):
    """text_fixes.page -> (manba fayllar, qayta yigʻish kaliti)"""
    m = re.fullmatch(r"paid:([a-z-]+):(\d+)", page)
    if m:
        name = f"{m.group(1)}-m{m.group(2)}"
        p, n = module_src(name)
        return ([p] if p else []), ("paid", n)
    m = re.fullmatch(r"(.+-m0)\*|(.+-m0)(?:-\d+|-yakun)?\.html", page)
    if m:
        name = m.group(1) or m.group(2)
        p, n = module_src(name)
        return ([p] if p else []), ("module", n)
    if page == "*":
        files = [p for p in SRC.glob("*-m0.*.html")] + LANDING + ATLAS + PLANNER + [ROOT / h for h in HAND]
        return files, ("all", None)
    if page.startswith(("atlas", "nl-sponsors", "ca-lmia")):
        return ATLAS, ("atlas", None)
    if page.startswith("master-planner"):
        return PLANNER, ("planner", None)
    if page.startswith(LAB_PREFIX):
        return LANDING, ("landing", None)
    return [ROOT / page], ("hand", None)


def variants(s):
    """Manbada ASCII apostrof (labs_data.py) yoki HTML belgi kodi boʻlishi mumkin"""
    v = [s]
    a = s.replace("ʻ", "'").replace("ʼ", "'")
    if a != s:
        v.append(a)
    h = s.replace("&", "&amp;").replace("ʼ", "&#700;")
    if h != s:
        v.append(h)
    return v


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv
    if not args:
        sys.exit(__doc__ or "foydalanish: apply_fixes.py fixes.json [--write]")
    fixes = json.loads(Path(args[0]).read_text(encoding="utf-8")) or []
    done, missing, builds = [], [], set()
    cache = {}
    for f in fixes:
        files, build = targets(f["page"])
        hits = []
        for p in files:
            if not p or not p.exists():
                continue
            s = cache.get(p) or p.read_text(encoding="utf-8")
            for i, old in enumerate(variants(f["old_text"])):
                n = s.count(old)
                if n:
                    new = f["new_text"]
                    if i == 1:   # ASCII apostrofli manba: yangi matn ham shu uslubda
                        new = new.replace("ʻ", "'").replace("ʼ", "'")
                    if i == 2:
                        new = new.replace("&", "&amp;").replace("ʼ", "&#700;")
                    s = s.replace(old, new)
                    hits.append((p, n))
                    break
            cache[p] = s
        if hits:
            done.append(f["id"])
            builds.add(build)
            print(f"✓ #{f['id']} {f['page']}: " + ", ".join(f"{p.relative_to(ROOT)} ×{n}" for p, n in hits))
        else:
            missing.append(f)
            print(f"✗ #{f['id']} {f['page']}: manbada topilmadi → «{f['old_text'][:60]}»")
    if not write:
        print(f"\nQuruq ishga tushirish: {len(done)} ta yoziladi, {len(missing)} ta topilmadi. Yozish: --write")
        return
    for p, s in cache.items():
        if p.exists() and p.read_text(encoding="utf-8") != s:
            p.write_text(s, encoding="utf-8")
    kinds = {k for k, _ in builds}
    mods = sorted({n for k, n in builds if k in ("module", "paid") and n})
    run = []
    if kinds & {"landing", "all"}:
        run.append([sys.executable, "tools/landing/build.py"])
    if "all" in kinds:
        run.append([sys.executable, "tools/modules/build.py"] + [p.name.split(".")[0] for p in SRC.glob("*-m0.*.html")])
        run.append([sys.executable, "tools/atlas/build_site.py"])
        run.append([sys.executable, "tools/site/planner.py"])
    if mods:
        run.append([sys.executable, "tools/modules/build.py"] + mods)
    if "atlas" in kinds:
        run.append([sys.executable, "tools/atlas/build_site.py"])
    if "planner" in kinds:
        run.append([sys.executable, "tools/site/planner.py"])
    for cmd in run:
        print("$", " ".join(cmd[1:]))
        subprocess.run(cmd, cwd=ROOT, check=True)
    paid = [n for k, n in builds if k == "paid" and n]
    if paid:
        subprocess.run([sys.executable, "tools/modules/paid_upload.py"] + paid, cwd=ROOT, check=True)
        print("\nPullik modul SQL: " + ", ".join(f"tools/modules/paid/upload_{n}.sql" for n in paid) + " → bazaga yuklang (MCP execute_sql).")
    if done:
        print(f"\nBazada belgilash:\nupdate text_fixes set status = 'baked', baked_at = now() where id in ({', '.join(map(str, done))});")
    if missing:
        print(f"\nTopilmadi ({len(missing)} ta): faol qoladi, qoʻlda koʻrib chiqing.")


if __name__ == "__main__":
    main()
