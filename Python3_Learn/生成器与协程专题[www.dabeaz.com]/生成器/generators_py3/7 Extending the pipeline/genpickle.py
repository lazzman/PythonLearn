# genpickle.py
# 将一个对象序列中的对象序列化为字符串
# Turn a sequence of objects into a sequence of pickle strings

import pickle


# 将对象序列 序列化为 字符串序列
def gen_pickle(source):
    for item in source:
        yield pickle.dumps(item)


# 从文件中读取字符串序列并反序列化为对象
def gen_unpickle(infile):
    while True:
        try:
            item = pickle.load(infile)
            yield item
        except EOFError:
            return
