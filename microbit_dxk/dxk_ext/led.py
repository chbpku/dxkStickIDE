from mb import *
def on(addr=None):
  command(slot(addr,3),b'set_led_on')
def off(addr=None):
  command(slot(addr,3),b'set_led_off')
