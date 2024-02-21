import cv2 as cv
import numpy as np

img = cv.imread("1.jpg")
translated = cv.warpAffine(img, np.float32(([1,0,-10],[0,1,-10])), (img.shape[1],img.shape[0]))
cv.imshow("translated", translated)
cv.waitKey(0)