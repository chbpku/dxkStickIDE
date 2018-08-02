from _module import *
def value(addr):
    return command(slot(addr), b'get_light_val',2)