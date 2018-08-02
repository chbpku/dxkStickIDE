from _module import *
def value(addr):
    return command(slot(addr), b'get_distance_val',2)