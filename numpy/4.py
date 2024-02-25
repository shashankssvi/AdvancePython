import numpy as np
#This is a Three dimensional array
n1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(n1)
kb1=np.array([100,200]) #AM,PM at Karolbagh for day1(monday), dim = 1
rk1=np.array([300,400]) #AM,PM at RK puram for day1(monday), dim = 1
del1 = np.array([kb1,rk1]) #AM,PM at Delhi, dim = 2

kb2=np.array([500,600]) #AM,PM at Karolbagh for day2(tuesday)
rk2=np.array([700,800]) #AM,PM at RK puram for day2(tuesday)
del2 = np.array([kb2,rk2]) #AM,PM at Delhi, dim = 2

kb3=np.array([900,1000]) #AM,PM at Karolbagh for day3(wednesday)
rk3=np.array([1100,1200]) #AM,PM at RK puram for day1(wednesday)
del3 = np.array([kb3,rk3]) #AM,PM at Delhi, dim = 2

delhi=np.array([del1,del2,del3]) #dim = 3
print(delhi)
print(delhi.ndim)
print(del1.ndim)
print(kb1.ndim)
print(delhi.shape)
print(del1.shape)
print(kb1.shape)