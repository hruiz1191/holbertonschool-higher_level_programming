#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Shape class"""
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    """Circle class That inherits from Shape"""
    
    def __init__(self, radius=0):
        if type(radius) in [int, float]:
            self.radius = abs(radius)
    
    def area(self):
        return (pi * (self.radius ** 2))
    
    def perimeter(self):
        return (2 * pi * self.radius)
    
class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        if type(width) in [int, float]:
            self.width = width

        if type(height) in [int, float]:
            self.height = height
        
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return (2 * self.height) + (2 * self.width)

def shape_info(shape):
    """Prints the information of a shape"""
    
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
