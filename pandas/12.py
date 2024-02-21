import pandas as pd
ds=pd.read_csv("./panda/Film.csv")
dropen_ds=ds.dropna()
x = ds['Year'].mean()
#y = ds['Year'].median()
#z = ds['Year'].mode()[0]
ds['Year'].fillna(x,inplace=True)
#ds['Year'].fillna(y,inplace=True)
#ds['Year'].fillna(z,inplace=True)
print(ds.to_string())
