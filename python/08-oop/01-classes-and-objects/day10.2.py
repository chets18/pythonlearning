# class variables = shared among all instances(objects) of a class
# defined outside the constructor allow you to share data among all objects created from that class 

class student:

    class_year = 2026
    num_student = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.num_student +=1

student1 = student("Sakalaka", 20)
student2 = student("Chater", 21)

print(student1.name, student1.age)
print(student2.name, student2.age) 
print(student.class_year)
print(student.num_student)