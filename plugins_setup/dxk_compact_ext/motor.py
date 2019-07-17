from mb import _exe as C,gc
def motor(val,addr):
    return C(addr,b'get%s%c'%('bf'[val>0],abs(val)//4))
gc()