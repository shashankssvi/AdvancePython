import pandas as pd

ds=pd.read_csv("Film.csv")
for x in ds.index:
    if ds.loc[7,'Year'] == 2000:
        ds.drop(2,inplace=True)

