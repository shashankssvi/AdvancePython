import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=np.random.randint(low=1,high=100,size=(10,10))
dd=pd.DataFrame(data)
print(dd)
sns.heatmap(data=data,cmap="YlOrBr",annot=True,xticklabels=True,yticklabels=True)
plt.show()