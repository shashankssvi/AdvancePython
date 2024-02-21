import pandas as pd
dataset={
    'name':{
        '0':'amer',
        '1':'anuj',
        '2':'asus'
        },
    'roll_no':{
        '0':2001,
        '1':2002,
        '2':2003
        }
    }
ds=pd.DataFrame(dataset)
print(ds.loc[0]) #location of row index
print(ds.loc[0:2]) #location of range of row index
print(ds.loc[0:2:2]) #location of range and iteration of row index
print(ds.loc[[0,2]]) #location of set of row index

