import time
import threading
from functools import wraps
from queue import Queue

class Actor(threading.Thread):
    _registry = { }
    def __init__(self, name, gen):
        super().__init__()
        self.daemon = True
        self.gen = gen
        self.mailbox = Queue()
        Actor._registry[name] = self
        self.start()

    def send(self, msg):
        self.mailbox.put(msg)

    def run(self):
        while True:
            msg = self.mailbox.get()
            self.gen.send(msg)

def send(name, msg):
    Actor._registry[name].send(msg)

def actor(func):
    @wraps(func)
    def wrapper(*args, id=func.__name__, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return Actor(id, gen)
    return wrapper

@actor
def ping():
    while True:
        n = yield
        print('ping %d' % n)
        send('pong', n + 1)

@actor
def pong():
    while True:
        n = yield
        print('pong %d' % n)
        send('ping', n + 1)

if __name__ == '__main__':
    ping()
    pong()
    send('ping', 0)
    while True:
        time.sleep(1)

