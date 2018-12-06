import neo_color
import mb
from microbit import *

grps=(1,2)
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

cs=[(100,0,0),(0,100,0),(0,0,100),(0,0,0)]


while 1:
    for p in range(24):
        neo_color.set_pixel(0,p,(75,60,0))
        neo_color.set_pixel(0,(p-1)%24,(0,0,0))
        sleep(10)
    for c in cs:
        neo_color.fill(1,c)
        sleep(200)
    for y in range(9):
        for x in range(9):
            neo_color.set_xy(2,x,y,(100,0,0))
    for x in range(9):
        neo_color.set_xy(2,x,-1,(0,100,0))
    for y in range(9):
        neo_color.set_xy(2,-1,y,(0,0,100))
    neo_color.set_xy(2,-1,-1,(0,0,0))
