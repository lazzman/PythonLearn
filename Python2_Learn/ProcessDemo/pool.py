#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月23日

进程池——Pool

@author: NodCat
'''

from multiprocessing import Pool
import time
import os

def f(x):
    print 'pid:' + str(os.getpid()) + ' result:' + str(x * x)
    time.sleep(1)
    return 'pid:' + str(os.getpid()), x * x

if __name__ == '__main__':
    pool = Pool(processes=8)  # 创建一个进程池里面有8个进程 线程数应该与cpu核数对应，不要大于cpu核数，如果进程数太多会产生僵尸进程，对系统造成很大压力
    res_list = []
    for i in range(10):
        res = pool.apply_async(f, [i, ])  # 从进程池中获取一个空闲进程分配任务
        # 等同于   # res = Process(target=f,args=(i,))
        res_list.append(res)
        
    for r in res_list:
        print r.get(timeout=2)  # 获取进程的返回结果，设置超时时间2秒
