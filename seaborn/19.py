import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
ds.head(10)
print(ds)
sns.pairplot(data=data,height=2,hue="species",
            palette="plasma",diag_kind='kde',plot_kws={"edgecolor":"yellow"})
plt.show()
