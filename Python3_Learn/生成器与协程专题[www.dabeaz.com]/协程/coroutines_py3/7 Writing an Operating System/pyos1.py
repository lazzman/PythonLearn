# ------------------------------------------------------------
# pyos1.py  -  The Python Operating System
# python实现操作系统-1.多任务
# Step 1: Tasks
# ------------------------------------------------------------

# This object encapsulates a running task.
# 该对象封装正在运行的任务
class Task(object):
    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid  # Task ID
        self.target = target  # Target coroutine
        self.sendval = None  # Value to send

    # Run a task until it hits the next yield statement
    def run(self):
        return self.target.send(self.sendval)


# ------------------------------------------------------------
#                       == Example ==
# ------------------------------------------------------------
if __name__ == '__main__':
    # A simple generator/coroutine function
    def foo():
        print("Part 1")
        yield
        print("Part 2")
        yield


    t1 = Task(foo())
    print("Running foo()")
    t1.run()
    print("Resuming foo()")
    t1.run()

    # If you call t1.run() one more time, you get StopIteration.
    # Uncomment the next statement to see that.

    # t1.run()
