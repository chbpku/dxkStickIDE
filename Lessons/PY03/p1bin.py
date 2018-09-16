from microbit import *
import oled

while True:
    raw=i2c.read(0x20,1)[0]
    res=0
    for i in range(8):
        res=res*2+(raw&1)
        raw//=2
    oled.show(0,0,b'\xb6\xfe\xbd\xf8\xd6\xc6%10s'%bin(res))
    oled.show(3,0,b'\xca\xae\xbd\xf8\xd6\xc6%4d'%res)
    sleep(200)
    
