import numpy as np
n1 = np.array([4,2,1,3])
nn1 = np.searchsorted(n1, 4)
nn2 =np.searchsorted(n1,4,side="right")
#We can put side="right"
#We can put side="left"
print(nn1)
print(nn2)