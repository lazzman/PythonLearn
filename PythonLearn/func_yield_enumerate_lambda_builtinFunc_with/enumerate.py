#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月13日

enumerate()是python的内置函数
enumerate在字典上是枚举、列举的意思
对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
enumerate多用于在for循环中得到计数

@author: NodCat
'''

# 如果对一个列表，既要遍历索引又要遍历元素时，首先可以这样写：
list1 = ["这", "是", "一个", "测试"]
for i in range (len(list1)):
    print i , list1[i]
    
print '===================================='    

# 上述方法有些累赘，利用enumerate()会更加直接和优美：
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print index, item

print '===================================='    

# enumerate还可以接收第二个参数，用于指定索引起始值，如：
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1, 1):
    print index, item

print '===================================='  
# 如果要统计文件的行数，可以这样写：
count = len(open('../res/dump_json.txt', 'r').readlines())
print count

# 这种方法简单，但是可能比较慢，当文件比较大时甚至不能工作。
# 可以利用enumerate()：
count = 0
for index, line in enumerate(open('../res/dump_json.txt','r')):
    print index,line
    count += 1
print count

