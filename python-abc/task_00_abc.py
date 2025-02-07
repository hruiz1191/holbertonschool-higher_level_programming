from abc import ABC, abstractmethod


class Animal(ABC):
    def sound(self):
        pass


class Dog(Animal):
    def sound(self)
        print("bark bark")


class Cat(Animal):
    def sound(self)
        print("meow")
