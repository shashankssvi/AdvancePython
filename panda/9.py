import pandas as pd
ds1=pd.read_csv("./panda/Film.csv")
print(ds1.to_string()) #line 7,13 are NaN
ds2=ds1.dropna()
print(ds2.to_string())
