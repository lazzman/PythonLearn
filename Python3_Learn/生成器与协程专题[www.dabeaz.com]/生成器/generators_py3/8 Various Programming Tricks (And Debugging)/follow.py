# follow.py
# 实现tail -f命令来监视文件追加的新内容
# Follow a file like tail -f.

import time

'''
概述
seek() 方法用于移动文件读取指针到指定位置。
语法
seek() 方法语法如下：
fileObject.seek(offset[, whence])
参数
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
返回值
该函数没有返回值。
'''


# 返回文件追加的行的序列
def follow(thefile):
    thefile.seek(0, 2)  # 游标移动到文件末尾
    while True:
        line = thefile.readline()
        if not line:  # 没有新的内容，则自动休眠0.1s
            time.sleep(0.1)
            continue
        yield line


# Example use
# Note : This example requires the use of an apache log simulator.
#
# Go to the directory run/foo and run the program 'logsim.py' from
# that directory.   Run this program as a background process and
# leave it running in a separate window.  We'll write program
# that read the output file being generated
#

if __name__ == '__main__':
    logfile = open("access-log", "r")
    loglines = follow(logfile)
    for line in loglines:
        print(line)
