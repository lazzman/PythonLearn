#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

对经常取指定索引范围的操作，用循环十分繁琐，Python提供了切片（Slice）操作符，能大大简化这种操作。
在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
有了切片操作，很多地方循环就不再需要了。Python的切片非常灵活，一行代码就可以实现很多行循环才能完成的操作。

'''

# 列表支持切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])  # 从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print('L[:3] =', L[:3])  # 同上
print('L[1:3] =', L[1:3])  # 从索引1开始取，直到索引3为止，但不包括索引3。即索引1，2，正好是2个元素。
print('L[-2:] =', L[-2:])  # 从倒数第2个元素开始取，到末尾为止

R = list(range(100))
print('R = ', R)
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])
R_copy = R[:]  # 复制原有列表元素
print('R_copy =', R_copy)

# 元组同样支持切片
tp = (0, 1, 2, 3, 4, 5)[:3]
print('tuple =', tp)

# 字符串也支持切片
st = 'ABCDEFG'[:3]
print('str =', st)

# 整数不支持
i = 123[:2]  # TypeError: 'int' object is not subscriptable
