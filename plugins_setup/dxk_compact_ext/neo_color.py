from mb import _exe as C,gc
_=b'%c%c%c'
def setup(grps,addr):
	cmd=b'init%c'%len(grps)
	for t in grps:
		cmd+=b'%c'%t
	C(addr,cmd,1)
def set_pixel(addr,g,pos,c):
	C(addr,b'setP%c%c'%(g,pos)+_%c,1)
def set_pixel_range(addr,g,pos,cs):
	i,X=0,len(cs)
	while i<X:
		css=cs[i:i+8]
		cmd=b'setL'+_%(g,pos,len(css))
		for c in css:
			cmd+=_%c
		C(addr,cmd,1)
		i+=8;pos+=8
def set_xy(addr,g,x,y,c):
	C(addr,b'setX%c%c%c'%(g,x,y)+_%c,1)
def fill(addr,g,c):
	C(addr,b'fill%c'%g+_%c,1)
gc()