#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。


'''

# 生成1-10之间的平方的列表
print([x * x for x in range(1, 11)])

# 生成1-10之间偶数的平方的列表
print([x * x for x in range(1, 11) if x % 2 == 0])

# 双重循环嵌套，前面的循环在外层，后面的循环在内层
print([m + n for m in 'ABC' for n in 'XYZ'])

# 迭代dict并生成列表
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

# 生成全小写的列表
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
