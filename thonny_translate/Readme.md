# Thonny主程序汉化

保存了汉化thonny模块所需的最少文件，基于Thonny 2.1.21 (7月31日pip install thonny)

汉化时直接覆盖入thonny package所在位置

## 内容：

### 菜单界面汉化

* thonny/workbench.py
    * 新增_translate_map对象与translate函数
    * 在add_command、add_view与get_menu函数内加入接口

### 设置界面汉化

* thonny/editor\_config_page.py
* thonny/font\_config_page.py
* thonny/general\_config_page.py
* thonny/interpreter\_config_page.py

## 待完成内容：

### 帮助文档汉化

* thonny/plugins/help/help.rst
    * 直接文本汉化