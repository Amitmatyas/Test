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
