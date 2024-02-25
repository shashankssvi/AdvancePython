import pandas as pd
dataset={
    'name':['amar','anuj','akash'],
    'roll_no':[2001,2002,2003]
    }
ds=pd.DataFrame(dataset)
# print(ds.loc[0]) #location of row index
# print(ds.loc[0:2]) #location of range of row index
# print(ds.loc[0:2:2]) #location of range and iteration of row index
print(ds.loc[[0,2]]) #location of set of row index

