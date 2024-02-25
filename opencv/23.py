import cv2 as cv
import numpy as np

img = cv.imread("1.jpg")

canny = cv.Canny(img, 125,175)

cv.imshow("Canny", canny)
cv.waitKey(0)