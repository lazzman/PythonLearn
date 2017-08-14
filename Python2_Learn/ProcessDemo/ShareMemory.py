#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月23日

除了queue可以实现多进程内存共享，还有一些其他方式 Value Array

@author: NodCat
'''

from multiprocessing import Process, Array, Value

def f(num, a, raw):
    num.value = 3.1415926
    for i in range(5):
        a[i] = -a[i]
    raw.append(9999)
    print raw

if __name__ == '__main__':
    
    '''
    typecode_to_type = {
    'c': ctypes.c_char,
    'b': ctypes.c_byte,  'B': ctypes.c_ubyte,
    'h': ctypes.c_short, 'H': ctypes.c_ushort,
    'i': ctypes.c_int,   'I': ctypes.c_uint,
    'l': ctypes.c_long,  'L': ctypes.c_ulong,
    'f': ctypes.c_float, 'd': ctypes.c_double
    }
    '''
    num = Value('d', 0.0)  # 浮点类型
    arr = Array('i', range(10))  # int类型数组
    raw_list = range(10)
    
    print '---多进程处理前---'
    
    print num.value
    print arr[:]
    print raw_list
    
    
    print '---多进程处理中---'
    
    p = Process(target=f, args=(num, arr, raw_list))
    p.start()
    p.join()
    
    print '---多进程处理后---'
    
    print num.value
    print arr[:]
    print raw_list
