from mb_radio import r_eval,channel,group
from microbit import *
def show(img,grp=-1):
  try:
    Image(img)
    r_eval(b"display.show(Image(%r))"%img,grp)
    return
  except:pass
  r_eval(b"display.show(Image.%s)"%img,grp)
def scroll(text,wait=0,grp=-1):
  r_eval(b"display.scroll(%r,wait=%d)"%(text,wait),grp)
def button(btn,grp=-1):
  res=[]
  for i,g in r_eval(b"button_%s.get_presses()"%btn.lower(),grp):
    res.append((int(i),g))
  return res
def play(mid,wait=0,grp=-1):
  r_eval(b"music.play(music.%s,wait=%d)"%(mid,wait),grp)