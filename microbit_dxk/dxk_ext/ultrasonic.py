from _module import *
def get_distance_val(addr):
    return command(slot(addr), b'get_distance_val',2)