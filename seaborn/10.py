import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
ds.head(10)
print(ds)
sns.countplot(y ='sepal_length', data = data,hue="sepal_width",palette="plasma",width=12)
plt.show()
