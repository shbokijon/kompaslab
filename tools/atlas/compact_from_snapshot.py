#!/usr/bin/env python3
"""Make offline mobile snapshot from existing validated official snapshot.

CI must not silently fetch third party data just to execute browser QA.
"""
import json
from pathlib import Path
from uk_sponsors import OUT, LITE, PAGE, MIN_SPONSORS, MAX_SPONSORS, compact_records

full = json.loads(OUT.read_text(encoding="utf-8"))
records = full.get("records", [])
assert full.get("source") == PAGE
assert MIN_SPONSORS <= len(records) <= MAX_SPONSORS
result = compact_records(records, source=PAGE, published=full.get("last_updated"),
                         retrieved=full.get("retrieved_at", ""))
LITE.write_text(json.dumps(result, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
bytes_full = OUT.stat().st_size
bytes_lite = LITE.stat().st_size
print(f"Mobile test snapshot: {bytes_lite:,} bytes vs full {bytes_full:,} ({100*(1-bytes_lite/bytes_full):.1f}% reduced)")
assert bytes_lite < bytes_full * 0.80, "Insufficient data compression"
