# inline_recursive.py
#
# Bizarre inline recursive example

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

# Example
if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor
    import time

    pool = ThreadPoolExecutor(max_workers=8)

    def recursive(n):
        yield pool.submit(time.sleep, 0.001)
        print('Tick:', n)
        Task(recursive(n+1)).step()

    Task(recursive(0)).step()
