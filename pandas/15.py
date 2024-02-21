import pandas as pd
ds=pd.read_csv("Film.csv")
ds.loc[7,'Year'] =2000
print(ds.to_string())

