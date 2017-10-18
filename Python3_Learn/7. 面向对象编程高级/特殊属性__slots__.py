#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性'

'''
正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。

使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。
'''

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class GraduateStudent(Student):
    pass


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
