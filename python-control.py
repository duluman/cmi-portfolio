a = 3 + 4
b = 5 > 4
c = ((3 + 4) * (32 + 4)) > 0
d = a == b # is equal to 
e = a != b # is not equal to
f = a >= b # is greater or equal
g = b <= a # is less or equal
h = not True # equivalent to False
i = not a > b 

# if elif else
if a > 10: # if conditie: 
    a = a + 1 # a += 1
    b = 10
    c = 1000
elif a == 7:
    a = a * 2
elif a < 3: 
    a = 4 * a
else:
    a = a - 1 # a -= 1
    print(b, c)

print(a)

# for
# c = 0
# pentru fiecare element din lista, adauga 1 la valoarea lui c

# pentru fiecare utilizator:
#   daca numele == "andrei":
#        numele = "andrei modificat"

# pentru fiecare numar de la 1 la 100:
#   calculeaza numar * numar
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = 0
for element in l:
    c += 1
print(c)

# while
# cat timp a > 0:
#   a -= 1
#   b *= 2
a = 5
b = 2
print(a, b)
while a > 0:
    a -= 1
    b = b * 2 # b *= 2
print(a, b)

for e1 in l:
    if e1 == 2:
        continue
    if e1 == 3:
        break
    for e2 in l:
        print(e1, e2, e1 * e2)

a = 6
b = 2
if a == 7:
    for e in l:
        print(a * e)
else:
    while not False:
        print(c)
        break

