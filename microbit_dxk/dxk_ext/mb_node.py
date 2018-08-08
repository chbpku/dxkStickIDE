from mb_radio import r_eval
from microbit import *
def show(img,grp=-1):
  try:
    Image(img)
    r_eval(b"display.show(Image(%r))"%img,grp)
    return
  except:pass
  r_eval(b"display.show(Image.%s)"%img,grp)
def scroll(text,grp=-1):
  r_eval(b"display.scroll(%r)"%text,grp)
def button(btn,grp=-1):
  res=[]
  try:
    for i in r_eval(b"button_%s.get_presses()"%btn.lower(),grp):
      res.append(i)
  except:pass
  return res
def play(mid,grp=-1):
  r_eval(b"music.play(music.%s)"%mid,grp)