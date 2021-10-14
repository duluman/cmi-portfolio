def sum(n):
    s = 0
    for i in range(0, n+1):
        s += i
    return s

def add(a, b=2, c=10):
    return a + b + c

def print_result(result):
    print(result)

def hello_world():
    print("Hello World!")

s = sum(10)
print(s)

a = add(2, 5)
print(a)

a2 = add(3)
print(a2)

a3 = add(3, 4)
print(a3)

r = print_result("result")
print(r)


f = sum
print(f(4))

print("Functions as part of lists")
l = [sum, add, print_result]
for fi in l:
    s = fi(2)
    print(s)

d = {
    'sum': sum,
    'add': add
}
print(d['add'](1,2,3))

print("Functions as params")

def is_odd(n):
    return n % 2 == 1

def is_even(n):
    return n % 2 == 0

def sum_by_condition(n, f):
    s = 0
    for i in range(0, n+1):
        if f(i):
            s += i
    return s

s1 = sum_by_condition(10, is_even)
s2 = sum_by_condition(10, is_odd)

print(s1)
print(s2)

print("Functions as return values")
def product(n, is_even):
    p = 1
    for i in range(1, n+1):
        if is_even(i):
            p *= i
    return p, is_even

p = product(is_even=is_even, n=10)
print(p)

f = lambda x, y: x + y
filt = lambda x: x > 5

print(f(1,2))

l = [1, 2, 3, 4, 5, 6, 7, 8]
m = map(lambda x: x**2, l)
print(m)
r = filter(is_even, m)
print(r)
for i in r:
    print(i)
print(r)

def f(a):
    a = a
    def pow2():
        return a**2

    return pow2()

def g(a):
    a = a
    def pow3():
        return a**3

    return pow3

print(f(3))

g1 = g(3)
print(g1())

registers = []
def h(f):
    def w():
        print(f"h: {f() + 2}")
        return f() + 2
    return w

def g(f):
    def w():
        print(f"g: {f() + 5}")
        return f() + 5
    return w

def i(f):
    def w():
        print(f"i: {f() + 10}")
        return f() + 10
    return w

@h
def t():
    return 2**4

@h
def u():
    return 3**5

@h
def v():
    return 2**6


# print("decorators")
# print(t())
# print(v())
# print(u())

def decorator_with_params():
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator

@decorator_with_params()
def x(a):
    return a ** 10

# print(x(2))



@h
@g
@i
def f():
    return 10

print(f())