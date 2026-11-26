# views and copy
# direct and indirect access

# first understand some attibutes
#base
#understand wherther the variable is original or copied 

import numpy as np

z = np.array([[[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [10, 11, 12]]])

print(z.base)          # z owns its own memory

v = z[0, 1:3, :]   
print(v)    # slicing returns a view
print(v.base is z)     # v points back to z's memory buffer


