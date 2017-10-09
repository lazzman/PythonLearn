# fieldmap.py
# 将字典序列中对应key的值再加工
# Take a sequence of dictionaries and remap one of the fields

def field_map(dictseq, name, func):
    '''
        dictseq 字典序列
        name 字典中的key
        func 处理value的函数
        '''
    for d in dictseq:
        d[name] = func(d[name])
        yield d


# Example

if __name__ == '__main__':

    loglines = open("access-log")

    import re

    # 匹配模式
    logpats = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
              r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

    logpat = re.compile(logpats)

    groups = (logpat.match(line) for line in loglines)

    # 分组匹配提取字段
    tuples = (g.groups() for g in groups if g)

    # 字段对应的key
    colnames = ('host', 'referrer', 'user', 'datetime',
                'method', 'request', 'proto', 'status', 'bytes')

    # 将元组序列转换为字典序列
    log = (dict(zip(colnames, t)) for t in tuples)

    # 将字典序列中'status'对应的值转换为int类型
    log = field_map(log, "status", int)

    # 将字典序列中'bytes'对应的值转换为int类型
    log = field_map(log, "bytes",
                    lambda s: int(s) if s != '-' else 0)

    for x in log:
        print(x)
