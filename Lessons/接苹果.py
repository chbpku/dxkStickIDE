from microbit import *
import music
from random import randrange
import oled,joypad
score = 0
pos = 2
oled.clear()
oled.show(0,0,b'\xb5\xc3\xb7\xd6\xa3\xba0')# 得分：0
while 1:
    dropy = 0
    dropx = randrange(5) 
    while dropy<=4:
        keys=joypad.keys()
        if keys[3]:
            pos=max(0,pos-1)
        elif keys[4]:
            pos=min(4,pos+1)
        display.clear()
        display.set_pixel(dropx,dropy,9)
        display.set_pixel(pos,4,9)
        dropy+=1
        sleep(max(200,500-5*score))
    if dropx==pos:
        score+=1
        music.play('C7:1',wait=False)
        oled.show(0,0,b'\xb5\xc3\xb7\xd6\xa3\xba%d'%score)# 得分：{score}
    else:
        break
oled.show(2,0,b'\xd3\xce\xcf\xb7\xbd\xe1\xca\xf8')# 游戏结束
music.play(music.POWER_DOWN)