import numpy as np
n1 = np.array([1.1, 2.1, 3.1])
nn1 = n1.astype('i')
n2 = np.array([1,2,3])
nn2 = n2.astype('f')
#We can also write 'nn1 = n1.astype(int)'
print(n1)
print(n1.dtype)
print(nn1)
print(nn1.dtype)
print(nn2)
print(nn2.dtype)
