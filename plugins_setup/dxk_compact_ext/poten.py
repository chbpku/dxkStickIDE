from mb import _exe,gc
def value(addr):
	return _exe(addr,b'get_poten_val',2)
gc()