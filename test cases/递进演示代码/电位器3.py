import poten, led  # 导入模块控制库
from microbit import sleep, display

is_on = False  # 记录LED当前状态，防止重复操作
led.off()  # 确保初始LED为关闭状态
function_map = [led.off, led.on]  # 包含对LED灯操作的列表

pos_real = 0  # 用于使像素点平滑移动

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
    pos_real = (pv * 25 / 4100 + pos_real) / 2
    pos = int(pos_real)
    display.set_pixel(pos % 5, pos // 5, 9)

    # 等待0.2秒后进行下一次读数
    sleep(200)