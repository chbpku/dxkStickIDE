from microbit import *
import random

while True:
    display.show("*")
    if accelerometer.was_gesture("shake"):
        display.show(str(random.randint(1, 6)))
        sleep(1000)
