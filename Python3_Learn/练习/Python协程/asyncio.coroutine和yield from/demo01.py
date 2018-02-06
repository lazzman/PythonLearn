"""
使用生成器，每次迭代会根据生成器的上一次context继续计算下一个值
yield from用于重构生成器
"""


def fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        yield b
        a, b = b, a + b
        index += 1


def copy_fib(n):
    print('I am copy from fib')
    yield from fib(n)
    print('Copy end')


print('-' * 10 + 'test yield fib' + '-' * 10)
for fib_res in copy_fib(20):  # 每次循环都会调用next(fib(20))
    print(fib_res)
