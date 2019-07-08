from mb import command,slot,gc
def value(addr=None):
	return command(slot(addr,8),b'get_distance_val',2)
gc()