"""
Example41.그림 출력
"""

import cv2 as cv

#print(cv.__version__)


img = cv.imread("img1.jpg", 1)
cv.namedWindow("image")
cv.imshow("image", img)
cv.waitKey()




