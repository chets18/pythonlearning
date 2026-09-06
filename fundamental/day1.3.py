# if-else are keywords; a special, reserved word that has a predefined meaning and purpose built directly into the language's syntax.keywords are strictly case-sensitive.(lowercase)
age= int(input("How old are you? "))
if age>=18:
    print("you're adult!")

elif age ==0 or age<0:
    print("better luck next time.")

else:
    print("you're a kid!")

#logical operators are keywords : and, or, not
temp = int(input("what is the temperate outside?: "))

if temp>=0 and temp <=40:
    print("the temperature is good today!")
    print("dil garden garden horiya hai")

else:
    print("you're boiling")