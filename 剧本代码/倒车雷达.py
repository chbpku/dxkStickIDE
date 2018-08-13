from microbit import *
import ultrasonic,led
import music

light_on=0
ltimer=0
led.off()

dist=ultrasonic.value()
update_timer=0

while 1:
    update_timer+=1
    if update_timer>100:
        update_timer-=50
        dd=ultrasonic.value()
        if dd!=None:
            dist=dd
            update_timer-=50
    if dist!=None:
        if dist>20:# 不响应距离
            if light_on:
                light_on=0
                led.off()
        else:
            ltimer+=1
            check=400 if dist>10 else 200 if dist>5 else 100
            if ltimer>check:
                music.pitch(1000,50,wait=0)
                ltimer-=check
                if light_on:
                    light_on=0
                    led.off()
                else:
                    light_on=1
                    led.on()
                
