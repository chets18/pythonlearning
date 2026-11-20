#today we will learn about python basics. so basics 

"""
type() is a built-in function 
other built-int functions are: 
print()
input()
int()
float()
str()
bool()

the keyword f" {name}" is called formatted string literal (f-string).


Python
│
├── Keywords
│   ├── if
│   ├── else
│   ├── for
│   ├── while
│   └── def
│
├── Functions
│   ├── print()
│   ├── input()
│   ├── type()
│   └── len()
│
├── Classes / Types
│   ├── int
│   ├── str
│   ├── float
│   └── bool
│
├── Modules
│   ├── math
│   ├── random
│   └── os
│
└── Special syntax
    └── f"Hello {name}"
"""

#to start with the variable 
name = "chetraj" #string
age = 17 #int
salary = 0.0 #float
is_student = True  #boolen

if is_student:
    print ("welcome, you're eligible.")

else:
    print (f"sorry, {name}  you're NOT a student.")

#to view the type
print (type(name))
print (type(age))
print (type(salary))
print (type(is_student))

#experiment with a program
name = input ("What is your name? ")
age = int (input ("What is your age? "))
salary = float (input ("What is your salary? "))
is_student = (input ("Are you a student? True/False: "))

verify1 = type(name)
verify2 = type(age)
verify3 = type(salary)
verify4 =type(is_student)

if age<=18 and salary <=15000 and is_student == True:
    print("allowed to go out.")

else: 
    print("you are not allowed to go out.")

if verify1 == str and verify2 == int and verify3 == float and verify4 == bool:
    print("done")
    
else: 
    print ("you are cooked.")
