#python is a interpreter language, which traslates and executes code line by line. 

# learning math module/librabry 
"""
Difference between module and library
module: A single file containing python code (functions, classes, or variables).For example, math.py, random.py

Library: An umbrella term for a collection of related packages and modules. While "package" and "library" are often used interchangeably in casual conversation, a library represents the overall functional concept (like data visualization or machine learning). For example, matplotlib, numpy.

Picture this: a library matplotlib and modules are pyplot (pyplot.py) that we import to plot graphs.

Package: A directory (folder) that bundles multiple modules together, organized hierarchically using fot notation. A package traditionally includes an _init_.py file.
"""

# let's learn how the code, folder structure looks like. 
"""
imagine you're writing a book, 
[Keywords / Logic] ➔ [Functions / Classes] ➔ [Module] ➔ [Package] ➔ [Library]
(Words)               (Sentences)            (Chapter)  (Book)     (Encyclopedia)

We Save functions (def area():) into a single file ending in .py. which is a module. smallest unit of code sharing.
when our code gets too big for one file, we put multiple .py files (module) into a folder. and that folder is what we call package.
and Library is a collection of these folders (packages) and files (modules) designed to solve a massive real-world problem (like building websites or analyzing data).


"""

import math
pi = 3.14

x=3
y=2
z=1
print (round(pi))
print (math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2)) 

print(math.sqrt(400))

print(max(x,y,z))
print(min(x,z,y))