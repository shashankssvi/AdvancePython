import pandas as pd
ds=pd.read_csv("./panda/Film.csv")
print(ds.duplicated())
ds.drop_duplicates(inplace = True)
print(ds.duplicated().any())
print(ds.to_string())
