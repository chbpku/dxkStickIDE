from microbit import i2c
_rmode=False
def remote_on():
  global mb_radio,_rmode,r_eval
  _rmode=True
  import mb_radio,radio
  radio.on()
  radio.config(length=64)
  r_eval=mb_radio.r_eval
def command(slot,bseq,size=0,raw=False):
  if isinstance(slot,tuple):
    return mb_radio.send(slot[0],bseq,size,not raw)
  i2c.write(slot,bseq)
  if size:
    data=i2c.read(slot,size)
    if not raw:
      data=int.from_bytes(data,'big')
    return data
def get_id(addr):
  addr=slot(addr)
  i2c.write(addr,b'get_id')
  return "%02x%02x%02x%02x" % tuple(i2c.read(addr,4))
def get_type(addr):
  return command(slot(addr),b'get_type',1)
def get_state(addr):
  return command(slot(addr),b'get_state',1)
def slot(addr=None,type=None):
  if isinstance(addr,int):
    return addr
  if addr==None:
    try:
      if get_type(22)==type:return 22
    except:pass
    try:
      if get_type(23)==type:return 23
    except:pass
    if _rmode:
      return (type,)
    raise OSError('no slot %s'%addr)
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
  raise OSError('no id %s'%addr)