# linesdir.py
# 讲一个目录下的所有匹配名称的日志文件（包含子目录下的压缩或未压缩日志文件）进行迭代，返回一个全部日志行内容的序列
# Generate a sequence of lines from files in a directory

from genfind import *
from gencat import *
from genopen import *


def lines_from_dir(filepat, dirname):
    names = gen_find(filepat, dirname)
    files = gen_open(names)
    lines = gen_cat(files)
    return lines


# Example use

if __name__ == '__main__':
    loglines = lines_from_dir("access-log*", "www")
    for line in loglines:
        print(line)
