#CONTOUR DETECTION
import cv2 as cv
import numpy as np

img = cv.imread("1.jpg")

canny = cv.Canny(img, 125,175)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresho = cv.threshold(gray, 180, 255, cv.THRESH_BINARY)

cv.imshow("Canny", thresho)
cv.waitKey(0)