# recvcount.py
# 协程
# Example of a co-routine

def recv_count():
    try:
        while True:
            n = (yield)
            print("T-minus", n)
    # 调用close()方法，会向生成器对象抛出GeneratorExit异常，可以在生成器内部捕获该异常并处理
    except GeneratorExit as g:
        print("Kaboom!")


# 创建一个generator对象
r = recv_count()

# 调用next()方法
# r.next() python3.x不支持这种写法
next(r)

# range(start, stop[, step]) -> range object => [5,4,3,2,1]
for i in range(5, 0, -1):
    # 将i的值付给n -> n = (yield)
    r.send(i)

# 调用close()方法，会向生成器对象抛出GeneratorExit异常，可以在生成器内部捕获该异常并处理
r.close()
