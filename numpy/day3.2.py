# SO, while reading the book from python to numpy. i realised that first of all,
# I should understand most common features and some theory. 
# What i mean why that is, how many initial bytes, bits are there in each datatype. 

import numpy as np
z = np.arange(9).reshape(3,3).astype(np.int16)
print(z)
print(z.itemsize)
print(z.shape)
print(len(z.shape))
print(z.ndim)

#The book said "strides of an array". so, what are the other properties of array
"""
what properties does an array have?
1) It can store numbers, char, int, float. almost anything
2) It can be updated in further program 
3) we can change size of an array. 
4) We can define or assign how much storage of data it can take like int16, float32
5) We can find the position of an item inside an array

"""

#strides
#stride = z.shape[1]*z.itemsize, z.itemsize

print(z.strides)

#question to ask, what does that shape[1] does, is it an axis or what. is it shape of z 
# but only take position 1 which might be 0 1 2 which shape is 3 that gives (3*2,2)

#i think like i should learn to get storage of specific item. such as i create a list, what's the size of that list in kb or like measure
print(f"{z.itemsize}GB") 
#what's the differece in itemsize and size

#How to compute the start and end offsets
index = 1, 1
# opion 1
print(z[index].tobytes())
#option 2
offset_start = 0
for i in range(z.ndim):
    offset_start += z.strides[i] * index[i]
offset_end = offset_start + z.itemsize

print(z.tobytes()[offset_start:offset_end])

