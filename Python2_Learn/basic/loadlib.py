#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
如果要引入其他模块，被引入模块所在的包必须含有__init__.py

一些常用系统常量
__name__ 是否为程序入口模块，即主文件 如果是主文件值应该为'__main__'
__file__ 当前文件路径
__doc__ 当前文件描述

python重复导包会自动优化，忽视重复的导包语句
'''

# import mylib
from basic import mylib # 首次导包
from basic import mylib # 再次导包会被优化，所以不会导入
reload(mylib)   # 强制重新导入包
if __name__ == '__main__':
    h = mylib.Hello()
    h.sayHello()

# from mylib import *
# 
# 
# if __name__ == '__main__':
#     h = Hello()
#     h.sayHello()