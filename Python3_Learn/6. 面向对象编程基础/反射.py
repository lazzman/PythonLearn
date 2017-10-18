#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性'y'
print('obj.y =', obj.y)  # 获取属性'y'

print('getattr(obj, \'z\') =', getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power')  # 获取属性'power'
print(f)
print(f())

'''
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
------------------------------
sum = obj.x + obj.y
------------------------------

就不要写：
------------------------------
sum = getattr(obj, 'x') + getattr(obj, 'y')
------------------------------

一个正确的用法的例子如下：
------------------------------
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
------------------------------

假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''
