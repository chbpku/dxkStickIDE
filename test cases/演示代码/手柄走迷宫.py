# 手柄走迷宫
# 简介：
# 由MicroPython示例代码之一改编；玩家在一个迷宫中（显示在micro:bit显示屏内），通过游戏手柄左摇杆的控制可以在迷宫内行走。
# 硬件模块：
# micro:bit×1；主板×1；延长插槽×1
# 模块×1：游戏手柄

import microbit
import joypad  # 模块控制库

d = microbit.display

# 迷宫路线
maze = [
    0b0000000000000000,
    0b0100010101011110,
    0b0100010101010010,
    0b0111110100000000,
    0b0000000111111110,
    0b0111111101000000,
    0b0101010001011100,
    0b0101000100000100,
    0b0100011111111100,
    0b0101010001000110,
    0b0101000100010010,
    0b0101010111010110,
    0b0111010101010010,
    0b0000010100010010,
    0b0111110111111110,
    0b0000000000000000,
]


# 获取迷宫指定坐标是否为墙
def get_maze(x, y):
    if 0 <= x < 16 and 0 <= y < 16:
        return (maze[y] >> (15 - x)) & 1
    else:
        return 1


# 绘制迷宫
def draw(x, y, tick):
    img = microbit.Image(5, 5)
    for j in range(5):
        for i in range(5):
            img.set_pixel(i, j, get_maze(x + i - 2, y + j - 2) * 5)

    # 绘制闪烁的玩家
    img.set_pixel(2, 2, (tick & 1) * 4 + 5)
    d.show(img)


def main():
    x = 0
    y = 0
    tick = 0
    while True:
        tick += 1
        if tick == 4:
            # 根据手柄摇杆输入进行移动
            tick = 0
            sx = joypad.stickxy()
            if sx != None:
                sx, sy = sx
                if sx > 1500 and get_maze(x + 1, y) == 0:
                    x += 1
                elif sx < -1500 and get_maze(x - 1, y) == 0:
                    x -= 1
                if sy > 1500 and get_maze(x, y + 1) == 0:
                    y += 1
                elif sy < -1500 and get_maze(x, y - 1) == 0:
                    y -= 1
            x = min(15, max(0, x))
            y = min(15, max(0, y))

        # 绘制迷宫
        draw(x, y, tick)
        microbit.sleep(50)


main()
