import numpy as np
n1 = np.array([1, 2, 3])
n2 = np.array([4, 5, 6])
nn1 = np.dstack((n1,n2)) # along the z-axis
#depth stack
print(nn1)
