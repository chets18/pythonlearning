# format specifers = {:flags} format a value based on what flags are inserted

"""
.(number)f = round to that many decimal places 
:(number) = allocate that many spaces
:03 = allocate and zero pad that many spaces
:< = left justify
:> = right justify
:^ center align
:+ = use a plus sign to indicate positive value
:= = place sign to leftmost position
: = insert a space before positive numbers
:, = comma separator
"""

price1 = 3.14
price2 = -987.9875
price3 = 12.98

print(f"price 1 is {price1:.2f}")
print(f"price 2 is {price2:.3f}")
print(f"price 3 is {price3:10}")