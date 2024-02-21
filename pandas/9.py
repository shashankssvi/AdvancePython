import pandas as pd
ds=pd.read_csv("./panda/Film.csv")
dropen_ds=ds.dropna()
print(dropen_ds.to_string())

