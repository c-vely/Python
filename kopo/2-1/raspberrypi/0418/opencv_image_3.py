# 다른 사진 삽입

import cv2

original = cv2.imread('whitecat.jpg', 1)
cv2.imshow('Original Image', original)
cv2.waitKey(2000)
cv2.destroyAllWindows()