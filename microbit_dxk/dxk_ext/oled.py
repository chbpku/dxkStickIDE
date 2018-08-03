from _module import *
from microbit import sleep
def show(y,x,string,addr=None):
  if isinstance(string,str):
    command(slot(addr,1),b'DisplayGB2312,%d,%d,%s'%(y,x,string))
  else:
    command(slot(addr,1),b'DisplayGB2312,%d,%d,'%(y,x)+string)
  sleep(len(string))
def clear(addr=None):
  command(slot(addr,1),b'ClearScreen')
  sleep(10)
