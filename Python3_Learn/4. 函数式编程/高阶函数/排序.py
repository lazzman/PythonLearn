#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''


'''

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))


class Person(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


# 对象列表
p_list = [
    Person("zhansgan", 12, 1111),
    Person("lisi", 11, 2222),
    Person("wangwu", 13, 3333)
]

# 按照年龄排序
p_list = sorted(p_list, key=lambda x: x.age, reverse=False);
print([str(x.name) + " " + str(x.age) + " " + str(x.salary) for x in p_list])
