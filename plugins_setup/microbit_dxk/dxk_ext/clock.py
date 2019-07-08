from mb import command,slot,gc
_=[0]*6
def time(addr=None):
	t=command(slot(addr,36),b'getT',6,1)
	if not t:
		return t
	for i in range(6):
		_[i]=t[i]-1
	return tuple(_)
def set_time(Y,M,D,h,m,s,addr=None):
	command(slot(addr,36),b"setT%c%c%c%c%c%c"%(Y,M,D,h,m,s))
gc()