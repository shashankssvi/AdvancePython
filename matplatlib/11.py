import matplotlib.pyplot as plt
import numpy as np
x = np.array([3, 8, 1, 10])
y = np.array([6, 2, 7, 11])
plt.title("data")
plt.xlabel("datax")
plt.ylabel("datay")
plt.plot(x, y)
plt.grid(color = 'yellow', linestyle = '-', linewidth = 1)
#We can also give axis='x'or 'y'
plt.show()

