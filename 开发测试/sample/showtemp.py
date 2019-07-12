from microbit import *
port_A = 0x16
port_B = 0x17

def get_temp(slot):
    i2c.write(slot, b'get_temp')
    b= i2c.read(slot, 1)
    v= int.from_bytes(b, 'big')
    return v

def get_poten(slot):
    i2c.write(slot, b'get_poten_val')
    b= i2c.read(slot, 2)
    v= int.from_bytes(b, 'big')
    return v

def show(slot, r, c, s):
    v= b'DisplayGB2312,%d,%d,%s   ' % (r, c, s)
    i2c.write(slot, v)
    sleep(50)
    return

c = 0
while True:
    t = get_poten(port_B)
    show(port_A, 2, 10, 'POTEN: %s C' % t)
    show(port_A, 4, 80, c)
    sleep(2000)
    c+= 1
