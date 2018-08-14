from mb import command,slot,gc
def on(addr=None):
  command(slot(addr,3),b'set_led_on')
def off(addr=None):
  command(slot(addr,3),b'set_led_off')
gc()
