#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月10日

@author: NodCat
'''


print("===========三目运算============")
# 三元运算符
def sanyuan():
    temp = None
#     if 1>3:
#         temp = 'gt'
#     else:
#         temp = 'lt'
    temp = 'gt' if 1 > 3 else 'lt'  # 三元运算代替上面的if else
    return temp
    
print(sanyuan())


print("===========Lambda============")
# Lambda表达式
def mysum(x, y):
    return x + y
print(mysum(4, 5))

temp = lambda x, y:x + y  # 等价于上面的mysum，相当于创建了一个temp匿名函数
print(temp)
print(temp(4, 5))


