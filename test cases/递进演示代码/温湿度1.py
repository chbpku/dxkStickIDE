import temp_humi, oled  # 导入模块控制库

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