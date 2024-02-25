import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("./datasets/penguins.csv")
dh = data.head(10)
print(dh)
sns.pairplot(data=data,height=2,hue="species",
            palette="plasma",diag_kind='auto',plot_kws={"edgecolor":"yellow"})
plt.show()


