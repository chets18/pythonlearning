import numpy as np

def random_walk_fastest(n=1000):
    steps = np.random.choice([-1, +1], n)
    return  np.cumsum(steps)

walk = random_walk_fastest(1000)
print(walk)