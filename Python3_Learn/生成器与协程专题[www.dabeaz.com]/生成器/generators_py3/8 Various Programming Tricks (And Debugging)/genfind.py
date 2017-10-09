# genfind.py
# 生成器-返回匹配模式的文件名序列
# A function that generates files that match a given filename pattern

import os
import fnmatch

'''
os.walk(top, topdown=True, onerror=None, followlinks=False) -> Directory tree generator.
可以得到一个三元tupple(dirpath, dirnames, filenames), 
第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
dirpath 是一个string，代表目录的路径，
dirnames 是一个list，包含了dirpath下所有子目录的名字。
filenames 是一个list，包含了非目录文件的名字。
这些名字不包含路径信息，如果需要得到全路径，需要使用os.path.join(dirpath, name).
'''

'''
fnmatch 模块使用模式来匹配文件名.
模式语法和 Unix shell 中所使用的相同. 星号(*) 匹配零个或更多个字符, 问号(?) 匹配单个字符.
你也可以使用方括号来指定字符范围, 例如 [0-9] 代表一个数字. 其他所有字符都匹配它们本身.

fnmatch.filter(names, pat) -> list
实现列表特殊字符的过滤或筛选,返回符合匹配模式的字符列表,当然names表示的是列表
'''


def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


# Example use
if __name__ == '__main__':
    lognames = gen_find("access-log*", "www")
    for name in lognames:
        print(name)
