#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年4月11日
自定义controller
@author: nodcat
'''

class Error():
    '''
    声明一个返回各种错误码的Controller
    '''
    def error404(self):    # 访问error/error404时调用
        print("错误代码404")
        
    def error500(self):    # 访问error/error500时调用
        print("错误代码500")