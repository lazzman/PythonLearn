# benchmark.py
# 对比协程与对象的处理性能
# A micro benchmark comparing the performance of sending messages into
# a coroutine vs. sending messages into an object

# 协程装饰器
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


# 对象的形式
class GrepHandler(object):
    def __init__(self, pattern, target):
        self.pattern = pattern
        self.target = target

    def send(self, line):
        if self.pattern in line:
            self.target.send(line)


# 协程
@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


# A null-sink to send data
@coroutine
def null():
    while True:
        item = (yield)


# A benchmark
line = 'python is nice'
p1 = grep('python', null())  # Coroutine
p2 = GrepHandler('python', null())  # Object

from timeit import timeit
from timeit import repeat

'''
一、timeit
通常在一段程序的前后都用上time.time(),然后进行相减就可以得到一段程序的运行时间，不过python提供了更强大的计时库：timeit
-------------------------------------------------------------------------
    #导入timeit.timeit
    from timeit import timeit  
    
    #看执行1000000次x=1的时间：
    timeit('x=1')
    
    #看x=1的执行时间，执行1次(number可以省略，默认值为1000000)：
    timeit('x=1', number=1)
    
    #看一个列表生成器的执行时间,执行1次：
    timeit('[i for i in range(10000)]', number=1)
    
    #看一个列表生成器的执行时间,执行10000次：
    timeit('[i for i in range(100) if i%2==0]', number=10000)
-------------------------------------------------------------------------

测试一个函数的执行时间：
-------------------------------------------------------------------------
    from timeit import timeit
    
    def func():
        s = 0
        for i in range(1000):
            s += i
        print(s)
    
    # timeit(函数名_字符串，运行环境_字符串，number=运行次数)
    t = timeit('func()', 'from __main__ import func', number=1000)
    print(t)
-------------------------------------------------------------------------
此程序测试函数运行1000次的执行时间

二、repeat
由于电脑永远都有其他程序也在占用着资源，你的程序不可能最高效的执行。所以一般都会进行多次试验，取最少的执行时间为真正的执行时间。
-------------------------------------------------------------------------
    from timeit import repeat
    
    def func():
        s = 0
        for i in range(1000):
            s += i
    
    #repeat和timeit用法相似，多了一个repeat参数，表示重复测试的次数(可以不写，默认值为3.)，返回值为一个时间的列表。
    t = repeat('func()', 'from __main__ import func', number=100, repeat=5)
    print(t) 
    print(min(t))
-------------------------------------------------------------------------

'''

print("coroutine:", timeit("p1.send(line)", "from __main__ import line, p1"))
print("coroutine min(repeat100):", min(repeat("p1.send(line)", "from __main__ import line, p1", repeat=100)))

print("object:", timeit("p2.send(line)", "from __main__ import line, p2"))
print("object min(repeat100):", min(repeat("p2.send(line)", "from __main__ import line, p2", repeat=100)))

print(__name__)
