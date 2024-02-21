import numpy as np
n1 = np.array([1, 2, 3, 4, 5])
x = n1.copy()
y = n1.view()
n1[0]=6
print(x)
print(y)

