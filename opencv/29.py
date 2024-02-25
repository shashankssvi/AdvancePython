import cv2 as cv
import numpy as np
img = np.zeros((500, 500, 3), dtype="uint8")
img1= cv.imread("1.jpg")
cv.putText(img1, "hello", org=(23, 25), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255))

cv.imshow("text", img1)
cv.waitKey(0)
