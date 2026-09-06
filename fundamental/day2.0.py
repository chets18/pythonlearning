
num = 10

print("positive" if num >0 else "negative")

a=1000
b=2000
age = 15
temp = int(input("enter the temperature: "))

max_num = a if a>b else b
min_num = a if a<b else b
print (max_num)
print (min_num)

status = "adult" if age>=18 else "kid"
weather = "hot" if temp>20 else "cold"
print (status)
print(weather)

# conditional expression.
#real world use case.

user_role = "guest"
acess_level = "Full Acess" if user_role == "admin" else "Limited access"
print(acess_level)