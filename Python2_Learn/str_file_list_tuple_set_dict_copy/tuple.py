#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月9日
说白了，元组就是常量列表，元素不可更改
@author: NodCat
'''

# 声明一个元组
a_tuple = (1,2,3,4,5)
print('tuple: ' + str(a_tuple))

# 列表转为元组
a_list = range(10)
b_tuple = tuple(a_list)
print('tuple: ' + str(b_tuple))

# 元组转列表
b_list = list(b_tuple)
print('list: ' + str(b_list))

