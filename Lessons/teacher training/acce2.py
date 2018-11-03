from microbit import *
import music

while True:
    music.pitch(accelerometer.get_y(), 10)
