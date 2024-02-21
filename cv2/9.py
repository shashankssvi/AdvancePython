import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
cv.line(blank,(500,100),(10,10),(0,255,0),thickness = 2)

cv.imshow("line", blank)
cv.waitKey(0)
