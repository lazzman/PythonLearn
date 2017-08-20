#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。

整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。

'''

print("浮点数相加结果是", 1.21 + 1.79, sep="")

print("浮点数相减", 2.3 - 1.1, sep="：")

print("浮点数相除结果是", 2.5 / 0.5, sep="：")

print("浮点数整除", 2.5 // 2, sep="：")

print("浮点数相乘", 1.5 * 2, sep="：")

print("科学计数法形式（等同于1.1*10的9次方）", 1.1e9, sep="：")
