# consumer.py
# 自动调用generator的next()方法的装饰器，常用于装饰协程生成器
# consumer decorator and co-routine example

# 装饰器，自动调用被装饰的生成器的next方法
def consumer(func):
    def start(*args, **kwargs):
        c = func(*args, **kwargs)
        next(c)
        return c

    return start


# Example
if __name__ == '__main__':

    @consumer
    def recv_count():
        try:
            while True:
                n = (yield)
                print("T-minus", n)
        except GeneratorExit:
            print("Kaboom!")


    # 创建生成器对象
    r = recv_count()
    for i in range(5, 0, -1):
        r.send(i)

    # 关闭生成器
    r.close()
