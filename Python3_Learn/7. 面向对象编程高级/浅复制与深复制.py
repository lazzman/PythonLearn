#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 默认做浅复制
l1 = [3, [55, 44], (7, 8, 9)]

l2 = list(l1)  # 通过构造方法进行复制
l2 = l1[:]  # 也可以这样想写
l2 == l1  # True
l2 is l1  # False
l2[1].append(33)
print(l1)  # [3, [55, 44, 33], (7, 8, 9)]

# 如何实现深复制
import copy

l1 = [3, [55, 44], (7, 8, 9)]

l2 = copy.copy(l1)  # 浅拷贝
l2 = copy.deepcopy(l1)  # 深拷贝
print(l2)  # [3, [55, 44, 33], (7, 8, 9)]
l2[1].append(33)
print(l1)  # [3, [55, 44, 33], (7, 8, 9)]
