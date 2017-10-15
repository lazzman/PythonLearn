# cm.py
#
# Context-manager example. See also contextlib.py in the standard library which
# addresses some rather tricky corner cases.

import sys


class GeneratorCM(object):
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, etype, val, tb):
        try:
            if etype is None:
                next(self.gen)
            else:
                self.gen.throw(etype, val, tb)
            raise RuntimeError("Generator didn't stop")
        except StopIteration:
            return True
        except:
            if sys.exc_info()[1] is not val: raise


def contextmanager(func):
    def run(*args, **kwargs):
        return GeneratorCM(func(*args, **kwargs))

    return run


# Simple Example
if __name__ == '__main__':
    import time


    @contextmanager
    def timethis():
        start = time.time()
        try:
            yield
        finally:
            end = time.time()
            print(end - start)


    with timethis():
        n = 1000000
        while n > 0:
            n -= 1

