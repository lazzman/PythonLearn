#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月9日

@author: NodCat
'''



print '==========================捕获异常基本语法==========================='

'''
基本语法：
try:
<语句>        #运行别的代码
except <异常类型>：
<语句>        #如果在try部份引发了'name'异常
except <异常类型>，<异常对象>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
finlly:
<语句>        #无论是否发生异常都执行
try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句
'''

try:
    fh = open("testfile", "r")
    fh.readline()
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError, e:
    print "Error: 没有找到文件或读取文件失败"
    print e
except Exception, e:
    print e
else:
    print "内容写入文件成功"
    fh.close()
finally:
    print 'finlly'

print '==========================自定义异常==========================='

class MyException(Exception):  # 继承Exception
    
    def __init__(self, msg):
        self.error = msg
    
    def __str__(self, *args, **kwargs):  # __str__相当于java中Object的toString()方法，当print该对象时，会调用__str__方法
        return str(self.__class__) + self.error

e = MyException("xxxx自定义异常的异常信息xxxx")
print e

try:
    raise MyException('手动触发自定义异常')
except Exception, e:
    print e

print '==========================手动抛出异常==========================='

'''
手动抛出异常
'''
# 定义函数
def mye(level):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)  # 触发异常
except Exception, e:
    print e
finally:
    print 'finally无论异常是否发生执行'
    
    
    
    
