# 精简库与普通库区别
1. 压缩了内核文件mb.py
    * 仅保留了必要的调用接口
    * 移除了对addr参数的匹配，需提前确定[接口位置](Document_addr.md)

1. 移除了不常用的功能
    * 移除了接口调用radio子节点功能，需手动发送radio指令

1. neo_color.py与neo_img.py接口更改
    * 除两个模块内setup函数以外所有函数将addr参数由末位挪至首位  
        例: neo_img.set_image_RGB  
        原接口: set_image_RGB(g, imgs, x=None, y=None, m=0, **addr=None**)  
        更改为: set_image_RGB(**addr**, g, imgs, x=None, y=None, m=0)