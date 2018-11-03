from microbit import *
import music

# 金属探测器
while True:
    fs = compass.get_field_strength()
    if fs > 60000:
        music.pitch(fs // 100, 10)
    sleep(200)
