from microbit import *
import microbit
#-- constants --
port_A = 0x16
port_B = 0x17
class Module:
    def __init__(self, port):
        self.port = port
        self.type = 0
        self.id = 0
        self.status = 0
types = {1:'OLED', 2:'Temp', 3:'LED', 4:'Poten', 5:'Light', 6:'Mic', 7:'Hand', 8:'Ultra'}
A = Module(port_A)
microbit.i2c.write(A.port, b'get_type')
A.type =  types[int.from_bytes(microbit.i2c.read(A.port, 1), 'big')]
microbit.i2c.write(A.port, b'get_id')
A.id = microbit.i2c.read(A.port, 16)
microbit.i2c.write(A.port, b'get_state')
A.status = microbit.i2c.read(A.port, 1)
B = Module(port_B)
microbit.i2c.write(B.port, b'get_type')
B.type =  types[int.from_bytes(microbit.i2c.read(B.port, 1), 'big')]
microbit.i2c.write(B.port, b'get_id')
B.id = microbit.i2c.read(B.port, 16)
microbit.i2c.write(B.port, b'get_state')
B.status = microbit.i2c.read(B.port, 1)
type=0
state=0
val1=0
val2=0
while True:
    for M in (A, B):
        if M.type != 'OLED':
            microbit.i2c.write(M.port, b'get_state')
            state = int.from_bytes(microbit.i2c.read(M.port, 1), 'big')
        if M.type == 'LED':
            type = 'led'        
            microbit.i2c.write(M.port, b'set_led_on')
            sleep(100)
            microbit.i2c.write(M.port, b'set_led_off')
            sleep(100)
        if M.type == 'Temp':
            type = 'temp'
            microbit.i2c.write(M.port, b'get_temp')
            val1 = 'temp:%04d'%int.from_bytes(microbit.i2c.read(M.port, 1), 'big')
            microbit.i2c.write(M.port, b'get_humi')
            val2 = 'humi:%04d'%int.from_bytes(microbit.i2c.read(M.port, 1), 'big')
        if M.type == 'Poten':
            type = 'poten'
            microbit.i2c.write(M.port, b'get_poten_val')
            val1 = 'poten:%04d'%int.from_bytes(microbit.i2c.read(M.port, 2), 'big')
        if M.type == 'Light':
            type = 'light'
            microbit.i2c.write(M.port, b'get_light_val')
            val1 = 'light:%04d'%int.from_bytes(microbit.i2c.read(M.port, 2), 'big')
        if M.type == 'Mic':
            type = 'mic'  
            microbit.i2c.write(M.port, b'get_mic_val')
            val1 = 'mic:%04d'%int.from_bytes(microbit.i2c.read(M.port, 2), 'big')
        if M.type == 'Hand':
            type = 'hand'
            i2c.write(port_B, b'get_key_val')
            s=i2c.read(port_B,9)
            val1 = 'button:%1d %1d %1d %1d %1d'%(s[0],s[1],s[2],s[3],s[4])
            val2 = 'handle:%4d %4d'%(int.from_bytes(s[5:7],'big'),int.from_bytes(s[7:],'big'))
        if M.type == 'Ultra':
            type = 'ultra'
            microbit.i2c.write(M.port, b'get_distance_val')
            val1 = 'distance:%04d'%int.from_bytes(microbit.i2c.read(M.port, 2), 'big')
        if M.type == 'OLED':
            #microbit.i2c.write(M.port, b'ClearScreen')
            microbit.i2c.write(M.port, b'DisplayGB2312,0,0,type:%s'%type)
            microbit.i2c.write(port_A, b'DisplayGB2312,2,0,state:%s'%state)
            microbit.i2c.write(M.port, b'DisplayGB2312,4,0,%s'%val1)
            #microbit.i2c.write(M.port, b'DisplayGB2312,6,0,%s'%val2)          
            