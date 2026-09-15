#function = A block of reusable code 
#place () after the function name to invoke it

def happy_birdthday(name, age):
    print("happy birthday to you)")
    print(f"you are {age} years old")
    print("Happy birthday to you")
    print()

happy_birdthday("BRO",20)
happy_birdthday("STEVE",30)
happy_birdthday("HOE",25)


# display invoice

def display_involved(username, amount, due_data):
    print(f"Hellow {username}")
    print(f"your bill of ${amount}")
    print(f"will be due on {due_data}")

display_involved("jeoschmo", 100.01, "01/02")

# function: to reduce code redundancy and to make code more optimized by using it in multiple areas.repr
# def means define a function. aboce display_involved is a functio name, just like variable name. and
# (username, amount, due_data): is the parameters which store inputs. 
# the last code, display_involved("value", int, "str") means we're calling the function and giving it values.
