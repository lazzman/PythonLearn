#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月13日

1.Python中的装饰器类似于Java中的AOP动态代理
2.装饰器的写法有点类似js闭包函数  函数内声明一个函数并返回该函数

@author: NodCat
'''

'''
该案例使用debug模式可以看到全部执行流程：
1.解释器从上向下解释代码，发现outer函数并保存在内存中
2.发现 @outer
3.将当前修饰的函数func1作为参数传入outer函数，将func1的函数代码整合到wrapper函数中
4.将wrapper函数返回并重新覆给func1变量 【func1此时其实就是wrapper】
5.print '123'
5.调用func1
'''

print '=====================修饰不带参函数的装饰器======================='

# 声明一个装饰器
def outer(fun):
    def wrapper():
        # 前切
        print 'before print'
        # 调用被修饰的函数
        fun()
        # 后切
        print 'after print'
    return wrapper

@outer
def func1():
    print 'func1'

print '123'
func1()

print '=====================修饰带参函数的装饰器======================='

# 声明一个装饰器
def outer2(fun):
    def mywrapper(arg):
        # 前切
        print 'before print'
        # 调用被修饰的函数
        fun(arg)
        # 后切
        print 'after print'
    return mywrapper

@outer2
def func2(arg):
    print 'func2', arg

print '123'
func2("invoke")

print '=====================修饰带参有返回值函数的装饰器======================='

# 声明一个装饰器
def outer3(fun):
    def mywrapper(arg):
        # 前切
        print 'before print'
        # 调用被修饰的函数
        result = fun(arg)  # 原来的函数返回值
        # 后切
        print 'after print'
        return '返回值再加工' + result
    return mywrapper

@outer3
def func3(arg):  # 有返回值的函数
    print 'func3', arg
    return arg

print '123'
print func3("invoke")

print '=====================使用带参的装饰器修饰函数，在函数的前后分别执行任意的函数======================='

def before_inv(arg, arg2):
    arg = 'before_inv_arg'
    arg2 = 'before_inv_arg2'
    print 'before_inv', arg, arg2

def after_inv(arg, arg2):
    arg = 'after_inv_arg'
    arg2 = 'after_inv_arg2'
    print 'after_inv', arg, arg2

# 声明一个装饰器
# def myfilter(before_func, after_func, fun):   # 这种写法错误
def myfilter(before_func, after_func):
    def outer(fun):  # fun代表被装饰的函数(即myfunc)
        def mywrapper(arg, arg2):
            # 前切
            before_func(arg, arg2)
            # 调用被修饰的函数
            result = fun(arg, arg2)  # 原来的函数返回值
            # 后切
            after_func(arg, arg2)
            return '返回值再加工' + str(result)
        return mywrapper
    return outer

@myfilter(before_inv, after_inv)  # 传入两个函数
def myfunc(arg, arg2):  # 有返回值的函数
    print 'myfunc', arg, arg2
    return arg, arg2

print '123'
print myfunc("invoke", 'myfunction')

print '=====================使用装饰器修饰函数，为被装饰的函数对象添加属性======================='

# 声明一个装饰器
def decorator(fun):  # fun代表被装饰的函数(即myfunc)
    # 为fun添加一个属性
    fun.info = '装饰器为该函数对象添加了一个info属性'
    return fun

@decorator  # 传入两个函数
def test(arg, arg2):  # 有返回值的函数
    print 'test', arg, arg2
    return arg, arg2

print test("invoke", 'test')
print test.info
print help(test.__class__)  # 函数也是一个类，并且是新式类

