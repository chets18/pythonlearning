import random

# print(help(random))
low=1
high = 1000

# x = random.randint(low,high)
# print(x) 

options = ("rock", "paper", "scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

option = random.choice(options)
card = random.shuffle(cards)

print(option)
print(card)

