import cv2

original = cv2.imread('example.jpg', 1)
cv2.imshow('Original Image', original)
cv2.waitKey(0)
cv2.destroyAllWindows()