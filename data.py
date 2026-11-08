"""Site-wide data: therapies, team, activities, blog."""
from template import wix

TODO = '<span class="todo">⚠️ {}</span>'
WA_T = "https://wa.me/34613613356?text="

# category keys
CATS = [
    ("cuerpo", "Cuerpo y dolor", "Terapias manuales y de salud física para el dolor, la tensión, la digestión y la energía."),
    ("mente", "Mente y emociones", "Acompañamiento psicológico y emocional para la ansiedad, las relaciones, los bloqueos y los momentos de cambio."),
    ("movimiento", "Movimiento y grupos", "Clases semanales y círculos para moverte, respirar y compartir en grupo."),
]

# key, name, slug, cat, pro key, card image, short description, source page (for body text), current URL
THERAPIES = [
    ("osteo", "Osteopatía", "/osteopata-barcelona", "cuerpo", "sergi", wix("4bcc8b_624e233a39bb4de8b2c8b7731c5d5a1d~mv2.jpeg", 800, 600),
     "Dolor de espalda, cervicales, migrañas y lesiones, con un enfoque integrativo que busca la causa.", None, "/osteopatia-esplugues"),
    ("reflexo", "Reflexología podal y drenaje linfático", "/reflexologia-podal-barcelona", "cuerpo", "cristina", wix("4bcc8b_4edf2fb4913c45e98656cf5b3a8ccaac~mv2.png", 800, 600),
     "Reflexología terapéutica para el estrés, el insomnio, el dolor y la retención de líquidos.", None, "/reflexologia-drenatge"),
    ("dieta", "Dietética y nutrición", "/dietista-esplugues", "cuerpo", "laura", wix("4bcc8b_780bd33d87d7430ea137c3592f4f5ad4~mv2.png", 800, 600),
     "Hábitos, peso, digestión y energía, sin dietas imposibles y adaptado a tu ritmo de vida.", "nutricio", "/nutricio"),
    ("pni", "PNI (psiconeuroinmunología)", "/pni-esplugues", "cuerpo", "laura", wix("4bcc8b_a68b50dc8ea447fea87ddd9428a93ae7~mv2.jpeg", 800, 600),
     "Alimentación, suplementación, ejercicio y gestión del estrés para entender el origen de la enfermedad.", "pni", "/pni"),
    ("acu", "Acupuntura y medicina china", "/acupuntura-esplugues", "cuerpo", "aurelie", wix("4bcc8b_c1bf23a73027497e8a64b4a31a0a3564~mv2.png", 800, 600),
     "Medicina tradicional china, acupuntura y fitoterapia para recuperar el equilibrio.", "acupuntura", "/acupuntura"),
    ("masaje", "Masaje integrativo sensitivo", "/masaje-integrativo-esplugues", "cuerpo", "olga", wix("d90004_3faf631ed871432b96cd9cb10ddce306~mv2.jpg", 800, 600),
     "Un masaje circulatorio, correctivo y energético para descargar tensión física y mental.", "massatge-integratiu", "/massatge-integratiu"),
    ("gestalt", "Terapia Gestalt", "/terapia-gestalt-barcelona", "mente", "nathalie", wix("4bcc8b_da2c8f0ef26348c9b94841fc01e3df6f~mv2.jpg", 800, 600),
     "Para salir del bucle mental, gestionar emociones y aprender a poner límites, integrando el cuerpo.", None, "/terapia-gestalt"),
    ("psico", "Psicoterapia", "/psicologa-esplugues", "mente", "sandra", wix("4bcc8b_47e0f33f09634013adcb55fc8928efea~mv2.png", 800, 600),
     "Psicoterapia corporal y transpersonal con una psicóloga colegiada especializada en trauma.", "psicologia", "/psicologia"),
    ("sexo", "Sexualidad consciente y bioenergética", "/sexualidad-consciente-bioenergetica", "mente", "sandra", wix("4bcc8b_2511289d57924f80b57e0d8e4364d52c~mv2.png", 800, 600),
     "Liberar bloqueos y sanar heridas relacionadas con la sexualidad, el placer y la intimidad.", "sexualitat-bioenergetica", "/sexualitat-bioenergetica"),
    ("chaman", "Chamanismo y terapia energética", "/chamanismo-terapia-energetica", "mente", "sandra", wix("4bcc8b_c2d6498e37924f79a3120550ee52fd6b~mv2.png", 800, 600),
     "Psicoterapia integrativa unida a la sabiduría ancestral, en los niveles consciente e inconsciente.", "xamanisme-esplugues", "/xamanisme-esplugues"),
    ("conste", "Constelaciones familiares", "/constelaciones-familiares-esplugues", "mente", "transi", wix("4bcc8b_a09ca7d7ecb84cb482b2cfc4c8a2aa22~mv2.png", 800, 600),
     "Sesiones individuales y talleres grupales para ordenar y sanar el sistema familiar.", "constellacions-familiars", "/constellacions-familiars"),
    ("coach", "Coaching psicocorporal", "/coaching-psicocorporal-esplugues", "mente", "olga", wix("11062b_dcbf357354c245eebaf86551a299974d~mv2.jpg", 800, 600),
     "Para procesos de cambio y decisiones importantes, trabajando cuerpo, mente, emoción y energía.", "coaching-psicocorporal", "/coaching-psicocorporal"),
    ("mint", "Movimiento Integral (reeducación postural)", "/movimiento-integral-esplugues", "movimiento", "lourdes", wix("11062b_bb3f671034ee40f7979218a8488c7dc7~mv2.jpg", 800, 600),
     "Reeducación postural en grupos pequeños o sesiones individuales, basada en las cadenas musculares.", "moviment-integral", "/moviment-integral"),
    ("mexp", "Movimiento Expresivo Río Abierto", "/movimiento-expresivo-esplugues", "movimiento", None, wix("11062b_724ab217c3854c38b84abf78187efdc8~mv2.jpg", 800, 600),
     "Danza consciente para soltar tensiones y reconectar con el cuerpo. No hace falta experiencia.", "moviment-expressiu", "/moviment-expressiu"),
    ("yoga", "Hatha yoga y meditación", "/yoga-esplugues", "movimiento", "gijilla", wix("d90004_5763fd339fc64cd5ae292241dae7e116~mv2.png", 800, 600),
     "Posturas, respiración y escucha consciente del cuerpo, respetando tus límites.", "yoga-meditacio", "/yoga-meditacio"),
    ("circulo", "Círculo de mujeres", "/circulo-de-mujeres-esplugues", "movimiento", "eli", wix("11062b_ef1082a875224e2eb2aace5f05c0256d~mv2.jpg", 800, 600),
     "Un viernes al mes, un espacio para el autoconocimiento, la autoestima y la fuerza personal.", "cercle-de-dones", "/cercle-de-dones"),
]
T = {t[0]: t for t in THERAPIES}

# key, name, role, credential line, photo, therapies, contact
TEAM = {
    "sergi": ("Sergi Català", "Osteópata DO", "Colegiado nº 143 · Naturopatía, PNIE y medicina ortomolecular · Más de 15 años en Creix",
              wix("4bcc8b_f627c5e455a3494a84a742f7b6d5bb91~mv2.jpg", 600, 600), ["osteo"], "613 61 33 56"),
    "nathalie": ("Nathalie López", "Terapeuta Gestalt", "Terapia Gestalt con enfoque somático: cuerpo y movimiento",
                 wix("4bcc8b_c282d03d7c2d48ec9416aa3a6c8ba412~mv2.jpg", 600, 600), ["gestalt"], "639 137 472"),
    "cristina": ("Cristina Negrié", "Reflexóloga", "Más de 10 años de experiencia · Reflexología y drenaje linfático",
                 wix("4bcc8b_0fb25c7f9cc442b4a2e5a3258629dc21~mv2.jpg", 600, 600), ["reflexo"], "613 61 33 56"),
    "laura": ("Laura Sitjes", "Dietista integrativa y kinesióloga", "Naturópata y coach nutricional · Más de 15 años de experiencia · PNI",
              wix("4bcc8b_df3098390f6540e1972ccc54a6a4279a~mv2.jpg", 600, 600), ["dieta", "pni"], "613 61 33 56"),
    "sandra": ("Sandra Fernández Ochoa", "Psicóloga", "Psicóloga col. nº 20527 · Más de 25 años de trayectoria · Trauma y sexualidad consciente",
               wix("4bcc8b_8b7155816f4b4d80aa467f2e77672e71~mv2.jpg", 600, 600), ["psico", "sexo", "chaman"], "660 92 97 89"),
    "aurelie": ("Aurelie Cabanat", "Medicina tradicional china", "Acupuntura, fitoterapia y nutrición ortomolecular",
                wix("d90004_8a29cce7163b4c9ea967e9f58c96cbf8~mv2.jpg", 600, 600), ["acu"], "613 61 33 56"),
    "olga": ("Olga Guerrero", "Coach psicocorporal", "Coaching integrativo y masaje integrativo sensitivo",
             wix("4bcc8b_be7fafb6b83d4c6990c4ae7efb198344~mv2.jpg", 600, 600), ["coach", "masaje"], "613 61 33 56"),
    "transi": ("Transi Alma", "Constelaciones familiares", "Máster en Constelaciones Familiares con Joan Garriga",
               wix("5ce116_801edaa0c12e4131be8bb239bb06f1c6~mv2.jpg", 600, 600), ["conste"], "646 000 643"),
    "lourdes": ("Lourdes Martí", "Movimiento Integral", "Facilitadora de Movimiento Integral desde hace 20 años",
                wix("4bcc8b_9b8c1a5a500e402088e2282f5893ebcd~mv2.jpeg", 600, 600), ["mint"], "613 61 33 56"),
    "gijilla": ("Gijilla Labastie", "Profesora de hatha yoga", "Hatha yoga y meditación",
                wix("d90004_5763fd339fc64cd5ae292241dae7e116~mv2.png", 600, 600), ["yoga"], "613 61 33 56"),
    "eli": ("Elisabet Sánchez", "Facilitadora de círculos de mujeres", "Pedagoga y coach transpersonal · Guía de yoga nidra",
            wix("d90004_d48513a7dabb471a891da3d5c8c09a35~mv2.jpeg", 600, 600), ["circulo"], "613 61 33 56"),
}

# secondary therapy page copy: h1, title, meta, lead (my SEO intro), schedule/practical line
SECONDARY = {
    "dieta": ("Dietista en Esplugues de Llobregat: nutrición integrativa", "Dietista y nutricionista en Esplugues | Creix",
              "Dietética y nutrición integrativa con Laura Sitjes en Esplugues de Llobregat: hábitos, peso, digestión y energía. Más de 15 años de experiencia.",
              "Si quieres mejorar tu alimentación, recuperar energía o encontrar tu peso sin dietas imposibles, Laura Sitjes te acompaña con un enfoque integrativo que tiene en cuenta tus hábitos y tus emociones."),
    "pni": ("PNI en Esplugues de Llobregat", "PNI (psiconeuroinmunología) en Esplugues | Creix",
            "Consulta de PNI en Esplugues de Llobregat con Laura Sitjes: alimentación, suplementación, ejercicio y gestión del estrés para tratar el origen.",
            "La PNI estudia cómo se relacionan el sistema nervioso, el digestivo, el inmunitario, el hormonal y el psicológico. En consulta buscamos el camino que te ha llevado al problema para poder deshacerlo."),
    "acu": ("Acupuntura en Esplugues de Llobregat", "Acupuntura y medicina china en Esplugues | Creix",
            "Acupuntura, medicina tradicional china y fitoterapia con Aurelie Cabanat en Creix, Esplugues de Llobregat, junto a Barcelona.",
            "La medicina tradicional china es uno de los enfoques holísticos más antiguos. Aurelie Cabanat combina acupuntura, fitoterapia y hábitos de vida para ayudarte a recuperar el equilibrio."),
    "masaje": ("Masaje integrativo sensitivo en Esplugues", "Masaje integrativo sensitivo en Esplugues | Creix",
               "Masaje integrativo sensitivo con Olga Guerrero en Esplugues de Llobregat: descarga el estrés, alivia el dolor y calma el sistema nervioso.",
               "Si notas el cuerpo cargado, la mente acelerada y poca energía, este masaje circulatorio, correctivo y energético te ayuda a soltar tensión y a descansar de verdad."),
    "psico": ("Psicóloga en Esplugues: psicoterapia corporal y transpersonal", "Psicóloga en Esplugues de Llobregat | Creix",
              "Psicoterapia con Sandra Fernández Ochoa, psicóloga col. nº 20527, en Esplugues de Llobregat. Trauma, bioenergética y enfoque transpersonal.",
              "Sandra Fernández Ochoa es psicóloga colegiada con más de 25 años de trayectoria. Su psicoterapia integra el cuerpo, la bioenergética y el trabajo con el trauma."),
    "sexo": ("Sexualidad consciente y bioenergética en Esplugues", "Sexualidad consciente y bioenergética | Creix Esplugues",
             "Terapia de sexualidad consciente y bioenergética con la psicóloga Sandra Fernández Ochoa en Esplugues de Llobregat.",
             "Un espacio terapéutico para liberar bloqueos del cuerpo, sanar heridas relacionadas con la sexualidad y la intimidad, y reconectar con tu energía vital."),
    "chaman": ("Chamanismo y terapia energética en Esplugues", "Chamanismo y terapia energética en Esplugues | Creix",
               "Psicoterapia y chamanismo con Sandra Fernández Ochoa, psicóloga col. nº 20527, en Esplugues de Llobregat.",
               "Un enfoque que une la psicoterapia contemporánea con la sabiduría ancestral para trabajar los niveles consciente e inconsciente, el cuerpo, la mente y el alma."),
    "conste": ("Constelaciones familiares en Esplugues de Llobregat", "Constelaciones familiares en Esplugues y Barcelona | Creix",
               "Constelaciones familiares con Transi Alma en Esplugues: sesiones individuales y talleres grupales mensuales. Constelar 80 €, participar con aportación voluntaria.",
               "Las constelaciones familiares ayudan a mirar el sistema familiar desde fuera y a ordenar lo que pesa. En Creix puedes hacerlas en sesión individual o en los talleres grupales de Transi Alma."),
    "coach": ("Coaching psicocorporal en Esplugues", "Coaching psicocorporal en Esplugues | Creix",
              "Coaching integrativo y psicocorporal con Olga Guerrero en Esplugues de Llobregat para procesos de cambio, decisiones y objetivos.",
              "Si estás en un momento de cambio o necesitas tomar decisiones, el coaching psicocorporal te ayuda a aclararte trabajando cuerpo, mente, emoción y energía."),
    "mint": ("Movimiento Integral: reeducación postural en Esplugues", "Reeducación postural (Movimiento Integral) en Esplugues | Creix",
             "Clases de Movimiento Integral con Lourdes Martí en Esplugues: reeducación postural en grupos pequeños, jueves 13:00 y 16:00.",
             "Un método de reeducación postural basado en las cadenas musculares de Mézières. Grupos pequeños, sesiones adaptadas a cada persona y la opción de sesiones individuales."),
    "mexp": ("Movimiento Expresivo Río Abierto en Esplugues", "Movimiento Expresivo Río Abierto en Esplugues | Creix",
             "Sesiones semanales de Movimiento Expresivo Río Abierto en Esplugues, los miércoles a las 18:00. Danza consciente sin experiencia previa.",
             "Danza consciente para disfrutar, soltar tensiones y flexibilizar el cuerpo, fluyendo con las emociones. No necesitas experiencia previa."),
    "yoga": ("Hatha yoga y meditación en Esplugues", "Clases de hatha yoga y meditación en Esplugues | Creix",
             "Clases de hatha yoga y meditación en Creix, Esplugues de Llobregat: posturas, respiración y escucha consciente del cuerpo.",
             "Un yoga de fuerza y escucha: posturas lentas, respiración y atención al cuerpo, respetando tus límites sin quedarte en la zona de confort."),
    "circulo": ("Círculo de mujeres en Esplugues", "Círculo de mujeres en Esplugues y Barcelona | Creix",
                "Círculo de mujeres mensual en Creix, Esplugues de Llobregat, con Elisabet Sánchez: autoconocimiento, autoestima y fuerza personal.",
                "Un viernes al mes nos encontramos para compartir, sin juicio y sin prisa. Un espacio para el autoconocimiento, la autoestima y la fuerza personal."),
}

SCHEDULE = [
    ("Lunes", []),
    ("Martes", [("19:30", "Danza Útera", None)]),
    ("Miércoles", [("09:30", "Mindful Vinyasa Yoga", "/yoga-esplugues"), ("18:00", "Movimiento Expresivo Río Abierto", "/movimiento-expresivo-esplugues"), ("19:30", "Mindful Vinyasa Yoga", "/yoga-esplugues")]),
    ("Jueves", [("13:00–14:30", "Movimiento Integral", "/movimiento-integral-esplugues"), ("16:00–17:30", "Movimiento Integral", "/movimiento-integral-esplugues")]),
    ("Viernes", [("18:30–20:00", "Mindfulness", None)]),
]

GROUPS = [
    ("Constelaciones familiares en grupo", "Con Transi Alma", "Talleres grupales: constelar 80 €, participar con aportación voluntaria.", wix("d90004_4617187fab1045eca48bb0781044a121~mv2.png", 800, 600), "/constelaciones-familiares-esplugues"),
    ("Grupo PAS (alta sensibilidad)", "Un jueves al mes, de 18 a 20 h", "Un espacio mensual para compartir experiencias y descubrir la fortaleza de la alta sensibilidad. Próximas fechas: 19 de noviembre, 10 de diciembre, 21 de enero, 18 de febrero, 18 de marzo, 15 de abril, 20 de mayo y 17 de junio.", wix("4bcc8b_bdd4a2027e0e4a979501a422560eb7c7~mv2.jpg", 800, 600), None),
    ("Círculo de mujeres", "Un viernes al mes", "Autoconocimiento, autoestima y fuerza personal en grupo, con Elisabet Sánchez.", wix("d90004_d48513a7dabb471a891da3d5c8c09a35~mv2.jpeg", 800, 600), "/circulo-de-mujeres-esplugues"),
    ("El viaje de la manzana entera", "Taller de octubre a diciembre", "Proceso de 3 meses para dejar de vivir el amor desde la ansiedad, con danza, visualizaciones y arteterapia.", wix("11062b_ef1082a875224e2eb2aace5f05c0256d~mv2.jpg", 800, 600), "https://despertant.cat/la-manzana-entera/"),
]

BLOG = [
    ("Primera visita al osteópata: qué esperar y qué preguntar", "/post/primera-visita-al-osteópata-qué-esperar-y-qué-preguntar", "Osteopatía", "10 sept", 4,
     "Cómo es la valoración, si hay que llevar pruebas médicas, si el tratamiento duele y cuántas sesiones harán falta.", wix("8ca5b9_797881ebe15545e7aa6300b2121b22b4~mv2.jpg", 800, 520)),
    ("Aprender a poner límites sin sentirte culpable", "/post/aprender-a-poner-límites-sin-sentirte-culpable", "Terapia Gestalt", "10 sept", 4,
     "Por qué nos cuesta decir que no y cómo expresar tus necesidades con respeto, aunque la culpa no desaparezca de golpe.", wix("8ca5b9_424a24bf00954116ad78f9304c14bb3c~mv2.jpg", 800, 520)),
    ("Respirar mejor, vivir mejor: el interruptor que siempre llevas contigo", "/post/respirar-mejor-vivir-mejor-el-interruptor-que-siempre-llevas-contigo", "Bienestar", "10 jul", 3,
     "La respiración es el único proceso automático del sistema nervioso que puedes controlar cuando quieras.", wix("8ca5b9_2b9855f679f7415699b56c18bb869a48~mv2.jpg", 800, 520)),
    ("Llega el verano: tu cuerpo recoge lo que has sembrado en primavera", "/post/llega-el-verano-tu-cuerpo-recoge-lo-que-has-sembrado-en-primavera", "Nutrición", "1 jun", 2,
     "Alergias, cansancio e inflamación: lo que notas ahora depende de cómo has cuidado tus hábitos estos meses.", wix("8ca5b9_7fea69aa67844615b3d898ff93fbf516~mv2.jpg", 800, 520)),
]

TESTIS = [
    ("Un ambiente muy acogedor y el trato del personal inmejorable. Sergi, el terapeuta muy cercano, súper profesional y amable. ¡Repetiremos!", "Mar"),
    ("Es maravilloso ver cómo la historia personal de una conecta con la de otra, cómo los miedos que tenemos arraigados se comprenden mejor desde la perspectiva de otra compañera.", "Noemie · Círculo de mujeres"),
    ("Acudí por un pinzamiento en el manguito rotador del hombro. El dolor era constante, ninguna medicina me aliviaba. En tres sesiones logró que volviera a tener una vida normal.", "Capi L. · Reseña en Google"),
]

SPACES = [
    (wix("d90004_7457b69329bf44e2b5e9c9daba2db938~mv2.jpg", 900, 1200), "Fachada de Creix en Esplugues de Llobregat"),
    (wix("d90004_3682c22b65654c5a854975f3c06b4a0f~mv2.jpg", 800, 600), "Escaleras de entrada al centro"),
    (wix("d90004_3faf631ed871432b96cd9cb10ddce306~mv2.jpg", 800, 600), "Consulta con camilla"),
    (wix("d90004_51d42e55ba984cc7b83a34702afe09b6~mv2.jpg", 800, 600), "Despacho de consulta"),
    (wix("d90004_3835f3da659e4bd5b4f2b5ad9db0646a~mv2.jpg", 800, 600), "Sala de actividades"),
    (wix("d90004_2970df4b5ac849ad9775ed3fa75a397b~mv2.jpg", 800, 600), "Sala polivalente"),
    (wix("d90004_3ecaad45a83248c8ad2aea0b1aebc03d~mv2.jpg", 800, 600), "Despacho luminoso"),
    (wix("4bcc8b_c63344b66665423bb00760f24a3c6294~mv2.png", 800, 600), "Pasillo con plantas"),
]
