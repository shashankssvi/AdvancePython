import pandas as pd
ds=pd.read_csv("./panda/Film.csv")
ds['Year']=pd.to_datetime(ds['Year'])
print(ds.to_string())

