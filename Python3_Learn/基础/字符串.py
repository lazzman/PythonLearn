#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件

在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
'''

# 转义字符
print('I\'m \"OK\"!', type('I\'m \"OK\"!'))

# 不转义字符
print(r"\n\d\t 都是转义字符", type(r"\n\d\t 都是转义字符"))

# 输出多行文本
print("""
如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，可以自己试试：
>>> print('''line1
line2
line3''')
line1
line2
line3
""")

s = 'Python-中文'
print(s, type(s))

# unicode转换为utf-8编码的字节数组形式输出
b = s.encode('utf-8')
print(b, type(b))

# 将utf-8字节数组解码为unicode
print(b.decode('utf-8'))

# 获取单个字符编码
print(ord('h'))

# 获取编码对应的字符
print(chr(104))

# 可以使用unicode编码形式声明字符串
a = '\u4e2d\u6587'
print(a)

print("""
""")

# 声明字节类型
x = b'HELLO'
print(x, "类型：", type(x), "长度：", len(x))

# 修改单个字节
x_a = bytearray(x)
# x_a[0] = bytearray(b'h')[0] 等价于下面的形式
x_a[0] = 104
print(x_a, "类型：", type(x_a), "长度：", len(x_a))

# 声明字符串
y = 'hELLO你好'
print(y, "类型：", type(y), "长度：", len(y))

# UnicodeEncodeError 字符串中包含中文，使用ascii编码无法转换中文，所以报错
# z = y.encode('ascii')
z = y.encode("unicode-escape")  # unicode编码
print(z, "类型：", type(z), "长度：", len(z))

v = z.decode("unicode-escape")  # unicode解码
print(v, "类型：", type(v), "长度：", len(v))
