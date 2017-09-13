# actor1.py
#
# Simple attempt at actors

_registry = { }

def send(name, msg):
    _registry[name].send(msg)

def actor(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        _registry[func.__name__] = gen
    return wrapper

if __name__ == '__main__':
    @actor
    def printer():
        while True:
            msg = yield
            print('printer:', msg)

    printer()
    n = 10
    while n > 0:
        send('printer', n)
        n -= 1
