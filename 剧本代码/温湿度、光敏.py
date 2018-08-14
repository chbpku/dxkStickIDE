import mb,oled,light,led,temp_humi
from microbit import *
import music
flag=0
oled.clear()
mb.remote_on()
led.off()
get_t=0
ll=0
tmp,hum='--','--'
while 1:
    get_t+=1
    if get_t>500:
        get_t-=500
        t,h=temp_humi.temp_humi()
        if t!=None:
            tmp,hum=t,h
        oled.clear()
        oled.show(1,8,b'\xce\xc2\xb6\xc8\xa3\xba%s\xa1\xe6'%tmp)
        oled.show(4,8,b'\xca\xaa\xb6\xc8\xa3\xba%s\xa3\xa5'%hum)
    if get_t%50==0:
        l=light.value()
        if l!=None:
            ll=l
        if ll>1000:
            if not flag:
                flag=1
                led.on()
        else:
            if flag:
                flag=0
                led.off()