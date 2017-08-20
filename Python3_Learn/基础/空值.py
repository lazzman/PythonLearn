#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到。
'''

a = 0
b = None

print(a)

print(b)

# del 删除a引用
del (a)

print(a)
