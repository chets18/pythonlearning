# for loops = execute a block of code a fixed number of times.
#you can ierate over a range, string, sequence etc. 

for x in range(1,90,2):
    print(x)

credit_card= "1234-5678-9012-0954"

for x in credit_card:
    print(x)

print("Happy NEW year!")

for y in range(1,23):
    if y ==13:
        continue
    else:
        print(y)