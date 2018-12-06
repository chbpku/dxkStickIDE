import neo_color
import neo_img
from microbit import *

grps=(1,3,2)
neo_img.setup(grps)
display.show(Image.HAPPY)

refresh=((0,0,0),)*24

while 1:
    neo_img.set_rainbow(0,0,0,24)
    neo_img.set_rainbow(1,1,0,30)
    neo_img.set_rainbow(2,0,18,45)
    sleep(2000)
    neo_color.set_pixel_range(0,0,refresh)
    for i in range(30):
        neo_color.set_pixel(1,i,(0,0,0))
    neo_color.fill(2,(0,0,0))
    sleep(1000)

