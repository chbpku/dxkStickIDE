from mb import command,slot,gc
def value(addr=None):
	return command(slot(addr,6),b'get_mic_val',2)
gc()