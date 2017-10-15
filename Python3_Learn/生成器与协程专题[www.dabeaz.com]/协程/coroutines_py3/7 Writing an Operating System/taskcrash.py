# taskcrash.py
# Python实现操作系统-演示任务意外终止调度器未处理的情况
# An example that shows how the initial scheduler doesn't handle
# task termination correctly.

from pyos2 import Scheduler


def foo():
    for i in range(10):
        print("I'm foo", i)
        yield


def bar():
    while True:
        print("I'm bar")
        yield


sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()
