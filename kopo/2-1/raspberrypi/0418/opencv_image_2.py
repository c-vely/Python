# 2초동안 보이게 하기

import cv2

original = cv2.imread('example.jpg', 1)
cv2.imshow('Original Image', original)
cv2.waitKey(2000)
cv2.destroyAllWindows()