#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
# getvalue()方法用于获得写入后的str。
print(f.getvalue())

# read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)  # 等价于f = BytesIO() f.write('中文'.encode('utf-8'))
print(f.read())
