#to open a file 

file = open("open.txt", "w")
file.write("Young man, you can be a hero too.\n")
file.close()

#alternative 
with open("open.txt", "a") as file:
    file.write("Learning is really fun!\n")


# to read a file
with open("open.txt", "r") as file:
    content = file.read()
print(content)


#Different methods to read files
 # method 1 as above: print all content

 #method 2 as:read one file 
with open("open.txt", "r") as file:
    line = file.readline()

print(line)

#method 3: read lines as list 
with open("open.txt", "r") as file:
    lines = file.readlines()
    
print(lines)