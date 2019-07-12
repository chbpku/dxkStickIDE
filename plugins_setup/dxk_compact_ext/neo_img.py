from mb import _exe as C,gc
_=b'%c%c%c'
def setup(grps,addr):
	cmd=b'init%c'%len(grps)
	for t in grps:
		cmd+=b'%c'%t
	C(addr,cmd,1)
def set_image(addr,g,img,x=None,y=None,m=0):
	if x==None:
		x=4-img.width()//2
	if y==None:
		y=4-img.height()//2
	C(addr,b'setI%c%c%c%c%s\x00'%(g,x,y,m,repr(img)[7:-3]),1)
def set_image_RGB(addr,g,imgs,x=None,y=None,m=0):
	if x==None:
		x=4-imgs[0].width()//2
	if y==None:
		y=4-imgs[0].height()//2
	cmd=b'seIC%c'%g+_%(x,y,m)
	for i in imgs:
		cmd+=b'%s\x00'%(repr(i)[7:-3])
	C(addr,cmd,1)
def shift(addr,g,x,y=0):
	C(addr,b'shft'+_%(g,P(x),P(y)),1)
def set_rainbow(addr,g,t,x,n):
	C(addr,b'rnbl%c%c%c%c '%(g,t,x,n),1)
gc()