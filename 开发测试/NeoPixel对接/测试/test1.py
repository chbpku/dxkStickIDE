import neo_color,neo_img
import oled,mb
from microbit import *

grps=(1,)
neo_color.setup(grps,addr=SLOT)
for row in range(4):
    pool=[mb.get_type(chr(ord('a')+row*4+i)) for i in range(4)]
    oled.show(row*2,0,pool)
display.show(Image.HAPPY)

while 1:
    for i in range(24):
        neo_color.set_pixel(0,i,(i*2,i*2,48-i*2))
    for i in range(24):
        neo_color.set_pixel(0,i,(0,0,0))
