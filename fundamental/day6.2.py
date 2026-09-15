# return = statement used to end a function, and send a result to the caller

def add(x,y):
    z = x+y
    return z

def subs(x,y):
    z = x-y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    return x/y


print(add(2,4))

#function to create name

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()

    return first + " " + last

full_name = create_name("learn", "python")
print(full_name)