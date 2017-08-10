#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月15日

类的继承详解

@author: NodCat
'''

class Father(object):
    
    def __init__(self):
        print '调用了Father的构造方法'
        self.fathername = 'father'
    
    def father_say(self):
        print self.fathername + '说：快去写作业！'
        
    def love(self):
        print self.fathername + '抽烟喝酒烫头'

class Son(Father):  # 继承Father
    
    def __init__(self):
        # 第一种调用父类构造方法的方式
#         Father.__init__(self)  # 调用父类的构造方法。python不会隐式调用父类构造函数，需要手动调用，否则就无法继承父类的普通字段(普通字段声明在__init__中)

        # 第二种调用父类构造方法的方式 （父类必须是新式类）
        super(Son, self).__init__()
        
        print '调用了Son的构造方法'
        self.sonname = 'son'
        
    def son_say(self):
        print self.sonname + '说：作业写完了！'
    
    # 方法重写(方法覆盖)
    def love(self):
        Father.love(self)  # 可以调用父类的方法
        print self.sonname + '不抽烟喝酒烫头'
        
    
if __name__ == '__main__':
    
    s = Son()
    s.father_say()
    s.son_say()
    s.love()
