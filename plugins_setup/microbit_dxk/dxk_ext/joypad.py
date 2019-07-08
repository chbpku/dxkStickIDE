from mb import command,slot,gc
def conv(data):
	x,y=data[5]*256+data[6],data[7]*256+data[8]
	x=x-2048;y=2048-y
	return tuple(data[:5]),(x,y)
def values(addr=None):
	data=command(slot(addr,7),b'get_key_val',9,True)
	if isinstance(data,bytes):
		return conv(data)
	if data==None:
		return None,None
	return tuple(conv(i) for i in data)
def keys(addr=None):
	return values(addr)[0]
def stickxy(addr=None):
	return values(addr)[1]
def stick_directions(addr=None):
	tmp=values(addr)[1]
	if tmp==None:return
	xd=1 if tmp[0]>1000 else -1 if tmp[0]<-1000 else 0
	yd=1 if tmp[1]>1000 else -1 if tmp[1]<-1000 else 0
	return (xd,yd)
gc()