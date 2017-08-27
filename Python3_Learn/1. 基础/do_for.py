#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
推荐使用enumerate包装迭代对象，因为enumerate使用了生成器yield
并且enumerate还提供了计数器
enumerate(iterable[, start]) -> iterator for index, value of iterable

    Return an enumerate object.  iterable must be another object that supports
    iteration.  The enumerate object yields pairs containing a count (from
    start, which defaults to zero) and a value yielded by the iterable argument.
    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

enumerate当然也实现了__iter__方法
'''
# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for i, name in enumerate(names):
    print(i, name)

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
