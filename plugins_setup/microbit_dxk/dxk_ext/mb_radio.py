import radio
from microbit import i2c,sleep
_res=[]
def channel():
	return i2c.read(0x20,1)[0]%32
def group():
	return i2c.read(0x20,1)[0]//32
def _send(bytes,to_int):
	radio.send_bytes(bytes)
	sleep(10)
	_res.clear()
	tmp=radio.receive_bytes()
	while tmp!=None:
		if to_int:
			tmp=int.from_bytes(tmp,'big')
		_res.append(tmp)
		tmp=radio.receive_bytes()
def send(id,bseq,size,to_int):
	radio.config(channel=i2c.read(0x20,1)[0]%32)
	_send(b'%s\r%s\r%s'%(id,size,bseq),to_int)
	if len(_res)==1:
		return _res[0]
	return tuple(_res)
def r_eval(seq,grp=-1):
	radio.config(channel=i2c.read(0x20,1)[0]%32)
	_send(b'%s\r%s'%(grp,seq),0)
	for i in range(len(_res)):
		i,grp=_res[i].split(b'\r')
		_res[i]=(i,int(grp))
	return tuple(_res)
	