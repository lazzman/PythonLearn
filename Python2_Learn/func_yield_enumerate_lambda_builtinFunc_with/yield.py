#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
当函数返回值不是用return返回，而是采用yield返回时，此时函数的返回值其实返回的是一个生成器(迭代器)对象，当我们迭代返回值时，就可以拿到yield的真正返回值
最大的好处是延迟生成，减少资源占用
让函数返回一个生成器，可以使函数分段执行并返回当前结果，执行一部分返回yield，当我们需要继续执行时，只需调用生成器的next()
可用于创建线程池，创建非阻塞方法
'''

print(range(5))  # 直接打印值，直接在内存中创建了列表
print(xrange(5))  # 打印的是xrange对象，并没有在内存中创建列表，仅仅是创建一个迭代器(生成器)对象（延迟创建），每次取值时才创建值，类似xreadlines()
for item in xrange(5):
    print item

print('=============简单案例================')

def foo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
ret = foo()
print(ret)
for item in ret:
    print (item)
    
print('==============常见用法===============')

def XReadLines():
    '''
    创建一个类似xreadlines()的生成器
    '''
    seek = 0
    while True:
        '''
        with file() as f:
                        等同于
        f = file()
        f.xxx()
        f.close
                       自动关闭文件流
        '''
        with open("../res/FileXReadLines.txt") as f: 
            f.seek(seek)  # 游标跳到指定字节处
            data = f.readline()  # 读取一行数据
            if data:  # 如果有数据(data不为Null)
                seek = f.tell()  # 取文件当前游标
                yield data
            else:
                return

print(XReadLines())
for item in XReadLines():
    print item

           
            
