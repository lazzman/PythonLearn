#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月20日

多线程的练习
thread 和 threading 模块的选择？使用更高级的threading模块

1.threading.Thread模块方法
start
getName()
setName()
isDaemon() 守护线程会随着用户线程的退出而退出，不会阻塞程序的退出
setDaemon()
join(timeout) 例如：t1.join(2000) 意味着当前线程必须等待t1线程执行完或者执行了2000毫秒后，才可以执行t1.join()后面的代码 与java一样
run()

2.线程锁
线程锁中的threading.Lock 和 threading.Rlock

@author: NodCat
'''

from threading import Thread

def show(*arg):
    print "thread:" + str(arg) +'\n'


t1 = Thread(target=show, args=(1, 22, 333))

t1.start()

print Thread.getName(t1);
print 'main\n'

