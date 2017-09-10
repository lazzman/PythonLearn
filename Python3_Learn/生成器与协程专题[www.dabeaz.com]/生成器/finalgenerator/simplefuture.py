# simplefuture.py
#
# Illustration of a future

from concurrent.futures import ThreadPoolExecutor

def func(x, y):
    'Some function. Nothing too interesting.'
    import time
    time.sleep(5)
    return x + y

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=8)

    def example1():
        '''
        Blocking. Wait for result.
        '''
        fut = pool.submit(func, 2, 3)
        r = fut.result()
        print('Got:', r)

    def example2():
        '''
        Blocking. With exception handling.
        '''
        fut = pool.submit(func, 2, 'Hello')
        try:
            r = fut.result()
            print('Got:', r)
        except Exception as e:
            print('Whoops:', e)

    def example3():
        '''
        With callback.
        '''
        fut = pool.submit(func, 2, 3)
        fut.add_done_callback(result_handler)

    def result_handler(fut):
        try:
            result = fut.result()
            print('Got:', result)
        except Exception as e:
            print('Whoops:', e)


    example1()
    example2()
    example3()
