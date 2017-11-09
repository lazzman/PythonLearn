#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Python中3种方式定义类方法, 常规方式, @classmethod修饰方式, @staticmethod修饰方式.'


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()

# 1.定义方式
'''
普通的类方法foo()需要通过self参数隐式的传递当前类对象的实例。 @classmethod修饰的方法class_foo()需要通过cls参数传递当前类对象。@staticmethod修饰的方法定义与普通函数是一样的。

self和cls的区别不是强制的，只是PEP8中一种编程风格，slef通常用作实例方法的第一参数，cls通常用作类方法的第一参数。即通常用self来传递当前类对象的实例，cls传递当前类对象。
'''

# 2.绑定对象
print(a.foo)  # <bound method A.foo of <__main__.A object at 0x000001C33A68C240>>
print(a.class_foo)  # <bound method A.class_foo of <class '__main__.A'>>
print(a.static_foo)  # <bound method A.class_foo of <class '__main__.A'>>
# foo方法绑定对象A的实例，class_foo方法绑定对象A，static_foo没有参数绑定。

# 3.调用方式
'''
foo可通过实例a调用，类对像A直接调用会参数错误。
-------------------------------------
>>> a.foo(1)
executing foo(<__main__.A object at 0x0278B170>,1)
self: <__main__.A object at 0x0278B170>
>>> A.foo(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() missing 1 required positional argument: 'x'
-------------------------------------

但foo如下方式可以使用正常，显式的传递实例参数a。
-------------------------------------
>>> A.foo(a, 1)
executing foo(<__main__.A object at 0x0278B170>,1)
self: <__main__.A object at 0x0278B170>
-------------------------------------

class_foo通过类对象或对象实例调用。
-------------------------------------
>>> A.class_foo(1)
executing class_foo(<class '__main__.A'>,1)
cls: <class '__main__.A'>
>>> a.class_foo(1)
executing class_foo(<class '__main__.A'>,1)
cls: <class '__main__.A'>
-------------------------------------

static_foo通过类对象或对象实例调用。
-------------------------------------
>>> A.static_foo(1)
executing static_foo(1)
>>> a.static_foo(1)
executing static_foo(1)
-------------------------------------
'''


# 4.继承与覆盖普通类函数是一样的。
class B(A):
    pass


b = B()
b.foo(1)
b.class_foo(1)
b.static_foo(1)
# executing foo(<__main__.B object at 0x007027D0>,1)
# self: <__main__.B object at 0x007027D0>
# executing class_foo(<class '__main__.B'>,1)
# cls: <class '__main__.B'>
# executing static_foo(1)

'''
问题：@staticmethod修饰的方法函数与普通的类外函数，为什么不直接使用普通函数？
@staticmethod是把函数嵌入到类中的一种方式，函数就属于类，同时表明函数不需要访问这个类。通过子类的继承覆盖，能更好的组织代码。

参考：What is the difference between @staticmethod and @classmethod in Python?
'''
