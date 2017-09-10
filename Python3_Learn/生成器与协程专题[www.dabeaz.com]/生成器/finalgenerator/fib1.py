# fib1.py
#
# Initial fibonacci example using inline futures

from inline_future import inlined_future, run_inline_future
from concurrent.futures import ProcessPoolExecutor

def fib(n):
    return 1 if n <= 2 else (fib(n-1) + fib(n-2))

@inlined_future
def compute_fibs(n):
    result = []
    for i in range(n):
        val = yield from pool.submit(fib, i)
        result.append(val)
    return result


pool = ProcessPoolExecutor(4)
result = run_inline_future(compute_fibs(35))
print(result)
