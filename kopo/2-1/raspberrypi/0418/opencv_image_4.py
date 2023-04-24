# 출력 모드 변환

import cv2

original = cv2.imread('whitecat.jpg', 1)
gray = cv2.imread('whitecat.jpg', 0)
unchange = cv2.imread('whitecat.jpg', -1)

cv2.imshow('Original Image', original)
cv2.imshow('Gray Image', gray)
cv2.imshow('Unchanged Image', unchange)
cv2.waitKey(0)
cv2.destroyAllWindows()