import matplotlib.pyplot as plt
import numpy as np
x = np.array([3, 8, 1, 10])
y = np.array([6, 2, 7, 11])
colors = np.array([0, 10, 50, 100])
#colors = np.array(["red","green","blue","yellow"])
plt.scatter(x, y, c=colors, cmap='viridis')
#cmap=
plt.colorbar()
plt.show()
