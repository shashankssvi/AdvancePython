import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=np.random.randint(low=1,high=100,size=(10,10))
dd=pd.DataFrame(data)
print(dd)
sns.histplot(y=dd[1],data=dd,palette="pastel",kde=True,edgecolor="gray",linestyle="-",discrete=False)
plt.show()