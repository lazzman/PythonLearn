#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月10日
常用的内置函数
@author: NodCat
'''
print('=============help============')
# help()
a = []
help(a)

print('=============dir============')
# dir() 打印当前模块的方法名
a = []
print(dir())

print('=============vars============')
# vars() 打印当前模块的方法名和值
a = []
print(vars())

print('=============type============')
# type() 打印当前对象的类型
a = []
b = ()
c = object
print(type(a))
print(type(b))
print(type(c))

print('=============import============')
# import 导包
import math
print(math.sqrt(16))

print('=============reload============')
# reload 重新导包
reload(math)
print(math.sqrt(16))

print('=============id============')
# id() 获取当前对象的内存标识(相当于内存地址)
print(id(math))
print(id(1))
print(id(1))
print(id(2))
print(id(2))

print('=============cmp============')
# cmp() 比较大小
print(cmp('a', 'b'))
print(cmp(1, 1))
print(cmp(3, 2))

print('=============abs============')
# abs() 取绝对值
print(abs(-23232))

print('=============bool============')
# bool() 取布尔值，非0为True
print(bool(-23232))
print(bool(0))
print(bool(""))
print(bool(None))

print('=============divmod============')
# divmod() 求出商和余数
print(divmod(9, 4))
print(divmod(15, 4))

print('=============max============')
# max() 取最大值
print(max([1, 2, 3, 4, 5]))
print(max(['1', 'a', 3, '4', 5]))

print('=============min============')
# min() 取最小值
print(min([1, 2, 3, 4, 5]))
print(min(['1', 'a', 3, '4', 5]))

print('=============sum============')
# sum() 求和
print(sum([1, 2, 3, 4, 5]))

print('=============pow============')
# pow() 求幂
print(pow(2, 10))

print('=============len============')
# len() 取长度
print(len([1, 2, 3]))
print(len("呵呵哒"))  # 字节长度

print('=============all============')
# all() 迭代所有元素，全为True则返回True
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))

print('=============any============')
# any() 迭代元素，有一个为True则返回True
print(all([0, 0, 3]))

print('=============chr============')
# chr() 返回指定Ascii码对应的字符
print(chr(65))
print(chr(97))

print('=============ord============')
# ord() 返回字符指定对应的Ascii码
print(ord('A'))
print(ord('a'))

print('=============hex============')
# hex() 返回数字的16进制形式
print(hex(1024))

print('=============bin============')
# bin() 返回数字的2进制形式
print(bin(1024))

print('=============oct============')
# oct() 返回数字的8进制形式
print(oct(1024))

print('=============enumerate============')
# enumerate()
a_list = ['aa', 'bb', 'cc']
for item in a_list:
    print(item)
for item in enumerate(a_list):
    print(item)
for item in enumerate(a_list, 3):  # 第二个参数指定序号从3开始
    print(item)

print('=============format============')
# format() 字符串格式化输出
print("hello {0} , this is my {1}".format('world', 'code'))

print('=============map============')
# map() 遍历第二个参数序列中的每个元素，使用第一个参数function作为处理函数处理每一个元素
def getPingfang(i):
    return i * i
print(map(getPingfang, [1, 2, 3, 4]))
print(map(lambda x:x * x, [1, 2, 3, 4]))  # lambda匿名函数

print('=============filter============')
# filter() 遍历第二个参数序列中的每个元素，使用第一个参数function作为处理函数处理每一个元素，如果返回true则保留元素到新的结果列表中
def myfilter(i):
    if i % 2 == 0:
        return True
    else:
        return False
print(filter(myfilter, [1, 2, 3, 4]))
print(filter(lambda x:x % 2 == 0, [1, 2, 3, 4]))  # lambda匿名函数

print('=============reduce============')
# reduce() 常用于累加或阶乘
def myreduce(x, y):
#     return x + y
    return x * y
print(reduce(myreduce, [1, 2, 3, 4]))
print(reduce(lambda x, y:x + y, [1, 2, 3, 4]))  # lambda匿名函数

print('=============zip============')
# zip() 难以描述，自己看吧
x = [1, 2, 3, 4]
y = [4, 5, 6, 5]
z = [7, 8, 9, ]
print(zip(x, y, z))

print('=============eval============')
# eval() 类似js中的eval
x = "8*8+1"
print(eval(x))

print('=============chr============')
# chr() 将ascii码转为对应的字符
x = 65
print(chr(x))





