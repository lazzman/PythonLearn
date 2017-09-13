# genlog.py
#
# 计算在Apache日志文件中传输的总字节数
# 使用生成器表达式计算在Apache服务器日志中传输的字节数。

wwwlog = open("access-log")
bytecolumn = (line.rsplit(None, 1)[1] for line in wwwlog)
bytes = (int(x) for x in bytecolumn if x != '-')

'''
sum(iterable)
# Return the sum of a 'start' value (default: 0) plus an iterable of numbers
'''
print("Total", sum(bytes))
