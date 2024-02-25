import pandas as pd

ds=pd.read_csv("./panda/Film.csv")
for x in ds.index:
    if ds.loc[x,'Year'] != 2010.0:
        ds.drop(x,inplace = True)
print(ds)
