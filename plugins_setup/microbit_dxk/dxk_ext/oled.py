from mb import command,slot,gc
from microbit import sleep
def show(y,x,string,addr=None):
	if isinstance(string,bytes):
		command(slot(addr,1),b'DisplayGB2312,%d,%d,'%(y,x)+string[:16])
	else:
		string=str(string)[:16]
		command(slot(addr,1),b'DisplayGB2312,%d,%d,%s'%(y,x,string))
	sleep(len(string))
def clear(addr=None):
	command(slot(addr,1),b'ClearScreen')
	sleep(15)
gc()