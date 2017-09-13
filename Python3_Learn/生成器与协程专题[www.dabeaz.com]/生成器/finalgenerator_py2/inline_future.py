# inline_future.py
#
# Final implementation

from concurrent.futures import Future
import inspect

def patch_future(cls):
    def __iter__(self):
        if not self.done():
            yield self
        return self.result()
    cls.__iter__ = __iter__

patch_future(Future)

class Task(Future):
    def __init__(self, gen):
        super().__init__()
        self._gen = gen

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            # Set the result of the task (return value from generator)
            self.set_result(exc.value)

    def _wakeup(self, fut):
        try:
            result = fut.result()
            self.step(result, None)
        except Exception as exc:
            self.step(None, exc)

def inlined_future(func):
    assert inspect.isgeneratorfunction(func)
    return func

def start_inline_future(fut):
    t = Task(fut)
    t.step()
    return t

def run_inline_future(fut):
    t  = start_inline_future(fut)
    return t.result()

# ------- Example
if __name__ == '__main__':
    import time
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=8)

    def func(x, y):
        time.sleep(1)
        return x + y

    @inlined_future
    def do_func(x, y):
        try:
            result = yield pool.submit(func, x, y)
            return result
        except Exception as e:
            print('Failed:', repr(e))

    @inlined_future
    def after(delay, fut):
        '''
        Run a future after a time delay.
        '''
        yield from pool.submit(time.sleep, delay)
        result = yield from fut
        return result

    result = run_inline_future(do_func(2,3))
    print('Result:', result)

    result = run_inline_future(after(10, do_func(2,3)))
    print('Result:', result)
