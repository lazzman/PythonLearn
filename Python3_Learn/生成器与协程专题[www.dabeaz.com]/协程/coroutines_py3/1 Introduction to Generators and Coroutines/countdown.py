# countdown.py
# 一个简单的生成器函数
# A simple generator function

def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1
    print("Done counting down")


# Example use
if __name__ == '__main__':
    for i in countdown(10):
        print(i)
