#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月23日

对于多进程来说，由于内存独立，所以很少有同步问题，但是，当我们多进程打印结果时，可以使用lock方式输出混乱
基本很少用上

@author: NodCat
'''

from multiprocessing import Process, Lock

def f(lock, i):
    lock.acquire() # 不加锁可能输出时打印内容会混在一起
    print 'helloworld', i
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    
    for num in range(10):
        Process(target=f, args=(lock, num)).start()
