import numpy as np 

array = np.array([['A', 'B', 'C'], 
                  ['D', 'E', 'F'], 
                  ['G', 'H', 'D'], 
                  ['I', 'J', 'K']])

word = array[2,-3] + array[0,1]
print(word)

print(array.ndim) #Number of dimension

#shortcut to find the number of dimension is look how many braces at last, 

print(array.shape)

print(array[0][-1][0][0])
print(array[3,-2])