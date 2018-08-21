# 测量温湿度-改进2

# 硬件模块：
# micro:bit×1；主板×1
# 模块×2：OLED显示屏、温湿度传感器

# 简介：
# 读取温湿度模块示数并显示在OLED显示屏上
# 增加条件结构以对当前温湿度状态分级
# 增加循环结构进行持续判断，并使用GB2312编码改用中文显示

import temp_humi, oled  # 导入模块控制库
from microbit import sleep

sleep(0)  # 若读数为0则增大该处停顿时长等待温湿度模块加载完成

# 循环进行
while True:
    # 读取温度、湿度
    tmp, hum = temp_humi.temp_humi()

    # 在OLED显示读数（中文）
    oled.clear()
    oled.show(0, 0, b'\xce\xc2\xb6\xc8\xa3\xba%s\xa1\xe6' % tmp)
    oled.show(2, 0, b'\xca\xaa\xb6\xc8\xa3\xba%s\xa3\xa5' % hum)

    # 判断温湿度状态
    if tmp < 20:
        tmp_state = b'\xb5\xcd\xce\xc2'  # 低温
    elif tmp < 30:
        tmp_state = b'\xca\xca\xd6\xd0'  # 适中
    else:
        tmp_state = b'\xb8\xdf\xce\xc2'  # 高温

    if hum < 50:
        hum_state = b'\xb8\xc9\xd4\xef'  # 干燥
    else:
        hum_state = b'\xb3\xb1\xca\xaa'  # 潮湿

    # 在OLED显示状态
    oled.show(6, 0, tmp_state + b', ' + hum_state)

    # 1秒后再次读取
    sleep(1000)