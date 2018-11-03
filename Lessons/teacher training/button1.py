from microbit import *

display.show(Image.ALL_CLOCKS, wait=True)
display.scroll(str(button_a.get_presses()))
