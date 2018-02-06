"""
未使用生成器，使用列表存储每个数字，比较耗内存
"""

def old_fib(n):
    res = [0] * n  # 创建长度为n的列表
    index = 0
    a = 0
    b = 1
    while index < n:
        res[index] = b
        a, b = b, a + b
        index += 1
    return res


print('-' * 10 + 'test old fib' + '-' * 10)
for fib_res in old_fib(20):
    print(fib_res)
