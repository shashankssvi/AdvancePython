import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("./datasets/brain_networks.csv")
dh = data.head(10)
print(dh)
sns.pairplot(data=data,height=2,hue="17.5",
            palette="plasma",diag_kind='hist',plot_kws={"edgecolor":"yellow"})
plt.show()


