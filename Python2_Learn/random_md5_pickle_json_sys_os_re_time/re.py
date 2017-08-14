#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月11日
re模块 ——正则表达式操作
@author: NodCat
'''

import re

print '==========mathch============'

# match 从字符串开头就开始匹配，匹配成功返回match对象，失败则返回None
# Try to apply the pattern at the start of the string, returning a match object, or None if no match was found
match1 = re.match('\d+', 'abc123def456g') 
print match1
if match1:
    print match1.group()


print '==========search============'

# search 匹配整个字符串，找出第一个匹配的部分返回一个match对象，匹配不到则返回None
# Scan through string looking for a match to the pattern, returning a match object, or None if no match was found.
match2 = re.search('\d+', 'abc123def456g')
print match2
if match2:
    print match2.group()

print '==========findall============'
# search 匹配整个字符串，找出所有匹配的字符串返回一个列表
# Return a list of all non-overlapping matches in the string.
match3 = re.findall('\d+', 'abc123def456g')
print match3

print '==========complie============'
# compile 将正则表达式先编译再去匹配，可以提高效率；后面可以直接使用编译的正则对象去匹配字符串
# Compile a regular expression pattern, returning a pattern object.
re_complile = re.compile('\d+')
match4 = re_complile.findall('abc123def456g')
print match4

print '==========分组============'
match5 = re.findall('(\d+)\w*(\d+)','abc123def456g')
print match5
match6 = re.search('(\d+)\w*(\d+)','abc123def456g')
if match6:
    print match6.group()
    print match6.groups()


'''
1.(...)用来匹配字符串中符合（）内规则的子串，匹配的字符串被看成是一个组；
2.接上，这个组可以被后续引用，引用的方式是\N,N是这个组对应的编号；
3.接上，编号是0的组始终代表匹配的是整个字符串，所以正则表达式里的组编号从1开始；
既然（）有如此的功能，我们在正则表达式中匹配‘（’和‘）’，要用‘\’对其转义；
groups（）：表示从group（1）开始往后的所有值，组合成一个元组类型的值；
group（）：表示取全部匹配的字符串或者指定的组，返回结果是一个字符串；
'''









