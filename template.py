"""Shared template for Creix service pages (SEO + copy + schema)."""
import json, html

SITE = "https://www.creixsalut.com"
NAP = {
    "name": "Creix — Espai de Salut",
    "street": "Carrer de Mossèn Jacint Verdaguer, 37",
    "zip": "08950",
    "city": "Esplugues de Llobregat",
    "region": "Barcelona",
    "phone": "+34613613356",  # ⚠️ confirmar teléfono principal
    "phone_h": "613 61 33 56",
    "email": "creixcasellas@gmail.com",
}
WX = "https://static.wixstatic.com/media/"
def wix(i, w=1200, h=900):
    return f"{WX}{i}/v1/fill/w_{w},h_{h},q_85/{i}"
GALLERY = [
    (wix("d90004_7457b69329bf44e2b5e9c9daba2db938~mv2.jpg", 900, 1200), "Fachada de Creix — Espai de Salut en Esplugues de Llobregat"),
    (wix("d90004_3faf631ed871432b96cd9cb10ddce306~mv2.jpg", 800, 600), "Consulta con camilla en Creix"),
    (wix("d90004_51d42e55ba984cc7b83a34702afe09b6~mv2.jpg", 800, 600), "Despacho de consulta en Creix"),
    (wix("d90004_3835f3da659e4bd5b4f2b5ad9db0646a~mv2.jpg", 800, 600), "Sala de actividades de Creix"),
    (wix("4bcc8b_c63344b66665423bb00760f24a3c6294~mv2.png", 800, 600), "Pasillo luminoso con plantas en Creix"),
]
MAPS = "https://www.google.com/maps/search/?api=1&query=Creix+Espai+de+Salut+Carrer+Mossen+Jacint+Verdaguer+37+Esplugues+de+Llobregat"
MAP_EMBED = "https://www.google.com/maps?q=Carrer+de+Moss%C3%A8n+Jacint+Verdaguer+37,+08950+Esplugues+de+Llobregat&output=embed"

CSS = """
:root{--bg:#fff;--band:#f1f2ec;--band2:#dde0d3;--foot:#f1f2ec;--ink:#303030;--text:#4a4b44;--green:#5e6156;--sage:#8d9180;--sage2:#bcc1ab;--wood:#5e6156;--cta:#8d9180;--cta-d:#5e6156;--dark:#303030;--display:'Cinzel',Georgia,serif;--title:'Jost',system-ui,sans-serif;--body:'Heebo',system-ui,sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:var(--body);font-weight:300;color:var(--text);font-size:18px;line-height:1.65;background:var(--bg)}
h1,h2,h3{font-family:var(--title);color:var(--ink);line-height:1.2;margin:0 0 .6em}
h1{overflow-wrap:break-word;font-family:var(--display);font-size:clamp(26px,4vw,46px);font-weight:400;letter-spacing:.04em;text-transform:uppercase;line-height:1.25}
h2{font-size:clamp(28px,3.2vw,38px);font-weight:300}
h3{font-size:21px;font-weight:400}
p{margin:0 0 1em}a{color:var(--green)}strong,b{font-weight:600;color:var(--ink)}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
.pad{padding:80px 0}.band{background:var(--band)}.center{text-align:center}
.lead{font-size:20px;max-width:760px}.center .lead{margin-left:auto;margin-right:auto}
.eyebrow{display:inline-block;font-family:var(--body);font-size:15px;font-weight:400;color:#fff;margin-bottom:18px}
.btn{display:inline-block;background:var(--cta);color:#fff;font-family:var(--title);font-weight:400;font-size:15px;letter-spacing:.16em;text-decoration:none;padding:15px 32px;border-radius:50px;transition:.2s}
.btn:hover{background:var(--cta-d)}.btn.ghost{background:transparent;color:var(--green);border:1px solid var(--green)}
.price{font-family:var(--title);display:flex;gap:12px;align-items:baseline;flex-wrap:wrap;margin:14px 0 22px}
.price s{color:#9a9a9a;font-size:20px}.price strong{font-size:34px;font-weight:400;color:var(--ink)}.price em{font-style:normal;font-size:14px;background:var(--band2);color:var(--ink);padding:4px 12px;border-radius:99px}.hero .price s{color:#bdbdb6}.hero .price strong{color:#fff}.hero .price em{background:rgba(255,255,255,.14);color:#fff}
header.top{border-bottom:1px solid var(--band2);background:#fff;position:sticky;top:0;z-index:20}
header.top .wrap{display:flex;justify-content:space-between;align-items:center;height:68px}
.logo{font-family:var(--title);font-weight:300;font-size:30px;letter-spacing:.2em;color:var(--ink);text-decoration:none;line-height:1;text-align:center}.logo small{display:block;font-size:13px;letter-spacing:.24em;margin-top:4px;color:var(--ink)}
nav.main{display:flex;gap:22px}nav.main a{font-family:var(--title);font-size:14px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink);text-decoration:none;padding:6px 0;border-bottom:1px solid transparent}nav.main a:hover,nav.main a.on{border-color:var(--sage)}
.hright{display:flex;align-items:center;gap:14px}.lang{font-family:var(--title);font-size:13px;letter-spacing:.12em;color:var(--sage);text-decoration:none}.btn.sm{padding:10px 20px;font-size:13px}
.mnav{display:none;position:relative}.mnav summary{list-style:none;cursor:pointer;font-size:26px;color:var(--ink)}.mnav summary::-webkit-details-marker{display:none}.mnav div{position:absolute;right:0;top:44px;background:#fff;box-shadow:0 10px 30px rgba(0,0,0,.12);border-radius:14px;padding:12px 20px;display:flex;flex-direction:column;min-width:230px}.mnav div a{padding:10px 0;color:var(--ink);text-decoration:none;font-family:var(--title);letter-spacing:.1em;text-transform:uppercase;font-size:14px;border-bottom:1px solid var(--band)}
footer .copy{display:block;margin-top:30px;padding-top:18px;border-top:1px solid var(--band2);font-size:13px;color:#777}footer a{text-decoration:none}
nav.crumbs{font-size:14px;padding:14px 0 0}nav.crumbs a{text-decoration:none}
.hero>*{min-width:0}.hero{display:grid;grid-template-columns:1fr 1fr;background:var(--dark);margin-top:14px}.hero .panel{padding:60px 7vw 60px 56px;color:#e9e9e4;display:flex;flex-direction:column;justify-content:center}.hero h1{color:#fff}.hero .lead{color:#e9e9e4;font-size:18px}.hero strong{color:#fff}.hero .checks li:before{color:var(--sage2)}
.hero img{width:100%;height:100%;min-height:560px;object-fit:cover;display:block}
.checks{list-style:none;padding:0;margin:22px 0 0;font-size:16px}.checks li{padding-left:28px;position:relative;margin:6px 0}.checks li:before{content:"✓";position:absolute;left:0;color:var(--green);font-weight:700}
.trust{background:var(--band);color:var(--ink)}.trust .wrap{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:26px 22px;text-align:center}
.trust b{display:block;color:var(--ink);font-family:var(--display);font-weight:400;font-size:24px}.trust span{font-size:15px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;margin-top:34px}
.card{background:#fff;border:1px solid var(--band2);border-radius:18px;padding:26px}.band .card{border:none}
.card p{font-size:16px;margin:0}
.split{display:grid;grid-template-columns:1fr 1fr;gap:52px;align-items:center}
.split img{width:100%;border-radius:20px;object-fit:cover;aspect-ratio:4/3}
.compare{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:30px}
.compare .card h3{color:var(--green)}
.creds{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}.creds span{background:var(--band);border-radius:99px;padding:6px 14px;font-size:15px}
.steps{counter-reset:s;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:30px}
.step{background:#fff;border-radius:18px;padding:26px;position:relative}.step:before{counter-increment:s;content:counter(s);font-family:var(--title);font-weight:700;font-size:44px;color:var(--band2);position:absolute;right:20px;top:8px}
.pricebox{background:#fff;border:2px solid var(--green);border-radius:22px;padding:34px;max-width:620px;margin:30px auto 0;text-align:left}
.testis{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:30px}
.testi{margin:0;background:#fff;border-radius:18px;padding:26px;font-size:16px}.testi .stars{color:#f5a623;letter-spacing:2px}.testi cite{display:block;font-style:normal;font-weight:600;margin-top:10px;color:var(--ink)}
.todo{background:#fff6d6;border:1px dashed #d9a400;padding:2px 6px;border-radius:6px;font-size:14px}
.loc{display:grid;grid-template-columns:.9fr 1.1fr;gap:40px;align-items:start}.loc iframe{width:100%;height:340px;border:0;border-radius:18px}
.faq details{background:var(--band);border-radius:14px;margin:12px 0;padding:4px 22px}
.faq summary{cursor:pointer;list-style:none;padding:16px 0}.faq summary::-webkit-details-marker{display:none}
.faq summary h3{display:inline;font-size:18px;margin:0}.faq summary:after{content:"+";float:right;font-size:24px;color:var(--green)}
.faq details[open] summary:after{content:"–"}.faq details p{font-size:16.5px}
.final{background:var(--dark);color:#fff;text-align:center}.final h2{color:#fff}.final p{color:#e9e9e4}
footer{background:var(--foot);font-size:15px;padding:40px 0}footer .wrap{display:grid;grid-template-columns:1.3fr 1fr 1fr 1fr;gap:28px}
.gallery{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:200px 200px;gap:12px;margin-top:30px}.gallery img{width:100%;height:100%;object-fit:cover;border-radius:14px}.gallery img:first-child{grid-row:span 2}
.mbar{display:none}
@media(max-width:1080px){nav.main{display:none}.mnav{display:block}}
@media(max-width:560px){footer .wrap{grid-template-columns:1fr}.hero .btn{display:block;text-align:center}.hero .ctas{flex-direction:column}}
@media(max-width:860px){.lang{display:none}.hero.tall img{min-height:0}.hero .panel h1{font-size:clamp(26px,6.4vw,38px)}.gallery{grid-template-columns:1fr 1fr;grid-template-rows:160px 160px 160px}.gallery img:first-child{grid-column:span 2;grid-row:auto}.hero,.split,.loc,.compare{grid-template-columns:1fr}.hero img{min-height:0;aspect-ratio:4/3}.hero .panel{padding:40px 22px}.trust .wrap{grid-template-columns:repeat(2,1fr)}.steps{grid-template-columns:1fr}footer .wrap{grid-template-columns:1fr 1fr}.pad{padding:56px 0}
.mbar{display:flex;position:fixed;bottom:0;left:0;right:0;background:#fff;box-shadow:0 -4px 16px rgba(0,0,0,.08);padding:10px 14px;gap:10px;align-items:center;justify-content:space-between;z-index:30}.mbar .btn{padding:12px 18px;font-size:15px}body{padding-bottom:70px}}
"""

WA = "https://wa.me/34613613356"
NAV = [("/terapias", "Terapias"), ("/equipo", "Equipo"), ("/actividades", "Actividades"), ("/el-centro", "El centro"),
       ("/alquiler-salas-esplugues", "Alquiler de salas"), ("/blog", "Blog"), ("/contacto", "Contacto")]

def header_html(active="", cta_href=None, cta_label="Pide cita"):
    cta_href = cta_href or WA + "?text=Hola%2C%20quiero%20pedir%20informaci%C3%B3n"
    links = "".join(f'<a href="{h}"{" class=on" if h == active else ""}>{l}</a>' for h, l in NAV)
    return (f'<header class="top"><div class="wrap"><a class="logo" href="/">Creix<small>espai de salut</small></a>'
            f'<nav class="main" aria-label="Menú principal">{links}</nav>'
            f'<div class="hright"><a class="lang" href="/ca" hreflang="ca" title="Català">CA</a><a class="btn sm" href="{cta_href}">{html.escape(cta_label)}</a>'
            f'<details class="mnav"><summary aria-label="Abrir menú">☰</summary><div>{links}</div></details></div></div></header>')

def footer_html():
    return f"""<footer><div class="wrap">
<div><a class="logo" href="/" style="text-align:left">Creix<small>espai de salut</small></a><p style="margin-top:16px">{NAP['street']}<br>{NAP['zip']} {NAP['city']} (Barcelona)<br>Tel. y WhatsApp <a href="tel:{NAP['phone']}">{NAP['phone_h']}</a><br><a href="mailto:{NAP['email']}">{NAP['email']}</a></p></div>
<div><strong>Terapias destacadas</strong><br><a href="/osteopata-barcelona">Osteopatía</a><br><a href="/terapia-gestalt-barcelona">Terapia Gestalt</a><br><a href="/reflexologia-podal-barcelona">Reflexología podal</a><br><a href="/psicologa-esplugues">Psicoterapia</a><br><a href="/dietista-esplugues">Dietética y nutrición</a><br><a href="/terapias">Todas las terapias →</a></div>
<div><strong>Creix</strong><br><a href="/equipo">Equipo</a><br><a href="/actividades">Actividades y talleres</a><br><a href="/el-centro">Nuestra historia</a><br><a href="/alquiler-salas-esplugues">Alquiler de salas</a><br><a href="/blog">Blog</a><br><a href="/contacto">Contacto</a></div>
<div><strong>Síguenos</strong><br><a href="https://www.instagram.com/creixespaidesalut/" rel="noopener">Instagram</a><br><a href="https://www.facebook.com/profile.php?id=100086472607934" rel="noopener">Facebook</a><br><a href="https://g.page/r/CekMa9_hz6drEB0/review" rel="noopener">Déjanos una reseña en Google</a><p style="margin-top:14px;font-size:13px"><a href="/aviso-legal">Aviso legal</a> · <a href="/politica-privacidad">Privacidad</a> · <a href="/politica-cookies">Cookies</a></p></div>
</div><div class="wrap copy">© Creix — Espai de Salut · Esplugues de Llobregat</div></footer>"""

def e(s):
    return html.escape(s, quote=False)

def schema(p):
    url = SITE + p["slug"]
    org_id = SITE + "/#centro"
    business = {
        "@type": ["MedicalBusiness", "HealthAndBeautyBusiness"],
        "@id": org_id,
        "name": NAP["name"],
        "url": SITE + "/",
        "telephone": NAP["phone"],
        "email": NAP["email"],
        "address": {"@type": "PostalAddress", "streetAddress": NAP["street"], "postalCode": NAP["zip"],
                     "addressLocality": NAP["city"], "addressRegion": NAP["region"], "addressCountry": "ES"},
        "areaServed": [{"@type": "City", "name": c} for c in
                        ["Esplugues de Llobregat", "Barcelona", "L'Hospitalet de Llobregat", "Cornellà de Llobregat", "Sant Just Desvern"]],
        "sameAs": ["https://www.instagram.com/creixespaidesalut/"],
    }
    person = {"@type": "Person", "@id": url + "#profesional", "name": p["pro_name"], "jobTitle": p["pro_job"],
              "worksFor": {"@id": org_id}}
    if p.get("pro_extra"):
        person.update(p["pro_extra"])
    service = {
        "@type": "Service", "@id": url + "#servicio", "name": p["service_name"], "serviceType": p["service_type"],
        "description": p["meta"], "url": url, "provider": {"@id": org_id},
        "areaServed": {"@type": "City", "name": "Barcelona"},
        "offers": [
            {"@type": "Offer", "name": "Sesión", "price": p["price"], "priceCurrency": "EUR"},
            {"@type": "Offer", "name": "Primera visita reservando online", "price": p["price_online"], "priceCurrency": "EUR"},
        ],
    }
    faq = {"@type": "FAQPage", "@id": url + "#faq",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]}
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Terapias", "item": SITE + "/terapias"},
        {"@type": "ListItem", "position": 3, "name": p["crumb"], "item": url}]}
    return json.dumps({"@context": "https://schema.org", "@graph": [business, person, service, faq, crumbs]},
                      ensure_ascii=False, indent=2)

def page(p):
    h = []
    a = h.append
    url = SITE + p["slug"]
    a(f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['meta'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{url}">
<link rel="alternate" hreflang="ca" href="{SITE}/ca{p['slug']}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(p['meta'])}">
<meta property="og:image" content="{p['img_hero']}">
<meta property="og:locale" content="es_ES">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400&family=Heebo:wght@300;400&family=Jost:wght@300;400&display=swap" rel="stylesheet">
<style>{CSS.replace('IMG_FINAL', p['img_final'])}</style>
<script type="application/ld+json">
{schema(p)}
</script>
</head>
<body>
{header_html(p.get('nav','/terapias'), p['book'], p['cta_short'])}
<main>
<div class="wrap"><nav class="crumbs" aria-label="Migas de pan"><a href="/">Inicio</a> › <a href="/terapias">Terapias</a> › {e(p['crumb'])}</nav></div>

<!-- 1 · HERO -->
<section class="hero"><img src="{p['img_hero']}" alt="{e(p['img_hero_alt'])}" width="640" height="560"><div class="panel">
<span class="eyebrow">{e(p['eyebrow'])}</span>
<h1>{e(p['h1'])}</h1>
<p class="lead">{p['hero_sub']}</p>
<div class="price"><s>{p['price']} €</s><strong>{p['price_online']} €</strong><em>primera visita reservando online</em></div>
<a class="btn" href="{p['book']}">{e(p['cta'])}</a>
<ul class="checks">{''.join(f'<li>{x}</li>' for x in p['hero_checks'])}</ul>
</div></section>

<!-- 2 · TRUST BAR -->
<div class="trust"><div class="wrap">{''.join(f'<div><b>{k}</b><span>{v}</span></div>' for k, v in p['trust'])}</div></div>

<!-- 3 · PROBLEMAS -->
<section class="pad band"><div class="wrap center">
<h2>{e(p['pains_h2'])}</h2><p class="lead">{p['pains_intro']}</p>
<div class="cards" style="text-align:left">{''.join(f'<div class="card"><h3>{e(t)}</h3><p>{d}</p></div>' for t, d in p['pains'])}</div>
</div></section>

<!-- 4 · QUÉ ES / MÉTODO -->
<section class="pad"><div class="wrap split"><div>
<h2>{e(p['what_h2'])}</h2>{p['what_body']}
</div><img src="{p['img_what']}" alt="{e(p['img_what_alt'])}" loading="lazy"></div></section>
""")
    if p.get("extra_sections"):
        for sec in p["extra_sections"]:
            a(sec)
    a(f"""
<!-- 5 · COMPARATIVA -->
<section class="pad band"><div class="wrap">
<h2 class="center">{e(p['cmp_h2'])}</h2><p class="lead center" style="margin:0 auto">{p['cmp_intro']}</p>
<div class="compare">{''.join(f'<div class="card"><h3>{e(t)}</h3>{d}</div>' for t, d in p['cmp'])}</div>
</div></section>

<!-- 6 · PROFESIONAL -->
<section class="pad"><div class="wrap split"><img src="{p['img_pro']}" alt="{e(p['img_pro_alt'])}" loading="lazy"><div>
<h2>{e(p['pro_h2'])}</h2>
<div class="creds">{''.join(f'<span>{c}</span>' for c in p['creds'])}</div>
{p['pro_body']}
</div></div></section>

<!-- 7 · PROCESO -->
<section class="pad band"><div class="wrap center">
<h2>{e(p['steps_h2'])}</h2>
<div class="steps" style="text-align:left">{''.join(f'<div class="step"><h3>{e(t)}</h3><p>{d}</p></div>' for t, d in p['steps'])}</div>
<p style="margin-top:26px">{p['steps_note']}</p>
</div></section>

<!-- 8 · PRECIO -->
<section class="pad" id="precio"><div class="wrap center">
<h2>{e(p['price_h2'])}</h2>
<div class="pricebox">
<div class="price"><s>{p['price']} €</s><strong>{p['price_online']} €</strong><em>primera visita reservando online</em></div>
{p['price_body']}
<a class="btn" href="{p['book']}">{e(p['cta'])}</a>
</div></div></section>

<!-- 9 · OPINIONES -->
<section class="pad band"><div class="wrap center">
<h2>{e(p['testi_h2'])}</h2>
<div class="testis" style="text-align:left">{''.join(f'<blockquote class="testi"><div class="stars">★★★★★</div>{q}<cite>{n}</cite></blockquote>' for q, n in p['testis'])}</div>
</div></section>

<!-- 9b · EL CENTRO -->
<section class="pad"><div class="wrap center">
<h2>{e(p['gallery_h2'])}</h2><p class="lead">Una casa luminosa en el centro de Esplugues, con consultas tranquilas y una sala para actividades.</p>
<div class="gallery">{''.join(f'<img src="{src}" alt="{e(alt)}" loading="lazy">' for src, alt in GALLERY)}</div>
</div></section>

<!-- 10 · UBICACIÓN -->
<section class="pad band"><div class="wrap loc"><div>
<h2>{e(p['loc_h2'])}</h2>
{p['loc_body']}
<p><strong>{NAP['name']}</strong><br>{NAP['street']}<br>{NAP['zip']} {NAP['city']} ({NAP['region']})<br>
Tel. <a href="tel:{NAP['phone']}">{NAP['phone_h']}</a></p>
<a class="btn ghost" href="{MAPS}" target="_blank" rel="noopener">Cómo llegar</a>
</div><iframe src="{MAP_EMBED}" title="Mapa de Creix en Esplugues de Llobregat" loading="lazy"></iframe></div></section>

<!-- 11 · FAQ (GEO) -->
<section class="pad faq" id="faq"><div class="wrap" style="max-width:860px">
<h2 class="center">{e(p['faq_h2'])}</h2>
{''.join(f'<details><summary><h3>{e(q)}</h3></summary><p>{e(ans)}</p></details>' for q, ans in p['faqs'])}
</div></section>

<!-- 12 · CTA FINAL -->
<section class="pad final"><div class="wrap">
<h2>{e(p['final_h2'])}</h2><p class="lead" style="margin:0 auto 26px">{p['final_body']}</p>
<a class="btn" href="{p['book']}">{e(p['cta'])}</a>
{('<p style="margin-top:18px"><a style="color:#fff" href="' + p['test'] + '">' + p['test_label'] + '</a></p>') if p.get('test') else ''}
</div></section>
</main>

{footer_html()}
<div class="mbar"><span><b>{p['price_online']} €</b> 1ª visita online</span><a class="btn" href="{p['book']}">Reservar</a></div>
</body>
</html>
""")
    return "".join(h)
