from mb import _exe as C,gc
def get_p(addr):
	return C(addr,b'getP',2)
def get_t(addr):
	return C(addr,b'getT',2)
def get_a(addr):
	return C(addr,b'getA',2)
gc()