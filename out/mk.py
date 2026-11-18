from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920; X,Y,w,h=108,190,864,1536; R=48
B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
import glob; heb=(glob.glob("/usr/share/fonts/**/FreeSansBold.ttf",recursive=True) or [B])[0]
bg=Image.new("RGBA",(W,H),(18,6,34,255))
g=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(g)
d.rounded_rectangle((X-6,Y-6,X+w+6,Y+h+6),R+6,outline=(170,80,255,255),width=14)
g=g.filter(ImageFilter.GaussianBlur(18)); bg=Image.alpha_composite(bg,g)
d=ImageDraw.Draw(bg)
d.rounded_rectangle((X-4,Y-4,X+w+4,Y+h+4),R+4,outline=(200,140,255,255),width=5)
m=Image.new("L",(W,H),255); ImageDraw.Draw(m).rounded_rectangle((X,Y,X+w,Y+h),R,fill=0)
bg.putalpha(Image.composite(bg.getchannel("A"),m,m))
def glowtext(img,xy,t,f,col):
    l=Image.new("RGBA",img.size,(0,0,0,0)); ImageDraw.Draw(l).text(xy,t,font=f,fill=col,anchor="mm",direction="rtl" if any('֐'<=c<='׿' for c in t) else None)
    gl=l.filter(ImageFilter.GaussianBlur(14)); img.alpha_composite(gl); img.alpha_composite(gl); img.alpha_composite(l)
glowtext(bg,(W//2,100),"⚡ SPARK",ImageFont.truetype(B,96),(235,210,255,255))
glowtext(bg,(W//2,1820),"סרטון דוגמה ל-Or-Digital",ImageFont.truetype(heb,70),(255,255,255,255))
bg.save("frame.png")
wm=Image.new("RGBA",(W,H),(0,0,0,0)); t=Image.new("RGBA",(1400,400),(0,0,0,0))
ImageDraw.Draw(t).text((700,200),"SPARK",font=ImageFont.truetype(B,260),fill=(255,255,255,110),anchor="mm",stroke_width=4,stroke_fill=(150,60,255,110))
t=t.rotate(30,expand=True); wm.alpha_composite(t,((W-t.width)//2,(H-t.height)//2)); wm.save("wm.png")

# --- logo version ---
import numpy as np
L=Image.open("spark_logo.png").convert("RGB"); a=np.asarray(L).astype(float)
al=np.clip((a.max(2)-20)*4,0,255).astype(np.uint8)
logo=L.convert("RGBA"); logo.putalpha(Image.fromarray(al)); logo=logo.crop(logo.getbbox())
fr=Image.open("frame.png"); ImageDraw.Draw(fr).rectangle((0,0,W,185),fill=(18,6,34,255))
s=logo.resize((130,int(130*logo.height/logo.width)))
f=ImageFont.truetype(B,96); tw=ImageDraw.Draw(fr).textlength("SPARK",font=f); x0=int((W-(130+30+tw))/2)
fr.alpha_composite(s,(x0,100-s.height//2))
glowtext(fr,(int(x0+160+tw/2),100),"SPARK",f,(235,210,255,255)); fr.save("frame.png")
wm=Image.new("RGBA",(W,H),(0,0,0,0)); s=logo.resize((620,int(620*logo.height/logo.width)))
s.putalpha(s.getchannel("A").point(lambda v:v*0.4)); wm.alpha_composite(s,((W-s.width)//2,(H-s.height)//2-60))
t=Image.new("RGBA",(W,300),(0,0,0,0)); ImageDraw.Draw(t).text((W//2,150),"SPARK",font=ImageFont.truetype(B,190),fill=(255,255,255,100),anchor="mm",stroke_width=4,stroke_fill=(150,60,255,100))
wm.alpha_composite(t,(0,(H+s.height)//2-110)); wm.save("wm.png")
