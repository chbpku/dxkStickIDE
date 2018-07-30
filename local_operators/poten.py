from _module import *
def get_poten_val(addr):
    return command(slot(addr), b'get_poten_val',2)