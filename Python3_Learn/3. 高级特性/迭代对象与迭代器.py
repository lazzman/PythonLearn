#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable, Iterator

'''
Python中关于迭代有两个概念，第一个是Iterable，第二个是Iterator，协议规定Iterable的__iter__方法会返回一个Iterator, Iterator的__next__方法（Python 2里是next）会返回下一个迭代对象，
如果迭代结束则抛出StopIteration异常。同时，Iterator自己也是一种Iterable，所以也需要实现Iterable的接口，也就是__iter__，这样在for当中两者都可以使用。
Iterator的__iter__只需要返回自己就行了。这样，下面的代码就可以工作：
-----------------------------------------------------------------------
for i in my_list:
    ...

for i in iter(mylist):
    ...

for i in (v for v in mylist if v is not None):
    ...
-----------------------------------------------------------------------

Python中许多方法直接返回iterator，比如itertools里面的izip等方法，如果Iterator自己不是Iterable的话，就很不方便，需要先返回一个Iterable对象，
再让Iterable返回Iterator。生成器表达式也是一个iterator，显然对于生成器表达式直接使用for是非常重要的。那么为什么不只保留Iterator的接口而还需要设计Iterable呢？
许多对象比如list、dict，是可以重复遍历的，甚至可以同时并发地进行遍历，通过__iter__每次返回一个独立的迭代器，就可以保证不同的迭代过程不会互相影响。
而生成器表达式之类的结果往往是一次性的，不可以重复遍历，所以直接返回一个Iterator就好。让Iterator也实现Iterable的兼容就可以很灵活地选择返回哪一种。

总结来说Iterator实现的__iter__是为了兼容Iterable的接口，从而让Iterator成为Iterable的一种实现。

补充一下题主对于for的理解基本上是正确的，但仍然有一点点偏差：for为了兼容性其实有两种机制，如果对象有__iter__会使用迭代器，但是如果对象没有__iter__，
但是实现了__getitem__，会改用下标迭代的方式。我们可以试一下：
------------------------------------------------------------------------
>>> class NotIterable(object):
...     def __init__(self, baselist):
...         self._baselist = baselist
...     def __getitem__(self, index):
...         return self._baselist[index]
...
>>> t = NotIterable([1,2,3])
>>> for i in t:
...     print i
...
1
2
3
>>> iter(t)
<iterator object at 0x0345E3D0>
--------------------------------------------------------------------------
当for发现没有__iter__但是有__getitem__的时候，会从0开始依次读取相应的下标，直到发生IndexError为止，这是一种旧的迭代协议。iter方法也会处理这种情况，
在不存在__iter__的时候，返回一个下标迭代的iterator对象来代替。一个重要的例子是str，字符串就是没有__iter__接口的。

'''

def g():
    yield 1
    yield 2
    yield 3


'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：
'''

# 列表是可迭代对象
print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
# 字符串是可迭代对象
print('Iterable? \'abc\':', isinstance('abc', Iterable))
# 整数不是可迭代对象
print('Iterable? 123:', isinstance(123, Iterable))
# 生成器是可迭代对象
print('Iterable? g():', isinstance(g(), Iterable))

print('=========================================================')

'''
生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数。

你可能会问，为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


'''
print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

print('=========================================================')

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

自定义可迭代对象：(需要对象实现__iter__()与next()方法)
class countdown(object):
    def __init__(self,start):
        self.count = start
    def __iter__(self):
        return self
    def next(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

>>> c = countdown(5)
>>> for i in c:
... print i,
...
5 4 3 2 1
>>>

'''
