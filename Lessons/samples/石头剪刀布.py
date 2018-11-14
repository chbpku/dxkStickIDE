# 无线通信石头剪刀布小游戏

# 简介：
# 两套micro:bit套件分别连接OLED显示屏与游戏手柄同时启动进行游戏
# 每轮游戏开始时会倒计时3秒，在5×5LED显示屏上显示，同时播放提示音
# 倒计时结束的一秒内，两个玩家按下游戏手柄右侧按键出拳
# 套件OLED显示屏上将显示玩家累计胜负情况及最近3局的胜负

# 硬件模块：
# micro:bit×2；主板×2；延长线×2
# 模块×4：OLED显示屏、游戏手柄

# 准备环境
from microbit import *
import radio, joypad, oled, music
from mb_radio import channel
radio.on()
radio.config(channel=channel())  # 通过拨码开关设置游戏频道

win_cond = ['ab', 'bc', 'ca']  # 胜过对方的出拳组合
input_map = {  # 出拳标记对应GB2312编码
    'a': b'\xca\xaf\xcd\xb7',  # "石头"
    'b': b'\xbc\xf4\xb5\xb6',  # "剪刀"
    'c': b' \xb2\xbc ',  # " 布 "
    'x': b'\xce\xb4\xb3\xf6'  # "未出"
}
res_map = [b'\xca\xa4', b'\xb8\xba', b'\xc6\xbd']  # 对局结果对应GB2312编码 (胜，负，平)
img_map = [Image.YES, Image.NO,
           Image('09990:90009:90009:90009:09990')]  # 对局结果对应LED屏显示图像 (胜，负，平)

res_pool = []  # 比赛记录列表
res_count = [0, 0, 0]  # 统计胜负用列表 (胜，负，平)


def show_log(data):
    '''输入(己方,对方,结果)三元组，输出对应对局记录'''
    self, other, result = data
    return input_map[self]+\
        b' vs '+\
        input_map[other]+\
        b', '+\
        res_map[result]


def check_result(self, other):
    '''输入己方、对方出拳标记，判断胜负、计入对局结果统计并返回对应下标'''
    if self == other:  # 平手
        res_count[2] += 1
        return 2
    if other == 'x' or self + other in win_cond:  # 己方胜
        res_count[0] += 1
        return 0
    # 己方负
    res_count[1] += 1
    return 1


display.show(Image.HAPPY)  # 开局前等待界面显示笑脸
while True:
    # 通过发送与接收'start'命令双方同步开局
    while radio.receive() != 'start':
        sleep(10)
        radio.send('start')
    for i in range(3, 0, -1):  # 倒计时三秒
        radio.send('start')
        music.pitch(440, 100, wait=0)
        display.show(i)
        time = running_time() + 1000
        while running_time() < time:
            radio.send('start')
            sleep(10)
    music.pitch(880, 100, wait=0)
    display.show(Image.TARGET)

    # 在一秒内接收第一个输入并重复发送己方出拳、接收对方出拳
    time, input, other = running_time() + 1000, 'x', 'x'
    while running_time() < time:
        if input == 'x':  # 等待己方输入
            tmp = joypad.keys()
            if tmp != None:
                if tmp[1]:
                    input = 'a'
                elif tmp[2]:
                    input = 'b'
                elif tmp[4]:
                    input = 'c'
        if other == 'x':  # 等待对方输入
            tmp = radio.receive()
            if tmp and tmp in 'xabc':  # 接收合法性判断
                other = tmp

        # 重复发送己方出拳
        radio.send(input)
        sleep(10)

    # 显示并记录当局结果
    time = running_time() + 2000  # 结果展示状态持续两秒
    res = check_result(input, other)  # 计算比赛结果
    display.show(img_map[res])
    res_pool.append((input, other, res))  # 保留至多3条比赛记录
    if len(res_pool) > 3:
        res_pool.pop(0)
    oled.clear()
    oled.show(0, 0, b'%2d\xca\xa4 %2d\xb8\xba %2d\xc6\xbd' %
              tuple(res_count))  # 第一行显示累计对局结果
    for i in range(len(res_pool)):  # 显示最近至多3条比赛记录
        oled.show(2 * i + 2, 0, show_log(res_pool[i]))
    while running_time() < time:  # 比赛结果显示保留2秒
        sleep(10)