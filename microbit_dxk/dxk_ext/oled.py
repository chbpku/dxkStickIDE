from _module import *
def show(addr,y,x,string):
    if isinstance(string,str):
        command(slot(addr), b'DisplayGB2312,%d,%d,%s'%(y,x,string))
    else:
        command(slot(addr), b'DisplayGB2312,%d,%d,'%(y,x)+string)
def clear(addr):
    command(slot(addr), b'ClearScreen')
