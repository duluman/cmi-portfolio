import asyncio


async def print_smth():
    while True:
        print("...Smth...")
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break


async def async_func(n):
    for i in range(n):
        await asyncio.sleep(1)
        yield i


async def main():
    t = asyncio.create_task(print_smth())
    async for i in async_func(10):
        print(f"Result = {i}")
    t.cancel()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
