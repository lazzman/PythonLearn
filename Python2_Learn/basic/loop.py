#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(0, 100):
    print("item {0} {1}".format(i, "Python is Easy"))

a = range(20)
a[0] = 99
print(a)

cup = (1, 2, 3, 4, 5)
i = 0
while i < 20:
    print(i, cup)
    i += 1

# 中断控制
for i in cup:
    if(i == 2):
        continue
    if(i == 3):
        break
    print(i)
    
