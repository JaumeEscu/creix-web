import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from template import page, wix

CF = "https://d1yei2z3i6k35z.cloudfront.net/15540281/"
TODO = '<span class="todo">⚠️ {}</span>'

def ph(text):
    return "https://placehold.co/600x750/edeeea/57756b?text=" + text.replace(" ", "+")

# ---------------------------------------------------------------- OSTEOPATÍA
osteo = dict(
    slug="/osteopata-barcelona", gallery_h2="Así es Creix, tu espacio de salud en Esplugues", img_final=wix("d90004_7457b69329bf44e2b5e9c9daba2db938~mv2.jpg", 1600, 900), crumb="Osteopatía",
    title="Osteópata en Barcelona · Consulta en Esplugues | Creix",
    meta="Osteopatía integrativa con Sergi Català, colegiado nº 143 y casi 20 años de experiencia. Sesión 50 €, primera visita online 40 €. En Esplugues, junto a Les Corts.",
    eyebrow="Osteópata colegiado nº 143 · Casi 20 años de experiencia",
    h1="Osteópata en Barcelona: osteopatía integrativa en Esplugues",
    hero_sub="Si llevas tiempo con <strong>dolor de espalda, cervicales o migrañas</strong> que van y vienen, buscamos juntos la causa en lugar de poner otro parche. Consulta presencial en Esplugues de Llobregat, a pocos minutos de Les Corts, Sants y L'Hospitalet.",
    price=50, price_online=40,
    book="https://creix.systeme.io/pagoosteopatia1a1",
    cta="Reservar mi primera visita por 40 €", cta_short="Reservar cita",
    hero_checks=["No pagas nada al reservar: se paga en consulta", "Valoración, tratamiento y plan personalizado en la primera visita", "Si no avanzas, ajustamos la estrategia sin coste en la revisión"],
    img_hero=wix("4bcc8b_8da7e6663e494c14b4c2abac6ca7a5d1~mv2.jpeg", 1000, 1000),
    img_hero_alt="Sergi Català, osteópata en Barcelona, en su consulta de Creix",
    trust=[("Nº 143", "Organización Colegial de Osteópatas"), ("~20 años", "de experiencia clínica"), ("5 ★", "reseñas en Google"), ("40 €", "primera visita online")],
    pains_h2="¿Dolor que vuelve una y otra vez? Lo que tratamos en consulta",
    pains_intro="Te han dicho que es estrés, que es la edad o que es normal. Probablemente has probado analgésicos, masajes o fisioterapia y el alivio dura unos días. Estos son los casos que más vemos:",
    pains=[
        ("Dolor lumbar y lumbalgia", "La lumbalgia persistente rara vez es solo un problema de la zona baja de la espalda. Revisamos postura, estrés, descanso e inflamación para que no vuelva."),
        ("Dolor cervical y tensión en el cuello", "Cervicales cargadas, rigidez al girar la cabeza o tensión que sube hacia la cabeza al final del día."),
        ("Migrañas y dolores de cabeza", "Cuando la migraña tiene un componente tensional, digestivo u hormonal, el enfoque integrativo ayuda a espaciar los episodios."),
        ("Hombro y lesiones articulares", "Pinzamientos, manguito rotador y articulaciones que limitan el día a día, el trabajo o el deporte."),
        ("Estrés, fatiga e inflamación", "Ese cansancio que no se va, digestiones pesadas y la sensación de que cuerpo y mente no van a la par."),
    ],
    what_h2="Osteopatía integrativa: tratar la causa, no solo el síntoma",
    what_body="""<p>La osteopatía es una terapia manual que trabaja sobre músculos, articulaciones, fascias y vísceras para devolver movilidad y equilibrio al cuerpo. En Creix la combinamos con la <strong>PNI (psiconeuroinmunología)</strong> y la <strong>medicina funcional</strong>.</p>
<p>¿Por qué? Porque tu dolor, tu estrés, tu descanso, tu digestión y tu energía están conectados. Si solo tratamos la zona que duele, el problema vuelve. Si entendemos qué lo provoca, podemos darte un camino claro.</p>
<p>Sin tecnicismos vacíos y sin humo: te explicamos cada paso, por qué lo hacemos y qué puedes esperar.</p>""",
    img_what=wix("4bcc8b_408ee89b7e73412ba0467fffceb53c49~mv2.jpeg", 1200, 900),
    img_what_alt="Sesión de osteopatía integrativa en Creix, Esplugues de Llobregat",
    cmp_h2="¿Osteópata o fisioterapeuta? Cuándo elegir cada uno",
    cmp_intro="Las dos disciplinas son complementarias. La pregunta no es cuál es mejor, sino cuál encaja con lo que te pasa.",
    cmp=[
        ("Fisioterapia", "<p>Ideal para rehabilitar una lesión concreta, recuperar fuerza tras una operación o trabajar una zona específica con ejercicio y aparatología.</p>"),
        ("Osteopatía integrativa", "<p>Útil cuando el dolor es recurrente, cambia de sitio o se acompaña de estrés, fatiga o malas digestiones. Busca el origen y mira el cuerpo como un conjunto.</p><p>Si ya has ido al fisio y el dolor vuelve, es buen momento para probarla.</p>"),
    ],
    img_pro=wix("4bcc8b_f627c5e455a3494a84a742f7b6d5bb91~mv2.jpg", 1000, 750),
    img_pro_alt="Sergi Català, osteópata colegiado, tratando a un paciente",
    pro_h2="Sergi Català, osteópata colegiado en Barcelona",
    creds=["Universidad Atlántico Norte (Santander)", "Colegiado nº 143", "Casi 20 años de experiencia", "Especializado en PNI y medicina funcional"],
    pro_body="""<p>Soy osteópata integrativo. Durante casi 20 años he acompañado a personas con estrés crónico, lumbalgias persistentes, migrañas, fatiga e inflamación a recuperar su bienestar cuando nada más parecía funcionar.</p>
<p>Mi forma de trabajar es cercana y realista: te explico qué pasa en tu cuerpo y te doy un plan claro para cambiarlo. No sobrevivir: vivir bien.</p>
<p><a href="/equipo#sergi-catala">Conoce más sobre Sergi →</a></p>""",
    steps_h2="Cómo es tu primera visita al osteópata",
    steps=[
        ("1. Reservas online y ahorras 10 €", "Eliges día y hora en menos de un minuto. Recibes la confirmación por correo y no pagas nada por adelantado."),
        ("2. Valoración completa de tu caso", "Hablamos de tus síntomas, tu historia y tus hábitos, y hacemos una exploración osteopática."),
        ("3. Tratamiento y plan personalizado", "Recibes el primer tratamiento y sales sabiendo qué te pasa, qué vamos a hacer y por qué."),
    ],
    steps_note='¿Es tu primera vez? Lee <a href="/post/primera-visita-al-osteópata-qué-esperar-y-qué-preguntar">Primera visita al osteópata: qué esperar y qué preguntar</a>.',
    price_h2="Precio de la osteopatía en Barcelona: 50 € por sesión (primera visita online, 40 €)",
    price_body="""<p>Cada sesión de osteopatía cuesta <strong>50 €</strong>. Si reservas tu <strong>primera visita online</strong>, son <strong>40 €</strong>; reservada por otras vías, 50 €.</p>
<ul class="checks"><li>Incluye valoración, tratamiento y plan personalizado</li><li>Pagas en la consulta, no al reservar</li><li>Si no avanzas como esperas, ajustamos la estrategia en la revisión sin coste adicional</li></ul><br>""",
    testi_h2="Opiniones de pacientes del osteópata",
    testis=[
        ("<p>«Acudí al osteópata Sergi Català por un pinzamiento en el manguito rotador del hombro. El dolor era constante las 24h, ninguna medicina me aliviaba. […] En tres sesiones logró que volviera a tener una vida normal.»</p>", "Capi L. · Reseña en Google"),
        ("<p>«Había ido anteriormente a otros osteópatas, pero nunca había experimentado mejoras tan significativas tanto a nivel de movilidad como de dolor de espalda. […] A día de hoy tengo mucha más movilidad, menos dolor y, sobre todo, una calidad de vida muchísimo mejor.»</p>", "Jaume E. · Reseña en Google"),
        ("<p>«Suelo ir con Sergi de Osteopatía integrativa y me encanta, salgo de ahí como nueva. Muy recomendable.»</p>", "Paulina R. · Reseña en Google"),
    ],
    loc_h2="Tu osteópata cerca de Sants, Les Corts, L'Hospitalet y Cornellà",
    loc_body="<p>La consulta está en Esplugues de Llobregat, en el límite con Barcelona. Muchos de nuestros pacientes vienen de Les Corts, Pedralbes, Sants, L'Hospitalet, Cornellà y Sant Just Desvern.</p><p>" + TODO.format("Añadir cómo llegar: línea de metro/TRAM/bus más cercana y aparcamiento") + "</p>",
    faq_h2="Preguntas frecuentes sobre osteopatía",
    faqs=[
        ("¿Cuánto cuesta una sesión de osteopatía en Creix?", "Cada sesión de osteopatía cuesta 50 €. La primera visita cuesta 40 € si la reservas online en la web; si la reservas por otra vía, 50 €. El pago se hace en la consulta de Creix, en Esplugues de Llobregat, no al reservar. La primera visita incluye valoración, tratamiento y un plan personalizado."),
        ("¿La osteopatía duele?", "No debería doler. Algunas zonas con más tensión pueden notarse sensibles durante el tratamiento, pero la técnica se adapta siempre a ti y a lo que tu cuerpo tolera en cada momento. Si algo te molesta, lo dices y se ajusta. Es normal notar el cuerpo algo cansado o con agujetas suaves uno o dos días después."),
        ("¿Cuántas sesiones de osteopatía necesito?", "Depende de cada caso, y por eso la primera visita empieza con una valoración. En ella Sergi Català te explica qué ve, qué plan propone y por qué, para que sepas desde el principio qué esperar. Muchos pacientes notan cambios en las primeras sesiones; los dolores crónicos suelen necesitar un seguimiento más largo."),
        ("¿Qué es la osteopatía integrativa?", "Es osteopatía que no se queda solo en la zona que duele. En Creix, Sergi Català combina el trabajo manual con la PNI (psiconeuroinmunología) y la medicina funcional para entender cómo se conectan tu dolor, tu estrés, tu descanso, tu digestión y tu energía, y tratar la causa en lugar de solo el síntoma."),
        ("¿Osteópata o fisioterapeuta: a quién voy si me duele la espalda?", "Si tienes una lesión concreta que rehabilitar, el fisioterapeuta es una buena opción. Si el dolor de espalda vuelve una y otra vez, cambia de sitio o viene acompañado de estrés, fatiga o malas digestiones, la osteopatía integrativa busca el origen. Son complementarias y muchos pacientes de Creix llegan después de haber probado fisioterapia."),
        ("¿La osteopatía sustituye al médico?", "No. La osteopatía es un enfoque complementario a la medicina. Si durante la valoración Sergi Català detecta algo que necesite estudio médico, te lo dirá con claridad para que lo consultes con tu médico."),
        ("¿Tengo que pagar al reservar online?", "No. Reservar online solo bloquea tu hora y te aplica el precio de 40 € para la primera visita. El pago se hace el día de la cita, en la consulta de Creix en Esplugues de Llobregat."),
        ("¿Cuánto dura una sesión de osteopatía?", "⚠️ PENDIENTE: confirmar con Sergi la duración de la primera visita y de las sesiones de seguimiento."),
        ("¿La osteopatía la cubre la mutua o el seguro?", "⚠️ PENDIENTE: confirmar si Creix emite factura para reembolso de mutuas o trabaja con alguna aseguradora."),
        ("¿Dónde está la consulta y cómo llego desde Barcelona?", "La consulta está en Creix — Espai de Salut, Carrer de Mossèn Jacint Verdaguer 37, 08950 Esplugues de Llobregat, en el límite con Barcelona. Está a pocos minutos de Les Corts, Pedralbes, Sants, L'Hospitalet y Cornellà. ⚠️ Añadir transporte público y aparcamiento."),
    ],
    final_h2="Reserva tu primera visita de osteopatía en Esplugues",
    final_body="Descubre qué está causando tu dolor y sal de la consulta con un plan claro. Primera visita a 40 € reservando online, sin pagar nada por adelantado.",
    test="https://creix.systeme.io/osteopatia", test_label="¿Aún no lo tienes claro? Haz el test gratuito de 9 preguntas →",  # ⚠️ URL real del test
    service_name="Osteopatía integrativa", service_type="Osteopatía",
    pro_name="Sergi Català", pro_job="Osteópata", pro_extra={"hasCredential": "Colegiado nº 143, Organización Colegial de Osteópatas", "alumniOf": "Universidad Atlántico Norte"},
)

# ---------------------------------------------------------------- GESTALT
gestalt = dict(
    slug="/terapia-gestalt-barcelona", gallery_h2="Así es Creix, tu espacio de salud en Esplugues", img_final=wix("d90004_7457b69329bf44e2b5e9c9daba2db938~mv2.jpg", 1600, 900), crumb="Terapia Gestalt",
    title="Terapia Gestalt en Barcelona · En Esplugues u online | Creix",
    meta="Terapia Gestalt y trabajo corporal con Nathalie para la ansiedad, los límites y la sobrecarga. Sesión 65 €, primera online 55 €. Sin compromiso de continuidad.",
    eyebrow="Gestalt, cuerpo y movimiento · Presencial u online",
    h1="Terapia Gestalt en Barcelona: recupera la calma sin dejar de ser tú",
    hero_sub="Si vives con la mente acelerada, te cuesta poner límites o sientes que no llegas a todo, la terapia Gestalt te ayuda a entender qué te pasa y a <strong>dejar de vivir en ansiedad para empezar a vivir en calma</strong>. Sesiones en Esplugues de Llobregat o por videollamada.",
    price=65, price_online=55,
    book="https://creix.systeme.io/nathalie",  # ⚠️ enlace directo a la página de reserva
    cta="Reservar mi primera sesión por 55 €", cta_short="Reservar sesión",
    hero_checks=["Sin compromiso: avanzamos sesión a sesión", "No pagas nada al reservar", "Presencial en Creix o online desde casa"],
    img_hero=wix("d90004_4b3f7e4cd8c949388ea01e6b84d5da2c~mv2.jpg", 900, 1125), img_hero_alt="Consulta de terapia Gestalt en Creix, Esplugues de Llobregat",
    trust=[("Gestalt", "+ trabajo corporal"), ("Online", "o presencial"), ("Sin", "compromiso de sesiones"), ("55 €", "primera sesión online")],
    pains_h2="¿Te reconoces en alguna de estas situaciones?",
    pains_intro="El problema no eres tú, no es tu forma de ser. Muchas veces es una forma de funcionar que aprendiste y que hoy te pesa.",
    pains=[
        ("Mente acelerada y bucles que no paran", "Analizas conversaciones y decisiones una y otra vez, incluso cuando ya han pasado."),
        ("Ansiedad y dificultad para desconectar", "Te cuesta parar, dormir bien o saber qué necesitas de verdad."),
        ("Poner límites sin sentirte culpable", "Dices que sí cuando querrías decir que no, y después te sientes desbordada."),
        ("Sobrecarga: llegar a todo y olvidarte de ti", "Tareas, obligaciones y los demás siempre por delante. Tú, al final de la lista."),
        ("Personas altamente sensibles (PAS)", "Sientes con más intensidad y te agotas antes. Entenderlo cambia la forma de cuidarte."),
    ],
    what_h2="¿Qué es la terapia Gestalt y cómo puede ayudarte?",
    what_body="""<p>La terapia Gestalt es una corriente de psicoterapia humanista que trabaja en el <strong>aquí y el ahora</strong>, a partir de una relación de confianza entre terapeuta y paciente.</p>
<p>No se trata de analizar toda tu vida, sino de darte cuenta de cómo sientes, piensas y actúas hoy, comprender tu mente y descubrir los recursos que ya tienes para vivir con más calma y claridad.</p>
<p>No se trata de cambiar quién eres, sino de vivir sin dejar de ser quien eres.</p>""",
    img_what=wix("d90004_3835f3da659e4bd5b4f2b5ad9db0646a~mv2.jpg"), img_what_alt="Sala de trabajo corporal y movimiento en Creix",
    extra_sections=["""
<!-- 4b · CUERPO -->
<section class="pad" style="padding-top:0"><div class="wrap" style="max-width:860px">
<h2>Gestalt y trabajo corporal: cuando el cuerpo también habla</h2>
<p>La ansiedad y la sobrecarga no se quedan solo en la cabeza: aparecen como agotamiento, tensión y rigidez, insomnio, dolores de cabeza o problemas digestivos. Por eso Nathalie integra la terapia Gestalt con el <strong>trabajo corporal y el movimiento</strong>, para que el cambio no sea solo de comprensión, sino también de cómo lo vives en el cuerpo.</p>
</div></section>
"""],
    cmp_h2="¿Terapia Gestalt o psicólogo? En qué se diferencian",
    cmp_intro="Es una de las dudas más habituales antes de empezar. Esta es la diferencia en pocas palabras.",
    cmp=[
        ("Psicología clínica", "<p>Ejercida por psicólogos sanitarios. Indicada para diagnosticar y tratar trastornos de salud mental, a menudo con enfoques como el cognitivo-conductual.</p>"),
        ("Terapia Gestalt", "<p>Psicoterapia humanista y experiencial, centrada en el presente, las emociones y el cuerpo. Encaja cuando buscas conocerte, salir de bucles, poner límites o atravesar una crisis vital.</p><p>Si tienes un diagnóstico de salud mental, es complementaria a tu tratamiento médico o psicológico.</p>"),
    ],
    img_pro=wix("4bcc8b_c282d03d7c2d48ec9416aa3a6c8ba412~mv2.jpg", 1000, 750), img_pro_alt="Nathalie López, terapeuta Gestalt en Creix",
    pro_h2="Nathalie López, terapeuta Gestalt en Barcelona",
    creds=["Terapia Gestalt", "Trabajo corporal y movimiento", "⚠️ Formación y años de experiencia"],
    pro_body="""<p>Hola, soy Nathalie. Acompaño a personas que viven con la mente acelerada, que se olvidan de sí mismas o que no saben cómo poner límites sin sentirse culpables.</p>
<p>Mi forma de trabajar une la terapia Gestalt con el cuerpo y el movimiento. Hablemos primero, sin compromiso de continuidad.</p>
<p><a href="/equipo#nathalie-lopez">Conoce más sobre Nathalie →</a> · <a href="https://nathaliemotion.com" rel="noopener">nathaliemotion.com</a></p>""",
    steps_h2="Cómo es la primera sesión de terapia Gestalt",
    steps=[
        ("1. Un espacio seguro para contar lo que te pasa", "Explicas tu situación con calma, sin prisas y sin juicios."),
        ("2. Valoramos juntas si encaja", "Vemos si este acompañamiento es lo que necesitas y si Nathalie es la persona adecuada."),
        ("3. Decides si continuar, sin compromiso", "Resuelves tus dudas antes de comprometerte. Puedes dejarlo en cualquier momento."),
    ],
    steps_note="Recibes la confirmación con la dirección de Creix o el enlace de la videollamada.",
    price_h2="Precio de la terapia Gestalt: 65 € por sesión (primera sesión online, 55 €)",
    price_body="""<p>Cada sesión cuesta <strong>65 €</strong>. Si reservas tu <strong>primera sesión online</strong>, son <strong>55 €</strong>.</p>
<ul class="checks"><li>Pagas el día de la sesión, no al reservar</li><li>Sin número mínimo de sesiones</li><li>Mismo precio presencial u online</li></ul><br>""",
    testi_h2="Opiniones sobre la terapia Gestalt con Nathalie",
    testis=[
        ("<p>«Aprender a poner límites cambió completamente mi forma de vivir.» " + TODO.format("pegar testimonio completo del embudo") + "</p>", "Laura, 38 años"),
        ("<p>" + TODO.format("pegar testimonio literal de Carlos (crisis personal, claridad sobre su mente)") + "</p>", "Carlos, 44 años"),
        ("<p>«Siempre estaba pendiente de cómo estaban los demás y me olvidaba de mí.» " + TODO.format("pegar testimonio completo") + "</p>", "Marta, 35 años"),
        ("<p>" + TODO.format("pegar testimonio literal de Raquel (PAS)") + "</p>", "Raquel"),
    ],
    loc_h2="Terapia Gestalt presencial en Esplugues u online",
    loc_body="<p>Las sesiones presenciales son en Creix, en Esplugues de Llobregat, en el límite con Barcelona y a pocos minutos de Les Corts, Sants y L'Hospitalet. Si lo prefieres, puedes hacer la terapia online por videollamada desde casa, con el mismo precio y la misma forma de trabajar.</p>",
    faq_h2="Preguntas frecuentes sobre la terapia Gestalt",
    faqs=[
        ("¿Qué es la terapia Gestalt?", "La terapia Gestalt es una corriente de psicoterapia humanista que trabaja en el aquí y el ahora, basada en una relación de confianza. Ayuda a darte cuenta de cómo te sientes, piensas y actúas, y a descubrir tus propios recursos. En Creix, Nathalie la integra con trabajo corporal y movimiento."),
        ("¿Cuánto cuesta la terapia Gestalt en Creix?", "Cada sesión de terapia Gestalt con Nathalie cuesta 65 €. La primera sesión cuesta 55 € si la reservas online. El pago se hace el día de la sesión, no al reservar, y el precio es el mismo presencial en Esplugues de Llobregat u online."),
        ("¿Qué pasa en la primera sesión?", "En la primera sesión explicas tu situación, valoráis juntas si el acompañamiento encaja y si Nathalie es la persona adecuada, y resuelves tus dudas. Después decides si quieres continuar, sin ningún compromiso."),
        ("¿Tengo que comprometerme a un número de sesiones?", "No. En la terapia Gestalt con Nathalie se avanza sesión a sesión y puedes dejarlo cuando quieras. No hay paquetes obligatorios ni número mínimo de sesiones."),
        ("¿La terapia Gestalt sirve para la ansiedad?", "La terapia Gestalt ayuda a muchas personas con ansiedad, mente acelerada y bucles mentales, porque trabaja cómo vives tus emociones en el presente e incluye el cuerpo, donde la ansiedad también se manifiesta. Si tienes un diagnóstico de trastorno de ansiedad, es un acompañamiento complementario a tu tratamiento médico o psicológico."),
        ("¿En qué se diferencia de ir al psicólogo?", "La psicología clínica diagnostica y trata trastornos de salud mental, a menudo con enfoques como el cognitivo-conductual. La terapia Gestalt es una psicoterapia humanista y experiencial, centrada en el presente, las emociones y el cuerpo. Encaja especialmente cuando buscas conocerte, salir de bucles, poner límites o atravesar una crisis vital."),
        ("¿La terapia Gestalt funciona online?", "Sí. Nathalie ofrece sesiones de terapia Gestalt por videollamada con la misma forma de trabajar que en consulta. Al reservar recibes el enlace de la videollamada. Es una buena opción si vives lejos de Esplugues de Llobregat o tienes poco tiempo para desplazarte."),
        ("¿Tengo que pagar al reservar online?", "No. Reservar online solo bloquea tu hora y te aplica el descuento de 10 €. Pagas 55 € el día de la primera sesión."),
        ("¿Cada cuánto son las sesiones y cuánto duran?", "⚠️ PENDIENTE: confirmar con Nathalie la duración y la frecuencia habitual de las sesiones."),
        ("¿Dónde son las sesiones presenciales?", "Las sesiones presenciales son en Creix — Espai de Salut, Carrer de Mossèn Jacint Verdaguer 37, 08950 Esplugues de Llobregat, en el límite con Barcelona y a pocos minutos de Les Corts, Sants y L'Hospitalet."),
    ],
    final_h2="Reserva tu primera sesión de terapia Gestalt",
    final_body="Hablemos primero, sin compromiso de continuidad. Primera sesión a 55 € reservando online, presencial en Esplugues u online.",
    service_name="Terapia Gestalt y trabajo corporal", service_type="Psicoterapia Gestalt",
    pro_name="Nathalie López", pro_job="Terapeuta Gestalt", pro_extra={"sameAs": ["https://nathaliemotion.com"]},
)

# ---------------------------------------------------------------- REFLEXOLOGÍA
reflexo = dict(
    slug="/reflexologia-podal-barcelona", gallery_h2="Así es Creix, tu espacio de salud en Esplugues", img_final=wix("d90004_7457b69329bf44e2b5e9c9daba2db938~mv2.jpg", 1600, 900), crumb="Reflexología podal",
    title="Reflexología podal en Barcelona · Terapéutica, en Esplugues | Creix",
    meta="Reflexología terapéutica con Cristina Negrié, +10 años de experiencia. Para dormir mejor, el estrés y la tensión. Sesión 50 €, primera visita online 40 €.",
    eyebrow="Reflexología terapéutica · +10 años de experiencia",
    h1="Reflexología podal en Barcelona: no es solo relajación",
    hero_sub="Si duermes pero no descansas, acumulas tensión o vives en alerta, la reflexología terapéutica <strong>ayuda a regular tu sistema nervioso y recuperar tu bienestar</strong>. Consulta en Esplugues de Llobregat, junto a Les Corts y Sants.",
    price=50, price_online=40,
    book="https://creix.systeme.io/reflexologia",  # ⚠️ enlace directo a la página de reserva
    cta="Reservar mi valoración por 40 €", cta_short="Reservar cita",
    hero_checks=["Valoración inicial personalizada", "No pagas nada al reservar", "Complementa la medicina, no la sustituye"],
    img_hero=wix("4bcc8b_2fb20821117449f58d71ea89cdb5f650~mv2.png", 1000, 900), img_hero_alt="Sesión de reflexología podal terapéutica en Creix, Esplugues",
    trust=[("+10 años", "de experiencia"), ("1–3", "sesiones para notar cambios*"), ("5 ★", "opiniones de pacientes"), ("40 €", "primera visita online")],
    pains_h2="¿Para qué sirve la reflexología? Lo que tratamos",
    pains_intro="La reflexología podal estimula puntos reflejos de los pies para enviar señales al cerebro y ayudar al cuerpo a regularse. Estos son los motivos de consulta más habituales:",
    pains=[
        ("Insomnio y sueño que no descansa", "Duermes, pero te levantas cansada. La reflexología ayuda a bajar el estado de alerta y mejorar la calidad del sueño."),
        ("Estrés y ansiedad", "Para cuando el sistema nervioso no sabe apagarse, también en procesos médicos exigentes."),
        ("Tensión en cuello, hombros y mandíbula", "Tensión muscular crónica que se acumula con el estrés del día a día."),
        ("Fascitis plantar y dolor de pies", "Dolor en los primeros pasos del día y pies cargados."),
        ("Cambios hormonales y fatiga", "Cansancio sin explicación, cambios de humor y la sensación de estar desconectada de ti."),
        ("Digestión y retención de líquidos", "Pesadez, hinchazón e inflamación que hacen el día más difícil."),
    ],
    what_h2="Cómo funciona la reflexología terapéutica",
    what_body="""<p>La reflexología podal, también llamada reflexoterapia, no es un masaje de pies: cada sesión es personalizada, con valoración previa y seguimiento cercano. Trabajamos sobre tres sistemas:</p>
<h3>Sistema nervioso: bajar el estado de alerta</h3><p>Reduce el estrés y la ansiedad y mejora la calidad del sueño.</p>
<h3>Sistema endocrino: equilibrio hormonal</h3><p>Ayuda con los cambios hormonales ligados a la fatiga, el humor y el malestar.</p>
<h3>Sistema linfático: menos inflamación y pesadez</h3><p>Favorece la eliminación de toxinas y reduce la retención de líquidos.</p>""",
    img_what=wix("4bcc8b_fdce4275a58741958c96d858586a5265~mv2.jpg"), img_what_alt="Sesión de reflexología podal terapéutica en Creix, Esplugues",
    extra_sections=["""
<!-- 4b · OTRAS TÉCNICAS (pendiente) -->
<section class="pad" style="padding-top:0"><div class="wrap" style="max-width:860px">
<h2>Otras técnicas de reflexología</h2>
<p><span class="todo">⚠️ PENDIENTE: confirmar con Cristina qué otras técnicas hace (manos, facial, craneal, auricular…). Un H3 y un párrafo por técnica. Si no hace ninguna, eliminar esta sección.</span></p>
</div></section>
""", """
<!-- 4c · EMBARAZO Y TRATAMIENTOS -->
<section class="pad band"><div class="wrap" style="max-width:860px">
<h2>Reflexología en el embarazo y durante tratamientos médicos</h2>
<p>La reflexología es compatible con muchos tratamientos médicos, también oncológicos, y puede ayudar con la fatiga, las náuseas y la ansiedad que los acompañan. También acompaña molestias del embarazo.</p>
<p><strong>Esto no sustituye a la medicina: la acompaña.</strong> Si estás embarazada o en tratamiento, coméntalo al reservar para adaptar la sesión. <span class="todo">⚠️ Añadir contraindicaciones que indique Cristina</span></p>
</div></section>
"""],
    cmp_h2="Reflexología terapéutica o masaje de pies: la diferencia",
    cmp_intro="Un masaje de pies relaja. La reflexología terapéutica busca un efecto concreto en tu cuerpo.",
    cmp=[
        ("Masaje de pies en un spa", "<p>Agradable y relajante, pensado para desconectar un rato. No hay valoración previa ni un objetivo terapéutico.</p>"),
        ("Reflexología terapéutica en Creix", "<p>Empieza con una valoración, trabaja puntos reflejos concretos según lo que te pasa y tiene seguimiento entre sesiones. No es solo relajación.</p>"),
    ],
    img_pro=wix("4bcc8b_0fb25c7f9cc442b4a2e5a3258629dc21~mv2.jpg", 1000, 750), img_pro_alt="Cristina Negrié, reflexóloga, durante una sesión en Creix",
    pro_h2="Cristina Negrié, reflexóloga en Barcelona",
    creds=["+10 años de experiencia", "Especializada en estrés, dolor físico y desequilibrio corporal", "⚠️ Formación"],
    pro_body="""<p>Trabajo con un enfoque serio, personalizado y honesto. Escucho lo que te pasa y adapto cada sesión a tus necesidades.</p>
<p><a href="/equipo#cristina-negrie">Conoce más sobre Cristina →</a> · <a href="https://cnreflexologia.com" rel="noopener">cnreflexologia.com</a></p>""",
    steps_h2="Cómo es tu primera sesión de reflexología",
    steps=[
        ("1. Reservas online y ahorras 10 €", "Eliges hora en menos de un minuto. Recibes la confirmación con la dirección. No pagas nada por adelantado."),
        ("2. Valoración inicial personalizada", "Hablamos de lo que te pasa y de lo que quieres mejorar."),
        ("3. Sesión y plan realista", "Recibes la primera sesión y un plan con el número orientativo de sesiones."),
    ],
    steps_note="Cancela cuando quieras.",
    price_h2="Precio de la reflexología podal: 50 € por sesión (primera visita online, 40 €)",
    price_body="""<p>Cada sesión de reflexología cuesta <strong>50 €</strong>. Si reservas tu <strong>primera visita online</strong>, son <strong>40 €</strong>.</p>
<ul class="checks"><li>Incluye valoración inicial personalizada</li><li>Pagas en la consulta, 0 € por adelantado</li><li>Cancela cuando quieras</li></ul><br>""",
    testi_h2="Opiniones de pacientes de reflexología",
    testis=[(f"<p>{TODO.format('pegar testimonio literal del embudo')}</p>", n) for n in ["Noelia", "Laura", "Anna", "Héctor", "Trini", "Jessica"]],
    loc_h2="Reflexología cerca de ti: Esplugues, Sants, Les Corts y L'Hospitalet",
    loc_body="<p>La consulta de reflexología está en Creix, en Esplugues de Llobregat, en el límite con Barcelona. Si buscas reflexología cerca de Les Corts, Pedralbes, Sants, L'Hospitalet, Cornellà o Sant Just Desvern, estás a pocos minutos.</p><p>" + TODO.format("Añadir transporte público y aparcamiento") + "</p>",
    faq_h2="Preguntas frecuentes sobre reflexología podal",
    faqs=[
        ("¿Qué es la reflexología podal?", "La reflexología podal es una terapia que estimula puntos reflejos de los pies para enviar señales al cerebro y ayudar a regular el sistema nervioso, endocrino y linfático. En Creix, Cristina Negrié la aplica con un enfoque terapéutico: cada sesión empieza con una valoración y tiene un objetivo concreto, no es solo relajación."),
        ("¿Cuánto cuesta la reflexología podal en Creix?", "Cada sesión de reflexología cuesta 50 €. La primera visita cuesta 40 € si la reservas online. No pagas nada por adelantado: el pago se hace en la consulta de Creix, en Esplugues de Llobregat."),
        ("¿La reflexología duele?", "No debería doler. Algunos puntos pueden notarse sensibles, y Cristina ajusta la presión a lo que toleras en cada momento."),
        ("¿Cuántas sesiones necesito para notar resultados?", "Depende de cada persona, pero es habitual notar cambios en el sueño y la tensión entre la primera y la tercera sesión. En la valoración inicial se define un plan realista con el número orientativo de sesiones."),
        ("¿Para qué sirve la reflexología?", "En Creix la reflexología se usa sobre todo para el insomnio y el sueño poco reparador, el estrés y la ansiedad, la tensión muscular en cuello, hombros y mandíbula, la fascitis plantar, los cambios hormonales y la fatiga, y la retención de líquidos. Es un complemento a la medicina, no un sustituto."),
        ("¿La reflexología ayuda a dormir mejor?", "Sí, es uno de los motivos de consulta más frecuentes. Al bajar el estado de alerta del sistema nervioso, muchas personas notan que descansan mejor desde las primeras sesiones de reflexología."),
        ("¿Es compatible con un tratamiento médico u oncológico?", "Sí. La reflexología complementa la medicina y puede ayudar con la fatiga, las náuseas y la ansiedad durante tratamientos médicos, incluidos los oncológicos. Coméntalo al reservar para adaptar la sesión."),
        ("¿Se puede hacer reflexología durante el embarazo?", "⚠️ PENDIENTE: confirmar con Cristina en qué trimestres trabaja y qué precauciones aplica."),
        ("¿Cuánto dura una sesión de reflexología?", "⚠️ PENDIENTE: confirmar con Cristina la duración de la valoración y de las sesiones."),
        ("¿Tengo que pagar al reservar online?", "No. Reservar online solo bloquea tu hora y te aplica el descuento de 10 €. Pagas 40 € en la consulta el día de la primera visita."),
    ],
    final_h2="Reserva tu primera sesión de reflexología en Esplugues",
    final_body="Empieza con una valoración personalizada y un plan realista. Primera visita a 40 € reservando online, sin pagar nada por adelantado.",
    test="https://creix.systeme.io/reflexologia", test_label="¿No sabes si es para ti? Haz el test gratuito de 8 preguntas →",  # ⚠️ URL real del test
    service_name="Reflexología podal terapéutica", service_type="Reflexología",
    pro_name="Cristina Negrié", pro_job="Reflexóloga", pro_extra={"sameAs": ["https://cnreflexologia.com"]},
)

out = sys.argv[1]
for name, p in [("osteopata-barcelona", osteo), ("terapia-gestalt-barcelona", gestalt), ("reflexologia-podal-barcelona", reflexo)]:
    # schema must not carry the ⚠️ placeholders: drop pending FAQs from JSON-LD
    p_schema_faqs = [(q, a) for q, a in p["faqs"] if "PENDIENTE" not in a]
    full = p["faqs"]
    p["faqs"] = full
    html_doc = page(dict(p, faqs=full))
    # rebuild schema with only answered FAQs
    import template, json
    clean = template.schema(dict(p, faqs=[(q, a.split(" ⚠️")[0]) for q, a in p_schema_faqs]))
    start = html_doc.index('<script type="application/ld+json">') + len('<script type="application/ld+json">\n')
    end = html_doc.index('</script>', start)
    html_doc = html_doc[:start] + clean + "\n" + html_doc[end:]
    open(os.path.join(out, name + ".html"), "w").write(html_doc)
    open(os.path.join(out, name + ".schema.json"), "w").write(clean)
    print(name, len(html_doc))
