#!/usr/bin/python3
"""Abstract classes"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract class named Animal"""
    
    @abstractmethod
    def sound(self):
        pass
    
class Dog(Animal):
    """Animal Dog"""
    
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    """Animal Cat"""
    
    def sound(self):
        return "Meow"
