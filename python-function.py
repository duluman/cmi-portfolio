def sum(n):
    s = 0
    for i in range(0, n+1):
        s += i
    return s

def sum2(n=10, b=10):
    print(f"b={b}")
    s = 0
    for i in range(0, n+1):
        s += i
    return s

def sum3(n:'int > 0'=10):
    s = 0
    for i in range(0, n+1):
        s += i
    return s, n

def is_even(n):
    return n % 2 == 0

def print_number_type(n, f):
    if f(n):
        print("Even")
    else:
        print("Odd")

def sum_even(n):
    s = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            s += i
    return s

def sum_odd(n):
    s = 0
    for i in range(0, n+1):
        if i % 2 == 1:
            s += i
    return s

def sum_odd_or_even(n, f):
    if f(n):
        return sum_even
    else:
        return sum_odd


sum1 = sum2()

s = sum2
print(s(20))

print_number_type(31, is_even)

summation = sum_odd_or_even(21, is_even)
print(summation(21))

from pack.module1 import isAnagram
from pack.module2 import fun
print(isAnagram('notea', 'tdone'))
print(fun())

def out_func(text):
    text = text 

    def inner_func():
        print(text)

    inner_func()

def sum_nested(n): 
    nin = n
    def sum_even():
        s = 0
        for i in range(0, nin+1):
            if i % 2 == 0:
                s += i
        return s

    def sum_odd():
        s = 0
        for i in range(0, nin+1):
            if i % 2 == 1:
                s += i
        return s 
    
    if nin % 2 == 0:
        return sum_even()
    else:
        return sum_odd()

print(sum_nested(10))
print(sum_nested(11))


def sum_clojure(n): 
    nin = n
    def sum_even():
        s = 0
        for i in range(0, nin+1):
            if i % 2 == 0:
                s += i
        return s

    def sum_odd():
        s = 0
        for i in range(0, nin+1):
            if i % 2 == 1:
                s += i
        return s 
    
    if nin % 2 == 0:
        return sum_even
    else:
        return sum_odd

f = sum_clojure(10)
print(f)
print(f())

registers = []

def register(func):
    print("I am in register")
    registers.append(func)
    return func

@register
def s():
    print("I am in S: Hello World")

@register
def s2():
    print("I am S2")
s()
s2()
print(registers)

def deco(func):
    def inner():
        return func() + 20
    return inner 

@register
@deco
def s3():
    return 10

print(s3())


