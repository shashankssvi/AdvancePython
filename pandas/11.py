import pandas as pd
ds=pd.read_csv("./panda/Film.csv")
ds.fillna('don\'t know',inplace=True)
print(ds.to_string())

