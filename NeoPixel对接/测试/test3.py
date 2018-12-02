from microbit import *
import neo
from random import randrange

grps=neo.setup((0,))
grps[0].set_rainbow(0,0,24)
display.show(Image.HAPPY)

