from microbit import *
# 测试超声波
import ultrasonic,music
counter=0
while 1:
    u=ultrasonic.value()
    if u==None:
        display.show(Image.SAD)
    else:
        music.pitch(1000-2*u,50,wait=0)
        display.clear()
        for i in range(25):
            if u>=10:
                display.set_pixel(i%5,i//5,9)
                u-=10
            else:
                display.set_pixel(i%5,i//5,int(9*u/10))
                break
    sleep(100)
