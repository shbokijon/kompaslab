# ═══════════════════════════════════════════════════════════════
#  Pullik modullarni Supabase paid_pages jadvaliga yuklash uchun SQL
#
#    python3 tools/modules/build.py master-lab-m1 ... master-lab-m8   # avval yigʻish
#    python3 tools/modules/paid_upload.py                             # SQL fayllar
#
#  Natija: tools/modules/paid/upload_<nom>.sql (har modul alohida, hajmi ~100 KB).
#  Ularni Supabase SQL Editor yoki MCP execute_sql (service role) bilan ishga tushiring.
#  Yuklangandan keyin: select course_slug, module_index, sha256, version from paid_pages;
#  sha256 shu skript chiqargan qiymat bilan mos boʻlishi kerak.
# ═══════════════════════════════════════════════════════════════
import hashlib, re, subprocess, sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAID = HERE / "paid"
TAG = "$kpaid$"


def version():
    try:
        h = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        h = "nogit"
    return date.today().isoformat() + "+" + h


def main(names):
    files = sorted(PAID.glob("*.html")) if not names else [PAID / (n + ".html") for n in names]
    ver = version()
    for f in files:
        m = re.fullmatch(r"([a-z-]+-lab)-m(\d+)", f.stem)
        if not m:
            continue
        course, idx = m.group(1), int(m.group(2))
        html = f.read_text(encoding="utf-8")
        assert TAG not in html, f.name + ": dollar-tag ichida uchradi"
        sha = hashlib.sha256(html.encode("utf-8")).hexdigest()
        sql = ("insert into public.paid_pages (course_slug, module_index, html, sha256, version) values ("
               f"'{course}', {idx}, {TAG}{html}{TAG}, '{sha}', '{ver}')\n"
               "on conflict (course_slug, module_index) do update set html = excluded.html, sha256 = excluded.sha256, "
               "version = excluded.version, updated_at = now();\n")
        out = PAID / ("upload_" + f.stem + ".sql")
        out.write_text(sql, encoding="utf-8")
        print(f"{f.stem}: {len(html)} belgi, sha256 {sha[:12]} -> {out.name}")


if __name__ == "__main__":
    main(sys.argv[1:])
