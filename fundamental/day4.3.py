#concession stand program

menu = {"pizza":2.50, "burger":2.50, "fries":2.50, "coke":2.50}

cart = []
total = 0

print("----------- MENU ------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("..................................")

while True:
    food = input("select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) != None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")


print()
print(f"Total is: ${total:.2f}")