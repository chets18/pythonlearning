# code vectorisation
import numpy as np
import random
# pure python
def add_python(z1,z2):
    return [z1+z2 for (z1,z2) in zip(z1,z2  )]


#vectorize
 

z1 = random.sample(range(1000), 100)
z2 = random.sample(range(1000), 100)
def adding(z1,z2):
    return np.add(z1,z2)

print(adding(z1,z2))

#write a Python function that adds two nested lists element by element, 
# regardless of how deeply nested they are.
#goal: add them

z3 = [5, [6, [7, 8]]]
z4 = [1, [2, [3, 4]]]
 # Note: there's no numpy array which can support this kind of operation. 
 # So we will convert them to pure python and then add them.
print(type(z3))