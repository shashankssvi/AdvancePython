import cv2 as cv
import numpy as np
img = cv.imread("2.jpg")
imgresized=cv.resize(img,(500,500))
cv.imshow("imgresized",imgresized)
cv.waitKey(0)