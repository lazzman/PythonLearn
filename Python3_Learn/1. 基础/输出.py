#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('The quick brown fox', 'jumps over', 'the lazy dog')
print(300)
print(100 + 200)
print('100 + 200 =', 100 + 200)
print("修改字符串默认分隔符", "修改成冒号", sep="：")

'''
%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数

'''
print("c语言占位符形式输出：%d %0.3f %s %x" % (100, 1.1e6, 'hello', 255))

