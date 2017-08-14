#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月15日

python 抽象类、抽象方法的实现
python 没有抽象类、接口的概念，所以要实现这种功能得abc.py 这个类库

@author: NodCat
'''

from abc import ABCMeta, abstractmethod

# 抽象类
class Headers(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.headers = ''

    @abstractmethod
    def _getBaiduHeaders(self):pass

    def __str__(self):
        return str(self.headers)

    def __repr__(self):
        return repr(self.headers)

# 实现类
class BaiduHeaders(Headers):
    def __init__(self, url, username, password):
        self.url = url
        self.headers = self._getBaiduHeaders(username, password)

    def _getBaiduHeaders(self, username, password):
        headers = dict()
        headers.username = username
        headers.password = password
        return headers
'''
如果子类不实现父类的_getBaiduHeaders方法,
则抛出TypeError: Can't instantiate abstract class BaiduHeaders with abstract methods  异常
'''