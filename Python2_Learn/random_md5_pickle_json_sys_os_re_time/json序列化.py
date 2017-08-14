#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月11日
json的序列化与反序列化
@author: NodCat
'''

import json

user = ['alex', 11, 'male']

print '=========================================='

print type(user.__class__)  # user.__class__ 获取user的类型

user_dumps = json.dumps(user)  # 序列化

print '序列化：', user_dumps

user_loads = json.loads(user_dumps)  # 反序列化

print '反序列化：', user_loads

print '=========================================='

user = {'name':'elifer', 'age':20}

json.dump(user, open('../res/dump_json.txt', 'w'))  # 序列化置文件中

result = json.load(open('../res/dump_json.txt', 'r'))  # 从文件中反序列化

print '从文件中反序列化：', result




