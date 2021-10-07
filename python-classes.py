class Person:
    c = 1

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.location = city
        self._secret = "secret"
        self.__secret = "reaaaally secret"

    def whoami(self):
        print(f"I am {self.name} and I am {self.age} years old. I live in {self.location}")

    def present(self):
        print("Allow me to introduce myself.")
        self.whoami()

    def change_name(self, new_name):
        self.name = new_name
        self.whoami()

    def tell_me_your_secret(self):
        print(self.__secret, self._secret)

    def __secret_method(self):
        print(self.__secret)

    @staticmethod
    def st():
        print("ss")

    @classmethod
    def cls_meth(cls, a):
        print(cls)

class Adult(Person):
    def __init__(self, name, age, city, address):
        super().__init__(name, age, city)
        self.address = address

class OldPerson(Adult):
    def __init__(self, name, age, city, address):
        super().__init__(name, age, city, address)


p1 = Person('andrei', 32, 'tgjiu')
p1.present()
p1.change_name("liviu")
p1.tell_me_your_secret()
print(p1._secret)
# print(p1.__secret)
# p1.__secret_method()

a1 = Adult('andrei', 32, 'tgjiu', 'acasa')
a1.whoami()
print(a1.address)

p2 = Person("liviu", 32, 'tgjiu')

print(f"p1.c = {p1.c}")
print(f"p2.c = {p2.c}")

Person.c += 2

print(f"p1.c = {p1.c}")
print(f"p2.c = {p2.c}")

p3 = Person("sa", 33, 'sada')
print(p3.c)
p3.c = 20
print(p3.c)

class Palindrom:

    def __init__(self, s):
        self.__s = s

    def is_palindrom(self):
        return self.__s == self.__s[::-1]

    def enter_string(self, s):
        self.__s = s

    def get_string(self):
        return self.__s
        

p = Palindrom('ana')
print(p.is_palindrom())

p2 = Palindrom('root')
print(p2.is_palindrom())

p.enter_string('sadas')
print(f"{p.get_string()} is palindrom = {p.is_palindrom()}")

