import pandas as pd

#this is like a set or JSON type
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
print(ds)
