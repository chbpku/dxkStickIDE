import neo_color
import neo_img
from microbit import *

neo_img.setup((1,),addr=0x16)
neo_img.setup((2,3),addr=0x17)
display.show(Image.HAPPY)

refresh=((0,0,0),)*24

while 1:
    neo_img.set_rainbow(0,0,0,24,addr=0x16)
    neo_img.set_rainbow(0,0,18,45,addr=0x17)
    neo_img.set_rainbow(1,1,0,30,addr=0x17)
    sleep(2000)
    neo_color.set_pixel_range(0,0,refresh,addr=0x16)
    neo_color.fill(0,(0,0,0),addr=0x17)
    for i in range(30):
        neo_color.set_pixel(1,i,(0,0,0),addr=0x17)
    sleep(1000)

