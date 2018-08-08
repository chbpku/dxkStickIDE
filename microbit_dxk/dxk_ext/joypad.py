from mb import *
def conv(data):
  x,y=data[5]*256+data[6],data[7]*256+data[8]
  x=x-2048;y=2048-y
  return tuple(data[:5]),(x,y)
def values(addr=None):
  data=command(slot(addr,7),b'get_key_val',9,True)
  if isinstance(data,bytes):
    return conv(data)
  return [conv(i) for i in data]
def keys(addr=None):
  return values(addr)[0]
def stickxy(addr=None):
  return values(addr)[1]