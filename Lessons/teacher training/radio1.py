﻿from microbit import *
import radio
import neopixel

np = neopixel.NeoPixel(pin16, 12)

# 自己的颜色
my = "60,0,0"

# 记录收到的颜色队列
clst = [(0, 0, 0) for i in range(12)]
radio.on()
while True:
    # 按钮控制自己发送颜色
    if button_a.was_pressed():
        radio.send(my)
    # 接收空中的颜色
    r = radio.receive()
    if r is not None:
        display.show(Image.YES)
        clst.pop(0)
        clst.append(tuple(map(int, r.split(","))))
    else:
        display.show(Image.ASLEEP)
    # 显示颜色队列
    np.clear()
    for i in range(12):
        np[i] = clst[i]
    np.show()
    # 停留一会儿
    sleep(100)
