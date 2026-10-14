# list comprehension = A concise way to create lists in python compact and easier to read than tradional loops {expression for value in iterable if condition}

#doubles = [expression for x in iterable]
doubles = [ x*2 for x in range(1,11)]
triples = [y *3 for y in range (1,11)]
squares = [z*z for z in range (1,11)]



print(doubles)
print(triples)
print(squares) 