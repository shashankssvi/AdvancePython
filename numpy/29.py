import numpy as np
n1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
nn1= np.array_split(n1, 3, axis=1)
#Split the 2-D array into three 2-D arrays along rows
print(nn1)