#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 指示使用ListMetaclass来定制类
class MyList(list, metaclass=ListMetaclass):
    pass

'''
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：

    1. 当前准备创建的类的对象；
    
    2. 类的名字；
    
    3. 类继承的父类集合；
    
    4. 类的方法集合。
'''

L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)
