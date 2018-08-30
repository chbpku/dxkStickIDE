# 声控小灯

# 简介：
# 麦克风模块会持续读取声音，当读数高于一定值时会使小灯点亮一段时间。

# 硬件模块：
# micro:bit×1；主板×1
# 模块×2：麦克风、LED灯泡

from microbit import *
import mic, led  # 模块控制库

thr = 60  # 声音强度阈值
dur = 50  # 亮灯时间

# 初始化LED灯闪烁系统
led_on = 0
led.off()

# 初始化计时变量
t_led_delay = 0
tloop = 0
volumn = 0

while True:
    tloop += 1

    # 每10帧取一次音量，保留最大值
    if tloop % 10:
        tmp = mic.value()
        if tmp != None:
            volumn = max(volumn, tmp)

    # 每30帧更新一次，在声音足够大时刷新LED灯点亮时间
    if tloop > 30:
        tloop -= 30
        if volumn > thr:
            t_led_delay = dur
        volumn = 0

    # 更新LED灯显示状态
    t_led_delay -= 1
    if t_led_delay > 0:
        if not led_on:
            led_on = 1
            led.on()
    else:
        if led_on:
            led_on = 0
            led.off()