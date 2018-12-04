from mb import command as C,slot as S,gc
_=b'%c%c%c'
def setup(grps,addr=None):
	cmd=b'init%c'%len(grps)
	for t in grps:
		cmd+=b'%c'%t
	C(S(addr,15),cmd,1)
def set_pixel(g,pos,c,addr=None):
	C(S(addr,15),b'setP%c%c'%(g,pos)+_%c,1)
def set_pixel_range(g,pos,cs,addr=None):
	cmd=b'setL'+_%(g,pos,len(cs))
	for c in cs:
		cmd+=_%c
	C(S(addr,15),cmd,1)
def set_xy(g,x,y,c,addr=None):
	if self.t!=2:return
	C(S(addr,15),b'setX%c%c%c'%(g,x,y)+_%c,1)
def fill(g,c,addr=None):
	C(S(addr,15),b'fill%c'%g+_%c,1)
gc()