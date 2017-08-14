#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月11日
sys模块常用函数介绍
@author: NodCat
'''

import sys


print sys.argv  # 命令行参数List，第一个元素是程序本身路径
print sys.version  # 获取Python解释程序的版本信息
print sys.maxint  # 最大的Int值
print sys.maxunicode  # 最大的Unicode值
print sys.path  # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print sys.platform  # 返回操作系统平台名称
print sys.getfilesystemencoding()  # 获取文件系统编码
sys.stdout.write('please:')  # 控制台输出
val = sys.stdin.readline()[:-1]  # 控制台输入([:-1]其实就是去除了这行文本的最后一个字符(换行符)后剩下的部分)
print val
sys.exit(0)  # 退出程序，正常退出时exit(0)
