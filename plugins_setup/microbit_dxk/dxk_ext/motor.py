from mb import command,slot,gc
def motor(val,addr=None):
    return command(slot(addr,20),b'get%s%c'%('bf'[val>0],abs(val)//4))
gc()