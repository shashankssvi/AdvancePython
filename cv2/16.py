import cv2 as cv
import numpy as np
img = cv.imread("1.jpg")
flipimg = cv.flip(img, 0)
cv.imshow("flipped", flipimg)

cv.waitKey(0)