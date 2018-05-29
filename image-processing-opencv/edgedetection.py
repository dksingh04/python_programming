import cv2
import numpy as np

img = cv2.imread("input1.jpg")

height, width = img.shape[:2]

#Extract sobel edges
sobel_x = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow("Original", img)
cv2.waitKey(0)

cv2.imshow("Sobel_X", sobel_x)
cv2.waitKey(0)
cv2.imshow("Sobel_Y", sobel_y)
cv2.waitKey(0)

sobel_or = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("Sobel_OR", sobel_or)

cv2.waitKey(0)

#laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow("Laplacian", laplacian)

cv2.waitKey(0)

#Canny
canny = cv2.Canny(img, 20, 80)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
