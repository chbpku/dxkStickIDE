from mb import _exe,gc
_res=[]
def temp(addr):
	return _exe(addr,b'get_temp',1)
def humi(addr):
	return _exe(addr,b'get_humi',1)
def temp_humi(addr):
	res=_exe(addr,b'get_temp_humi',2)
	if res==None:
		return None,None
	t,h=res//256,res%256
	if t>=128:t-=256
	return t,h
gc()