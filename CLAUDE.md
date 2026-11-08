# Web de Creix Salut: normes per a Claude

Aquest repositori genera creixsalut.com amb Python (sense dependències). Les peticions de canvi arriben
dels clients (Creix) i les revisa en Jaume abans de publicar.

## Què pots tocar
- `data.py`: contingut (teràpies, equip, agenda, blog, espais, preus, horaris).
- `svc.json`: textos de les pàgines de teràpies secundàries.
- Textos dins de `build.py` i `pages.py` quan el contingut només viu allà.

## Què NO pots tocar sense que en Jaume ho demani explícitament
- El CSS, la capçalera, el peu i l'estructura de `template.py` (disseny).
- `netlify.toml`, `.github/` i aquest fitxer.
- Crear o esborrar pàgines.

## Estil de marca
- Només el botó principal (CTA) és taronja #FB7704. Títols Poppins, cos Heebo Light.
- Textos en castellà, to proper i professional. No inventis preus, horaris, telèfons ni titulacions:
  si la petició no ho diu, pregunta-ho al comentari.

## Abans d'acabar
1. `mkdir -p public && python3 build.py public && python3 pages.py public` ha de funcionar sense errors.
2. Comprova que la pàgina canviada conté el text nou.
3. Explica el canvi en una o dues frases senzilles, sense termes tècnics (el client no és programador).
