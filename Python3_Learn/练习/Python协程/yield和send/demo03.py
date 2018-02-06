"""
可以向fib(20)发送数据，那不是就可以在Python中实现协程了嘛。

于是，Python中的生成器有了send函数，yield表达式也拥有了返回值。
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


print('-' * 10 + 'test yield send' + '-' * 10)
N = 20
sfib = stupid_fib(N)
fib_res = next(sfib)
while True:
    print(fib_res)
    try:
        fib_res = sfib.send(random.uniform(0, 0.5))
    except StopIteration as e:
        print('-' * 10 + e.value + '-' * 10)
        break
