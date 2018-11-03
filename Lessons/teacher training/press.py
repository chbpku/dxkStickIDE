from microbit import *
import music

level = 0
lst = ["3", "2", "1", Image.TARGET]
while True:
    display.scroll(str(level))
    sleep(100)
    display.show(Image.ASLEEP)
    music.play(music.POWER_UP)
    display.show(lst, delay=200)
    button_a.was_pressed()
    button_b.was_pressed()
    sleep(1000 - level * 100)
    if button_a.was_pressed() and button_b.was_pressed():
        display.show(Image.HAPPY)
        music.play(music.JUMP_UP)
        level += 1
        if level >= 10:
            music.play(music.ENTERTAINER, wait=False, loop=True)
            display.scroll("MASTER!", loop=True)
            break
    else:
        display.show(Image.SKULL)
        music.play(music.WAWAWAWAA)
