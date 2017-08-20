#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 转义字符
print('I\'m \"OK\"!', type('I\'m \"OK\"!'))

# 不转义字符
print(r"\n\d\t 都是转义字符", type(r"\n\d\t 都是转义字符"))

s = 'Python-中文'
print(s, type(s))

# unicode转换为utf-8编码的字节数组形式输出
b = s.encode('utf-8')
print(b, type(b))

# 将utf-8字节数组解码为unicode
print(b.decode('utf-8'))
