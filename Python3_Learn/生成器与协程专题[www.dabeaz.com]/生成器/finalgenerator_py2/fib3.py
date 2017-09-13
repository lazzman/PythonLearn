# fib3.py
#
# Different thread execution model.  Here, the inlined future is constrained to a single
# execution thread.  You get the same performance, but control flow doesn't change threads.

from inline_future import inlined_future, run_inline_future
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import threading
import time

def run_inline_thread(gen):
    value = None
    exc = None
    while True:
        try:
            if exc:
                fut = gen.throw(exc)
            else:
                fut = gen.send(value)
            try:
                value = fut.result()
                exc = None
            except Exception as e:
                exc = e
        except StopIteration as exc:
            return exc.value

def fib(n):
    return 1 if n <= 2 else (fib(n-1) + fib(n-2))

@inlined_future
def compute_fibs(n):
    result = []
    for i in range(n):
#        print(threading.current_thread())    # Uncomment to see weirdness
        val = yield from pool.submit(fib, i)
        result.append(val)
    return result

pool = ProcessPoolExecutor(4)

start = time.time()
result = run_inline_future(compute_fibs(34))
result = run_inline_future(compute_fibs(34))
end = time.time()
print("Sequential:", end-start)

tpool = ThreadPoolExecutor(8)
start = time.time()
t1 = tpool.submit(run_inline_thread, compute_fibs(34))
t2 = tpool.submit(run_inline_thread, compute_fibs(34))
result1 = t1.result()
result2 = t2.result()
end = time.time()
print("Parallel:", end-start)



