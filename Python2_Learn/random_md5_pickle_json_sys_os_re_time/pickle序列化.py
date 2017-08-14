#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月11日
类似java的序列化，将对象转为序列化字符串，可以将字符串再反序列化为原对象
@author: NodCat
'''

import pickle

user = ['alex', 11, 'male']

print '=========================================='

print type(user.__class__)  # user.__class__ 获取user的类型

user_dumps = pickle.dumps(user)  # 序列化

print '序列化：', user_dumps

user_loads = pickle.loads(user_dumps)  # 反序列化

print '反序列化：', user_loads

print '=========================================='

user = {'name':'elifer', 'age':20}

pickle.dump(user, open('../res/dump_pickle.txt', 'w'))  # 序列化置文件中

result = pickle.load(open('../res/dump_pickle.txt', 'r'))  # 从文件中反序列化

print '从文件中反序列化：', result




