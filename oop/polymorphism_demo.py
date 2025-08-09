# Enhance your understanding of polymorphism 
# in Python by creating a set of classes 
# that demonstrate method overriding and polymorphic behavior.

import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()
        return math.pi * self.radius ** 2
        
