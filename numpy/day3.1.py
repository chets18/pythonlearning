# learning further numpy (vectorisation) from a book From Python to NumPy by Nicolas P. Rougier

#object oriented approach
import random
class RandomWalker:
    def __init__(self):
        self.position = 0

    def walk (self, n):
        self.position =0
        for i in range(n):
            yield self.position #it returns a value froma function one at a time
            self.position += 2* random.randint(0,1) -1 

Walker = RandomWalker()
Walk = [position for position in Walker.walk(1000)]
print(f"Position iz: {Walk}\n")

#procedural method


def random_walk(t):
    position = 0
    walk = [position]
    for i in range(t):
        position += 2* random.randint(0,1) - 1
        walk.append(position)
    return walk

    

walking = random_walk(1000)
print(f"{walking}\n")


#vectorized approach

def random_walk_faster(n=800):
    from itertools import accumulate
    steps = random.choices([-1, +1], k=n)
    return[0] +list (accumulate(steps))

walk = random_walk_faster(800)
print(walk)

#numpy way
import numpy as np

def random_walk_fastest(n=1000):
    steps = np.random.choice([-1, +1], n)
    return  np.cumsum(steps)

walk = random_walk_fastest(1000)
print(walk)