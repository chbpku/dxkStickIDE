from _module import *
def on(addr):
    command(slot(addr), b'set_led_on')
def off(addr):
    command(slot(addr), b'set_led_off')
