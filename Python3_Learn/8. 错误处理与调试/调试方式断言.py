#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


main()

'''
assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，assert语句本身就会抛出AssertionError

程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert

关闭后，你可以把所有的assert语句当成pass来看。
'''
