from mb import _exe,gc
from microbit import sleep
def show(y,x,string,addr):
	if isinstance(string,bytes):
		_exe(addr,b'DisplayGB2312,%d,%d,'%(y,x)+string[:16])
	else:
		string=str(string)[:16]
		_exe(addr,b'DisplayGB2312,%d,%d,%s'%(y,x,string))
	sleep(len(string))
def clear(addr):
	_exe(addr,b'ClearScreen')
	sleep(15)
gc()