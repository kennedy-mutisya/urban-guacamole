"""
inheritance 
can extend a class using another class
->a class inherits methods and properties
->DRY<Dont Repeat Yourself>
-----------------------------------------
Biology classification is a good example of inheritance
-------------------------------------------------------
shapes
Rectangle and Square<triangle>
---shapes. <shape_name>
---sides.<rectangle, square, trapezium> side a, side b, side c
---area.<>
---methods. parameters. <side a, side b, side c> of the shape

"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.shape_name = "Rectangle"

    def area(self):
        area = self.length * self.width
        print(f"for rectangle with length: {self.length} and width: {self.width}, the area is: {area}")


class Square:
    def __init__(self, side):
        self.length = side
        self.width = side
        self.shape_name = "Square"

    def area(self):
        area = self.length * self.width
        print(f"for square with length: {self.length} and width: {self.width}, the area is: {area}")


# Usage
r1 = Rectangle(length=20, width=10)
r1.area()
print(f"the shape name is: {r1.shape_name}")

s1 = Square(side=10)
s1.area()
print(f"the shape name is: {s1.shape_name}")
