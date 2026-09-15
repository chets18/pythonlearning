# *args = allows us to pass multiple non-key arguments
# kwargs = allows us to pass multiple keyword-arguments
#         * unpacking operator
#            1. Posiional, 2. Default, 3. Keyword, 4. Arbitrary

# def add(a, b):
def add(*args):
    total = 0
    for arg in args:
        total +=arg
    return(total)



# print(add(1,6))
print(add(1,2, 4,8,10,50,89.9))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

    
display_name("chet", "raj", "Jaishi", "bro")

#using kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}", end = " ")

print("\n")

print_address(street="fahh st.", 
              city="kathmandu", 
              state="bagmati", 
              zip=44650)