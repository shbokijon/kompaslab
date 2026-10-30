#!/usr/bin/env python3
"""Build Kompas Atlas's Canada snapshot: employers that received a positive
Labour Market Impact Assessment (LMIA) in the latest published quarter.

Source: Open Government Portal dataset 90fed587-1364-4f33-a9ee-208181dc0b97
(Open Government Licence - Canada). Historical data: a positive LMIA in a past
quarter is NOT a current vacancy or a work permit.

Needs openpyxl. Safe update: on any failure the existing snapshot is kept.
"""
from __future__ import annotations

import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

DATASET = "90fed587-1364-4f33-a9ee-208181dc0b97"
API = f"https://open.canada.ca/data/api/action/package_show?id={DATASET}"
PAGE = f"https://open.canada.ca/data/en/dataset/{DATASET}"
OUT = Path(__file__).resolve().parents[2] / "data" / "ca-lmia.json"
MIN_ROWS = 1_000
MAX_ROWS = 200_000
HOSTS = {"open.canada.ca", "www.open.canada.ca"}
QUARTER = re.compile(r"(20\d{2})_?q([1-4])_pos(?:itive)?_en\.xlsx$", re.I)

# Column header keywords (English file). Matched case-insensitively.
COLS = {
    "province": ("province",),
    "stream": ("program stream", "stream"),
    "employer": ("employer",),
    "address": ("address",),
    "occupation": ("occupation",),
    "positions": ("approved positions", "positions"),
}


def download(url: str, *, limit: int, any_https: bool = False) -> bytes:
    """API sahifasi faqat open.canada.ca dan. Fayl havolasi rasmiy API dan olinadi,
    portal uni fayl omboriga yoʻnaltirishi mumkin: bunda faqat HTTPS talab qilinadi."""
    if urlsplit(url).hostname not in HOSTS:
        raise RuntimeError("Resource must be listed on open.canada.ca")
    req = Request(url, headers={"User-Agent": "KompasLab-Atlas/1.0 (official open data importer; https://kompaslab.uz)"})
    with urlopen(req, timeout=90) as resp:
        final = urlsplit(resp.geturl())
        if final.hostname not in HOSTS and not (any_https and final.scheme == "https"):
            raise RuntimeError(f"Unexpected redirect host: {final.hostname}")
        if final.hostname not in HOSTS:
            print(f"Redirected to {final.hostname}", flush=True)
        body = resp.read(limit + 1)
    if len(body) > limit:
        raise RuntimeError("Download too large")
    return body


def latest_resource(package: dict) -> tuple[str, str]:
    best = None
    for res in package["result"]["resources"]:
        url = res.get("url") or ""
        m = QUARTER.search(url)
        if not m:
            continue
        key = (int(m.group(1)), int(m.group(2)))
        if best is None or key > best[0]:
            best = (key, url)
    if not best:
        raise RuntimeError("No English quarterly positive-LMIA XLSX found")
    (year, q), url = best
    return url, f"{year}-Q{q}"


def find_columns(header: list[str]) -> dict[str, int]:
    low = [(h or "").strip().lower() for h in header]
    idx = {}
    for key, words in COLS.items():
        for w in words:
            hit = next((i for i, h in enumerate(low) if w in h and i not in idx.values()), None)
            if hit is not None:
                idx[key] = hit
                break
    if "employer" not in idx or "province" not in idx:
        raise RuntimeError(f"Unexpected header: {header}")
    return idx


def parse_rows(rows: list[list]) -> list[list]:
    def is_header(r):
        cells = [c.lower() for c in r if isinstance(c, str)]
        return any("employer" in c for c in cells) and any("province" in c for c in cells)

    header_at = next((i for i, r in enumerate(rows[:40]) if is_header(r)), None)
    if header_at is None:
        raise RuntimeError("Header row with 'Employer' not found")
    idx = find_columns([str(c) if c is not None else "" for c in rows[header_at]])

    def cell(r, k):
        i = idx.get(k)
        if i is None or i >= len(r) or r[i] is None:
            return ""
        return " ".join(str(r[i]).split())[:220]

    out, seen = [], set()
    for r in rows[header_at + 1:]:
        emp = cell(r, "employer")
        prov = cell(r, "province")
        if not emp or not prov or emp.lower().startswith(("note", "source")):
            continue
        pos = cell(r, "positions")
        try:
            pos = int(float(pos)) if pos else None
        except ValueError:
            pos = None
        rec = [emp, prov, cell(r, "address"), cell(r, "occupation"), cell(r, "stream"), pos]
        key = tuple(str(x).casefold() for x in rec[:5])
        if key in seen:
            continue
        seen.add(key)
        out.append(rec)
    out.sort(key=lambda x: (x[0].casefold(), x[1]))
    return out


def run() -> None:
    import openpyxl  # noqa: PLC0415

    package = json.loads(download(API, limit=5_000_000))
    url, period = latest_resource(package)
    print(f"Latest resource: {period} {url}", flush=True)
    wb = openpyxl.load_workbook(io.BytesIO(download(url, limit=40_000_000, any_https=True)), read_only=True, data_only=True)
    ws = wb.worksheets[0]
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    recs = parse_rows(rows)
    if not (MIN_ROWS <= len(recs) <= MAX_ROWS):
        raise RuntimeError(f"Unexpected row count: {len(recs)}")
    provinces = sorted({r[1] for r in recs})
    data = {
        "schema": 1, "source": PAGE, "file_url": url, "period": period,
        "retrieved_at": datetime.now(timezone.utc).date().isoformat(),
        "licence": "Open Government Licence - Canada",
        "count": len(recs), "provinces": provinces,
        "fields": ["employer", "province", "address", "occupation", "stream", "positions"],
        "rows": recs,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    tmp.replace(OUT)
    print(f"Saved {len(recs):,} positive LMIA rows for {period}")


if __name__ == "__main__":
    try:
        run()
    except Exception as exc:
        print(f"ERROR: Existing snapshot preserved; {exc}", file=sys.stderr)
        raise SystemExit(1)
