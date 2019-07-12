from microbit import *
import mb,touch,oled

for row in range(4):
    pool=[mb.get_type(chr(ord('a')+row*4+i)) for i in range(4)]
    oled.show(row*2,0,pool)
while 1:
    display.show(Image.HAPPY if touch.get() else Image.SAD)
    sleep(100)