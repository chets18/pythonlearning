""" fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "pottoes"]
meat=        ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meat]

print(groceries[2][1]) # 1 is for meat, 2 is for fish


"""
#or 
groceries = [ ["apple", "orange", "banana", "coconut"],
              ["celery", "carrots", "pottoes"],
              ["chicken", "fish", "turkey"]]


for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print() 
    


num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           (0,"#","*"))

for row in num_pad:
    for num in row:
        print(num, end= " ")

    print()