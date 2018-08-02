from _module import *
def values(addr):
    data=command(slot(addr), b'get_key_val',9,True)
    return tuple(data[:5]),(data[5]*256+data[6],data[7]*256+data[8])
def keys(addr):
    return values(addr)[0]
def stickxy(addr):
    return values(addr)[1]