import radio
from microbit import i2c
radio.on()
def send(id,bseq,size,to_int):
  radio.config(channel=min(i2c.read(0x20,1)[0],100))
  radio.send_bytes(b'%s\r%s\r%s'%(id,bseq,size))
  res,tmp=[],radio.receive_bytes()
  while tmp:
    if to_int:
      tmp=int.from_bytes(tmp,'big') 
    res.append(tmp)
    tmp=radio.receive_bytes()
  return res