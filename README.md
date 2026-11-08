# Generador web Creix

Python 3 (sense dependències, excepte Pillow per a shrink.py).

- `data.py`: contingut (teràpies, equip, agenda, blog, espais). `svc.json`: textos extrets de la web actual per a les pàgines secundàries.
- `template.py`: CSS, capçalera/peu comuns i plantilla de les 3 pàgines principals (osteo, Gestalt, reflexo).
- `build.py`: dades i build de les 3 pàgines principals (+ .schema.json).
- `pages.py`: home, hubs i 13 pàgines de teràpia secundàries.

Build de producció (imatges remotes a static.wixstatic.com, enllaços absoluts):
    python3 build.py out && python3 pages.py out

Previsualització local (descarrega imatges i fonts, enllaços relatius):
    python3 localize.py out preview && python3 shrink.py preview

`extract.py` regenera svc.json a partir de dumps de text de la web actual (no cal per al build).
`preview-assets/` conté les imatges i fonts ja descarregades i optimitzades (noms = md5 de la URL).
Les imatges en producció es carreguen des de static.wixstatic.com: si es deixa Wix, cal descarregar-les i servir-les des del repo.

## Publicació (Netlify)
Netlify executa el build de `netlify.toml` i publica la carpeta `public/`. Cada pull request té la seva URL de prova (Deploy Preview).

## Canvis per conversa
Obre una issue amb la petició en llenguatge normal. La GitHub Action de Claude (`.github/workflows/claude.yml`) fa el canvi en una branca i obre una pull request. Per demanar retocs, comenta a la pull request començant amb `@claude`. Cal el secret `ANTHROPIC_API_KEY` al repositori.
