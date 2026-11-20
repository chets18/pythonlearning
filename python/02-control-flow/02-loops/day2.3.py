# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")
"""
if name == "":
    print("you didn't enter your name.") 

else:
    print(f"Hello, {name}")
"""
    #while
    
while name == "":
    print("you didn't remember your name?")
    name = input("Enter your name: ")

print (f"Hello! {name}")



#real world practice:
food = input("Enter a food you like (q to quit): ")
while food.lower() !="q":
    print(f"you like {food}")
    food = input("Enter another food you like (q to quit): ")

print("thanks, see yah!")