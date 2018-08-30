# 通信测试（LED灯泡、子节点控制）

# 简介：
# 主节点读取子节点按钮按下次数，并将相应的结果再次发回至子节点进行显示
# 按钮A按下时将根据其按下次数逐个点亮/熄灭主节点与子节点显示屏上的像素
# 按钮B按下后将切换LED灯泡的亮暗情况，并相应在子节点上播放音效

# 硬件模块：
# micro:bit×2；主板×2
# 模块×1：LED灯泡

import mb,mb_node,led
from microbit import *
import music
mb.remote_on()
counter=0
imap=Image(5,5)
flag=1
while 1:
    x=mb_node.button('a')
    if x:
        x=x[0][0]
        for i in range(x):
            i,j=counter%5,counter//5
            imap.set_pixel(i,j,9-imap.get_pixel(i,j))
            counter=(counter+1)%25
        mb_node.show(repr(imap)[7:-2])
        display.show(imap)
    y=mb_node.button('b')
    if y and y[0][0]:
        if flag:
            led.on()
            sleep(10)
            mb_node.play('POWER_UP')
        else:
            led.off()
            sleep(10)
            mb_node.play('POWER_DOWN')
        flag=not flag