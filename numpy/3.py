import numpy as np
#This is a Two dimensional array
n1=np.array([100,200]) #AM,PM at Karolbagh
n2=np.array([300,400]) #AM,PM at RK puram
n3 = np.array([n1, n2]) #AM,PM at Delhi
n4=np.array([[100,200],[300,400]])
sum1=n1[0]+n2[0]
sum2=n1[1]+n2[1]
print(sum1,sum2)
print(n3)
print(n4)

