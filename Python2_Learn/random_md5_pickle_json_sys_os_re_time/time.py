#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月13日
日期时间模块详解
@author: NodCat
'''

'''
time的三种表现形式：
1. 时间戳  1970年1月1日的秒数    time.time()
2. 元组 包含了：年、月、日、星期等... time.struct_time
3. 格式化的字符串：2017-04-19 12:00 
'''

print '===============time=============='

import time
# 1、时间戳    1970年1月1日之后的秒
# 3、元组 包含了：年、日、星期等... time.struct_time
# 4、格式化的字符串    2014-11-11 11:11
 
print 'time.time() 返回时间戳形式：', time.time()

# 时间戳转元组
print '时间戳转元组：', time.gmtime()  # 可加时间戳参数
# 时间戳转元组
print '时间戳转元组：', time.localtime()  # 可加时间戳参数
# 元组转时间戳
print '元组转时间戳：', time.mktime(time.localtime())  # 可加元组形式时间参数
# 字符串转元组
print '字符串转元组：', time.strptime('2014-11-11', '%Y-%m-%d')
# 元组转字符串【常用】
print '元组转字符串：', time.strftime('%Y-%m-%d %H:%M:%S')  # 默认当前时间，可追加元组时间参数
print '元组转字符串：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 默认当前时间
# 英文时间格式
print '英文时间格式', time.asctime()
print '英文时间格式', time.asctime(time.localtime())
print '英文时间格式', time.ctime(time.time())


print '=============datatime================'

import datetime
'''
datetime.date：表示日期的类。常用的属性有year, month, day
datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond
datetime.datetime：表示日期时间
datetime.timedelta：表示时间间隔，即两个时间点之间的长度
timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
strftime("%Y-%m-%d")
'''

print datetime.datetime.now()
print datetime.datetime.now() - datetime.timedelta(days=5)
