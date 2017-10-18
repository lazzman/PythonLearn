#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'当一个类实现了__call__方法时，可以直接使用 实例名()方式调用__call__()方法'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()
