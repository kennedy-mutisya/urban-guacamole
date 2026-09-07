""" 
shape class.
properties and methods common to all shapes

"""
class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def describe(self):
        print(f"This is a {self.shape_name}.")

    def display_info(self):
        print("------------------------")
        print(f"Shape: {self.shape_name}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print("------------------------")

#inheritance class name (clsass inheriting from)

class Rectangle(Shape):
    def __init__(self, length, width):
        #name of the shape is rectangle
        #super().__init__("Rectangle")  # Call the parent class constructor
        #self <specific object created the class>
        super().__init__(shape_name="Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

#code for the squre class
class Square(Rectangle):
    def __init__(self, side):
        #super -->its not shape its rectangle
        super().__init__(length=side, width=side)
        self.shape_name="Square"

s1=Square(side=35)
print("shape name", s1.shape_name)
print("area is ", s1.area())
s1.describe()
s1.display_info()

# r1 = Rectangle(length=20, width=10)#shape_name="Rectangle"

# print("shape name", r1.shape_name)
# print("area is", r1.area())#rectangle area<>
# r1.describe()#shape
# r1.display_info()#shape