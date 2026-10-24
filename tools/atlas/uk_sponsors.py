#!/usr/bin/env python3
"""Build Kompas Atlas's UK Skilled Worker sponsor snapshot from GOV.UK.

Uses Python stdlib only. Safe update: on fetch/parse/validation failure, exits
nonzero without replacing the existing published snapshot.
"""
from __future__ import annotations

import csv
import io
import json
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import Request, urlopen

PAGE = "https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers"
OUT = Path(__file__).resolve().parents[2] / "data" / "uk-sponsors.json"
LITE = OUT.with_name("uk-sponsors-lite.json")
MAX_CSV_BYTES = 22_000_000
MIN_SPONSORS = 10_000
MAX_SPONSORS = 150_000
REQUIRED = ("Organisation Name", "Town/City", "County", "Type & Rating", "Route")


class CsvLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        href = dict(attrs).get("href", "")
        parsed = urlsplit(href)
        if parsed.path.lower().endswith(".csv") and ("assets.publishing.service.gov.uk" in parsed.netloc or "/media/" in parsed.path):
            self.links.append(href)


def download(url: str, *, limit: int) -> bytes:
    request = Request(url, headers={"User-Agent": "KompasLab-Atlas/1.0 (official public data importer; https://kompaslab.uz)", "Accept": "text/csv,text/html,*/*"})
    with urlopen(request, timeout=50) as response:
        final_url = response.geturl()
        if urlsplit(final_url).hostname not in {"www.gov.uk", "assets.publishing.service.gov.uk"}:
            raise RuntimeError("Unexpected redirect host")
        content = response.read(limit + 1)
    if len(content) > limit:
        raise RuntimeError("Download too large")
    return content


def parse_csv(csv_bytes: bytes) -> list[dict]:
    # GOV.UK's CSV is UTF-8, sometimes with a byte order mark.
    reader = csv.DictReader(io.StringIO(csv_bytes.decode("utf-8-sig"), newline=""))
    columns = set(reader.fieldnames or [])
    if not set(REQUIRED).issubset(columns):
        raise RuntimeError(f"Unexpected header: {reader.fieldnames}")
    result = []
    seen = set()
    for row in reader:
        if (row.get("Route") or "").strip() != "Skilled Worker":
            continue
        record = {
            "name": (row["Organisation Name"] or "").strip()[:220],
            "town": (row["Town/City"] or "").strip()[:220],
            "county": (row["County"] or "").strip()[:220],
            "rating": (row["Type & Rating"] or "").strip()[:220],
        }
        if not record["name"]:
            continue
        key = (record["name"].casefold(), record["town"].casefold(), record["rating"].casefold())
        if key in seen:
            continue
        seen.add(key)
        result.append(record)
    if not (MIN_SPONSORS <= len(result) <= MAX_SPONSORS):
        raise RuntimeError(f"Unexpected Skilled Worker record count: {len(result)}")
    result.sort(key=lambda x: (x["name"].casefold(), x["town"].casefold()))
    return result



def compact_records(records: list[dict], *, source: str, published: str | None, retrieved: str) -> dict:
    """Dictionary-encode repeated town/county/rating strings for mobile downloads.

    Names are preserved verbatim; no approximate entity matching or sponsorship
    eligibility inference is performed.
    """
    towns, counties, ratings = [], [], []
    ti, ci, ri = {}, {}, {}
    rows = []
    for item in records:
        for value, values, ids in (
            (item["town"], towns, ti), (item["county"], counties, ci),
            (item["rating"], ratings, ri)
        ):
            if value not in ids:
                ids[value] = len(values)
                values.append(value)
        rows.append([item["name"], ti[item["town"]], ci[item["county"]], ri[item["rating"]]])
    return {
        "schema": 1, "source": source, "last_updated": published,
        "retrieved_at": retrieved, "route": "Skilled Worker",
        "count": len(records), "towns": towns, "counties": counties,
        "ratings": ratings, "rows": rows,
    }


def run() -> None:
    html = download(PAGE, limit=1_800_000).decode("utf-8")
    links = CsvLinks()
    links.feed(html)
    if not links.links:
        raise RuntimeError("GOV.UK page contains no official asset CSV link")
    csv_url = urljoin(PAGE, links.links[0])
    if urlsplit(csv_url).hostname != "assets.publishing.service.gov.uk":
        raise RuntimeError("CSV must be hosted on assets.publishing.service.gov.uk")
    records = parse_csv(download(csv_url, limit=MAX_CSV_BYTES))
    # Prefer the actual CSV edition date in the official file name.
    match = re.search(r"20\d{2}-\d{2}-\d{2}", unquote(csv_url))
    published = match.group(0) if match else None
    result = {
        "source": PAGE,
        "csv_url": csv_url,
        "last_updated": published,
        "retrieved_at": datetime.now(timezone.utc).date().isoformat(),
        "route": "Skilled Worker",
        "records": records,
    }
    compact = compact_records(records, source=PAGE, published=published,
                              retrieved=result["retrieved_at"])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp_full = OUT.with_suffix(".json.tmp")
    tmp_lite = LITE.with_suffix(".json.tmp")
    tmp_full.write_text(json.dumps(result, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    tmp_lite.write_text(json.dumps(compact, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    # Both files are completely written before either is published.
    tmp_full.replace(OUT)
    tmp_lite.replace(LITE)
    reduction = round(100 * (1 - LITE.stat().st_size / OUT.stat().st_size))
    print(f"Saved {len(records):,} Skilled Worker register records; edition {published or 'unknown'}; compact {LITE.stat().st_size:,} bytes ({reduction}% smaller)")


if __name__ == "__main__":
    try:
        run()
    except Exception as exc:
        print(f"ERROR: Existing snapshot preserved; {exc}", file=sys.stderr)
        raise SystemExit(1)
