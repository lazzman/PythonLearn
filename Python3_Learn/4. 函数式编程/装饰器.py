#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


# 无参装饰器
def log(func):
    @functools.wraps(func)  # 保证func.__name__输出的还是被装饰函数的名称，如果不使用functools.wraps装饰，被装饰函数名称就会变为wrapper
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 等价于now = log(now)
@log
def now():
    print('2015-3-25')


now()

print('-------------------------------------------------------------------------')


# 有参装饰器
def logger(text):
    def decorator(func):
        @functools.wraps(func)  # 保证func.__name__输出的还是被装饰函数的名称，如果不使用functools.wraps装饰，被装饰函数名称就会变为wrapper
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


# 等价于today = logger('DEBUG')(today)
@logger('DEBUG')
def today():
    print('2015-3-25')


today()
print(today.__name__)

'''
本质上，decorator就是一个返回函数的高阶函数。
因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
--------------------------------------------------
>>> now.__name__
'wrapper'
--------------------------------------------------
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
--------------------------------------------------
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
--------------------------------------------------

或者针对带参数的decorator：
--------------------------------------------------
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
--------------------------------------------------
import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。
'''
