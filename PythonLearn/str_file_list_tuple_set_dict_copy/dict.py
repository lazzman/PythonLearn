#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月9日
类似java中的HashMap
@author: NodCat
'''

# 声明一个字典
a_dict = dict({1:'a', 2:'b'})
print('dict: ' + str(a_dict))
b_dict = {"a":1, "b":2, "c":3}
print('dict: ' + str(b_dict))

# 查找key对应的value
a_dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'c'}
value = a_dict[2]
print('dict[key]: ' + str(value))

# 根据key查找value。如果value不存在则返回默认值;如果value不存在又没有传入默认值则抛异常
value = a_dict.get(6, 'e')
print('dict.get(key,default): ' + str(value))

# 判断key是否存在
flag = a_dict.has_key(6)
print('dict.has_key(key): ' + str(flag))

# 返回dict的key的列表
keys = a_dict.keys()
print('dict.keys(): ' + str(keys))

# 返回dict的value的列表
values = a_dict.values()
print('dict.values(): ' + str(values))

# 返回dict中的键值对的列表形式
entrys = a_dict.items()
print('dict.items(): ' + str(entrys))

# 字典合并，重复的key对应的value会被覆盖
a_dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'c'}
b_dict = {4:'4', 6:'e', 7:'f'}
a_dict.update(b_dict)
print('dict.update(): ' + str(a_dict))

# 从字典中返回一个键值对，如果字典已空则抛异常
entry = a_dict.popitem()
print('dict.popitem(): ' + str(entry) + ' 原字典： ' + str(a_dict))

# 清空字典
a_dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'c'}
a_dict.clear()
print('dict.clear(): ' + str(a_dict))

# 拷贝字典
a_dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'c'}
b_dict = a_dict.copy()
print('dict.copy(): ' + str(b_dict))

# 字典的比较(优先级为元素个数、键大小、键值大小)，第一大返回1，小则返回-1，一样则返回0
value = cmp(a_dict, b_dict)
print('cmp(dictA,dictB): ' + str(value))








