from mb import *
_res=[]
def temp(addr=None):
  return command(slot(addr,2),b'get_temp',1)
def humi(addr=None):
  return command(slot(addr,2),b'get_humi',1)
def temp_humi(addr=None):
  res=command(slot(addr,2),b'get_temp_humi',2)
  if isinstance(res,int):
    t,h=res//256,res%256
    if t>=128:t-=256
    return t,h
  if res==None:
    return None,None
  _res.clear()
  for rr in res:
    t,h=rr//256,rr%256
    if t>=128:t-=256
    _res.append((t,h))
  return tuple(_res)