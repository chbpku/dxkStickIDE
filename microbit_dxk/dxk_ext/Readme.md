# 模块调用库解决方案

## 文件内容

### 1. 烧录工具 (文件名：__*)

* __uflash.bat + __uflash.py  
    烧录python解释器至microbit

* __code.bat  
    (调用microfs库ufs命令)写入相关文件至microbit硬盘

### 2. microbit所需代码文件

* main.py  
    测试用代码，python解释器入口

* 其余  
    调用硬件模块的接口库

## 安装方式

1. 运行__uflash.bat

1. 编写主程序并命名为main.py

1. 运行__code.bat

1. 组装并运行硬件