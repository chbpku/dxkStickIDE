import mb,mb_node,led
from microbit import *
import music
mb.remote_on()
counter=0
imap=Image(5,5)
flag=1
while 1:
    x=mb_node.button('a')
    if x:
        x=x[0][0]
        for i in range(x):
            i,j=counter%5,counter//5
            imap.set_pixel(i,j,9-imap.get_pixel(i,j))
            counter=(counter+1)%25
        mb_node.show(repr(imap)[7:-2])
        display.show(imap)
    y=mb_node.button('b')
    if y and y[0][0]:
        if flag:
            led.on()
            sleep(10)
            mb_node.play('POWER_UP')
        else:
            led.off()
            sleep(10)
            mb_node.play('POWER_DOWN')
        flag=not flag