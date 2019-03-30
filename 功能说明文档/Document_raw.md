# dxkStick 开发者文档
## 模块：clock
1. ### time(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
1. ### set_time(Y, M, D, h, m, s, addr=None)
    #### 参数:
    - Y: 
    - M: 
    - D: 
    - h: 
    - m: 
    - s: 
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：joypad
1. ### conv(data)
    #### 参数:
    - data: 
    #### 返回值: 
1. ### values(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
1. ### keys(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
1. ### stickxy(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
1. ### stick_directions(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：led
1. ### on(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
1. ### off(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：light
1. ### value(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：mb
1. ### remote_on(short=1)
    #### 参数:
    - short(默认为1): 
    #### 返回值: 
1. ### _exe(s, b, l, r)
    #### 参数:
    - s: 
    - b: 
    - l: 
    - r: 
    #### 返回值: 
1. ### command(slot, bseq, size=0, raw=False)
    #### 参数:
    - slot: 
    - bseq: 
    - size(默认为0): 
    - raw(默认为False): 
    #### 返回值: 
1. ### get_state(addr)
    #### 参数:
    - addr: 
    #### 返回值: 
1. ### get_type(addr)
    #### 参数:
    - addr: 
    #### 返回值: 
1. ### get_id(addr)
    #### 参数:
    - addr: 
    #### 返回值: 
1. ### slot(addr, type=None)
    #### 参数:
    - addr: 
    - type(默认为None): 
    #### 返回值: 
1. ### get_bin()
    #### 参数: 无
    #### 返回值: 
1. ### refresh(p)
    #### 参数:
    - p: 
    #### 返回值: 
---
## 模块：mb_node
1. ### show(img, grp=-1)
    #### 参数:
    - img: 
    - grp(默认为-1): 
    #### 返回值: 
1. ### scroll(text, wait=0, grp=-1)
    #### 参数:
    - text: 
    - wait(默认为0): 
    - grp(默认为-1): 
    #### 返回值: 
1. ### button(btn, grp=-1)
    #### 参数:
    - btn: 
    - grp(默认为-1): 
    #### 返回值: 
1. ### play(mid, wait=0, grp=-1)
    #### 参数:
    - mid: 
    - wait(默认为0): 
    - grp(默认为-1): 
    #### 返回值: 
---
## 模块：mb_radio
1. ### channel()
    #### 参数: 无
    #### 返回值: 
1. ### group()
    #### 参数: 无
    #### 返回值: 
1. ### _send(bytes, to_int)
    #### 参数:
    - bytes: 
    - to_int: 
    #### 返回值: 
1. ### send(id, bseq, size, to_int)
    #### 参数:
    - id: 
    - bseq: 
    - size: 
    - to_int: 
    #### 返回值: 
1. ### r_eval(seq, grp=-1)
    #### 参数:
    - seq: 
    - grp(默认为-1): 
    #### 返回值: 
---
## 模块：mic
1. ### value(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：neo_color
1. ### setup(grps, addr=None)
    #### 参数:
    - grps: 
    - addr(默认为None): 
    #### 返回值: 
1. ### set_pixel(g, pos, c, addr=None)
    #### 参数:
    - g: 
    - pos: 
    - c: 
    - addr(默认为None): 
    #### 返回值: 
1. ### set_pixel_range(g, pos, cs, addr=None)
    #### 参数:
    - g: 
    - pos: 
    - cs: 
    - addr(默认为None): 
    #### 返回值: 
1. ### set_xy(g, x, y, c, addr=None)
    #### 参数:
    - g: 
    - x: 
    - y: 
    - c: 
    - addr(默认为None): 
    #### 返回值: 
1. ### fill(g, c, addr=None)
    #### 参数:
    - g: 
    - c: 
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：neo_img
1. ### setup(grps, addr=None)
    #### 参数:
    - grps: 
    - addr(默认为None): 
    #### 返回值: 
1. ### set_image(g, img, x=None, y=None, m=0, addr=None)
    #### 参数:
    - g: 
    - img: 
    - x(默认为None): 
    - y(默认为None): 
    - m(默认为0): 
    - addr(默认为None): 
    #### 返回值: 
1. ### set_image_RGB(g, imgs, x=None, y=None, m=0, addr=None)
    #### 参数:
    - g: 
    - imgs: 
    - x(默认为None): 
    - y(默认为None): 
    - m(默认为0): 
    - addr(默认为None): 
    #### 返回值: 
1. ### shift(g, x, y=0, addr=None)
    #### 参数:
    - g: 
    - x: 
    - y(默认为0): 
    - addr(默认为None): 
    #### 返回值: 
1. ### set_rainbow(g, t, x, n, addr=None)
    #### 参数:
    - g: 
    - t: 
    - x: 
    - n: 
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：oled
1. ### show(y, x, string, addr=None)
    #### 参数:
    - y: 
    - x: 
    - string: 
    - addr(默认为None): 
    #### 返回值: 
1. ### clear(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：poten
1. ### value(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：temp_humi
1. ### temp(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
1. ### humi(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
1. ### temp_humi(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：touch
1. ### get(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
---
## 模块：ultrasonic
1. ### value(addr=None)
    #### 参数:
    - addr(默认为None): 
    #### 返回值: 
---
