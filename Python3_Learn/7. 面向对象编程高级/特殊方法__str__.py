#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'当类实现了__str__方法时，print(实例)时就可以输出__str__的返回值，等同于java中的toString()方法'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


print(Student('Michael'))
