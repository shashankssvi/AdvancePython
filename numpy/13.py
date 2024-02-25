import numpy as np
n1 = np.array([1, 2, 3, 4, 5])
x = n1.copy()
y = n1.view()
#Used to see whether x is a copy or a original
print(x.base) #we get none here
print(y.base) 



