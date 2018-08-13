from microbit import *
import mic,led

thr=40# 声音强度阈值
dur=30# 亮灯时间

t=0
flag=0
led.off()
while 1:
    m=mic.value()
    if m!=None:
        if m>50:
            t=30
        else:
            t-=1
    if t>0:
        if not flag:
            flag=1
            led.on()
    else:
        if flag:
            flag=0
            led.off()