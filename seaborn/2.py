import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("tips")
ds=pd.DataFrame(data);
dd=ds.head()
print(dd)
sns.histplot(x="tip",y="smoker",data=data,hue="sex",kde=False,palette="pastel",
                linewidth="0.1",edgecolor="gray",discrete=False)
plt.show()