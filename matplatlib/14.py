import matplotlib.pyplot as plt
import numpy as np
x = np.array([3, 8, 1, 10])
y = np.array([6, 2, 7, 11])
sizes = np.array([20,50,100,200])
plt.scatter(x, y, color = 'black', s=sizes, alpha=0.5)
plt.show()
