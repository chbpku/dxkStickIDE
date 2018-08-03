from _module import *
def value(addr=None):
  return command(slot(addr,4),b'get_poten_val',2)