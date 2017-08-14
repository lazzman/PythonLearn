#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月23日

多进程内存共享除了Queue Value Array之外，还有一个更好用的Manage
比较常用的是Queue Manage

@author: NodCat
'''

from multiprocessing import Process, Manager
import os


def f(mydict, mylist):
    # 其他进程调用此方法，修改共享内存中的元素
    mydict[1] = '1'
    mydict['2'] = 2
    mydict[0.25] = None
    mydict['pid'] = os.getpid()
    mylist.append(os.getpid())
    mylist.reverse()
    
if __name__ == '__main__':
    manager = Manager()

    mydict = manager.dict()
    mylist = manager.list(range(10))
    print '---未修改前的数据---'
    print mydict
    print mylist
    
    p = Process(target=f, args=(mydict, mylist))
    p.start()
    p.join()
    
    print '---其他进程修改后的数据---'
    print mydict
    print mylist
