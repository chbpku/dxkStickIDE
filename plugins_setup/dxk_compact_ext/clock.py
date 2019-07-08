from mb import _exe,gc
_=[0]*6
def time(addr):
	_exe(addr,b'getT',6,1)
	try:
		for i in range(6):
			_[i]=t[i]-1
		return tuple(_)
	except:pass
def set_time(Y,M,D,h,m,s,addr):
	_exe(addr,b"setT%c%c%c%c%c%c"%(Y,M,D,h,m,s))
gc()