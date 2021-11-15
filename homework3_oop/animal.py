"""
    Create a class "Animal". You will use this class later to extend it
    with other types of animals.
    This should be an abstract class (no functionality, only works as an
    interface for the other classes). https://docs.python.org/3/library/abc.html
    public attributes:
        - color: str
        - age: int
        - animal_type: Enum (https://docs.python.org/3/library/enum.html)
    public methods:
        - sound() - returns str
            - should return the sound the animal makes
                e.g. Dog - "woof"
        - tell_age() - returns int
            - returns the current animal age
        - age_up() - returns nothing
            - should add 1 year to the current age
        - all_implemented() - returns bool
            - this method must have a functionality, if all the methods
            above have been implemented, then this should return True,
            otherwise it should return False.
    This is an abstract class! Pay attention, this class MUST NOT have any
    functionality in it (besides all_implemented()).
    The explanations for what the methods should do are mainly for the classes
    that will extend the Animal class.
"""
import abc
from enum import Enum
from typing import Union


class AnimalTypeEnum(Enum):
    DOG = 1
    CAT = 2
    DUCK = 3


class Animal(abc.ABC):
    def __init__(self, color: str, age: int, animal_type: AnimalTypeEnum):
        self.color = color
        self.age = age
        self.animal_type = animal_type

    @abc.abstractmethod
    def sound(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def tell_age(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def age_up(self):
        raise NotImplementedError()

    @classmethod
    def all_implemented(cls):
        if len(cls.__abstractmethods__):
            return True
        else:
            return False


"""
    Create 3 classes:
        - Cat
        - Dog
        - Mouse
    All of these 3 classes must inherit from the Animal class.
    public attributes:
        - inherited from Animal (on init (or also called constructor))
        - enemy (on constructor (init))
            - is reference to the enemy of the current Animal
            e.g. Dog is the enemy of Cat
    private attributes:
        - specific_sound: str
    public methods:
        - inherited from Animal
    private methods:
        - enemy_fear_sound() - returns str
            - this is called inside the sound() method, and if an enemy has
            been passed on the constructor, then the sound should be different
            than the usual sound of the animal
            e.g.
                if Cat is called with enemy = Dog, then the cat should make
            a "meoooooow scared" sound.
                else the cat makes a "meow" sound
"""


class Cat(Animal):
    def __init__(self, color: str, age: int, enemy=None):
        super().__init__(color, age, AnimalTypeEnum.CAT)
        self.enemy = enemy
        self.__specific_sound = "meooooooow"

    def __enemy_fear_sound(self):
        return "meow scared"

    def sound(self):
        if self.enemy is not None:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age = self.age + 1


class Dog(Animal):
    def __init__(self, color: str, age: int, enemy=None):
        super().__init__(color, age, AnimalTypeEnum.DOG)
        self.enemy = enemy
        self.__specific_sound = "woof"

    def __enemy_fear_sound(self):
        return "woof scared"

    def sound(self):
        if self.enemy is not None:
            return self.__enemy_fear_sound()
        else:
            return self.__specific_sound

    def tell_age(self):
        return self.age

    def age_up(self):
        self.age = self.age + 1


if __name__ == "__main__":
    dog1 = Dog('brown', 10, Cat)
    print(dog1.sound())

