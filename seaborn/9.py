import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("tips")
ds=pd.DataFrame(data);
ds.head(10)
print(ds)
sns.barplot(y ="tip", x="sex", data = data, palette ='plasma',hue='smoker',ci=True,saturation=0.2,facecolor=[1,0,1,0],edgecolor='0.01')
plt.show()
