import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
ds.head(10)
print(ds)
sns.violinplot(x ="sepal_length", y="sepal_width", data = data,
        hue ='sepal_length', split = True,palette="plasma",saturation=0.5,linewidth=0.1)
plt.show()
