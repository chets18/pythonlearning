# scalar arithmatic 

import numpy as np

array = np.array([1,2,3])

print(array +1)
print(array -4)
print(array *3)
print(array / 2)
print(array ** 4)

#vectorized math function

arr = np.array([1.98,2.81,3.67])

print(np.sqrt(arr))
print(np.round(arr))
print(np.pi)

radii = np.array([1,2,3])
print(np.pi * radii ** 2)

#element wise arithmetic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6 ])

print(array1 + array2)
print(array1 - array2)
print(array2 / array1)
print(array1 ** array2)


#comparison operators 
scores = np.array([91,28,32, 69, 99, 100])

print(scores == 100) #boolean array
print(scores >= 40)
scores [scores < 40] = 0
print(scores)