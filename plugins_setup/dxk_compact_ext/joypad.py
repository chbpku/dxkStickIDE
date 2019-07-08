from mb import _exe,gc
def conv(data):
	x,y=data[5]*256+data[6],data[7]*256+data[8]
	x=x-2048;y=2048-y
	return tuple(data[:5]),(x,y)
def values(addr):
	data=_exe(addr,b'get_key_val',9,True)
	try:
		return conv(data)
	except:
		return None,None
def keys(addr):
	return values(addr)[0]
def stickxy(addr):
	return values(addr)[1]
def stick_directions(addr):
	tmp=values(addr)[1]
	if tmp==None:return
	xd=1 if tmp[0]>1000 else -1 if tmp[0]<-1000 else 0
	yd=1 if tmp[1]>1000 else -1 if tmp[1]<-1000 else 0
	return (xd,yd)
gc()