import re, json, sys, glob, os
src = sys.argv[1]
out = {}
for f in glob.glob(src + "/*.txt"):
    k = os.path.basename(f)[:-4]
    t = open(f).read().split("==IMGS==")[0]
    t = t.split("\nEspañol\n", 1)[-1]
    t = t.split("\nCreix\n\nespai de salut")[0]
    lines = [re.sub(r"\s+", " ", l.replace("​", "")).strip() for l in t.split("\n")]
    lines = [l for l in lines if l]
    paras = []
    for l in lines:
        if re.search(r"@|Tel\.|^\d{3} ?\d|^Quiero probar|^¡PIDE|^Reserva|^EMAIL|^WHATSAPP|^Instagram|www\.", l): continue
        if len(l.split()) < 6 and not l.startswith(("•", "-", "⪢")): continue
        paras.append(l)
    out[k] = paras
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
for k, v in out.items(): print(k, len(v), sum(len(x.split()) for x in v))
