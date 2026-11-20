# this code is just for practice 

#feature 1: 1) give storage information to user, like how many storage left (in total), how many used.

"""
How would i do this: 
i'll first ask user what they want to do; see (storage, find, file size, screentime) or edit (file arrangement, deleteting specific files)

"""
from functions import *

# ask user to choose 1
print("Type what you want to do: ")
print("----------------------------")
print("See (storage, find, file size, screentime)")
print("Edit (file arrangement, deleting specific files)\n")
see = input("Type here: ")

options = {1: "Storage", 2: "Folder size", 3: "Task Manager", 4: "Time & Date", 5: "Screentime", 6: "File Finder", 7: "File Location", 8: "File Arrangement AUTO", 9:"File Arrangement (type)", 10: "Delete specific file(s)" }

if see.lower() == "see":
    print("I got you!!\n")
    print("Choose a number between 1 to 10 based on your preferences.")
    print("----------------------------------------------------------")
    for keys, value in options.items():
        print(f"{keys}. {value}")

    see_input = input("\nNumber goes here: ")
    while not see_input.isdigit() or not 1 <= int(see_input) <= 10:
        see_input = input("Invalid choice. Enter a number between 1 and 10: ")
        
    see_input = int(see_input)

    if see_input == 1:
        Storage.run()
    
    elif see_input == 2:
        pass

    elif see_input == 3:
        pass

    elif see_input == 4:
        pass

    elif see_input == 5:
        pass

    elif see_input == 6:
        pass

    elif see_input == 7:
        pass

    elif see_input == 8:
        pass

    elif see_input == 9:
        pass

    elif see_input == 10:
        pass

