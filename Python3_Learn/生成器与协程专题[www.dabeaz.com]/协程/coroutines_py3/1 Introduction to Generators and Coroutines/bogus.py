# bogus.py
#
# Bogus example of a generator that produces and receives values

def countdown(n):
    print("Counting down from", n)
    while n >= 0:
        newvalue = (yield n)
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


# The holy grail countdown
c = countdown(5)
for x in c:
    print(x)
    if x == 5:
        c.send(3)

next(c)

'''
步骤：
1. for迭代等价于调用next()
    Counting down from 5
    yield 5 # print(5)
2. c.send(3)
    newvalue = 3
    n = newvalue
    yield 3 # 此时c.send(3)并没有打印返回值
3. for迭代等价于调用next()等价于send(None)
    newvalue = None
    n = 2
    yield 2 # print(2)
4. for迭代等价于调用next()等价于send(None)
    newvalue = None
    n = 1
    yield 1 # print(1)
5. for迭代等价于调用next()等价于send(None)
    newvalue = None
    n = 0
    yield 0 # print(0)
6. for迭代等价于调用next()等价于send(None)
    newvalue = None
    n = -1
    # 此时无法调用yield，抛出StopIteration异常
    # for迭代自动处理StopIteration异常，for迭代结束

'''
