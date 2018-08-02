from _module import *
def value(addr):
    return command(slot(addr), b'get_poten_val',2)