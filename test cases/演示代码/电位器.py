# 电位器控制闪烁小灯

# 简介：
# 通过读取电位器旋钮的读数控制LED灯泡闪烁与蜂鸣器发声的频率

# 硬件模块：
# micro:bit×1；主板×1
# 模块×2：电位器、LED灯泡

from microbit import *
import music
import poten, led  # 模块控制库

# 初始化记录变量
t, led_on = 0, 0
led.off()

while True:
    # 向计时变量增加部分读数
    t += poten.value() or 1
    if t > 5000:
        t -= 5000

        # 蜂鸣
        music.pitch(1000, 50, wait=0)

        # 切换LED灯状态
        if led_on:
            led_on = 0
            led.off()
        else:
            led_on = 1
            led.on()

    # 延迟50ms后继续读数
    sleep(50)