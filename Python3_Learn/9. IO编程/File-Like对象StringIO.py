#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'StringIO顾名思义就是在内存中读写str'

from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
# getvalue()方法用于获得写入后的str。
print(f.getvalue())

# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
