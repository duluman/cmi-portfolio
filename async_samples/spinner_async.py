import asyncio

from async_samples.mini_module import mini_main

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(mini_main())
    loop.close()
