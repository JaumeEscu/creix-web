"""Builds the rest of the Creix site (home, hubs, secondary therapies) with the shared template."""
import sys, os, json, re, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from template import CSS, SITE, NAP, MAPS, MAP_EMBED, WA, GALLERY, header_html, footer_html, e, wix
from data import *

HERE = os.path.dirname(__file__)
SVC = json.load(open(os.path.join(HERE, "svc.json")))

EXTRA = """
.hero.tall img{min-height:640px}.hero .ctas{display:flex;gap:12px;flex-wrap:wrap}.btn.light{background:transparent;border:1px solid #e9e9e4;color:#fff}.btn.light:hover{background:rgba(255,255,255,.1)}
.kicker{font-family:var(--title);font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--sage);display:block;margin-bottom:12px}
.hero .kicker{color:var(--sage2)}
.tcards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:34px}
.tcard{background:#fff;border-radius:18px;overflow:hidden;text-decoration:none;color:var(--text);display:flex;flex-direction:column;transition:.2s;border:1px solid var(--band2)}.band .tcard{border:none}
.tcard:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(48,48,48,.08)}
.tcard img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}.tcard div{padding:22px 24px 26px}.tcard h3{margin:0 0 8px}.tcard p{font-size:16px;margin:0 0 10px}
.tcard .who{font-size:14px;color:var(--sage)}.tcard .more{font-family:var(--title);font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--green)}
.feat .tcard .tag{display:inline-block;background:var(--band2);color:var(--ink);font-size:13px;padding:3px 12px;border-radius:99px;margin-bottom:10px}
.chips{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:22px}.chips a{background:#fff;border:1px solid var(--band2);border-radius:99px;padding:8px 18px;text-decoration:none;color:var(--ink);font-size:15px}.chips a:hover{border-color:var(--sage)}
.team{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:34px}
.member{background:#fff;border-radius:18px;overflow:hidden;border:1px solid var(--band2)}.member img{width:100%;aspect-ratio:1;object-fit:cover;object-position:top;display:block}
.member div{padding:18px 20px 22px}.member h3{margin:0 0 2px;font-size:19px}.member .role{color:var(--sage);font-size:15px;margin:0 0 8px}.member p{font-size:14.5px;margin:0 0 8px;line-height:1.5}.member a{font-size:14.5px}
.faces{display:flex;justify-content:center;margin:26px 0 10px}.faces img{width:64px;height:64px;border-radius:50%;object-fit:cover;object-position:top;border:3px solid var(--band);margin-left:-12px}
.sched{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:30px;text-align:left}.day{background:#fff;border-radius:16px;padding:20px}.day h3{font-size:17px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:12px}
.slot{border-top:1px solid var(--band);padding:10px 0;font-size:15px;line-height:1.4}.slot b{display:block;font-weight:400;color:var(--sage);font-size:14px}.slot a{text-decoration:none;color:var(--ink)}
.posts{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:22px;margin-top:30px}
.post{background:#fff;border-radius:18px;overflow:hidden;text-decoration:none;color:var(--text);border:1px solid var(--band2)}.post img{width:100%;aspect-ratio:16/10;object-fit:cover;display:block}.post div{padding:20px 22px 24px}.post h3{font-size:19px}.post p{font-size:15.5px;margin:0}.post .meta{font-size:13px;color:var(--sage);letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px;display:block}
.body{max-width:780px;margin:0 auto}.body h3{margin-top:1.6em}.body ul{padding-left:20px}.body li{margin:6px 0}
.procard{display:grid;grid-template-columns:180px 1fr;gap:28px;align-items:center;background:var(--band);border-radius:22px;padding:28px;max-width:860px;margin:0 auto}.procard img{width:180px;height:180px;border-radius:50%;object-fit:cover;object-position:top}
.form{display:grid;gap:12px;max-width:520px}.form input,.form textarea,.form select{font:inherit;font-size:16px;padding:13px 16px;border:1px solid var(--band2);border-radius:12px;background:#fff;width:100%}.form textarea{min-height:120px}
.info{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:30px}.info .card h3{font-size:18px;letter-spacing:.1em;text-transform:uppercase}
.newsletter{display:flex;gap:10px;max-width:520px;margin:20px auto 0}.newsletter input{flex:1;font:inherit;padding:13px 18px;border:1px solid var(--band2);border-radius:50px}
.quote{font-family:var(--display);font-size:clamp(22px,2.6vw,30px);color:var(--ink);line-height:1.45;max-width:820px;margin:0 auto}
.hero .todo{color:#5a4500}.tcards.g4{grid-template-columns:repeat(4,1fr)}
.gallery.big{grid-template-columns:2fr 1fr 1fr 1fr;grid-template-rows:220px 220px}
@media(max-width:960px){.tcards,.tcards.g4,.team{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}.sched{grid-template-columns:1fr 1fr}.info{grid-template-columns:1fr}.hero .todo{color:#5a4500}.tcards.g4{grid-template-columns:repeat(4,1fr)}
.gallery.big{grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,160px)}}
@media(max-width:600px){.faces img{width:46px;height:46px;margin-left:-8px}.tcards,.tcards.g4,.team,.sched{grid-template-columns:1fr}.day{padding:14px 18px}.day h3{margin-bottom:4px}.procard{grid-template-columns:1fr;text-align:center}.procard img{margin:0 auto}.newsletter{flex-direction:column}}
"""

BUSINESS = {
    "@type": ["MedicalBusiness", "HealthAndBeautyBusiness"], "@id": SITE + "/#centro", "name": NAP["name"], "url": SITE + "/",
    "telephone": NAP["phone"], "email": NAP["email"], "image": wix("d90004_7457b69329bf44e2b5e9c9daba2db938~mv2.jpg", 1200, 1600),
    "address": {"@type": "PostalAddress", "streetAddress": NAP["street"], "postalCode": NAP["zip"], "addressLocality": NAP["city"],
                "addressRegion": NAP["region"], "addressCountry": "ES"},
    "areaServed": [{"@type": "City", "name": c} for c in ["Esplugues de Llobregat", "Barcelona", "L'Hospitalet de Llobregat", "Cornellà de Llobregat", "Sant Just Desvern"]],
    "sameAs": ["https://www.instagram.com/creixespaidesalut/", "https://www.facebook.com/profile.php?id=100086472607934"],
}


def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}


def crumbs_html(items):
    parts = [f'<a href="{u}">{e(n)}</a>' for n, u in items[:-1]] + [e(items[-1][0])]
    return f'<div class="wrap"><nav class="crumbs" aria-label="Migas de pan">{" › ".join(parts)}</nav></div>'


def shell(slug, title, meta, body, graph, og_img, active="", cta=None):
    url = SITE + (slug if slug != "/" else "/")
    ca = SITE + "/ca" + (slug if slug != "/" else "")
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(meta)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{url}">
<link rel="alternate" hreflang="ca" href="{ca}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(meta)}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="es_ES">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400&family=Heebo:wght@300;400&family=Jost:wght@300;400&display=swap" rel="stylesheet">
<style>{CSS}{EXTRA}</style>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header_html(active, *(cta or ()))}
<main>
{body}
</main>
{footer_html()}
</body>
</html>
"""


def wa(text):
    from urllib.parse import quote
    return WA + "?text=" + quote(text)


def pro_line(key):
    return TEAM[key][0] if key else "Equipo de Creix"


def tcard(k, feat=False, price=False):
    key, name, slug, cat, pro, img, desc, _, _ = T[k]
    tag = '<span class="tag">Primera visita 40 € reservando online</span>' if price else ""
    return (f'<a class="tcard" href="{slug}"><img src="{img}" alt="{e(name)} en Creix, Esplugues de Llobregat" loading="lazy">'
            f'<div>{tag}<h3>{e(name)}</h3><p>{e(desc)}</p><p class="who">Con {e(pro_line(pro))}</p><span class="more">Ver terapia →</span></div></a>')


def location_block(h2="Cómo llegar a Creix"):
    return f"""<section class="pad band"><div class="wrap loc"><div>
<h2>{e(h2)}</h2>
<p>Estamos en el centro de Esplugues de Llobregat, en el límite con Barcelona: a pocos minutos de Les Corts, Pedralbes, Sants, L'Hospitalet, Cornellà y Sant Just Desvern.</p>
<p><strong>{NAP['name']}</strong><br>{NAP['street']}<br>{NAP['zip']} {NAP['city']} (Barcelona)<br>Tel. y WhatsApp <a href="tel:{NAP['phone']}">{NAP['phone_h']}</a></p>
<p>{TODO.format('Horario del centro')}<br>{TODO.format('Metro, TRAM o bus más cercano y aparcamiento')}</p>
<a class="btn ghost" href="{MAPS}" target="_blank" rel="noopener">Cómo llegar</a>
</div><iframe src="{MAP_EMBED}" title="Mapa de Creix en Esplugues de Llobregat" loading="lazy"></iframe></div></section>"""


def final_block(h2, body, href, label):
    return f"""<section class="pad final"><div class="wrap"><h2>{e(h2)}</h2><p class="lead" style="margin:0 auto 26px">{body}</p>
<a class="btn" href="{href}">{e(label)}</a></div></section>"""


def faq_block(h2, faqs):
    return (f'<section class="pad faq" id="faq"><div class="wrap" style="max-width:860px"><h2 class="center">{e(h2)}</h2>'
            + "".join(f'<details><summary><h3>{e(q)}</h3></summary><p>{a}</p></details>' for q, a in faqs) + "</div></section>")


def faq_ld(url, faqs):
    return {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
        for q, a in faqs if "⚠️" not in a]}


# ------------------------------------------------------------------ HOME
def home():
    faces = "".join(f'<img src="{TEAM[k][3]}" alt="{e(TEAM[k][0])}" loading="lazy">' for k in ["sergi", "nathalie", "cristina", "laura", "sandra", "olga", "transi", "aurelie"])
    others = [t for t in THERAPIES if t[0] not in ("osteo", "gestalt", "reflexo")]
    chips = "".join(f'<a href="{t[2]}">{e(t[1])}</a>' for t in others)
    sched = "".join(
        f'<div class="day"><h3>{d}</h3>' + ("".join(f'<div class="slot"><b>{h}</b>{(f"<a href={chr(34)}{u}{chr(34)}>{e(n)}</a>") if u else e(n)}</div>' for h, n, u in s) or '<div class="slot">—</div>') + "</div>"
        for d, s in SCHEDULE if s)
    posts = "".join(post_card(p) for p in BLOG[:3])
    testis = "".join(f'<blockquote class="testi"><div class="stars">★★★★★</div><p>«{e(q)}»</p><cite>{e(n)}</cite></blockquote>' for q, n in TESTIS)
    faqs = [
        ("¿Qué terapias ofrece Creix en Esplugues de Llobregat?", "En Creix — Espai de Salut trabajan profesionales de osteopatía, terapia Gestalt, reflexología podal y drenaje linfático, psicoterapia, dietética y nutrición, PNI, acupuntura, constelaciones familiares, coaching psicocorporal, masaje integrativo y sexualidad consciente. También hay clases semanales de yoga, Movimiento Integral y Movimiento Expresivo, y grupos mensuales."),
        ("No sé qué terapia me conviene, ¿me podéis orientar?", "Sí. Escríbenos por WhatsApp al 613 61 33 56 contando brevemente qué te pasa y te recomendamos la terapia y el profesional del equipo de Creix que mejor encaja contigo, sin compromiso."),
        ("¿Dónde está Creix y cómo llego desde Barcelona?", "Creix está en el Carrer de Mossèn Jacint Verdaguer 37, en el centro de Esplugues de Llobregat (08950), en el límite con Barcelona y a pocos minutos de Les Corts, Pedralbes, Sants, L'Hospitalet, Cornellà y Sant Just Desvern."),
        ("¿Cuánto cuesta la primera visita?", "Depende de la terapia. En osteopatía y reflexología podal la sesión cuesta 50 € y la primera visita 40 € si la reservas online. En terapia Gestalt la sesión cuesta 65 € y la primera visita online 55 €. Para el resto de terapias, consulta con cada profesional."),
        ("¿Las sesiones son presenciales?", "Sí, todas las terapias de Creix se hacen en el centro de Esplugues de Llobregat. Algunos profesionales también ofrecen sesiones online; pregúntalo al pedir cita."),
    ]
    body = f"""
<section class="hero tall"><img src="{wix('4bcc8b_a0bb8cae2b5f45a6a9cd2ceb3023293d~mv2.jpg', 1100, 1100)}" alt="Equipo de terapeutas de Creix — Espai de Salut en Esplugues de Llobregat" width="640" height="640"><div class="panel">
<span class="kicker">Centro de bienestar integral · Esplugues de Llobregat</span>
<h1>Centro de terapias y bienestar en Esplugues de Llobregat</h1>
<p class="lead">Vuelve a sentirte bien contigo. Un espacio cercano, a pocos minutos de Barcelona, donde tu cuerpo, tus hábitos y tus emociones se acompañan de forma integrativa y personalizada.</p>
<div class="ctas"><a class="btn" href="/terapias">Ver todas las terapias</a><a class="btn light" href="{wa('Hola, no sé qué terapia me conviene. ¿Me podéis orientar?')}">¿No sabes qué te conviene? Te orientamos</a></div>
<ul class="checks"><li>Más de 15 terapias y 11 profesionales en un mismo centro</li><li>Osteopatía, reflexología y Gestalt con primera visita a precio reducido online</li><li>Clases semanales de yoga y movimiento</li></ul>
</div></section>

<div class="trust"><div class="wrap"><div><b>+15</b><span>terapias y actividades</span></div><div><b>11</b><span>profesionales</span></div><div><b>5 ★</b><span>reseñas en Google</span></div><div><b>10 min</b><span>de Barcelona</span></div></div></div>

<section class="pad"><div class="wrap center feat">
<span class="kicker">Lo más consultado</span>
<h2>Nuestras terapias principales</h2>
<p class="lead">Tres terapias con reserva online y primera visita a precio reducido. Si no sabes por dónde empezar, suele ser por aquí.</p>
<div class="tcards" style="text-align:left">{tcard('osteo', price=True)}{tcard('gestalt')}{tcard('reflexo', price=True)}</div>
</div></section>

<section class="pad band"><div class="wrap center">
<h2>Más terapias en Creix</h2>
<p class="lead">Cuerpo, mente y movimiento en un mismo lugar, con profesionales que se conocen y se derivan entre ellos cuando hace falta.</p>
<div class="chips">{chips}</div>
<p style="margin-top:30px"><a class="btn ghost" href="/terapias">Ver todas las terapias</a></p>
</div></section>

<section class="pad"><div class="wrap center">
<h2>¿No sabes qué terapia te conviene?</h2>
<p class="lead">Es la pregunta más habitual. Te ayudamos en tres pasos.</p>
<div class="steps" style="text-align:left">
<div class="step card"><h3>Nos cuentas qué te pasa</h3><p>Por WhatsApp o teléfono, con dos líneas basta: qué te preocupa y desde cuándo.</p></div>
<div class="step card"><h3>Te recomendamos a alguien</h3><p>Te decimos qué terapia y qué profesional del equipo encaja mejor contigo, y por qué.</p></div>
<div class="step card"><h3>Reservas tu primera visita</h3><p>En el centro de Esplugues, con tiempo para escucharte y un plan claro.</p></div>
</div>
<p style="margin-top:30px"><a class="btn" href="{wa('Hola, no sé qué terapia me conviene. ¿Me podéis orientar?')}">Escríbenos por WhatsApp</a></p>
</div></section>

<section class="pad band"><div class="wrap center">
<span class="kicker">Agenda semanal</span>
<h2>Actividades y clases en grupo</h2>
<p class="lead">Yoga, movimiento y mindfulness cada semana, y grupos mensuales de constelaciones, alta sensibilidad y círculo de mujeres.</p>
<div class="sched">{sched}</div>
<p style="margin-top:30px"><a class="btn ghost" href="/actividades">Ver actividades y talleres</a></p>
</div></section>

<section class="pad"><div class="wrap center">
<h2>Un equipo, muchas miradas</h2>
<div class="faces">{faces}</div>
<p class="lead">Osteópatas, psicólogas, terapeutas Gestalt, reflexólogas, dietistas y facilitadores de movimiento que comparten casa y forma de trabajar: cercana, honesta y sin humo.</p>
<p><a class="btn ghost" href="/equipo">Conoce al equipo</a></p>
</div></section>

<section class="pad band"><div class="wrap center"><h2>Lo que dicen de Creix</h2>
<div class="testis" style="text-align:left">{testis}</div>
<p style="margin-top:24px"><a href="https://g.page/r/CekMa9_hz6drEB0/review" rel="noopener">¿Has venido a Creix? Explícanos tu experiencia en Google →</a></p>
</div></section>

<section class="pad"><div class="wrap center">
<h2>Así es Creix</h2><p class="lead">Una casa luminosa en el centro de Esplugues, con consultas tranquilas y una sala para actividades. <a href="/el-centro">Conoce nuestra historia →</a></p>
<div class="gallery">{''.join(f'<img src="{s}" alt="{e(a)}" loading="lazy">' for s, a in GALLERY)}</div>
</div></section>

<section class="pad band"><div class="wrap center"><h2>Ideas para cuidarte con más criterio</h2>
<div class="posts" style="text-align:left">{posts}</div>
<p style="margin-top:26px"><a class="btn ghost" href="/blog">Ir al blog</a></p>
<h3 style="margin-top:56px">Recibe novedades y promociones</h3>
<form class="newsletter" onsubmit="return false"><input type="email" placeholder="Tu email" aria-label="Email"><button class="btn" type="submit">Suscribirme</button></form>
<p style="font-size:13px;margin-top:10px">Al suscribirte aceptas la <a href="/politica-privacidad">política de privacidad</a>.</p>
</div></section>

{location_block('Dónde estamos: Esplugues de Llobregat, junto a Barcelona')}
{faq_block('Preguntas frecuentes sobre Creix', faqs)}
{final_block('Vuelve a sentirte bien contigo', 'Cuéntanos qué te pasa y te orientamos hacia la terapia y el profesional que mejor encajan contigo.', wa('Hola, me gustaría pedir información'), 'Pide información por WhatsApp')}
"""
    graph = [dict(BUSINESS, description="Centro de terapias y bienestar integral en Esplugues de Llobregat: osteopatía, terapia Gestalt, reflexología, psicoterapia, nutrición, PNI, acupuntura y actividades de yoga y movimiento.",
                  hasOfferCatalog={"@type": "OfferCatalog", "name": "Terapias", "itemListElement": [
                      {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t[1], "url": SITE + t[2]}} for t in THERAPIES]}),
             {"@type": "WebSite", "@id": SITE + "/#web", "url": SITE + "/", "name": "Creix — Espai de Salut", "inLanguage": "es"},
             faq_ld(SITE + "/", faqs)]
    return shell("/", "Centro de terapias en Esplugues, junto a Barcelona | Creix Salut",
                 "Creix es un centro de terapias y bienestar en Esplugues de Llobregat: osteopatía, terapia Gestalt, reflexología, psicoterapia, nutrición, yoga y más. A 10 min de Barcelona.",
                 body, graph, GALLERY[0][0])


def post_card(p):
    t, u, cat, date, mins, ex, img = p
    return (f'<a class="post" href="{u}"><img src="{img}" alt="{e(t)}" loading="lazy"><div><span class="meta">{e(cat)} · {date} · {mins} min</span>'
            f'<h3>{e(t)}</h3><p>{e(ex)}</p></div></a>')


# ------------------------------------------------------------------ TERAPIAS HUB
def terapias():
    secs = []
    for i, (ck, cname, cdesc) in enumerate(CATS):
        cards = "".join(tcard(t[0], price=t[0] in ("osteo", "reflexo")) for t in THERAPIES if t[3] == ck)
        secs.append(f'<section class="pad{" band" if i % 2 == 0 else ""}" id="{ck}"><div class="wrap"><h2>{e(cname)}</h2><p class="lead">{e(cdesc)}</p><div class="tcards">{cards}</div></div></section>')
    faqs = [
        ("¿Qué terapia me conviene si tengo dolor de espalda?", 'Para el dolor de espalda, las cervicales o las migrañas que vuelven, la terapia más indicada en Creix suele ser la <a href="/osteopata-barcelona">osteopatía integrativa</a> con Sergi Català. Si el dolor tiene mucho componente de tensión o postura, se puede complementar con <a href="/movimiento-integral-esplugues">Movimiento Integral</a>.'),
        ("¿Qué terapia me conviene si tengo ansiedad o estrés?", 'Depende de cómo te afecte. Si es sobre todo mental y emocional, la <a href="/terapia-gestalt-barcelona">terapia Gestalt</a> o la <a href="/psicologa-esplugues">psicoterapia</a>. Si lo notas en el cuerpo, en el sueño o en la tensión muscular, la <a href="/reflexologia-podal-barcelona">reflexología podal</a> o el masaje integrativo ayudan a bajar el estado de alerta.'),
        ("¿Puedo combinar varias terapias?", "Sí, y es una de las ventajas de Creix: los profesionales comparten centro y pueden coordinarse o derivarte cuando lo ven útil, por ejemplo osteopatía con nutrición o PNI, o terapia Gestalt con trabajo corporal."),
        ("¿Cómo pido cita?", 'Para osteopatía, reflexología y terapia Gestalt puedes reservar online desde su página. Para el resto de terapias, escríbenos por WhatsApp al 613 61 33 56 y te ponemos en contacto con el profesional.'),
    ]
    items = [("Inicio", "/"), ("Terapias", "/terapias")]
    body = f"""{crumbs_html(items)}
<section class="pad" style="padding-bottom:40px"><div class="wrap center">
<span class="kicker">Esplugues de Llobregat · junto a Barcelona</span>
<h1>Terapias en Esplugues de Llobregat</h1>
<p class="lead">Más de 15 terapias y actividades para el cuerpo, la mente y las emociones, con profesionales que trabajan en el mismo centro y se conocen entre ellos.</p>
<div class="chips">{''.join(f'<a href="#{c}">{e(n)}</a>' for c, n, _ in CATS)}</div>
</div></section>
{''.join(secs)}
<section class="pad"><div class="wrap center"><h2>¿Dudas entre varias?</h2><p class="lead">Escríbenos dos líneas sobre lo que te pasa y te recomendamos por dónde empezar.</p>
<a class="btn" href="{wa('Hola, no sé qué terapia me conviene. ¿Me podéis orientar?')}">Te orientamos por WhatsApp</a></div></section>
{faq_block('Preguntas frecuentes sobre las terapias', faqs)}
"""
    graph = [BUSINESS, {"@type": "ItemList", "name": "Terapias en Creix", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t[1], "url": SITE + t[2]} for i, t in enumerate(THERAPIES)]},
        faq_ld(SITE + "/terapias", faqs), crumbs_ld(items)]
    return shell("/terapias", "Terapias en Esplugues de Llobregat | Creix Espai de Salut",
                 "Osteopatía, terapia Gestalt, reflexología, psicoterapia, nutrición, PNI, acupuntura, constelaciones, yoga y más terapias en Esplugues de Llobregat, junto a Barcelona.",
                 body, graph, THERAPIES[0][5], "/terapias")


# ------------------------------------------------------------------ EQUIPO
def anchor(name):
    return unicodedata.normalize("NFKD", name.lower()).encode("ascii", "ignore").decode().replace(" ", "-")


def equipo():
    cards = []
    for k, (name, role, cred, img, ths, tel) in TEAM.items():
        links = " · ".join(f'<a href="{T[t][2]}">{e(T[t][1])}</a>' for t in ths)
        cards.append(f'<article class="member" id="{anchor(name)}"><img src="{img}" alt="{e(name)}, {e(role.lower())} en Creix" loading="lazy">'
                     f'<div><h3>{e(name)}</h3><p class="role">{e(role)}</p><p>{e(cred)}</p><p>{links}</p></div></article>')
    items = [("Inicio", "/"), ("Equipo", "/equipo")]
    body = f"""{crumbs_html(items)}
<section class="pad" style="padding-bottom:30px"><div class="wrap center">
<span class="kicker">Quién te acompaña</span>
<h1>Equipo de terapeutas de Creix</h1>
<p class="lead">Once profesionales de la salud y el bienestar que comparten casa en Esplugues de Llobregat. Cada uno con su especialidad y una misma forma de trabajar: escuchar, explicar y acompañar sin humo.</p>
</div></section>
<section class="pad band"><div class="wrap"><div class="team">{''.join(cards)}</div>
<p class="center" style="margin-top:26px">{TODO.format('Revisar con cada profesional su titulación, nº de colegiado y años de experiencia')}</p></div></section>
<section class="pad"><div class="wrap center"><h2>¿Eres terapeuta y buscas consulta?</h2><p class="lead">Alquilamos consultas y salas equipadas para profesionales de la salud y el bienestar.</p><a class="btn ghost" href="/alquiler-salas-esplugues">Alquiler de salas</a></div></section>
{final_block('¿Con quién empiezo?', 'Cuéntanos qué te pasa y te recomendamos el profesional que mejor encaja contigo.', wa('Hola, ¿me podéis orientar sobre qué profesional me conviene?'), 'Te orientamos por WhatsApp')}
"""
    graph = [BUSINESS] + [{"@type": "Person", "@id": SITE + "/equipo#" + anchor(n), "name": n, "jobTitle": r, "image": img, "worksFor": {"@id": SITE + "/#centro"},
                           "knowsAbout": [T[t][1] for t in ths]} for n, r, c, img, ths, tel in TEAM.values()] + [crumbs_ld(items)]
    return shell("/equipo", "Equipo de terapeutas en Esplugues | Creix Espai de Salut",
                 "Conoce al equipo de Creix: osteópata, psicóloga, terapeuta Gestalt, reflexóloga, dietista y más profesionales de la salud en Esplugues de Llobregat.",
                 body, graph, TEAM["sergi"][3], "/equipo")


# ------------------------------------------------------------------ ACTIVIDADES
def actividades():
    sched = "".join(
        f'<div class="day"><h3>{d}</h3>' + ("".join(f'<div class="slot"><b>{h}</b>{(f"<a href={chr(34)}{u}{chr(34)}>{e(n)}</a>") if u else e(n)}</div>' for h, n, u in s) or '<div class="slot">Sin clases</div>') + "</div>"
        for d, s in SCHEDULE if s)
    groups = "".join(
        f'<{"a" if u else "div"} class="tcard"{f" href={chr(34)}{u}{chr(34)}" if u else ""}><img src="{img}" alt="{e(t)} en Creix, Esplugues" loading="lazy"><div><h3>{e(t)}</h3><p class="who">{e(w)}</p><p>{e(d)}</p>{"<span class=more>Más información →</span>" if u else ""}</div></{"a" if u else "div"}>'
        for t, w, d, img, u in GROUPS)
    items = [("Inicio", "/"), ("Actividades", "/actividades")]
    events_ld = [{"@type": "Event", "name": "Grupo PAS (alta sensibilidad)", "startDate": d, "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
                  "location": {"@id": SITE + "/#centro"}, "organizer": {"@id": SITE + "/#centro"}}
                 for d in ["2026-11-19T18:00", "2026-12-10T18:00", "2027-01-21T18:00", "2027-02-18T18:00", "2027-03-18T18:00", "2027-04-15T18:00", "2027-05-20T18:00", "2027-06-17T18:00"]]
    body = f"""{crumbs_html(items)}
<section class="pad" style="padding-bottom:30px"><div class="wrap center">
<span class="kicker">Agenda</span>
<h1>Actividades, clases y talleres en Esplugues</h1>
<p class="lead">Clases semanales de yoga, movimiento y mindfulness, y grupos mensuales para compartir y crecer. Todas las actividades son en la sala de Creix, en Esplugues de Llobregat.</p>
</div></section>
<section class="pad band"><div class="wrap center"><h2>Clases semanales</h2><div class="sched">{sched}</div>
<p style="margin-top:22px">{TODO.format('Confirmar horarios y profesor/a de Mindfulness, Mindful Vinyasa Yoga y Danza Útera')}</p>
<p><a class="btn" href="{wa('Hola, quiero probar una clase')}">Quiero probar una clase</a></p></div></section>
<section class="pad"><div class="wrap"><h2 class="center">Grupos y talleres mensuales</h2><div class="tcards g4">{groups}</div>
<p class="center" style="margin-top:26px">Información y reservas: <a href="tel:{NAP['phone']}">{NAP['phone_h']}</a></p></div></section>
{final_block('¿Te apuntas?', 'Escríbenos y te contamos plazas, precios y próximas fechas.', wa('Hola, quiero información sobre las actividades'), 'Pide información por WhatsApp')}
"""
    graph = [BUSINESS] + events_ld + [crumbs_ld(items)]
    return shell("/actividades", "Actividades y talleres en Esplugues: yoga, movimiento | Creix",
                 "Agenda de Creix en Esplugues de Llobregat: yoga, Movimiento Integral, Movimiento Expresivo, mindfulness, constelaciones familiares, grupo PAS y círculo de mujeres.",
                 body, graph, GROUPS[0][3], "/actividades")


# ------------------------------------------------------------------ EL CENTRO (historia)
def el_centro():
    items = [("Inicio", "/"), ("El centro", "/el-centro")]
    gal = "".join(f'<img src="{s}" alt="{e(a)}" loading="lazy">' for s, a in SPACES[:7])
    body = f"""{crumbs_html(items)}
<section class="hero"><img src="{SPACES[0][0]}" alt="Fachada de Creix — Espai de Salut en Esplugues de Llobregat" width="640" height="560"><div class="panel">
<span class="kicker">Nuestra historia</span>
<h1>Creix, espai de salut en Esplugues de Llobregat</h1>
<p class="lead">Creix continúa el proyecto que iniciaron hace muchos años Carme Casellas y Josefina Vilà, entonces «Creix el taller»: un espacio donde las personas pudieran sanar física y emocionalmente, dar charlas de crecimiento personal e intercambiar experiencias humanas profundas.</p>
</div></section>
<section class="pad"><div class="wrap center"><p class="quote">«Con agradecimiento por el pasado recibido y con las alas abiertas para seguir volando hacia adelante.»</p></div></section>
<section class="pad band"><div class="wrap"><h2 class="center">Cómo trabajamos</h2><div class="cards">
<div class="card"><h3>Integrativo</h3><p>Cuerpo, hábitos y emociones van juntos. Por eso en una misma casa hay osteopatía, psicoterapia, nutrición, reflexología y movimiento.</p></div>
<div class="card"><h3>Cercano</h3><p>Un centro de barrio, con tiempo para escucharte y profesionales que te explican qué hacen y por qué.</p></div>
<div class="card"><h3>En equipo</h3><p>Los terapeutas se conocen y se derivan entre ellos cuando ven que otra mirada te puede ayudar.</p></div>
</div><p class="center" style="margin-top:22px">{TODO.format('Año de fundación de Creix el taller y relevo actual (para dar fuerza a la historia)')}</p></div></section>
<section class="pad"><div class="wrap center"><h2>Conoce el centro</h2><p class="lead">Una casa luminosa con consultas individuales, una sala polivalente para grupos y zonas comunes tranquilas.</p>
<div class="gallery big">{gal}</div></div></section>
{location_block()}
{final_block('¿Quieres alquilar una sala?', 'Consultas individuales y una sala polivalente para terapeutas y talleres.', '/alquiler-salas-esplugues', 'Ver alquiler de salas')}
"""
    graph = [dict(BUSINESS, founder=[{"@type": "Person", "name": "Carme Casellas"}, {"@type": "Person", "name": "Josefina Vilà"}]), crumbs_ld(items)]
    return shell("/el-centro", "Nuestra historia: Creix, espai de salut en Esplugues | Creix",
                 "Creix continúa el proyecto de Creix el taller de Carme Casellas y Josefina Vilà: un centro de salud integral en Esplugues de Llobregat. Conoce la casa y sus espacios.",
                 body, graph, SPACES[0][0], "/el-centro")


# ------------------------------------------------------------------ ALQUILER
def alquiler():
    items = [("Inicio", "/"), ("Alquiler de salas", "/alquiler-salas-esplugues")]
    faqs = [
        ("¿Qué tipo de salas alquiláis en Creix?", "En Creix, en Esplugues de Llobregat, alquilamos consultas individuales (ideales para psicología, nutrición, PNI o acupuntura, con camilla si hace falta) y una sala polivalente para grupos, talleres, yoga, formaciones o charlas."),
        ("¿Se puede alquilar por horas?", "⚠️ PENDIENTE: confirmar modalidades (horas, medias jornadas, días fijos) y precios."),
        ("¿Qué incluye el alquiler?", "Las salas están equipadas, son luminosas y tranquilas. Incluyen el uso de las zonas comunes: sala de espera para tus pacientes, zona de descanso para profesionales y baño adaptado."),
        ("¿Cómo puedo ver las salas?", "Escríbenos por WhatsApp al 613 61 33 56 y quedamos para que vengas a ver el centro."),
    ]
    sp = [("Consultas individuales", "Ideales para psicología, nutrición, PNI o acupuntura. Con camilla si la necesitas.", wix("4bcc8b_ad8104d5e1144502a2777bf3760aa9f8~mv2.png", 800, 600)),
          ("Sala polivalente para grupos", "Para talleres, yoga, formaciones o charlas, con espejo y luz natural.", wix("4bcc8b_dcf837f08f98421f811122014c5251b5~mv2.png", 800, 600)),
          ("Zonas comunes", "Sala de espera acogedora, zona de descanso para profesionales y baño adaptado.", wix("4bcc8b_c63344b66665423bb00760f24a3c6294~mv2.png", 800, 600))]
    cards = "".join(f'<div class="tcard"><img src="{i}" alt="{e(t)} en Creix, Esplugues" loading="lazy"><div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>' for t, d, i in sp)
    body = f"""{crumbs_html(items)}
<section class="hero"><img src="{wix('4bcc8b_734eb9edafed4a1b98349a80227e142b~mv2.png', 1000, 900)}" alt="Sala polivalente para talleres y yoga en Creix, Esplugues" width="640" height="560"><div class="panel">
<span class="kicker">Para profesionales</span>
<h1>Alquiler de consultas y salas para terapeutas en Esplugues</h1>
<p class="lead">Únete a una comunidad de salud integral. Alquilamos espacios equipados, luminosos y tranquilos para terapeutas, psicólogos y profesionales del bienestar, a pocos minutos de Barcelona.</p>
<div class="ctas"><a class="btn" href="{wa('Hola, me interesa alquilar una sala en Creix')}">Quiero alquilar</a></div>
</div></section>
<section class="pad band"><div class="wrap"><h2 class="center">Nuestros espacios</h2><div class="tcards">{cards}</div></div></section>
<section class="pad"><div class="wrap split"><div><h2>Pide información</h2><p>Cuéntanos qué tipo de espacio necesitas y con qué frecuencia y te respondemos con disponibilidad y precio.</p>
<p>{TODO.format('Precios orientativos por hora / media jornada')}</p></div>
<form class="form" onsubmit="return false"><input placeholder="Nombre y apellido"><input type="email" placeholder="Email"><input placeholder="Teléfono"><select><option>Consulta individual</option><option>Sala polivalente</option></select><textarea placeholder="¿Qué actividad harás y qué días te interesan?"></textarea><button class="btn" type="submit">Enviar</button></form></div></section>
{faq_block('Preguntas frecuentes sobre el alquiler de salas', faqs)}
"""
    graph = [BUSINESS, {"@type": "Service", "name": "Alquiler de consultas y salas para terapeutas", "provider": {"@id": SITE + "/#centro"},
                        "areaServed": {"@type": "City", "name": "Esplugues de Llobregat"}, "url": SITE + "/alquiler-salas-esplugues"},
             faq_ld(SITE + "/alquiler-salas-esplugues", faqs), crumbs_ld(items)]
    return shell("/alquiler-salas-esplugues", "Alquiler de salas y consultas para terapeutas en Esplugues | Creix",
                 "Alquila una consulta o una sala polivalente para terapias, talleres o yoga en Creix, Esplugues de Llobregat. Espacios equipados y luminosos junto a Barcelona.",
                 body, graph, sp[1][2], "/alquiler-salas-esplugues")


# ------------------------------------------------------------------ BLOG
def blog():
    items = [("Inicio", "/"), ("Blog", "/blog")]
    cats = sorted(set(p[2] for p in BLOG))
    body = f"""{crumbs_html(items)}
<section class="pad" style="padding-bottom:30px"><div class="wrap center">
<span class="kicker">Blog</span><h1>Blog de salud y bienestar</h1>
<p class="lead">Ideas para cuidarte con más criterio, escritas por el equipo de terapeutas de Creix.</p>
<div class="chips">{''.join(f'<a href="#">{e(c)}</a>' for c in cats)}</div></div></section>
<section class="pad band"><div class="wrap"><div class="posts">{''.join(post_card(p) for p in BLOG)}</div>
<p class="center" style="margin-top:26px">{TODO.format('Firmar cada artículo con el nombre del terapeuta (ahora sale «seo1220») y enlazar a su página')}</p></div></section>
<section class="pad"><div class="wrap center"><h3>Recibe novedades y promociones</h3>
<form class="newsletter" onsubmit="return false"><input type="email" placeholder="Tu email" aria-label="Email"><button class="btn" type="submit">Suscribirme</button></form></div></section>
"""
    graph = [BUSINESS, {"@type": "Blog", "name": "Blog de Creix", "url": SITE + "/blog", "blogPost": [
        {"@type": "BlogPosting", "headline": p[0], "url": SITE + p[1], "image": p[6]} for p in BLOG]}, crumbs_ld(items)]
    return shell("/blog", "Blog de salud y bienestar | Creix Espai de Salut",
                 "Artículos sobre osteopatía, emociones, respiración y nutrición escritos por los terapeutas de Creix, centro de salud integral en Esplugues de Llobregat.",
                 body, graph, BLOG[0][6], "/blog")


# ------------------------------------------------------------------ CONTACTO
def contacto():
    items = [("Inicio", "/"), ("Contacto", "/contacto")]
    body = f"""{crumbs_html(items)}
<section class="pad" style="padding-bottom:30px"><div class="wrap center">
<span class="kicker">Estamos para ayudarte</span><h1>Contacto y cómo llegar a Creix</h1>
<p class="lead">Escríbenos por WhatsApp, llámanos o ven a vernos al centro de Esplugues de Llobregat.</p>
<div class="info" style="text-align:left">
<div class="card"><h3>WhatsApp y teléfono</h3><p><a href="tel:{NAP['phone']}">{NAP['phone_h']}</a><br>{TODO.format('Hay otro teléfono en la web (625 401 537): dejar uno solo')}</p><a class="btn sm" href="{wa('Hola, me gustaría pedir información')}">Escribir por WhatsApp</a></div>
<div class="card"><h3>Dirección</h3><p>{NAP['street']}<br>{NAP['zip']} {NAP['city']} (Barcelona)</p><a class="btn sm ghost" href="{MAPS}" rel="noopener">Cómo llegar</a></div>
<div class="card"><h3>Email y horario</h3><p><a href="mailto:{NAP['email']}">{NAP['email']}</a><br>{TODO.format('Horario de atención')}</p></div>
</div></div></section>
<section class="pad band"><div class="wrap loc"><div><h2>Envíanos un mensaje</h2><p>Si lo prefieres, déjanos tus datos y te llamamos.</p>
<form class="form" onsubmit="return false"><input placeholder="Nombre"><input placeholder="Teléfono o email"><select><option>¿Sobre qué terapia?</option>{''.join(f'<option>{e(t[1])}</option>' for t in THERAPIES)}<option>Alquiler de salas</option></select><textarea placeholder="Escribe tu mensaje"></textarea><button class="btn" type="submit">Enviar</button></form></div>
<iframe src="{MAP_EMBED}" title="Mapa de Creix en Esplugues de Llobregat" loading="lazy" style="height:520px"></iframe></div></section>
"""
    graph = [BUSINESS, {"@type": "ContactPage", "url": SITE + "/contacto", "about": {"@id": SITE + "/#centro"}}, crumbs_ld(items)]
    return shell("/contacto", "Contacto | Creix Espai de Salut, Esplugues de Llobregat",
                 "Contacta con Creix en Carrer de Mossèn Jacint Verdaguer 37, Esplugues de Llobregat. Teléfono y WhatsApp 613 61 33 56.",
                 body, graph, GALLERY[0][0], "/contacto")


# ------------------------------------------------------------------ SECONDARY THERAPY PAGES
def clean(s):
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"_?[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4} ?-[0-9a-f]{12}_?", "", s)
    s = re.sub(r"[🥦⚖️⛹️🏊🧘‍♀️🤸🍎]", "", s)
    for a, b in [("entornoíntimo", "entorno íntimo"), ("Familiarescon", "Familiares con"), ("equipos(", "equipos ("), ("Mindfullnessy", "Mindfulness y"), ("accesoa", "acceso a"), ("trabajo:Pedagoga", "trabajo: Pedagoga"), ("ya la del", "y a la del"), ("Movimento", "Movimiento"), ("SÓN", "SUEÑO"), ("una poderoso", "un poderoso")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def body_html(paras, skip):
    out, ul = [], []
    def flush():
        if ul:
            out.append("<ul>" + "".join(f"<li>{e(x)}</li>" for x in ul) + "</ul>")
            ul.clear()
    for p in paras:
        p = clean(p)
        if any(p.startswith(s) for s in skip):
            continue
        if p[:1] in "•-⪢":
            ul.append(p.lstrip("•-⪢ ").strip()); continue
        if p.endswith("?") and len(p.split()) < 14:
            flush(); out.append(f"<h3>{e(p)}</h3>"); continue
        if len(p.split()) < 16 and not p.endswith((".", ":", "»", "”", '"')):
            ul.append(p); continue
        flush(); out.append(f"<p>{e(p)}</p>")
    flush()
    return "\n".join(out)


SKIP = ["Dietética y nutrición en Esplugues", "Movimento Integral-corrección", "Movimiento Expresivo-Rio Abierto", "Masaje Integrativo Sensitivo",
        "Hatha Yoga y meditación", "Psicoterapia y Chamanismo: Un Camino", "Un Enfoque Integral para la Sanación"]


def secondary(k):
    key, name, slug, cat, pro, img, desc, src, old = T[k]
    h1, title, meta, lead = SECONDARY[k]
    url = SITE + slug
    paras = SVC.get(src, [])
    content = body_html(paras, SKIP)
    p = TEAM.get(pro)
    hero_img = img
    pro_html = ""
    if p:
        tel = p[5].replace(" ", "")
        pro_html = f"""<section class="pad band"><div class="wrap"><div class="procard" style="background:#fff"><img src="{p[3]}" alt="{e(p[0])}, {e(p[1].lower())} en Creix" loading="lazy"><div>
<span class="kicker">Quién te acompaña</span><h2 style="margin-bottom:6px">{e(p[0])}</h2><p class="role" style="color:var(--sage)">{e(p[1])}</p><p>{e(p[2])}</p>
<p><a href="/equipo#{anchor(p[0])}">Ver en el equipo →</a> · Tel. <a href="tel:+34{tel}">{p[5]}</a></p></div></div></div></section>"""
    related = [t for t in THERAPIES if t[3] == cat and t[0] != k][:3]
    rel = "".join(tcard(t[0]) for t in related)
    items = [("Inicio", "/"), ("Terapias", "/terapias"), (name, slug)]
    cta = wa(f"Hola, quiero información sobre {name}")
    body = f"""{crumbs_html(items)}
<section class="hero"><img src="{hero_img}" alt="{e(name)} en Creix, Esplugues de Llobregat" width="640" height="560"><div class="panel">
<span class="kicker">{e(pro_line(pro))}</span>
<h1>{e(h1)}</h1>
<p class="lead">{e(lead)}</p>
<div class="ctas"><a class="btn" href="{cta}">Pide información o cita</a></div>
<ul class="checks"><li>Sesiones presenciales en Esplugues, junto a Barcelona</li><li>{TODO.format('Precio y duración de la sesión')}</li></ul>
</div></section>
<section class="pad"><div class="wrap"><div class="body">
<h2>{e(name)} en Creix</h2>
{content}
</div></div></section>
{pro_html}
<section class="pad"><div class="wrap"><h2 class="center">Otras terapias que te pueden interesar</h2><div class="tcards">{rel}</div></div></section>
{location_block(f'{name} cerca de Barcelona')}
{final_block(f'¿Quieres probar {name.lower()}?', 'Escríbenos y te contamos disponibilidad, precio y cómo es la primera sesión.', cta, 'Pide información por WhatsApp')}
"""
    svc = {"@type": "Service", "@id": url + "#servicio", "name": name, "description": meta, "url": url, "provider": {"@id": SITE + "/#centro"},
           "areaServed": [{"@type": "City", "name": "Esplugues de Llobregat"}, {"@type": "City", "name": "Barcelona"}]}
    graph = [BUSINESS, svc]
    if p:
        graph.append({"@type": "Person", "@id": SITE + "/equipo#" + anchor(p[0]), "name": p[0], "jobTitle": p[1], "image": p[3], "worksFor": {"@id": SITE + "/#centro"}})
        svc["performer"] = {"@id": SITE + "/equipo#" + anchor(p[0])}
    graph.append(crumbs_ld(items))
    return shell(slug, title, meta, body, graph, img, "/terapias", (cta, "Pide cita"))


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    pages = {"index": home(), "terapias": terapias(), "equipo": equipo(), "actividades": actividades(), "el-centro": el_centro(),
             "alquiler-salas-esplugues": alquiler(), "blog": blog(), "contacto": contacto()}
    for k in SECONDARY:
        pages[T[k][2].strip("/")] = secondary(k)
    for name, doc in pages.items():
        open(os.path.join(out, name + ".html"), "w").write(doc)
        print(name, len(doc))
