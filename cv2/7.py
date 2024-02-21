import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
cv.circle(blank, (40,40),40,(250,250,25), thickness = -1)

cv.imshow("circle", blank)
cv.waitKey(0)
