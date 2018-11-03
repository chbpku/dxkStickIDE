from microbit import *
import neopixel

np = neopixel.NeoPixel(pin16, 12)
i = 0
while True:
    np.clear()
    np[i] = (30, 0, 0)
    np[(i + 6) % 12] = (0, 30, 0)
    np.show()
    i = (i + 1) % 12
    sleep(200)
