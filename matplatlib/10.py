import matplotlib.pyplot as plt
import numpy as np
x = np.array([3, 8, 1, 10])
y = np.array([6, 2, 7, 11])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Data", fontdict = font1,loc = 'left')
plt.xlabel("datax", fontdict = font2)
plt.ylabel("datay", fontdict = font2)
plt.plot(x, y)
plt.show()

