#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'判断对象类型的常用方式：type() isintance() 获取对象的所有属性和方法：dir()'


'''
type()

基本类型都可以用type()判断

'''

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

import types

print('type(\'abc\')==str?', type('abc')==str)


'''
isinstance()

对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

我们回顾上次的例子，如果继承关系是：

object -> Animal -> Dog -> Husky

那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
--------------------------------------
>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
--------------------------------------

然后，判断：
--------------------------------------
>>> isinstance(h, Husky)
True
--------------------------------------
'''