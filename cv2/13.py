import cv2 as cv
import numpy as np

img = cv.imread("1.jpg")

rotated = cv.warpAffine(img, cv.getRotationMatrix2D((img.shape[1]//2,img.shape[0]//2), 45, 1.0), (img.shape[1],img.shape[0]))
cv.imshow("Rotated", rotated)

cv.waitKey(0)