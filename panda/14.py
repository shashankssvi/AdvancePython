import pandas as pd
ds=pd.read_csv("./panda/Film.csv")
ds.dropna(subset=['Year'], inplace = True)
print(ds.to_string())

