#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。

为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。
假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
你可以猜到，这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。
'''

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 67
print("dict =", d)

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Adam'] = 69
print("dict =", d)

# 如果key不存在，dict就会报错 KeyError: 'name'
# print(d['name'])

'''
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在 因为dict实现了__contains__方法，所以可以使用in来判断
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
注意：返回None的时候Python的交互式命令行不显示结果。
'''
print("dict have name?", "name" in d)
print("dict.get(key,defaultValue)", d.get("name"))
print("dict.get(key,defaultValue)", d.get("name", "没有找到"))
