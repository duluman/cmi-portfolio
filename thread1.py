import threading
from time import sleep


def sum1():
    s = 0
    sleep(10)
    for i in range(0, 500000):
        # sleep(0.2)
        s += i
    return s


def sum2():
    s = 0
    for i in range(500000, 1000001):
        # sleep(0.5)
        s += i
    return s


if __name__ == "__main__":
    t1 = threading.Thread(target=sum1)
    t2 = threading.Thread(target=sum2)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # print(s1 + s2)