# 电位器控制灯泡-改进3

# 硬件模块：
# micro:bit×1；主板×1
# 模块×2：电位器、LED灯泡

# 简介：
# 根据电位器读数设置LED灯泡状态
# 加入记录LED状态的变量以防止重复发出指令
# 使用函数列表方式简化语句
# 在micro:bit显示屏上增加对电位器示数的显示
# 绘制显示像素点移动的尾迹

import poten, led  # 导入模块控制库
from microbit import sleep, display

is_on = False  # 记录LED当前状态，防止重复操作
led.off()  # 确保初始LED为关闭状态
function_map = [led.off, led.on]  # 包含对LED灯操作的列表

pos_old = int(poten.value() * 25 / 4100)  # 用于记录上一帧像素点位置

# 循环进行
while True:
    # 读取电位器位置（0-4095）
    pv = poten.value()

    # 根据读数设置LED灯状态
    new_stat = (pv >= 2048)
    if new_stat != is_on:
        is_on = new_stat
        function_map[is_on]()

    # 渐隐效果
    for i in range(5):
        for j in range(5):
            lightness = display.get_pixel(i, j)
            display.set_pixel(i, j, max(0, lightness - 1))

    # 计算并设置点亮像素位置
    pos = int(pv * 25 / 4100)
    pt = pos
    while True:
        display.set_pixel(pt % 5, pt // 5, 9)
        if pt == pos_old:
            break
        elif pt > pos_old:
            pt -= 1
        else:
            pt += 1
    pos_old = pos

    # 等待0.2秒后进行下一次读数
    sleep(200)