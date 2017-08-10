#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib

'''
Created on 2017年4月11日
md5模块学习
@author: NodCat
'''
print '======================================='

md5 = hashlib.md5()  # 创建一个md5实例
md5.update('elifer')
print '返回一个对"elifer"的128bitmd5摘要：', md5.hexdigest()


