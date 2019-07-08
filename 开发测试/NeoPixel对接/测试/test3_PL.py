import neo_color
import mb
from microbit import *

SLOT=0x35
LIGHT=Image().invert()
def _exe(s,b,l,r):
    try:
        i2c.write(s,b)
        if l:
            try:
                d=i2c.read(s,l)
                if not r:
                    d=int.from_bytes(d,'big')
                display.show(LIGHT)
                sleep(50)
                display.clear()
                return d
            except:
                display.scroll('R',delay=50)
    except:
        display.scroll('W',delay=50)


grps=(1,2,3)
neo_color.setup(grps)
display.show(Image.HAPPY)
##i2c.write(22,b'setP%c%c'%(0,0)+b'%c%c%c'%(10,20,40))
##i2c.read(22,1)
pool_set1=((255,255,0),(0,100,0),(0,0,100))*8
pool_set2=((100,80,0),(0,100,80),(80,0,100))*10
pool_clear1=((0,0,0),)*24
pool_clear2=((0,0,0),)*30
##mb._exe=_exe
while 1:
    neo_color.set_pixel_range(0,0,pool_set1)
    neo_color.set_pixel_range(1,0,pool_set2)
    neo_color.set_pixel_range(2,0,pool_set2)
    for i in range(24):
        neo_color.set_pixel(0,i,(0,0,0))
    for i in range(30):
        neo_color.set_pixel(1,i,(0,0,0))
        neo_color.set_pixel(2,i,(0,0,0))
