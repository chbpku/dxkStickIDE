# 模块接口测试1
# 简介：
# 分别插入两组模块后，将分别调用不同的测试程序测试所有的模块接口
# 硬件模块：
# micro:bit×1；主板×1
# 模块×4：（组1）OLED显示屏、温湿度传感器；（组2）LED灯泡、电位器

# 分组1
# 测试对象：
# OLED显示屏、温湿度传感器、拨码开关（主板）
# 内容：
# OLED显示屏上将显示温湿度读数，同时拨码开关位置将按位显示在micro:bit显示屏上
# 拨动拨码开关以进行测试

# 分组2
# 测试对象：
# LED灯泡、电位器
# 内容：
# LED灯泡将根据电位器旋钮位置进行不同频率的闪烁
# 旋转电位器旋钮以进行测试

from microbit import *
from mb import get_type
ta, tb = 0, 0
display.clear()
while 1:
    ta = get_type(22)
    if ta:
        for i in (0, 1):
            for j in range(5):
                display.set_pixel(i, j, 9)
    else:
        for i in (0, 1):
            for j in range(5):
                display.set_pixel(i, j, 0)
    tb = get_type(23)
    if tb:
        for i in (0, 1):
            for j in range(5):
                display.set_pixel(i + 3, j, 9)
    else:
        for i in (0, 1):
            for j in range(5):
                display.set_pixel(i + 3, j, 0)
    if ta == None or tb == None:
        continue
    if ta > tb:
        ta, tb = tb, ta
    if ta == 1 and tb == 2:
        # 测试OLED、温湿度、拨码
        import oled, temp_humi
        display.clear()
        while not (button_a.get_presses() + button_b.get_presses()):
            chn = i2c.read(0x20, 1)[0]
            ptr = 1
            for i in range(10):
                display.set_pixel(i % 4, i // 4, 9 * bool(chn & ptr))
                ptr *= 2
            oled.clear()
            temp, humi = temp_humi.temp_humi()
            oled.show(0, 0, b'\xce\xc2\xb6\xc8\xa3\xba%s\xa1\xe6' % temp)
            oled.show(2, 0, b'\xca\xaa\xb6\xc8\xa3\xba%s%%' % humi)
            temp, humi = temp_humi.temp(), temp_humi.humi()
            oled.show(4, 0, b'\xce\xc2\xb6\xc8\xa3\xba%s\xa1\xe6' % temp)
            oled.show(6, 0, b'\xca\xaa\xb6\xc8\xa3\xba%s%%' % humi)
            sleep(500)
        break
    elif ta == 3 and tb == 4:
        # 测试LED、电位器
        display.show(Image.HAPPY)
        import led, poten
        led.off()
        flag, counter = 0, 0
        while not (button_a.get_presses() + button_b.get_presses()):
            counter += poten.value()
            if counter >= 4096:
                counter -= 4096
                if flag:
                    led.off()
                    flag = 0
                else:
                    led.on()
                    flag = 1
        break
    else:
        sleep(10)
display.clear()