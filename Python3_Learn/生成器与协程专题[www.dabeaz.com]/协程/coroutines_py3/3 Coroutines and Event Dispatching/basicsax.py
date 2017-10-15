# basicsax.py
# 一个简单的sax解析的例子
# A very simple example illustrating the SAX XML parsing interface

import xml.sax

'''
一、python str和repr的区别
尽管str(),repr()和``运算在特性和功能方面都非常相似，事实上repr()和``做的是完全一样的事情，它们返回的是一个对象的“官方”字符串表示，也就是说绝大多数情况下可以通过求值运算（使用内建函数eval()）重新得到该对象。

但str()则有所不同，str()致力于生成一个对象的可读性好的字符串表示，它的返回结果通常无法用于eval()求值，但很适合用于print语句输出。需要再次提醒的是，并不是所有repr()返回的字符串都能够用 eval()内建函数得到原来的对象。 也就是说 repr() 输出对 Python比较友好，而str()的输出对用户比较友好。

虽然如此，很多情况下这三者的输出仍然都是完全一样的。 大家可以看下下面的代码，来进行对比
---------------------------------------------
    >>> s = 'Hello, world.'
    >>> str(s)
    'Hello, world.'
    >>> repr(s)
    "'Hello, world.'"
    >>> str(0.1)
    '0.1'
    >>> repr(0.1)
    '0.10000000000000001'
    >>> x = 10 * 3.25
    >>> y = 200 * 200
    >>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
    >>> print s
    The value of x is 32.5, and y is 40000...
    >>> # The repr() of a string adds string quotes and backslashes:
    ... hello = 'hello, world\n'
    >>> hellos = repr(hello)
    >>> print hellos
    'hello, world\n'
    >>> # The argument to repr() may be any Python object:
    ... repr((x, y, ('spam', 'eggs')))
    "(32.5, 40000, ('spam', 'eggs'))"
-----------------------------------------------

'''

class MyHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print("startElement", name)

    def endElement(self, name):
        print("endElement", name)

    def characters(self, text):
        print("characters", repr(text)[:40])


xml.sax.parse("allroutes.xml", MyHandler())
