import cv2 as cv
import numpy as np
img = cv.imread("2.jpg")
imgresized=cv.resize(img,(200,200))
cv.imshow("imgresized",imgresized)
cv.waitKey(0)