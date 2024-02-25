import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
dd=ds.head(10)
print(dd)
sns.scatterplot(x="sepal_length",y="sepal_width",data=ds,hue="petal_length",palette="flare")
#more palette:- https://seaborn.pydata.org/tutorial/color_palettes.html
plt.show()