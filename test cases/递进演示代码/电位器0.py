# 电位器控制灯泡-基础
# 硬件模块：
# micro:bit×1；主板×1
# 模块×2：电位器、LED灯泡
# 简介：
# 根据电位器读数设置LED灯泡状态
# LED在关闭状态下重复接收关闭指令时将会闪烁

import poten, led  # 导入模块控制库
from microbit import sleep

# 循环进行
while True:
    # 读取电位器位置（0-4095）
    pv = poten.value()

    # 根据读数设置LED灯状态
    if pv < 2048:
        led.off()
    else:
        led.on()

    # 等待0.2秒后进行下一次读数
    sleep(200)