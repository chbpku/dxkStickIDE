from microbit import *
from mb import get_type
ta,tb=0,0
display.clear()
while 1:
    ta=get_type(22)
    if ta:
        for i in (0,1):
            for j in range(5):
                display.set_pixel(i,j,9)
    else:
        for i in (0,1):
            for j in range(5):
                display.set_pixel(i,j,0)
    tb=get_type(23)
    if tb:
        for i in (0,1):
            for j in range(5):
                display.set_pixel(i+3,j,9)
    else:
        for i in (0,1):
            for j in range(5):
                display.set_pixel(i+3,j,0)
    if ta==None or tb==None:
        continue
    if ta>tb:
        ta,tb=tb,ta
    if ta==5 and tb==8:
        # 测试光照、超声波（延长）
        import light,ultrasonic,music
        counter=0
        while not (button_a.get_presses()+button_b.get_presses()):
            display.clear()
            l,u=light.value(),ultrasonic.value()
            for i in range(10):
                if l>=410:
                    display.set_pixel(i%5,i//5,9)
                    l-=410
                else:
                    display.set_pixel(i%5,i//5,int(9*l/410))
                    break
            music.pitch(1000-2*u,50,wait=0)
            for i in range(15):
                if u>=10:
                    display.set_pixel(i%5,2+i//5,9)
                    u-=10
                else:
                    display.set_pixel(i%5,2+i//5,int(9*u/10))
                    break
            sleep(100)
        break
    elif ta==6 and tb==7:
        # 测试声音、手柄（延长）
        import mic,joypad
        while not (button_a.get_presses()+button_b.get_presses()):
            display.clear()
            keys,stick=joypad.values()
            for i in range(5):
                display.set_pixel(i,0,9*keys[i])
            x=max(0,min(4,2+round(stick[0]/1000)))
            y=max(0,min(4,2+round(stick[1]/1000)))
            display.set_pixel(x,4,9)
            display.set_pixel(4,y,9)
            m=mic.value()
            for i in range(12):
                if m>=30:
                    display.set_pixel(i%4,i//4+1,9)
                    m-=30
                else:
                    display.set_pixel(i%4,i//4+1,int(9*m/30))
                    break
            sleep(50)
        break
    else:
        sleep(10)
display.clear()