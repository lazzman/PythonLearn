#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月23日

多进程内存同步——共享内存Queue

Queue是一个进程安全的队列

@author: NodCat
'''

from multiprocessing import Process, Queue
import os


def f(q, n):
    q.put([n, 'pid:' + str(os.getpid()) ])
    
if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        p = Process(target=f, args=(q, i))
        p.start()
    
    print '主进程pid:' + str(os.getpid())
    while True:
        print q.get()
    
    print q.get()


