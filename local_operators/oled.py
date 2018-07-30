from _module import *
def display_text(addr,y,x,string):
    command(slot(addr), b'DisplayGB2312,%d,%d,%s'%(y,x,string))
def clear(addr):
    command(slot(addr), b'ClearScreen')
