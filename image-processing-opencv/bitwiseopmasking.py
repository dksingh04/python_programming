import cv2
import numpy as np

#create rectangle

squre = np.zeros((300,300), np.uint8)

cv2.rectangle(squre, (50, 50), (250, 250), 255, -2)
cv2.imshow("Square", squre)
cv2.waitKey(0)

elipse = np.zeros((300,300), np.uint8)
cv2.ellipse(elipse, (150, 150), (150,150), 45, 0, 180, 255, -1)
cv2.imshow("Ellipse", elipse)

cv2.waitKey(0)

And = cv2.bitwise_and(squre, elipse)
cv2.imshow("And", And)
Or = cv2.bitwise_or(squre, elipse)
cv2.imshow("OR", Or)
Xor = cv2.bitwise_xor(squre, elipse)
cv2.imshow("XOR", Xor)
notsq = cv2.bitwise_not(squre)
cv2.imshow("Not - Square", notsq)

cv2.waitKey(0)
cv2.destroyAllWindows()
