import pandas as pd
ds=pd.read_csv("./panda/Film.csv")
ds.fillna('WRONG VALUE',inplace=True)
print(ds.to_string())

