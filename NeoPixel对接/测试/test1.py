import neo
from microbit import *

grps=neo.setup((0,))
display.show(Image.HAPPY)
while 1:
    for y in range(8):
        for x in range(8):
            grps[0].set_pixel(y*8+x,(10*y,10*(7-x),10*x))
    for i in range(64):
        grps[0].set_pixel(i,(0,0,0))
