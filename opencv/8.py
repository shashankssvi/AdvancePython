import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
width=blank.shape[1]//2
height=blank.shape[0]//2
cv.circle(blank, (width,height),40,(250,250,25), thickness = -1)

cv.imshow("circle", blank)
cv.waitKey(0)
