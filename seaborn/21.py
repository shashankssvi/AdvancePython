import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
dd=ds.tail(10)
print(dd)
sns.catplot(x="sepal_length",y="sepal_width",data=dd,kind="point",hue="species",palette="plasma",col="petal_width",height=3,col_wrap=3)
plt.show()
