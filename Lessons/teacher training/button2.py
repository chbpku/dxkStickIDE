from microbit import *

while running_time() < 5000:
    display.show(Image.ASLEEP)
else:
    display.show(Image.SURPRISED)
