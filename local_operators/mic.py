from _module import *
def get_mic_val(addr):
    return command(slot(addr), b'get_mic_val',2)