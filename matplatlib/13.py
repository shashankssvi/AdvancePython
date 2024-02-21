import matplotlib.pyplot as plt
import numpy as np

x = np.array([3, 8, 1, 10])
y = np.array([6, 2, 7, 11])
plt.subplot(1,2, 2)
plt.plot(x, y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("gr1")
plt.suptitle("total")
plt.show()
