import cv2 as cv
import numpy as np

img = cv.imread("1.jpg")
n=np.vstack([img,img])

cv.waitKey(0)