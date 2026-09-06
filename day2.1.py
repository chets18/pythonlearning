#string method

name = input ("Enter your full name: ")

#result = len(name)
#result= name.find("i")
#result2= name.rfind("i") #r means reverse

#print(result)
#print(result2)


#capitalize name 
name = name.capitalize()
name=name.upper()
name = name.lower()
result = name.isdigit()
result= name.isalpha()
print(name)
print(result)

phone_number=input("Enter your phone number: ")
check= len(phone_number)
countit = phone_number.count("-")
print("you're not allowed" if check == 10 else "try again!")
print(countit)

phone_number = phone_number.replace ("-", "")
print(phone_number)


#to learn more use this
#print(help(str))


#exercise
"""
validate user input 
1. username is no more than 12 characters
2. username must not contain spaces
3. username must not contains digits
"""

username = input("Enter a username: ")
check = len(username)
username= username.replace (" ", "")
check1 = username.isalpha()

if check <= 12 and check1 == True:
    print(f"welcome! {username}")

else:
    print("enter username, no more than 12 characters!")

    

 #exercise: check whether the first 4 character is +977 or not

phone_number = input("Enter your phone number: ")
check = phone_number[:4]
if check == "+977":
    print("valid")
    
else:
    print("Please enter valid phone number.") 