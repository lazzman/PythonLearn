#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外'

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
except Exception as ex:
    print("exception", ex)
else:  # 当没有发生异常时进入
    print("no except")
finally:  # 无论是否发生异常都进入
    print('finally...')

print('END')
