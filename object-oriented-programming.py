"""
In Python, object-oriented programming is a programming paradigm that relies on the concept of "classes" and "objects".
It is used to structure a software program into simple, reusable pieces of code blueprints, which are used to create
individual "objects" that are specific instances of classes.

You're tasked to create a class Rectangle with the following methods:

__init__(self, length, width): Constructor method to initialize the rectangle with length and width.
area(self): Calculate and return the area of the rectangle.
perimeter(self): Calculate and return the perimeter of the rectangle.

"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2



#Test Case

rectangle = Rectangle(3, 4)
print(rectangle.area()) # Should be 12
print(rectangle.perimeter()) # Should be 14
