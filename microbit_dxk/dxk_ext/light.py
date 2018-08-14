from mb import command,slot,gc
def value(addr=None):
  return command(slot(addr,5),b'get_light_val',2)
gc()