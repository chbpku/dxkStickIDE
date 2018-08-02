from _module import *
def get_light_val(addr):
    return command(slot(addr), b'get_light_val',2)