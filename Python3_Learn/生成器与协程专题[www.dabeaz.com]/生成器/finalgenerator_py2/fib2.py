# fib2.py
#
# Performance test (GIL!)

from inline_future import inlined_future, run_inline_future, start_inline_future
from concurrent.futures import ProcessPoolExecutor
import threading
import time

def fib(n):
    return 1 if n <= 2 else (fib(n-1) + fib(n-2))

@inlined_future
def compute_fibs(n):
    result = []
    for i in range(n):
        # print(threading.current_thread())    # Uncomment to see weird thread switching
        val = yield from pool.submit(fib, i)
        result.append(val)
    return result

pool = ProcessPoolExecutor(4)

start = time.time()
result1 = run_inline_future(compute_fibs(34))
result2 = run_inline_future(compute_fibs(34))
end = time.time()
print("Sequential:", end-start)

start = time.time()
t1 = start_inline_future(compute_fibs(34))
t2 = start_inline_future(compute_fibs(34))
result1 = t1.result()
result2 = t2.result()
end = time.time()
print("Parallel:", end-start)
