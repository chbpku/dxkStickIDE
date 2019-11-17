from mb import command,slot,gc
def get_voice_id(addr):
	return C(slot(addr,33),b'get_command',1)
gc()