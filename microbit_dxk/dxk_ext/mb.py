from microbit import i2c
_rmode=False
_short=1
_iter_type=None
_iter_res=[]
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
    _iter_res.clear()
    flag=0
    try:
      if get_type(22)==_iter_type:
        rr=command(22,bseq,size,raw)
        if rr!=None:
          _iter_res.append(rr)
        flag=1
    except:pass
    try:
      if get_type(23)==_iter_type:
        rr=command(23,bseq,size,raw)
        if rr!=None:
          _iter_res.append(rr)
        flag=1
    except:pass
    if _rmode and not (flag and _short):
      rr=command((_iter_type,),bseq,size,raw)
      if rr!=None:
        if isinstance(rr,tuple):
          _iter_res.extend(rr)
        else:
          _iter_res.append(rr)
    if not _iter_res:
      return None
    if len(_iter_res)==1:
      return _iter_res[0]
    return tuple(_iter_res)
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
def slot(addr=None,type=None):
  if isinstance(addr,int) or addr==None:
    if addr==None:
      global _iter_type
      _iter_type=type
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
  return None