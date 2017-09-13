import asyncio

def func(x, y):
    return x + y

@asyncio.coroutine
def do_func(x, y):
    yield from asyncio.sleep(1)
    return func(x, y)

loop = asyncio.get_event_loop()
result = loop.run_until_complete(do_func(2,3))
print("Got:", result)

