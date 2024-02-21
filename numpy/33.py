import numpy as np
n1 = np.array([4,2,1,3])
nn1 = np.searchsorted(n1, 4)
#We can put side="right"
print(nn1)