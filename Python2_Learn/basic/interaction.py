#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
用户交互练习
'''
# 声明一个词典
userDict = dict()

# 高亮输出    格式：\033[显示方式;前景色;背景色m
print("\033[1;31;40m 高亮输出 \033[1;31;40m")

# 获取用户输入
name = raw_input('Please input your name: ')

age = raw_input('Please input your age: ')

userDict['name'] = name

userDict['age'] = age

# 格式化输出
print('''
    Name:    %s
    Age:     %s
''' %(name,age))

