import neo_color,neo_img
import touch
from random import randrange
from microbit import *

neo_img.setup((1,3,2))
display.show(Image.HAPPY)

refresh=((0,0,0),)*24

neo_img.set_rainbow(0,2,0,24)
neo_img.set_rainbow(1,3,18,45)
while 1:
    neo_color.fill(2,tuple(randrange(100) for i in range(3)) if touch.get() else (0,0,0),addr=0x17)
    sleep(100)