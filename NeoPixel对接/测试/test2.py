import neo_color
import neo_img
from microbit import *

grps=(1,3,2)
neo_color.setup(grps)
display.show(Image.HAPPY)

while 1:
    for i in range(24):
        neo_color.set_pixel(0,i,(10,0,0))
    for i in range(24):
        neo_color.set_pixel(0,i,(0,0,0))
    for i in range(30):
        neo_color.set_pixel(1,i,(0,10,0))
    for i in range(30):
        neo_color.set_pixel(1,i,(0,0,0))
    for y in range(9):
        for x in range(9):
            if x in (1,4,7) and y in (1,4,7):
                continue
            neo_color.set_pixel(2,y*9+x,(10*y,10*(7-x),10*x))
    for i in range(81):
        neo_color.set_pixel(2,i,(0,0,0))