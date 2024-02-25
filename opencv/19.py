import cv2 as cv
import numpy as np

img = cv.imread("1.jpg")
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blurred", blur)

cv.waitKey(0)