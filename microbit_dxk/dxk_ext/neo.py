from mb import command as C,slot as S,gc
_=b'%c%c%c'
P=lambda x:x+128 if x<0 else x
def setup(grps,addr=None):
	addr=S(addr,15)
	cmd=b'init%c'%len(grps)
	res=[]
	for i,t in enumerate(grps):
		cmd+=b'%c'%t
		res.append(G(i,t,addr))
	C(addr,cmd,1)
	return res
class G:
	def __init__(s,g,t,a):
		s.g=g;s.t=t;s.a=a
	def set_pixel(s,pos,c):
		C(S(s.a,15),b'setP%c%c'%(s.g,pos)+_%c,1)
	def set_pixel_range(s,pos,cs):
		cmd=b'setL'+_%(s.g,pos,len(cs))
		for c in cs:
			cmd+=_%c
		C(S(s.a,15),cmd,1)
	def set_xy(s,x,y,c):
		if self.t!=2:return
		C(S(s.a,15),b'setX%c%c%c'%(s.g,x,y)+_%c,1)
	def fill(s,c):
		C(S(s.a,15),b'fill%c'%s.g+_%c,1)
	def set_image(s,img,x=None,y=None,m=0):
		if x==None:
			x=P(4-img.width()//2)
			y=P(4-img.height()//2)
		C(S(s.a,15),b'setI%c%c%c%c%s\x00'%(s.g,x,y,m,repr(img)[7:-3]),1)
	def set_image_RGB(s,imgs,x=None,y=None,m=0):
		if x==None:
			x=P(4-imgs[0].width()//2)
			y=P(4-imgs[0].height()//2)
		cmd=b'seIC%c'%s.g+_%(x,y,m)
		for i in imgs:
			cmd+=b'%s\x00'%(repr(i)[7:-3])
		C(S(s.a,15),cmd,1)
	def shift(s,x,y=0):
		C(S(s.a,15),b'shft'+_%(s.g,P(x),P(y)),1)
	def set_rainbow(s,t,x,n):
		C(S(s.a,15),b'rnbl%c%c%c%c'%(s.g,t,x,n),1)
gc()