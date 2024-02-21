import numpy as np
n1 = np.array([1, 2, 3])
n2 = np.array([4, 5, 6])
nn1 = np.concatenate((n1,n2),axis=1)
#axis=0 also
print(nn1)