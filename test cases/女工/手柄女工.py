from microbit import *
from mb import get_type
import mic,joypad
while 1:
    try:
        keys,stick=joypad.values()
        x=max(0,min(4,2+round(stick[0]/1000)))
        y=max(0,min(4,2+round(stick[1]/1000)))
        display.clear()
        for i in range(5):
            display.set_pixel(i,0,9*keys[i])
        display.set_pixel(x,y,9)
        sleep(10)
    except:
        display.show(Image.SAD)
        sleep(50)
