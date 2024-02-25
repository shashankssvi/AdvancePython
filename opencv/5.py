import cv2 as cv
import numpy as np

blankimg = np.zeros((500,500,3), dtype="uint8")
cv.rectangle(blankimg,(450,450), (10,10), (0,255,255), thickness = 2)
cv.imshow("rectangle",blankimg)
cv.waitKey(0)
