# default aruguments = A default value for certain parameters default is used when that argument is omitted make your functions more flexible, reduces # of arguments
#               1. positional, 2. default, 3. keyword, 4. arbitrary.


def net_price(list_price, discount=0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500, 0, 0.05))
print(net_price(500, 0.1, 0.1))


import time
def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(0.1)
    print("done")

count(1, 10)

# KEYWOED arguments = an argument preceded by an identifier helps with readability.

def hello(gretting, title, first, last):
    print(f"{gretting} {title} {first} {last}")

# hello("hello", "Mr.", "bro", "lro")
hello(title="Mr.", gretting="hello", last="bro", first="lro")

#positional argument follows keyword argument


print("1", "2", "3", sep="---", end="\n")

#program

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
 
print(get_phone(country ="1", area = "123", first = "456", last = "7890"))