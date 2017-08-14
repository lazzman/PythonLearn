#!/usr/bin/python
# -*- coding: UTF-8 -*-

import copy

'''
Created on 2017年4月9日

# 深拷贝与浅拷贝

所有集合实现的copy方法都是浅拷贝，意味着当调用copy方法时，只会复制第一层基本类型值，当第一层含有对象或者集合时，copy并不会复制一个新的对象或集合，仅仅会复制其引用，类似java中的clone
深拷贝则会将每一层都复制一个新的副本，不管有多少层对象包含关系
实现深copy需要引入copy模块
copy中包含了deepcopy()方法

@author: NodCat
'''

# 浅拷贝
print("===浅拷贝范例===")
a_list = [1,2,3,4,5,[6,7,8]]
b_list = copy.copy(a_list)  
print(id(a_list))
print(id(b_list))
print(id(a_list[5]))
print(id(b_list[5]))

# 深拷贝
print("===深拷贝范例===")
a_list = [1,2,3,4,5,[6,7,8]]
b_list = copy.deepcopy(a_list)
print(id(a_list))
print(id(b_list))
print(id(a_list[5]))
print(id(b_list[5]))
