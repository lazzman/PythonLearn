#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Python中有一个被称为属性函数(property)的小概念，它可以做一些有用的事情。在这篇文章中，我们将看到如何能做以下几点：
1.将类方法转换为只读属性
2.重新实现一个属性的setter和getter方法
'''

print '=========================property类=========================='
# help(property)
'''
在Python中，property()是一个内置函数，用于创建和返回一个property对象。该函数的签名为：
    property(fget=None, fset=None, fdel=None, doc=None)
这里，fget是一个获取属性值的函数，fset是一个设置属性值的函数，fdel是一个删除属性的函数，doc是一个字符串（类似于注释）。从函数实现上看，这些函数参数都是可选的。

Property对象有三个方法，getter(), setter()和delete()，用来在对象创建后设置fget，fset和fdel。
这就意味着，这行代码：temperature = property(get_temperature,set_temperature)可以被分解为：
    # make empty property
    temperature = property()
    # assign fget
    temperature = temperature.getter(get_temperature)
    # assign fset
    temperature = temperature.setter(set_temperature)
它们之间是相互等价的。
熟悉Python中装饰器decorator的程序员能够认识到上述结构可以作为decorator实现。
我们可以更进一步，不去定义名字get_temperature和set_temperature，因为他们不是必须的，并且污染类的命名空间。
为此，我们在定义getter函数和setter函数时重用名字temperature。下边的代码展示如何实现它。

    class Celsius(object):
        def __init__(self, temperature = 0):
            self._temperature = temperature
     
        def to_fahrenheit(self):
            return (self.temperature * 1.8) + 32
     
        @property
        def temperature(self):
            print("Getting value")
            return self._temperature
     
        @temperature.setter
        def temperature(self, value):
            if value < -273:
                raise ValueError("Temperature below -273 is not possible")
            print("Setting value")
            self._temperature = value

'''

print '=========================property代替getter setter=========================='
'''
# 使用传统的getter setter方式
class Celsius(object):
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)
 
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
 
    # new update
    def get_temperature(self):
        return self._temperature
 
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
        
'''
# 使用property的方式（新式类才支持这种写法）
class Celsius(object):
    def __init__(self, temperature=0):
        self.__temperature = temperature  # 初始化是会调用一次
 
    def to_fahrenheit(self):
        return (self.__temperature * 1.8) + 32
 
    def get_temperature(self):
        print("Getting value")
        return self.__temperature
 
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self.__temperature = value
 
    temperature = property(get_temperature, set_temperature)

# 任何获取temperature值的代码都会自动调用get_temperature()，而不是去字典表（__dict__）中进行查找。同样的，任何赋给temperature值的代码也会自动调用set_temperature()
cel = Celsius()
print cel.temperature
print cel.__dict__ # temperature字段并不在__dict__中
cel.temperature = 200  # 调用了set_temperature方法
print cel.temperature  # 调用了get_temperature方法


print '=========================经典类==============================='

class jingdianclass():
    '''
    经典类中的属性(property)是可读可写的。（没有只读功能）
    '''
    
    def __init__(self):
        self.__name = 'nodcat'

    @property
    def Name(self):
        print '访问特性时并不会调用这些代码'
        return self.__name

    
jd = jingdianclass()  
jd.Name = 'elifer'  # 经典类属性可读可写,可以直接访问
print jd.Name


print '=========================新式类==============================='

class xinshiclass(object):
    '''
    新式类中的属性(property)是只读，不可写，如果要可写，需要再创建一个被@xxx.setter修饰的属性。
    '''
    
    def __init__(self, name, age):
        self.name = name
        # 定义一个私有字段age,外部无法直接访问
        self.__age = age

    def read_name(self):
        print 'my name is %s ' % self.name

    def read_age(self):
        # 外部无法访问,但是可以通过内部访问到。
        print 'my age is %s' % self.__age

    # 默认age只有只读权限
    @property
    def age(self):
        return self.__age

    # 为age添加修改权限
    @age.setter
    def age(self, value):
        print '新式类当中的setter方法是可以添加一些代码操作的'
        self.__age = value
        

cla = xinshiclass('elifer', 12)

# 读取正常字段
cla.read_name()

# 使用属性方法读取__age私有字段
print type(cla.age)
print cla.age

# 更改类中的__私有字段
cla.age = 18
print cla.age
