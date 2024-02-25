from matplotlib.colors import Colormap
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
dd=ds.head(10)
print(dd)
sns.scatterplot(x="sepal_length",y="sepal_width",data=ds,
                hue="petal_length",palette="flare",marker="*",alpha=0.5)
plt.show()