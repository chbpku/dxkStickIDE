# 测量温湿度-改进1
# 硬件模块：
# micro:bit×1；主板×1
# 模块×2：OLED显示屏、温湿度传感器
# 简介：
# 读取温湿度模块示数并显示在OLED显示屏上
# 增加条件结构以对当前温湿度状态分级

import temp_humi, oled  # 导入模块控制库
from microbit import sleep

sleep(0)  # 若读数为0则增大该处停顿时长等待温湿度模块加载完成

# 读取温度、湿度
tmp, hum = temp_humi.temp_humi()

# 在OLED显示读数
oled.clear()
oled.show(0, 0, b'Temp: %s\'C' % tmp)
oled.show(2, 0, b'Humi: %s%%' % hum)

# 判断温湿度状态
if tmp < 20:
    tmp_state = b'Cold'
elif tmp < 30:
    tmp_state = b'Cool'
else:
    tmp_state = b'Hot'

if hum < 50:
    hum_state = b'Dry'
else:
    hum_state = b'Wet'

# 在OLED显示状态
oled.show(6, 0, tmp_state + b', ' + hum_state)