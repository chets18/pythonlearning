# Iterables = AN object/collecction that can return its elements one at a time,
# allowing it to be iterated over in a loop

#tuples are also iterables, dict too. 

from os import ST_NOSUID
numbers = [1,2,3,4,5,6,7,8,9,10]
fruits = {"apple","banana","cherry","orange","mango"}

for number in reversed(numbers): #number is a variable, you can use anything
    print(number, end=" \n")

for item in fruits:
    print(item, end=" \n")


#Membership operators = Used to test whether a value or variable is found in a sequence (string, list, tuple, set or dictionary)
# 1. in, 2. Not in

word = "APPLE"
letter = input("guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} not found")
else:
    print(f"There is a {letter}")


#set of students
students = { "chetraj", "sanjog", "bibek", "roshan", "sandeep"}

name = input("enter your name: ")

if name.lower() in students:
    print(f"{name} has given exam.")
else:
    print(f"{name} has not given exam.")


#there are just a practices. 

email = "brocode@gmail.com"
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")

