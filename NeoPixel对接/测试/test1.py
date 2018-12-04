import neo_color,neo_img
import oled,mb
from microbit import *

grps=(1,3,2)
neo_color.setup(grps)
for row in range(4):
    pool=[mb.get_type(chr(ord('a')+row*4+i)) for i in range(4)]
    oled.show(row*2,0,pool)
display.show(Image.HAPPY)
##i2c.write(22,b'setP%c%c'%(0,0)+b'%c%c%c'%(10,20,40))
##i2c.read(22,1)

while 1:
    for y in range(8):
        for x in range(8):
            neo_color.set_pixel(0,y*8+x,(10*y,10*(7-x),10*x),addr=22)
    for i in range(64):
        neo_color.set_pixel(0,i,(0,0,0),addr=22)
