# Multiple inheritance = inherit from more than one parent class C(A,B)

# multilevel inheritance = inherit from a parent which inherits from another parent 
#   C(B) <- B(A) <- A


class Animal:
    def eat(self):
        print("This animal can eat like human do.")

    def sleep(self):
        print("This animal sleeps 12 hours a day")

class Pray(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):   #self as their first parameter
        print("This animal is hunting")

class Rabbit(Pray):
    pass

class Hawk(Predator):
    pass

class Fish(Pray, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
# rabbit.hunt () will show an error cuz' rabbit belongs to Pray class

fish.hunt()
fish.flee()

rabbit.eat()
rabbit.sleep()
hawk.eat()
hawk.sleep()
fish.eat()
fish.sleep()