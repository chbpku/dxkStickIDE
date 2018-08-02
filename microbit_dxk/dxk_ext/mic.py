from _module import *
def value(addr):
    return command(slot(addr), b'get_mic_val',2)