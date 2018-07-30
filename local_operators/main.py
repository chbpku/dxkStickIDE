from microbit import *
from led import *
from oled import *

while 1:
    set_led_on(22)
    display_text(23,0,0,'aaaaaaaa')
    sleep(1000)
    display_text(23,0,0,'bbbbbbbb')
    set_led_off(22)
    sleep(1000)