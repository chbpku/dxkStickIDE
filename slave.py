import radio
from microbit import *
radio.on()
radio.config(length=100)
def get_id(addr):
  i2c.write(addr,b'get_id')
  return b"%02x%02x%02x%02x" % tuple(i2c.read(addr,4))
def get_type(addr):
  i2c.write(addr,b'get_type')
  return i2c.read(addr,1)[0]
while 1:
    sleep(10)
    radio.config(channel=min(i2c.read(0x20,1)[0],100))
    seq=radio.receive_bytes()
    if seq==None:
        continue
    seq=seq.split(b'\r')
    if len(seq)==2:
        grp,bseq=seq
        try:
            res=eval(bseq)
            if res!=None:
                radio.send_bytes(b'%r'%res)
        except:
            pass
    if len(seq)==3:
        id,bseq,size=seq
        size=int(size)
        if len(id)==8:
            try:
                if get_id(22)==id:
                    i2c.write(22,bseq)
                    if size:
                        radio.send_bytes(i2c.read(22,size))
            except:pass
            try:
                if get_id(23)==id:
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
    
