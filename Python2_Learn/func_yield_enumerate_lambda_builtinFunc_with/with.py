#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月22日

Python与java相比有一个比较好用的关键字，with
with的比较常见的操作用于对文件的操作，线程锁的操作
    with open('20. 单元测试.txt') as f:
        print f.read()

    with self.lock:    #使用“with”语句管理锁的获取和释放
        print 'lock acquired by %s' % self.name
        self.output.write(d.read())
        print 'write done by %s' % self.name
        print 'lock released by %s' % self.name
        
@author: NodCat
'''

'''
短短的几行代码既能够实现对文件的读取，但是我们怎样创建一个自己的额class并支持with关键字呢？
Python对with的处理还很聪明。基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
举例说明
'''

class WithDemo(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print 'enter:' + self.name
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'in:' + self.name
        print "type:", exc_type
        print "value:", exc_val
        print "trace:", exc_tb

    def do_something(self):
        bar = 1 / 0
        return bar + 10
    

with WithDemo('with原理') as w:
    # print w
    # w.do_something()
    print w
    
# 需要注意的地方__enter__返回一个对象然后赋值给w，在__exit__进行一些clear的操作，挺方便的。