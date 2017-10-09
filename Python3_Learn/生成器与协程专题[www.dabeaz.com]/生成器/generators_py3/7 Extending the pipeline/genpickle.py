# genpickle.py
# 将一个对象序列中的对象序列化为字符串
# Turn a sequence of objects into a sequence of pickle strings

import pickle


# 将对象序列 序列化为 字符串序列
def gen_pickle(source):
    for item in source:
        yield pickle.dumps(item)


# 读取字符串序列并反序列化为对象
def gen_unpickle(infile):
    while infile:
        try:
            item = pickle.loads(infile)
            yield item
            infile = None
        except EOFError:
            return
