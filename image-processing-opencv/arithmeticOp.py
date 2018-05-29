import cv2
import numpy as np

img = cv2.imread("input1.jpg")

M = np.ones(img.shape, dtype=np.uint8) * 75
added = cv2.add(img, M);
cv2.imshow("Added Img", added)

#substracted
substract = cv2.subtract(img, M)
cv2.imshow("Substracted", substract)

cv2.waitKey(0)
cv2.destroyAllWindows()