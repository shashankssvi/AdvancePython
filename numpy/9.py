import numpy as np
n1 = np.array(['one','two', 'three', 'four', 'five'], dtype='S')
n2 = np.array([1, 2, 3, 4, 5])
n3 = np.array([True,False,False], dtype='b')
n4 = np.array([1.1, 2.2, 3.3, 4.4],dtype='f')
n5 = np.array(['2024-02-24'], dtype='M')
print(n1.dtype)
print(n2.dtype)
print(n3.dtype)
print(n4.dtype)
print(n5.dtype)
'''
datatype:-
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
