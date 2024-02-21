import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = sns.load_dataset("iris")
ds=pd.DataFrame(data);
ds.head(10)
print(ds)
s=sns.PairGrid(data)
s.map_offdiag(sns.barplot)
plt.show()
