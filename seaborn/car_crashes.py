import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=pd.read_csv("./datasets/car_crashes.csv")
dh = data.head(10)
print(dh)
sns.pairplot(data=dh,height=2,hue="speeding",
            palette="plasma",diag_kind='kde',plot_kws={"edgecolor":"yellow"})
plt.show()


