# Logotip fayllarini manba rasmdan qayta yaratish (repo ildizidan):
#   python3 tools/brand/make_logo.py
# Manba: tools/brand/logo-source.png (2000x2000, oq fon)
# Natija: img/brand/ — logo-base/arrow.webp (animatsiya qatlamlari), logo.webp, logo-512.png,
#         favicon-16/32.png, favicon.ico, apple-touch-icon, icon-192/512 (+maskable).
# Havola rasmi (og.jpg) alohida: tools/brand/og.html ni 1200x630 da skrinshot qilinadi.
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "img/brand"

im = np.asarray(Image.open(HERE / "logo-source.png").convert("RGB")).astype(int)
r, g, b = im[..., 0], im[..., 1], im[..., 2]
mn = np.minimum(np.minimum(r, g), b)
a = np.clip((255 - mn - 45) / 70, 0, 1)            # oq fon va xira halqa -> shaffof
blue = (b > r + 30) & (a > 0)                       # strelka
red = (r > g + 60) & ~blue & (a > .5)               # "<" (L)
H, W = r.shape
ys = np.arange(H)

# Strelka orqasida yashiringan qizil burchakni 45° chiziqlar boʻyicha toʻldirish (strelka harakatlanganda teshik koʻrinmasin)
xl = np.array([np.argmax(red[y]) if red[y].any() else -1 for y in ys])
occ = np.array([xl[y] > 2 and blue[y, max(0, xl[y] - 3)] for y in ys])
oy = ys[occ]
top = [y for y in range(oy.min() - 250, oy.min() - 30) if xl[y] > 0]
bot = [y for y in range(oy.max() + 30, oy.max() + 250) if xl[y] > 0]
c1 = np.median([xl[y] + y for y in top]); c2 = np.median([xl[y] - y for y in bot])
X, Y = np.meshgrid(np.arange(W), ys)
fill = blue & (X + Y >= c1) & (X - Y >= c2)
base_rgb = im.copy(); base_rgb[fill] = np.median(im[red], axis=0)
base_a = np.where(blue, 0, a); base_a = np.where(fill, 1, base_a)

y_, x_ = np.where(a > 0.05)
pad = 30; s = max(y_.max() - y_.min(), x_.max() - x_.min()) + 2 * pad
Y0 = (y_.min() + y_.max()) // 2 - s // 2; X0 = (x_.min() + x_.max()) // 2 - s // 2
crop = lambda arr: arr[Y0:Y0 + s, X0:X0 + s]
layer = lambda rgb, al: Image.fromarray(np.dstack([crop(rgb), crop(al * 255)]).astype(np.uint8), "RGBA")
full, base, arrow = layer(im, a), layer(base_rgb, base_a), layer(im, a * blue)
mark = layer(im, np.where(blue | (r > g + 60), a, 0))   # matnsiz belgi (favicon uchun)

OUT.mkdir(parents=True, exist_ok=True)
for img, n in [(full, "logo"), (base, "logo-base"), (arrow, "logo-arrow")]:
    img.resize((128, 128), Image.LANCZOS).save(OUT / (n + ".webp"), quality=90, method=6)
full.resize((512, 512), Image.LANCZOS).save(OUT / "logo-512.png", optimize=True)

def tile(src, size, fill=.84, rad=.24, opaque=False):
    t = Image.new("RGBA", (size, size), (0, 0, 0, 0)); m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * rad), fill=255)
    t.paste(Image.new("RGBA", (size, size), (255, 255, 255, 255)), (0, 0), m)
    if opaque: t = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    c = src.crop(src.getbbox()); k = size * fill / max(c.size)
    c = c.resize((max(1, int(c.width * k)), max(1, int(c.height * k))), Image.LANCZOS)
    t.alpha_composite(c, ((size - c.width) // 2, (size - c.height) // 2)); return t

tile(mark, 32, .86).save(OUT / "favicon-32.png"); tile(mark, 16, .9).save(OUT / "favicon-16.png")
tile(mark, 48, .86).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
tile(full, 180, .78, 0).save(OUT / "apple-touch-icon.png")
tile(full, 192, .78, .22).save(OUT / "icon-192.png"); tile(full, 512, .78, .22).save(OUT / "icon-512.png")
for size in (192, 512):
    tile(full, size, .58, 0, opaque=True).convert("RGB").save(OUT / ("icon-maskable-%d.png" % size), optimize=True)
print("img/brand/ yangilandi")
