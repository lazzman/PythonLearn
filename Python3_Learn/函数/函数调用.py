#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

Python内置了很多有用的函数，我们可以直接调用。

要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：

http://docs.python.org/3/library/functions.html#abs

也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。

'''

x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

'''
数据类型转换
'''
# 字符串转整数
print(int('123'))
# 浮点数转整数
print(int(12.34))
# 字符串转浮点数
print(float('12.34'))
# 小数转字符串
print(str(1.23))
# 整数转字符串
print(str(100))
# 整数转布尔
print(bool(1))
# 字符串转布尔
print(bool(''))
