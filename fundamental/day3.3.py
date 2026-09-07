#collection = single "variable" used to store multiple values

#list = [] ordered and changeable, DUplicates OK
#set = {} unordered and immutable, but Add/Remove OK, NO duplicates
# Tuple = () ordered and unchangeable. DUplicates OK. Faster


#list

fruits = ["apple", "orange", "cocunut", "banana"]
fruits.append("papaya")
fruits[0] = "Mango"
fruits.remove("orange")
fruits.insert(0,"pineapple")
fruits.sort()
fruits.reverse()
# all gone,   fruits.clear()
print(fruits.index("pineapple"))
print(fruits.count("pineapple"))

print(fruits)

# print(dir(fruits)) output: methods you can use with the list.
# print(help(fruits))  you know what help mean don't you?

print(len(fruits))
print("pineapple" in fruits)


for fruit in fruits:
    print(fruit)


#set

cars = {"BMW","Porche","Toyota","Audi","BMW"} #no data repeat
print(cars)

#output: not in order, it's random everytime.fruits

# print(cars[0]) # error: 'set' object is not subscriptable
cars.add("mercedes")
cars.remove("BMW")
fruits.pop()
print(cars)

# Tuple

AI=("ChatGPT", "Gemini", "Claude", "Copilot")
print(AI.count("ChatGPT"))
print(AI.index("Gemini"))
print(len(AI))
