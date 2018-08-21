import temp_humi, oled  # 导入模块控制库

# 读取温度、湿度
tmp, hum = temp_humi.temp_humi()

# 在OLED显示读数
oled.clear()
oled.show(0, 0, b'Temp: %s\'C' % tmp)
oled.show(2, 0, b'Humi: %s%%' % hum)