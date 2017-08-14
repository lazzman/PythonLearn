#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
反射讲解
1.根据字符串的形式导入模块。
2.根据字符串的形式去对象（某个模块）中操作其成员　
'''

# from list.text import commons
# __import__(' list.text.commons',fromlist=True) #如果不加上fromlist=True,只会导入list目录

moudleName = 'os'  # 字符串形式的模块名
modle = __import__(moudleName)  # 使用__import__函数导入

print modle.path

class Foo(object):
 
    def __init__(self):
        self.name = 'abc'
 
    def func(self):
        return 'ok'
 
obj = Foo()
# 获取成员
ret = getattr(obj, 'func')  # 获取的是个对象
r = ret()
print(r)
# 检查成员
ret = hasattr(obj, 'func')  # 因为有func方法所以返回True
print(ret)
# 设置成员
print(obj.name)  # 设置之前为:abc
ret = setattr(obj, 'name', 19)
print(obj.name)  # 设置之后为:19
# 删除成员
print(obj.name)  # abc
delattr(obj, 'name')
print(obj.name)  # 报错
