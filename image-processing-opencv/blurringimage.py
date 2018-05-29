import cv2 
import numpy as np

img = cv2.imread("input1.jpg")

cv2.imshow("Original", img)
cv2.waitKey(0)
k_7x7 = np.ones((4,4), dtype=None)/7

blurred = cv2.filter2D(img, -1, k_7x7)

cv2.imshow("Blurred Image", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()