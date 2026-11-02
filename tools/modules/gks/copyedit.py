"""GKS Lab matn tahriri: formatlar va kodni oʻzgartirmasdan koʻrinadigan matnni tozalash.
Yangi alifboga oʻtkazish js/alifbo.js vazifasi; manba eski lotin yozuvida qoladi.
"""
import json
import re
from pathlib import Path

FIXES = json.loads(Path(__file__).with_name("copyedit.json").read_text(encoding="utf-8"))
PARTS = re.compile(r'(<script\b[^>]*>[\s\S]*?</script>|<style\b[^>]*>[\s\S]*?</style>|<span\b[^>]*lang=["\x27]en["\x27][^>]*>[\s\S]*?</span>|<!--[\s\S]*?-->|<[^>]+>)', re.I)
ATTR = re.compile(r'\b(placeholder|aria-label|title|content|alt|data-tip)="([^"]*)"')

def polish_text(s):
    for old, new in FIXES:
        s = s.replace(old, new)
    return s

def polish_gks_html(s):
    out = []
    for part in PARTS.split(s):
        if not part.startswith("<"):
            out.append(polish_text(part))
        elif re.match(r'<(?:script|style|!--|span\b[^>]*lang=["\x27]en)', part, re.I):
            out.append(part)
        else:
            out.append(ATTR.sub(lambda m: m.group(1) + '="' + polish_text(m.group(2)) + '"', part))
    return "".join(out)
