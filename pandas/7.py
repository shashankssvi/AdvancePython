import pandas as pd
movies=pd.read_csv("./panda/Film.csv")
print(movies)
print(movies.head(10)) #to print the 10 datas form first
print(movies.tail(10)) #to print the 10 datas form last
