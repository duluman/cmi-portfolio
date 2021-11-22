import threading
from time import sleep

s = 0


def sum1():
    global s

    for i in range(0, 500000):
        sleep(5)
        s += i


def sum3():
    global s

    for i in range(0, 500000):
        sleep(1)
        s += i


def sum2():
    global s

    for i in range(500000, 1000001):
        sleep(0.1)
        s += i


# sum1()
# print(f"Sum up to 500k = {s}")
# sum2()
# print(f"Sum up to 1mil = {s}")


# s = 0
t1 = threading.Thread(name='sum1', target=sum1)
t2 = threading.Thread(name='sum2', target=sum2)

print(t1)
print(t2)

t1.run()
t2.run()

# t1.join()
# t2.join()

print(s)