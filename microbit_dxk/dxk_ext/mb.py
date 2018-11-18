from microbit import i2c
from gc import collect as gc
from array import array
_rmo=False
_sho=1
_typ=None
_res=[]
_map=b'\x16\x1723456789:;<=>?'
_tt=array('B',(-1 for i in range(16)))
def remote_on(short=1):
	global mb_radio,_rmo,r_eval,_sho
	_rmo=True
	_sho=short
	import mb_radio,radio
	radio.on()
	radio.config(length=64)
	r_eval=mb_radio.r_eval
def _exe(s,b,l,r):
	try:
		i2c.write(s,b)
		if l:
			d=i2c.read(s,l)
			if not r:
				d=int.from_bytes(d,'big')
			return d
	except:pass
def command(slot,bseq,size=0,raw=False):
	if isinstance(slot,tuple):
		return mb_radio.send(slot[0],bseq,size,not raw)
	if slot==None:
		_res.clear()
		flag=0
		for i in range(16):
			if _tt[i]==_typ:
				rr=_exe(_map[i],bseq,size,raw)
				if rr!=None:_res.append(rr)
				flag=1
		if _rmo and not (flag and _sho):
			rr=command((_typ,),bseq,size,raw)
			if rr!=None:
				if isinstance(rr,tuple):_res.extend(rr)
				else:_res.append(rr)
		if not _res:return None
		return _res[0] if len(_res)==1 else tuple(_res)
	return _exe(i,bseq,size,raw)
def get_state(addr):
	return command(slot(addr),b'get_state',1)
def get_type(addr):
	t=slot(addr);n=t-22-26*(t>23)
	if _tt[n]<0:refresh(n)
	return _tt[n]
def get_id(addr):
	raw=_exe(slot(addr),b'get_id',16,1)
	return raw and '%08x'%int.from_bytes(raw[:4],'little')
def slot(addr,type=None):
	global _typ
	if isinstance(addr,int) or addr==None:
		if addr==None:
			_typ=type
		return addr
	addr=addr.lower()
	if len(addr)<8:
		addr=addr[-1].lower()
		if 'a'<=addr<='p':
			return _map[ord(addr)-97]
	for i in _map:
		if get_type(i)>0 and get_id(i)==addr:return i
	if _rmo:return (addr,)
def get_bin():
	tmp=i2c.read(32,1)[0]
	res,ptr='',1
	for i in range(8):
		res+=str(int(tmp&ptr>0))
		ptr*=2
	return res
def refresh(p):
	_tt[p]=_exe(_map[p],b'get_type',1,0) or 0
gc()