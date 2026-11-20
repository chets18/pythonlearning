import numpy as np

generator = np.random.default_rng()

print(generator.integers(low = 1, high = 101, size =(4,2)))
 
# shuffle an array

array = np.array([1,2,3,4,5])
generator.shuffle(array)
print(array)

fruits = np.array(["apple", "banana", "coconut", "pineapple"])

print(np.random.choice(fruits, size=(3, 4)))