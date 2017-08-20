#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 打印数字 0 - 9
for x in range(10):
    # 到7终止循环2
    if x == 7:
        break
    # 跳过5
    if x == 5:
        continue
    print(x)
else:
    print("else")


'''
range对象实现了__iter__方法，而list的构造方法可以传入一个可迭代对象来构造一个list对象
list(iterable) -> new list initialized from iterable's items
'''
a = range(1, 6)
print(type(a))
print(list(a))
