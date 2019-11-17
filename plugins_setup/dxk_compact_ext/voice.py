from mb import _exe,gc
def get_voice_id(addr):
	return _exe(addr,b'get_command',1)
gc()