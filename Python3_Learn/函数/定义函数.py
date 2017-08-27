#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# TypeError: bad operand type:
# my_abs('123')

# 默认参数 - 可变对象特殊情景
def defaultChangeParam(L=[]):
    L.append('END')
    return L


print(defaultChangeParam([123]))  # [123, 'END']
print(defaultChangeParam())  # ['END']
print(defaultChangeParam())  # ['END', 'END']
print(defaultChangeParam())  # ['END', 'END', 'END']
'''

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

'''
