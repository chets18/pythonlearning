# super() function = Function used in a child class to call methofs from a parent class (superclass).
# Allows you to extend the functionality of the inherited methods

from sys import is_finalizing
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'Filled' if self.filled else 'Not Filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
 

circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=False, width=51)
triangle = Triangle(color="brown", filled=True, width=12, height=15)

print(circle.color)
print(circle.filled)
 
circle.describe()