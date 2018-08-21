import temp_humi, oled  # 导入模块控制库
from microbit import sleep

# 循环进行
while True:
    # 读取温度、湿度
    tmp, hum = temp_humi.temp_humi()

    # 在OLED显示读数（中文）
    oled.clear()
    oled.show(1, 8, b'\xce\xc2\xb6\xc8\xa3\xba%s\xa1\xe6' % tmp)
    oled.show(5, 8, b'\xca\xaa\xb6\xc8\xa3\xba%s\xa3\xa5' % hum)

    # 判断温湿度状态
    tmp_state = b'\xb5\xcd\xce\xc2' if tmp < 20 else b'\xca\xca\xd6\xd0' if tmp < 30 else b'\xb8\xdf\xce\xc2'  # 低温<适中<高温
    hum_state = b'\xb8\xc9\xd4\xef' if hum < 50 else b'\xb3\xb1\xca\xaa'  # 干燥<潮湿

    # 在OLED显示状态
    oled.show(6, 0, tmp_state + b', ' + hum_state)

    # 1秒后再次读取
    sleep(1000)