# genopen.py
# 生成器-返回解压后的gz与bz2文件对象序列
# Takes a sequence of filenames as input and yields a sequence of file
# objects that have been suitably open

import gzip, bz2


# 生成器-自动解压文件列表中的压缩文件并返回文件对象序列
def gen_open(filenames):
    for name in filenames:
        if name.endswith(".gz"):
            yield gzip.open(name)
        elif name.endswith(".bz2"):
            yield bz2.BZ2File(name)
        else:
            yield open(name)


# Example use
if __name__ == '__main__':
    from genfind import gen_find

    lognames = gen_find("access-log*", "www")
    logfiles = gen_open(lognames)
    for f in logfiles:
        print(f)
