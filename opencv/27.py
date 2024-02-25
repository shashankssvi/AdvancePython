import cv2 as cv
import numpy as np

img1 = cv.imread("./datasets/png/img1.png")
img2 = cv.imread("./datasets/png/img2.png")
n=np.hstack([img1,img2])
cv.imshow("image",n)
cv.waitKey(0)