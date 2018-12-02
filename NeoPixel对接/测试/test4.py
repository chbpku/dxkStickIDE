from microbit import *
import neo
from random import randrange

grps=neo.setup((0,1,2))
grps[1].set_rainbow(0,0,24)
display.show(Image.HAPPY)