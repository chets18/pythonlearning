#Polymorphism = Greek Word that means to "have many forms or faces"
# poly = main, morph= form

#  Two ways to achieve polymorphism
# 1. Inheritance = an object could be treated of the same type as a parent class
# 2. "Duck Typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side **2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

shapes = [Circle(5), Square(9), Triangle(3,8)]
for shape in shapes:
    print(f"{shape.area()} cm^2")