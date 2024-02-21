import pandas as pd

ds=pd.read_csv("Film.csv")
print(ds.corr())
