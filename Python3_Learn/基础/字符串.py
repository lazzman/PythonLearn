#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
