variable1 = 23
variable2 = "aceasta este o variabla"

# numbers
variable3 = 30
variable4 = 33.22
variable5 = 0.0000000001
print(variable5)

# boolean 
variable6 = True 
variable7 = False 

# strings
variable8 = "acesta este un text intre ghilimele 3434 %%£@ if for def"
variable9 = 'fsrtdfsdjfksd fdkslfkdls fdkslfkds fsdlfkdslfk fdsfsd erwerewrew ewrwre309420490234923 irulgk'
variable10 = variable8.upper()
variable11 = variable8.find("este")
print(variable11)
variable8 = 'dksajdkjsad'
print(variable8)

# sequences
# lists 
l1 = [1, 2, 3, "string", True, False, 23.0, 22.10]
el1 = l1[2]
l1[0] = "first element"
l1[-1] = "last element"
els = l1[2:5]

print(el1)
print(l1)
print(els)

l1.append("appended element")

l2 = [2, 324, 121, 99]
l2.sort(reverse=True)
print(l2)

# mappings
d1 = {
    "name": "andrei",
    "age": 32,
    "country": "romania",
    1: "ceva valoare" 
}
d2 = {
    "name": "ii",
    "age": 33,
    "country": "romania",
    1: "alta valoare" 
}
d1["country"] = "ro"

d1.update({2: "a"})
print(d1)


print(d1["country"])
l3 = [d1, d2]

print( l3[1]["country"] )

# logical operators
# a == b a is equal to b 
# a != b a is not equal to b
# a > b a is greater than b
# a >= b a is greater than or equal to b
# a <= b a is less than or equal to b
# not True --> False 
# not ((a == b) and ((c > d) or (c == a))))
# and --> True iff ambii termeni sunt adevarati
# or --> sau False iff ambii termeni sunt falsi 

# arithmetic operators
# + ( a + b )
# - ( a - b )
# / ( a / b )
# * ( a * b )
# ** ( a ** b )
# % ( restul impartirii celor doua numere, eg 3 % 2 = 1) 
# a % 2 == 0 --> check if a is even
# a % 2 == 1 --> check if a is odd

# if elif else
# daca a % 2 == 0
#   print(a)
#   a = a * 2
# altfel
#   print(a)
#   a = a * 3
a = 11
if a % 2 == 0:
    print('is even', a)
    a = a * 2
elif a % 2 == 1 and a > 10:
    print('is odd & greater than 10', a)
else:
    print('is odd', a)
    a = a * 3
print(a)

# for
# pentru fiecare element din sequence
#   executa instructiunile de aici
# pentru a intre 1 si 10
#   executa intructiunile de aici
for i in l3:
    print(i)

for i in range(0, 10):
    print(i, i*2)

if a % 2 == 1:
    for i in range(0, a):
        print(i)

for i in range(0, a):
    if i % 2 == 1:
        print(i)

# while 
# cat timp ceva este adevarat
#   executa instructiunile de aici

while a > 0:
    print(a)
    a = a - 1 

# sequences bonus 
# tuples
t1 = (1, 2, 3, 2, 2)
print('tuple', t1[2])
print(t1.count(2))
print(t1.index(3))

# set
s1 = {1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1}
print(s1)
s1.add(3)
print(s1.difference({2,2,11}))
print(s1.union({2,2,11}))