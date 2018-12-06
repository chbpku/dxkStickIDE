from mb import command as C,slot as S,gc
_=b'%c%c%c'
def setup(grps,addr=None):
	cmd=b'init%c'%len(grps)
	for t in grps:
		cmd+=b'%c'%t
	C(S(addr,15),cmd,1)
def set_image(g,img,x=None,y=None,m=0,addr=None):
	if x==None:
		x=4-img.width()//2
	if y==None:
		y=4-img.height()//2
	C(S(addr,15),b'setI%c%c%c%c%s\x00'%(g,x,y,m,repr(img)[7:-3]),1)
def set_image_RGB(g,imgs,x=None,y=None,m=0,addr=None):
	if x==None:
		x=4-imgs[0].width()//2
	if y==None:
		y=4-imgs[0].height()//2
	cmd=b'seIC%c'%g+_%(x,y,m)
	for i in imgs:
		cmd+=b'%s\x00'%(repr(i)[7:-3])
	C(S(addr,15),cmd,1)
def shift(g,x,y=0,addr=None):
	C(S(addr,15),b'shft'+_%(g,P(x),P(y)),1)
def set_rainbow(g,t,x,n,addr=None):
	C(S(addr,15),b'rnbl%c%c%c%c '%(g,t,x,n),1)
gc()