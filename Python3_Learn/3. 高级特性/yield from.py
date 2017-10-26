#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器：返回字符串每个字符的Unicode码值
def each_ascii(s):
    for ch in s:
        yield ord(ch)
    # return语句实际上会抛出StopIteration() 异常，所以return的值会成为调用者中yield from表达式的返回值。
    return "len('" + s + "')= %s" % len(s)


def yield_from(s):
    # r的返回值是由each_ascii(s)中迭代结束时抛出的StopIteration异常的第一个参数（即迭代器中return 的值）。
    r = yield from each_ascii(s)
    print(r)


def main():
    for x in each_ascii('abc'):
        print(x)  # => 'a', 'b', 'c'
    it = each_ascii('xyz')
    try:
        while True:
            print(next(it))  # => 'x', 'y', 'z'
    except StopIteration as s:
        print(s.value)  # => '3 chars'

    # using yield from in main() will change main() from 2. 函数 to generator:
    # r = yield from each_ascii('hello')

    for ch in yield_from('hello'):
        pass


main()
