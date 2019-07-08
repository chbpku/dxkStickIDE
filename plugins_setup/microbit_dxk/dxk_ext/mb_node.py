from mb_radio import r_eval
from microbit import *
_res=[]
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
	_res.clear()
	for i,g in r_eval(b"button_%s.get_presses()"%btn.lower(),grp):
		_res.append((int(i),g))
	return tuple(_res)
def play(mid,wait=0,grp=-1):
	r_eval(b"music.play(music.%s,wait=%d)"%(mid,wait),grp)