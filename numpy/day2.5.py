# Filtering = Reders to the process of selecting elements from an array that match a given condition

import numpy as np 
  
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages <19] 
adults = ages[(ages < 18) | (ages >=65)]
print(teenagers)
print(adults)
evens = ages[ages % 2 == 0]
odds = ages[ages %2 !=0]
print(evens)
print(odds)

adult = np.where(ages >=18, ages, 0)
print(adult)