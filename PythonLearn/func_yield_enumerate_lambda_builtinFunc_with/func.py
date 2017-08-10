#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月10日

@author: nodcat
'''

# 当action未传入时，则等于默认值            -- 默认参数
def foo(name, action='默认动作', time='现在'):
    print name, time, '要执行', action

# -- 可变长参数，参数可传入任意个，我们可以将参数打包为元组传入
def showTuple(*arg):
    print '可变长参数Tuple', arg

# -- 可变长参数，参数可传入任意个，我们可以将参数打包为字典传入
def showDict(**arg):
    print '可变长参数Dict', arg

# 返回多个值时，其实是返回一个元组
def retMuchResult(name=None, age=0):
    return name, age
    

if __name__ == '__main__':
    # 调用方式
    foo('zhangsan')
    foo('lisi', '多个参数的方法')
    foo('lisi', '多个参数的方法', '一会')
    foo('list', time='昨天', action='指定参数的方法')
    # 可以将多个参数打包为字典，调用时使用**会自动将字典拆分为多个参数形式
    params = dict(name='elfier', time='未来', action='多个参数')
    foo(**params)
    
    # 传参方式
    showTuple(11, 22, 33)
    data_tuple = [44, 55, 66]  # 或data_tuple = (44,55,66)
    showTuple(*data_tuple)  # 常用
    
    # 传参方式
    showDict(name='zhangsan', age=12, sex='male')
    user_dict = {'name':'lisi', 'age':11, 'sex':'male'}  # 我们可以将参数打包为字典再传入
    showDict(**user_dict)  # 常用

    # 多个返回值接收方式1
    result = retMuchResult('nodcat', 20);
    print result
    # 多个返回值接收方式2
    ret1, ret2 = retMuchResult('nodcat2', 10);
    print ret1, ret2
