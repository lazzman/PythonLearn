#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
    return x * x

'''
Python内建了map()和reduce()函数。

如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。

我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回，
Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
'''
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
