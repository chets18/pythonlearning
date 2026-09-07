# nested loop = A loop within another loop (outer, inner)
#  outer loop:
# inner loop:

"""
 for x in range(3):
    for y in range(1,12):
     print(y, end="")
    print()
 """

# rentangular shape using text

rows =int(input("Enter the number of rows: "))
columns =int(input("Enter the number of column: "))
symbol = input("enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()
