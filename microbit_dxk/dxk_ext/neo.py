from mb import command,slot,gc
_=lambda c:b'%c%c%c'%c
__=lambda x:x+128 if x<0 else x
def setup(groups,addr=None):
	addr=slot(addr,15)
	cmd=b'init%c'%len(groups)
	res=[]
	for i,t in enumerate(groups):
		cmd+=b'%c'%t
		res.append(Group(i,t,addr))
	command(addr,cmd)
	return res
class Group:
    def __init__(s,g,t,a):
        s.g=g
        s.t=t
        s.a=a
    def set_pixel(s,pos,c):
        command(s.a,b'setP%c%c'%(s.g,pos)+_(c))
    def set_pixel_range(s,pos,cs):
        cmd=b'setL%c%c%c'%(s.g,pos,len(cs))
        for c in cs:
            cmd+=_(c)
        command(s.a,cmd)
    def set_xy(s,x,y,c):
        if self.t!=2:return
        command(s.a,b'setX%c%c%c'%(s.g,x,y)+_(c))
    def fill(s,c):
        command(s.a,b'fill%c'%s.g+_(c))
    def set_image(s,img,x=None,y=None,m=0):
        if x==None:x=__(4-img.width()//2 if self.t==2 else 0)
        if y==None:y=__(4-img.height()//2)
        command(s.a,b'setI%c%c%c%c%s\x00'%(s.g,x,y,m,repr(img)))
    def set_image_RGB(s,imgs,x=None,y=None,m=0):
        if x==None:x=__(4-imgs[0].width()//2 if self.t==2 else 0)
        if y==None:y=__(4-imgs[0].height()//2)
        cmd=b'seIC%c%c%c%c'%(s.g,x,y,m)
        for i in imgs:
            cmd+=b'%s\x00'%repr(i)
        command(s.a,cmd)
    def shift(s,x,y=0):
        command(s.a,b'shft%c%c%c'%(s.g,__(x),__(y)))
    def set_rainbow(s,t,x,n):
        command(s.a,b'rnbl%c%c%c%c'%(s.g,t,x,n))
gc()