import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
ds.head(10)
print(ds)
sns.stripplot(x ='sepal_length', y ='sepal_width',data = data,jitter = 0.2, 
            hue ='sepal_length', dodge = True,palette="plasma",marker="o",size=2,
            linewidth=1,edgecolor="violet")
plt.show()
