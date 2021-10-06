# numbers
variable1 = 10
variable2 = 39.0
this_is_a_variable_name = 10

# strings
variable3 = 'aceasta este o variabila'
variable4 = "acesta este un string"
variable5 = f'acesta este un string {variable1}'
variable6 = variable3
# print(f'caracter pe pozitia 0: {variable6[0]}')
# print(f'caracter pe pozitia 7: {variable3[7]}')
# print(f'al 3lea caracter: {variable3[2]}')
# print(f'ultimul caracter: {variable3[-1]}')
# print(variable3[0:3])
# print(variable6[5:10])

variable7 = variable3.capitalize()
variable8 = variable7.upper()
variable9 = variable8.lower()
variable10 = variable3.split(" ")
variable11 = "_SEPARATOR_".join(variable10)

# print(variable7)
# print(variable8)
# print(variable10)
# print(variable11)

# sequences
# lists
l1 = [] 
l2 = list()
l3 = [1, 2, 'a', 'a', 'u', 100, 10.831, 'asdasd', [0, 100, 100]]
print(l3[2])
print(l3[-1])
l4 = l3[0:5]
print(l4)
l4[0] = 'new value'
print(l4)
print(l3)
l5 = l4
l5[0] = 'other new value'
print(l4, l5)
l1.append(1)
print(l1)
l1.insert(1, 0)
print(l1)
l1.insert(1, -1)
print(l1)
last_element_l1 = l1.pop()
print(l1, last_element_l1)
first_element_l1 = l1.pop(0)
print(l1, first_element_l1)
l4.remove('a')
l9 = [45, 6, 1, 314]
l10 = l9.sort()
print(l10, l9)
l11 = sorted(l9, reverse=True)
s1 = sorted(variable3)
print(s1)

# boolean
a = True
f = False 

# mappings 
d1 = {}
d2 = dict()
d3 = {
    0: 'smth',
    "name": "andrei",
    "age": 32,
    "country": "romania",
    "courses": [1, 3, 5, 10]
}
print(d3['name'])
d3['courses'].append(20)
print(d3['courses'])
print(d3.keys())
print(d3.values())
print(d3[list(d3.keys())[0:2]])

