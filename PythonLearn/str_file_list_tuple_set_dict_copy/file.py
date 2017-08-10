#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from fileinput import filename

'''
文件操作相关

文件处理模式
r 以只读模式打开文件
w 以只写模式打开文件
a 以追加模式打开文件
r+b 以读写二进制模式打开文件
w+b 以写读二进制模式打开文件
a+b 以追加及读二进制模式打开文件
'''

filePath = "../res/FileRW.txt"
    
def fileRead(filePath):
    '''
    文件读取操作
    '''
    f = file(filePath)
    # xreadlines()性能比readlines()要好,尤其是读取大文件时,readlines()会将所有数据读入内存，xreadlines()不会这样
    for line in f.xreadlines():
        line = line.strip('\n')
        print(line)
    f.close()

def fileWrite():
    '''
    文件写出操作(会覆盖原有内容)
    '''
    filePath = "../res/FileWrite.txt"
    # 判断文件是否存在，不存在则创建
#     if not(os.path.exists(filePath) and os.path.isfile(filePath)):
#         os.makedirs("../res");
    f = file(filePath, 'w')
    f.write("fileWrite操作成功！")
    f.close()

def fileAppend():
    '''
    文件内容追加
    '''
    filePath = "../res/FileWrite.txt"
    # 判断文件是否存在，不存在则创建
#     if not(os.path.exists(filePath) and os.path.isfile(filePath)):
#         os.makedirs("../res");
    f = file(filePath, 'a')
    f.writelines("\nfileAppend操作成功！")
    f.close()
    
def fileCursor(cursor=0):
    # 当前游标默认为0
    '''
    文件游标
    '''
    filePath = "../res/FileXReadLines.txt"
    with open(filePath,'r') as f:
        f.seek(cursor)
        data = f.readline()
        print("len(data):"+str(len(data)),"content:"+data)
        print(f.tell())  # 打印文件当前游标
        data = f.readline()
        print("len(data):"+str(len(data)),"content:"+data)
        print(f.tell())  # 打印文件当前游标
        
if __name__ == '__main__':
    fileRead(filePath)
    fileWrite()
    fileAppend()
    fileRead("../res/FileWrite.txt")
    fileCursor(2)
    
