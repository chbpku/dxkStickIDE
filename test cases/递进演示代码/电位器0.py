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