from _module import *
def set_led_on(addr):
    command(slot(addr), b'set_led_on')
def set_led_off(addr):
    command(slot(addr), b'set_led_off')
