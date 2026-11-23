# Today we'll learn more about available np.method options

import numpy as np

z = np.array([[[1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12]]])

print(f"{z.nbytes/1024} KB")

print(z.itemsize) #Bytes per element

print(z.size) #total element count
# print(np.size(z))

print(z.shape) # z has 1 outer array, containing 4 rows with 3 values each.
# print(np.shape(z))

print(z.ndim)

print(z.dtype)

print(z.strides)

print(z.flags)

# manipulate it
"""
It's simple, .add(), subtract, multiply, divide, etc.
"""