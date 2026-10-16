# ═══════════════════════════════════════════════════════════════
#  Globus maʼlumotlari: data/globe.json
#
#  Manbalar (Natural Earth, jamoat mulki — https://www.naturalearthdata.com/about/terms-of-use/):
#    naturalearth_lowres (1:110m davlatlar) va naturalearth_cities (poytaxtlar),
#    geopandas==0.14.4 paketidagi nusxa. Quruqlik nuqtalari: global-land-mask.
#  Ishga tushirish:
#    pip download geopandas==0.14.4 --no-deps -d /tmp/ne && unzip -o /tmp/ne/*.whl 'geopandas/datasets/naturalearth_*' -d /tmp/ne/x
#    pip install pyshp global-land-mask
#    python3 tools/globe/build_globe.py /tmp/ne/x/geopandas/datasets
# ═══════════════════════════════════════════════════════════════
import json, math, sys
from pathlib import Path
import shapefile
from global_land_mask import globe

DS = Path(sys.argv[1])
OUT = Path(__file__).resolve().parents[2] / "data" / "globe.json"
TOL = 0.3       # Duglas-Pekker soddalashtirish, gradus
STEP = 1.6      # quruqlik nuqtalari qadami, gradus

# Lab yoʻnalishlari: poytaxt va asosiy shaharlar (oʻzbekcha nom, kenglik, uzunlik)
CITIES = {
    "UZB": [("Toshkent", 41.31, 69.28, 1), ("Samarqand", 39.65, 66.96, 0), ("Buxoro", 39.77, 64.42, 0), ("Namangan", 41.0, 71.67, 0), ("Andijon", 40.78, 72.34, 0), ("Fargʻona", 40.39, 71.78, 0), ("Nukus", 42.46, 59.6, 0)],
    "GBR": [("London", 51.51, -0.13, 1), ("Manchester", 53.48, -2.24, 0), ("Edinburg", 55.95, -3.19, 0), ("Birmingem", 52.49, -1.89, 0), ("Lids", 53.8, -1.55, 0)],
    "USA": [("Vashington", 38.9, -77.04, 1), ("Nyu-York", 40.71, -74.01, 0), ("Boston", 42.36, -71.06, 0), ("Chikago", 41.88, -87.63, 0), ("Los-Anjeles", 34.05, -118.24, 0), ("San-Fransisko", 37.77, -122.42, 0)],
    "DEU": [("Berlin", 52.52, 13.4, 1), ("Myunxen", 48.14, 11.58, 0), ("Gamburg", 53.55, 9.99, 0), ("Frankfurt", 50.11, 8.68, 0)],
    "KOR": [("Seul", 37.57, 126.98, 1), ("Pusan", 35.18, 129.08, 0), ("Tejon", 36.35, 127.38, 0)],
    "POL": [("Varshava", 52.23, 21.01, 1), ("Krakov", 50.06, 19.94, 0), ("Vrotslav", 51.11, 17.03, 0)],
    "HUN": [("Budapesht", 47.5, 19.04, 1), ("Debretsen", 47.53, 21.63, 0), ("Seged", 46.25, 20.15, 0)],
    "TUR": [("Anqara", 39.93, 32.86, 1), ("Istanbul", 41.01, 28.98, 0), ("Izmir", 38.42, 27.14, 0)],
    "CHN": [("Pekin", 39.9, 116.4, 1), ("Shanxay", 31.23, 121.47, 0), ("Guanchjou", 23.13, 113.26, 0), ("Uxan", 30.59, 114.31, 0)],
    "JPN": [("Tokio", 35.68, 139.69, 1), ("Osaka", 34.69, 135.5, 0)],
}


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    a, b = pts[0], pts[-1]
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = math.hypot(dx, dy) or 1e-9
    i, dmax = 0, -1
    for k in range(1, len(pts) - 1):
        d = abs(dy * (pts[k][0] - a[0]) - dx * (pts[k][1] - a[1])) / n
        if d > dmax:
            i, dmax = k, d
    if dmax > eps:
        return rdp(pts[: i + 1], eps)[:-1] + rdp(pts[i:], eps)
    return [a, b]


def inside(x, y, ring):
    c = False
    for i in range(len(ring)):
        x1, y1 = ring[i - 1]
        x2, y2 = ring[i]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c


sf = shapefile.Reader(str(DS / "naturalearth_lowres/naturalearth_lowres.shp"))
countries, rings, polys = [], [], []
for ci, (rec, shp) in enumerate(zip(sf.records(), sf.shapes())):
    countries.append(rec["iso_a3"] if rec["iso_a3"] != "-99" else rec["name"][:3].upper())
    parts = list(shp.parts) + [len(shp.points)]
    for a, b in zip(parts[:-1], parts[1:]):
        ring = shp.points[a:b]
        polys.append((ci, ring))
        m = len(ring) // 2
        xs, ys = [q[0] for q in ring], [q[1] for q in ring]
        tol = min(TOL, math.hypot(max(xs) - min(xs), max(ys) - min(ys)) / 40)  # kichik davlatlar shaklini saqlash
        s = rdp(ring[: m + 1], tol) + rdp(ring[m:], tol)[1:]
        if len(s) < 3:
            continue
        flat, px, py = [ci], 0, 0
        for x, y in s:
            qx, qy = round(x * 10), round(y * 10)
            flat += [qx - px, qy - py]
            px, py = qx, qy
        rings.append(flat)

dots = []
lat = -58.0
while lat <= 80:
    n = max(1, int(round(360 * math.cos(math.radians(lat)) / STEP)))
    for i in range(n):
        lon = -180 + 360 * i / n
        if not globe.is_land(lat, lon):
            continue
        cc = -1
        for ci, ring in polys:
            if inside(lon, lat, ring):
                cc = ci
                break
        dots += [round(lat * 10), round(lon * 10), cc]
    lat += STEP

cf = shapefile.Reader(str(DS / "naturalearth_cities/naturalearth_cities.shp"))
caps = [[round(s.points[0][1], 2), round(s.points[0][0], 2)] for s in cf.shapes()]
cities = {k: [[n, la, lo, c] for n, la, lo, c in v] for k, v in CITIES.items()}

data = {"src": "Natural Earth 1:110m (jamoat mulki); quruqlik: global-land-mask", "c": countries, "r": rings, "d": dots, "cap": caps, "city": cities}
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
print(OUT, OUT.stat().st_size, "bayt;", len(rings), "chegara,", sum(len(r) for r in rings) // 2, "nuqta,", len(dots) // 3, "quruqlik nuqtasi,", len(caps), "poytaxt")
