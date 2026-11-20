from numpy.lib.format import read_array_header_1_0
import numpy as np

#broadcasting allows Numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.slice

# The dimensions have the same size 0R
# one of the dimensions has a size of 1

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1], [2], [3], [4]])

array10 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
arrays = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(array1.shape)
print(array2.shape)
print(array1 *array2)

print(arrays.shape)
print(array10.shape)
print(array10 * arrays)