#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'一个类定义了__getitem__方法后，就可被for迭代或者切片'


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[0])
print(f[5])
print(f[100])
print(f[0:5])
print(f[:10])

# 注意无限循环输出
for i in f:
    print(i)
