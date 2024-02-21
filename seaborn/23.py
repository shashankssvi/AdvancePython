import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
ds.head(10)
print(ds)
sns.kdeplot(x="sepal_length",y="sepal_width",data=data,shade=True,color="yellow",palette="plasma")
plt.show()
