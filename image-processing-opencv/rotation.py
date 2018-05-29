import cv2
import numpy as np

img = cv2.imread("input1.jpg")
height, width = img.shape[:2]
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 270, 1)
rotatedImg = cv2.warpAffine(img, rotationMatrix, (width, height))

cv2.imshow("Rotated Image by 270 degree", rotatedImg)

rotatedImg = cv2.transpose(img)
cv2.imshow("Rotated Image by Transpose", rotatedImg)

smaller = cv2.pyrDown(img)
largerImg = cv2.pyrUp(img)
largest = cv2.pyrUp(largerImg)
cv2.imshow("Smaller Image", smaller)
cv2.imshow("Larger", largerImg)
cv2.imshow("Largest", largest)

cv2.waitKey()
cv2.destroyAllWindows()
