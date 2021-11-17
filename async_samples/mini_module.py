import asyncio
import itertools
import sys
from random import randint


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    write('\n..SPINNING...')
    for char in itertools.cycle('|/-\\'):
        status = char + " " + msg + "\n"
        write(status)
        flush()
        write('\x80' * len(status))
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break
    write('\n..SPINNING DONE.' + '\x80' * len(status))


async def slow_function():
    for i in range(2):
        await asyncio.sleep(randint(1, 4))
        yield i


async def supervisor():
    spinner = asyncio.create_task(spin("thinking!"))
    print('spinner object: ', spinner)
    async for i in slow_function():
        result = i
        yield result
    spinner.cancel()


async def mini_main():
    async for result in supervisor():
        print("\n..SPINNER PAUSED... Answer: ", result)
    print("Hello")