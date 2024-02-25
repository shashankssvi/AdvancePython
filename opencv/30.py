import cv2 as cv
import numpy as np

list3=[]
list4=[]
row=2
col=3
def func(b,c):
    list1=[]
    list2=[]
    for i in range(b,c,1):
        a=str(i)+".jpg"
        img1 = cv.imread(a)
        im1=cv.resize(img1,(400,400))
        list1.append(im1)
    img=np.hstack(list1)
    list2.append(img)
    cv.imshow("",list2[0])
    return list2[0]

list4=[]
list5=[]
a=1
for i in range(0,row,1):
    list4.append(a)
    list5.append(list4[i]+col+1)
    a=a+col
print(list4,list5)

for i in range(0,row,1):
    lis=func(list4[i],list5[i])
    list3.append(lis)

img2=np.vstack(list3)
list3.append(img2)
cv.imwrite("read.jpg",img2)
cv.waitKey(0)

# lis=func(list4[1],list5[1])
# list3.append(lis)
# lis=func(list4[2],list5[2])
# list3.append(lis)
