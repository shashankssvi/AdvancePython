import cv2 as cv
import numpy as np

img1 = cv.imread("./datasets/png/img1.png")
img2 = cv.imread("./datasets/png/img2.png")
img3 = cv.imread("./datasets/png/img3.png")
n=np.vstack([img1,img2,img3])
cv.imshow("image",n)
cv.waitKey(0)