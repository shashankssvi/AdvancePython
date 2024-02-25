import numpy as np
n1 = np.array([[1, 2],[3, 4]])
n2 = np.array([[5,6],[7,8]])
nn1 = np.concatenate((n1,n2),axis=1)
nn2 = np.concatenate((n1,n2),axis=0)
print(nn1)
print(nn2)