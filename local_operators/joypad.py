from _module import *
def get_key_val(addr):
    data=command(slot(addr), b'get_key_val',9,True)
    return tuple(data[:5]),(data[5]*256+data[6],data[7]*256+data[8])