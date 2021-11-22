import concurrent.futures
from time import sleep


def sum1(n, name):
    s = 0
    for i in range(n):
        # print(f"THREAD {name} ---> s = {s}")
        s += i
        sleep(0.5)
    return s


tasks = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    k = 10
    while k:
        n = int(input("Please enter a number: "))
        future = executor.submit(sum1, n, str(k))
        tasks.append((n, future))
        k = k - 1

for n, task in tasks:
    print(f"n = {n} --- result = {task.result()}")
print("Done!")
