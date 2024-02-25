import numpy as np
n1 = np.array([[[1, 2],[3, 4]],[[5,6],[7,8]]])
for items1 in n1:
    for items2 in items1:
        for items3 in items2:
            print(items3)
