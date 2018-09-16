from microbit import *
import oled, mb

while True:
    r = mb.get_bin()
    oled.show(0,0,b'\xb6\xfe\xbd\xf8\xd6\xc60b%8s'%r)
    oled.show(3,0,b'\xca\xae\xbd\xf8\xd6\xc6%4d'%int(r, 2))
    sleep(200)
    