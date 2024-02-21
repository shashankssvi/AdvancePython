import numpy as np
n1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
nn1= np.vsplit(n1, 3) #which is alternative of hstack
#Split the 2-D array into three 2-D arrays along rows
print(nn1)