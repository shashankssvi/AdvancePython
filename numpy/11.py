import numpy as np
n1 = np.array([1, 2, 3, 4, 5])
x = n1.view()
#This can change if n1 changes
print(x) #x is not a new object
print(n1)

