# genlog.py
#
# 计算在Apache日志文件中传输的总字节数
# 使用生成器表达式计算在Apache服务器日志中传输的字节数。

wwwlog = open("access-log")
bytecolumn = (line.rsplit(None, 1)[1] for line in wwwlog)  # 生成器对象，返回当前行中代表请求字节数的字段值
bytes = (int(x) for x in bytecolumn if x != '-')  # 生成器对象，将字节数字段字符串类型转为整数类型

'''
语法：
    sum(iterable)
返回值：
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
'''
print("总计字节数：", sum(bytes))
