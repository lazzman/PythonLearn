#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月9日

@author: NodCat
'''
from StrStr_File_List_Tuple_Set_Dict_Copy_FuncpyOperation import a_list

# 创建一个list
a_lsit = [1,2,3,5,6,6,6,7,7,8,8,8,8,9]

# 创建一个set去重list
a_set = set(a_lsit)
print("===集合去重===")
print a_set

a_set = set([1,2,3,4])
b_set = set([3,4,5,6])
# 交集
print("===交集===")
print(a_set.intersection(b_set))

# 并集
print("===并集===")
print(a_set.union(b_set))

# 差集
print("===差集===")
print(a_set.difference(b_set))

# 对称差集
print("===对称差集===")
print(a_set.symmetric_difference(b_set))

# 是否是子集
print("===判断子集===")
print(a_set.issubset(b_set))

# 是否包含关系
print("===判断包含===")
print(a_set.issuperset(b_set))


