#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
字符串处理
'''

if __name__ == '__main__':
    s = 'abcdefghijklmnopqrstuvwxyzcdghijklm'
    s2 = '哈哈哈哈呵呵呵'
    
    print('s.find()从左向右查找子串，返回第一个找到的子串的索引，否则返回-1   结果是：' + str(s.find('cd')))
    
    print('s.rfind()从右向左查找子串，返回第一个找到的子串的索引，否则返回-1   结果是：' + str(s.rfind('cd')))
    
    print('s.index()从左向右查找子串，返回子串的索引，否则抛出ValueError异常   结果是：' + str(s.index('cde')))
    
    print('s.rindex()从右向左查找子串，返回第一个找到的子串的索引，否则抛出ValueError异常   结果是：' + str(s.rindex('cd')))
    
    print('s.capitalize()返回一个首字母大写字符串的副本        结果是：' + str(s.capitalize()))
    
    print('s.lower()返回一个转为小写字符串的副本        结果是：' + str(s.lower()))
    
    print('s.upper()返回一个转为大写字符串的副本        结果是：' + str(s.upper()))
    
    print('s.swapcase()返回一个大小写互换字符串的副本        结果是：' + str(s.swapcase()))
    
    print('s.split()以参数分割，返回一个列表        结果是：' + str(s.split("cd")))
    
    print('len(str)返回str的字节长度        结果是：' + str(len(s2)))
    
    print('cmp(str1,str2)比较字符串，如果str1>str2，返回1 结果是：' + str(cmp(s, s2)))
    
    print('max("abcdefg")找出字符串中最大的字符   结果是：' + str(max(s)))

    print('min("abcdefg")找出字符串中最小的字符   结果是：' + str(min(s)))
    
    print "以unicode编码存储字符串(u'字符串'):", u'unicode'
    
    print "防止字符串转义(r'字符串')：", r'\t\n'
