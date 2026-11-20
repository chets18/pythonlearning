#in this method we'll learn same as if else but alternative:
import os

print(os.getcwd()) #This commands means Current Working Directory.

try:
    with open("opens.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File doesn't exist.")


# this code will create a file if not exits or delete all existing content if exits and add the content provided below.
with open("/home/chetraj/projects/learnpython/open.txt", "w") as file:
    file.write("Saved on Desktop.")