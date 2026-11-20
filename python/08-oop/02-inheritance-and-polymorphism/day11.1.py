#Inheritance = Allows a class to inherit attributes and methods from another class
# helps with code reusability and extensibility class child(parent):

class Animal:
    def __init__(self, name):
        self.name = name #create an attribute called name 
        self.is_alive = True #can create new attribute without stating in (self, name)

    def eat(self):
        print(f"{self.name} is eating") 

    def sleep(self):
        print(f"{self.name} is sleeping") 

class dog(Animal):
    pass

class cat(Animal):
    pass

class mouse(Animal):
    pass

Dog = dog("scooby")
Cat = cat("kimty")
Mouse = mouse("nimchi")

print(Dog.name)
print(Cat.is_alive)