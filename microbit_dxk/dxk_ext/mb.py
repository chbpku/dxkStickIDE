from microbit import i2c
from gc import collect as gc
_rmode=False
_short=1
_type=None
_res=[]
def remote_on(short=1):
  global mb_radio,_rmode,r_eval,_short
  _rmode=True
  _short=short
  import mb_radio,radio
  radio.on()
  radio.config(length=64)
  r_eval=mb_radio.r_eval
def command(slot,bseq,size=0,raw=False):
  if isinstance(slot,tuple):
    return mb_radio.send(slot[0],bseq,size,not raw)
  if slot==None:
    _res.clear()
    flag=0
    try:
      if get_type(22)==_type:
        rr=command(22,bseq,size,raw)
        if rr!=None:
          _res.append(rr)
        flag=1
    except:pass
    try:
      if get_type(23)==_type:
        rr=command(23,bseq,size,raw)
        if rr!=None:
          _res.append(rr)
        flag=1
    except:pass
    if _rmode and not (flag and _short):
      rr=command((_type,),bseq,size,raw)
      if rr!=None:
        if isinstance(rr,tuple):
          _res.extend(rr)
        else:
          _res.append(rr)
    if not _res:
      return None
    if len(_res)==1:
      return _res[0]
    return tuple(_res)
  try:
    i2c.write(slot,bseq)
    if size:
      data=i2c.read(slot,size)
      if not raw:
        data=int.from_bytes(data,'big')
      return data
  except:
    return None 
def get_type(addr):
  return command(slot(addr),b'get_type',1)
def get_state(addr):
  return command(slot(addr),b'get_state',1)
def get_id(addr):
  addr=slot(addr)
  i2c.write(addr,b'get_id')
  id=i2c.read(addr,16)
  return "%02x%02x%02x%02x"%(id[3],id[2],id[1],id[0])
def slot(addr,type=None):
  if isinstance(addr,int) or addr==None:
    if addr==None:
      global _type
      _type=type
    return addr
  addr=addr.lower()
  if len(addr)<8:
    addr=addr[-1].lower()
    if addr=='a':
      return 22
    if addr=='b':
      return 23
  if get_id(22)==addr:
    return 22
  if get_id(23)==addr:
    return 23
  if _rmode:
    return (addr,)
gc()