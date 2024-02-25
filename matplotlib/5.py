import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'red', mfc = 'blue')
#ms=marker size(ms)
#marker edge color(mec)
#marker face color(mfc)
plt.show()
