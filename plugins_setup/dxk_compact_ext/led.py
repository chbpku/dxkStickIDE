from mb import _exe,gc
def on(addr):
	_exe(addr,b'set_led_on')
def off(addr):
	_exe(addr,b'set_led_off')
gc()