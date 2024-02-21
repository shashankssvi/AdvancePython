import pandas as pd
ds=pd.read_csv("Film.csv")
ds.drop_duplicates(inplace = True)
print(ds.duplicated())
