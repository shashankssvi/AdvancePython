import pandas as pd

ds=pd.read_csv("./panda/iris1.csv")
print(ds.corr())
