# Sobel fiter 엣지검출

import cv2

original = cv2.imread('example.jpg', 1)
dx = cv2.Sobel(original, -1, 1, 0)
dy = cv2.Sobel(original, -1, 0, 1)

cv2.imshow('Original Image', original)
cv2.imshow('sobel X Image', dx)
cv2.imshow('sobel Y Image', dy)
cv2.waitKey(3000)
cv2.destroyAllWindows()