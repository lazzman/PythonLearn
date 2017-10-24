# ------------------------------------------------------------
#                       === Tasks === 任务
# ------------------------------------------------------------
class Task(object):
    # 全局计数器
    taskId = 0

    # 构造方法
    def __init__(self, target):
        Task.taskId += 1
        self.tid = Task.taskId  # 当前任务ID
        self.target = target  # 目标协程
        self.sendvalue = None  # 发送到协程中的值

    # 运行协程任务直到协程中使用yield返回
    def run(self):
        return self.target.send(self.sendvalue)


# ------------------------------------------------------------
#                      === Scheduler === 任务调度
# ------------------------------------------------------------
from queue import Queue


class Scheduler(object):
    def __init__(self):
        self.ready = Queue()  # 准备执行的任务队列
        self.taskmap = {}  # 保存活着的的任务key是任务ID,value是任务实例

        self.exit_waiting = {}  # 等待其他任务执行完毕后执行

    # 向任务调度中添加一个新任务
    def new(self, target):
        newtask = Task(target)  # 创建一个任务实例
        self.taskmap[newtask.tid] = newtask  # 存入要执行的任务
        self.scheduler(newtask)
        return newtask.tid

    # 将任务放入到准备队列
    def scheduler(self, task):
        self.ready.put(task)

    # 任务退出
    def exit(self, task):
        print('Task %d terminated' % (task.tid,))
        self.taskmap.pop(task.tid)

    # 任务调度循环（从准备队列中取出任务执行，直到任务执行到yield语句，yield<==>traps）[任务的执行顺序是根据队列中任务的存放顺序，先进先出FIFO]
    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
                # 如果返回的是系统调用实例，就做一些代表系统调用的任务
                if isinstance(result, SystemCall):
                    result.task = task
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)  # 如果任务执行完毕则删除任务
                continue  # 任务调度继续
            self.scheduler(task)


# ------------------------------------------------------------
#                   === System Calls === 系统调用
# ------------------------------------------------------------

# 系统调用的父类，所有的系统调用都要继承此类
class SystemCall(object):
    def handle(self):
        pass


# 获取用户任务Id的系统调用
class GetTid(SystemCall):
    # 从用户任务中取得tid，并将用户任务再次加入到任务准备队列，当用户任务再次run()时，将会取的tid
    def handle(self):
        self.task.sendvalue = self.task.tid  # 将用户任务tid返回到用户任务
        self.sched.scheduler(self.task)  # 将用户任务再次加入到任务准备队列


# 创建一个新的用户任务
class NewTask(SystemCall):
    def __init__(self, target):
        self.target = target

    def handle(self):
        tid = self.sched.new(self.target)  # 调用scheduler添加一个新任务
        self.sched.scheduler(self.task)  # 将任务添加到任务队列
        self.task.sendval = tid  # 将新建的任务tid返回到原本用户任务


# 根据tid终止用户任务
class KillTask(SystemCall):
    def __init__(self, tid):
        self.tid = tid

    def handle(self):
        task = self.sched.taskmap.get(self.tid, None)
        if task:
            task.target.close()  # 关闭任务(关闭生成器)
            self.task.sendvalue = True
        else:
            self.task.sendvalue = False
        self.sched.scheduler(self.task)  # 将用户任务再次加入到任务准备队列


if __name__ == '__main__':
    import itertools

    # count()会创建一个从0开始无限递增的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出
    natuals = itertools.count(0)

    '''
    # Two tasks
    def foo():
        for n in natuals:
            print("%d I'm foo" % (n,))
            yield
    '''


    def foo():
        # 此处先执行系统调用，执行完毕后将系统调用返回值返回到当前任务中的mytid
        mytid = yield GetTid()
        print('SystemCall=>foo tid: %s' % (mytid,))
        for n in natuals:
            print("%d I'm foo" % (n,))
            yield


    def bar():
        # 通过系统调用获取当前任务的tid
        mytid = yield GetTid()
        print('SystemCall=>bar tid: %s' % (mytid,))
        # 通过系统调用创建一个新的用户任务
        newtid = yield NewTask(foo())
        print('SystemCall=>NewTask crate a new task , tid : %s' % (newtid,))
        for i in range(10):
            print("%d I'm bar" % (i,))
            yield
        # 通过系统调用关闭上面新建的用户任务
        success = yield KillTask(newtid)
        if success:
            print('SystemCall=>KillTask task success, tid : %s' % (newtid,))
        else:
            print('SystemCall=>KillTask task fail, tid : %s' % (newtid,))


    # Run them
    sched = Scheduler()
    # sched.new(foo())
    sched.new(bar())
    sched.mainloop()
