# btw,i'm following a tutorial by a youtube channel "bro code" shout out to him for a long 12 hours long detailed video.

#dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = { "USA": "Washington D.C.",
             "India": "New Delhi",
             "China": "Beijing",
             "Nepal":"Kathmandu" }


print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("The capital exists")
else:
    print("That capital doesn't ex ist")

capitals.update({"Japan": "Tokyo"})
print(capitals)

# capitals["Russia"] = "Moscow"
# print(capitals.pop("Russia")) 

# you know what keys and value, don't you?
keys = capitals.keys()
values = capitals.values()

print(keys)
print(values)

#for value in capitals.values():

items = capitals.items()
for key, value in capitals.items():
    print(f"The capital of {key} is {value}")