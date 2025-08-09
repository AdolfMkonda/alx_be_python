# Solidify your understanding of 
# class methods and static methods in Python 
# by implementing examples of each in a class, 
# demonstrating their usage and differences.


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        return a * b