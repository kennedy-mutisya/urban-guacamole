""" 
oop.
<js, python, java, c++>

concept in programing  to make
work easy. by using principles of oop we can make our code more readable, reusable and maintainable.

1.Encapsulation
-keeping data and methods <functions>inside a class.
while restricting direct access to internal data.
2.Abstraction
-hiding unnecessary complexity or implrtration of details.
3.Inheritance
-one class to reuse or extend properties 
and methods of another class.
4.Polymorphism.
-appearing in different forms. Method can 
have different behaviors.
-------------------------
JS and Python are object oriented.
->number.toString() ,string.toLowerCase(),string.toUpperCase() are examples of polymorphism in JS.
"""
""" 
->class->
-blueprint of object.<>
->class could be an architectural drawing of a house.
 object->implementation of class.<>object is an instance of class.
 ie implementation of a drawing of a house.
"""

#is to have the name Capitalized and singular.
#fields are the properties of the class.

class House:
    bedrooms=3
    bathrooms=2
    floors=1
    area=120
    owner=""
    location=""
    architect= "KIMANI"

    #js  construtor
    def __init__(self, owner, location):
        print("Class house created. initializer called")
        self.owner=owner
        self.location=location
    def config(self, owner, location):
        self.owner=owner
        self.location=location
    def print_self(self):
        #this<the object itself> self<object>
        print(self)
        print(self.__dict__)#dictionary of the object properties.<print all the properties>

#when acess object properties use dot notation.
#Bracker notation is for dictionary.
marcrine_house=House(owner="marcrine", location="kikuyu")
#marcrine_house.config(owner="marcrine", location="kikuyu")
print(f"Macrines House Owner{marcrine_house.owner}")
print(f"Macrines House Location{marcrine_house.location}")
print(f"Macrines House Bedrooms{marcrine_house.bedrooms}")
print(f"Macrines House Bathrooms{marcrine_house.bathrooms}")
print(f"Macrines House Floors{marcrine_house.floors}")
print(f"Macrines House Area{marcrine_house.area}")
print(f"Macrines House Architect{marcrine_house.architect}")
marcrine_house.print_self()
print("---------------------------------------------------")
daniel_house=House(owner="daniel", location="Murang'a")
#daniel_house.owner="daniel"
#daniel_house.location="Murang'a"
daniel_house.config(owner="daniel", location="Murang'a")#__init__ method is called when the object is created.
print(f"Daniels House Owner{daniel_house.owner}")
print(f"Daniels House Location{daniel_house.location}")
print(f"Daniels House Bedrooms{daniel_house.bedrooms}")
print(f"Daniels House Bathrooms{daniel_house.bathrooms}")
print(f"Daniels House Floors{daniel_house.floors}")
print(f"Daniels House Area{daniel_house.area}")
print(f"Daniels House Architect{daniel_house.architect}")
daniel_house.print_self()
print("---------------------------------------------------")