#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

print('classmates =', classmates)

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print("classmates.append('Adam') =", classmates)

# 把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Apple')
print("classmates.insert(1, 'Apple') =", classmates)

# 删除list末尾的元素，用pop()方法
print('classmates.pop() =', classmates.pop(), classmates)

# 删除指定位置的元素，用pop(i)方法，其中i是索引位置
print('classmates.pop(1) =', classmates.pop(1), classmates)

# 把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[0] = 'ipad'
print('classmates =', classmates)

'''
list里面的元素的数据类型也可以不同
list元素也可以是另一个list
如果一个list中一个元素也没有，就是一个空的list，它的长度为0
'''

s = ['python', 'java', 'javascript', [666, True], 'lua']
print("s =", s)
