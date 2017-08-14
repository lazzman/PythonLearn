#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

'''
Created on 2017年4月11日
random模块学习
@author: NodCat
'''
print '======================================='
print '返回一个0-1之间的浮点数：', random.random()

print '返回一个指定区间的整数：', random.randint(1, 5)  # [1,5]区间

print '返回一个左开右闭区间的整数：', random.randrange(1, 3)  # [1,3)区间

print '======================================='

print '随机生成一个字母：', chr(random.randint(65, 90))

print '======================================='

code = ""
for i in range(6):
    code = code + chr(random.randint(65, 90))
                      
print '随机生成6位字母验证码：', code
