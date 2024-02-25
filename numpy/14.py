import numpy as np
n1 = np.array([1, 2, 3, 4, 5])
n2= n1.copy()
n1[0]=6
print(n1)
print(n2) # this won't change

