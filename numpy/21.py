import numpy as np
n1 = np.array([1, 2, 3, 4, 5])
for x in n1:
    for y in x:
        for z in y:
            print(z)
