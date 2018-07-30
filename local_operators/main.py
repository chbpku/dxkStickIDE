from microbit import *
from oled import *
from ultrasonic import *

while 1:
    data=get_distance_val(22)
    display_text(23,0,0,data)
    sleep(1000)