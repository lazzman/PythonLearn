#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月22日

两个线程访问临界资源，需要使用lock来同步，否则数据会出错

对于这个demo中多线程属于cpu密集型操作，多线程性能很差，不如单线程的性能

@author: NodCat
'''

import threading

i = 0  # 定义一个全局变量，多线程操作其自增加

def zizeng(lock):
    n = 0;
    global i;
    while n < 10000:
#         lock.acquire()  # 获取锁，类似java中的lock
#         i = i + 1
#         lock.release()  # 释放锁
        with lock:  # 也可以这这写
            i = i + 1
        print i
        n = n + 1



lock = threading.Lock()

t1 = threading.Thread(target=zizeng, args=(lock,))

t2 = threading.Thread(target=zizeng, args=(lock,))

t1.start()

t2.start()

# threading._sleep(2) # 睡眠两秒

# print i
