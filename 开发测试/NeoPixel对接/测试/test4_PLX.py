import neo_color
import mb
from microbit import *

grps=(1,3,2)
neo_color.setup(grps)
display.show(Image.HAPPY)


##def _exe(s,b,l,r):
##    try:
##        i2c.write(s,b)
##        if l:
##            try:
##                d=i2c.read(s,l)
##                if not r:
##                    d=int.from_bytes(d,'big')
##                display.show(LIGHT)
##                sleep(50)
##                display.clear()
##                return d
##            except:
##                display.scroll('R',delay=50)
##    except:
##        display.scroll('W',delay=50)
##mb._exe=_exe
pool_set1=((255,255,0),(0,100,0),(0,0,100))*8
pool_set2=((100,80,0),(0,100,80),(80,0,100))*10
pool_clear1=((0,0,0),)*24
pool_clear2=((0,0,0),)*30

G=2
while 1:
    neo_color.set_pixel_range(0,0,pool_set1)
    neo_color.set_pixel_range(1,0,pool_set2)
    for y in range(9):
        for x in range(9):
            neo_color.set_xy(G,x,y,(100,0,0))
    for x in range(9):
        neo_color.set_xy(G,x,-1,(0,100,0))
    for y in range(9):
        neo_color.set_xy(G,-1,y,(0,0,100))
    for i in range(24):
        neo_color.set_pixel(0,i,(0,0,0))
    for i in range(30):
        neo_color.set_pixel(1,i,(0,0,0))
    neo_color.set_xy(G,-1,-1,(0,0,0))
