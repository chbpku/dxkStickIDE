import radio
from microbit import i2c,sleep
def channel():
  return i2c.read(0x20,1)[0]%32
def group():
  return i2c.read(0x20,1)[0]//32
def _send(bytes):
  radio.send_bytes(bytes)
  sleep(50)
  res,tmp=[],radio.receive_bytes()
  while tmp!=None:
    res.append(tmp)
    tmp=radio.receive_bytes()
  return res
def send(id,bseq,size,to_int):
  radio.config(channel=i2c.read(0x20,1)[0]%32)
  res=_send(b'%s\r%s\r%s'%(id,size,bseq))
  if to_int:
    res=[int.from_bytes(t,'big') for t in res]
  return res
def r_eval(seq,grp=-1):
  radio.config(channel=i2c.read(0x20,1)[0]%32)
  res=[]
  for i in _send(b'%s\r%s'%(grp,seq)):
    i,grp=i.split(b'\r')
    res.append((i,int(grp)))
  return res
  