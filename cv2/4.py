import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
blank[20:480,20:480]=255,0,255
cv.imshow("blank",blank)
cv.waitKey(0)
