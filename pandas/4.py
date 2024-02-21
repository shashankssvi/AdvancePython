import pandas as pd
bikes=['yamaha','hero','ninja']
cars={1:'mahendra',2:'maruthi',3:'supra'}
ds=pd.Series(bikes)
ds=pd.Series(bikes,index=['x','y','z']) #changing indexes

ds1=pd.Series(cars)
ds1=pd.Series(cars,index=[1,2]) #changing indexes
print(ds)
print(ds1)
