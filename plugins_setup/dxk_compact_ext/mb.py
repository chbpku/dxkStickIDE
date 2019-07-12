from microbit import i2c
from gc import collect as gc
def _exe(s,b,l=0,r=0):
	try:
		i2c.write(s,b)
		if l:
			d=i2c.read(s,l)
			if not r:
				d=int.from_bytes(d,'big')
			return d
	except:pass
def get_type(addr):
	return _exe(addr,b'get_type',1,0)
gc()