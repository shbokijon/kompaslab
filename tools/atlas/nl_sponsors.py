#!/usr/bin/env python3
"""Build Kompas Atlas's Netherlands snapshot from the IND public register
of recognised sponsors (work: highly skilled migrants and similar routes).

Stdlib only. Safe update: on fetch/parse/validation failure the existing
published snapshot is kept and the script exits nonzero.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

PAGE = "https://ind.nl/en/public-register-recognised-sponsors/public-register-work"
OUT = Path(__file__).resolve().parents[2] / "data" / "nl-sponsors.json"
MIN_ROWS = 1_000
MAX_ROWS = 60_000
KVK = re.compile(r"^\d{8}$")
MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], 1)}


class Rows(HTMLParser):
    """Collect table rows as lists of cell texts."""

    def __init__(self):
        super().__init__()
        self.rows: list[list[str]] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None
        self.text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self._row = []
        elif tag in ("td", "th") and self._row is not None:
            self._cell = []

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self._row is not None and self._cell is not None:
            self._row.append(" ".join("".join(self._cell).split()))
            self._cell = None
        elif tag == "tr" and self._row is not None:
            if self._row:
                self.rows.append(self._row)
            self._row = None

    def handle_data(self, data):
        if self._cell is not None:
            self._cell.append(data)
        self.text.append(data)


def download(url: str, *, limit: int) -> bytes:
    req = Request(url, headers={
        "User-Agent": "KompasLab-Atlas/1.0 (official public data importer; https://kompaslab.uz)",
        "Accept": "text/html,*/*"})
    with urlopen(req, timeout=60) as resp:
        if urlsplit(resp.geturl()).hostname not in {"ind.nl", "www.ind.nl"}:
            raise RuntimeError("Unexpected redirect host")
        body = resp.read(limit + 1)
    if len(body) > limit:
        raise RuntimeError("Download too large")
    return body


def parse(html: str) -> tuple[list[list[str]], str | None]:
    p = Rows()
    p.feed(html)
    out, seen = [], set()
    for row in p.rows:
        kvk = next((c for c in row if KVK.match(c.replace(" ", ""))), None)
        name = next((c for c in row if c and not KVK.match(c.replace(" ", ""))), "")
        if not kvk or not name:
            continue
        kvk = kvk.replace(" ", "")
        key = (name.casefold(), kvk)
        if key in seen:
            continue
        seen.add(key)
        out.append([name[:220], kvk])
    out.sort(key=lambda r: r[0].casefold())
    text = " ".join(" ".join(p.text).split())
    m = re.search(r"last updated on (\d{1,2}) (\w+) (20\d{2})", text, re.I)
    updated = None
    if m and m.group(2).lower() in MONTHS:
        updated = f"{m.group(3)}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    return out, updated


def run() -> None:
    rows, updated = parse(download(PAGE, limit=12_000_000).decode("utf-8", "replace"))
    if not (MIN_ROWS <= len(rows) <= MAX_ROWS):
        raise RuntimeError(f"Unexpected row count: {len(rows)}")
    data = {
        "schema": 1, "source": PAGE, "last_updated": updated,
        "retrieved_at": datetime.now(timezone.utc).date().isoformat(),
        "count": len(rows), "fields": ["name", "kvk"], "rows": rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    tmp.replace(OUT)
    print(f"Saved {len(rows):,} IND recognised sponsors; register date {updated or 'unknown'}")


if __name__ == "__main__":
    try:
        run()
    except Exception as exc:
        print(f"ERROR: Existing snapshot preserved; {exc}", file=sys.stderr)
        raise SystemExit(1)
