from datetime import datetime


def func_without_yield(n):
    l = []
    for i in range(n):
        l.append(i)
    return l


def func_with_yield(n):
    for i in range(n):
        yield i


if __name__ == "__main__":
    t0 = datetime.now()
    l1 = func_without_yield(100)
    t1 = datetime.now()
    print(f"Duration func_without_yield = {(t1-t0).microseconds}")

    t0 = datetime.now()
    l2 = func_with_yield(10)
    t1 = datetime.now()
    print(f"Duration func_with_yield = {(t1 - t0).microseconds}")

    # print(f"Result from func_without_yield = {l1}")
    # print(f"Result from func_with_yield = {l2}")

    r1 = next(l2)
    print(f"Result from func_with_yield = {r1}")
    r2 = next(l2)
    print(f"Result from func_with_yield = {r2}")
    r3 = list(l2)
    print(f"Result from func_with_yield = {r3}")
    r1 = next(l2)
    print(f"Result from func_with_yield = {r1}")

