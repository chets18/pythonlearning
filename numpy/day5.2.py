# uniform vectorization
# Game of life :- the simplest form of vectorization where all the elements 
# share the same computation at every time step with no specific processing 
# for any element.

# What is Game of life

"""
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of 
      square cells, each of which is in one of two possible states, live or dead. 
      Every cell interacts with its eight neighbours, which are the cells that are 
      directly horizontally, vertically, or diagonally adjacent. At each step in time, 
      the following transitions occur:
1) Any live cell with fewer than two live neighbours dies, as if by needs caused by underpopulation.
2) Any live cell with more than three live neighbours dies, as if by overcrowding.
3) Any live cell with two or three live neighbours lives, unchanged, to the next generation.
4) Any dead cell with exactly three live neighbours becomes a live cell.

"""

import numpy as np

Z = [[0,0,0,0,0,0],
     [0,0,0,1,0,0],
     [0,1,0,1,0,0],
     [0,0,1,1,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]]

def compute_neighbours(Z):
    shape = len(Z), len(Z[0])
    N = [[0,]*(shape[0]) for i in range(shape[1])]
    for x in range(1,shape[0]-1):
        for y in  range(1,shape[1]-1):
            N[x][y] = Z[x-1][y-1] + Z[x] [y-1] + Z[x+1][y-1] \
                + Z[x-1][y]                    + Z[x+1][y]    \
                    + Z[x-1][y+1] + Z[x][y+1] + Z[x+1][y+1]
    return N

print(compute_neighbours(Z))

def iterate(Z):
     shape = len(Z), len(Z[0])
     N = compute_neighbours(Z)
     for x in range(1, shape[0] -1):
        for y in range(1,shape[1] -1):
            if Z [x][y] ==1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] ==0 and N[x][y] ==3:
                Z[x][y] =1
     return Z
print(iterate(Z))

"""
Let me explain what does this program does.
1. Z is a cell (your skin cell)
2. we first know how many cells are in row and in column so it'll be easy for us to find its neighbour
3. N creates 6 0 in row and 6 columns of 0. 
6. and then what we do is, we pick every cell (one after another) and we sum all 8 neighbour cell of every cell.
7. and we perform a program where, we decide whether the cell should alive or be dead with a rule. if less than 2 or more than 3 dead (which is 0)
if not alive.

"""