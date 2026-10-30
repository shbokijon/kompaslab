"""Umumiy sayt qobigʻi (head, menyu, footer) generator bilan yigʻiladigan
sahifalar uchun: Atlas sahifalari va Bepul reja.

Matn manbada ASCII apostrof bilan yoziladi; `uz()` uni oʻ/gʻ (U+02BB) va
tutuq (U+02BC) ga oʻgiradi. Shu sabab HTML atributlari va CSS faqat qoʻsh
qoʻshtirnoqda yoziladi; JS alohida .js faylda turadi.
"""
from __future__ import annotations

import re

SITE = "https://www.kompaslab.uz"
TABS = [
    ("index.html#labs", "Lablar", "labs"),
    ("master-planner.html", "Bepul reja", "reja"),
    ("qanday-ishlaydi.html", "Qanday ishlaydi", "qanday"),
    ("narxlar.html", "Narxlar", "narx"),
    ("atlas.html", "Atlas", "atlas"),
    ("savollar.html", "Savollar", "savol"),
]


def uz(text: str) -> str:
    """o'/g' -> oʻ/gʻ (U+02BB), qolgan ' -> ʼ (U+02BC)."""
    text = re.sub(r"([oOgG])'", lambda m: m.group(1) + "ʻ", text)
    return text.replace("'", "ʼ")


def tabs(active: str) -> str:
    out = []
    for href, label, key in TABS:
        cur = ' aria-current="page"' if key == active else ""
        out.append(f'<a href="{href}"{cur}>{label}</a>')
    return '<div class="kl-tabs" role="navigation" aria-label="Sayt bo\'limlari">' + "".join(out) + "</div>"


def head(*, title: str, desc: str, path: str, css: str = "", extra: str = "", jsonld: str = "") -> str:
    canon = f"{SITE}/{path}" if path else f"{SITE}/"
    ld = f'<script type="application/ld+json">{jsonld}</script>\n' if jsonld else ""
    return f"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#2d4a3e">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/img/brand/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Caladea:ital,wght@0,400;0,700;1,400;1,700&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&family=Playfair+Display:wght@400;700&text=%CA%BB%CA%BC%C3%96%C3%B6%C4%9E%C4%9F%C5%9E%C5%9F%C3%87%C3%A7&display=swap" rel="stylesheet"><script src="js/alifbo.js"></script>
<link rel="stylesheet" href="css/home.css">
<link rel="stylesheet" href="css/brand.css">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" href="img/brand/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="img/brand/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="stylesheet" href="css/kompas-ui.css">
<link rel="stylesheet" href="css/atlas.css">
<script src="js/kompas-ui.js"></script>
<script src="js/pwa.js" defer></script>
<script src="js/sfx.js" defer></script>
{ld}{extra}{('<style>' + css + '</style>') if css else ''}
</head>
"""


def nav(active: str, page_key: str) -> str:
    t = tabs(active)
    return f"""<body data-kpage="{page_key}">
<nav class="nav" data-sfx>
  <div class="wrap">
    <a href="index.html" class="logo"><span class="klogo"><img class="klogo-b" src="img/brand/logo-base.webp" alt="" width="128" height="128"><img class="klogo-a" src="img/brand/logo-arrow.webp" alt="" width="128" height="128"></span><span class="logo-t">Kompas Lab</span></a>
    {t}
    <span class="kl-sfx" data-sfx-slot></span><a href="login.html" class="btn btn-g btn-sm">Kirish</a>
  </div>
</nav>
<div class="kl-tabbar" data-sfx>{t}</div>
"""


def pagehead(crumbs: list[tuple[str, str | None]], h1: str, lead: str, art: str = "") -> str:
    parts = []
    for label, href in crumbs:
        parts.append(f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>")
    crumb = '<span aria-hidden="true">/</span>'.join(parts)
    img = f'<img class="kl-head-art float" src="img/3d/{art}.webp" alt="" width="160" height="160">' if art else ""
    return f"""<header class="kl-pagehead">
  <div class="wrap">
    <nav class="kl-crumb" aria-label="Yo'l">{crumb}</nav>
    <div class="kl-head-row"><div><h1>{h1}</h1><p class="lead">{lead}</p></div>{img}</div>
  </div>
</header>
"""


FOOTER = """<footer>
  <div class="wrap">
    <div><a href="index.html">Kompas Lab</a><a href="index.html#labs">Lablar</a><a href="atlas.html">Atlas</a><a href="sources.html">Rasmiy manbalar</a><a href="mailto:kompaslab.uz@gmail.com" translate="no">kompaslab.uz@gmail.com</a><a href="https://t.me/kompaslab" target="_blank" rel="noopener">Telegram</a><a href="maxfiylik.html">Maxfiylik siyosati</a></div>
    <div>&copy; 2026 Kompas Lab, O'zbekiston</div>
  </div>
</footer>
"""


def page(*, head_html: str, body: str, scripts: str = "") -> str:
    return uz(head_html + body + FOOTER + scripts + "</body>\n</html>\n")
