import mb,oled,temp_humi,light
from microbit import *
import music
mb.remote_on()
counter=0
imap=Image(5,5)
flag=0
while 1:
    data=temp_humi.temp_humi()
    tmp,hum,lig='--','--','--'
    if data:
        if isinstance(data[0],int):
            tmp,hum=data
        else:
            tmp,hum=data[0]
    data=light.value()
    if isinstance(data,int):
        lig=data
    elif data:
        lig=data[0]
    oled.clear()
    oled.show(0,0,b'\xce\xc2\xb6\xc8\xa3\xba%s\xa1\xe6'%tmp)
    oled.show(2,0,b'\xca\xaa\xb6\xc8\xa3\xba%s\xa3\xa5'%hum)
    oled.show(4,0,b'\xb9\xe2\xc3\xf4\xa3\xba%s\xa6\xb8'%lig)
    sleep(500)