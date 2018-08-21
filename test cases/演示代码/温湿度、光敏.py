# 远程测量温湿度、亮度

# 简介：
# 主节点读取子节点上传感器的读数并将结果显示在自身的元件上：
# 温湿度传感器的读数将直接显示于OLED显示屏内，光敏电阻则会在光强低于一定阈值时点亮LED灯泡，在光强高于阈值时则熄灭

# 硬件模块：
# micro:bit×2；主板×2
# 模块×4：（主节点）OLED显示屏、LED灯泡；（子节点）温湿度传感器、光敏电阻

import mb,oled,light,led,temp_humi # 主板、模块控制库
from microbit import *
import music

# 初始化
mb.remote_on()# 启动远程模式
led_on=0
oled.clear()
led.off()
timer=0
light_read=0
tmp,hum='--','--'
while True:
    timer+=1

    # 每500帧更新温湿度读数
    if timer>500:
        timer-=500
        t,h=temp_humi.temp_humi()
        if t!=None:
            tmp,hum=t,h
        oled.clear()
        oled.show(1,8,b'\xce\xc2\xb6\xc8\xa3\xba%s\xa1\xe6'%tmp)
        oled.show(4,8,b'\xca\xaa\xb6\xc8\xa3\xba%s\xa3\xa5'%hum)
    
    # 每50帧更新光敏电阻读数，显示于LED上
    if timer%50==0:
        l=light.value()
        if l!=None:
            light_read=l
        if light_read>1000:
            if not led_on:
                led_on=1
                led.on()
        else:
            if led_on:
                led_on=0
                led.off()