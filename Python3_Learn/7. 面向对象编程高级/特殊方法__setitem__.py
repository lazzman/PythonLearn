#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'一个类定义了__setitem__方法后，就可以使用对象[key]=value的方式赋值'


class Fib(object):
    def __getitem__(self, key):
        return self.__getattribute__(key)  # getattr(self,key)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)  # setattr(self,key,value)


f = Fib()
f['name'] = "zhangsan"
f['age'] = 10

print(f['name'], f['age'])
print(f.__dict__)
