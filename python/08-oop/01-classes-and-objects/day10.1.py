#object = A bundle of related attributes (variables) and methods (functions)
# E.g. phone, cup, book
# you need a 'class' to create many objects 

# class = (blueprint) used to design the structure and layout of an object



"""
you may not fully understand this code, so, let's breakdown every single code 


"""
from day10 import *

car1 = car("BYD", 2026, "navy blue", True)
car2 = car("TOYOTA ", 2002, "WHITE", False)
print(car1) # output = memory adress of our object

print(car2.for_sale)

car1.drive()
car2.stop()
