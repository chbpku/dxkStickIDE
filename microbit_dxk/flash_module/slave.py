import radio,music
from microbit import *
radio.on()
radio.config(length=64)
def get_id(addr):
  try:
    i2c.write(addr,b'get_id')
    raw=i2c.read(addr,16)
    return b"%02x%02x%02x%02x"%(raw[3],raw[2],raw[1],raw[0])
  except:
    return None
def get_type(addr):
  i2c.write(addr,b'get_type')
  return i2c.read(addr,1)[0]
music.play(music.POWER_UP,wait=False)
for i in range(25):
  display.set_pixel(i%5,i//5,9)
  sleep(10)
for i in range(25):
  display.set_pixel(i%5,i//5,0)
  sleep(10)
id_a=get_id(22)
id_b=get_id(23)
timer=0
while 1:
  timer+=1
  if timer>5000:
    timer-=5000
    id_a=get_id(22)
    id_b=get_id(23)
  gid=i2c.read(0x20,1)[0]
  radio.config(channel=gid%32)
  seq=radio.receive_bytes()
  if seq==None:
    continue
  seq=seq.split(b'\r')
  if len(seq)==2:
    grp,bseq=seq
    try:grp=int(grp)
    except:continue
    if grp==-1 or grp==gid//32:
      try:
        res=eval(bseq)
        if res!=None:
          radio.send_bytes(b'%r\r%d'%(res,gid//32))
      except:pass
  if len(seq)==3:
    id,size,bseq=seq
    try:size=int(size)
    except:continue
    if len(id)==8:
      try:
        if id_a==id:
          i2c.write(22,bseq)
          if size:
            radio.send_bytes(i2c.read(22,size))
      except:pass
      try:
        if id_b==id:
          i2c.write(23,bseq)
          if size:
            radio.send_bytes(i2c.read(23,size))
      except:pass
    else:
      try:
        id=int(id)
      except:continue
      try:
        if get_type(22)==id:
          i2c.write(22,bseq)
          if size:
            radio.send_bytes(i2c.read(22,size))
      except:pass
      try:
        if get_type(23)==id:
          i2c.write(23,bseq)
          if size:
            radio.send_bytes(i2c.read(23,size))
      except:pass
  
