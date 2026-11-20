# so, today i don't have internet in my room. so, we're building/creating a program which just store the information of my projefcts.repr

#we'll use time built-in library as well,.


"""
n= int(input("How many projects you want to introduce: "))
projects = []

for item in range(n):
    item = input("Enter the project name: ")
    projects.append(item)

print("------------ saving------------")
print(projects)

to_check=input("Enter the project you want to check: ")

if to_check in projects:
    print(f"we've got {to_check}")

else:
   
   adding =input("If this is the new project type 'new' else type q: ")
   if adding.lower == "q":
    print("we're out")
   else:
    projects.append(adding)
    print(projects)

"""
   
   #it worked after may corrections and mistakes. so this is how learning happens. not through using claude, chatgpt for debugging.projects.projects

   #however, i wanted the program to continue until user type q. so, let's build that.set
   # so, the program will continue in a loop untill user type q at last. 


n= int(input("How many projects you want to introduce: "))
projects = []


for item in range(n):
    item = input("Enter the project name: ")
    projects.append(item)

print("------------ saving------------")
print(projects)

to_check=input("Enter the project you want to check: ")

if to_check in projects:
    print(f"we've got {to_check}")

else: 
   adding = input("If this is the new project type 'new' else type q: ")
   if adding.lower() == "q":
     print("we're out")
   elif adding.lower() == "new":
     new = input("Enter the new project name: ")
     projects.append(new)
     print(projects)