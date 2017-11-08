#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试一段代码的运行时间，在python里面有个很简单的方法，就是使用timeit模块，使用起来超级方便'

'''
主要就是这两个函数：

1,    timeit(stmt='pass', setup='pass', timer=<defaulttimer>, number=1000000)

       返回：

            返回执行stmt这段代码number遍所用的时间，单位为秒，float型

       参数：

            stmt：要执行的那段代码

            setup：执行代码的准备工作，不计入时间，一般是import之类的

            timer：这个在win32下是time.clock()，linux下是time.time()，默认的，不用管

            number：要执行stmt多少遍

2,    repeat(stmt='pass', setup='pass', timer=<defaulttimer>, repeat=3, number=1000000)

       这个函数比timeit函数多了一个repeat参数而已，表示重复执行timeit这个过程多少遍，返回一个列表，表示执行每遍的时间

当然，为了方便，python还用了一个Timer类，Timer类里面的函数跟上面介绍的两个函数是一样一样的

class timeit.Timer(stmt='pass', setup='pass',timer=<timer function>)

        Timer.timeit(number=1000000)

        Timer.repeat(repeat=3,number=1000000)

看懂了吧，一样的，使用的时候哪种方便用哪种 O(∩_∩)O

就相当于

   timeit(stmt='pass', setup='pass', timer=<defaulttimer>, number=1000000)

= Timer(stmt='pass', setup='pass', timer=<timerfunction>).timeit(number=1000000)

  repeat(stmt='pass', setup='pass', timer=<defaulttimer>, repeat=3, number=1000000)

= Timer(stmt='pass', setup='pass', timer=<timerfunction>).repeat(repeat=3, number=1000000)
'''

import math
import pprint
import timeit


def myfun():
    for i in range(100):
        for j in range(2, 10):
            math.pow(i, 1 / j)


n = 100

t1 = timeit.timeit(stmt=myfun, number=n)
pprint.pprint(t1)
t2 = timeit.repeat(stmt=myfun, number=n, repeat=5)
pprint.pprint(t2)

print()

timeitObj = timeit.Timer(stmt=myfun)
t3 = timeitObj.timeit(number=n)
pprint.pprint(t3)
t4 = timeitObj.repeat(number=n, repeat=5)
pprint.pprint(t4)
