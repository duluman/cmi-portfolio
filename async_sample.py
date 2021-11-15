# generators
from datetime import datetime

import aiohttp
import requests


def squared(n):
    n_squared = []
    for i in range(n):
        n_squared.append(i * i)
    return n_squared


def squared_gen(n):
    for i in range(n):
        yield i * i


# async
import asyncio
from random import randint


async def print_hello(name, n):
    for i in range(n):
        time_to_wait = randint(1, 10)
        print(f"Hello {name}, I am counting to {n}. I am at {i}. Will wait for {time_to_wait}")
        await asyncio.sleep(time_to_wait)


async def fetch(session, url):
    async with session.get(url) as resp:
        r = await resp.json()
        return r


async def fetch_all(cities):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for city in cities:
            tasks.append(
                fetch(
                    session,
                    f"https://geo.api.gouv.fr/communes?nom={city}&fields=nom,region&format=json&geometry=centr",
                )
            )
        resps = await asyncio.gather(*tasks, return_exceptions=True)
        return resps


def fetch_all_classic(cities):
    resps = []
    with requests.session() as session:
        for city in cities:
            resp = session.get(f"https://geo.api.gouv.fr/communes?nom={city}&fields=nom,region&format=json&geometry=centr")
            resps.append(resp.json())
        return resps


def run_async(cities):
    resps = asyncio.run(fetch_all(cities))
    return resps


def run(cities):
    return fetch_all_classic(cities)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    tasks = [
        asyncio.ensure_future(print_hello("Andrei", 10)),
        asyncio.ensure_future(print_hello("Liviu", 20))
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    # cities = ['paris', 'brux', 'bro', 'mars', 'nice'] * 50
    # t0 = datetime.now()
    # run_async(cities)
    # t1 = datetime.now()
    # print(f"Async {(t1 - t0).seconds}")
    # t0 = datetime.now()
    # run(cities)
    # t1 = datetime.now()
    # print(f"Classic {(t1 - t0).seconds}")
    # loop.close()