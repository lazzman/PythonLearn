#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月23日

多进程演示

@author: NodCat
'''

from multiprocessing import Pool
import time

def f(x):
    time.sleep(1)  # 阻塞1秒
    return x * x;

if __name__ == '__main__':
    p = Pool(5)  # 创建进程池对象
    print p.map(f, [1, 2, 3, 4, 5])  # 如果是多线程或者是单线程 执行5次函数一共需要阻塞5秒，而多进程不会被阻塞5秒
