#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'__init__是实例的初始化方法，但是Python并不像Java一般拥有重载机制，无法拥有多个__init__方法，但是Python提供了classmethod'


class Teacher(object):
    # 默认的初始化方法，默认最低学历是研究生
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__education = '研究生'

    def info(self):
        print('''教师信息 :
    name: %s
    age: %s
    sex: %s
    education: %s
        ''' % (self.__name, self.__age, self.__sex, self.__education))

    # 当新来一个老师，学历不是研究生时，可以调用此方法返回一个指定学历的teacher对象
    @classmethod
    def getNewInstance(cls, name, age, sex, education):
        t = cls(name, age, sex)
        t.__education = education
        # t.__setattr__('_Teacher__education', education) # 不推荐
        return t

    # 静态方法，类似Java的static修饰方法，所有老师的职责都是“教书”
    @staticmethod
    def getDuty():
        print('老师的职责是教书育人')


if __name__ == '__main__':
    Teacher.getDuty()

    t1 = Teacher('zhangsan', 25, '男')
    t1.info()
    t1.getDuty()

    t2 = Teacher.getNewInstance('lisi', 30, '女', '小学')
    t2.info()
    t2.getDuty()
