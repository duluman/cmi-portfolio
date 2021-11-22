import numpy as np
from pprint import pprint


class A:
    def __init__(self, a=None):
        if a is None:
            self.a = np.zeros(shape=(10, 10))
        else:
            self. a = a

    def mark_as_visited(self, x, y):
        self.a[x, y] = 1

    def mark_as_empty(self, x, y):
        self.a[x, y] = 0


b = A()
print(b.a)

# b.mark_as_visited(8, 5)
b.mark_as_visited(3, 4)
print(b.a)
print(b.a[:, 3])
print(b.a[3, :])

b.mark_as_empty(3, 4)
print(b.a)
