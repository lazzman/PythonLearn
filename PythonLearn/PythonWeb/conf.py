#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''

路由配置映射

'''

def index():
    return 'index'

def login():
    return 'login'


url = (
    ('/index',index),
    ('/login',login),
)