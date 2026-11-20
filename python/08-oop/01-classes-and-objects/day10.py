#self are to give each objects thier own identify, think like, you've BMW, mustang, BYD etc. and you have to assign each cars thier own fields.
class car:
    def __init__(self, model, year, color, for_sale):
        self.model = model #assign to the object
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):   #these additional functions are called methods.
        print(f"The CAR {self.model} is driving")

    def stop(self):
        print(f"The CAR {self.model} is stopped")


#Note that the _init__() method is only called when a new object is created, not when you call the drive() or stop() methods