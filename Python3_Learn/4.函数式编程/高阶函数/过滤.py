#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''


# 如果为奇数则返回True
def is_odd(n):
    return n % 2 == 1


L = range(100)

print(list(filter(is_odd, L)))


# 字符串不为空串|None|空格时返回True
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
