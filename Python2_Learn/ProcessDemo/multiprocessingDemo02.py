#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月23日

多进程演示
多进程会将主进程内存复制N份，非常耗内存

@author: NodCat
'''

from multiprocessing import Process
import os
import time
from test.test_threading_local import target


def info(title):
    print title
    print '5. 模块 name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    
    print 'process id:', os.getpid()

def f(name):
    info('2. 函数 f')
    print 'hello', name

if __name__ == '__main__':
    f('main line')
    print '-------------------'
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    
    
