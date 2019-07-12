from mb import command,slot,gc
def value(addr=None):
	return command(slot(addr,4),b'get_poten_val',2)
gc()