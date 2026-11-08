import sys,os,glob,re
from PIL import Image
d=sys.argv[1]; ren={}
for f in glob.glob(d+"/img/*"):
    im=Image.open(f)
    if im.mode in("RGBA","LA","P"):
        im=im.convert("RGBA"); bg=Image.new("RGB",im.size,(241,242,236)); bg.paste(im,mask=im.split()[-1]); im=bg
    else: im=im.convert("RGB")
    im.thumbnail((1400,1400))
    n=f.rsplit(".",1)[0]+".jpg"; im.save(n,"JPEG",quality=80,optimize=True,progressive=True)
    if n!=f: os.remove(f); ren[os.path.basename(f)]=os.path.basename(n)
for h in glob.glob(d+"/*.html"):
    t=open(h).read()
    for a,b in ren.items(): t=t.replace("img/"+a,"img/"+b)
    open(h,"w").write(t)
