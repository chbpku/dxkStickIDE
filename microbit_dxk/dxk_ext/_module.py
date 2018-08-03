from microbit import i2c
def command(slot,bseq,returnsize=0,raw=False):
  i2c.write(slot,bseq)
  if returnsize:
    data=i2c.read(slot,returnsize)
    if raw:
      return data
    return int.from_bytes(data,'big')
def get_id(addr):
  addr=slot(addr)
  i2c.write(addr,'get_id')
  return "%02x%02x%02x%02x" % tuple(i2c.read(addr,4))
def get_type(addr):
  return command(slot(addr),'get_type',1)
def get_state(addr):
  return command(slot(addr),'get_state',1)
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
