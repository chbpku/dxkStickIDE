from _module import *
def get_temp(addr):
    return command(slot(addr), b'get_temp',1)
def get_humi(addr):
    return command(slot(addr), b'get_humi',1)
def get_temp_humi(addr):
    res=command(slot(addr), b'get_temp_humi',2)
    return res//256,res%256