# gencat.py
# 从多种文件对象中获取日志的每一行内容的序列
# Concatenate multiple generators into a single sequence

def gen_cat(sources):
    for s in sources:
        for item in s:
            # 由于解压后的文件内容编码是bytes类型，需要进一步判断与处理
            if isinstance(item, bytes):
                item = str(item, 'utf-8')
            yield item


# Example use
if __name__ == '__main__':
    from genfind import gen_find
    from genopen import gen_open

    lognames = gen_find("access-log*", "www")
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)
    for line in loglines:
        print(line)
