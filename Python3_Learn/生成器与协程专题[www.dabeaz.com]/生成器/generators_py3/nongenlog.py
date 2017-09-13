# nongenlog.py
#
# 计算在Apache日志文件中传输的总字节数
# 使用简单的for-loop计算Apache服务器日志中传输的字节数。不使用生成器。

wwwlog = open("access-log")
total = 0
for line in wwwlog:
    '''
    语法
        str.split(str="", num=string.count(str)).
    参数
        str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
        num -- 分割次数。
    返回值
        返回分割后的字符串列表。
    '''
    bytestr = line.rsplit(None, 1)[1]  # 以空字符分割字符串1次，得到的列表取第二个元素，代表每次请求的传输字节数
    if bytestr != '-':
        total += int(bytestr)

print("共计 %d Bytes" % (total,))
