# apachelog.py
# 将apache日志文件解析为结构化数据（字典）
# Parse an apache log file into a sequence of dictionaries

from fieldmap import *

'''
re.match函数
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
函数语法：
re.match(pattern, string, flags=0)
函数参数说明：
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
匹配成功re.match方法返回一个匹配的对象，否则返回None。
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
匹配对象方法	描述
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''

'''
re.search方法
re.search 扫描整个字符串并返回第一个成功的匹配。
函数语法：
re.search(pattern, string, flags=0)
函数参数说明：
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
匹配成功re.search方法返回一个匹配的对象，否则返回None。
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
匹配对象方法	描述
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''


def apache_log(lines):
    '''
    :param lines:日志内容行序列
    :return:
    '''

    import re

    # 分组匹配模式
    logpats = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
              r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

    # 编译为模式对象
    logpat = re.compile(logpats)

    # 返回匹配对象的序列
    groups = (logpat.match(line) for line in lines)

    # 返回分组匹配后的元组序列(排除不匹配的对象)
    tuples = (g.groups() for g in groups if g)

    colnames = ('host', 'referrer', 'user', 'datetime',
                'method', 'request', 'proto', 'status', 'bytes')

    # 元组换字典
    log = (dict(zip(colnames, t)) for t in tuples)

    # 字典值类型转换
    log = field_map(log, "status", int)

    # 字典值类型转换
    log = field_map(log, "bytes",
                    lambda s: int(s) if s != '-' else 0)
    # 返回结果序列
    return log


# Example use:

if __name__ == '__main__':
    from linesdir import *

    lines = lines_from_dir("access-log*", "www")
    log = apache_log(lines)
    for r in log:
        print(r)
