import mb
import neo

from microbit import *

grps=neo.setup((1,3,2))
display.show(Image.HAPPY)
while 1:
    display.scroll(grps[0].g,wait=0)
    for i in range(24):
        grps[0].set_pixel(i,(10,0,0))
    for i in range(24):
        grps[0].set_pixel(i,(0,0,0))
    display.scroll(grps[1].g,wait=0)
    for i in range(30):
        grps[1].set_pixel(i,(0,10,0))
    for i in range(30):
        grps[1].set_pixel(i,(0,0,0))
    for y in range(9):
        for x in range(9):
            if x in (1,4,7) and y in (1,4,7):
                continue
            grps[2].set_pixel(y*9+x,(10*y,10*(7-x),10*x))
    for i in range(81):
        grps[2].set_pixel(i,(0,0,0))