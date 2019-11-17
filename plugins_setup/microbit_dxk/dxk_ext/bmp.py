from mb import command,slot,gc
def get_p(addr):
	return C(slot(addr,26),b'getP',2)
def get_t(addr):
	return C(slot(addr,26),b'getT',2)
def get_a(addr):
	return C(slot(addr,26),b'getA',2)
gc()