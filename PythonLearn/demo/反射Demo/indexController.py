#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年4月11日
自定义controller
@author: nodcat
'''

class Index():
    '''
    声明一个Controller
    '''
#     __account = None    # 私有 静态属性
#     __password = None   # 私有静态属性
    
    def __init__(self, act, pwd):
        self.__account = act  # 对象的普通属性
        self.__password = pwd  # 对象的普通属性
    
    def login(self):  # 访问index/login时调用
        print("Account: {0} login success! Password: {1}".format(self.__account, self.__password))
