"""
可以向fib(20)发送数据，那不是就可以在Python中实现协程了嘛。

于是，Python中的生成器有了send函数，yield表达式也拥有了返回值。

yield from 的意义
PEP380 分6点说明了yield from 的行为。

子生成器产出的值都直接传给委派生成器的调用方（客户端代码）

使用send() 方法发给委派生成器的值都直接传给子生成器。如果发送的值是None，那么会调用子生成器的 __next__()方法。如果发送的值不是None，那么会调用子生成器的send()方法。如果调用的方法抛出StopIteration异常，那么委派生成器恢复运行。任何其他异常都会向上冒泡，传给委派生成器。

生成器退出时，生成器（或子生成器）中的return expr 表达式会触发 StopIteration(expr) 异常抛出。

yield from表达式的值是子生成器终止时传给StopIteration异常的第一个参数。

传入委派生成器的异常，除了 GeneratorExit 之外都传给子生成器的throw()方法。如果调用throw()方法时抛出 StopIteration 异常，委派生成器恢复运行。StopIteration之外的异常会向上冒泡。传给委派生成器。

如果把 GeneratorExit 异常传入委派生成器，或者在委派生成器上调用close() 方法，那么在子生成器上调用close() 方法，如果他有的话。如果调用close() 方法导致异常抛出，那么异常会向上冒泡，传给委派生成器；否则，委派生成器抛出 GeneratorExit 异常。
"""

import random
import time


def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_cnt = yield b
        print('let me think {0} secs'.format(sleep_cnt))
        time.sleep(sleep_cnt)
        a, b = b, a + b
        index += 1
    return 'end'


def copy_stupid_fib(n):
    print('I am copy from stupid fib')
    result = yield from stupid_fib(n)  # 当stupid_fib中执行return时，会将值覆给result
    print(result)
    print('Copy end')


print('-' * 10 + 'test yield send' + '-' * 10)
N = 20
csfib = copy_stupid_fib(N)
fib_res = next(csfib)
while True:
    print(fib_res)
    try:
        fib_res = csfib.send(random.uniform(0, 0.5))
    except StopIteration:
        break
