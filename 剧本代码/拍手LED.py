from microbit import *
import mic,led

thr=100# 声音强度阈值
dur=30# 亮灯时间

t=0
flag=0
led.off()
k1=k2=k3=k4=k5=0
tloop=0
m=0
while 1:
    tloop+=1
    if tloop%10:
        mm=mic.value()
        if mm!=None:
            m=max(m,mm)
    if tloop>50:
        tloop-=50
        if m!=None:
            if m>thr:
                t=dur
            t1=m%5
            t2=(m//5)%5
            t3=(m//25)%5
            t4=(m//625)%5
            t5=(m//3125)%5
            if (t5,t4,t3,t2,t1)>(k5,k4,k3,k2,k1):
                for i in range(5):
                    exec("k{x}=t{x}".format(x=i+1))
            img=Image(5,5)
            for i in range(5):
                eval("img.set_pixel(k%d,%d,5)"%(5-i,i))
                eval("img.set_pixel(t%d,%d,9)"%(5-i,i))
            display.show(img)
        m=0
    t-=1
    if t>0:
        if not flag:
            flag=1
            led.on()
    else:
        if flag:
            flag=0
            led.off()