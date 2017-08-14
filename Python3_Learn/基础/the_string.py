#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s)

# unicode转换为utf-8编码输出
b = s.encode('utf-8')
print(b)

# 将utf-8字符串解码为unicode
print(b.decode('utf-8'))
