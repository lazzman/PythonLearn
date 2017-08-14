# !/usr/bin/python
# -*- coding: UTF-8 -*-

'''
通过对象访问：普通字段、普通方法 、property
通过类访问的有:静态字段、静态方法、类方法
Python中实际上是没有私有变量的。有一些简单的被遵循的规范。Python本身不会应用任何限制。
__dict__存储了当前对象的所有成员变量，因此私有属性的值也可以直接获取或者修改
'''

class Province(object):
    
    country = '中国'  # 静态字段
    
    # 构造方法 __init__
    def __init__(self, name, capital, leader, abbreviation):
        self.name = name  # 普通字段
        self.capital = capital  # 普通字段
        self.leader = leader  # 普通字段
        self.__abbreviation = abbreviation  # 私有普通字段
    
    # 析构函数 __del__ (不常用，类似java中的finalize())
    def __del__(self):
        print '解释器要销毁' + str(self) + '对象了。。。。'
        
    # __call__方法
    def __call__(self):
        print '调用' + str(self) + '的__call__方法了'
        
    # 等同于java Object.toSting()方法
    def __str__(self, *args, **kwargs):
        return self.name
    
    # 表示当前对象是一个可迭代对象
    def __iter__(self):
        pass
    
    # 表示当前对象可以支持下标索引
    def __getitem__(self):
        pass
    
    # 声明一个普通方法
    def sports_meet(self):
        print self.name, '正在开运动会'
        
    # 声明一个静态方法
    @staticmethod
    def anti_corruption():
        print Province.country, '所有的省会都需要反腐'
    
    # 声明一个类方法 (类方法只能使用类名.方法名调用，并且必须传入cls参数代表当前类)
    @classmethod
    def class_method(cls):
        print str(cls) + 'class_method'
    

    # 声明一个property（访问方式如同访问对象字段一般，调用方式有点类似vue.js中的计算属性，类似java中的gettersetter）
    @property
    def currentLeaderName(self):
        return self.leader

    # 声明一个私有普通方法(此方法仅在内部可被访问)
    def __setAbbreviation(self, arg):
        self.__abbreviation = arg
    
    # 使用property访问私有字段
    @property
    def abbreviation(self):
        return self.__abbreviation
    
    # 使用property修改私有字段值(装饰器：@方法名.setter)
    @abbreviation.setter
    def abbreviation(self, arg):
        self.__abbreviation = arg
    
    
if __name__ == '__main__':
    
    # 查看类的成员__dict__
    print Province.__dict__
    
    # 创建一个省会对象
    ah = Province('安徽', '合肥', 'elifer', '沪')
    
    # 查看当前对象的__dict__ 可以看到所有的属性值，并可以修改
    print ah.__dict__
    ah.__dict__['_Province__abbreviation'] = '鲁'
    print ah.__dict__
    
    # 打印当前省会信息
    print Province.country, ah.name, ah.capital, ah.leader
    
    # 调用对象的普通方法
    ah.sports_meet()
    
    # 调用对象的静态方法
    ah.anti_corruption()
    
    # 访问对象的property
    print ah.currentLeaderName
    
    # 直接访问对象的私有字段会报错，因为私有字段只能在对象内部访问，但是python也提供了一种方式强制在外部访问私有字段(方法)，字段名可以通过__dict__看到
#     print ah.__abbreviation
    ah._Province__setAbbreviation('皖')  # 强制访问对象的私有字段或私有方法(不推荐使用)
    ah._Province__abbreviation = '赣'  # 强制访问对象的私有字段或私有方法(不推荐使用)
    
    # 使用property访问私有字段（推荐）
    ah.abbreviation = '皖'
    print ah.abbreviation  # 使用property间接访问私有成员
    
    # 调用对象的__call__方法
    ah()  # 直接对象()会调用对象的__call__方法
    
    # 调用类方法
    Province.class_method()
    
    # 调用对象的__str__方法
    print ah
    
    
    
    
    
