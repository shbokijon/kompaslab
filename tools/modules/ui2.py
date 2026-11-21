"""UI2 (2026-11-20, asoschi): pullik modullarning telefondagi kamçiliklari.

1. Jadval: 640px dan tor ekranda har qator kartochka, ustun nomi har qiymat ustida (td[data-label]).
2. Dars tablari (Diqqat, Asosiy qism, Xulosa, Topshiriq) ekranga teng boʻlinadi, gorizontal surish yoʻq.
3. Modul xaritasi: tugallangan (.done), joriy (.cur, ramka va sokin pulsatsiya), keyingi (xira) holatlari.
4. Modul ichidagi emoji va ✓ ✗ ★ ⚠️ belgilari yagona chiziqli SVG ikonkaga almashadi
   (Lucide uslubi, ISC litsenziyasi, stroke 2). 3D ikonkalar (img/3d) oʻzgarmaydi.

Qoʻllanadigan dasturlar: UI2_LABS. Hammasi faqat <main data-ui2> ichida ishlaydi,
shuning uchun roʻyxatda yoʻq dastur oʻzgarmaydi. Belgilar faqat HTML belgilashda almashtiriladi,
<script> ichidagi satrlarga tegilmaydi (JS yasaydigan qismlar oʻz belgisi bilan qoladi).
"""
import re

UI2_LABS = ("master-lab", "bachelor-lab")  # bachelor-lab: 2026-11-21 (Bakalavr v2)


def enabled(name):
    return name.startswith(UI2_LABS) and not name.endswith("-m0")


_P = {
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "list": '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>',
    "copy": '<rect width="14" height="14" x="8" y="8" rx="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
    "ccheck": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "book": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    "pen": '<path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "filter": '<path d="M22 3H2l8 9.46V19l4 2v-8.54L22 3z"/>',
    "brief": '<rect width="20" height="14" x="2" y="7" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "mic": '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v3"/>',
    "star": '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/>',
    "print": '<path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect width="12" height="8" x="6" y="14"/>',
    "upload": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m17 8-5-5-5 5"/><path d="M12 3v12"/>',
    "alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
}

# Belgi -> ikonka (VS16 U+FE0F bilan ham, bilmasdan ham)
_SYM = {
    "✓": "check", "✔": "check", "✗": "x", "✘": "x", "✅": "ccheck", "📋": "list", "📊": "chart",
    "📄": "file", "✉": "mail", "👥": "users", "📒": "book", "📚": "book", "📝": "pen", "✍": "pen",
    "🎯": "target", "🔍": "search", "🔻": "filter", "💼": "brief", "🧳": "brief", "🎙": "mic",
    "🎤": "mic", "★": "starf", "☆": "star", "⚠": "alert", "🖨": "print", "📤": "upload",
}


def icon(name, cls="ki"):
    # "starf" = toʻla yulduz (★), "star" = boʻsh (☆): "★★★★☆" kabi baho maʼnosi saqlanadi
    fill = "currentColor" if name == "starf" else "none"
    return ('<svg class="%s" viewBox="0 0 24 24" width="1em" height="1em" fill="%s" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>') % (cls, fill, _P["star" if name == "starf" else name])


_SYM_RE = re.compile("(" + "|".join(re.escape(k) for k in sorted(_SYM, key=len, reverse=True)) + ")️?")


def _icons_markup(html):
    """Faqat teglar orasidagi matnda (script/style/textarea dan tashqari) belgilarni almashtiradi."""
    out, pos = [], 0
    for m in re.finditer(r"<(script|style|textarea)\b.*?</\1>", html, flags=re.S | re.I):
        out.append(_icons_chunk(html[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(_icons_chunk(html[pos:]))
    return "".join(out)


def _icons_chunk(s):
    # teg atributlariga tegmaslik: faqat >...< oraligʻidagi matn
    def text(m):
        t = m.group(0)
        # "📋 Nusxa" kabi: belgidan keyingi boʻshliq ikonka oraligʻiga aylanadi
        return _SYM_RE.sub(lambda k: icon(_SYM[k.group(1)]), t)
    return re.sub(r">[^<]+<", text, s)


CSS = """<style id="kui2">
[data-ui2] svg.ki{width:1.05em;height:1.05em;vertical-align:-.16em;flex-shrink:0}
[data-ui2] .node .dot svg.ki{width:20px;height:20px;vertical-align:0}
[data-ui2] .ok svg.ki{width:.9em;height:.9em;vertical-align:-.1em}
/* 2. Tablar: teng boʻlinadi, surish yoʻq */
[data-ui2] .tabs{overflow:visible;gap:0;padding:6px 4px 0}
[data-ui2] .tab{flex:1 1 auto;min-width:0;padding:10px 4px;text-align:center;font-size:14px;white-space:nowrap}
[data-ui2] .tab .seen{margin-left:3px;width:6px;height:6px}
@media(max-width:420px){[data-ui2] .tab{font-size:13.5px;padding:10px 2px}}
@media(max-width:360px){[data-ui2] .tab{font-size:12.5px;white-space:normal;line-height:1.2}}
/* 3. Xarita holatlari */
[data-ui2] .node.cur{color:var(--accent)}
[data-ui2] .node.cur .dot{border:3px solid var(--accent);color:var(--accent);background:var(--surface);animation:kui2p 2.4s ease-in-out infinite}
[data-ui2] .node:not(.done):not(.cur){opacity:.5}
[data-ui2] .node:not(.done):not(.cur):hover{opacity:.8}
@keyframes kui2p{0%,100%{box-shadow:0 0 0 2px rgba(45,74,62,.16)}50%{box-shadow:0 0 0 7px rgba(45,74,62,0)}}
@media(prefers-reduced-motion:reduce){[data-ui2] .node.cur .dot{animation:none;box-shadow:0 0 0 3px rgba(45,74,62,.16)}}
/* 1. Jadval -> kartochka */
@media(max-width:640px){
[data-ui2] .tbl{overflow:visible}
[data-ui2] table.kst{min-width:0;font-size:14.5px}
[data-ui2] table.kst thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
[data-ui2] table.kst,[data-ui2] table.kst tbody,[data-ui2] table.kst tr,[data-ui2] table.kst td,[data-ui2] table.kst tbody th{display:block;width:100%}
[data-ui2] table.kst tr{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:8px 14px;margin:0 0 10px}
[data-ui2] table.kst td,[data-ui2] table.kst tbody th{border:0;padding:5px 0;background:none;color:inherit;text-align:left}
[data-ui2] table.kst td+td{border-top:1px dashed var(--border)}
[data-ui2] table.kst td[data-label]::before{content:attr(data-label);display:block;font-size:12px;font-weight:700;color:var(--muted);margin-bottom:1px}
[data-ui2] table.kst td:first-child{font-weight:700}
[data-ui2] table.kst td:first-child::before{font-weight:700}
[data-ui2] table.kst td:empty{display:none}
[data-ui2] table.kst input,[data-ui2] table.kst select,[data-ui2] table.kst textarea{width:100%}
}
@media print{[data-ui2] .node.cur .dot{animation:none}}
</style>
"""

JS = """<script id="kui2-js">(function(){
var main=document.querySelector("main[data-ui2]");if(!main)return;
function lab(t){var hs=[].map.call(t.querySelectorAll("thead th"),function(h){return (h.textContent||"").replace(/\\s+/g," ").trim();});
 if(hs.length<2)return;t.classList.add("kst");
 [].forEach.call(t.querySelectorAll("tbody tr"),function(r){var i=0;[].forEach.call(r.children,function(c){var n=+(c.getAttribute("colspan")||1);if(hs[i]&&c.getAttribute("data-label")!==hs[i])c.setAttribute("data-label",hs[i]);i+=n;});});}
function tables(){[].forEach.call(main.querySelectorAll("table"),lab);}
function nodes(){var f=false;[].forEach.call(main.querySelectorAll(".map .node"),function(n){var c=!f&&!n.classList.contains("done");if(c)f=true;if(n.classList.contains("cur")!==c)n.classList.toggle("cur",c);if(c){if(n.getAttribute("aria-current")!=="step")n.setAttribute("aria-current","step");}else if(n.hasAttribute("aria-current"))n.removeAttribute("aria-current");});}
var q=0;function run(){q=0;tables();nodes();}
run();
new MutationObserver(function(){if(!q)q=requestAnimationFrame(run);}).observe(main,{subtree:true,childList:true,attributes:true,attributeFilter:["class"]});
})();</script>
"""


def apply(name, html):
    if not enabled(name) or "data-ui2" in html:
        return html
    html = re.sub(r"<main\b", "<main data-ui2", html, count=1)
    html = _icons_markup(html)
    html = html.replace("</head>", CSS + "</head>", 1)
    i = html.rfind("</body>")
    return html[:i] + JS + html[i:]
