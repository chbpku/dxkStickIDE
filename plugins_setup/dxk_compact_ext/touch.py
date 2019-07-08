from mb import _exe,gc
def get(addr):
    return _exe(addr,b'get_touch',1)
gc()