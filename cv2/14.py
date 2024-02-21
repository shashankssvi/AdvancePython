import cv2 as cv
import numpy as np

img = cv.imread("1.jpg")

rotated = cv.warpAffine(img, cv.getRotationMatrix2D((300,200), 180, 0.5), (750,750))
cv.imshow("Rotated", rotated)

cv.waitKey(0)