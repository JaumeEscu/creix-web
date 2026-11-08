import sys, os, re, hashlib, glob, urllib.request, shutil
src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst + "/img", exist_ok=True); os.makedirs(dst + "/fonts", exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
# fonts
FONT = "https://fonts.googleapis.com/css2?family=Cinzel:wght@400&family=Heebo:wght@300;400&family=Jost:wght@300;400&display=swap"
css = get(FONT).decode()
def fnt(m):
    u = m.group(1); n = hashlib.md5(u.encode()).hexdigest()[:10] + ".woff2"
    p = dst + "/fonts/" + n
    if not os.path.exists(p): open(p, "wb").write(get(u))
    return f"url(fonts/{n})"
css = re.sub(r"url\((https://fonts.gstatic.com/[^)]+)\)", fnt, css)
# keep only latin subsets
blocks = re.findall(r"(/\* ([\w-]+) \*/\s*@font-face \{[^}]+\})", css)
css = "\n".join(b for b, sub in blocks if sub in ("latin", "latin-ext")) or css
open(dst + "/fonts.css", "w").write(css)
pages = {os.path.basename(f)[:-5] for f in glob.glob(src + "/*.html")}
cache = {}
def img(m):
    u = m.group(0)
    if u not in cache:
        ext = os.path.splitext(u.split("?")[0])[1] or ".jpg"
        ext = ".png" if ext.lower() == ".png" else ".jpg"
        n = hashlib.md5(u.encode()).hexdigest()[:10] + ext
        p = dst + "/img/" + n
        if not os.path.exists(p):
            try: open(p, "wb").write(get(u))
            except Exception as ex: print("FAIL", u, ex)
        cache[u] = "img/" + n
    return cache[u]
def link(m):
    h = m.group(1)
    if h.startswith("/post/"): return f'href="https://www.creixsalut.com{h}" target="_blank"'
    path, _, frag = h.partition("#")
    s = path.strip("/") or "index"
    if s in pages: return f'href="{s}.html{"#" + frag if frag else ""}"'
    return 'href="#"'
for f in glob.glob(src + "/*.html"):
    t = open(f).read()
    t = re.sub(r'<link rel="preconnect"[^>]+>', "", t)
    t = t.replace(f'<link href="{FONT}" rel="stylesheet">', '<link href="fonts.css" rel="stylesheet">')
    t = re.sub(r"https://static\.wixstatic\.com/media/[^\"' )]+", img, t)
    t = re.sub(r'href="(/[^"]*)"', link, t)
    t = re.sub(r'<iframe src="https://www.google.com/maps[^>]*></iframe>', '<a class="mapbox" href="https://www.google.com/maps/search/?api=1&query=Creix+Espai+de+Salut+Esplugues" target="_blank" rel="noopener"><span>📍 Mapa de Google<br><small>Carrer de Mossèn Jacint Verdaguer, 37 · Esplugues de Llobregat</small></span></a>', t)
    t = t.replace("</style>", ".mapbox{display:flex;align-items:center;justify-content:center;min-height:340px;border-radius:18px;background:var(--band2);text-decoration:none;color:var(--ink);text-align:center;font-family:var(--title);font-size:20px}.mapbox span{background:rgba(255,255,255,.9);padding:18px 26px;border-radius:14px}</style>")
    open(dst + "/" + os.path.basename(f), "w").write(t)
print(len(cache), "images")
