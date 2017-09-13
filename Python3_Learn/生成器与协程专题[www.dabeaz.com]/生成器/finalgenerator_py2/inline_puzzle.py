# inline_puzzle.py
#
# Various attempts at making library functions work (puzzler)

class Task:
    def __init__(self, gen):
        self._gen = gen

    def step(self, value=None, exc=None):
        try:
            if exc:
                fut = self._gen.throw(exc)
            else:
                fut = self._gen.send(value)
            fut.add_done_callback(self._wakeup)
        except StopIteration as exc:
            pass

    def _wakeup(self, fut):
        try:
            result = fut.result()
            self.step(result, None)
        except Exception as exc:
            self.step(None, exc)

# ------- Example
if __name__ == '__main__':
    import time
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=8)

    def func(x, y):
        time.sleep(1)
        return x + y

    def do_func(x, y):
        try:
            result = yield pool.submit(func, x, y)
            print('Got:', result)
        except Exception as e:
            print('Failed:', repr(e))

    def example1():
        '''
        Broken. The 'yield fut' statement doesn't produce a proper Future object
        '''
        def after(delay, fut):
            '''
            Run a future after a time delay.
            '''
            yield pool.submit(time.sleep, delay)
            yield fut

        Task(after(10, do_func(2, 3))).step()

    def example2():
        '''
        Broken.  Runs, but result gets lost.
        '''
        def after(delay, fut):
            '''
            Run a future after a time delay.
            '''
            yield pool.submit(time.sleep, delay)
            for f in fut:
                yield f

        Task(after(10, do_func(2, 3))).step()

    def example3():
        '''
        Works, but solution not obvious.
        '''
        def after(delay, fut):
            '''
            Run a future after a time delay.
            '''
            yield pool.submit(time.sleep, delay)
            try:
                while True:
                    f = fut.send(result)
                    result = yield f
            except StopIteration:
                pass

        Task(after(10, do_func(2, 3))).step()

    def example4():
        '''
        Works, using yield from.  But "yield" and "yield from" both used
        '''
        def after(delay, fut):
            '''
            Run a future after a time delay.
            '''
            yield pool.submit(time.sleep, delay)
            yield from fut

        Task(after(10, do_func(2, 3))).step()

    def example5():
        '''
        Does not work. Can't use "yield from" everywhere
        '''
        def after(delay, fut):
            '''
            Run a future after a time delay.
            '''
            yield from pool.submit(time.sleep, delay)
            yield from fut

        Task(after(10, do_func(2, 3))).step()

