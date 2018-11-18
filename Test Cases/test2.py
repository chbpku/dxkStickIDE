# 模块接口测试1
# 简介：
# 分别插入两组模块后，将分别调用不同的测试程序测试所有的模块接口
# 硬件模块：
# micro:bit×1；主板×1
# 模块×4：（组1）光敏电阻、超声测距；（组2）游戏手柄、麦克风

# 分组1
# 测试对象：
# 光敏电阻、超声测距、蜂鸣器（主板）
# 内容：
# micro:bit显示屏前两列将显示光敏电阻读数，后三行将显示超声测距读数
# 同时蜂鸣器将根据超声测距远近发出不同频率的声音
# 改变光敏电阻接收光强及超声测距距离以测试其功能

# 分组2
# 测试对象：
# 游戏手柄、麦克风
# 内容：
# micro:bit显示屏将在不同位置显示游戏手柄摇杆位置、各按键按下情况，及麦克风接收声音大小
# 使用游戏手柄及发出声音以进行测试

from microbit import *
from mb import get_type,refresh
ta,tb=0,0
display.clear()
while 1:
	refresh(0);refresh(1)
	ta=get_type(22)
	if ta:
		for i in (0,1):
			for j in range(5):
				display.set_pixel(i,j,9)
	else:
		for i in (0,1):
			for j in range(5):
				display.set_pixel(i,j,0)
	tb=get_type(23)
	if tb:
		for i in (0,1):
			for j in range(5):
				display.set_pixel(i+3,j,9)
	else:
		for i in (0,1):
			for j in range(5):
				display.set_pixel(i+3,j,0)
	if ta==None or tb==None:
		continue
	if ta>tb:
		ta,tb=tb,ta
	if ta==5 and tb==8:
		# 测试光照、超声波（延长）
		import light,ultrasonic,music
		counter=0
		while not (button_a.get_presses()+button_b.get_presses()):
			display.clear()
			l,u=light.value(),ultrasonic.value()
			for i in range(10):
				if l>=410:
					display.set_pixel(i%5,i//5,9)
					l-=410
				else:
					display.set_pixel(i%5,i//5,int(9*l/410))
					break
			music.pitch(1000-2*u,50,wait=0)
			for i in range(15):
				if u>=10:
					display.set_pixel(i%5,2+i//5,9)
					u-=10
				else:
					display.set_pixel(i%5,2+i//5,int(9*u/10))
					break
			sleep(100)
		break
	elif ta==6 and tb==7:
		# 测试声音、手柄（延长）
		import mic,joypad
		while not (button_a.get_presses()+button_b.get_presses()):
			display.clear()
			keys,stick=joypad.values()
			for i in range(5):
				display.set_pixel(i,0,9*keys[i])
			x=max(0,min(4,2+round(stick[0]/1000)))
			y=max(0,min(4,2+round(stick[1]/1000)))
			display.set_pixel(x,4,9)
			display.set_pixel(4,y,9)
			m=mic.value()
			for i in range(12):
				if m>=30:
					display.set_pixel(i%4,i//4+1,9)
					m-=30
				else:
					display.set_pixel(i%4,i//4+1,int(9*m/30))
					break
			sleep(50)
		break
	else:
		sleep(10)
display.clear()