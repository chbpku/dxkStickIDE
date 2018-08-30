# 倒车雷达

# 简介：
# 模拟倒车雷达功能，通过超声测距模块测量与障碍物的距离
# 并根据距离远近发出不同频率的蜂鸣声与LED灯闪烁提示。

# 硬件模块：
# micro:bit×1；主板×1；延长插槽×1
# 模块×2：超声测距、LED灯泡

from microbit import *
import music
import ultrasonic, led  # 模块控制库

# 初始化LED灯闪烁系统
light_on = 0
ltimer = 0
led.off()

# 初始化测距记录系统
dist = ultrasonic.value()
update_timer = 0

while True:
    # 每隔一段时间读取一次距离示数
    update_timer += 1
    if update_timer > 50:
        update_timer -= 50
        dd = ultrasonic.value()
        if dd != None:  # 仅在读取示数成功时更新距离记录
            dist = dd
            update_timer -= 50

    # 在获取到距离读数后进入响应系统
    if dist != None:
        if dist > 20:  # 在该距离以上不响应
            if light_on:
                light_on = 0
                led.off()
        else:
            # 由距离确定闪烁频率
            check = 400 if dist > 10 else 200 if dist > 5 else 100

            # 更新闪烁计时
            ltimer += 1
            if ltimer > check:
                ltimer -= check

                # 蜂鸣
                music.pitch(1000, 50, wait=0)

                # 切换LED灯状态
                if light_on:
                    light_on = 0
                    led.off()
                else:
                    light_on = 1
                    led.on()