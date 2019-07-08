from mb import command,slot,gc
def get(addr=None):
    return command(slot(addr,9),b'get_touch',1)
gc()