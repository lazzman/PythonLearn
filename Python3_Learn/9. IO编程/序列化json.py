#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

'''
JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
JSON类型	Python类型
{}	        dict
[]	        list
"string"    str
1234.56     int或float
true/false  True/False
null        None
'''

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
json.dump(d, open('json', 'w'))
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)


s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

'''
Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
--------------------------------------------------------
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))
--------------------------------------------------------

运行代码，毫不留情地得到一个TypeError：
--------------------------------------------------------
Traceback (most recent call last):
  ...
TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
--------------------------------------------------------

错误的原因是Student对象不是一个可序列化为JSON的对象。

如果连class的实例对象都无法序列化为JSON，这肯定不合理！

别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：

https://docs.python.org/3/library/json.html#json.dumps

这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。

可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
--------------------------------------------------------
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
--------------------------------------------------------

这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
--------------------------------------------------------
>>> print(json.dumps(s, default=student2dict))
{"age": 20, "name": "Bob", "score": 88}
--------------------------------------------------------

不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
--------------------------------------------------------
print(json.dumps(s, default=lambda obj: obj.__dict__))
--------------------------------------------------------

因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
--------------------------------------------------------
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
--------------------------------------------------------

运行结果如下：
--------------------------------------------------------
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> print(json.loads(json_str, object_hook=dict2student))
<__main__.Student object at 0x10cd3c190>
--------------------------------------------------------
打印出的是反序列化的Student实例对象。
'''
