import cv2 as cv
import numpy as np

img = cv.imread("1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("Gray", gray)
cv.waitKey(0)