import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
ds.head(10)
print(ds)
sns.boxplot(x ="sepal_length", y="sepal_width", data = data, 
            hue ="sepal_length",palette="plasma",linewidth=1,orient="x")

plt.show()
