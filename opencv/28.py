import cv2 as cv
import numpy as np

img1 = cv.imread("2.jpg")
img2 = cv.imread("3.jpg")

im1=cv.resize(img1,(200,200))
im2=cv.resize(img2,(200,200))

n=np.hstack([im1,im2])
cv.imshow("image",n)
cv.waitKey(0)