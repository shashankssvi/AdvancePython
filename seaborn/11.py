import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
ds.head(10)
print(ds)
sns.countplot(x='species', data = data,hue="petal_width",linewidth=1)
# we can alsogive saturation,color,face color,edgewidth also
plt.show()