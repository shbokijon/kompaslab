"""Master M1–M8 v2 (2026-11-19): dars matnini qisqa standartga oʻtkazish uchun yordamchi.
Manba src/*.src.html dagi <article class="lesson"> ichidagi 4 ta .panel ni topadi."""
import re

def find_div_end(s, i):
    """s[i:] '<div' bilan boshlanadi; mos '</div>' oxirini qaytaradi."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[i:]):
        if m.group(0) == '<div': depth += 1
        else:
            depth -= 1
            if depth == 0: return i + m.end()
    raise ValueError('div yopilmadi')

def lesson_span(s, lid):
    a = s.index('<article class="lesson" id="%s">' % lid)
    b = s.index('</article>', a) + len('</article>')
    return a, b

def panels(art):
    """art ichidagi .l-body ning bevosita .panel bolalari: [(start,end)]"""
    out, pos = [], 0
    while True:
        i = art.find('<div class="panel">', pos)
        if i < 0: break
        j = find_div_end(art, i)
        out.append((i, j)); pos = j
    return out

INTERACTIVE = re.compile(r'\bid="|data-save=|<input|<textarea|<select|<button|data-q=|class="quiz|data-tool')

def interactive(html):
    return bool(INTERACTIVE.search(html))
