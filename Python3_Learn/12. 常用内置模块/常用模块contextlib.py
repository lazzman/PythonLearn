#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'with ... as ..语法需要编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法'

from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('nodcat') as cq:
    print('invoke1')
    print('invoke2')
    print('invoke3')

'''
@closing

如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
-------------------------------------------------
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
-------------------------------------------------

closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
-------------------------------------------------
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
-------------------------------------------------

它的作用就是把任意对象变为上下文对象，并支持with语句。

@contextlib还有一些其他decorator，便于我们编写更简洁的代码。
'''
