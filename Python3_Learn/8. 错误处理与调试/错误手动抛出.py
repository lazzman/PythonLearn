# err_raise.py

'因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。'

# 定义一个错误
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        # 手动抛出错误
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')
