#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月15日

详细介绍新式类与经典类的区别
1.从Python2.2开始，Python 引入了 new style class（新式类）
2.Python 2.x中默认都是经典类，只有显式继承了object才是新式类
3.Python 3.x中默认都是新式类，不必显式的继承object

推荐大家使用新式类

@author: NodCat
'''

print '==============区别1.新式类对象可以直接通过__class__属性获取自身类型:type===================='

class E:    
# 经典类  
    pass  

class E1(object):    
# 新式类  
    pass  
       
e = E()  
print "经典类"  
print e  
print type(e)  
print e.__class__  


# E1是定义的新式类。那么输输出e1的时候，不论是type(e1)，还是e1.__class__都是输出的<class '__main__.E1'>
print "新式类"  
e1 = E1()  
print e1  
print type(e1)  
print e1.__class__  

print '==============区别2.继承搜索的顺序发生了改变,经典类多继承属性搜索顺序: 先深入继承树左侧，再返回，开始找右侧;新式类多继承属性搜索顺序: 先水平搜索，然后再向上移动===================='

'''
                                继承树
        A（show()方法）
                       ↗                         ↖
B(继承A的方法)     C（重写A的show()方法）
                             ↖            ↗
            D

A是B、C的父类
D继承B、C ( class D(B,C): )
此时创建D的实例，调用show()方法：
经典类的继承搜索顺序是：首先要查找类D中是否有show()，如果没有则按顺序查找B->A->C。它是一种深度优先查找方式。
新式类的继承搜索顺序是：首先要查找类D中是否有show()，如果没有则按顺序查找B->C->A。它是一种广度优先查找方式。

'''
# 经典类范例
class A:
    def __init__(self):
        pass
    def show(self):
        print 'this is a show from A'
        
class B(A):
    def __init__(self):
        pass
class C(A):
    def __init__(self):
        pass
    def show(self):
        print 'this is a show from C'
class D(B, C):
    def __init__(self):
        pass
# 创建D的实例并调用show()方法
d = D()
print '经典类继承搜索顺序'
d.show()


# 新式类范例
class A1(object):
    def __init__(self):
        pass
    def show(self):
        print 'this is a show from A1'
        
class B1(A1):
    def __init__(self):
        pass
class C1(A1):
    def __init__(self):
        pass
    def show(self):
        print 'this is a show from C1'
class D1(B1, C1):
    def __init__(self):
        pass
# 创建D1的实例并调用show()方法
d = D1()
print '新式类继承搜索顺序'
d.show()


print '==============区别3.新式类增加了__slots__内置属性, 可以把实例属性的种类锁定到__slots__规定的范围之中===================='

'''
__slots__属性虽然令实例失去了绑定任意属性的便利，但是因为每一个实例没有__dict__属性，却能有效节省每一个实例的内存消耗，有利于生成小而精干的实例。

'''
# 比如只允许对F实例添加name和age属性:
class F(object):    
    __slots__ = ('name', 'age')   
  
class F1():    
    __slots__ = ('name', 'age')   
      
f1 = F1()  
f = F()  

# 经典类可以给对象添加任意属性
f1.name1 = "a1"
# 新式类使用__slots__后只允许添加指定的属性
f.name = 'aaa'
# f.name1 = "a"  # 报错：AttributeError: 'F' object has no attribute 'name1'


print '==============区别4.新式类增加了__getattribute__方法===================='

class G(object):
    def __init__(self):  
        self.test = "新式类"
    def __getattribute__(self, *args, **kwargs):    
        print "访问了新式类实例的属性"  
           
      
class G1():
    def __init__(self):
        self.test = "经典类"
    def __getattribute__(self, *args, **kwargs): 
        print "访问了经典类实例的属性"
          
      
g1 = G1()  
g = G()  
  
g.test  # 访问新式类实例的属性时会调用实例的__getattribute__方法
g1.test  # 访问经典类实例的属性时不会调用实例的__getattribute__方法



